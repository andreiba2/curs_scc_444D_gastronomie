import unittest
from app.lib.biblioteca_gastronomie import text_provenienta, text_ingrediente, text_preparare

class TestGastronomie(unittest.TestCase):
    def test_provenienta(self):
        self.assertIn("Italia", text_provenienta())
    
    def test_ingrediente(self):
        self.assertIn("Guanciale", text_ingrediente())

    def test_preparare(self):
        self.assertIn("emulsia", text_preparare())

if __name__ == '__main__':
    unittest.main()
