from selenium import webdriver
from selenium.webdriver.common.keys import Keys

base_url = "https://play1.automationcamp.ir"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(f"{base_url}/forms.html")

python_check = driver.find_element('name', 'python')
python_check.click()

check_validate = driver.find_element('id', 'check_validate').text
assert check_validate == 'PYTHON'

hello_text = 'Hello World!'
driver.find_element('id', 'notes').send_keys(hello_text)
assert driver.find_element('id', 'area_notes_validate').text == hello_text
