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
        # self.fillData()

    def fillData(self, path):
        contextLayout = QVBoxLayout()
        contextWidget = QWidget()
        contextWidget.setLayout(contextLayout)

        result = findAllFilesWithSpecifiedSuffix(path, 'xls')
        result2 = findAllFilesWithSpecifiedSuffix(path, 'xlsx')
        result.extend(result2)

        for fileName in result:
            contextLayout.addWidget(QLabel(fileName.replace("/", '\\')))
        self.scroll.setWidget(contextWidget)
