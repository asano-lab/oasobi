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
try:
    logout_button = browser.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div/div/div/div/div/div/div[2]/div/a"
    )
    print(logout_button.get_attribute("innerText"))
    print("既にログインしています")
    logout_button.click()
except WebDriverException:
    user_input = browser.find_element(By.ID, "EntryUserId")
    pswd_input = browser.find_element(By.ID, "EntryPassword")
    with open("private/flets_info.txt", "r") as f:
        user, pswd = f.readlines()
        user_input.send_keys(user)
        pswd_input.send_keys(pswd)
    login_btn = browser.find_element(By.ID, "login_btn")
    login_btn.click()

# q = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
# q = browser.find_element(By.NAME, "q")
# q.send_keys("あいうえお\n")

# r = browser.find_element(By.XPATH, "/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div/a")
# r.click()

# s = browser.find_element(By.XPATH, "/html/body/div/div/div[3]/main/div[2]/div[4]/div[1]/p")
# print(s.get_attribute("innerText"))

time.sleep(10)
print(browser.page_source)

browser.quit()
