"""
Para executar a aplicação, verifique se o UV está corretamente instalado.

Ative o vitual Env no terminal use o comando no linux (ou Codespace):
-> source .venv/bin/activate

No CMD do windows:
-> source .venv/bin/activate.bat

Execute o comando do Streamlit via terminal:
-> streamlit run app.py

Abra no navegador ou use o codigo http

"""

import streamlit as st
from src.dao.connection import DBConnection
from src.dao.pergunta_dao import PerguntaDAO
from src.models.quiz import Quiz
from src.views.quiz_page import show_quiz_view

# Inicialização do Banco (Responsabilidade do Felipe sendo chamada na raiz)
DBConnection.init_db()

st.set_page_config(page_title="Educa Quiz - ObjectFlow", layout="centered", page_icon="🎓")

# Navegação Lateral
st.sidebar.title("Navegação")
page = st.sidebar.radio("Ir para:", ["Home", "Responder Quiz"])

if page == "Home":
    st.title("Bem-vindo ao Educa Quiz 🎓")
    
    # --- CONTEXTO SOLICITADO (MAX 250 CARACTERES) ---
    st.markdown("""
    > **Sobre a Aplicação:**
    > 
    > Sistema educacional desenvolvido pela equipe **ObjectFlow** para avaliação de competências. 
    > Utiliza arquitetura modular (MVC) e persistência em SQLite para gerenciar quizzes dinâmicos, 
    > calculando métricas de desempenho baseadas em níveis de dificuldade configuráveis.
    """)
    
    st.divider()
    st.info("👈 Selecione 'Responder Quiz' no menu lateral para iniciar.")

elif page == "Responder Quiz":
    # Fluxo de carregamento e exibição
    perguntas_db = PerguntaDAO.listar_todas()
    
    # Construção do objeto Quiz (Marcus)
    quiz = Quiz("Avaliação de Conhecimentos Gerais")
    for p in perguntas_db:
        quiz.adicionar_pergunta(p)
        
    # Renderização da View (Thierry)
    show_quiz_view(quiz)
