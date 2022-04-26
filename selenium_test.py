from selenium import webdriver
import time

def main():
    print(webdriver)

    driver = webdriver.Chrome("C:\FreeSoft\chromedriver_win32\chrome100\chromedriver.exe")

    driver.get("https://www.google.co.jp")
    print(driver)


    time.sleep(5)

if __name__ == "__main__":
    main()
