from views.cadastro import Ui_cadastro_Veiculos
from controller.db import DataBase
import logging
from PyQt5 import QtWidgets
import datetime 

class CadastroVeiculos(QtWidgets.QMainWindow):
    def __init__(self, *args, **argvs):# Metodo construtor da aplicação
        super(CadastroVeiculos, self).__init__(*args, **argvs)
        self.ui = Ui_cadastro_Veiculos()
        self.ui.setupUi(self)
        self.dataDeHoje = datetime.datetime.now()
        self.ui.dateEdit.setDate(self.dataDeHoje)
        self.ui.pushButton_3.clicked.connect(self.set_cadastrarnovoveiculo)
        self.log = logging.getLogger(__name__)
        self.log.debug("Inicializando Cadastro de veiculos")
        self.db = DataBase()
        self.catalogarveiculos()
        self.ui.pushButton_2.clicked.connect(self.pesquisarveiculo)
    
    def set_cadastrarnovoveiculo(self):
        try:

            ano = self.ui.dateEdit.text()
            ano = datetime.datetime.strptime(ano, '%d/%m/%Y')
            ano = ano.strftime('%Y-%m-%d')

            nomeDoVeiculo = self.ui.lineEdit.text()
            descicao =  self.ui.lineEdit_2.text()
            marca =  self.ui.lineEdit_3.text()
            placa = self.ui.lineEdit_5.text()
            chassi = self.ui.lineEdit_6.text()

            if not ano or not nomeDoVeiculo:
                QtWidgets.QMessageBox.information(self, "Aviso", "Preencha todos os campos para o cadastro do veiculo")
                self.ui.lineEdit.setStyleSheet('background-color: rgb(255, 73, 73);color: rgb(255, 255, 255);')
                return
            elif not descicao or not marca:
                QtWidgets.QMessageBox.information(self, "Aviso", "Preencha todos os campos para o cadastro do veiculo")
                self.ui.lineEdit_2.setStyleSheet('background-color: rgb(255, 73, 73);color: rgb(255, 255, 255);')
                self.ui.lineEdit_3.setStyleSheet('background-color: rgb(255, 73, 73);color: rgb(255, 255, 255);')
                return
            elif not placa or not chassi:
               self.ui.lineEdit_5.setStyleSheet('background-color: rgb(255, 73, 73);color: rgb(255, 255, 255);')
               self.ui.lineEdit_6.setStyleSheet('background-color: rgb(255, 73, 73);color: rgb(255, 255, 255);')
               QtWidgets.QMessageBox.information(self, "Aviso", "Preencha todos os campos para o cadastro do veiculo")
               return
            
            self.db.conectardb()
            self.db.executa_DML(f"""INSERT INTO carros
                                    (NOME, ANO, DESCRICAO, MARCA, PLACA, CHASSI)
                                    VALUES('{nomeDoVeiculo}', '{ano}', '{descicao}', '{marca}', '{placa}', '{chassi}');
                                    """)

            
            self.catalogarveiculos()        
            self.set_limparcampos()

            QtWidgets.QMessageBox.information(self, "Aviso", "Novo carro cadastrado com sucesso")                        
        except Exception as erro:
            QtWidgets.QMessageBox.critical(self, "Erro", "Ocoreu um erro ao tentar cadastrar o novo veiculo")
            logging.exception('{}'.format(erro))
            return
        finally:
            # if is SystemError
            logging.info("Fim do metodo ")

    def set_limparcampos(self):
        self.ui.lineEdit.setText("")# Limpando todos os campos
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_5.setText("")
        self.ui.lineEdit_6.setText("")

    def catalogarveiculos(self):
        try:
            
            catalogo = self.db.executa_DQL("""SELECT IDCARRO, NOME, DESCRICAO, MARCA, PLACA, CHASSI, ANO
                                                FROM vendas.carros;""")
            
            self.ui.tableWidget_2.setRowCount(len(catalogo))
            self.ui.tableWidget_2.setColumnCount(7)

            for i in range(0, len(catalogo)):
                for j in range(0, 7):
                    self.ui.tableWidget_2.setItem(
                        i, j, QtWidgets.QTableWidgetItem(str(catalogo[i][j])))
            
        except Exception as erro:
            QtWidgets.QMessageBox.critical(self, "Erro", "Ocoreu um erro ao tentar catalogar o veiculo descrito")
            logging.exception('{}'.format(erro))
    

    def pesquisarveiculo(self):
        try:
            pesquisar = self.ui.pesquisarveiculo.text()
            clausula = self.ui.comboBox.currentText()

            datadehoje = self.ui.dateEdit.text()
            datadehoje = datetime.datetime.strptime(datadehoje, '%d/%m/%Y')
            datadehoje = datadehoje.strftime('%Y-%m-%d')
            if clausula == "Codigo":
                catalogo = self.db.executa_DQL(f"""SELECT IDCARRO, NOME, DESCRICAO, MARCA, PLACA, CHASSI, ANO
                                                    FROM carros WHERE IDCARRO = '{pesquisar}';""")
            elif clausula == "Nome":
                catalogo = self.db.executa_DQL(f"""SELECT IDCARRO, NOME, DESCRICAO, MARCA, PLACA, CHASSI, ANO
                                                    FROM carros WHERE NOME = '{pesquisar}';""")
            elif clausula == "Descrição":
                catalogo = self.db.executa_DQL(f"""SELECT IDCARRO, NOME, DESCRICAO, MARCA, PLACA, CHASSI, ANO
                                                    FROM carros WHERE MARCA = '{pesquisar}';""")
            elif clausula == "Marca":
                catalogo = self.db.executa_DQL(f"""SELECT IDCARRO, NOME, DESCRICAO, MARCA, PLACA, CHASSI, ANO
                                                    FROM carros WHERE MARCA = '{pesquisar}';""")
            elif clausula == "Placa":
                catalogo = self.db.executa_DQL(f"""SELECT IDCARRO, NOME, DESCRICAO, MARCA, PLACA, CHASSI, ANO
                                                    FROM carros WHERE PLACA = '{pesquisar}';""")
            elif clausula == "Chassi":
                catalogo = self.db.executa_DQL(f"""SELECT IDCARRO, NOME, DESCRICAO, MARCA, PLACA, CHASSI, ANO
                                                    FROM carros WHERE CHASSI = '{pesquisar}';""")
            elif clausula == "Ano":
                catalogo = self.db.executa_DQL(f"""SELECT IDCARRO, NOME, DESCRICAO, MARCA, PLACA, CHASSI, ANO
                                                    FROM carros WHERE Ano = '{pesquisar}';""")
            elif clausula == "Todos":
                catalogo = self.db.executa_DQL(f"""SELECT IDCARRO, NOME, DESCRICAO, MARCA, PLACA, CHASSI, ANO
                                                    FROM carros;""")

            self.ui.tableWidget_2.setRowCount(len(catalogo))
            self.ui.tableWidget_2.setColumnCount(7)

            for i in range(0, len(catalogo)):
                for j in range(0, 7):
                    self.ui.tableWidget_2.setItem(
                        i, j, QtWidgets.QTableWidgetItem(str(catalogo[i][j])))
            
        except Exception as erro:
            QtWidgets.QMessageBox.critical(self, "Erro", "Ocoreu um erro ao tentar catalogar o veiculo descrito")
            logging.exception('{}'.format(erro))