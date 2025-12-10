from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout,
                             QPushButton, QWidget, QTextEdit, QLineEdit, QLabel)
from core.parse_phone_number import PhoneNumberParser


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Phone Number Parser")
        self.setGeometry(700, 300, 800, 500)

        self.input = QTextEdit()
        self.code_input = QLineEdit()
        self.button = QPushButton("Get Phone Number Info")
        self.clear_button = QPushButton("Clear")
        self.output = QTextEdit()

        self.build_ui()

    def build_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        vbox = QVBoxLayout()

        code_label = QLabel("Country Code (e.g., TN, GB, FR, US):")
        vbox.addWidget(code_label)
        vbox.addWidget(self.code_input)

        phone_label = QLabel("Phone Number:")
        vbox.addWidget(phone_label)
        vbox.addWidget(self.input)

        vbox.addWidget(self.button)
        vbox.addWidget(self.clear_button)

        output_label = QLabel("Result:")
        vbox.addWidget(output_label)
        vbox.addWidget(self.output)

        self.output.setReadOnly(True)
        self.input.setPlaceholderText("Enter phone number here...")
        self.code_input.setPlaceholderText("TN")

        self.button.setObjectName("button_editor")
        self.clear_button.setObjectName("clear_button")
        self.input.setObjectName("input_editor")
        self.output.setObjectName("output_editor")
        self.code_input.setObjectName("code_editor")

        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: #333;
                margin-top: 10px;
            }
            #code_editor {
                background-color: #ffffff;
                border: 2px solid #ccc;
                border-radius: 6px;
                padding: 8px;
                font-family: Consolas, Monaco, monospace;
                font-size: 18px;
                color: #333;
            }
            #code_editor:focus {
                border: 2px solid #4CAF50;
            }
            #input_editor {
                background-color: #ffffff;
                border: 2px solid #ccc;
                border-radius: 6px;
                padding: 8px;  
                font-family: Consolas, Monaco, monospace;
                font-size: 24px;
                color: #333;
                min-height: 60px;
            }
            #input_editor:focus {
                border: 2px solid #4CAF50;
            }
            #output_editor {
                background-color: #f9f9f9;
                border: 2px solid #bbb;
                border-radius: 6px;
                padding: 12px;
                font-family: Consolas, Monaco, monospace;
                font-size: 20px;
                color: #222;
                min-height: 100px;
            }
            #button_editor { 
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 12px 28px;
                font-weight: bold;
                font-size: 16px;
                letter-spacing: 0.5px;
                margin-top: 10px;
            }
            #button_editor:hover {
                background-color: #45a049;
                cursor: pointer;
            }
            #button_editor:pressed {
                background-color: #3d8b40;
            }
            #clear_button {
                background-color: #f44336;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 26px;
                font-weight: bold;
                font-size: 16px;
                letter-spacing: 0.5px;
            }
            #clear_button:hover {
                background-color: #da190b;
                cursor: pointer;
            }
            #clear_button:pressed {
                background-color: #c41c0b;
            }
        """)

        central_widget.setLayout(vbox)

        self.button.clicked.connect(self.clean)
        self.clear_button.clicked.connect(self.clear_all)

    def clean(self):
        try:
            text = self.input.toPlainText()
            code = self.code_input.text().strip().upper()

            if not code:
                code = "TN"

            if not text or not text.strip():
                self.output.setStyleSheet("""
                    QTextEdit {
                        background-color: #fff3cd;
                        border: 2px solid #ffc107;
                        color: #856404;
                        font-size: 16px;
                        padding: 10px;
                    }
                """)
                self.output.setText("⚠️ Warning: Please enter a phone number")
                return

            if len(text) > 100:
                self.output.setStyleSheet("""
                    QTextEdit {
                        background-color: #fff3cd;
                        border: 2px solid #ffc107;
                        color: #856404;
                        font-size: 16px;
                        padding: 10px;
                    }
                """)
                self.output.setText(
                    "⚠️ Warning: Phone number is too long\n\n"
                    "Maximum length: 100 characters\n"
                    f"Your input: {len(text)} characters"
                )
                return

            if len(code) != 2 or not code.isalpha():
                self.output.setStyleSheet("""
                    QTextEdit {
                        background-color: #fff3cd;
                        border: 2px solid #ffc107;
                        color: #856404;
                        font-size: 16px;
                        padding: 10px;
                    }
                """)
                self.output.setText(
                    f"⚠️ Warning: Invalid country code '{code}'\n\n"
                    "Please use 2-letter country codes:\n"
                    "• TN (Tunisia)\n"
                    "• US (United States)\n"
                    "• GB (United Kingdom)\n"
                    "• FR (France)\n"
                    "etc."
                )
                return

            parser = PhoneNumberParser(text, code)
            result = parser.validate()

            if isinstance(result, tuple):
                phone_number, phone_type = result

                self.output.setStyleSheet("""
                    QTextEdit {
                        background-color: #d4edda;
                        border: 2px solid #28a745;
                        color: #155724;
                        font-size: 18px;
                        padding: 12px;
                        font-weight: bold;
                    }
                """)

                self.output.setText(
                    f"✅ Valid Phone Number\n\n"
                    f"📞 Number: {phone_number}\n"
                    f"📱 Type: {phone_type}\n"
                    f"🌍 Country: {code}"
                )

            else:
                self.output.setStyleSheet("""
                    QTextEdit {
                        background-color: #f8d7da;
                        border: 2px solid #dc3545;
                        color: #721c24;
                        font-size: 16px;
                        padding: 10px;
                    }
                """)

                self.output.setText(f"❌ {result}")

        except Exception as e:
            self.output.setStyleSheet("""
                QTextEdit {
                    background-color: #f8d7da;
                    border: 2px solid #dc3545;
                    color: #721c24;
                    font-size: 16px;
                    padding: 10px;
                }
            """)

            self.output.setText(
                f"❌ Critical Error\n\n"
                f"An unexpected error occurred:\n"
                f"{str(e)}\n\n"
                f"Please report this issue if it persists."
            )

            print(f"[CRITICAL ERROR in GUI] {e}")
            import traceback
            traceback.print_exc()

    def clear_all(self):
        self.input.clear()
        self.code_input.clear()
        self.output.clear()

        self.output.setStyleSheet("""
            QTextEdit {
                background-color: #f9f9f9;
                border: 2px solid #bbb;
                color: #222;
                font-size: 20px;
                padding: 10px;
            }
        """)