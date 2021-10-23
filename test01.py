#参考：https://qiita.com/Nobu12/items/acd3caa625be8eebc09c

#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QFrame)
from PyQt5.QtGui import QColor


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0) # 黒

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        print("QWidget { background-color: %s }" % col.name)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        # self.setWindowTitle('Input dialog')
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        # 入力ダイアログ
        text, ok = QInputDialog.getText(self, '---Input Dialog---', 'Enter your name:')
        if ok:
            self.le.setText(str(text))
        



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())