import pytest
from gastronomie import app 
from app.lib.biblioteca_gastronomie import provenienta_gulas, ingrediente_gulas, preparare_gulas

@pytest.fixture
def client():
    app.config['TESTING'] = true
    with app.test_client() as client:
        yeld client

def test_origine_gulas_not_empty():
    rezultat = provenienta_gulas()
    assert rezultat is not None
    assert len(rezultat) > 0

def test_origine_gulas_contine_cuvant_cheie():
    rezultat = provenienta_gulas()
    assert "maghiar" in rezultat.lower() or "ungaria" in rezultat.lower()

def test_ingrediente_gulas_not_empty():
    rezultat = ingrediente_gulas()
    assert rezultat is not None
    assert len(rezultat) > 0

def test_ingrediente_gulas_contine_carne():
    rezultat = ingrediente_gulas()
    assert "carne" in rezultat.lower() or "vită" in rezultat.lower()
    
def test_route():
    raspuns = client.get('/gulas')
    assert raspuns.status_code == 200
    

