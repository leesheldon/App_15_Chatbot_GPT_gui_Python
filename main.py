from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QTextEdit, QLineEdit, QPushButton
import sys


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chatbot GPT App")
        self.setMinimumSize(700, 500)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 30)

        # Add the button
        self.send_button = QPushButton("Send", self)
        self.send_button.setGeometry(500, 340, 100, 30)

        self.show()


class Chatbot:
    pass


app = QApplication(sys.argv)
chatbot_app = ChatbotWindow()
sys.exit(app.exec())















































