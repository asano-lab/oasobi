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
        col = QColor(0, 0, 0) # 黒

        self.idbtn = QPushButton('Input Dialog', self)
        self.idbtn.move(20, 40)
        self.idbtn.clicked.connect(self.showInputDialog)

        self.cdbtn = QPushButton('Color Dialog', self)
        self.cdbtn.move(20, 80)
        self.cdbtn.clicked.connect(self.showColorDialog)

        self.textEdit = QTextEdit(self)
        # self.setCentralWidget(self.textEdit)

        self.textEdit.move(200, 200)
        self.textEdit.resize(100, 100)
        
        self.statusBar()

        # メニューバーのアイコン設定
        openFile = QAction(QIcon('Images/imoyokan.jpg'), 'Open', self)
        # ショートカット設定
        openFile.setShortcut('Ctrl+O')
        # ステータスバー設定
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showFileDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.frm = QFrame(self)
        print("QWidget { background-color: %s }" % col.name)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(150, 80, 100, 100)

        self.le = QLineEdit(self)
        self.le.move(150, 40)

        self.setGeometry(300, 300, 1000, 600)
        self.setWindowTitle('dialog')
        self.show()

    def showInputDialog(self):
        # 入力ダイアログ
        text, ok = QInputDialog.getText(self, '---Input Dialog---', 'Enter your name:')
        if ok:
            self.le.setText(str(text))
        
    def showColorDialog(self):
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())

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