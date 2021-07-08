import sys
from PyQt5.QtWidgets import *


class test(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        grid = QHBoxLayout()
        contextLayout = QVBoxLayout()
        scroll = QScrollArea()
        contextWidget = QWidget()
        contextWidget.setLayout(contextLayout)
        for x in range(50):
            contextLayout.addWidget(QPushButton(str(x)))

        # scrollarea 作为一个组件，可以设置窗口
        scroll.setWidget(contextWidget)
        grid.addWidget(scroll)
        self.setLayout(grid)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = test()
    sys.exit(app.exec_())
