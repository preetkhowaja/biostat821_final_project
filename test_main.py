from main import root
from main import movie
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == [
        "Hello folks! In order to use the recommendation engine, type one of the following:"
        " Sad, Angry, Anticipating, Horror, Content, Motivated, or Bollywood"
    ]
