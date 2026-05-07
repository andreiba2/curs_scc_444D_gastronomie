from app import app


def test_home_page_returns_ok():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_home_page_shows_baklava_content():
    client = app.test_client()

    response = client.get("/")
    body = response.get_data(as_text=True)

    assert "Baklava" in body
    assert "/recipe" in body
    assert "/history" in body
    assert "/serving-tips" in body


def test_recipe_route_returns_content():
    client = app.test_client()

    response = client.get("/recipe")

    assert response.status_code == 200
    assert "Baklava Recipe" in response.get_data(as_text=True)


def test_history_route_returns_content():
    client = app.test_client()

    response = client.get("/history")

    assert response.status_code == 200
    assert "The Rich History of Baklava" in response.get_data(as_text=True)


def test_serving_tips_route_returns_content():
    client = app.test_client()

    response = client.get("/serving-tips")

    assert response.status_code == 200
    assert "Serving Tips" in response.get_data(as_text=True)
