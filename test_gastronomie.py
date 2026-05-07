from gastronomie import app

def test_status_provenienta():
    client = app.test_client()
    response = client.get('/margherita/provenienta')
    assert response.status_code == 200
    assert b"Italia" in response.data

def test_status_ingrediente():
    client = app.test_client()
    response = client.get('/margherita/ingrediente')
    assert response.status_code == 200
    assert b"mozzarella" in response.data

def test_status_preparare():
    client = app.test_client()
    response = client.get('/margherita/preparare')
    assert response.status_code == 200
    assert b"cuptor" in response.data
