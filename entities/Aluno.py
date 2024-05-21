
from typing import Tuple

from entities.Entity_error import ParamNotValidated

class Aluno:
    nome: str
    email: str
    senha: str
    id: int
    turma: str

    def __init__(self, nome: str=None, email: str=None, senha: str=None, id: int=None, turma: str=None):
        valida_nome = self.validate_nome(nome)
        if valida_nome[0] == False:
            raise ParamNotValidated("nome", valida_nome[1])
    
    @staticmethod
    def validate_nome(nome: str) -> Tuple[bool, str]:
        if nome is None:
            return (False, "O nome é necessário")
        if type(nome) != str:
            return (False, "O nome deve ser uma string")
        return (True, "")
    
    @staticmethod
    def valida_email(email: str) -> Tuple[bool, str]:
        if "@" not in email:
            return (False, "O email deve ser válido")
        if type(email) != str:
            return(False, "O email deve ser uma string")
        return(True, "")