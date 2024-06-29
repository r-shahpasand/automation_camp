from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
# 0:Ask     1:Allow     2:Deny
prefs = {
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.notifications": 1,
}

options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options)

driver.get("https://play1.automationcamp.ir/")
# driver.execute_script("Notification.requestPermission()")
sleep(5)
