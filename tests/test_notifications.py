import pytest
from app.notifications import envoyer_notification


def test_notification_service_non_configure():
    with pytest.raises(RuntimeError) as erreur:
        envoyer_notification("Taux eleve")

    assert str(erreur.value) == "Service non configure"