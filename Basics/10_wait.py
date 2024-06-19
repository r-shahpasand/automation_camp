from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

base_url = "https://play1.automationcamp.ir/expected_conditions.html"
driver = webdriver.Chrome()
driver.get(base_url)
driver.implicitly_wait(1)


def wait_until_element_has_an_attribute(element_selector, element_locator, attribute, attribute_value, timeout=5):
    for i in range(timeout * 5):
        try:
            element = driver.find_element(element_selector, element_locator)
            assert attribute_value in element.get_attribute(attribute)
            return
        except:
            sleep(0.2)
    raise Exception("Element attribute  " + str(attribute_value) + "not found.")

trigger = driver.find_element(By.ID, "enabled_trigger")
trigger.location_once_scrolled_into_view
trigger.click()

wait_until_element_has_an_attribute(By.ID, "enabled_target", "class", "success")
