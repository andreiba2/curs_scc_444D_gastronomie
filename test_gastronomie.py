import unittest
from app.lib.biblioteca_gastronomie import ingrediente_ramen, descriere_ramen

class TestRamen(unittest.TestCase):
    
    def test_ingrediente(self):
        rezultat = ingrediente_ramen()
        self.assertIn("Tăiței", rezultat)
        
    def test_descriere(self):
        rezultat = descriere_ramen()
        self.assertIn("japonez", rezultat)

if __name__ == '__main__':
    unittest.main()
