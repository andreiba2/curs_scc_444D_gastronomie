import unittest
from gastronomie import app
from app.lib.biblioteca_gastronomie import text_provenienta, text_ingrediente, text_preparare

class TestGastronomie(unittest.TestCase):
    
    # --- TESTELE TALE (Logica) ---
    def test_provenienta_text(self):
        self.assertIn("Italia", text_provenienta())
    
    def test_ingrediente_text(self):
        self.assertIn("Guanciale", text_ingrediente())

    # --- TESTELE "STIL COLEG" (Rute Web) ---
    def setUp(self):
        self.client = app.test_client()

    def test_home_route(self):
        response = self.client.get('/gastronomie')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Carbonara", response.get_data(as_text=True))

    def test_provenienta_route(self):
        response = self.client.get('/provenienta')
        self.assertEqual(response.status_code, 200)

    def test_ingrediente_route(self):
        response = self.client.get('/ingrediente')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
