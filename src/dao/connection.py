import sqlite3
import os
DB_PATH = os.path.join("data", "quiz.db")
class DBConnection:

# Gerencia a conexão com o banco SQLite e a inicialização da estrutura de tabelas.

    @staticmethod
    def get_connection():
    # Cria e retorna uma conexão com o banco de dados configurado.
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        return sqlite3.connect(DB_PATH)
    @staticmethod
    def init_db():

    # Cria a tabela 'perguntas' se não existir e popula com dados iniciais (Seed)
    # caso a tabela esteja vazia.

        conn = DBConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS perguntas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                enunciado TEXT NOT NULL,
                alternativas TEXT NOT NULL,
                correta_idx INTEGER NOT NULL,
                dificuldade TEXT NOT NULL,
                tema TEXT NOT NULL
            )
        ''')
        # Seed inicial
        cursor.execute('SELECT count(*) FROM perguntas')
        if cursor.fetchone()[0] == 0:
            questions = [
                ("Qual a capital da França?", "Londres|Paris|Berlim|Madri", 1, "FACIL", "Geografia"),
                ("Elemento químico do Oxigênio?", "O|H|N|He", 0, "FACIL", "Química"),
                ("Quem escreveu Dom Casmurro?", "Machado de Assis|Jorge Amado|Clarice Lispector", 0, "MEDIO",
                "Literatura"),
                ("Qual o maior planeta do sistema solar?", "Terra|Marte|Júpiter|Saturno", 2, "MEDIO", "Astronomia"),
                ("Valor aproximado de Pi?", "3.10|3.12|3.14|3.16", 2, "FACIL", "Matemática")
            ]
            cursor.executemany('''
                INSERT INTO perguntas (enunciado, alternativas, correta_idx, dificuldade, tema)
                VALUES (?, ?, ?, ?, ?)
                ''', questions)
            conn.commit()
            print("Banco inicializado com 5 perguntas padrão.")
        conn.close()