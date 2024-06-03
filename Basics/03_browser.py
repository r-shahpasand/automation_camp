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

# Browser Action > Current handle
driver.switch_to.new_window('window')
driver.get('https://wikipedia.com')
current_handle = driver.current_window_handle
print('current handle:' + str(current_handle))
sleep(1)

# Browser Action > Close tab
driver.close()
sleep(1)

# Browser Action > All handles
all_handles = driver.window_handles
print('current all handles:' + str(all_handles))
sleep(1)

# Browser Action > Switch
driver.switch_to.window(all_handles[0])
sleep(1)

# Browser Action > Get window size
window_size = driver.get_window_size()
print(window_size)

# Browser Action > Quit session
driver.set_window_size(900, 800)
sleep(1)

# Browser Action > Window position
print(driver.get_window_position())
driver.set_window_position(80, 8)
sleep(1)

# Browser Action > minimize
driver.minimize_window()
sleep(1)

# Browser Action > maximize
driver.maximize_window()
sleep(1)

# Browser Action > fullscreen
driver.fullscreen_window()

# Browser Action > Quit session
driver.quit()
