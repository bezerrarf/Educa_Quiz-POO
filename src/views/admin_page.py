import streamlit as st
import pandas as pd
from src.dao.pergunta_dao import PerguntaDAO
from src.controllers.game_controller import GameController
from src.models.pergunta import QuestaoMultiplaEscolha

def show_admin_view():
    st.header("🛠️ Administração")
    tab1, tab2 = st.tabs(["Banco de Perguntas", "Configurações"])

    with tab1:
        st.caption("Edite as células abaixo e clique em Salvar.")
        perguntas = PerguntaDAO.listar_todas()
        
        # Prepara dados para o editor visual
        data = [{
            "ID": p.id, 
            "Enunciado": p.enunciado, 
            "Tema": p.tema,
            "Dificuldade": p.dificuldade, 
            "Alternativas": "|".join(p.alternativas),
            "Correta_Idx": p.correta_idx
        } for p in perguntas]

        df = pd.DataFrame(data)
        edited_df = st.data_editor(df, num_rows="dynamic", key="data_editor")

        if st.button("💾 Salvar Alterações no Banco"):
            # Processa inserções e edições
            for i, row in edited_df.iterrows():
                try:
                    p = QuestaoMultiplaEscolha(
                        id=row["ID"], 
                        enunciado=row["Enunciado"],
                        alternativas=row["Alternativas"].split("|"),
                        correta_idx=int(row["Correta_Idx"]),
                        dificuldade=row["Dificuldade"], 
                        tema=row["Tema"]
                    )
                    
                    # Se ID é NaN (vazio no editor), é novo registro
                    if pd.isna(row["ID"]):
                        PerguntaDAO.salvar_nova(p)
                    else:
                        PerguntaDAO.atualizar(p)
                        
                except Exception as e:
                    st.error(f"Erro na linha {i}: {e}")
            
            st.success("Banco atualizado!")
            st.rerun()

    with tab2:
        cfg = GameController.carregar_configuracoes()
        new_time = st.number_input("Tempo (min)", value=cfg.get("tempo_limite_minutos", 5))
        new_qtd = st.number_input("Qtd Perguntas", value=cfg.get("qtd_perguntas_quiz", 5))

        if st.button("Atualizar Configs"):
            cfg["tempo_limite_minutos"] = new_time
            cfg["qtd_perguntas_quiz"] = new_qtd
            GameController.salvar_configuracoes(cfg)
            st.success("Configurações salvas!")