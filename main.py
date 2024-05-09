import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit
from aes_gui import AESApp


def main():
    app = QApplication(sys.argv)
    ex = AESApp()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
