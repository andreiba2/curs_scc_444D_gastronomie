import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.tortilla_de_patatas import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_origine(self):
        response = self.app.get('/origine')
        self.assertEqual(response.status_code, 200)

    def test_ingrediente(self):
        response = self.app.get('/ingrediente')
        self.assertEqual(response.status_code, 200)

    def test_preparare(self):
        response = self.app.get('/preparare')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
