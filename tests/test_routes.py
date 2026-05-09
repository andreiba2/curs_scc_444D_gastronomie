from clatite import app

def test_home_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Tema: Clatite americane" in response.data

def test_element_route():
    client = app.test_client()
    response = client.get("/clatite_americane")
    assert response.status_code == 200
    assert b"Element ales: Clatite americane" in response.data

def test_ingrediente_route():
    client = app.test_client()
    response = client.get("/clatite_americane/ingrediente")
    assert response.status_code == 200
    assert b"Ingrediente" in response.data

def test_descriere_route():
    client = app.test_client()
    response = client.get("/clatite_americane/descriere")
    assert response.status_code == 200
    assert b"Descriere" in response.data

