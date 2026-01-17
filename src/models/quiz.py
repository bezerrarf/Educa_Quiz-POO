import random

class Quiz:
    def __init__(self, titulo):
        self.titulo = titulo
        self._perguntas = []

    def adicionar_pergunta(self, pergunta):
        self._perguntas.append(pergunta)

    def preparar_rodada(self, quantidade):
        """Seleciona N perguntas aleatórias do banco total."""
        if quantidade > len(self._perguntas):
            quantidade = len(self._perguntas)
        # Embaralha e corta a lista
        self._perguntas = random.sample(self._perguntas, quantidade)

    def __len__(self):
        return len(self._perguntas)

    def __getitem__(self, index):
        """Permite acessar quiz[0] diretamente."""
        return self._perguntas[index]