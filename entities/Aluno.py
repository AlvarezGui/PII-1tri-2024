
from typing import Tuple

from entities.Entity_error import ParamNotValidated

class Aluno:
    nome: str
    email: str
    senha: str
    turma: str

    def __init__(self, nome: str=None, email: str=None, senha: str=None, turma: str=None):
        valida_nome = self.validate_nome(nome)
        if valida_nome[0] == False:
            raise ParamNotValidated("nome", valida_nome[1])
        self.nome = nome

        valida_email = self.validate_email(email)
        if valida_email[0] == False:
            raise ParamNotValidated("email", valida_email[1])
        self.email = email

        valida_senha = self.validate_senha(senha)
        if valida_senha[0] == False:
            raise ParamNotValidated("senha", valida_senha[1])
        self.senha = senha

        valida_turma = self.validate_turma(turma)
        if valida_turma[0] == False:
            raise ParamNotValidated("turma", valida_turma[1])
        self.turma
        

    
    @staticmethod
    def validate_nome(nome: str) -> Tuple[bool, str]:
        if nome is None:
            return (False, "O nome é necessário")
        if type(nome) != str:
            return (False, "O nome deve ser uma string")
        return (True, "")
    
    @staticmethod
    def validate_email(email: str) -> Tuple[bool, str]:
        if email is None:
            return(False, "O email não pode ser None")
        if "@" not in email:
            return (False, "O email deve ser válido")
        if type(email) != str:
            return(False, "O email deve ser uma string")
        return(True, "")
    
    @staticmethod
    def validate_senha(senha: str) -> Tuple[bool, str]:
        if senha is None:
            return(False, "A senha não pode ser None")
        if type(senha) != str:
            return (False, "A senha deve ser uma string")
        if len(senha) < 8:
            return (False, "A senha deve ter no mínimo 8 carateres")
        return (True, "")
    
    @staticmethod
    def validate_turma(turma: str) -> Tuple[bool, str]:
        if turma is None:
            return (False, "A turma não pode ser None")
        if type(turma) != str:
            return (False, "A turma deve ser uma string")
        if len(turma) > 10:
            return (False, "As turmas tem no maximo 10 caracteres")
        return (True, "")

    
    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "turma": self.turma
        }
