# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Projeto_Weslei\Sistema de aluguel de carros\views\telaprincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(911, 571)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/carro-esporte.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(207, 220, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setContentsMargins(0, 0, 0, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMinimumSize(QtCore.QSize(5, 4))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(r".\\img\\image_main.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(901, 100))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setSpacing(27)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cadastrarCarro = QtWidgets.QPushButton(self.frame_2)
        self.cadastrarCarro.setMinimumSize(QtCore.QSize(0, 67))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.cadastrarCarro.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/cadastro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastrarCarro.setIcon(icon1)
        self.cadastrarCarro.setIconSize(QtCore.QSize(50, 50))
        self.cadastrarCarro.setAutoDefault(True)
        self.cadastrarCarro.setDefault(True)
        self.cadastrarCarro.setFlat(False)
        self.cadastrarCarro.setObjectName("cadastrarCarro")
        self.horizontalLayout.addWidget(self.cadastrarCarro)
        self.venderCarro = QtWidgets.QPushButton(self.frame_2)
        self.venderCarro.setMinimumSize(QtCore.QSize(0, 67))
        self.venderCarro.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.venderCarro.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones-de-dinheiro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.venderCarro.setIcon(icon2)
        self.venderCarro.setIconSize(QtCore.QSize(43, 50))
        self.venderCarro.setAutoDefault(True)
        self.venderCarro.setDefault(True)
        self.venderCarro.setFlat(False)
        self.venderCarro.setObjectName("venderCarro")
        self.horizontalLayout.addWidget(self.venderCarro)
        self.alugarCarro = QtWidgets.QPushButton(self.frame_2)
        self.alugarCarro.setMinimumSize(QtCore.QSize(0, 67))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.alugarCarro.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/alugar-um-carro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alugarCarro.setIcon(icon3)
        self.alugarCarro.setIconSize(QtCore.QSize(49, 50))
        self.alugarCarro.setAutoDefault(True)
        self.alugarCarro.setDefault(True)
        self.alugarCarro.setFlat(False)
        self.alugarCarro.setObjectName("alugarCarro")
        self.horizontalLayout.addWidget(self.alugarCarro)
        self.editarCarro = QtWidgets.QPushButton(self.frame_2)
        self.editarCarro.setMinimumSize(QtCore.QSize(0, 67))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.editarCarro.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/editar-arquivo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editarCarro.setIcon(icon4)
        self.editarCarro.setIconSize(QtCore.QSize(54, 53))
        self.editarCarro.setAutoDefault(True)
        self.editarCarro.setDefault(True)
        self.editarCarro.setFlat(False)
        self.editarCarro.setObjectName("editarCarro")
        self.horizontalLayout.addWidget(self.editarCarro)
        self.contas = QtWidgets.QPushButton(self.frame_2)
        self.contas.setMinimumSize(QtCore.QSize(0, 67))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.contas.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/salario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.contas.setIcon(icon5)
        self.contas.setIconSize(QtCore.QSize(43, 50))
        self.contas.setAutoDefault(True)
        self.contas.setDefault(True)
        self.contas.setFlat(False)
        self.contas.setObjectName("contas")
        self.horizontalLayout.addWidget(self.contas)
        self.geraRelatorio = QtWidgets.QPushButton(self.frame_2)
        self.geraRelatorio.setMinimumSize(QtCore.QSize(0, 67))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.geraRelatorio.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.geraRelatorio.setIcon(icon6)
        self.geraRelatorio.setIconSize(QtCore.QSize(44, 50))
        self.geraRelatorio.setAutoDefault(True)
        self.geraRelatorio.setDefault(True)
        self.geraRelatorio.setFlat(False)
        self.geraRelatorio.setObjectName("geraRelatorio")
        self.horizontalLayout.addWidget(self.geraRelatorio)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 21))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuVender = QtWidgets.QMenu(self.menubar)
        self.menuVender.setObjectName("menuVender")
        self.menuAlugar = QtWidgets.QMenu(self.menubar)
        self.menuAlugar.setObjectName("menuAlugar")
        self.menuEditar = QtWidgets.QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        self.menuContas = QtWidgets.QMenu(self.menubar)
        self.menuContas.setObjectName("menuContas")
        MainWindow.setMenuBar(self.menubar)
        self.actionSair = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/application_side_expand.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSair.setIcon(icon7)
        self.actionSair.setObjectName("actionSair")
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/script_save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalvar.setIcon(icon8)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionCarros_usados = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/car_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCarros_usados.setIcon(icon9)
        self.actionCarros_usados.setObjectName("actionCarros_usados")
        self.actionCarros_novos = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/car_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCarros_novos.setIcon(icon10)
        self.actionCarros_novos.setObjectName("actionCarros_novos")
        self.actionCarros_usados_2 = QtWidgets.QAction(MainWindow)
        self.actionCarros_usados_2.setIcon(icon9)
        self.actionCarros_usados_2.setObjectName("actionCarros_usados_2")
        self.actionCarros_novos_2 = QtWidgets.QAction(MainWindow)
        self.actionCarros_novos_2.setIcon(icon10)
        self.actionCarros_novos_2.setObjectName("actionCarros_novos_2")
        self.actionCadastro_de_clientes = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/paste_plain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCadastro_de_clientes.setIcon(icon11)
        self.actionCadastro_de_clientes.setObjectName("actionCadastro_de_clientes")
        self.actionCadastro_de_veiculos = QtWidgets.QAction(MainWindow)
        self.actionCadastro_de_veiculos.setIcon(icon11)
        self.actionCadastro_de_veiculos.setObjectName("actionCadastro_de_veiculos")
        self.actionA_receber = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/table_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionA_receber.setIcon(icon12)
        self.actionA_receber.setObjectName("actionA_receber")
        self.actionA_pagar = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/table_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionA_pagar.setIcon(icon13)
        self.actionA_pagar.setObjectName("actionA_pagar")
        self.actionA_vencer = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/table_refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionA_vencer.setIcon(icon14)
        self.actionA_vencer.setObjectName("actionA_vencer")
        self.menuArquivo.addAction(self.actionSair)
        self.menuArquivo.addAction(self.actionSalvar)
        self.menuVender.addAction(self.actionCarros_usados)
        self.menuVender.addAction(self.actionCarros_novos)
        self.menuAlugar.addAction(self.actionCarros_usados_2)
        self.menuAlugar.addAction(self.actionCarros_novos_2)
        self.menuEditar.addAction(self.actionCadastro_de_clientes)
        self.menuEditar.addAction(self.actionCadastro_de_veiculos)
        self.menuContas.addAction(self.actionA_receber)
        self.menuContas.addAction(self.actionA_pagar)
        self.menuContas.addAction(self.actionA_vencer)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuVender.menuAction())
        self.menubar.addAction(self.menuAlugar.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuContas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aluguel De Carros 1.0.0"))
        self.cadastrarCarro.setText(_translate("MainWindow", "Cadastrar"))
        self.venderCarro.setText(_translate("MainWindow", "Vender"))
        self.alugarCarro.setText(_translate("MainWindow", "Alugar"))
        self.editarCarro.setText(_translate("MainWindow", "Editar"))
        self.contas.setText(_translate("MainWindow", "Contas"))
        self.geraRelatorio.setText(_translate("MainWindow", "Relatorios"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuVender.setTitle(_translate("MainWindow", "Vender"))
        self.menuAlugar.setTitle(_translate("MainWindow", "Alugar"))
        self.menuEditar.setTitle(_translate("MainWindow", "Editar"))
        self.menuContas.setTitle(_translate("MainWindow", "Contas"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar"))
        self.actionCarros_usados.setText(_translate("MainWindow", "Carros usados"))
        self.actionCarros_novos.setText(_translate("MainWindow", "Carros novos"))
        self.actionCarros_usados_2.setText(_translate("MainWindow", "Carros usados"))
        self.actionCarros_novos_2.setText(_translate("MainWindow", "Carros novos"))
        self.actionCadastro_de_clientes.setText(_translate("MainWindow", "Cadastro de clientes"))
        self.actionCadastro_de_veiculos.setText(_translate("MainWindow", "Cadastro de veiculos"))
        self.actionA_receber.setText(_translate("MainWindow", "A receber"))
        self.actionA_pagar.setText(_translate("MainWindow", "A pagar"))
        self.actionA_vencer.setText(_translate("MainWindow", "A vencer"))
