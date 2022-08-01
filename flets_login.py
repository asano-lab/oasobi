#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import re
import requests
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from urllib.request import urlopen
from urllib.error import URLError


CHROMEDRIVER = "/usr/lib/chromium-browser/chromedriver"
CHROME_SERVICE = fs.Service(executable_path=CHROMEDRIVER)

FLETS_INFO_PATH = "/home/sonoda/.secret/flets_info.txt"
FLETS_LOGIN_URL = "https://wifi.e-flets.jp"

GOOGLE_URL = "https://www.google.com"

# 平文で保存してある
TOKEN_PATH = "/home/sonoda/.secret/line_token01.txt"
LINE_NOTIFY_API = "https://notify-api.line.me/api/notify"


t_delta = datetime.timedelta(hours=9)  # 9時間
JST = datetime.timezone(t_delta, "JST")  # UTCから9時間差の「JST」タイムゾーン

def internet_on():
    """
    インターネットに接続しているかどうか
    """
    res = True
    try:
        urlopen(GOOGLE_URL, timeout=1)
    except URLError:
        res = False
    return res

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
    # インターネットに接続していれば確実にログインしている
    if internet_on():
        notification_message = concat_now(f"successfully connected to '{GOOGLE_URL}'")
        # ログイン済みの通知はうざいのでログだけ残す
        print(notification_message)
        return -1
    try:
        # GUIが使える場合
        browser = webdriver.Chrome(service=CHROME_SERVICE)
    except WebDriverException:
        # GUIが使えない場合
        options = Options()
        options.add_argument("--headless")
        browser = webdriver.Chrome(service=CHROME_SERVICE, options=options)

    # ログインページにアクセス
    try:
        browser.get(FLETS_LOGIN_URL)
    except WebDriverException:
        notification_message = concat_now(f"unable to access '{FLETS_LOGIN_URL}'")
        # 送信不能
        print(notification_message)
        return 1

    res = 0
    try:
        # ログアウトボタンを発見
        logout_button = browser.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div/div/div/div/div/div/div[2]/div/a"
        )
        notification_message = concat_now("you are already logged in")
        # ログイン済みの通知はうざいのでログだけ残す
        print(notification_message)
        res = -1
    except WebDriverException:
        user_input = browser.find_element(By.ID, "EntryUserId")
        pswd_input = browser.find_element(By.ID, "EntryPassword")
        with open(FLETS_INFO_PATH, "r", encoding="UTF-8") as f:
            user, pswd = f.readlines()
            user_input.send_keys(user)
            pswd_input.send_keys(pswd)
        login_btn = browser.find_element(By.ID, "login_btn")
        login_btn.click()
        for i in range(30):
            time.sleep(1)
            if re.search("ユーザ認証完了", browser.page_source) is not None:
                notification_message = concat_now("login was successful")
                send_line_notify(notification_message, line_token)
                break
        else:
            notification_message = concat_now("login may have failed")
            send_line_notify(notification_message, line_token)
    finally:
        browser.quit()
        return res

if __name__ == "__main__":
    main()
