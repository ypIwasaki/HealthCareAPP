"""Standalone GUI scenario; assertions observe visible UI and event-loop exit."""

from pathlib import Path
import sys

from PySide6.QtCore import QTimer, Qt
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QLabel, QPushButton

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from healthcare.app import create_application

app, window = create_application([])
failures: list[str] = []


def close_window() -> None:
    try:
        assert window.isVisible(), "Window is not visible"
        assert window.windowTitle() == "ヘルスケア"
        assert any(label.text() == "体重記録と振り返り" for label in window.findChildren(QLabel))
        if sys.argv[1] == "button":
            buttons = [button for button in window.findChildren(QPushButton) if button.text() == "終了"]
            assert len(buttons) == 1, "Exit button is missing"
            QTest.mouseClick(buttons[0], Qt.MouseButton.LeftButton)
        else:
            window.close()
    except Exception as error:
        failures.append(str(error))
        app.exit(1)


def timeout() -> None:
    failures.append("The event loop did not exit after closing the window")
    app.exit(1)


QTimer.singleShot(100, close_window)
QTimer.singleShot(5000, timeout)
exit_code = app.exec()
assert not failures, failures
assert not window.isVisible(), "Window remains visible after exit"
assert exit_code == 0, exit_code
