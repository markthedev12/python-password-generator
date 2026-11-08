import contextlib
import io
import string
import unittest
from password_generator import generate_password, main

class GeneratorTests(unittest.TestCase):
    def test_length_and_alphabet(self):
        for length in (1, 20, 4096):
            value = generate_password(length, letters=False, symbols=False)
            self.assertEqual(len(value), length)
            self.assertTrue(set(value) <= set(string.digits))

    def test_invalid_lengths(self):
        for length in (0, -1, 4097, True, 1.5, "20"):
            with self.subTest(length=length), self.assertRaises(ValueError):
                generate_password(length)

    def test_empty_pool(self):
        with self.assertRaises(ValueError):
            generate_password(20, letters=False, numbers=False, symbols=False)

    def test_cli(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(main(["--length", "16", "--no-symbols"]), 0)
        self.assertEqual(len(output.getvalue().strip()), 16)

    def test_cli_rejects_invalid_input(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
            main(["--length", "0"])
        self.assertEqual(error.exception.code, 2)
