from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

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


def wait_until_element_has_not_an_attribute(element_selector, element_locator, attribute, attribute_value, timeout=5):
    for i in range(timeout * 5):
        try:
            element = driver.find_element(element_selector, element_locator)
            assert attribute_value not in element.get_attribute(attribute)
            return
        except:
            sleep(0.2)
    raise Exception("Element attribute  " + str(attribute_value) + " found.")


trigger = driver.find_element(By.ID, "enabled_trigger")
trigger.location_once_scrolled_into_view

wait_until_element_has_not_an_attribute(By.ID, "enabled_target", "class", "success")
wait_until_element_has_an_attribute(By.ID, "enabled_target", "class", "danger")


# trigger.click()
# wait_until_element_has_an_attribute(By.ID, "enabled_target", "class", "success")

def wait_until_element_is_enabled(selector, locator, timeout):
    for i in range(timeout * 5):
        try:
            element = driver.find_element(selector, locator)
            assert element.is_enabled()
        except:
            sleep(0.5)


# trigger.click()
# wait_until_element_is_enabled(By.ID, "enabled_target", 5)


# wait until element is visible
def wait_until_element_is_visible(selector, locator, timeout=5):
    for i in range(timeout * 5):
        try:
            element = driver.find_element(selector, locator)
            assert element.is_displayed()
        except:
            sleep(0.5)


# wait until element is invisible
def wait_until_element_is_not_visible(selector, locator, timeout=5):
    for i in range(timeout * 5):
        try:
            element = driver.find_element(selector, locator)
            assert not element.is_displayed()
        except:
            sleep(0.5)


target = driver.find_element(By.ID, "visibility_trigger")
target.location_once_scrolled_into_view
target.click()
wait_until_element_is_visible(By.ID, "visibility_target")

# WebDriverWait until expected condition
trigger.click()
wait = WebDriverWait(driver, 5)
element2 = wait.until(expected_conditions.element_to_be_clickable((By.ID, "enabled_target")))
print(element2.is_enabled())


# wait until page is loaded
def wait_until_page_is_loaded(timeout=10):
    for i in range(timeout * 2):
        try:
            state = driver.execute_script("return document.readyState")
            assert state == 'complete'
            print(state)
            return
        except:
            sleep(0.5)


driver.get("https://archive.org/details/texts")
wait_until_page_is_loaded()
