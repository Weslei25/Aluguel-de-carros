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
        MainWindow.setMinimumSize(QtCore.QSize(911, 571))
        MainWindow.setMaximumSize(QtCore.QSize(911, 571))
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
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(491, 311))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/carro-esporte.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/money_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 35))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/car_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 35))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/paste_plain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setAutoDefault(True)
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 35))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/coins_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setAutoDefault(True)
        self.pushButton_4.setDefault(True)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 35))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/page_excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setAutoDefault(True)
        self.pushButton_5.setDefault(True)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(72, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 20))
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/application_side_expand.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSair.setIcon(icon6)
        self.actionSair.setObjectName("actionSair")
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/script_save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalvar.setIcon(icon7)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionCarros_usados = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/car_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCarros_usados.setIcon(icon8)
        self.actionCarros_usados.setObjectName("actionCarros_usados")
        self.actionCarros_novos = QtWidgets.QAction(MainWindow)
        self.actionCarros_novos.setIcon(icon2)
        self.actionCarros_novos.setObjectName("actionCarros_novos")
        self.actionCarros_usados_2 = QtWidgets.QAction(MainWindow)
        self.actionCarros_usados_2.setIcon(icon8)
        self.actionCarros_usados_2.setObjectName("actionCarros_usados_2")
        self.actionCarros_novos_2 = QtWidgets.QAction(MainWindow)
        self.actionCarros_novos_2.setIcon(icon2)
        self.actionCarros_novos_2.setObjectName("actionCarros_novos_2")
        self.actionCadastro_de_clientes = QtWidgets.QAction(MainWindow)
        self.actionCadastro_de_clientes.setIcon(icon3)
        self.actionCadastro_de_clientes.setObjectName("actionCadastro_de_clientes")
        self.actionCadastro_de_veiculos = QtWidgets.QAction(MainWindow)
        self.actionCadastro_de_veiculos.setIcon(icon3)
        self.actionCadastro_de_veiculos.setObjectName("actionCadastro_de_veiculos")
        self.actionA_receber = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/table_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionA_receber.setIcon(icon9)
        self.actionA_receber.setObjectName("actionA_receber")
        self.actionA_pagar = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/table_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionA_pagar.setIcon(icon10)
        self.actionA_pagar.setObjectName("actionA_pagar")
        self.actionA_vencer = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("c:\\Projeto_Weslei\\Sistema de aluguel de carros\\views\\../img/icones/icons/table_refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionA_vencer.setIcon(icon11)
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
        self.pushButton.setText(_translate("MainWindow", "Vender"))
        self.pushButton_2.setText(_translate("MainWindow", "Alugar"))
        self.pushButton_3.setText(_translate("MainWindow", "Editar"))
        self.pushButton_4.setText(_translate("MainWindow", "Contas"))
        self.pushButton_5.setText(_translate("MainWindow", "Relatorios"))
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
