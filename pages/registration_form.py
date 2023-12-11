from pages import By
from pages.base_page import BasePage

class RegistrationForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.name_field_locator = By.ID, "signupName"
        self.last_name_field_locator = By.ID, "signupLastName"
        self.email_field_locator = By.ID, "signupEmail"
        self.already_registered_locator = By.XPATH, "//div[@class='alert alert-danger' and text()='User already exists']"
        self.already_registered_locator = 'alert alert-danger'
        self.already_registered_locator = By.XPATH, "//*[contains(text(), 'User already exists')]"


        

        self.password_field = lambda: self.driver.find_element(By.ID, "signupPassword")
        self.reenter_password_field = lambda: self.driver.find_element(By.ID, "signupRepeatPassword")
        self.register_button = lambda: self.driver.find_element(By.XPATH, "//button[text()='Register']")

    @property
    def name_field(self):
        return self.driver.find_element(*self.name_field_locator)

    @name_field.setter
    def name_field(self, locator):
        self.name_field_locator = locator

    @property
    def last_name_field(self):
        return self.driver.find_element(*self.last_name_field_locator)


    @property
    def email_field(self):
        return self.driver.find_element(*self.email_field_locator)
    
    @property
    def already_registered_allert(self):
        return self.driver.find_element(*self.already_registered_locator)
