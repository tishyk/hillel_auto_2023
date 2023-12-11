from pages import known_pages

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.registration_url = known_pages.REGISTRATION_PAGE
        