from dataclasses import asdict


def test_user_get_id(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/user?id=7' page is requested (GET)
    THEN check that the response is valid
    """

    response = test_client.get("api/user?id=7")
    assert response.status_code == 200
    assert response.json["id"] == 7


def test_user_get_mail(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/user?mail=type@mail.ru' page is requested (GET)
    THEN check that the response is valid
    """

    response = test_client.get("api/user?mail=type@mail.ru")
    assert response.status_code == 200
    assert response.json["mail"] == "type@mail.ru"


def test_user_get_id_mail(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/user?mail=type@mail.ru&id=7' page is requested (GET)
    THEN check that the response is valid
    """

    response = test_client.get("api/user?mail=type@mail.ru&id=7")
    assert response.status_code == 400


def test_user_get_none(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/user' page is requested (GET)
    THEN check that the response is valid
    """

    response = test_client.get("api/user")
    assert response.status_code == 400
    
def test_user_get_no_user(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/user?id=0' page is requested (GET)
    THEN check that the response is valid
    """

    response = test_client.get("api/user?id=0")
    assert response.status_code == 404



def test_user_post(test_client, new_user):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/user' page is requested (POST)
    THEN check that the response is valid
    """
    args = asdict(new_user)

    # remove None from User args
    for key, val in {**args}.items():
        if val == None:
            del args[key]

    response = test_client.post("api/user", json=args)
    assert response.status_code == 201
    assert response.json["message"] == "success"


def test_user_post_already_used(test_client, new_user):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/user' page is requested (POST)
    THEN check that the response is valid
    """

    args = asdict(new_user)

    # remove None from User args
    for key, val in {**args}.items():
        if val == None:
            del args[key]

    response = test_client.post("api/user", json=args)
    assert response.status_code == 409


def test_user_post_no_data(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/user' page is requested (POST)
    THEN check that the response is valid
    """

    response = test_client.post("api/user")
    assert response.status_code == 415


def test_user_post_no_json_data(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/user' page is requested (POST)
    THEN check that the response is valid
    """

    response = test_client.post("api/user", json={})
    assert response.status_code == 400


def test_user_delete(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/user?mail=testing@mail.ru' page is requested (DELETE)
    THEN check that the response is valid
    """

    response = test_client.delete("api/user?mail=testing@mail.ru")

    assert response.status_code == 200


def test_user_delete_no_data(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/user' page is requested (DELETE)
    THEN check that the response is valid
    """

    response = test_client.delete("api/user")

    assert response.status_code == 400


def test_user_delete_no_json_data(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/user' page is requested (DELETE)
    THEN check that the response is valid
    """

    response = test_client.delete("api/user", json={})

    assert response.status_code == 400
    

def test_user_delete_id_mail(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/user?mail=not_existing@mail.ru' page is requested (DELETE)
    THEN check that the response is valid
    """

    response = test_client.delete("api/user?mail=not_existing@mail.ru&id=0")

    assert response.status_code == 400


def test_user_delete_no_user(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/user?mail=not_existing@mail.ru' page is requested (DELETE)
    THEN check that the response is valid
    """

    response = test_client.delete("api/user?mail=not_existing@mail.ru")

    assert response.status_code == 404


def test_user_patch_no_id(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/user' page is requested (PATCH)
    THEN check that the response is valid
    """

    response = test_client.patch("api/user", json={})
    assert response.status_code == 400


def test_user_patch_no_user(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/user' page is requested (PATCH)
    THEN check that the response is valid
    """

    response = test_client.patch("api/user", json={"id": 0})
    assert response.status_code == 404


def test_user_patch_data(test_client, new_user, new_user2):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/user' page is requested (PATCH)
    THEN create User, update User, check for valid update
    """

    args: dict = asdict(new_user)

    # remove None from User args
    for key, val in {**args}.items():
        if val == None:
            del args[key]

    # create user
    create = test_client.post("api/user", json=args)
    args2: dict = asdict(new_user2)

    # remove None from User args
    for key, val in {**args2}.items():
        if val == None:
            del args2[key]

    args2["id"] = create.json["user"]["id"]

    # update
    update = test_client.patch("api/user", json=args2)

    assert update.status_code == 200
    assert update.json["user"]["name"] == "Максим"
    assert update.json["user"]["secondname"] == "Головин"
    assert update.json["user"]["about"] == "some info2"

    # delete after test
    test_client.delete("api/user?mail=testing@mail.ru")
