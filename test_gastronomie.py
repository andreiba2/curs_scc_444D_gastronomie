from app.lib.biblioteca_gastronomie import get_descriere, get_origine, get_ingrediente, get_preparare

def test_verificare_descriere():
    assert "brânză" in get_descriere()

def test_verificare_ingrediente():
    assert "zahăr" in get_ingrediente()
