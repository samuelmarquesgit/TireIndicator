import pytest
from app.services import RecommendationEngine

def test_recommendation_sedan():
    veiculo = {"categoria": "Sedan"}
    pneus = RecommendationEngine.recommend_tires(veiculo)
    assert len(pneus) > 0
    assert pneus[0]["largura"] == 205
    assert pneus[0]["aro"] == "R16"

def test_recommendation_suv():
    veiculo = {"categoria": "SUV"}
    pneus = RecommendationEngine.recommend_tires(veiculo)
    assert len(pneus) > 0
    assert pneus[0]["largura"] == 225
    assert pneus[0]["aro"] == "R17"

def test_recommendation_default():
    veiculo = {"categoria": "Desconhecido"}
    pneus = RecommendationEngine.recommend_tires(veiculo)
    assert len(pneus) > 0
    # Deve usar o padrão (sedan)
    assert pneus[0]["largura"] == 205
