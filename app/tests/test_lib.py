from app.lib.biblioteca_gastronomie import (
    origine,
    ingrediente,
    preparare,
)


def test_origine():
    rezultat = origine()

    assert isinstance(rezultat, str)
    assert len(rezultat) > 0
    assert "Japonia" in rezultat
    assert "japonez" in rezultat.lower()


def test_ingrediente():
    rezultat = ingrediente()

    assert isinstance(rezultat, str)
    assert len(rezultat) > 0
    assert "orez" in rezultat.lower()
    assert "nori" in rezultat.lower()
    assert "wasabi" in rezultat.lower()


def test_preparare():
    rezultat = preparare()

    assert isinstance(rezultat, str)
    assert len(rezultat) > 0
    assert "orezul" in rezultat.lower()
    assert "rulează" in rezultat.lower() or "ruleaza" in rezultat.lower()
