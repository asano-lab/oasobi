# 実行環境
`uname -a`
```:出力
Linux ホスト名 5.15.32-v8+ #1538 SMP PREEMPT Thu Mar 31 19:40:39 BST 2022 aarch64 GNU/Linux
```
`python3 -V`
```:出力
Python 3.9.2
```
`chromium-browser --version`
```:出力
Chromium 101.0.4951.57 Built on Debian , running on Debian 11
```

# seleniumのインストール
```bash
pip install selenium
```
## バージョン確認
`pip list | grep selenium`
```:出力
selenium          4.3.0
```

# Chromiumドライバのインストール
```bash
sudo apt install chromium-chromedriver
```
## バージョン確認
`chromedriver --version`
```:出力
ChromeDriver 101.0.4951.57 (352920124de66f14c4af140139f61c798937eda9-refs/branch-heads/4951@{#1148})
```

# 雑なサンプルコード
googleの検索ボックスで「あいうえお」と検索し、Wikipediaに飛んで「あいうえお」
の説明を表示するプログラム。
```python:selenium_test.py
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

# q = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
q = browser.find_element(By.NAME, "q")
q.send_keys("あいうえお\n")

r = browser.find_element(By.XPATH, "/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div/a")
r.click()

s = browser.find_element(By.XPATH, "/html/body/div/div/div[3]/main/div[2]/div[4]/div[1]/p")
print(s.get_attribute("innerText"))

time.sleep(1)
browser.quit()
```
以下のように出力されれば成功…?
```:出力
あいうえお、アイウエオとは、五十音のこと。またその中のあ行のこと。日本語の母音。
```