import pytest
from unittest.mock import Mock
from app.moderation import decider


def test_decider_bloquer_spam():
    modele = Mock()
    modele.predict.return_value = "spam"

    resultat = decider(modele, "Offre miracle")

    assert resultat == "bloquer"
    modele.predict.assert_called_once_with("Offre miracle")
def test_decider_autoriser_message_normal():
    modele = Mock()
    modele.predict.return_value = "normal"

    resultat = decider(modele, "Bonjour")

    assert resultat == "autoriser"
    modele.predict.assert_called_once_with("Bonjour")    
def test_decider_propage_erreur_modele():
    modele = Mock()
    modele.predict.side_effect = RuntimeError("Modele indisponible")

    with pytest.raises(RuntimeError, match="Modele indisponible"):
        decider(modele, "Bonjour")    