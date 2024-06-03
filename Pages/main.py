class Main:
    def __init__(self, driver):
        self.driver=driver
        self.dashboard_label_id = ""

    def check_dashboard(self):
        self.driver.find_element('xpath', "//h6[text()='Dashboard']")