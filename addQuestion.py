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
    QGraphicsScene, QWidget, QPushButton, QApplication, QFileDialog,
    QTextEdit, QMessageBox, QLabel, QGraphicsView
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap

# 拡張子の種類
JPEG_EXT = [r'.*.jpg', r'.*.jpeg', r'.*.JPG', r'.*.JPEG']

class MyTextEdit(QTextEdit):

    def __init__(self, obj):
        self.obj = obj # 引数を保存
        super().__init__(obj)

    def dropEvent(self, e):
        urls = e.mimeData().urls()
        path = urls[0].toLocalFile()
        self.setText(path)
        self.obj.setImage(path)
    
    def keyPressEvent(self, e):
        super().keyPressEvent(e)
        self.obj.setImage(self.toPlainText())

class Example(QWidget):
    X1 = 230

    def __init__(self):
        super().__init__()

        # 必要なディレクトリが存在しない場合は終了
        if not os.path.isdir("_posts"):
            print("_posts ディレクトリが存在しません。")
            sys.exit()
        if not os.path.isdir("images"):
            print("images ディレクトリが存在しません。")
            sys.exit()

        self.image = QImage()
        self.pixmap = QPixmap.fromImage(self.image)

        self.calcQuestionId()
        self.initUI()

    def initUI(self):
        self.fdbtn = QPushButton("画像ファイルを選択", self)
        self.fdbtn.move(40, 40)
        self.fdbtn.clicked.connect(self.showFileDialog)

        self.img_label = QLabel(self)
        self.img_label.setText("ファイルのパスを入力\nまたは入力欄にD&D")
        self.img_label.move(40, 80)
        self.img_label.setAlignment(Qt.AlignCenter)
        
        self.mkbtn = QPushButton("作成", self)
        self.mkbtn.move(500, 500)
        self.mkbtn.clicked.connect(self.makeQuestionFiles)

        # 画像ファイルのパス入力欄
        self.textEdit = MyTextEdit(self)
        self.textEdit.setGeometry(self.X1, 40, 400, 80)
        self.textEdit.setText("path/to/image")

        # 問題文入力欄
        self.prob_input = QTextEdit(self)
        self.prob_input.setGeometry(self.X1, 130, 400, 80)
        self.prob_input.setText("施設名を答えてください。")

        self.prob_label = QLabel(self)
        self.prob_label.setText("問題文を記入")
        self.prob_label.move(70, 140)

        # ヒント入力欄
        self.hint_input = QTextEdit(self)
        self.hint_input.setGeometry(self.X1, 220, 400, 80)
        self.hint_input.setText("ヒント1,ヒント2,ヒント3")

        self.hint_label = QLabel(self)
        self.hint_label.setText("ヒントを記入\n(複数ある場合はcsv形式)")
        self.hint_label.move(30, 220)
        self.hint_label.setAlignment(Qt.AlignCenter)
        
        # 正誤判定用文字列入力欄
        self.cand_input = QTextEdit(self)
        self.cand_input.setGeometry(self.X1, 310, 400, 80)
        self.cand_input.setText("解答候補,かいとうこうほ")

        self.cand_label = QLabel(self)
        self.cand_label.setText("解答の候補を記入\n(複数ある場合はcsv形式)")
        self.cand_label.move(30, 310)
        self.cand_label.setAlignment(Qt.AlignCenter)

        # 解答入力欄
        self.ans_input = QTextEdit(self)
        self.ans_input.setGeometry(self.X1, 400, 400, 80)
        self.ans_input.setText("長野県長野市…")

        self.ans_label = QLabel(self)
        self.ans_label.setText("正確な解答を記入\n(空なら「未発表」扱い)")
        self.ans_label.move(40, 400)
        self.ans_label.setAlignment(Qt.AlignCenter)

        # プレビュー
        self.graphics_view = QGraphicsView(self)
        self.graphics_view.setGeometry(700, 40, 300, 300)

        self.graphics_view_label = QLabel(self)
        self.graphics_view_label.setText("プレビュー")
        self.graphics_view_label.move(700, 20)

        self.setGeometry(300, 300, 1200, 600)

        self.setWindowTitle("第{:d}問の作成".format(self.q_id))
        self.show()

    # 最新の問題番号を取得し, 次の問題番号を設定
    # ついでに画像ファイルのパスも
    def calcQuestionId(self):
        m_list = [re.search(r'q(\d{3}).md', i) for i in os.listdir(path="./_posts")]
        self.q_id = max(int(m.group(1)) for m in m_list if m) + 1
        self.fname_img = "images/q{:d}.jpg".format(self.q_id)
    
    def setImage(self, path):
        # 空文字は無視
        if not path:
            return
        self.image = QImage(path)
        self.pixmap = QPixmap.fromImage(self.image)
        self.scene = QGraphicsScene(self)
        self.scene.addPixmap(self.pixmap)
        self.graphics_view.setScene(self.scene)

    # ファイルダイアログの表示
    def showFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.')

        if fname[0]:
            self.textEdit.setText(fname[0])
        
        self.setImage(fname[0])
    
    # ファイル作成
    def makeQuestionFiles(self):
        self.now = datetime.datetime.now()
        fnamer = self.textEdit.toPlainText()

        # ファイルの存在確認
        if not os.path.exists(fnamer):
            QMessageBox.question(self, "エラー", "パスが存在しません。", QMessageBox.Ok, QMessageBox.Ok)
            return
        if os.path.isdir(fnamer):
            QMessageBox.question(self, "エラー", "ディレクトリです。", QMessageBox.Ok, QMessageBox.Ok)
            return
        
        # 画像を出力
        # jpegファイルかどうかチェック
        for i in JPEG_EXT:
            # jpegならそのままコピー
            if re.match(i, fnamer):
                try:
                    shutil.copy2(fnamer, "images/q{:d}.jpg".format(self.q_id))
                except shutil.SameFileError:
                    QMessageBox.question(self, "エラー", "コピー元とコピー先が同じです。", QMessageBox.Ok, QMessageBox.Ok)
                    return
                break
        # jpeg以外なら圧縮して保存
        else:
            # 画像の保存に失敗した場合はエラー (そもそも画像ファイルが選択されてない)
            if not self.pixmap.save("images/q{:d}.jpg".format(self.q_id), "jpg"):
                QMessageBox.question(self, "エラー", "画像ファイル作成失敗", QMessageBox.Ok, QMessageBox.Ok)
                return
        
        fnamew = "_posts/" + self.now.strftime('%Y-%m-%d') + "-q{:03d}.md".format(self.q_id)
        content = self.makeMdFile()
        # print(content)
        
        # markdownの保存
        with open(fnamew, "w", encoding="utf-8") as f:
            f.write(content)
        
        # 作成成功
        QMessageBox.question(self, "作成成功", "アプリを終了します。", QMessageBox.Ok, QMessageBox.Ok)
        sys.exit()
    
    # csv形式の文字列をリストに変換
    # 改行もカンマと同等に見なす
    def csv2list(self, csv_str):
        # 一旦ファイルストリームに変換
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
        # ヘッダの作成
        moji = "---\nlayout: post\ntitle: \"第{:d}回\"\ndate: ".format(self.q_id)
        moji += self.now.strftime('%Y-%m-%d %H:%M:%S +0900\n')
        moji += "categories: question\n---\n\n"
        moji += "![第{:d}回　写真](/kokodoko/{:s})\n\n".format(self.q_id, self.fname_img)

        # 問題文
        moji += self.prob_input.toPlainText() + "\n\n"

        # ヒント
        hints = self.csv2list(self.hint_input.toPlainText())
        for i, j in enumerate(hints):
            moji += "- [ヒント{:d}](javascript:void(0)){{: .hint}}\n".format(i + 1)
            moji += "   - " + j + "\n"
        
        # 正誤判定用ハッシュ (重複排除)
        cands = set(self.csv2list(self.cand_input.toPlainText()))
        if cands:
            moji += "\n1. {: #ans_input}\n"
            for i, j in enumerate(cands):
                h_arg = "第{:d}回".format(self.q_id) + j
                h = hashlib.sha256(h_arg.encode("utf-8")).hexdigest()
                moji += "1. " + h + "\n"
        
        # 古い形式の方がなんだかんだ見やすい
        moji += "\n[答えを表示する](javascript:void(0)){: #ansbtn}\n>"
        
        ans = self.ans_input.toPlainText()
        if not ans:
            ans = "未発表"
        moji += ans + "\n{: #answer}\n"

        return moji

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
