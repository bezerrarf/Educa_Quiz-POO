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
from src.views.admin_page import show_admin_view
from src.controllers.game_controller import GameController

# Inicializa Banco (Felipe)
DBConnection.init_db()

st.set_page_config(page_title="Educa Quiz", page_icon="🎓", layout="centered")

# Estilo para botões grandes
st.markdown("""
<style>
div.stButton > button:first-child { width: 100%; height: 60px; font-size: 20px; }
</style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- ROTA HOME ---
if st.session_state.page == 'home':
    st.title("Educa Quiz 🎓")
    st.markdown("""
    **Bem-vindo ao Sistema de Avaliação ObjectFlow.**
    
    Esta aplicação utiliza conceitos avançados de POO e arquitetura MVC para oferecer 
    quizzes dinâmicos. Teste seus conhecimentos com questões aleatórias e receba 
    feedback imediato sobre seu desempenho.
    """) 
    
    st.divider()
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("👤 USUÁRIO"):
            st.session_state.page = 'usuario'
            st.rerun()
        st.write("")
        if st.button("⚙️ ADMINISTRAÇÃO"):
            st.session_state.page = 'admin'
            st.rerun()

# --- ROTA USUÁRIO ---
elif st.session_state.page == 'usuario':
    if st.button("⬅️ Voltar"):
        st.session_state.page = 'home'
        st.rerun()
    
    # Carrega Quiz Randômico (Lógica da Samira)
    if 'quiz_atual' not in st.session_state:
        config = GameController.carregar_configuracoes()
        perguntas_db = PerguntaDAO.listar_todas() # Busca dados (Felipe)
        
        quiz = Quiz("Conhecimentos Gerais")
        for p in perguntas_db:
            quiz.adicionar_pergunta(p)
            
        quiz.preparar_rodada(config['qtd_perguntas_quiz']) # Embaralha
        st.session_state.quiz_atual = quiz
        
    show_quiz_view(st.session_state.quiz_atual)

# --- ROTA ADMIN ---
elif st.session_state.page == 'admin':
    if st.button("⬅️ Voltar"):
        st.session_state.page = 'home'
        st.rerun()
    show_admin_view()