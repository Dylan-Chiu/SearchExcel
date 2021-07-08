import sys
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
        self.setStyleSheet("background-color: rgb(200,200,200);")


        edit = QLineEdit(self)
        label = QLabel('目标文件夹：')
        button = QPushButton("...")
        button.setFixedWidth(40)

        grid.addWidget(label)
        grid.addWidget(edit)
        grid.addWidget(button)
