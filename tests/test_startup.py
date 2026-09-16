"""Exercise the startup boundary in a separate Qt process for each close method."""

from pathlib import Path
import subprocess
import sys
import unittest


class StartupTest(unittest.TestCase):
    def test_japanese_window_opens_and_exits(self) -> None:
        for close_method in ("button", "window"):
            with self.subTest(close_method=close_method):
                result = subprocess.run(
                    [sys.executable, str(Path(__file__).with_name("startup_scenario.py")), close_method],
                    cwd=Path(__file__).resolve().parents[1],
                    capture_output=True,
                    text=True,
                    timeout=30,
                )
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
