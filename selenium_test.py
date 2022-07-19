#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
# sys.path.append('/home/pi/.local/lib/python3.5/site-packages/')
from selenium import webdriver
from selenium.webdriver.chrome import service as fs

CHROMEDRIVER = "/usr/lib/chromium-browser/chromedriver"
CHROME_SERVICE = fs.Service(executable_path=CHROMEDRIVER)
browser = webdriver.Chrome(service=CHROME_SERVICE)

time.sleep(1)
browser.quit()

# browser = webdriver.Chrome()
# browser.get("https://www.google.com/")
