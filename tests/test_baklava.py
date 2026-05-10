import pytest
from gastronomie import app
from app.lib.biblioteca_gastronomie import provenienta_baklava, ingrediente_baklava, preparare_baklava

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Teste unitare pentru funcțiile din bibliotecă
def test_functii_biblioteca():
    assert "Imperiul Otoman" in provenienta_baklava()
    assert "yufka" in ingrediente_baklava()
    assert "sirop" in preparare_baklava()

# Teste pentru rutele Flask (asigură funcționarea corectă a aplicației web)
def test_route_baklava(client):
    response = client.get('/baklava')
    assert response.status_code == 200
    html = response.data.decode('utf-8')
    assert "turkish-havuc-dilim-baklava" in html
    assert 'href="/baklava/provenienta"' in html
    assert 'href="/baklava/ingrediente"' in html
    assert 'href="/baklava/preparare"' in html

def test_route_provenienta(client):
    response = client.get('/baklava/provenienta')
    assert response.status_code == 200
    assert "Imperiul Otoman" in response.data.decode('utf-8')

def test_route_ingrediente(client):
    response = client.get('/baklava/ingrediente')
    assert response.status_code == 200
    assert "yufka" in response.data.decode('utf-8')

def test_route_preparare(client):
    response = client.get('/baklava/preparare')
    assert response.status_code == 200
    assert "sirop" in response.data.decode('utf-8')