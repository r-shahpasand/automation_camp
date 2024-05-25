from selenium import webdriver
from time import sleep

base_url = "https://play1.automationcamp.ir"

driver = webdriver.Chrome()
driver.get(f"{base_url}/forms.html")

python_check = driver.find_element('name', 'python')
python_check.click()

check_validate = driver.find_element('id', 'check_validate').text
assert check_validate == 'PYTHON'

sleep(2)
hello_text = 'Hello World!'
driver.find_element('id', 'notes').send_keys(hello_text)
assert driver.find_element('id', 'area_notes_validate').text == hello_text
sleep(3)

driver.quit()