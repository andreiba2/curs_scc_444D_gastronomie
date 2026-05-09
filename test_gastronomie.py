from app.lib.biblioteca_gastronomie import get_descriere, get_origine, get_ingrediente, get_preparare

def test_verificare_descriere():
    assert "mascarpone" in get_descriere().lower()

def test_verificare_ingrediente():
    assert "cafea" in get_ingrediente().lower()
