def test_users_get(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/users/' page is requested (GET)
    THEN check that the response is valid
    """

    response = test_client.get("api/users/")
    assert response.status_code == 200
