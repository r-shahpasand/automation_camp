from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

base_url = "https://trytestingthis.netlify.app/"

driver = webdriver.Chrome()
driver.get(base_url)
actions = ActionChains(driver)

# Double Click
el = driver.find_element('xpath',"//button[text()='Double-click me']")
actions.double_click(el).perform()

driver.find_element('id', "demo")

# Right Click
el2 = driver.find_element('id', 'fname')
actions.context_click(el2).perform()
# Coordinate
loc = driver.find_element('xpath', "//*[text()='This is your form title:']").location
# Move by offset
actions.move_by_offset(loc['x'], loc['y']).click().perform()
sleep(1)

# Hover
el3 = driver.find_element('xpath', "//*[@class = 'tooltip']")
actions.move_to_element(el3).perform()
sleep(1)

# Drag and Drop
driver.get('https://selenium08.blogspot.com/2020/01/drag-drop.html')
el4 = driver.find_element('id', 'draggable')
el5 = driver.find_element('id', 'droppable')
actions.drag_and_drop(el4, el5).perform()