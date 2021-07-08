import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication, QVBoxLayout, QLabel, QFrame, QInputDialog, QLineEdit,
                             QHBoxLayout)

class InputPart(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QHBoxLayout()
        self.setLayout(grid)
        self.setStyleSheet("background-color: rgb(240,240,240);")

        self.edit = QLineEdit(self)
        label = QLabel('目标文件夹：')
        button = QPushButton("...")
        button.setFixedWidth(40)
        button.clicked.connect(self.button_onClick)
        grid.addWidget(label)
        grid.addWidget(self.edit)
        grid.addWidget(button)

    def getText(self):
        text = self.edit.text()
        return text

    def button_onClick(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "getExistingDirectory", "./")
        self.edit.setText(directory)
