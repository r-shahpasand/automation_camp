from Pages.login import Login
from Pages.main import Main
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(3)

login = Login(driver=driver)
main = Main(driver=driver)

login.enter_user_name('Admin')
login.enter_password('admin123')
login.click_on_login_button()
main.check_dashboard()
sleep(2)
