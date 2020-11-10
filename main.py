from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



class Instagram:

    def __init__ (self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path="geckodriver")

    def exitbrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(2)
        #"//input[@name='username']"
        #"//input[@name='password']"


if __name__ == "__main__":
    # ig = Instagram("tyrone.tong", "(Tong800000)")
    driver = webdriver.Firefox(executable_path="geckodriver")
    driver.get('https://www.instagram.com/')