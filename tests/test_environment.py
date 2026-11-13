"""Tests de cohérence de l'environnement Python."""

from pathlib import Path


def test_requirements_pins_versions(root: Path):
    lines = [
        ligne.strip()
        for ligne in (root / "requirements.txt").read_text().splitlines()
    ]
    lines = [ligne for ligne in lines if ligne and not ligne.startswith("#")]

    assert lines, "requirements.txt est vide"

    for line in lines:
        assert "==" in line, f"Dépendance sans version épinglée : {line}"