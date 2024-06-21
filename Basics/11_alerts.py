from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

base_url = "https://the-internet.herokuapp.com/javascript_alerts"
driver = webdriver.Chrome()
driver.get(base_url)
driver.maximize_window()
driver.implicitly_wait(1)
alert = Alert(driver)

driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

# get alert text
print(alert.text)

# accept alert
alert.accept()
driver.find_element(By.XPATH, "//p[text()='You successfully clicked an alert']")
dom = driver.page_source
assert 'You successfully clicked an alert' in dom

# dismiss alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
alert.dismiss()
assert 'You clicked: Cancel' in dom
