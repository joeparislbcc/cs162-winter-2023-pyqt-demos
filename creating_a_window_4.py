#!/usr/bin/env python3
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclassing QMainWindows lets you call __init__ to customize the application's
# main window.
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Hello CS162")
        button = QPushButton("Press Me!")

        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

# Start the event loop.
sys.exit(app.exec())

print("The application has closed.")
