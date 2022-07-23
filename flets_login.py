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

browser.get("https://wifi.e-flets.jp")
# logout_button = browser.find_element(By.CLASS_NAME, "btn btn-entry-common btn-block")
logout_button = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/div/div/div/div[2]/div/a")
print(browser.page_source)
print(logout_button.get_attribute("innerText"))

# q = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
# q = browser.find_element(By.NAME, "q")
# q.send_keys("あいうえお\n")

# r = browser.find_element(By.XPATH, "/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div/a")
# r.click()

# s = browser.find_element(By.XPATH, "/html/body/div/div/div[3]/main/div[2]/div[4]/div[1]/p")
# print(s.get_attribute("innerText"))

time.sleep(1)
browser.quit()
