import allure
from allure_commons.types import AttachmentType

from pages import known_pages
from pages.base_facade import BaseFacade


class RegistrationPage(BaseFacade):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.open_page()

    def open_page(self):
        self.page = self.driver.get(known_pages.REGISTRATION_PAGE)

    @allure.step("Register user")
    def registration(self, user):
        self._main_page.sing_up_button().click()
        self._registration_form.name_field.send_keys(user.first_name)
        self._registration_form.last_name_field.send_keys(user.last_name)
        self._registration_form.email_field.send_keys(user.email)
        self._registration_form.password_field().send_keys(user.password)
        self._registration_form.reenter_password_field().send_keys(user.password)
        allure.attach(self.driver.get_screenshot_as_png(), name="screen", attachment_type=AttachmentType.PNG)
        self._registration_form.register_button().click()

    def check_is_user_logged_in(self):
        return len(self._garage_page.empty_garage()) > 0

    def check_header(self):
        import ipdb; ipdb.set_trace()
    
    def check_footer(self):
        import ipdb; ipdb.set_trace()
