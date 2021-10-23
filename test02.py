#参考：https://qiita.com/Nobu12/items/acd3caa625be8eebc09c

#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import os
import shutil
import re
import datetime
import csv
import hashlib
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QApplication, QFileDialog,
    QTextEdit, QMessageBox, QLabel
)
from PyQt5.QtCore import Qt

class MyTextEdit(QTextEdit):

    def dropEvent(self, e):
        urls = e.mimeData().urls()
        self.setText(urls[0].toLocalFile())
        # print(self.toPlainText())

class Example(QWidget):
    X1 = 230

    def __init__(self):
        super().__init__()
        self.calcQuestionId()
        self.initUI()

    def initUI(self):
        self.fdbtn = QPushButton("画像ファイルを選択", self)
        self.fdbtn.move(20, 40)
        self.fdbtn.clicked.connect(self.showFileDialog)
        
        self.mkbtn = QPushButton("作成", self)
        self.mkbtn.move(500, 500)
        self.mkbtn.clicked.connect(self.makeQuestionFiles)

        # 画像ファイルのパス入力欄
        self.textEdit = MyTextEdit(self)
        self.textEdit.setGeometry(self.X1, 40, 400, 80)

        # 問題文入力欄
        self.prob_input = MyTextEdit(self)
        self.prob_input.setGeometry(self.X1, 130, 400, 80)

        self.prob_label = QLabel(self)
        self.prob_label.setText("問題文を記入")
        self.prob_label.move(60, 130)

        # ヒント入力欄
        self.hint_input = MyTextEdit(self)
        self.hint_input.setGeometry(self.X1, 220, 400, 80)

        self.hint_label = QLabel(self)
        self.hint_label.setText("ヒントを記入\n(複数ある場合はcsv形式)")
        self.hint_label.move(30, 220)
        self.hint_label.setAlignment(Qt.AlignCenter)
        
        # 正誤判定用文字列入力欄
        self.cand_input = MyTextEdit(self)
        self.cand_input.setGeometry(self.X1, 310, 400, 80)

        self.cand_label = QLabel(self)
        self.cand_label.setText("解答の候補を記入\n(複数ある場合はcsv形式)")
        self.cand_label.move(30, 310)
        self.cand_label.setAlignment(Qt.AlignCenter)

        self.setGeometry(300, 300, 1000, 600)

        self.setWindowTitle("第{:d}問の作成".format(self.q_id))
        self.show()

    # 最新の問題番号を取得し, 次の問題番号を設定
    # ついでに画像ファイルのパスも
    def calcQuestionId(self):
        m_list = [re.search(r'q(\d{3}).md', i) for i in os.listdir(path="./_posts")]
        self.q_id = max(int(m.group(1)) for m in m_list if m) + 1
        self.fname_img = "images/q{:d}.jpg".format(self.q_id)

    def showFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.')

        if fname[0]:
            self.textEdit.setText(fname[0])
            # print(fname[0])
    
    def makeQuestionFiles(self):
        self.now = datetime.datetime.now()
        fnamew = "_posts/" + self.now.strftime('%Y-%m-%d') + "-q{:03d}.md".format(self.q_id)
        self.makeMdFile()
        fnamer = self.textEdit.toPlainText()
        if not os.path.exists(fnamer):
            reply = QMessageBox.question(self, "エラー", "パスが存在しません。", QMessageBox.Ok, QMessageBox.Ok)
            return
        if os.path.isdir(fnamer):
            reply = QMessageBox.question(self, "エラー", "ディレクトリです。", QMessageBox.Ok, QMessageBox.Ok)
            return
        # shutil.copy2(fnamer, "Images")
        print("ある")
    
    # csv形式の文字列をリストに変換
    # 一次元配列で返す
    def csv2list(self, csv_str):
        f = csv.StringIO()
        f.write(csv_str)
        f.seek(0)

        reader = csv.reader(f)
        l = []
        for i in reader:
            l += i

        f.close()
        return l
    
    # ファイルの中身を作成
    def makeMdFile(self):
        moji = "---\nlayout: post\ntitle \"第{:d}回\"\ndate: ".format(self.q_id)
        moji += self.now.strftime('%Y-%m-%d %H:%M:%S +0900\n')
        moji += "categories: question\n---\n\n"
        moji += "![第{:d}回　写真](/kokodoko/{:s})\n\n".format(self.q_id, self.fname_img)
        moji += self.prob_input.toPlainText() + "\n\n"

        hints = self.csv2list(self.hint_input.toPlainText())
        for i, j in enumerate(hints):
            moji += "- [ヒント{:d}](javascript:void(0)){{: .hint}}\n".format(i + 1)
            moji += "   - " + j + "\n"
        
        cands = self.csv2list(self.cand_input.toPlainText())
        if cands:
            moji += "\n<label>解答入力欄 <input type=\"text\" id=\"ans_col\"></label>\n\n"
            moji += "- [判定](javascript:void(0)){{: #judge_but}}\n"
            for i, j in enumerate(cands):
                h_arg = "第{:d}回".format(42) + j
                h = hashlib.sha256(h_arg.encode("utf-8")).hexdigest()
                moji += "   - " + h + "\n"

        print(moji)
        print(cands)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
