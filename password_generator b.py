"""Compatibility entry point; use password_generator.py for new commands."""
from password_generator import main

if __name__ == "__main__":
    raise SystemExit(main())
