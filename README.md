# Python Password Generator

A small Python CLI and importable function for generating passwords with
operating-system-backed randomness. This learning project demonstrates input
validation, a reusable core, command-line interfaces, and boundary tests.

## Run locally

Requires Python 3.12+; no third-party dependencies or accounts are needed.

```sh
python password_generator.py
python password_generator.py --length 24 --no-symbols
python -m unittest discover -s tests -v
```

Default: 20 characters drawn from ASCII letters, digits, and punctuation. Use
`--help` for all options. Invalid length or an empty character pool exits with
status 2. The old filename remains a compatibility entry point.

## Design

`generate_password()` uses `secrets.choice`, not the general-purpose `random`
module. CLI parsing is separate, so importing the function does not prompt for
input or print a password. Length is limited to 1–4096 characters to catch
accidental requests; permitting length 1 is not a security recommendation.

Every position is sampled independently from the selected alphabet. Selecting a
category does not guarantee it appears. Tests verify allowed characters and
boundaries, not flaky statistical claims about randomness.

## Security and limitations

Passwords print to your terminal and may be captured by terminal logging or
screen sharing. The tool does not store, encrypt, or manage credentials. Use a
password manager for real credential storage and prefer long, unique passwords.
This is a focused utility rather than a password-strength certification tool.

## Project map and next steps

- `password_generator.py`: generator and CLI.
- `tests/`: unit and CLI tests, also run in GitHub Actions.
- Next: optional passphrases and clipboard behavior with explicit user controls.

Contributions should include a focused change and relevant boundary tests. Run
the test command above before opening a pull request.
