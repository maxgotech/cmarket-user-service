from userService.models import UserModel


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the fields are defined correctly
    """

    user = UserModel(
        name="maxim",
        secondname="golovin",
        mail="test@mail.ru",
        password="secretpassword",
        role="teacher",
        about="some info",
        pfp_path="path to pic",
    )

    assert user.name == "maxim"
    assert user.secondname == "golovin"
    assert user.mail == "test@mail.ru"
    assert user.password == "secretpassword"
    assert user.role == "teacher"
    assert user.about == "some info"
    assert user.pfp_path == "path to pic"
