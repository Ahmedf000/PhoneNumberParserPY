from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QTextEdit
from core.parse_phone_number import PhoneNumberParser
from core.parse_raw import CleanParser

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

        self.button.setObjectName("button_editor")
        self.input.setObjectName("input_editor")
        self.output.setObjectName("output_editor")

        self.setStyleSheet("""
                #input_editor {
                    background-color: #f9f9f9;
                    border: 1px solid #ccc;
                    border-radius: 6px;
                    padding: 8px;  
                    font-family: Consolas, monospace;
                    font-size: 30px;
                    color: #333;      
                }
                #output_editor {
                    background-color: #f0f0f0;
                    border: 1px solid #bbb;
                    border-radius: 6px;
                    padding: 8px;
                    font-family: Consolas, monospace;
                    font-size: 30px;
                    color: #222;
                }
                #button_editor { 
                    color: black;
                    border: 1px solid #555;
                    border-radius: 6px;
                    padding: 10px 26px;
                    font-weight: bold;
                    font-size: 16px;
                    letter-spacing: 0.5px;
                }
                #button_editor:hover {
                    background-color: white;
                    border: 1px solid #777;
                    color: black;
                    cursor: pointer;
                }
                """)


        central_widget.setLayout(vbox)

        self.button.clicked.connect(self.clean)

    def clean(self):
       text = self.input.toPlainText()
       code = "TN"
       clean = PhoneNumberParser(text, code)
       result = clean.validate()
       self.output.appendPlainText(result)