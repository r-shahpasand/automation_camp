from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

# Browser Action > Open browser
driver.get("https://google.com")
sleep(1)

# Browser Action > Browser title
browser_title = driver.title
print(browser_title)

# Browser Action > Browser back
driver.get('https://wikipedia.com')
sleep(1)
driver.back()
sleep(1)

# Browser Action > Browser forward
driver.forward()
sleep(2)

# Browser Action > Refresh
driver.refresh()

# Browser Action > Open window
driver.switch_to.new_window("tab")
sleep(1)