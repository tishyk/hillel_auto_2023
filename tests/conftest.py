import logging
import allure

import subprocess as sp
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.registration_page import RegistrationPage
from data.users import UserCreator, RegistrationTestsDataPath


@pytest.fixture
def valid_user():
    yield UserCreator.registration_users(data_path=RegistrationTestsDataPath)[-3]


@pytest.fixture
def registration_user(valid_user):
    sp.run("git status")
    sp.Popen("git status")
    sp.check_call("git status")
    sp.check_output("git status")
    sp.call("git status")
    yield valid_user
    session = requests.Session()
    session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=valid_user.session_data())
    session.delete(url="https://qauto2.forstudy.space/api/users")


@pytest.fixture
def invalid_user():
    yield UserCreator.registration_users(data_path=RegistrationTestsDataPath)[0]


@pytest.fixture
def logger():
    yield logging.getLogger()


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless") # Ubuntu server required option
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.close()


@pytest.fixture
def registration_page(driver):
    page = RegistrationPage(driver)
    yield page


@pytest.fixture
def session(registration_user):
    session = requests.Session()
    user = yield session
    session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=user_data())
    session.delete(url="https://qauto2.forstudy.space/api/users")


def pytest_pyfunc_call(pyfuncitem):
    logger = pyfuncitem._request.getfixturevalue("logger")
    logger.critical(f"Hook: {pyfuncitem.function.__doc__}")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    marker = item.get_closest_marker("registration_ui")
    if marker:
        if rep.when == "call" and rep.failed:  # we only look at actual failing test calls, not setup/teardown
            try:
                driver = item.funcargs.get("driver")
                allure.attach(driver.get_screenshot_as_png(),
                              name=item.name,
                              attachment_type=allure.attachment_type.PNG)
                driver.save_screenshot("screenshot.png")
            except Exception as e:
                print(e)
