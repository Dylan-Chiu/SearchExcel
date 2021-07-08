import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout

from MainWindow.RightPart import RightPart
from MainWindow.LeftPart import LeftPart

if __name__ == '__main__':
    global previewPartPointer

    app = QApplication(sys.argv)
    window = QWidget()
    window.showMaximized()
    window.show()
    window.setWindowTitle("Excel内容搜索    Author: Q")
    # 创建左右大盒子
    grid = QtWidgets.QHBoxLayout()
    window.setLayout(grid)

    leftPart = LeftPart()
    rightPart = RightPart()

    #绑定单击事件（开始搜索）
    def OKButton_click(self):
        path = leftPart.startPart.inputPart.getText()
        key = leftPart.startPart.OKPart.edit.text()
        leftPart.previewPart.fillData(path)
        rightPart.outputPart.fillData(path,key)
    leftPart.startPart.OKPart.OKButton.clicked.connect(OKButton_click)


    grid.addWidget(leftPart)
    grid.addWidget(rightPart)

    sys.exit(app.exec_())

