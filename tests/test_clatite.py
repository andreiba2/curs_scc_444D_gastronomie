import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from gastronomie import app
from app.lib.biblioteca_gastronomie import (
    text_provenienta,
    text_ingrediente,
    text_preparare
)

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# --- Testăm funcțiile din bibliotecă ---
def test_text_provenienta():
    assert "America" in text_provenienta()
    assert "pufoasă" in text_provenienta()

def test_text_ingrediente():
    assert "Făină" in text_ingrediente()
    assert "lapte" in text_ingrediente()
    assert "ouă" in text_ingrediente()

def test_text_preparare():
    assert "amestecă" in text_preparare()
    assert "prăjesc" in text_preparare()


# --- Testăm rutele aplicației ---
def test_route_gastronomie(client):
    response = client.get('/gastronomie')
    assert response.status_code == 200
    html = response.data.decode('utf-8')

    assert "Clătite Americane" in html
    assert "clatite.jpg" in html
    assert "/clatite/preparare" in html
    assert "/clatite/ingrediente" in html
    assert "/clatite/origine" in html


def test_route_origne(client):
    response = client.get('/clatite/origine')
    assert response.status_code == 200
    assert "America" in response.data.decode('utf-8')


def test_route_ingrediente(client):
    response = client.get('/clatite/ingrediente')
    assert response.status_code == 200
    assert "Făină" in response.data.decode('utf-8')


def test_route_preparare(client):
    response = client.get('/clatite/preparare')
    assert response.status_code == 200
    assert "amestecă" in response.data.decode('utf-8')
