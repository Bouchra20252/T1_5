"""Tests d'intégration : démarrage et comportement de l'API."""

from pathlib import Path

import pytest

MODELE = Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"
pytestmark = pytest.mark.skipif(
    not MODELE.exists(),
    reason="modèle non produit : python src/train.py",
)


def test_demarrage_reel_charge_le_modele():
    """D.1 : le lifespan charge réellement le modèle."""
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        reponse = client.get("/health")

    assert reponse.status_code == 200
    assert "TP2" in reponse.json()["model"]


def test_modele_absent_refuse_demarrage(monkeypatch, tmp_path):
    """D.2 : l'API refuse de démarrer si le modèle est absent."""
    from fastapi.testclient import TestClient

    import predict as predict_module
    from api.main import app

    predict_module.charger_modele.cache_clear()
    monkeypatch.setattr(
        predict_module,
        "MODELE",
        tmp_path / "modele_inexistant.joblib",
    )

    with pytest.raises(FileNotFoundError):
        with TestClient(app):
            pass

    predict_module.charger_modele.cache_clear()


def test_modele_non_charge_retourne_503(monkeypatch):
    """D.3 : les endpoints renvoient 503 sans classifier."""
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        monkeypatch.setattr(app.state, "classifier", None)

        assert client.get("/health").status_code == 503
        assert client.post(
            "/predict",
            json={"text": "Excellent produit"},
        ).status_code == 503


@pytest.mark.parametrize(
    "exception",
    [
        RuntimeError("panne du modèle"),
        ValueError("bug interne"),
    ],
)
def test_erreur_prediction_retourne_500_sans_details(monkeypatch, exception):
    """D.4 : les erreurs internes ne sont jamais exposées au client."""
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        classifier = app.state.classifier

        def prediction_en_erreur(text):
            raise exception

        monkeypatch.setattr(classifier, "predict", prediction_en_erreur)

        reponse = client.post(
            "/predict",
            json={"text": "Excellent produit"},
        )

        assert reponse.status_code == 500
        assert str(exception) not in reponse.text
        assert "Erreur interne du serveur" in reponse.text



def test_classes_inattendues_refusent_demarrage(monkeypatch):
    """E.3 : le démarrage est refusé si le modèle contient une classe inconnue."""
    import api.model as model_module

    class FauxModele:
        classes_ = ["negative", "positive", "neutral"]

    monkeypatch.setattr(
        model_module,
        "charger_modele",
        lambda: FauxModele(),
    )

    with pytest.raises(ValueError, match="Classes du modèle inattendues"):
        model_module.SentimentClassifier()

















