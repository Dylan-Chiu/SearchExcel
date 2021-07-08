import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout

from MainWindow.RightPart import RightPart
from MainWindow.LeftPart import LeftPart

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.showMaximized()
    window.show()

    # 创建左右大盒子
    grid = QtWidgets.QHBoxLayout()
    window.setLayout(grid)

    grid.addWidget(LeftPart())
    grid.addWidget(RightPart())

    sys.exit(app.exec_())
