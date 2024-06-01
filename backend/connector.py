from mysql.connector import (connection)

class connector():
    
    def __init__(self):
        self.cnx = connection.MySQLConnection( user=user, password=password, host=host, port=port) 
        self.cursor = self.cnx.cursor(buffered=True)

        self.cursor.execute("USE teste")


    def adicionar_aluno(self, nome, email, senha, turma):
        if email.endswith("@jpiaget.g12.br"):
            sql = "INSERT INTO alunos (emailAluno, senhaAluno, nomeAluno, turmaAluno) VALUES (%s, %s, %s, %s)"
            val = [
                (email, senha, nome, turma)
            ]

            self.cursor.executemany(sql, val)
            self.cnx.commit()
            return True
        else: 
            return False # email inválido

    def verificar_aluno(self, email, senha):

        sql = "SELECT CASE WHEN EXISTS(SELECT * FROM alunos WHERE emailAluno = %s AND senhaAluno = %s) THEN 1 ELSE 0 END AS RESULT"
        val = [(email, senha)]
        
        self.cursor.executemany(sql, val)
        resultado = self.cursor.fetchone()
        
        # TODO recusar entrada caso senha ou email esteja errado
        if resultado[0] == 1: 
            return True
        else:
            return False

    def adicionar_professor(self, nome, email, senha):
        if email.endswith("@jpiaget.pro.br"):
            sql = "INSERT INTO professores (emailProfessor, senhaProfessor, nomeProfessor) VALUES (%s, %s, %s)"
            val = [(email, senha, nome)]

            self.cursor.executemany(sql, val)
            self.cnx.commit()
            return True
        else: 
            return False

    def verificar_professor(self, email, senha):
        sql = "SELECT CASE WHEN EXISTS(SELECT * FROM professores WHERE emailProfessor = %s AND senhaProfessor = %s) THEN 1 ELSE 0 END AS RESULT"
        val = [(email, senha)]

        self.cursor.executemany(sql, val)
        resultado = self.cursor.fetchone()

        if resultado[0] == 1: print("Essa conta existe")
        else: print("Essa conta não existe")

    # TODO funções das perguntas
    def adicionar_perguntas(self):
        pass

    def solicitar_pergunta(self, id_pergunta):

        sql = "SELECT * FROM perguntas WHERE idPergunta = %s" % (id_pergunta)

        self.cursor.execute(sql)
        pergunta = self.cursor.fetchall()[0]

        return pergunta


    # TODO close na conexão

    def numero_de_perguntas(self):
        self.cursor.execute("SELECT * FROM perguntas")

        numero = self.cursor.fetchall()

        return len(numero)