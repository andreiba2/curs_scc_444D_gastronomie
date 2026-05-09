import pytest
from gastronomie import app
from app.lib.biblioteca_gastronomie import descriere_baklava

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_descriere_baklava_functie():
    # Testăm funcția de bază din biblioteca ta
    assert "desert dulce" in descriere_baklava()

def test_route_baklava(client):
    # Testăm dacă pagina principală se încarcă și conține imaginea și butoanele
    response = client.get('/baklava')
    assert response.status_code == 200
    html = response.data.decode('utf-8')
    assert "turkish-havuc-dilim-baklava" in html  # Verifică prezența imaginii
    assert 'href="/baklava/descriere"' in html    # Verifică butonul descriere
    assert 'href="/baklava/origine"' in html      # Verifică butonul origine

def test_route_descriere(client):
    # Testăm dacă descrierea se randează corect
    response = client.get('/baklava/descriere')
    assert response.status_code == 200
    assert "desert dulce" in response.data.decode('utf-8')