from locators import *


class Login:
    def __init__(self, driver):
        self.driver = driver

    def enter_user_name(self, username):
        self.driver.find_element('name', username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element('name', password_textbox_name).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element('xpath', login_button_type).click()
