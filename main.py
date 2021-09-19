from views.telaprincipal import Ui_MainWindow
from controller.db import DataBase
from PyQt5 import QtWidgets
from controller.vendas import Vendas
import sys
import logging
import os




class AlugarApp(QtWidgets.QMainWindow):# Classe que inicializa o sistema
    def __init__(self, *args, **argvs):# Metodo construtor da aplicação
        super(AlugarApp, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conexao = DataBase()
        self.conexao.conectardb()
        self.ui.pushButton.clicked.connect(self.testandocs)

        
    def testandocs(self):
        self.window = Vendas()
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
    logging.basicConfig(filename='Logs/Sistema_De_Aluguel_Carros.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format=log_format,
                    encoding='UTF-8')
    logging.info("Criando a aplicação")
    login.show()
    sys.exit(app.exec_())