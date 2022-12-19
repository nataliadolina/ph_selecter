from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget

from content import SelectFolderButton, FolderComboBox, FileNamesContainer
from algorithm import copy_files


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        width = 500
        height = 200
        self.setMinimumSize(width, height)

        self.label = QLabel()
        self.select_folder_button = SelectFolderButton()

        self.folder_from_label = QLabel("Папка с файлами.")
        self.folder_from_combobox = FolderComboBox()
        self.from_layout = QHBoxLayout()
        self.from_layout.addWidget(self.folder_from_label)
        self.from_layout.addWidget(self.folder_from_combobox)

        self.folder_to_label = QLabel("Папка,\nкуда будут скопированы файлы.")
        self.folder_to_combobox = FolderComboBox()
        self.to_layout = QHBoxLayout()
        self.to_layout.addWidget(self.folder_to_label)
        self.to_layout.addWidget(self.folder_to_combobox)

        self.file_names_label = QLabel("Название файлов,\nкоторые будут скопированы.")
        self.file_names_container = FileNamesContainer()
        self.file_names_layout = QHBoxLayout()
        self.file_names_layout.addWidget(self.file_names_label)
        self.file_names_layout.addWidget(self.file_names_container)

        self.proceed_button = QPushButton("Скопировать")
        self.proceed_button.clicked.connect(self.proceed)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.from_layout)
        self.layout.addLayout(self.to_layout)
        self.layout.addLayout(self.file_names_layout)
        self.layout.addWidget(self.proceed_button)

        container = QWidget()
        container.setLayout(self.layout)

        self.setCentralWidget(container)

    def proceed(self):
        file_names = self.file_names_container.get_all_values()
        folder_from = self.folder_from_combobox.currentText()
        folder_to = self.folder_to_combobox.currentText()
        copy_files(dir_from=folder_from, dir_to=folder_to, files_to_copy=file_names)
