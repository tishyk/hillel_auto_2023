from pages import By

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.sign_up_btn_locator = By.XPATH, "//button[text()='Sign up']"
        
    def sing_up_button(self):
        return self.driver.find_element(*self.sign_up_btn_locator)