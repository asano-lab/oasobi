#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

CHROMEDRIVER = "/usr/lib/chromium-browser/chromedriver"
CHROME_SERVICE = fs.Service(executable_path=CHROMEDRIVER)

try:
    # GUIが使える場合
    browser = webdriver.Chrome(service=CHROME_SERVICE)
except WebDriverException:
    # GUIが使えない場合
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(service=CHROME_SERVICE, options=options)

# ログインページにアクセス
browser.get("https://wifi.e-flets.jp")
res = 0
try:
    logout_button = browser.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div/div/div/div/div/div/div[2]/div/a"
    )
    # print(logout_button.get_attribute("innerText"))
    # print("既にログインしています")
    # logout_button.click()
    res = -1
except WebDriverException:
    user_input = browser.find_element(By.ID, "EntryUserId")
    pswd_input = browser.find_element(By.ID, "EntryPassword")
    with open("private/flets_info.txt", "r") as f:
        user, pswd = f.readlines()
        user_input.send_keys(user)
        pswd_input.send_keys(pswd)
    login_btn = browser.find_element(By.ID, "login_btn")
    login_btn.click()
    time.sleep(10)
finally:
    browser.quit()
    exit(res)

