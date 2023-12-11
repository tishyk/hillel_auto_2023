import allure

from pytest import mark, raises
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

@allure.feature("Register tests")
@allure.issue(url="https://google.com", name="Link for very important bag")
@allure.link(url="https://google.com", name="Link to TestRail")
@mark.order(1)
@mark.new_user
def test_registration_form(logger, registration_page, registration_user):
    # Test registartion form and delete user immediately after creation
    logger.info("User registration test")
    registration_page.registration(registration_user)
    assert registration_page.check_is_user_logged_in()


@mark.registration_test
@mark.registration_ui
def test_registered_user(logger, registration_page, valid_user):
    # Test registration test
    registration_page.registration(valid_user)
    assert registration_page._registration_form.already_registered_allert.text == "User already exists"
    assert registration_page.check_is_user_logged_in()

@mark.registration_test
@mark.order(2)
#@mark.xfail(raises=AssertionError)
def test_registration_duplicate_expected_to_fail(logger, registration_page, valid_user):
    # Test registartion form test for already created user
    logger.info("User registration test")
    registration_page.registration(valid_user)
    assert registration_page.check_is_user_logged_in()
