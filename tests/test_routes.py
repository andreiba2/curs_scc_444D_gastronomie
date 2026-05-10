import pytest
from gastronomie import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Tema" in response.data
    assert b"Cl" in response.data  

def test_element_route(client):
    response = client.get('/clatite_americane')
    assert response.status_code == 200
    assert b"Cl" in response.data

def test_ingrediente_route(client):
    response = client.get('/clatite_americane/ingrediente')
    assert response.status_code == 200
    assert b"Ingrediente" in response.data

def test_descriere_route(client):
    response = client.get('/clatite_americane/descriere')
    assert response.status_code == 200
    assert b"Descriere" in response.data

def test_preparare_route(client):
    response = client.get('/clatite_americane/preparare')
    assert response.status_code == 200
    assert b"Preparare" in response.data
