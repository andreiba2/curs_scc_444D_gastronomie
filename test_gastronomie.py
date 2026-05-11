import unittest
from app.lib.biblioteca_gastronomie import provenienta_ramen, ingrediente_ramen, preparare_ramen

class TestProvenientaRamen(unittest.TestCase):
    
    def test_provenienta_contine_japonia(self):
        self.assertIn("Japonia", provenienta_ramen())
        
    def test_provenienta_contine_chineza(self):
        self.assertIn("chinez", provenienta_ramen())
        
    def test_provenienta_not_empty(self):
        self.assertTrue(len(provenienta_ramen()) > 0)

class TestIngredienteRamen(unittest.TestCase):

    def test_ingrediente_contine_taitei(self):
        self.assertIn("Tăiței", ingrediente_ramen())
        
    def test_ingrediente_contine_carne(self):
        self.assertIn("carne", ingrediente_ramen())
        
    def test_ingrediente_not_empty(self):
        self.assertTrue(len(ingrediente_ramen()) > 0)

class TestPreparareRamen(unittest.TestCase):
        
    def test_preparare_contine_supa(self):
        self.assertIn("Supa", preparare_ramen())

    def test_preparare_contine_taitei(self):
        self.assertIn("Tăițeii", preparare_ramen())

    def test_preparare_not_empty(self):
        self.assertTrue(len(preparare_ramen()) > 0)

if __name__ == '__main__':
    unittest.main()

