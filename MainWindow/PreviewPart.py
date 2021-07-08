import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication, QVBoxLayout, QLabel, QFrame, QScrollArea, QHBoxLayout)
from Service.SearchFile import findAllFilesWithSpecifiedSuffix


class PreviewPart(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QHBoxLayout()
        self.scroll = QScrollArea()
        grid.addWidget(self.scroll)
        self.setLayout(grid)
        self.fillData()

    def fillData(self):
        contextLayout = QVBoxLayout()
        contextWidget = QWidget()
        contextWidget.setLayout(contextLayout)
        result = findAllFilesWithSpecifiedSuffix('E:\Chrome下载内容', 'jpg')
        for fileName in result:
            contextLayout.addWidget(QLabel(fileName))
        self.scroll.setWidget(contextWidget)
