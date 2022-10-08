#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="家のWi-Fiにログインするためのプログラム")

    parser.add_argument("-b", "--browser", help="ブラウザ", default="Firefox")
    parser.add_argument("--headless",
                        help="ヘッドレスモード", action="store_true")
    parser.add_argument("--debug",
                        help="デバッグモード (めっちゃ通知する)", action="store_true")
    args = parser.parse_args()

    from urllib.error import URLError
    from urllib.request import urlopen
    from selenium.common.exceptions import WebDriverException
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    from selenium.webdriver.chrome import service as fs
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    import datetime
    import requests
    import re
    import time
    import os
else:
    exit()


PRIVATE_DIR = "./private"

DOWNLOAD_URL = "https://www.minecraft.net/en-us/download/server/bedrock"

GOOGLE_URL = "https://www.google.com"

# 平文で保存してある
TOKEN_PATH = os.path.abspath(os.path.join(PRIVATE_DIR, "line_token_ssb.txt"))
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
    headless = args.headless

    # with open(TOKEN_PATH, "r", encoding="UTF-8") as f:
    #     line_token = f.read()

    # GUIが使える場合
    if not args.headless:
        try:
            if args.browser == "Firefox":
                options = FirefoxOptions()
                options.binary_location = "/usr/bin/firefox"
                browser = webdriver.Firefox(options=options)
            else:
                chrome_service = fs.Service(
                    executable_path="/usr/lib/chromium-browser/chromedriver")
                browser = webdriver.Chrome(service=chrome_service)
        except WebDriverException:
            headless = True

    # GUIを使わない, 使えない場合
    if headless:
        if args.browser == "Firefox":
            options = FirefoxOptions()
            options.binary_location = "/usr/bin/firefox"
            options.add_argument("--headless")
            browser = webdriver.Firefox(options=options)
        else:
            chrome_service = fs.Service(
                executable_path="/usr/lib/chromium-browser/chromedriver")
            options = ChromeOptions()
            options.add_argument("--headless")
            browser = webdriver.Chrome(
                service=chrome_service, options=options)

    # ダウンロードページにアクセス
    try:
        browser.get(DOWNLOAD_URL)
    except WebDriverException:
        notification_message = concat_now(
            f"unable to access '{DOWNLOAD_URL}'")
        # 送信不能
        print(notification_message)
        return 1

    res = 0
    try:
        # ダウンロードボタンを発見
        download_button = browser.find_element(
            By.XPATH,
            "/html/body/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[3]/div/a"
        )
        print(download_button.get_attribute("href"))
    except WebDriverException:
        print("ボタンがない")
    finally:
        browser.quit()
        return res


if __name__ == "__main__":
    main()
