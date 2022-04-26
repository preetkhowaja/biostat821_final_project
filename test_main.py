from main import root
from main import movie
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello folks!"}

def test2():
    response = client.get("/movie/lion king")
    assert response.json() == emp_list
