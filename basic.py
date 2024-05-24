from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://google.com")

search_field = driver.find_element('name', 'q')
search_field.send_keys("Keep it simple stupid")
search_field.send_keys(Keys.RETURN)