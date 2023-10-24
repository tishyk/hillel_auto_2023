import allure
from selenium import webdriver
import requests

from pages.registration_facade import RegistrationFacade
from src.logger import Logger

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

    @allure.feature("Beautiful tests")
    @allure.issue(url="https://google.com", name="Link for very important bag")
    @allure.link(url="https://google.com", name="Link to TestRail")
    def test_registration(self, logger):
        self._registration_facade.registration_user("test", 'testlastname', self.user_email, self.user_password,
                                                    self.user_password)
        assert self._registration_facade.check_is_user_logged_in()

    # def test_delete_user(self): # все что ниже из за того что def teardown_method(self) не работает
    #     self.driver.get("https://qauto2.forstudy.space/panel/settings")
    #     delete_users = self.driver.find_element(By.XPATH, "//button[text()='Remove my account']")
    #     delete_users.click()
    #     delete_users_confirm = self.driver.find_element(By.XPATH, "//button[text()='Remove']")
    #     delete_users_confirm.click()  # как проверить что удаление прошло успешно если это конец теста?
