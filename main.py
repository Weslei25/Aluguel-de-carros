from views.telaprincipal import Ui_MainWindow
from PyQt5 import QtWidgets
from controller.vendas import Vendas
from controller.cadastrodeveiculos import CadastroVeiculos
from controller.AlugarVeiculoController import AlugarVeiculo
import sys
import logging
import os

class AlugarApp(QtWidgets.QMainWindow):# Classe que inicializa o sistema
    
    def __init__(self, *args, **argvs):# Metodo construtor da aplicação
        super(AlugarApp, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.venderCarro.clicked.connect(self.venderveiculo)
        self.ui.cadastrarCarro.clicked.connect(self.cadastrarveiculo)
        self.ui.alugarCarro.clicked.connect(self.alugarveiculo)
        self.ui.actionCarros_usados.triggered.connect(self.venderveiculo)
        self.ui.actionCarros_novos.triggered.connect(self.venderveiculo)
        
    def venderveiculo(self):
        self.window = Vendas()
        self.window.show()
        

    def cadastrarveiculo(self):
        self.window = CadastroVeiculos()
        self.window.show()
    
    def alugarveiculo(self):
        self.window = AlugarVeiculo()
        self.window.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')
    login = AlugarApp()
    try:
        os.mkdir("./Logs")
    except Exception as erro:
        pass
    log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s' # Configuracao de logs
    logging.basicConfig(filename='Logs\{}.log'.format(__name__),
                    filemode='w',
                    level=logging.DEBUG,
                    format=log_format,
                    encoding='UTF-8')
    logging.info("Criando a aplicação")
    login.show()
    sys.exit(app.exec_())
    