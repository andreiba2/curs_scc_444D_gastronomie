from app.lib.biblioteca_gastronomie import descriere_macarons, ingrediente_macarons

def test_descriere():
    assert "Macarons" in descriere_macarons()

def test_ingrediente():
    assert "migdale" in ingrediente_macarons()
