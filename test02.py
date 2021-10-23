#参考：https://qiita.com/Nobu12/items/acd3caa625be8eebc09c

#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import os
import shutil
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QApplication, QFileDialog,
    QTextEdit, QMessageBox
)
from PyQt5.QtGui import (QIcon)

class MyTextEdit(QTextEdit):

    def dropEvent(self, e):
        urls = e.mimeData().urls()
        self.setText(urls[0].toLocalFile())
        # print(self.toPlainText())

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.fdbtn = QPushButton("画像ファイルを選択", self)
        self.fdbtn.move(20, 40)
        self.fdbtn.clicked.connect(self.showFileDialog)
        
        self.mkbtn = QPushButton("作成", self)
        self.mkbtn.move(500, 300)
        self.mkbtn.clicked.connect(self.makeQuestionFiles)

        self.textEdit = MyTextEdit(self)
        self.textEdit.setGeometry(200, 40, 400, 100)

        self.setGeometry(300, 300, 1000, 600)
        self.setWindowTitle("問題追加")
        self.show()

    def showFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.')

        if fname[0]:
            self.textEdit.setText(fname[0])
            # print(fname[0])
    
    def makeQuestionFiles(self):
        fnamer = self.textEdit.toPlainText()
        if not os.path.exists(fnamer):
            reply = QMessageBox.question(self, "エラー", "パスが存在しません。", QMessageBox.Ok, QMessageBox.Ok)
            return
        if os.path.isdir(fnamer):
            reply = QMessageBox.question(self, "エラー", "ディレクトリです。", QMessageBox.Ok, QMessageBox.Ok)
            return
        print("ある")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())