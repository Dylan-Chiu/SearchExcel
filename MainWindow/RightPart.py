import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication, QVBoxLayout, QLabel, QFrame, QTableWidget)

from MainWindow.OutputPart import OutputPart


class RightPart(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QVBoxLayout()
        self.setLayout(grid)
        self.outputPart = OutputPart()
        grid.addWidget(self.outputPart)


