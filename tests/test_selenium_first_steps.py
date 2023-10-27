import logging

import allure
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.registration_facade import RegistrationFacade

logger = logging.getLogger()
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")

# registration

class TestDase:
    def setup_method(self):
        self._driver = webdriver.Chrome()
        self._session = requests.Session()
        self._registration_facade = RegistrationFacade(self._driver)

        self._driver.implicitly_wait(3)
        self._driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

    def teardown_method(self):
        self._driver.close()


class TestRegisteration(TestDase):

    def setup_class(self):
        # self.driver.implicitly_wait(3)
        # self.session = requests.Session()
        self.user_email = "sytischenko@gmail.com"
        self.user_password = "N9Xb46SCbgd8wy!"
        self.user_to_login = {
            "email": self.user_email,
            "password": self.user_password,
            "remember": False
        }

    def teardown_method(self):
        self._session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=self.user_to_login)
        self._session.delete(url="https://qauto2.forstudy.space/api/users")
        super().teardown_method()

    @allure.feature("Beautiful tests")
    @allure.issue(url="https://google.com", name="Link for very important bag")
    @allure.link(url="https://google.com", name="Link to TestRail")
    def test_registration(self):
        logger.info("User register")
        self._registration_facade.registration_user("test", 'testlastname', self.user_email, self.user_password,
                                                    self.user_password)
        assert self._registration_facade.check_is_user_logged_in()

    def test_failed_registration_test(self):
        self._driver.get("https://qauto2.forstudy.space/panel/settings")
        try:
            delete_users = self._driver.find_element(By.XPATH, "//button[text()='Remove my account']")
        except NoSuchElementException:
            logger.critical("No element found")
            # raise RuntimeError("No element found //button[text()='Remove my account']")
        else:
            delete_users.click()
            delete_users_confirm = self._driver.find_element(By.XPATH, "//button[text()='Remove']")
            delete_users_confirm.click()
