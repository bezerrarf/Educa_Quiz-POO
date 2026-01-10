from src.dao.connection import DBConnection
from src.models.pergunta import Pergunta

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
            # Reconstrói o objeto Pergunta a partir do DB
            p = Pergunta(
                id=row[0],
                enunciado=row[1],
                alternativas=row[2].split("|"),
                correta_idx=row[3],
                dificuldade=row[4],
                tema=row[5]
            )
            lista_objs.append(p)
        return lista_objs