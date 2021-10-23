#参考：https://qiita.com/Nobu12/items/acd3caa625be8eebc09c

#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLineEdit, QInputDialog,
    QApplication, QFrame, QColorDialog, QFileDialog,
    QTextEdit, QAction, QMainWindow
)
from PyQt5.QtGui import (QColor, QIcon)


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.idbtn = QPushButton('File Dialog', self)
        self.idbtn.move(20, 40)
        self.idbtn.clicked.connect(self.showFileDialog)

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(100, 100, 100, 100)

        self.setGeometry(300, 300, 1000, 600)
        self.setWindowTitle("問題追加")
        self.show()

    def showFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.')

        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())