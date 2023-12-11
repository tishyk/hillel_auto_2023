import sys
import string
from pytest import mark
from data.users import UserCreator, RegistrationTestsDataPath


@mark.parametrize('user',
                  UserCreator.registration_users(data_path=RegistrationTestsDataPath))
def test_user_config_file(user, logger):
    """Validate password requirements"""
    assert any([s.isdigit() for s in user.password])


@mark.parametrize('user,password',
                  [("Andrii", '123456'),
                   ("Marta","987654321"),
                   ("Vitalii","qwerty123")])
def test_user_names(logger, user, password):
    """Validate password requirements"""
    logger.critical(f"{user}, {password}")
    assert user.istitle()


@mark.xfail(reason="BUG_ID or link")
@mark.existing_user
def test_sign_up1(logger):
    """Test to verify user signup 1"""  # test_sign_up.__doc__
    logger.info("Test to verify user signup")
    assert False


@mark.skip(reason="no way of currently testing this")
@mark.new_user
def test_sign_up2(logger):
    """Test to verify user signup 2"""  # test_sign_up.__doc__
    logger.info("Test to verify user signup 2")


@mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
@mark.deleted_user
def test_sign_up3(logger):
    """Test to verify user signup 3"""  # test_sign_up.__doc__
    logger.info("Test to verify user signup")


def test_sign_up4(logger):
    """Test to verify user signup 4"""  # test_sign_up.__doc__
    logger.info("Test to verify user signup")
