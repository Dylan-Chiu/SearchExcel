import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication, QVBoxLayout, QLabel, QFrame)


class PreviewPart(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QVBoxLayout()
        self.setLayout(grid)
        l1 = QLabel('ttt1', self)
        self.setStyleSheet("background-color: rgb(200,200,200);")
