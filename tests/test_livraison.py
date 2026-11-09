import pytest
from app.livraison import frais_livraison


def test_livraison_panier_ordinaire():
    # Arrange : préparer
    montant = 120

    # Act : appeler
    resultat = frais_livraison(montant)

    # Assert : vérifier
    assert resultat == 25


