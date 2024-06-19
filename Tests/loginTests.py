from Pages.login import Login
from Pages.main import Main
from selenium import webdriver
from time import sleep
import unittest


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_valid_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login = Login(driver=self.driver)
        main = Main(driver=self.driver)

        login.enter_user_name('Admin')
        login.enter_password('admin123')
        login.click_on_login_button()
        main.check_dashboard()
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
