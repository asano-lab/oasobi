#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import datetime
from urllib.request import urlopen
from urllib.error import URLError
import os


PRIVATE_DIR = "./private"


# 平文で保存してある
TOKEN_PATH = os.path.abspath(os.path.join(PRIVATE_DIR, "line_token01.txt"))
LINE_NOTIFY_API = "https://notify-api.line.me/api/notify"


t_delta = datetime.timedelta(hours=9)  # 9時間
JST = datetime.timezone(t_delta, "JST")  # UTCから9時間差の「JST」タイムゾーン


def send_line_notify(notification_message, token):
    """
    LINEに通知する
    標準出力も
    """
    print(notification_message)
    line_notify_token = token
    headers = {"Authorization": f"Bearer {line_notify_token}"}
    data = {"message": f"{notification_message}"}
    requests.post(LINE_NOTIFY_API, headers=headers, data=data)


def concat_now(moji: str) -> str:
    """
    文字列に現在時刻を付加
    """
    return datetime.datetime.now(JST).strftime(f"%a, %d %b %Y %H:%M:%S %z: {moji}")


def main():
    with open(TOKEN_PATH, "r", encoding="UTF-8") as f:
        line_token = f.read().split("\n")[1]
    notification_message = concat_now("active")
    send_line_notify(notification_message, line_token)


if __name__ == "__main__":
    main()
