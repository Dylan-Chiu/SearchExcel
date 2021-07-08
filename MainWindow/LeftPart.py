import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication, QVBoxLayout, QLabel, QFrame)

from MainWindow.StartPart import StartPart
from MainWindow.PreviewPart import PreviewPart


class LeftPart(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QVBoxLayout()
        self.setLayout(grid)
        grid.addWidget(StartPart())
        grid.addWidget(PreviewPart())

