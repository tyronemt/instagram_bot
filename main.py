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
        time.sleep(5)
        u = driver.find_element_by_xpath("//input[@name='username']")
        u.send_keys(self.username)
        p = driver.find_element_by_xpath("//input[@name='password']")
        p.send_keys(self.password)
        p.send_keys(Keys.RETURN)


if __name__ == "__main__":
    ig = Instagram("tyrone.tong", "(Tong800000)")
    ig.login()