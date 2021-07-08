import os
import sys
from functools import partial
from re import split

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication, QVBoxLayout, QLabel, QFrame, QTableWidget, QHeaderView,
                             QTableWidgetItem)
from Service.SearchFile import findAllCellInAllExcel


class OutputPart(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QVBoxLayout()
        self.setLayout(grid)
        self.tableWidget = QTableWidget()

        headList = ['文件路径', '文件名', '单元格内容', '具体位置', '文件']
        self.tableWidget.setRowCount(0)  # 行数
        self.tableWidget.setColumnCount(len(headList))  # 列数

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        self.tableWidget.setHorizontalHeaderLabels(headList)
        grid.addWidget(self.tableWidget)
        self.setStyleSheet("background-color: rgb(255,255,255);")

    def fillData(self, path, key):
        data = findAllCellInAllExcel(path, key)
        self.tableWidget.setRowCount(len(data))  # 行数
        for i in range(len(data)):  # 注意上面列表中数字加单引号，否则下面不显示(或者下面str方法转化一下即可)
            cell = data[i]
            list = []
            list.append(str(cell.fileName))
            list.append(os.path.split(cell.fileName)[1])
            list.append(str(cell.context))
            list.append("第{0}张sheet，第{1}行，第{2}列".format(cell.sheetId + 1, cell.rowId + 1, cell.colId + 1))
            for j in range(len(list)):
                item = QTableWidgetItem(str(list[j]))
                item.setFont(QFont('宋体', 10))
                self.tableWidget.setItem(i, j, item)
                openFileButton = QPushButton('打开文件')

                def openFile(path):
                    os.popen(path)

                openFileButton.clicked.connect(partial(openFile, list[0]))
                self.tableWidget.setCellWidget(i, 4, openFileButton)
