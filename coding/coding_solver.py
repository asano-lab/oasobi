#!/usr/bin/env python3
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="符号化技術特論基礎編の課題を解くプログラム")
    parser.add_argument("username", help="ユーザー名")
    parser.add_argument("studentnumber", help="学籍番号")
    parser.add_argument("-c", "--chapter",
                        help="章 (1, 2, 3-1, 3-2,...)", nargs="+")

    parser.add_argument(
        "-b", "--browser", help="ブラウザ (Chrome, Edge, Firefox)", type=str, default="Edge")
    parser.add_argument("--repeat", help="繰り返して解く回数", type=int, default=1)

    args = parser.parse_args()

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import re
import os
import platform
from coding_questions import QUESTIONS

SLEEP_TIME = 0

RETRY_MAX = 0


def solve_questions(driver, chapter):
    e1 = driver.find_element(
        by=By.XPATH, value="/html/body/dir[1]/table/tbody/tr/td/blockquote")
    answer_input = driver.find_element(
        by=By.XPATH, value="/html/body/dir[2]/form/input")
    answer_button = driver.find_element(
        by=By.XPATH, value="/html/body/input[5]")

    inner_html = e1.get_attribute("innerHTML")

    print(inner_html)
    for q in QUESTIONS[chapter]["questions"]:
        # print(q["pattern"])
        m = re.search(q["pattern"], inner_html)
        if m:
            answer_input.send_keys(q["solver"](m))
            answer_button.click()
            return True

    print("合致する問題がありません")
    return False


def complete_questions(driver, chapter, username, studentnumber):
    quiz_link = driver.find_element(
        by=By.XPATH, value=QUESTIONS[chapter]["xpath"])
    quiz_link.click()

    time.sleep(SLEEP_TIME)

    username_input = driver.find_element(
        by=By.XPATH, value="/html/body/dl/dd[2]/form/table/tbody/tr[1]/td[2]/input")
    username_input.send_keys(username)

    studentnumter_input = driver.find_element(
        by=By.XPATH, value="/html/body/dl/dd[2]/form/table/tbody/tr[2]/td[2]/input")
    studentnumter_input.send_keys(studentnumber)

    start_button = driver.find_element(
        by=By.XPATH, value="/html/body/dl/dd[2]/form/input[5]")
    start_button.click()

    time.sleep(SLEEP_TIME)

    start_button = driver.find_element(
        by=By.XPATH, value="/html/body/center/form[1]/input[8]")
    # input(f"ユーザ名: {username}\n学籍番号: {studentnumber}\nが正しければEnterを押してください")
    start_button.click()

    cleared = True
    retry_count = 0

    while cleared:
        time.sleep(SLEEP_TIME)
        cleared = solve_questions(driver, chapter)
        if cleared:
            time.sleep(SLEEP_TIME)
            try:
                next_button = driver.find_element(
                    by=By.XPATH, value="/html/body/blockquote/dir/form/input[5]")
                next_button.click()
            except NoSuchElementException:
                try:
                    back_button = driver.find_element(
                        by=By.XPATH, value="/html/body/blockquote/p/a")
                    back_button.click()
                    print("#%s クリア!!" % chapter)
                    break
                except NoSuchElementException:
                    print("不正解!")
                    input("press enter to end: ")
                    if retry_count < RETRY_MAX:
                        retry_button = driver.find_element(
                            by=By.XPATH, value="/html/body/center/table[2]/tbody/tr/td[1]/form/input[8]")
                        retry_button.click()
                        retry_count += 1
                    else:
                        back_button = driver.find_element(
                            by=By.XPATH, value="/html/body/center/table[2]/tbody/tr/td[2]/a")
                        back_button.click()
                        break


def main(username, studentnumber, chapter_list, browser, repeat):
    pf = platform.system()

    if pf == "Linux":
        # options = Options()
        # options.binary_location = "/usr/bin/firefox"
        # options.add_argument("-headless")
        # driver = webdriver.Firefox(options=options)options = Options()
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        # options.add_argument('--window-size=1024,768')

        driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", chrome_options=options);
    else:
        env_var = [i for i in os.getenv("PATH").split(";") if os.path.isdir(i)]
        if browser == "Chrome":
            driver_name = "chromedriver.exe"
            driver_type = webdriver.Chrome
        elif browser == "Firefox":
            options = Options()
            options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            driver_name = "geckodriver.exe"
            driver_type = webdriver.Firefox
        else:
            driver_name = "msedgedriver.exe"
            driver_type = webdriver.Edge
        for dir_name in env_var:
            driver_path = dir_name + "\\" + driver_name
            # print(driver_path)
            if os.path.isfile(driver_path):
                print(driver_path)
                if browser == "Firefox":
                    driver = driver_type(options=options)
                else:
                    driver = driver_type(driver_path)
                break
        else:
            print(f"{browser} ドライバが見つかりません")
            return -1

    with open("private/coding_url.txt") as f:
        url = f.read()
        print(url)
        driver.get(url)

    time.sleep(SLEEP_TIME)

    # 章を指定しなければ全て解く
    for i in range(repeat):
        print("%d回目" % (i + 1))
        if chapter_list is None:
            for chapter in QUESTIONS.keys():
                complete_questions(driver, chapter, username, studentnumber)
                time.sleep(SLEEP_TIME)
        else:
            for chapter in chapter_list:
                if chapter in QUESTIONS.keys():
                    complete_questions(
                        driver, chapter, username, studentnumber)
                    time.sleep(SLEEP_TIME)

    # input("press enter to end: ")
    # time.sleep(3)


if __name__ == "__main__":
    main(args.username, args.studentnumber,
         args.chapter, args.browser, args.repeat)
