#参考：https://qiita.com/Nobu12/items/acd3caa625be8eebc09c

#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QFrame, QColorDialog)
from PyQt5.QtGui import QColor


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0) # 黒

        self.idbtn = QPushButton('Input Dialog', self)
        self.idbtn.move(20, 20)
        self.idbtn.clicked.connect(self.showDialog)

        self.cdbtn = QPushButton('Color Dialog', self)
        self.cdbtn.move(20, 40)
        self.cdbtn.clicked.connect(self.showColorDialog)

        self.frm = QFrame(self)
        print("QWidget { background-color: %s }" % col.name)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('dialog')
        self.show()

    def showDialog(self):
        # 入力ダイアログ
        text, ok = QInputDialog.getText(self, '---Input Dialog---', 'Enter your name:')
        if ok:
            self.le.setText(str(text))
        
    def showColorDialog(self):
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())