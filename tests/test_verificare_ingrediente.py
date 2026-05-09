from app.lib.biblioteca_gastronomie import get_ingrediente

def test_verificare_ingrediente():
    assert "zahăr" in get_ingrediente()
