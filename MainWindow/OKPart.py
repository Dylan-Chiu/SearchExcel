import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication, QVBoxLayout, QLabel, QFrame, QInputDialog, QLineEdit,
                             QHBoxLayout)

from MainWindow.PreviewPart import PreviewPart
from MainWindow.OutputPart import OutputPart

class OKPart(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QHBoxLayout()
        self.setLayout(grid)
        self.setStyleSheet("background-color: rgb(240,240,240);")
        self.edit = QLineEdit()
        self.OKButton = QPushButton("开始搜索")

        grid.addWidget(QLabel("关键字："))
        grid.addWidget(self.edit)
        grid.addWidget(self.OKButton)

