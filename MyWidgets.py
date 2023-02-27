from PyQt6.QtWidgets import QPushButton, QComboBox, QTextEdit, QLabel, QWidget, QVBoxLayout, QDialog
from PyQt6.QtCore import Qt
import re
from os import path


class FolderComboBox(QComboBox):
    def __init__(self):
        super(FolderComboBox, self).__init__()

        self.setEditable(True)
        self.setDuplicatesEnabled(False)
        self.set_signals()

    def current_folder(self):
        return path.normcase(self.currentText())

    def set_signals(self):
        self.lineEdit().editingFinished.connect(self.on_editing_finished)

    def on_editing_finished(self):
        self.setCurrentText(self.current_folder())

    def set_items(self, items):
        self.clear()

        for i in items:
            self.addItem(i)


class FileNamesContainer(QTextEdit):
    def __init__(self):
        super(FileNamesContainer, self).__init__()

    def get_all_values(self):
        text = self.toPlainText()
        items = list(set(re.findall("\d{4}", text)))
        return items


class InfoPanel(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Info")
        self.num_labels = 0
        self.submit_button = QPushButton("ок")
        self.submit_button.clicked.connect(self.submit)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.submit_button, alignment=Qt.AlignmentFlag.AlignTrailing)

        self.setLayout(self.layout)

    def add_ui(self):
        self.layout.addWidget(self.submit_button, alignment=Qt.AlignmentFlag.AlignTrailing)

    def add_text_in_text_area(self, data):
        text_edit = QTextEdit(data)
        text_edit.setFixedHeight(100)
        self.layout.addWidget(text_edit)

    def add_text_info(self, data):
        log_label = QLabel(data)
        self.layout.addWidget(log_label, alignment=Qt.AlignmentFlag.AlignTop)

    def submit(self, result):
        self.done(result)


class FoldersWidget(QWidget):
    def __init__(self, config):
        super().__init__()

        self.config = config
        self.set_ui()
        self.set_start_values()
        self.set_signals()

    def set_ui(self):
        self.folder_from_label = QLabel("Папка с файлами.")
        self.folder_from_combobox = FolderComboBox()

        self.from_layout = QVBoxLayout()
        self.from_layout.addWidget(self.folder_from_label)
        self.from_layout.addWidget(self.folder_from_combobox)

        self.folder_to_label = QLabel("Папка, в которую будут скопированы\перенесены файлы."
                                      "\nЕсли не существует, будет создана.")
        self.folder_to_combobox = FolderComboBox()

        self.to_layout = QVBoxLayout()
        self.to_layout.addWidget(self.folder_to_label)
        self.to_layout.addWidget(self.folder_to_combobox)

        self.main_layout = QVBoxLayout()

        self.main_layout.addLayout(self.from_layout)
        self.main_layout.addLayout(self.to_layout)

        self.setLayout(self.main_layout)

    def set_start_values(self):
        items_from = self.config.get_last_from_dirs()
        items_to = self.config.get_last_to_dirs()
        self.folder_from_combobox.set_items(items_from)
        self.folder_to_combobox.set_items(items_to)

    def set_signals(self):
        self.folder_from_combobox.lineEdit().editingFinished.connect(self.folder_from_combobox_editing_finished_slot)

    def folder_from(self):
        return self.folder_from_combobox.current_folder()

    def folder_to(self):
        return self.folder_to_combobox.current_folder()

    def folder_from_combobox_editing_finished_slot(self):
        text = self.folder_from_combobox.current_folder()
        if self.folder_to_combobox.currentText() == "":
            self.folder_to_combobox.setCurrentText(text)

    def save_last_selected_values(self):
        self.config.set_last_from_dir(self.folder_from_combobox.current_folder())
        self.config.set_last_to_dir(self.folder_to_combobox.current_folder())
        self.config.save()
