import sys
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
        tableWidget = QTableWidget()

        data = findAllCellInAllExcel('E:\综测计算\大一\计信院综测细则', '汤闽')
        tableWidget.setRowCount(len(data))  # 行数
        tableWidget.setColumnCount(5)  # 列数

        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        tableWidget.setHorizontalHeaderLabels(['文件路径', '单元格内容', 'sheet', 'row', 'col'])

        for i in range(len(data)):  # 注意上面列表中数字加单引号，否则下面不显示(或者下面str方法转化一下即可)
            item = data[i]
            list = item.getList()
            for j in range(len(list)):
                item = QTableWidgetItem(str(list[j]))
                tableWidget.setItem(i, j, item)

        grid.addWidget(tableWidget)

        self.setStyleSheet("background-color: rgb(200,200,200);")
