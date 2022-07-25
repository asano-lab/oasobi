#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

CHROMEDRIVER = "/usr/lib/chromium-browser/chromedriver"
CHROME_SERVICE = fs.Service(executable_path=CHROMEDRIVER)
FLETS_INFO_PATH = "/home/sonoda/.secret/flets_info.txt"
FLETS_LOGIN_URL = "https://wifi.e-flets.jp"

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
    print(f"unable to access '{FLETS_LOGIN_URL}'")
    exit(1)

res = 0
try:
    # ログアウトボタンを発見
    logout_button = browser.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div/div/div/div/div/div/div[2]/div/a"
    )
    print("you are already logged in")
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
            print("login was successful")
            break
    else:
        print("login may have failed")
finally:
    browser.quit()
    exit(res)
