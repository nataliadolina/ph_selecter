from PyQt6.QtWidgets import QApplication, QMainWindow
from window_content import MainWindow

app = QApplication([])

window = MainWindow()
window.show()

app.exec()