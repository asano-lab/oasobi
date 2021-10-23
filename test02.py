#参考：https://qiita.com/Nobu12/items/acd3caa625be8eebc09c

#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QApplication, QFileDialog,
    QTextEdit
)
from PyQt5.QtGui import (QIcon)

class MyTextEdit(QTextEdit):

    def dropEvent(self, e):
        urls = e.mimeData().urls()
        self.setText(urls[0].toLocalFile())

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.idbtn = QPushButton("画像ファイルを選択", self)
        self.idbtn.move(20, 40)
        self.idbtn.clicked.connect(self.showFileDialog)

        self.textEdit = MyTextEdit(self)
        self.textEdit.setGeometry(200, 40, 400, 100)

        self.setGeometry(300, 300, 1000, 600)
        self.setWindowTitle("問題追加")
        self.show()

    def showFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.')

        if fname[0]:
            self.textEdit.setText(fname[0])
            print(fname[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())