"""Raccord entre l'API et le modèle entraîné au TP2."""

import sys
from pathlib import Path
from typing import Literal, TypedDict

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "src"))

from predict import charger_modele  # noqa: E402
from predict import predict as _predict  # noqa: E402

SEUIL_ABSTENTION = 0.60


class SentimentResult(TypedDict):
    label: Literal["POSITIVE", "NEGATIVE", "INDETERMINE"]
    score: float
    text: str


class SentimentClassifier:
    """Enveloppe du modèle TP2 avec l'interface attendue par l'API."""

    model_name = "tfidf-logreg (TP2, models/sentiment.joblib)"

    def __init__(self) -> None:
        classes = set(charger_modele().classes_)
        classes_attendues = {"negative", "positive"}

        if classes != classes_attendues:
            raise ValueError(
                f"Classes du modèle inattendues : {sorted(classes)}"
            )

    def predict(self, text: str) -> SentimentResult:
        """Renvoie une prédiction ou INDETERMINE si la confiance est insuffisante."""
        r = _predict(text)
        score = r["score"]

        correspondance: dict[str, Literal["POSITIVE", "NEGATIVE"]] = {
            "positive": "POSITIVE",
            "negative": "NEGATIVE",
        }

        label: Literal["POSITIVE", "NEGATIVE", "INDETERMINE"] = (
            correspondance[r["label"]]
        )

        if score < SEUIL_ABSTENTION:
            label = "INDETERMINE"

        return {
            "label": label,
            "score": score,
            "text": text[:100],
        }


def load_model() -> SentimentClassifier:
    """Construit le classifier."""
    return SentimentClassifier()