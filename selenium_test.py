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

browser.get("https://www.google.com/")

q = browser.find_element(By.NAME, "q")
q.send_keys("あいうえお\n")

# クラス名は変わる場合あり
element_list = browser.find_elements(By.CLASS_NAME, "LC20lb.MBeuO.DKV0Md")
for el in element_list:
    if "Wikipedia" in el.get_attribute("innerText"):
        el.click()
        break

# xpathは変わる場合あり
s = browser.find_element(
    By.XPATH, "/html/body/div[1]/div/div[4]/main/div[2]/div[3]/div[1]/p")

print(s.get_attribute("innerText"))

time.sleep(1)
browser.quit()
