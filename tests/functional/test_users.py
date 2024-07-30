
def test_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'api/users/' page is requested (GET)
    THEN check that the response is valid
    """

    response = test_client.get("api/users/")
    print(response.json)
    assert response.status_code == 200
    assert response.json
