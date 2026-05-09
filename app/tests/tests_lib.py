import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.lib.biblioteca_tortilla import origine_tortilla, ingrediente_tortilla, preparare_tortilla

class TestBiblioteca(unittest.TestCase):

    def test_origine(self):
        self.assertEqual(
            origine_tortilla(),
            "Tortilla de patatas provine din Spania si este un preparat traditional al bucatariei spaniole."
        )

    def test_ingrediente(self):
        self.assertEqual(
            ingrediente_tortilla(),
            "Ingredientele principale sunt cartofii, ouale, ceapa, amestec de branzeturi, uleiul de masline, sarea si piperul."
        )

    def test_preparare(self):
        self.assertEqual(
            preparare_tortilla(),
            "Cartofii se prajesc usor, se amesteca cu ouale si ceapa, apoi se gateste compozitia in tigaie pe ambele parti."
        )

if __name__ == "__main__":
    unittest.main()
