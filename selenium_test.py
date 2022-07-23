#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument("--headless")

CHROMEDRIVER = "/usr/lib/chromium-browser/chromedriver"
CHROME_SERVICE = fs.Service(executable_path=CHROMEDRIVER)
browser = webdriver.Chrome(service=CHROME_SERVICE, options=options)

browser.get("https://www.google.com/")

# q = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
q = browser.find_element(By.NAME, "q")
q.send_keys("あいうえお\n")

r = browser.find_element(By.XPATH, "/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div/a")
r.click()

print(browser.page_source)

time.sleep(1)
browser.quit()
