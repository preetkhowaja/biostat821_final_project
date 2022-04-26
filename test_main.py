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
def test2():
    response = client.get("/movie/string1?string1=lion king")
    assert response.status_code == 200
    assert response.json() == [
        "Harry",
        "Harry",
        "Harry",
        "Harry Potter and the Sorcerer's Stone",
        "Bosch",
        "Harry Potter and the Goblet of Fire",
        "Harry Potter and the Deathly Hallows: Part 2",
        "The Ipcress File",
        "Barry",
        "Harry Wild",
        "Marry Me",
        "Harry Potter and the Prisoner of Azkaban",
        "Harry Potter and the Chamber of Secrets",
        "Harry Potter and the Order of the Phoenix",
        "The Ultimatum: Marry or Move On",
        "Harry Potter and the Half-Blood Prince",
        "Harry Potter and the Deathly Hallows: Part 1",
        "Dirty Harry",
        "When Harry Met Sally...",
        "Harrow",
    ]
def test3():
    response = client.get("/genre/lion king")
    assert response.status_code == 200
    assert response.json() == [
        'Animation'
    ]
