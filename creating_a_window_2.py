#!/usr/bin/env python3
import sys  # needed for command line args

from PyQt6.QtWidgets import QApplication, QPushButton

# You need (exactly) one instance of QApplication per application. Pass in argv
# to forward command line args to your application.
app = QApplication(sys.argv)

# Create an instance of QPushButton which will serve as the main window for our
# application.
window = QPushButton("Push Me")

# Windows are hidden by default.
window.show()

# Start the event loop.
sys.exit(app.exec())


print("The application has closed.")
