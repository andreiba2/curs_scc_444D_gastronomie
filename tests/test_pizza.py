import unittest, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.lib.biblioteca_gastronomie import origine_pizza, descriere_pizza
from gastronomie import app

class TestBiblioteca(unittest.TestCase):
    def test_origine_not_empty(self):
        self.assertGreater(len(origine_pizza()), 0)
    def test_origine_contine_napoli(self):
        self.assertIn("Napoli", origine_pizza())
    def test_origine_contine_italia(self):
        self.assertIn("Italia", origine_pizza())
    def test_descriere_not_empty(self):
        self.assertGreater(len(descriere_pizza()), 0)
    def test_descriere_contine_aluat(self):
        self.assertIn("aluat", descriere_pizza())
    def test_descriere_contine_mozzarella(self):
        self.assertIn("mozzarella", descriere_pizza())

class TestRute(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
    def test_index(self):
        self.assertEqual(self.client.get('/').status_code, 200)
    def test_pizza(self):
        self.assertEqual(self.client.get('/pizza').status_code, 200)
    def test_origine(self):
        self.assertEqual(self.client.get('/origine_pizza').status_code, 200)
    def test_descriere(self):
        self.assertEqual(self.client.get('/descriere_pizza').status_code, 200)

if __name__ == '__main__':
    unittest.main()
