
from typing import Tuple

from entities.Entity_error import ParamNotValidated
from ..enum.answer_type_enum import AnswerTypeEnum

class Pergunta:
    enunciado: str
    alternativas: int
    resposta_correta: AnswerTypeEnum

    def __init__(self, enunciado: str=None, alternativas: int=None, resposta_correta: AnswerTypeEnum=None):
        valida_enunciado = self.validate_enunciado(enunciado)
        if valida_enunciado[0] == False:
            raise ParamNotValidated("enunciado", valida_enunciado[1])
        self.enunciado = enunciado

        valida_alternativas = self.validate_alternativas(alternativas)
        if valida_alternativas[0] == False:
            raise ParamNotValidated("alternativas", valida_alternativas[1])
        self.alternativas = alternativas

        valida_resposta_c = self.validate_resposta_correta(resposta_correta)
        if valida_resposta_c[0] == False:
            raise ParamNotValidated("resposta correta", valida_resposta_c[1])
        self.resposta_correta = resposta_correta


    @staticmethod
    def validate_enunciado(enunciado: str) -> Tuple[bool, str]:
        if enunciado is None:
            return (False, "A pergunta é necessária")
        if type(enunciado) != str:
            return (False, "O enunciado deve ser uma string")
        return (True, "")
    
    @staticmethod
    def validate_alternativas(alternativas: int) -> Tuple[bool, str]: 
        if alternativas is None:
            return(False, "Devem existir alternativas")
        if alternativas <= 3:
            return(False, "Devem existir mais de 3 alternativas")
        return (True, "")
    
    @staticmethod
    def validate_resposta_correta(resposta_correta: AnswerTypeEnum) -> Tuple[bool,  str]:
        if resposta_correta is None:
            return(False, "Selecione uma resposta correta")
        if type(resposta_correta) != AnswerTypeEnum:
            return(False, "A resposta correta deve ser uma string")
        if len(resposta_correta) != 1:
            return(False, "A resposta correta deve ter apenas um caractere")
        return(True, "")
    
    def to_dict(self):
        return {
            "enunciado": self.enunciado,
            "alternativas": self.alternativas,
            "resposta_correta": self.resposta_correta
        }