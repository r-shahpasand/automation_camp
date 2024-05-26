from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("https://yahoo.com")
sleep(1)

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
sleep(4)
