from PyQt6.QtWidgets import QApplication, QMainWindow
from window_content import MainWindow

import sys

app = QApplication([])

window = MainWindow()
window.show()

app.exec()