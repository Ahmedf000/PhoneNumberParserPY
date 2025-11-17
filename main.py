import sys
from PyQt5.QtWidgets import QApplication

def main():
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()