from lib.info_cheesecake import get_descriere, get_ingrediente

def test_verificare_descriere():
    assert "brânză" in get_descriere()

def test_verificare_ingrediente():
    assert "zahăr" in get_ingrediente()
