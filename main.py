from PyQt6.QtWidgets import QApplication
from window_content import MainWindow

app = QApplication([])

window = MainWindow()
window.show()

app.exec()