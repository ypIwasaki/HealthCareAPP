"""Shared entry point for source execution and the Windows executable."""

import sys

from healthcare.app import create_application


def main() -> int:
    app, window = create_application(sys.argv)
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
