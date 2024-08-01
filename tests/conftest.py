import pytest
import os
from app import app
from userService.models import UserModel


@pytest.fixture(scope="module")
def test_client():
    """
    Yields test client with app context
    """
    # Set the Testing configuration prior to creating the Flask application
    os.environ["CONFIG_TYPE"] = "config.TestingConfig"

    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope="module")
def new_user() -> "UserModel":
    """
    Returns User Instance
    """
    user = UserModel(
        name="maxim",
        secondname="golovin",
        mail="testing@mail.ru",
        password="secretpassword",
        role="teacher",
        about="some info",
    )
    return user


@pytest.fixture(scope="module")
def new_user2() -> "UserModel":
    """
    Returns User Instance
    """
    user = UserModel(
        name="Максим",
        secondname="Головин",
        mail="testing@mail.ru",
        password="secretpassword",
        role="teacher",
        about="some info2",
    )
    return user
