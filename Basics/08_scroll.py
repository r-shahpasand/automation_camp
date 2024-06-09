from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

base_url = "https://trytestingthis.netlify.app/"

driver = webdriver.Chrome()
driver.get(base_url)
driver.maximize_window()
actions = ActionChains(driver)

driver.execute_script("window.scrollBy(0,400)")

driver.execute_script("window.scrollTo(0,800)")

driver.get("https://m.imdb.com/chart/top/")
element = driver.find_element('link text', "89. Capernaum")
driver.execute_script("arguments[0].scrollIntoView();", element)
sleep(2)


# to know if a specific element exists
def scroll_to_find_element(selector, item, scroll_pixel):
    for i in range(10):
        try:
            driver.find_element(selector, item)
            print(f"The element '{selector}, {item}' is founded!")
        except:
            driver.execute_script(f"window.scrollBy(0,{str(scroll_pixel)})")
            sleep(0.5)
    # raise Exception(f"The element '{selector}, {item}' cannot be found.")
    print(f"The element '{selector}, {item}' cannot be found.")


driver.execute_script("window.scrollTo(0,0)")
scroll_to_find_element("link text", "not exists", 1800)

# scroll using actions
page_element = driver.find_element('tag name', 'html')
actions.send_keys_to_element(page_element, Keys.PAGE_UP).perform()
sleep(1)

# scroll using driver
element2 = driver.find_element('link text', "The Handmaiden")
element2.location_once_scrolled_into_view
sleep(1)
