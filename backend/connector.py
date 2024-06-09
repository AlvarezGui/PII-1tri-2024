from mysql.connector import (connection)

class connector():
    
    def __init__(self):
        self.cnx = connection.MySQLConnection(user=user, password=password, host=host, port=port) 
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

        if resultado[0] == 1: print("Essa aluno existe")
        else: print("Essa aluno não existe")

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
    
    def solicitar_ranking(self, tipo:str):
        # TODO solicitar o ranking do jogador
        # Se o usuario for professor, voltar todos os rankings, se n, voltar apenas os 5 primeiros da turma
        if tipo == "professor":
            sql = "SELECT * FROM alunos ORDER BY pontos"
        elif tipo == "aluno":
            sql = "SELECT nomeAluno, pontosAluno FROM alunos ORDER BY pontosAluno LIMIT 5"

        self.cursor.execute(sql)
        alunos = self.cursor.fetchall()
        return alunos

    def deletar_turma(self, id:int):
        # TODO deletar turma
        # será usado na tela de deletar
        sql = "DELETE FROM turma WHERE idTurma = %s" % (id)
        self.cursor.execute(sql)
        return

    def deletar_aluno(self, id:int):
        # TODO deletar aluno
        # será usado na tela de deletar
        sql = "DELETE FROM alunos WHERE idaluno = %s" % (id)
        self.cursor.execute(sql)
        return print("AAAAAA")

    def solictar_turma(self):
        # TODO solicitar turma
        # vai ser usado nas telas tanto de atualizar turma quanto de deletar turma
        sql = "SELECT * FROM turma"
        self.cursor.execute(sql)
        turmas = self.cursor.fetchall()
        return turmas

    def solicitar_aluno(self):
        # TODO solicitar aluno
        # vai ser usado nas telas tanto de atualizar aluno quanto de deletar aluno
        sql = "SELECT * FROM alunos"
        self.cursor.execute(sql)
        alunos = self.cursor.fetchall()
        return alunos

    def adicionar_turma(self, turma:str):
        # TODO adicionar turma
        # será usado na tela de criar turma
        sql = "INSERT INTO turmas (nomeTurma) VALUES (%s)" % (turma)
        self.cursor.execute(sql)
        self.cnx.commit()
        return
