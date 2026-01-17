import pytest
from src.controllers.game_controller import GameController
from src.models.quiz import Quiz
from src.models.pergunta import QuestaoMultiplaEscolha

# Fixture: Cria dados falsos para usar nos testes
@pytest.fixture
def quiz_populado():
    q = Quiz("Quiz Teste")
    # Adiciona 3 perguntas
    for i in range(3):
        p = QuestaoMultiplaEscolha(i, f"P{i}", ["A","B","C"], 0, "FACIL", "Geral")
        q.adicionar_pergunta(p)
    return q

# --- TESTES DO CONTROLLER ---

def test_calculo_aprovacao_sucesso():
    """7 acertos em 10 (70%) não aprova (precisa ser > 70%)."""
    # Cenário: 70% exato
    perc, aprovado, msg = GameController.calcular_resultado(acertos=7, total_perguntas=10)
    assert perc == 70.0
    assert aprovado is False # A regra diz > 70%, então 70% reprova

def test_calculo_aprovacao_passou():
    """8 acertos em 10 (80%) deve aprovar."""
    perc, aprovado, msg = GameController.calcular_resultado(acertos=8, total_perguntas=10)
    assert perc == 80.0
    assert aprovado is True
    assert "Parabéns" in msg

def test_divisao_por_zero():
    """Não pode quebrar o sistema se o total de perguntas for 0."""
    perc, aprovado, msg = GameController.calcular_resultado(acertos=0, total_perguntas=0)
    assert perc == 0
    assert aprovado is False
    assert "Sem perguntas" in msg

# --- TESTES DA CLASSE QUIZ (RANDOMIZAÇÃO) ---

def test_quiz_preparar_rodada_limite(quiz_populado):
    """
    Se pedirmos 10 perguntas, mas o quiz só tem 3, 
    ele não pode dar erro, deve retornar as 3 disponíveis.
    """
    # O quiz da fixture tem 3 perguntas. Pedimos 10.
    quiz_populado.preparar_rodada(quantidade=10)
    
    # O tamanho do quiz deve ser ajustado para 3, não 10 (evita erro)
    assert len(quiz_populado) == 3 

def test_quiz_acesso_item(quiz_populado):
    """Testa se o método __getitem__ funciona (acesso por índice)."""
    quiz_populado.preparar_rodada(1)
    # Deve conseguir acessar como lista
    pergunta = quiz_populado[0]
    assert isinstance(pergunta, QuestaoMultiplaEscolha)