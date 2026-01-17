import json
import os

 
SETTINGS_PATH = os.path.join("config", "settings.json")

class GameController:
    """
    Controlador principal responsável pela orquestração das regras de negócio globais
    e comunicação com arquivos de configuração.
    """

    @staticmethod
    def carregar_configuracoes() -> dict:
        """
        Lê o arquivo JSON de configurações definido em config/settings.json.
        Returns:
            dict: Dicionário contendo configurações como pesos e limites.
            Retorna configurações padrão (fallback) caso o arquivo não seja encontrado.
        """
        caminho = os.path.join("config", "settings.json")
        try:
            with open(SETTINGS_PATH, 'r', encoding='utf-8') as f: 
                return json.load(f) 
        except FileNotFoundError: 
            return {"tempo_limite_minutos": 5, "qtd_perguntas_quiz": 5} 
 
    @staticmethod 
    def salvar_configuracoes(novas_configs): 
        with open(SETTINGS_PATH, 'w', encoding='utf-8') as f: 
            json.dump(novas_configs, f, indent=4) 
 
    @staticmethod 
    def calcular_resultado(acertos, total_perguntas): 
        """Regra de Negócio: Aprovação se acertos > 70%.""" 
        if total_perguntas == 0: 
            return 0, False, "Sem perguntas." 
         
        percentual = (acertos / total_perguntas) * 100 
        aprovado = percentual > 70 
         
        msg = "Parabéns! Você domina o assunto." if aprovado else "Estude mais e tente novamente na próxima." 
        return percentual, aprovado, msg


