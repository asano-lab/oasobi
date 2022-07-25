#!/usr/bin/env python3

import requests

# 平文で保存してある
TOKEN_PATH = "/home/sonoda/.secret/line_token01.txt"

LINE_NOTIFY_API = "https://notify-api.line.me/api/notify"


def main():
    with open(TOKEN_PATH, "r", encoding="UTF-8") as f:
        line_token = f.read().split("\n")[1]
    print(line_token)
    # send_line_notify("てすとてすと", line_token)


def send_line_notify(notification_message, token):
    """
    LINEに通知する
    """
    line_notify_token = token
    headers = {"Authorization": f"Bearer {line_notify_token}"}
    data = {"message": f"message: {notification_message}"}
    requests.post(LINE_NOTIFY_API, headers=headers, data=data)


if __name__ == "__main__":
    main()
