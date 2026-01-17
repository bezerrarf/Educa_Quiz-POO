from src.dao.connection import DBConnection
from src.models.pergunta import QuestaoMultiplaEscolha

class PerguntaDAO:
    @staticmethod
    def listar_todas():
        conn = DBConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM perguntas')
        rows = cursor.fetchall()
        conn.close()
        
        lista_objs = []
        for row in rows:
            p = QuestaoMultiplaEscolha(
                id=row[0], 
                enunciado=row[1],
                alternativas=row[2].split("|"),
                correta_idx=row[3], 
                dificuldade=row[4], 
                tema=row[5]
            )
            lista_objs.append(p)
        return lista_objs

    @staticmethod
    def salvar_nova(pergunta):
        conn = DBConnection.get_connection()
        cursor = conn.cursor()
        alts = "|".join(pergunta.alternativas)
        sql = "INSERT INTO perguntas (enunciado, alternativas, correta_idx, dificuldade, tema) VALUES (?,?,?,?,?)"
        cursor.execute(sql, (pergunta.enunciado, alts, pergunta.correta_idx, pergunta.dificuldade, pergunta.tema))
        conn.commit()
        conn.close()

    @staticmethod
    def atualizar(pergunta):
        conn = DBConnection.get_connection()
        cursor = conn.cursor()
        alts = "|".join(pergunta.alternativas)
        # A linha do SQL abaixo foi unificada para evitar erros de sintaxe
        sql = "UPDATE perguntas SET enunciado=?, alternativas=?, correta_idx=?, dificuldade=?, tema=? WHERE id=?"
        cursor.execute(sql, (pergunta.enunciado, alts, pergunta.correta_idx, pergunta.dificuldade, pergunta.tema, pergunta.id))
        conn.commit()
        conn.close()