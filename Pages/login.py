class Login:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_name = "username"
        self.password_textbox_name = "password"
        self.login_button_class = "oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"

    def enter_user_name(self, username):
        self.driver.find_element('name', self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element('name', self.password_textbox_name).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element('xpath',"//button[@type='submit']").click()
