import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.lib.biblioteca_gastronomie import provenienta_gulas, ingrediente_gulas

def test_origine_gulas_not_empty():
    rezultat = provenienta_gulas()
    assert rezultat is not None
    assert len(rezultat) > 0

def test_origine_gulas_contine_cuvant_cheie():
    rezultat = provenienta_gulas()
    assert "maghiar" in rezultat.lower() or "ungaria" in rezultat.lower()

def test_ingrediente_gulas_not_empty():
    rezultat = ingrediente_gulas()
    assert rezultat is not None
    assert len(rezultat) > 0

def test_ingrediente_gulas_contine_carne():
    rezultat = ingrediente_gulas()
    assert "carne" in rezultat.lower() or "vită" in rezultat.lower()
