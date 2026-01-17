import pytest
from src.models.pergunta import QuestaoMultiplaEscolha

# --- CENÁRIOS DE SUCESSO (HAPPY PATH) ---
def test_criacao_questao_valida():
    """Testa se consegue instanciar uma questão com dados corretos."""
    q = QuestaoMultiplaEscolha(
        id=1,
        enunciado="Teste?",
        alternativas=["A", "B", "C"],
        correta_idx=0,
        dificuldade="FACIL",
        tema="Teste"
    )
    assert q.enunciado == "Teste?"
    assert len(q.alternativas) == 3
    assert q.validar_resposta(0) is True  # Polimorfismo funcionando
    assert q.validar_resposta(1) is False

# --- CENÁRIOS DE ERRO (SAD PATH) ---

def test_erro_minimo_alternativas():
    """Deve lançar ValueError se tiver menos de 3 alternativas."""
    with pytest.raises(ValueError) as excinfo:
        QuestaoMultiplaEscolha(
            id=1,
            enunciado="Erro?",
            alternativas=["A", "B"], # Só 2 (Inválido)
            correta_idx=0,
            dificuldade="FACIL",
            tema="Erro"
        )
    assert "entre 3 e 5 alternativas" in str(excinfo.value)

def test_erro_maximo_alternativas():
    """Deve lançar ValueError se tiver mais de 5 alternativas."""
    with pytest.raises(ValueError):
        QuestaoMultiplaEscolha(
            id=1,
            enunciado="Erro?",
            alternativas=["A", "B", "C", "D", "E", "F"], # 6 (Inválido)
            correta_idx=0,
            dificuldade="FACIL",
            tema="Erro"
        )

def test_erro_indice_invalido_out_of_bounds():
    """Deve lançar ValueError se o índice da correta não existir na lista."""
    with pytest.raises(ValueError) as excinfo:
        QuestaoMultiplaEscolha(
            id=1,
            enunciado="Erro?",
            alternativas=["A", "B", "C"], # Índices 0, 1, 2
            correta_idx=5,                # Índice 5 não existe
            dificuldade="FACIL",
            tema="Erro"
        )
    assert "Índice da resposta inválido" in str(excinfo.value)

def test_erro_indice_negativo():
    """Deve lançar ValueError se o índice for negativo (embora Python aceite, nossa regra nega)."""
    with pytest.raises(ValueError):
        QuestaoMultiplaEscolha(
            id=1,
            enunciado="Erro?",
            alternativas=["A", "B", "C"],
            correta_idx=-1,
            dificuldade="FACIL",
            tema="Erro"
        )