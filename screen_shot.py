from selenium import webdriver
from time import sleep
import os
from pathlib import Path

driver = webdriver.Chrome()
driver.get("https://yahoo.com")
sleep(1)

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
sleep(1)

current_path = Path(__file__).parent
file_name = os.path.join(str(current_path), 'screenshot.png')    # extension should be .png
driver.save_screenshot(file_name)
