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
        contextLayout = QVBoxLayout()
        scroll = QScrollArea()
        contextWidget = QWidget()
        contextWidget.setLayout(contextLayout)
        # for x in range(50):
        #     contextLayout.addWidget(QPushButton(str(x)))

        result = findAllFilesWithSpecifiedSuffix('E:\Chrome下载内容', 'jpg')
        for fileName in result:
            contextLayout.addWidget(QLabel(fileName))

        # scrollarea 作为一个组件，可以设置窗口
        scroll.setWidget(contextWidget)
        grid.addWidget(scroll)
        self.setLayout(grid)




