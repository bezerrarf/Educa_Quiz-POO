class Quiz:
    """
    Classe agregadora que compõe um conjunto de perguntas para formar uma avaliação.
    Implementa o protocolo de iteração do Python.
    """
    def __init__(self, titulo: str):
        self.titulo = titulo
        self._perguntas = []

    def adicionar_pergunta(self, pergunta):
        """Adiciona um objeto Pergunta à lista interna do quiz."""
        self._perguntas.append(pergunta)

    def __len__(self):
        """Permite usar len(quiz) para saber o total de questões."""
        return len(self._perguntas)

    def __iter__(self):
        """Permite iterar diretamente sobre o objeto: 'for p in quiz:'"""
        return iter(self._perguntas)
    