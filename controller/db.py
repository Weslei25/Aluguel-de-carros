import mysql.connector

class DataBase():
    def __init__(self, host='localhost', user='WESLEI', password='0803', db='vendas', auth_plugin='mysql_native_password'):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.plugin = auth_plugin

    def conectardb(self):
        self.conexao = mysql.connector.connect(host=self.host,
                                               user=self.user,
                                               password=self.password,
                                               database=self.db,
                                               auth_plugin=self.plugin)
        self.cursor = self.conexao.cursor()

    def desconecta(self):
        self.conexao.close()

    def executa_DQL(self, sql):
        self.conectardb()
        self.cursor.execute(sql)
        resposta = self.cursor.fetchall()
        self.desconecta()
        return resposta

    def executa_DML(self, sql):
        self.conectardb()
        self.cursor.execute(sql)
        self.conexao.commit()
        self.desconecta()
