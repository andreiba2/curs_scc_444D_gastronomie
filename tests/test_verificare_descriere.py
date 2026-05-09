from app.lib.biblioteca_gastronomie import get_descriere

def test_verificare_descriere():
    assert "brânză" in get_descriere()
