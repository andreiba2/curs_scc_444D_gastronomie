from app.lib.biblioteca_gastronomie import descriere_ratatouille, origine_ratatouille

def test_descriere_ratatouille():
    assert "rosii" in descriere_ratatouille()
    assert "ardei" in descriere_ratatouille()
    assert "Ratatouille" in descriere_ratatouille()
    
def test_origine_ratatouille():
    assert "Proventa" in origine_ratatouille()
    assert "sudul Frantei" in origine_ratatouille()
