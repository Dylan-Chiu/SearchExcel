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
        self.setStyleSheet("background-color: rgb(200,200,200);")
        preButton = QPushButton("准备搜索")
        OKButton = QPushButton("开始搜索")
        OKButton.clicked.connect(self.OKButton_click())

        grid.addWidget(preButton)
        grid.addWidget(OKButton)

    def OKButton_click(self):
        PreviewPart.fillData()

