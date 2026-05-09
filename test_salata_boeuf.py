from app.lib.biblioteca_gastronomie import descriere_salata_boeuf, ingrediente_salata_boeuf

def test_continut_salata():
    assert len(descriere_salata_boeuf()) > 0
    assert len(ingrediente_salata_boeuf()) > 0

def test_cuvinte_cheie():
    ingrediente = ingrediente_salata_boeuf().lower()
    assert "cartofi" in ingrediente
    assert "maioneza" in ingrediente
