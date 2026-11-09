import pytest
from unittest.mock import patch
from app.surveillance import surveiller


def test_surveillance_taux_eleve():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.15)

        assert resultat == "alerte"
        notifier.assert_called_once_with("Taux eleve")
def test_surveillance_taux_faible():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.05)

        assert resultat == "ok"
        notifier.assert_not_called()      
def test_surveillance_taux_exactement_seuil():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.10)

        assert resultat == "ok"
        notifier.assert_not_called()    
def test_surveillance_propage_erreur_notification():
    with patch("app.surveillance.envoyer_notification") as notifier:
        notifier.side_effect = RuntimeError("Service indisponible")

        with pytest.raises(RuntimeError, match="Service indisponible"):
            surveiller(0.15)

        notifier.assert_called_once_with("Taux eleve")              