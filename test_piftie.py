from app.lib.biblioteca_gastronomie import descriere_piftie, ingrediente_piftie

def test_descriere():
    assert "Piftia" in descriere_piftie()

def test_ingrediente():
    assert "carne" in ingrediente_piftie()
