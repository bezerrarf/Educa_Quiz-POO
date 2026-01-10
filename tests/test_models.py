import pytest
from src.models.pergunta import Pergunta

def test_criacao_pergunta_valida():
    # Deve criar sem erros
    p = Pergunta(1, "Q1", ["A", "B", "C"], 0, "FACIL", "Geral")
    assert p.enunciado == "Q1"
    assert len(p.alternativas) == 3

def test_erro_poucas_alternativas():
    # Deve falhar com 2 alternativas (Mínimo 3)
    with pytest.raises(ValueError):
        Pergunta(1, "Q1", ["A", "B"], 0, "FACIL", "Geral")

def test_erro_indice_invalido():
    # Deve falhar se índice da correta for 3 (pois só tem indices 0, 1, 2)
    with pytest.raises(ValueError):
        Pergunta(1, "Q1", ["A", "B", "C"], 3, "FACIL", "Geral")

        