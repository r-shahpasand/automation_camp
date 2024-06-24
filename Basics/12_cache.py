from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
user_dir = "C:/Users/Raheleh/Documents/automation_camp/user_dir"
options.add_argument(f"user-data-dir={user_dir}")


base_url = "https://app.clockify.me/en/signup"
driver = webdriver.Chrome(options)
driver.get(base_url)
windows = driver.window_handles
driver.switch_to.window(windows[0])

driver.implicitly_wait(2)

sleep(3)