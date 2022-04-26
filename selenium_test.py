
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import re
from math import log2

SLEEP_TIME = 0.3

def solve_questions(driver):
    e1 = driver.find_element_by_xpath("/html/body/dir[1]/table/tbody/tr/td/blockquote")
    answer_input = driver.find_element_by_xpath("/html/body/dir[2]/form/input")
    answer_button = driver.find_element_by_xpath("/html/body/input[5]")
    inner_html = e1.get_attribute("innerHTML")

    print(inner_html)

    m = re.search(r'アナログ信号をディジタル化', inner_html)
    if m:
        answer_input.send_keys("2")
        answer_button.click()
        return True
    m = re.search(r'次の情報のうち「ディジタル」', inner_html)
    if m:
        answer_input.send_keys("2 3")
        answer_button.click()
        return True
    m = re.search(r'次の情報のうちディジタルがアナログより', inner_html)
    if m:
        answer_input.send_keys("1 4")
        answer_button.click()
        return True
    m = re.search(r'最高周波数が (\d+) Hz', inner_html)
    if m:
        ans = str(int(m.groups()[0]) * 2)
        print(ans)
        answer_input.send_keys(ans)
        answer_button.click()
        return True
    m = re.search(r'(\d+) Mb/s である。アナログ信号を表すために <br>\n(\d+)レベル', inner_html)
    if m:
        mg = m.groups()
        ans = str(int(mg[0]) // int(log2(int(mg[1]))))
        print(ans)
        answer_input.send_keys(ans)
        answer_button.click()
        return True
    m = re.search(r'ディジタル化するとき, (\d+) ビット/サンプル', inner_html)
    if m:
        ans = str(1 << int(m.groups()[0]))
        print(ans)
        answer_input.send_keys(ans)
        answer_button.click()
        return True
    m = re.search(r'次の文章', inner_html)
    if m:
        answer_input.send_keys(3)
        answer_button.click()
        return True
    return False

def main():
    # print(webdriver)

    driver = webdriver.Chrome("C:\FreeSoft\chromedriver_win32\chrome100\chromedriver.exe")

    # driver.get("https://www.google.co.jp")

    # Percent-encoding
    driver.get("http://ece:Ue%2B%25%24R%2Fg%3D%2C@www-comm.cs.shinshu-u.ac.jp/coding/")
    print(driver)

    time.sleep(SLEEP_TIME)
    # print(Alert(driver).text)

    quiz1 = driver.find_element_by_xpath("/html/body/div[2]/ol/li[1]/p/table/tbody/tr[2]/td[3]/a")
    quiz1.click()

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
    while cleared:
        cleared = solve_questions(driver)
        if cleared:
            time.sleep(SLEEP_TIME)
            try:
                next_button = driver.find_element_by_xpath("/html/body/blockquote/dir/form/input[5]")
                next_button.click()
            except NoSuchElementException:
                back_button = driver.find_element_by_xpath("/html/body/blockquote/p/a")
                back_button.click()
                break

    # driver.switch_to.alert.authenticate("cheese", "secretGouda")
    # Alert(driver).accept()

    time.sleep(3)

if __name__ == "__main__":
    main()

