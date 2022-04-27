
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import re
import os
from coding_questions import QUESTIONS

SLEEP_TIME = 0.1

RETRY_MAX = 0

def solve_questions(driver, chapter):
    e1 = driver.find_element_by_xpath("/html/body/dir[1]/table/tbody/tr/td/blockquote")
    answer_input = driver.find_element_by_xpath("/html/body/dir[2]/form/input")
    answer_button = driver.find_element_by_xpath("/html/body/input[5]")

    inner_html = e1.get_attribute("innerHTML")

    print(inner_html)
    for q in QUESTIONS[chapter]["questions"]:
        # print(q["pattern"])
        m = re.search(q["pattern"], inner_html)
        if m:
            answer_input.send_keys(q["solver"](m))
            answer_button.click()
            return True
    
    return False

def complete_questions(driver, chapter):
    quiz_link = driver.find_element_by_xpath(QUESTIONS[chapter]["xpath"])
    quiz_link.click()

    time.sleep(SLEEP_TIME)

    name_input = driver.find_element_by_xpath("/html/body/dl/dd[2]/form/table/tbody/tr[1]/td[2]/input")
    name_input.send_keys("username")

    student_numter_input = driver.find_element_by_xpath("/html/body/dl/dd[2]/form/table/tbody/tr[2]/td[2]/input")
    student_numter_input.send_keys("20W2000A")

    start_button = driver.find_element_by_xpath("/html/body/dl/dd[2]/form/input[5]")
    start_button.click()

    time.sleep(SLEEP_TIME)

    start_button = driver.find_element_by_xpath("/html/body/center/form[1]/input[8]")
    start_button.click()

    cleared = True
    retry_count = 0

    while cleared:
        cleared = solve_questions(driver, chapter)
        if cleared:
            time.sleep(SLEEP_TIME)
            try:
                next_button = driver.find_element_by_xpath("/html/body/blockquote/dir/form/input[5]")
                next_button.click()
            except NoSuchElementException:
                try:
                    back_button = driver.find_element_by_xpath("/html/body/blockquote/p/a")
                    back_button.click()
                    print("#%s クリア!!" % chapter)
                    break
                except NoSuchElementException:
                    print("不正解!")
                    input("press enter to end: ")
                    if retry_count < RETRY_MAX:
                        retry_button = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td[1]/form/input[8]")
                        retry_button.click()
                        retry_count += 1
                    else:
                        back_button = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td[2]/a")
                        back_button.click()
                        break

def main():
    # print(webdriver)

    env_var = [i for i in os.getenv("PATH").split(";") if os.path.isdir(i)]
    for dir_name in env_var:
        driver_path = dir_name + "\chromedriver.exe"
        if os.path.isfile(driver_path):
            driver = webdriver.Chrome(driver_path)
            break
    else:
        print("ドライバが見つかりません")
        return -1

    print(type(driver))
    print(driver)
    # driver.get("https://www.google.co.jp")

    # Percent-encoding
    with open("private/coding_url.txt") as f:
        url = f.read()
        print(url)
        driver.get(url)

    time.sleep(SLEEP_TIME)

    for chapter in QUESTIONS.keys():
        # if chapter == "4-3":
        complete_questions(driver, chapter)
        time.sleep(SLEEP_TIME)

    # input("press enter to end: ")
    # time.sleep(3)

if __name__ == "__main__":
    main()

