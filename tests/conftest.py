import logging

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.registration_facade import RegistrationFacade


def user_data():
    """ This function should be replaced with a new fixture registration_user
    fixture should return only one correct user!!!"""
    user_email = "sytischenko@gmail.com"
    user_password = "N9Xb46SCbgd8wy!"
    user_to_login = {
        "email": user_email,
        "password": user_password,
        "remember": False
    }
    return user_to_login


@pytest.fixture
def logger():
    yield logging.getLogger()


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless") # Ubuntu server required option
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.close()


@pytest.fixture
def registration_facade(driver):
    facade = RegistrationFacade(driver)
    yield facade


@pytest.fixture
def session():
    session = requests.Session()
    user = yield session
    session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=user_data())
    session.delete(url="https://qauto2.forstudy.space/api/users")
