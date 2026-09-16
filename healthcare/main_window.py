"""The minimal Japanese view; data entry is added in later issues."""

from PySide6.QtWidgets import QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("ヘルスケア")
        self.resize(480, 240)

        content = QWidget(self)
        layout = QVBoxLayout(content)
        layout.addWidget(QLabel("体重記録と振り返り"))
        message = QLabel("アプリを起動しました。\n体重記録の入力機能は、今後追加します。")
        message.setWordWrap(True)
        layout.addWidget(message)
        layout.addStretch()
        close_button = QPushButton("終了")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)
        self.setCentralWidget(content)
