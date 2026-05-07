import unittest
from app.lib.biblioteca_gastronomie import provenienta_ramen, ingrediente_ramen, preparare_ramen

class TestRamen(unittest.TestCase):
    
    def test_provenienta(self):
        rezultat = provenienta_ramen()
        self.assertIn("Japonia", rezultat)
        
    def test_ingrediente(self):
        rezultat = ingrediente_ramen()
        self.assertIn("Tăiței", rezultat)
        
    def test_preparare(self):
        rezultat = preparare_ramen()
        self.assertIn("Supa", rezultat)

if __name__ == '__main__':
    unittest.main()
