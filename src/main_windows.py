from PyQt6.QtWidgets import QHBoxLayout, QLineEdit, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.line_edit = QLineEdit()  # Zone de saisie du message
        self.push_button = QPushButton("Envoyer le message")  # Bouton pour envoyer le message

        self.input_message_layout = QHBoxLayout()  # creation zone horizontal
        self.input_message_layout.addWidget(self.line_edit)  # ajout zone de saisie
        self.input_message_layout.addWidget(self.push_button)  # ajout bouton

        self.message_layout = QVBoxLayout()  # creation zone verticale
        self.message_layout.addLayout(self.input_message_layout)  # ajout tout le contenu precedent

        self.text_edit = QTextEdit()  # déclaration zone de texte
        self.message_layout.addWidget(self.text_edit)  # ajout dans le layout vertical

        self.central_widget.setLayout(self.message_layout)

        # Zone de de chat   |    button (envoyer le message)
        # Zone d'affichage des messages
