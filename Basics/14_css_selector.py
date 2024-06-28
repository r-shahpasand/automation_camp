from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

base_url = "https://play2.automationcamp.ir"
driver = webdriver.Chrome()
driver.get(base_url)

driver.find_element(By.CSS_SELECTOR, "input[id =fname]").send_keys("CSS Selector")
sleep(1)
