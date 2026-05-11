import unittest
from app.lib.biblioteca_gastronomie import provenienta_ramen, ingrediente_ramen, preparare_ramen
from gastronomie import app

class TestBibliotecaRamen(unittest.TestCase):
    
    def test_provenienta_contine_japonia(self):
        self.assertIn("Japonia", provenienta_ramen())
        
    def test_provenienta_contine_chineza(self):
        self.assertIn("chineză", provenienta_ramen().lower())
        
    def test_provenienta_not_empty(self):
        self.assertTrue(len(provenienta_ramen()) > 0)

    def test_ingrediente_contine_taitei(self):
        self.assertIn("Tăiței", ingrediente_ramen())
        
    def test_ingrediente_contine_carne(self):
        self.assertIn("carne", ingrediente_ramen().lower())
        
    def test_ingrediente_not_empty(self):
        self.assertTrue(len(ingrediente_ramen()) > 0)
        
    def test_preparare_contine_supa(self):
        self.assertIn("Supa", preparare_ramen())

class TestRuteRamen(unittest.TestCase):
    def setUp(self):
        # Pregatim clientul de testare Flask
        self.client = app.test_client()

    def test_ruta_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_ruta_ramen(self):
        response = self.client.get('/ramen')
        self.assertEqual(response.status_code, 200)
        
    def test_ruta_provenienta(self):
        response = self.client.get('/ramen/provenienta')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

