from app import app

def test_home_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Text Classifier" in response.data
