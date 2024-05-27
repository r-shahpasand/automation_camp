from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://wikipedia.com")
sleep(1)

# el1 = driver.find_element('id', "searchInput")
el1 = driver.find_element('css selector', "#searchInput")
el2 = driver.find_element('xpath', "//input[@type='search']")
assert el1 == el2
sleep(1)

el3 = driver.find_element('xpath', "//*[text() = 'Deutsch']")
el3.click()
sleep(1)
driver.back()

el4 = driver.find_element('tag name', "select")
el4.click()
sleep(1)

el5 = driver.find_element('link text', "Download Wikipedia for Android or iOS")
el5.click()
sleep(1)
driver.back()

el6 = driver.find_element('partial link text', "Download")
el6.click()
sleep(1)
driver.back()

el1.send_keys('Hello World!')
# el7 = driver.find_element('class name', "svg-search-icon")
el7 = driver.find_element('css selector', ".svg-search-icon")
el7.click()
sleep(1)
driver.back()
