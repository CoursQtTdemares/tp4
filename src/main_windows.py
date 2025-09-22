import datetime

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QHBoxLayout, QLineEdit, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget

from src.domain.constants import ICONS_FILE_PATH, MESSAGES_FILE_PATH, PARIS_TZ, STYLES_FILE_PATH
from src.domain.utils import load_messages, load_styles, save_messages


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Chat")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon(str(ICONS_FILE_PATH)))

        self.setStyleSheet(load_styles(STYLES_FILE_PATH))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.line_edit = QLineEdit()  # Zone de saisie du message
        self.push_button = QPushButton("Envoyer le message")  # Bouton pour envoyer le message
        self.push_button.clicked.connect(self._on_click_push_button)

        self.input_message_layout = QHBoxLayout()  # creation zone horizontal
        self.input_message_layout.addWidget(self.line_edit)  # ajout zone de saisie
        self.input_message_layout.addWidget(self.push_button)  # ajout bouton

        self.message_layout = QVBoxLayout()  # creation zone verticale
        self.message_layout.addLayout(self.input_message_layout)  # ajout tout le contenu precedent

        self.text_edit = QTextEdit()  # déclaration zone de texte
        self.text_edit.setReadOnly(True)
        self._load_messages()

        self.message_layout.addWidget(self.text_edit)  # ajout dans le layout vertical

        self.central_widget.setLayout(self.message_layout)

        # Zone de de chat   |    button (envoyer le message)
        # Zone d'affichage des messages

    def _load_messages(self) -> None:
        self.messages = load_messages(MESSAGES_FILE_PATH)
        for message in self.messages:
            self.text_edit.append(message["message"])

    def _save_messages(self) -> None:
        save_messages(MESSAGES_FILE_PATH, self.messages)

    def _on_click_push_button(self) -> None:
        if self.line_edit.text().strip() == "":
            return

        date_now = datetime.datetime.now(PARIS_TZ).strftime("%Y-%m-%d %H:%M:%S")
        new_message = f"{date_now} : {self.line_edit.text().strip()}"
        self.messages.append({"message": new_message})

        self.text_edit.append(new_message)
        self.line_edit.clear()
        self._save_messages()
