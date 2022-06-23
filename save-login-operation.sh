#!/bin/bash
# 初期設定用ファイル
# ID, パスワードが平文で保存されるので注意

url="https://login.shinshu-u.ac.jp"

echo "$url で自動ログインするための操作を記録するスクリプト"
echo "操作を保存するパスを入力"
read line

lynx $url -cmd_log $line

echo "操作の保存が完了しました."
echo "以下を実行すれば自動でログインできます."
echo "lynx \"$url\" -cmd_script $line"
