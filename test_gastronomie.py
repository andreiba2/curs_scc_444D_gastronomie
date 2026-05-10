import unittest
from gastronomie import descriere_brasovence, ingrediente_brasovence

class TestBrasovence(unittest.TestCase):
	def test_descriere(self):
	    rezultat = descriere_brasovence()
	    self.assertIn("clatite", rezultat)

	def test_ingrediente(self):
	    rezultat = ingrediente_brasovence()
	    self.assertIn("carne", rezultat)

if __name__ == '__main__':
    unittest.main()
