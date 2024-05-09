from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit
from aes_core import aes_encrypt, aes_decrypt


class AESApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        self.plainTextEdit = QTextEdit()
        self.plainTextEdit.setPlaceholderText("Enter plaintext here...")
        layout.addWidget(self.plainTextEdit)

        encryptButton = QPushButton('Encrypt')
        encryptButton.clicked.connect(self.encrypt)
        layout.addWidget(encryptButton)

        self.encryptedTextEdit = QTextEdit()
        self.encryptedTextEdit.setPlaceholderText("Encrypted text will appear here...")
        layout.addWidget(self.encryptedTextEdit)

        decryptButton = QPushButton('Decrypt')
        decryptButton.clicked.connect(self.decrypt)
        layout.addWidget(decryptButton)

        self.decryptedTextEdit = QTextEdit()
        self.decryptedTextEdit.setPlaceholderText("Decrypted text will appear here...")
        layout.addWidget(self.decryptedTextEdit)

        self.setWindowTitle('AES Encryption/Decryption')
        self.setGeometry(300, 300, 350, 300)

    def encrypt(self):
        plaintext = self.plainTextEdit.toPlainText()
        encrypted_text = aes_encrypt(plaintext, 'thisis16charkey!')
        self.encryptedTextEdit.setText(encrypted_text)

    def decrypt(self):
        ciphertext = self.encryptedTextEdit.toPlainText()
        decrypted_text = aes_decrypt(ciphertext, 'thisis16charkey!')
        self.decryptedTextEdit.setText(decrypted_text)
