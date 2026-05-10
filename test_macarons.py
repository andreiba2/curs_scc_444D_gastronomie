from app.lib.biblioteca_gastronomie import origine_macarons, ingrediente_macarons, preparare_macarons

def test_origine():
    rezultat = origine_macarons()
    assert "Italia" in rezultat

def test_ingrediente():
    rezultat = ingrediente_macarons()
    assert "migdale" in rezultat

def test_preparare():
    rezultat = preparare_macarons()
    assert "bezea" in rezultat
