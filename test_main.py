from main import root
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello folks!"}

def test2():
    response = client.get("/movie/lion king")
    assert response.status_code == 200
    assert response.json() == ['The Lion King', 'Lion King', 'Lion King', 'Untitled Lion King Prequel', 'Lion Kingdom', 'Lion King - Free Healthcare', 'Lion King - Behind the Scenes', 'Lion King: Adventure at Pride Rock', 'The Lion King', 'The Scorpion King', 'The Lion King', "The Lion King II: Simba's Pride", 'The Lion King', 'The Lion King 3: Hakuna Matata', 'The Lion Guard Drama King', 'Simba: The King Lion', 'The Lion King 1½', 'Jason King', 'The Making of the Lion King', 'The Lion King Read-Along']
