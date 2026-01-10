import json
import os

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
            with open(caminho, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"pesos_dificuldade": {"FACIL": 1, "MEDIO": 2, "DIFICIL": 3}}

    @staticmethod
    def calcular_pontuacao(perguntas_acertadas: list) -> int:
        """
        Calcula a pontuação total do usuário baseada nos pesos de dificuldade.
        Args:
            perguntas_acertadas (list): Lista de objetos Pergunta que o usuário acertou.
        Returns:
            int: Somatório total dos pontos.
        """
        config = GameController.carregar_configuracoes()
        pesos = config.get("pesos_dificuldade", {})
        total = 0
        for p in perguntas_acertadas:
            # Obtém o peso da dificuldade, padrão 1 se não definido
            total += pesos.get(p.dificuldade, 1)
        return total
