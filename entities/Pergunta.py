
from typing import Tuple

from entities.Entity_error import ParamNotValidated

class Pergunta:
    enunciado: str
    alternativas: str
    resposta_correta: str

    def __init__(self, enunciado: str=None, alternativas: str=None, resposta_correta: str=None):
        valida_enunciado = self.validate_enunciado(enunciado)
        if valida_enunciado[0] == False:
            raise ParamNotValidated("enunciado", valida_enunciado[1])
        self.enunciado = enunciado

        valida_alternativas = self.validate_alternativas(alternativas)
        if valida_alternativas[0] == False:
            raise ParamNotValidated("alternativas", valida_alternativas[1])
        self.alternativas = alternativas

    @staticmethod
    def validate_enunciado(enunciado: str) -> Tuple[bool, str]:
        if enunciado is None:
            return (False, "A pergunta é necessária")
        if type(enunciado) != str:
            return (False, "O enunciado deve ser uma string")
        return (True, "")

    @staticmethod
    def validate_alternativas(alternativas: str) -> Tuple[bool, str]: 
        if alternativas is None:
            return(False, "Devem existir alternativas")
        if len(alternativas) <= 3:
            return(False, "Devem existir mais de 3 alternativas")
        return (True, "")
    
    def to_dict(self):
        return {
            "enunciado": self.enunciado,
            "alternativas": self.alternativas
        }
