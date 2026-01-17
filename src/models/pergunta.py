from abc import ABC, abstractmethod 
 
class Questao(ABC): 
    """Classe Pai Abstrata.""" 
    def __init__(self, id, enunciado, dificuldade, tema): 
        self.id = id 
        self.enunciado = enunciado 
        self.dificuldade = dificuldade 
        self.tema = tema 
 
    @abstractmethod 
    def validar_resposta(self, resposta): 
        """Cada tipo de questão valida de um jeito.""" 
        pass 
 
    def __str__(self): 
        return f"[{self.tema}] {self.enunciado}" 
 
class QuestaoMultiplaEscolha(Questao): 
    """Implementação concreta com alternativas.""" 
    def __init__(self, id, enunciado, alternativas, correta_idx, dificuldade, tema): 
        super().__init__(id, enunciado, dificuldade, tema) 
        self._alternativas = None 
        self.alternativas = alternativas 
        self._correta_idx = None 
        self.correta_idx = correta_idx 
 
    @property 
    def alternativas(self): 
        return self._alternativas 
 
    @alternativas.setter 
    def alternativas(self, valor): 
        if not (3 <= len(valor) <= 5): 
            raise ValueError("A questão deve ter entre 3 e 5 alternativas.") 
        self._alternativas = valor 
 
    @property 
    def correta_idx(self): 
        return self._correta_idx 
 
    @correta_idx.setter 
    def correta_idx(self, valor): 
        if not (0 <= valor < len(self.alternativas)): 
            raise ValueError("Índice da resposta inválido.") 
        self._correta_idx = valor 
 
    def validar_resposta(self, indice_escolhido): 
        """Implementação específica da validação.""" 
        return int(indice_escolhido) == self.correta_idx 
    
        
