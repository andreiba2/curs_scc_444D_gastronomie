from app.lib.biblioteca_gastronomie import descriere_baklava

def test_descriere_baklava():
    assert "desert dulce" in descriere_baklava()