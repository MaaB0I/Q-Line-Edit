import PyQt6
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QSlider, QHBoxLayout, QTextBrowser, QGridLayout, QLabel, QLineEdit, QTextBrowser
from PyQt6.QtCore import pyqtSlot, Qt, QSize


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        layout = QGridLayout(self)

        self.decimal = QLineEdit(parent)
        self.hexa = QLineEdit(parent)
        self.bin = QLineEdit(parent)
        self.char = QLineEdit(parent)
        self.upper_char = QLineEdit(parent)

        self.decimal.setInputMask("9000")
        self.hexa.setInputMask("HHHHHH")
        self.bin.setInputMask("BBBbbbbbbb")
        # fuer Aa* ist eine input mask nicht moeglich
        self.upper_char.setInputMask(">A")

        self.decimal.textEdited.connect(self.text_edited)
        self.decimal.editingFinished.connect(self.text_finished)
        self.decimal.inputRejected.connect(self.text_rejected)

        layout.addWidget(QLabel("Dezimal:"), 1, 1, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QLabel("Hexadezimal:"), 2, 1, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QLabel("Binär:"), 3, 1, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QLabel("Buchstaben:"), 4, 1, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QLabel("Großbuchstaben:"), 5, 1, Qt.AlignmentFlag.AlignRight)

        layout.addWidget(self.decimal, 1, 2)
        layout.addWidget(self.hexa, 2, 2)
        layout.addWidget(self.bin, 3, 2)
        layout.addWidget(self.char, 4, 2)
        layout.addWidget(self.upper_char, 5, 2)

        self.text_browser = QTextBrowser()
        layout.addWidget(self.text_browser, 6, 1, 3, 2)

        self.setLayout(layout)

    @pyqtSlot()
    def text_rejected(self):
        self.text_browser.append("\t(input rejected)")

    @pyqtSlot()
    def text_finished(self):
        self.text_browser.append("\t(editing finished)")
        text = self.decimal.text()
        self.text_browser.append(text + "\t(finished text)")

    @pyqtSlot(str)
    def text_edited(self, text_from_signal: str):
        self.text_browser.append(text_from_signal + "\t(edited event)")
