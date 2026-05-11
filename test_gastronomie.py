import unittest
from gastronomie import app

class TestGastronomie(unittest.TestCase):

    def setUp(self):
        # Pregătim clientul de testare Flask
        self.client = app.test_client()
        self.client.testing = True

    # RUTA 1: Testare Temă Generală
    def test_home_route(self):
        response = self.client.get('/gastronomie')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Gastronomie", response.get_data(as_text=True))

    # RUTA 2: Testare Element Specific (Carbonara)
    def test_element_route(self):
        response = self.client.get('/gastronomie/carbonara')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Paste Carbonara", response.get_data(as_text=True))

    # RUTA 3: Testare Informație Specifică 1 (Proveniență)
    def test_provenienta_route(self):
        response = self.client.get('/gastronomie/carbonara/provenienta')
        self.assertEqual(response.status_code, 200)

    # RUTA 4: Testare Informație Specifică 2 (Ingrediente)
    def test_ingrediente_route(self):
        response = self.client.get('/gastronomie/carbonara/ingrediente')
        self.assertEqual(response.status_code, 200)
        # Verificăm dacă un ingredient cheie apare în pagină
        self.assertIn("Guanciale", response.get_data(as_text=True))

    # RUTA EXTRA: Mod de preparare
    def test_preparare_route(self):
        response = self.client.get('/gastronomie/carbonara/preparare')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
