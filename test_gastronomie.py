import unittest
from app.lib.biblioteca_gastronomie import ingrediente_ciorba_de_burta, descriere_ciorba_de_burta

class TestCiorba(unittest.TestCase):

    def test_ingrediente(self):
        rezultat = ingrediente_ciorba_de_burta()
        self.assertIn("usturoi", rezultat)

    def test_descriere(self):
        rezultat = descriere_ciorba_de_burta()
        self.assertIn("românească", rezultat)

if __name__ == '__main__':
    unittest.main()
