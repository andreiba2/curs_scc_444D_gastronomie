import unittest
from app.lib.biblioteca_gastronomie import ingrediente_bouyourdi, descriere_bouyourdi

class TestBouyourdi(unittest.TestCase):
    def test_ingrediente(self):
        rezultat = ingrediente_bouyourdi()
        self.assertIn('feta', rezultat)

    def test_descriere(self):
        rezultat = descriere_bouyourdi()
        self.assertIn('grecesc', rezultat)

if __name__ == '__main__':
    unittest.main()