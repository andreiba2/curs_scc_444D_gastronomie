import unittest
from gastronomie import app
from app.lib.biblioteca_gastronomie import (
    provenienta_chilli_con_carne,
    ingrediente_chilli_con_carne,
    preparare_chilli_con_carne
)


class TestBibliotecaGastronomie(unittest.TestCase):
    """Teste pentru functiile din biblioteca."""

    def test_provenienta_returneaza_string(self):
        rezultat = provenienta_chilli_con_carne()
        self.assertIsInstance(rezultat, str)
        self.assertGreater(len(rezultat), 0)

    def test_provenienta_contine_texas(self):
        rezultat = provenienta_chilli_con_carne()
        self.assertIn("Texas", rezultat)

    def test_ingrediente_returneaza_string(self):
        rezultat = ingrediente_chilli_con_carne()
        self.assertIsInstance(rezultat, str)
        self.assertGreater(len(rezultat), 0)

    def test_ingrediente_contine_carne(self):
        rezultat = ingrediente_chilli_con_carne()
        self.assertIn("Carne", rezultat)

    def test_preparare_returneaza_string(self):
        rezultat = preparare_chilli_con_carne()
        self.assertIsInstance(rezultat, str)
        self.assertGreater(len(rezultat), 0)


class TestRuteFlask(unittest.TestCase):
    """Teste pentru rutele aplicatiei Flask."""

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_pagina_principala(self):
        response = self.client.get('/gastronomie')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Chilli con carne', response.data)

    def test_ruta_chilli_con_carne(self):
        response = self.client.get('/chilli_con_carne')
        self.assertEqual(response.status_code, 200)

    def test_ruta_provenienta(self):
        response = self.client.get('/chilli_con_carne/provenienta')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Texas', response.data)

    def test_ruta_ingrediente(self):
        response = self.client.get('/chilli_con_carne/ingrediente')
        self.assertEqual(response.status_code, 200)

    def test_ruta_preparare(self):
        response = self.client.get('/chilli_con_carne/preparare')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
