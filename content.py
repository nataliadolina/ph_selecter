from PyQt6.QtWidgets import QPushButton, QComboBox, QTextEdit
import re


class SelectFolderButton(QPushButton):
    def __init__(self):
        super(SelectFolderButton, self).__init__()
        self.setText("Select folder")


class FolderComboBox(QComboBox):
    def __init__(self):
        super(FolderComboBox, self).__init__()
        self.setEditable(True)


class FileNamesContainer(QTextEdit):
    def __init__(self):
        super(FileNamesContainer, self).__init__()

    def get_all_values(self):
        text = self.toPlainText()
        items = re.findall("\d{4}", text)
        return items
