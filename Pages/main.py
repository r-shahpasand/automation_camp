from locators import *


class Main:
    def __init__(self, driver):
        self.driver=driver

    def check_dashboard(self):
        self.driver.find_element('xpath', dashboard_label_id)
