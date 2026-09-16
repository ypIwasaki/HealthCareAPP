"""Application startup: create the Qt application and its first view."""

from PySide6.QtWidgets import QApplication

from healthcare.main_window import MainWindow


def create_application(arguments: list[str]) -> tuple[QApplication, MainWindow]:
    app = QApplication(arguments)
    app.setApplicationName("HealthCareAPP")
    app.setApplicationDisplayName("ヘルスケア")
    window = MainWindow()
    window.show()
    return app, window
