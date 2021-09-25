from views.AlugarVeiculo import Ui_AlugarVeiculo
from PyQt5 import QtWidgets
import logging
from controller.db import DataBase
import datetime


class AlugarVeiculo(QtWidgets.QMainWindow):# Classe que inicializa o sistema
    def __init__(self, *args, **argvs):# Metodo construtor da aplicação
        super(AlugarVeiculo, self).__init__(*args, **argvs)
        self.ui = Ui_AlugarVeiculo()
        self.ui.setupUi(self)
        self.log = logging.getLogger(__name__)
        self.log.info("Entra Classe {}".format(__name__))