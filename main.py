from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

lst = ["tongtyrone"]
m= "instagram bot testing"

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
        u = driver.find_element_by_xpath("//input[@name='username']")
        u.send_keys(self.username)
        p = driver.find_element_by_xpath("//input[@name='password']")
        p.send_keys(self.password)
        p.send_keys(Keys.RETURN)
        time.sleep(5)
        
    def dm(self):
        driver = self.driver
        dm = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a")
        dm.click()
        time.sleep(3)
        not_now = driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
        not_now.click()
        home = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[1]/div/div[1]/a")
        home.click()
        time.sleep(2)
        for i in lst:
            self.search(i)
            self.message()
            
    def search(self,i):
        driver = self.driver
        search = driver.find_element_by_xpath("//*[contains(text(), 'Search')]")
        search.click()
        search1 = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        search1.click()
        search1.send_keys(i)
        time.sleep(2)
        search1.send_keys(Keys.RETURN)
        search1.send_keys(Keys.RETURN)
        time.sleep(3)
    
    def message(self):
        driver = self.driver
        message = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button")
        message.click()
        time.sleep(3)
        send = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        send.click()
        send.send_keys(m)
        send.send_keys(Keys.RETURN)
        time.sleep(2)
        home = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[1]/div/div[1]/a")
        home.click()
        time.sleep(2)
    

if __name__ == "__main__":
    ig = Instagram("tyrone.tong", "(Tong800000)")
    ig.login()
    ig.dm()


            