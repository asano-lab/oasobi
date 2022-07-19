#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
# sys.path.append('/home/pi/.local/lib/python3.5/site-packages/')
from selenium import webdriver
from selenium.webdriver.chrome import service as fs

CHROMEDRIVER = "/usr/lib/chromium-browser/chromedriver"
CHROME_SERVICE = fs.Service(executable_path=CHROMEDRIVER)
browser = webdriver.Chrome(service=CHROME_SERVICE)

# browser = webdriver.Chrome()
# browser.get("https://www.google.com/")
