import unittest
from app.lib.lib_gastronomie import ingrediente, preparare, provenienta

class TestRamen(unittest.TestCase):
    
    def test_provenienta(self):
        rezultat = provenienta()
        self.assertIn("francez", rezultat)
        
    def test_ingrediente(self):
        rezultat = ingrediente()
        self.assertIn("făină", rezultat)
        
    def test_preparare(self):
        rezultat = preparare()
        self.assertIn("Coace", rezultat)

if __name__ == '__main__':
    unittest.main()