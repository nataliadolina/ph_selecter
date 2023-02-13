from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

from Config import Config
from MyWidgets import FileNamesContainer, InfoPanel, FoldersWidget
from functions import copy_files, read_file_data


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FastPhCopier")
        width = 500
        height = 200
        self.setMinimumSize(width, height)

        self.config = Config()
        self.folders_widget = FoldersWidget(self.config)

        self.file_names_label = QLabel("Название файлов,\nкоторые будут скопированы.")
        self.file_names_container = FileNamesContainer()
        self.file_names_container.setToolTip(read_file_data("files/instruction.txt"))
        self.file_names_layout = QVBoxLayout()
        self.file_names_layout.addWidget(self.file_names_label)
        self.file_names_layout.addWidget(self.file_names_container)

        self.proceed_button = QPushButton("Скопировать")
        self.proceed_button.clicked.connect(self.proceed)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.folders_widget)

        self.layout.addLayout(self.file_names_layout)
        self.layout.addWidget(self.proceed_button)

        container = QWidget()
        container.setLayout(self.layout)

        self.setCentralWidget(container)

    def proceed(self):
        file_names = self.file_names_container.get_all_values()
        folder_from = self.folders_widget.folder_from()
        folder_to = self.folders_widget.folder_to()
        try:
            result, not_copied_files, copied_files = copy_files(dir_from=folder_from, dir_to=folder_to,
                                                                files_to_copy=file_names)
        except Exception as e:
            info_panel = InfoPanel()
            info_panel.add_text_error(
                "Что-то пошло не так. Пожалуйста, проверьте введённые директории, и попробуйте ещё раз."
                "\nДиректории должны различаться и первая директория (папка с файлами) должна"
                "\nсуществовать в проводнике.")
            info_panel.add_ui()
            info_panel.exec()
        else:
            self.folders_widget.save_last_selected_values()
            info_panel = InfoPanel()
            if not result:
                not_copied_string = "; ".join(not_copied_files)
                info_panel.add_text_error(f"Не были найдены файлы с номерами {not_copied_string} в названии.")
            if len(copied_files) == 0:
                info_panel.add_text_error(f"В папку {folder_to} не было скопировано ни одного файла.")
            elif len(copied_files) > 0:
                info_panel.add_text_info(
                    f"Готово! Количество скопированных в папку {folder_to} файлов: {len(copied_files)}.")
            info_panel.add_ui()
            info_panel.exec()
            self.folders_widget.clear()
            self.folders_widget.set_start_values()
