class Pergunta:
    """
    Representa uma questão individual do quiz, contendo validações de integridade
    para alternativas e respostas corretas.
    """

    def __init__(self, id: int, enunciado: str, alternativas: list, correta_idx: int, dificuldade: str, tema: str):
        self.id = id
        self.enunciado = enunciado
        self._alternativas = None
        self.alternativas = alternativas # Aciona validação setter
        self._correta_idx = None
        self.correta_idx = correta_idx   # Aciona validação setter
        self.dificuldade = dificuldade
        self.tema = tema

    @property
    def alternativas(self):
        return self._alternativas

    @alternativas.setter
    def alternativas(self, valor: list):
        """
        Define as alternativas da pergunta.
        
        Raises:
            ValueError: Se o número de alternativas for menor que 3 ou maior que 5.
        """
        if not (3 <= len(valor) <= 5):
            raise ValueError("A pergunta deve ter entre 3 e 5 alternativas.")
        self._alternativas = valor

    @property
    def correta_idx(self):
        return self._correta_idx

    @correta_idx.setter
    def correta_idx(self, valor: int):
        """
        Define o índice da resposta correta.

        Raises:
            ValueError: Se o índice estiver fora do intervalo da lista de alternativas.
        """
        if not (0 <= valor < len(self.alternativas)):
            raise ValueError("Índice da resposta inválido.")
        self._correta_idx = valor

    def __str__(self):
        return f"{self.enunciado} ({self.dificuldade})"
    