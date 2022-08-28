#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from urllib.request import urlopen
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium import webdriver
import re
import time


GOOGLE_URL = "https://www.google.com"


def main():

    options = FirefoxOptions()
    options.binary_location = "/usr/bin/firefox"
    options.add_argument("--headless")
    browser = webdriver.Firefox(options=options)

    browser.get(GOOGLE_URL)
    print(browser.page_source)
    browser.quit()


if __name__ == "__main__":
    main()
