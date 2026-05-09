import unittest
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.lib.biblioteca_gastronomie import reteta_mici, descriere_mici

class TestMici(unittest.TestCase):

    def test_reteta_not_empty(self):
        self.assertGreater(len(reteta_mici()), 0)

    def test_reteta_contine_carne(self):
        self.assertIn("carne", reteta_mici().lower())

    def test_descriere_not_empty(self):
        self.assertGreater(len(descriere_mici()), 0)

    def test_descriere_contine_romanesc(self):
        self.assertIn("romanesc", descriere_mici().lower())

if __name__ == '__main__':
    unittest.main()
