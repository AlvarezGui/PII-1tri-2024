from mysql.connector import (connection)

class connector():
    
    def __init__(self):
        self.cnx = connection.MySQLConnection()
        self.cursor = self.cnx.cursor(buffered=True)

        self.cursor.execute("USE teste")

        # TODO criar tabela alunos e usar ela


    def adicionar_aluno(self, email, senha):
        # TODO fazer essa lógica funcionar com a tabela dos alunos, e depois com as demais tabelas


        sql = "INSERT INTO testeTabela (idTabela, nome) VALUES (%s, %s)"
        val = [
            (1222, "Eu amo testes")
        ]

        self.cursor.executemany(sql, val)
        self.cnx.commit()

        self.cursor.execute("SELECT nome FROM testeTabela")

        for i in self.cursor:
            print(i)

    def verificar_aluno(self, email, senha):
        # TODO verificar se o aluno existe na tabela
        pass