"""Generate passwords using the operating system's secure randomness."""
import argparse
import secrets
import string


def generate_password(length=20, *, letters=True, numbers=True, symbols=True):
    """Sample uniformly from selected pools; no character category is guaranteed."""
    if isinstance(length, bool) or not isinstance(length, int) or not 1 <= length <= 4096:
        raise ValueError("length must be an integer between 1 and 4096")
    pool = (string.ascii_letters if letters else "")
    pool += string.digits if numbers else ""
    pool += string.punctuation if symbols else ""
    if not pool:
        raise ValueError("select at least one character category")
    return "".join(secrets.choice(pool) for _ in range(length))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--length", type=int, default=20)
    parser.add_argument("--no-letters", action="store_true")
    parser.add_argument("--no-numbers", action="store_true")
    parser.add_argument("--no-symbols", action="store_true")
    args = parser.parse_args(argv)
    try:
        password = generate_password(args.length, letters=not args.no_letters,
                                     numbers=not args.no_numbers, symbols=not args.no_symbols)
    except ValueError as error:
        parser.error(str(error))
    print(password)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
