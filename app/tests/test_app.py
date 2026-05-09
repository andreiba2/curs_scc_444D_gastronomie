from app.gastronomie import app


def test_pagina_principala():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200

    continut = response.data.decode("utf-8")
    assert "Sushi" in continut
    assert "Preparat tradițional japonez" in continut
    assert "Țara de proveniență" in continut
    assert "Ingrediente principale" in continut
    assert "Modul de preparare" in continut


def test_ruta_gastronomie():
    client = app.test_client()
    response = client.get("/gastronomie")

    assert response.status_code == 200
    assert "Sushi" in response.data.decode("utf-8")


def test_ruta_sushi():
    client = app.test_client()
    response = client.get("/gastronomie/sushi")

    assert response.status_code == 200
    assert "Sushi" in response.data.decode("utf-8")


def test_ruta_origine():
    client = app.test_client()
    response = client.get("/origine")

    assert response.status_code == 200

    continut = response.data.decode("utf-8")
    assert "Țara de proveniență" in continut
    assert "Japonia" in continut


def test_ruta_ingrediente():
    client = app.test_client()
    response = client.get("/ingrediente")

    assert response.status_code == 200

    continut = response.data.decode("utf-8")
    assert "Ingrediente principale" in continut
    assert "orez" in continut.lower()


def test_ruta_preparare():
    client = app.test_client()
    response = client.get("/preparare")

    assert response.status_code == 200

    continut = response.data.decode("utf-8")
    assert "Modul de preparare" in continut
    assert "orezul" in continut.lower()
