from app.lib.biblioteca_gastronomie import origine_piftie, ingrediente_piftie, preparare_piftie

def test_continut_piftie():
    assert len(origine_piftie()) > 0
    assert len(ingrediente_piftie()) > 0
    assert len(preparare_piftie()) > 0

def test_cuvinte_cheie_piftie():
    assert "românesc" in origine_piftie().lower()
    assert "usturoi" in ingrediente_piftie().lower()
    assert "fierbe" in preparare_piftie().lower()
