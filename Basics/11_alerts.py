from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

base_url = "https://the-internet.herokuapp.com/javascript_alerts"
driver = webdriver.Chrome()
driver.get(base_url)
actions = ActionChains(driver)
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
dom = driver.page_source
assert 'You clicked: Cancel' in dom

# send keys to alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
alert.send_keys('Hello world!')
sleep(1)
alert.accept()
assert 'Hello world!' in driver.page_source

# Open dialog
driver.get('https://material.angular.io/components/dialog/examples')
driver.find_element(By.XPATH, "//span[text()='Open dialog']").click()
material_btn = driver.find_element(By.XPATH, "//span[text()=' Material ']")
offset = material_btn.location
driver.find_element(By.XPATH, "//span[text()='Install']")

actions.move_by_offset(offset['x'], offset['y']).pause(1).click().perform()



