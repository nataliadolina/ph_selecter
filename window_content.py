from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout

from Config import Config
from MyWidgets import FileNamesContainer, InfoPanel, FoldersWidget
from functions import copy_files, move_files, read_file_data


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.wait_message = "Подождите..."
        self.copy_button_message = "Скопировать"
        self.move_button_message = "Переместить"
        self.create_ui()
        self.create_messages()

    def create_ui(self):
        self.setWindowTitle("FastPhCopier")
        width = 400
        height = 170
        self.setMinimumSize(width, height)

        self.config = Config()
        self.folders_widget = FoldersWidget(self.config)

        self.file_names_label = QLabel("Название файлов,\nкоторые будут скопированы.")
        self.file_names_container = FileNamesContainer()
        self.file_names_container.setToolTip(read_file_data("files/instruction.txt"))

        self.file_names_layout = QVBoxLayout()
        self.file_names_layout.addWidget(self.file_names_label)
        self.file_names_layout.addWidget(self.file_names_container)

        self.buttons_layout = QHBoxLayout()

        self.copy_button = QPushButton(self.copy_button_message)
        self.copy_button.clicked.connect(self.proceed_copy_button)

        self.move_button = QPushButton(self.move_button_message)
        self.move_button.clicked.connect(self.proceed_move_button)

        self.buttons_layout.addWidget(self.copy_button)
        self.buttons_layout.addWidget(self.move_button)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.folders_widget)

        self.bottom_layout = QVBoxLayout()
        self.bottom_layout.setContentsMargins(10, 0, 10, 10)

        self.bottom_layout.addLayout(self.file_names_layout)
        self.bottom_layout.addLayout(self.buttons_layout)

        self.layout.addLayout(self.bottom_layout)

        container = QWidget()
        container.setLayout(self.layout)

        self.setCentralWidget(container)

    def create_messages(self):
        self.move_messages = {"nothing operated": "В папку {} не было перенесено ни одного файла.",
                              "operated": "Готово! В папку {} были перенесены следующие файлы:",
                              "not operated": "Следующие файлы были пропущены,"
                                              " так как уже находятся в папке назначения:",
                              "num operated": "Количество перенесённых файлов - {}."}
        self.copy_messages = {"nothing operated": "В папку {} не было скопировано ни одного файла.",
                              "operated": "Готово! В папку {} были скопированы следующие файлы:",
                              "not operated": "Следующие файлы были пропущены,"
                                              " так как уже находятся в папке назначения:",
                              "num operated": "Количество скопированных файлов - {}."}

    def proceed_copy_button(self):
        self.copy_button.setText(self.wait_message)
        self.do_operation(copy_files, self.copy_messages, self.copy_button_callback)

    def proceed_move_button(self):
        self.move_button.setText(self.wait_message)
        self.do_operation(move_files, self.move_messages, self.move_button_callback)

    def copy_button_callback(self):
        self.copy_button.setText(self.copy_button_message)

    def move_button_callback(self):
        self.move_button.setText(self.move_button_message)

    def do_operation(self, operation, messages, callback):
        file_names = self.file_names_container.get_all_values()
        folder_from = self.folders_widget.folder_from()
        folder_to = self.folders_widget.folder_to()
        try:
            operated, not_operated, not_found = operation(folder_from, folder_to, file_names)
        except Exception as e:
            callback()
            info_panel = InfoPanel()
            info_panel.add_text_info(
                "Что-то пошло не так. Пожалуйста, проверьте введённые директории, и попробуйте ещё раз."
                "\nДиректории должны различаться и первая директория (папка с файлами) должна"
                "\nсуществовать в проводнике.")
            info_panel.add_ui()
            info_panel.exec()
        else:
            callback()
            info_panel = InfoPanel()
            if not_found:
                not_copied_string = "; ".join(not_found)
                info_panel.add_text_info(f"Не были найдены файлы с следующими номерами в названии:")
                info_panel.add_text_in_text_area(not_copied_string)
            if len(not_operated) > 0:
                info_panel.add_text_info(messages["not operated"])
                info_panel.add_text_in_text_area("; ".join(not_operated))
            if len(operated) == 0:
                info_panel.add_text_info(messages["nothing operated"].format(folder_to))
            elif len(operated) > 0:
                copied_files_string = "; ".join(operated)
                info_panel.add_text_info(messages["operated"].format(folder_to))
                info_panel.add_text_in_text_area(copied_files_string)
                info_panel.add_text_info(messages["num operated"].format(len(operated)))
            info_panel.add_ui()
            info_panel.exec()
            self.folders_widget.save_last_selected_values()
            self.folders_widget.set_start_values()
