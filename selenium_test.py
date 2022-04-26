
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import re
from math import log2

SLEEP_TIME = 0.2

RETRY_MAX = 1

def solve_q1_1_1(m):
    print("固定値: 2")
    return "2"

def solve_q1_1_2(m):
    print("固定値: 2 3")
    return "2 3"

def solve_q1_1_3(m):
    print("固定値: 1 4")
    return "1 4"

def solve_q1_1_4(m):
    ans = str(int(m.groups()[0]) * 2)
    print("最高周波数の倍 %s サンプル必要" % ans)
    return ans

def solve_q1_1_5(m):
    mg = m.groups()
    ans = str(int(mg[0]) // int(log2(int(mg[1]))))
    print("通信速度をレベルのビット数で割った %s MHz" % ans)
    return ans

def solve_q1_1_6(m):
    ans = str(1 << int(m.groups()[0]))
    print("レベルは2のビット数乗 %s" % ans)
    return ans

def solve_q1_1_7(m):
    print("固定値: 3")
    return "3"

def solve_q2_1_1(m):
    print("固定値: 25/36")
    return "25/36"
    
def solve_q2_1_2(m):
    print("固定値: 25/36")
    return "25/36"

def solve_q2_1_3(m):
    print("固定値: 5/324")
    return "5/324"

def solve_q2_1_4(m):
    return ""

QUESTIONS = {
    "1": {
        "xpath": "/html/body/div[2]/ol/li[1]/p/table/tbody/tr[2]/td[3]/a",
        "questions": [
            {"pattern": re.compile(r'アナログ信号をディジタル化'), "solver": solve_q1_1_1},
            {"pattern": re.compile(r'次の情報のうち「ディジタル」'), "solver": solve_q1_1_2},
            {"pattern": re.compile(r'次の情報のうちディジタルがアナログより'), "solver": solve_q1_1_3},
            {"pattern": re.compile(r'最高周波数が (\d+) Hz'), "solver": solve_q1_1_4},
            {"pattern": re.compile(r'(\d+) Mb/s である。アナログ信号を表すために <br>\n(\d+)レベル'), "solver": solve_q1_1_5},
            {"pattern": re.compile(r'ディジタル化するとき, (\d+) ビット/サンプル'), "solver": solve_q1_1_6},
            {"pattern": re.compile(r'次の文章.*用語はなにか'), "solver": solve_q1_1_7}
        ]
    },
    "2": {
        "xpath": "/html/body/div[2]/ol/li[1]/p/table/tbody/tr[3]/td[3]/a",
        "questions": [
            {"pattern": re.compile(r'さいころを 2 回振る。このとき \d の目が 1 回も出ない'), "solver": solve_q2_1_1},
            {"pattern": re.compile(r'2 個のさいころを同時に振る。このとき \d の目が出ない'), "solver": solve_q2_1_2},
            {"pattern": re.compile(r'\d の目がちょうど 3 回'), "solver": solve_q2_1_3},
            {"pattern": re.compile(r'このとき 1 の目か 2 の目または 1 と 2 の両方'), "solver": solve_q2_1_4}
        ]
    }
}

def solve_questions(driver, chapter):
    e1 = driver.find_element_by_xpath("/html/body/dir[1]/table/tbody/tr/td/blockquote")
    answer_input = driver.find_element_by_xpath("/html/body/dir[2]/form/input")
    answer_button = driver.find_element_by_xpath("/html/body/input[5]")

    inner_html = e1.get_attribute("innerHTML")

    print(inner_html)
    for q in QUESTIONS[chapter]["questions"]:
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
                    break
                except NoSuchElementException:
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

    driver = webdriver.Chrome("C:\FreeSoft\chromedriver_win32\chrome100\chromedriver.exe")

    print(type(driver))
    print(driver)
    # driver.get("https://www.google.co.jp")

    # Percent-encoding
    with open("private/coding_url.txt") as f:
        url = f.read()
        print(url)
        driver.get(url)

    time.sleep(SLEEP_TIME)

    complete_questions(driver, "2")
    

    time.sleep(3)

if __name__ == "__main__":
    main()

