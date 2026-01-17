import streamlit as st
import time
from src.controllers.game_controller import GameController

def show_quiz_view(quiz_obj):
    # --- TELA 1: PREPARAÇÃO ---
    if 'quiz_iniciado' not in st.session_state:
        st.title("⏱️ Preparação")
        st.subheader("Você está pronto?")
        
        tempo = GameController.carregar_configuracoes()['tempo_limite_minutos']
        st.write(f"Você terá **{tempo} minutos** para responder.")
        
        if st.button("Sim, iniciar agora!"):
            st.session_state.quiz_iniciado = True
            st.session_state.start_time = time.time()
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.rerun()
        return

    # --- TELA 2: QUIZ EM ANDAMENTO ---
    tempo_limite_sec = GameController.carregar_configuracoes()['tempo_limite_minutos'] * 60
    tempo_decorrido = time.time() - st.session_state.start_time
    restante = tempo_limite_sec - tempo_decorrido

    # Timer Superior Direito
    col1, col2 = st.columns([4, 1])
    
    # Evita divisão por zero se a lista for vazia (proteção opcional)
    total_questions = len(quiz_obj) if len(quiz_obj) > 0 else 1
    col1.progress((st.session_state.q_index) / total_questions)

    if restante > 0:
        mins, secs = divmod(int(restante), 60)
        col2.metric("Tempo", f"{mins:02d}:{secs:02d}")
    else:
        st.error("Tempo Esgotado!")
        st.session_state.q_index = len(quiz_obj)  # Força fim do quiz

    # Renderiza Pergunta Atual
    idx = st.session_state.q_index

    if idx < len(quiz_obj):
        pergunta = quiz_obj[idx]
        st.markdown(f"### Q{idx+1}: {pergunta.enunciado}")
        
        with st.form(key=f"q_form_{idx}"):
            escolha = st.radio("Alternativas:", pergunta.alternativas, index=None)
            
            # Botão muda texto na última pergunta
            label_btn = "Finalizar Quiz" if idx == len(quiz_obj) - 1 else "Próxima Pergunta"
            submitted = st.form_submit_button(label_btn)

            if submitted:
                if not escolha:
                    st.warning("Escolha uma opção!")
                else:
                    # Validação usando Polimorfismo (assumindo que sua classe tem esse método)
                    idx_escolhido = pergunta.alternativas.index(escolha)
                    
                    if pergunta.validar_resposta(idx_escolhido):
                        st.session_state.score += 1
                        st.success("Correto! 🎉")
                    else:
                        st.error("Incorreto. ❌")
                    
                    time.sleep(1)  # Pausa para ler feedback
                    st.session_state.q_index += 1
                    st.rerun()

    else:
        # --- TELA 3: RESULTADO ---
        perc, aprovado, msg = GameController.calcular_resultado(st.session_state.score, len(quiz_obj))
        
        if aprovado:
            st.balloons()
            
        st.title("Resultado Final")
        cor = "green" if aprovado else "red"
        
        st.markdown(f"### Desempenho: :{cor}[{perc:.1f}%]")
        st.info(msg)
        
        if st.button("Voltar ao Menu"):
            st.session_state.clear()
            st.rerun()