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
print(browser.page_source)

time.sleep(1)
browser.quit()

# browser = webdriver.Chrome()
# browser.get("https://www.google.com/")
