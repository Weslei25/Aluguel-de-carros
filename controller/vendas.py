from views.teladevendas import Ui_Vendas
from PyQt5 import QtWidgets
import logging
from controller.db import DataBase

class Vendas(QtWidgets.QMainWindow):# Classe que inicializa o sistema
    def __init__(self, *args, **argvs):# Metodo construtor da aplicação
        super(Vendas, self).__init__(*args, **argvs)
        self.ui = Ui_Vendas()
        self.ui.setupUi(self)
        logging.info("Class Vendas instaciada com sucesso")