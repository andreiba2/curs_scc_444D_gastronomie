from gastronomie import app

def test_status_tema():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_continut_margherita():
    client = app.test_client()
    response = client.get('/margherita')
    assert b"Margherita" in response.data
