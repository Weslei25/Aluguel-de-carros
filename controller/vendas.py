from views.teladevendas import Ui_Vendas
from PyQt5 import QtWidgets
import logging
from controller.db import DataBase
import datetime


class Vendas(QtWidgets.QMainWindow):# Classe que inicializa o sistema
    def __init__(self, *args, **argvs):# Metodo construtor da aplicação
        super(Vendas, self).__init__(*args, **argvs)
        self.ui = Ui_Vendas()
        self.ui.setupUi(self)
        logging.info("Class Vendas instaciada com sucesso")
        dataDeHoje = datetime.datetime.now()
        self.ui.dateEdit.setDate(dataDeHoje)
        self.ui.dateEdit_2.setDate(dataDeHoje)
        self.ui.pushButton_3.clicked.connect(self.realizarvendanovoveiculo)

    def realizarvendanovoveiculo(self):
        try:
            print('Ola')
        except Exception as erro:
            QtWidgets.QMessageBox.critical(self, "Erro", "Ocorreu um erro ao tentar realizar a venda do veiculo")
            logging.exception("{}".format(erro))
            return