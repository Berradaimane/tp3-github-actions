import pytest
from app.web import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()
def test_api_message_normal(client):
    reponse = client.post(
        "/moderate",
        json={"message": "bonjour"}
    )

    assert reponse.status_code == 200
    assert reponse.get_json() == {"decision": "autoriser"}
def test_api_message_spam(client):
    reponse = client.post(
        "/moderate",
        json={"message": "ceci est du SPAM"}
    )

    assert reponse.status_code == 200
    assert reponse.get_json() == {"decision": "bloquer"}    
@pytest.mark.parametrize("donnees", [
    {},
    {"message": 42},
])
def test_api_message_invalide(client, donnees):
    reponse = client.post("/moderate", json=donnees)

    assert reponse.status_code == 400
    assert reponse.get_json() == {"error": "Invalid message"}   
def test_api_message_espace(client):
    reponse = client.post(
        "/moderate",
        json={"message": " "}
    )

    assert reponse.status_code == 400
    assert reponse.get_json() == {"error": "Invalid message"}    
def test_api_corps_json_liste(client):
    reponse = client.post(
        "/moderate",
        json=["bonjour"]
    )

    assert reponse.status_code == 400
    assert reponse.get_json() == {"error": "JSON object required"}     