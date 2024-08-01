def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the fields are defined correctly
    """

    assert new_user.name == "maxim"
    assert new_user.secondname == "golovin"
    assert new_user.mail == "testing@mail.ru"
    assert new_user.password == "secretpassword"
    assert new_user.role == "teacher"
    assert new_user.about == "some info"
