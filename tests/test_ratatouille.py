from app.lib.biblioteca_gastronomie import descriere_ratatouille, origine_ratatouille

def test_descriere_ratatouille():
    assert b"rosii" in descriere_ratatouille()
    assert b"ardei" in descriere_ratatouille()
    assert b"Ratatouille" in descriere_ratatouille()
    
def test_origine_ratatouille():
    assert b"Proventa" in origine_ratatouille()
    assert b"sudul Frantei" in origine_ratatouille()
