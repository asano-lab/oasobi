from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

def main():
    # print(webdriver)

    driver = webdriver.Chrome("C:\FreeSoft\chromedriver_win32\chrome100\chromedriver.exe")

    # driver.get("https://www.google.co.jp")
    driver.get("http://ece:Ue%2B%25%24R%2Fg%3D%2C@www-comm.cs.shinshu-u.ac.jp/coding/")
    print(driver)

    # time.sleep(1)
    # print(Alert(driver).text)

    # driver.switch_to.alert.authenticate("cheese", "secretGouda")
    # Alert(driver).accept()

    time.sleep(5)

if __name__ == "__main__":
    main()
