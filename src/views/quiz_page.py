import streamlit as st
from src.controllers.game_controller import GameController

def show_quiz_view(quiz_obj):
    """
    Renderiza a interface do Quiz utilizando componentes do Streamlit.
    Gerencia o estado das respostas e invoca o cálculo final de pontuação.

    Args:
        quiz_obj (Quiz): Objeto contendo a lista de perguntas a serem exibidas.
    """
    st.header(f"📝 {quiz_obj.titulo}")
    
    if 'respostas' not in st.session_state:
        st.session_state.respostas = {}
        
    acertos = []
    
    # Itera sobre o objeto Quiz (usando o __iter__ definido no Model)
    for i, pergunta in enumerate(quiz_obj):
        st.subheader(f"Q{i+1}: {pergunta.enunciado}")
        st.caption(f"Dificuldade: {pergunta.dificuldade} | Tema: {pergunta.tema}")
        
        escolha = st.radio(
            "Escolha uma opção:", 
            pergunta.alternativas, 
            key=f"q_{pergunta.id}",
            index=None
        )
        
        if escolha:
            idx_escolhido = pergunta.alternativas.index(escolha)
            if idx_escolhido == pergunta.correta_idx:
                if pergunta not in acertos:
                    acertos.append(pergunta)

    st.markdown("---")
    if st.button("Finalizar e Ver Nota"):
        pontuacao = GameController.calcular_pontuacao(acertos)
        st.success(f"🎉 Quiz Finalizado! Sua Pontuação Total: **{pontuacao} pontos**")
        st.balloons()
        