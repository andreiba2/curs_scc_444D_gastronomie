import pytest
from flask import Flask
from gastronomie import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_route_gastronomie(client):
    response = client.get("/gastronomie")
    assert response.status_code == 200
    assert b"gastronomie" in response.data.lower()
    
def test_route_ratatouille(client):
    response = client.get("/ratatouille")
    assert response.status_code == 200
    assert b"ratatouille" in response.data.lower()
    
def test_route_descriere(client):
    response = client.get("/ratatouille/descriere")
    assert response.status_code == 200
    assert b"preparat simplu" in response.data.lower()
    
def test_route_origine(client):
    response = client.get("/ratatouille/origine")
    assert response.status_code == 200
    assert b"Proventa" in response.data
