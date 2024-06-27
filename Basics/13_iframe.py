from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

base_url = "https://play1.automationcamp.ir/frames.html"
driver = webdriver.Chrome()
driver.get(base_url)

driver.switch_to.frame("frame1")
driver.find_element(By.ID, "click_me_1").click()
sleep(1)
driver.switch_to.frame("frame2")
driver.find_element(By.ID, "click_me_2").click()
sleep(1)

driver.switch_to.parent_frame()  # back to parent
driver.switch_to.frame("frame3")
driver.switch_to.frame("frame4")
driver.find_element(By.ID, "click_me_4").click()
sleep(1)
driver.switch_to.default_content()  # back to main page


driver.quit()