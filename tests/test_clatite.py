from app.lib.biblioteca_gastronomie import ingrediente_clatite, descriere_clatite

def test_ingrediente():
    assert "făină" in ingrediente_clatite()

def test_descriere():
    assert "pufoase" in descriere_clatite()
