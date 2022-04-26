from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

def main():
    # print(webdriver)

    driver = webdriver.Chrome("C:\FreeSoft\chromedriver_win32\chrome100\chromedriver.exe")

    # driver.get("https://www.google.co.jp")

    # Percent-encoding
    driver.get("http://ece:Ue%2B%25%24R%2Fg%3D%2C@www-comm.cs.shinshu-u.ac.jp/coding/")
    print(driver)

    time.sleep(1)
    # print(Alert(driver).text)

    quiz1 = driver.find_element_by_xpath("/html/body/div[2]/ol/li[1]/p/table/tbody/tr[2]/td[3]/a")

    quiz1.click()

    time.sleep(1)

    name_input = driver.find_element_by_xpath("/html/body/dl/dd[2]/form/table/tbody/tr[1]/td[2]/input")
    name_input.send_keys("username")
    
    student_numter_input = driver.find_element_by_xpath("/html/body/dl/dd[2]/form/table/tbody/tr[2]/td[2]/input")
    student_numter_input.send_keys("20W2000A")

    start_button = driver.find_element_by_xpath("/html/body/dl/dd[2]/form/input[5]")
    start_button.click()

    time.sleep(1)

    start_button = driver.find_element_by_xpath("/html/body/center/form[1]/input[8]")
    start_button.click()

    e1 = driver.find_element_by_xpath("/html/body/dir[1]/table/tbody/tr/td/blockquote")
    print(e1.get_attribute("innerHTML"))

    # driver.switch_to.alert.authenticate("cheese", "secretGouda")
    # Alert(driver).accept()

    time.sleep(5)

if __name__ == "__main__":
    main()
