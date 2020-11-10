from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="C:/web_driver/geckodriver")
driver.get('https://google.com')