import unittest
from gastronomie import app

class TestGastronomie(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_ruta_tema(self):
        raspuns = self.app.get('/')
        self.assertEqual(raspuns.status_code, 200)
        self.assertIn(b'Gastronomie', raspuns.data)

    def test_ruta_element(self):
        raspuns = self.app.get('/paella')
        self.assertEqual(raspuns.status_code, 200)
        self.assertIn(b'Paella', raspuns.data)

    def test_ruta_ingrediente(self):
        raspuns = self.app.get('/paella/ingrediente')
        self.assertEqual(raspuns.status_code, 200)
        self.assertIn(b'Orez bomba', raspuns.data)

    def test_ruta_preparare(self):
        raspuns = self.app.get('/paella/preparare')
        self.assertEqual(raspuns.status_code, 200)
        self.assertIn(b'socarrat', raspuns.data)

if __name__ == '__main__':
    unittest.main()
