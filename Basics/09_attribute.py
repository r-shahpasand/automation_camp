from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

base_url = "https://material.angular.io/components/input/examples"
driver = webdriver.Chrome()
driver.get(base_url)

# get value of input
input_el = driver.find_element(By.ID, 'mat-input-1')
input_el.send_keys('Attributes')
sleep(1)
input_value = input_el.get_attribute('value')
print(input_value)
assert input_value == 'Attributes'

# input field errors
error_el = driver.find_element(By.ID, 'mat-mdc-error-2')
assert error_el.text == 'Please enter a valid email address'
