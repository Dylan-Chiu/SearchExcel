import sys
from MainWindow.InputPart import InputPart
from MainWindow.OKPart import OKPart
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication, QVBoxLayout, QLabel, QFrame, QInputDialog, QLineEdit,
                             QHBoxLayout)


class StartPart(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QVBoxLayout()
        self.setLayout(grid)
        self.setStyleSheet("background-color: rgb(230,230,230);")
        self.OKPart = OKPart()
        self.inputPart = InputPart()
        grid.addWidget(self.inputPart)
        grid.addWidget(self.OKPart)
