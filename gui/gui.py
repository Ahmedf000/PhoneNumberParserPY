from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QTextEdit
from core.parse_phone_number import PhoneNumberParser

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Phone Number Parser")
        self.setGeometry(700, 300, 800, 500)
        self.input = QTextEdit()
        self.button = QPushButton("Get Phone Number Info")
        self.output = QTextEdit()
        self.build_ui()

    def build_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        vbox = QVBoxLayout()

        vbox.addWidget(self.input)
        vbox.addWidget(self.button)
        vbox.addWidget(self.output)
        central_widget.setLayout(vbox)

        self.button.clicked.connect(self.clean)

    def clean(self):
       text = self.input.toPlainText()
       clean = PhoneNumberParser()
       self.output.setText(clean.validate(text))