from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QTextEdit, QLineEdit, QLabel
from core.parse_phone_number import PhoneNumberParser


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Phone Number Parser")
        self.setGeometry(700, 300, 800, 500)
        self.code_input = QLineEdit()
        self.input = QTextEdit()
        self.button = QPushButton("Get Phone Number Info")
        self.clear_button = QPushButton("Clear")
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.build_ui()

    def build_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        vbox = QVBoxLayout()

        code_label = QLabel("Country Code (e.g., TN, GB, FR):")
        vbox.addWidget(code_label)
        vbox.addWidget(self.code_input)

        phone_label = QLabel("Phone Number:")
        vbox.addWidget(phone_label)
        vbox.addWidget(self.input)
        vbox.addWidget(self.button)
        vbox.addWidget(self.clear_button)
        vbox.addWidget(self.output)

        self.button.setObjectName("button_editor")
        self.clear_button.setObjectName("clear_button")
        self.input.setObjectName("input_editor")
        self.output.setObjectName("output_editor")
        self.code_input.setObjectName("code_editor")

        self.setStyleSheet("""
                #code_editor {
                    background-color: #f9f9f9;
                    border: 1px solid #ccc;
                    border-radius: 6px;
                    padding: 8px;
                    font-family: Consolas, monospace;
                    font-size: 20px;
                    color: #333;
                }
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
                #clear_button {
                    color: black;
                    border: 1px solid #555;
                    border-radius: 6px;
                    padding: 10px 26px;
                    font-weight: bold;
                    font-size: 16px;
                    letter-spacing: 0.5px;
                }
                #clear_button:hover {
                    background-color: #ffcccc;
                    border: 1px solid #ff0000;
                    color: black;
                    cursor: pointer;
                }
                """)

        central_widget.setLayout(vbox)

        self.button.clicked.connect(self.clean)
        self.clear_button.clicked.connect(self.clear_all)

    def clean(self):
        text = self.input.toPlainText().strip()
        code = self.code_input.text().strip().upper()

        if not text:
            self.output.setText("✗ Error\n\nPlease enter a phone number")
            return

        if not code:
            self.output.setText("✗ Error\n\nPlease enter a country code (e.g., TN, GB, FR)")
            return

        if len(code) != 2:
            self.output.setText("✗ Error\n\nCountry code must be 2 letters (e.g., TN, GB, FR)")
            return

        try:
            parser = PhoneNumberParser(text, code)
            result = parser.validate()
            self.output.setText(str(result))
        except Exception as e:
            self.output.setText(f"✗ Unexpected Error\n\n{str(e)}")

    def clear_all(self):
        self.input.clear()
        self.code_input.clear()
        self.output.clear()