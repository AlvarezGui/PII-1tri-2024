from mysql.connector import (connection)

class connector():
    
    def __init__(self):
        self.cnx = connection.MySQLConnection(user='user', password='senha', host='host', port='port')
        self.cursor = self.cnx.cursor(buffered=True)

        self.cursor.execute("USE teste")

        # TODO criar tabela alunos e usar ela


    def adicionar_aluno(self, nome, email, senha, turma):
        # TODO fazer essa lógica funcionar com a tabela dos alunos, e depois com as demais tabelas


        sql = "INSERT INTO alunos (emailAluno, senhaAluno, nomeAluno, turmaAluno) VALUES (%s, %s, %s, %s)"
        val = [
            (email, senha, nome, turma)
        ]

        self.cursor.executemany(sql, val)
        self.cnx.commit()

        # self.cursor.execute("SELECT nome FROM testeTabela")

        # for i in self.cursor:
        #     print(i)

    def verificar_aluno(self, email, senha):
        # TODO verificar se o aluno existe na tabela
        pass