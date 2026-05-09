import unittest

def reteta_mici():
    return (
        "Reteta mici: 500g carne de vita, 200g carne de porc, "
        "1 lingurita bicarbonat, usturoi, cimbru, piper, sare. "
        "Se amesteca bine, se formeaza micii si se grileaza."
    )

def descriere_mici():
    return (
        "Micii sunt un preparat traditional romanesc, "
        "sub forma de chiftele alungite fara invelis, "
        "preparate din carne tocata amestecata cu condimente."
    )

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
