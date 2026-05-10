import pytest
from gastronomie import app
from app.lib.biblioteca_gastronomie import (
    text_provenienta,
    text_ingrediente,
    text_preparare
)

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_text_provenienta():
    assert "America" in text_provenienta()
    assert "pufoasă" in text_provenienta()

def test_text_ingrediente():
    assert "Făină" in text_ingrediente()
    assert "lapte" in text_ingrediente()
    assert "ouă" in text_ingrediente()

def test_text_preparare():
    assert "amestecă" in text_preparare()
    assert "prăjesc" in text_preparare()
