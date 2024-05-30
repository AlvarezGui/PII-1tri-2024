from mysql.connector import (connection)

class connector():
    
    def __init__(self):
        self.cnx = connection.MySQLConnection(user=user, password=password, host=host, port=port) 
        self.cursor = self.cnx.cursor(buffered=True)

        self.cursor.execute("USE teste")

        # TODO criar tabela alunos e usar ela


    def adicionar_aluno(self, nome, email, senha, turma):

        sql = "INSERT INTO alunos (emailAluno, senhaAluno, nomeAluno, turmaAluno) VALUES (%s, %s, %s, %s)"
        val = [
            (email, senha, nome, turma)
        ]

        self.cursor.executemany(sql, val)
        self.cnx.commit()

        # for i in self.cursor:
        #     print(i)

    def verificar_aluno(self, email, senha):
        # TODO verificar se o aluno existe na tabela

        sql = "SELECT CASE WHEN EXISTS(SELECT * FROM alunos WHERE emailAluno = %s AND senhaAluno = %s) THEN 1 ELSE 0 END AS RESULT"
        val = [(email, senha)]
        
        self.cursor.executemany(sql, val)
        resultado = self.cursor.fetchone()
        
        # TODO recusar entrada caso senha ou email esteja errado
        if resultado[0] == 1: print("Essa conta existe")
        else: print("Essa conta não existe")

    def adicionar_professor(self, nome, email, senha):
        sql = "INSERT INTO professores (emailProfessor, senhaProfessor, nomeProfessor) VALUES (%s, %s, %s)"
        val = [(email, senha, nome)]

        self.cursor.executemany(sql, val)
        self.cnx.commit()

    def verificar_professor(self, email, senha):
        sql = "SELECT CASE WHEN EXISTS(SELECT * FROM professores WHERE emailProfessor = %s AND senhaProfessor = %s) THEN 1 ELSE 0 END AS RESULT"
        val = [(email, senha)]

        self.cursor.executemany(sql, val)
        resultado = self.cursor.fetchone()

        if resultado[0] == 1: print("Essa conta existe")
        else: print("Essa conta não existe")

    # TODO funções dos professores e das perguntas

    # TODO close na conexão