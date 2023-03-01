# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Oficinas_e_cursos_popup.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QListView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(941, 832)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 30, 891, 741))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(254, 226, 230);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(170, 0, 181, 71))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_cadastro_Oficinas = QLabel(self.frame_2)
        self.label_cadastro_Oficinas.setObjectName(u"label_cadastro_Oficinas")
        self.label_cadastro_Oficinas.setGeometry(QRect(10, 20, 181, 41))
        font = QFont()
        font.setFamilies([u"Abel"])
        font.setPointSize(36)
        self.label_cadastro_Oficinas.setFont(font)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 70, 291, 81))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lineEdit_CPF_Oficinas = QLineEdit(self.frame_3)
        self.lineEdit_CPF_Oficinas.setObjectName(u"lineEdit_CPF_Oficinas")
        self.lineEdit_CPF_Oficinas.setGeometry(QRect(0, 40, 232, 32))
        self.lineEdit_CPF_Oficinas.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;scrollbar-width: thin;\n"
"  scrollbar-color: #F9EDEC;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")
        self.label_CPF_Oficinas = QLabel(self.frame_3)
        self.label_CPF_Oficinas.setObjectName(u"label_CPF_Oficinas")
        self.label_CPF_Oficinas.setGeometry(QRect(10, 10, 51, 24))
        self.label_CPF_Oficinas.setMaximumSize(QSize(285, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Abel"])
        font1.setPointSize(12)
        self.label_CPF_Oficinas.setFont(font1)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(290, 70, 141, 81))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.comboBox_Tipo_Oficinas = QComboBox(self.frame_4)
        self.comboBox_Tipo_Oficinas.setObjectName(u"comboBox_Tipo_Oficinas")
        self.comboBox_Tipo_Oficinas.setGeometry(QRect(0, 40, 131, 32))
        self.comboBox_Tipo_Oficinas.setStyleSheet(u"QComboBox{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;scrollbar-width: thin;\n"
"  scrollbar-color: #F9EDEC;}\n"
"QComboBox:focus{outline:0; border: 2px solid #A85751}\n"
"")
        self.label_Tipo_Oficinas = QLabel(self.frame_4)
        self.label_Tipo_Oficinas.setObjectName(u"label_Tipo_Oficinas")
        self.label_Tipo_Oficinas.setGeometry(QRect(10, 10, 51, 24))
        self.label_Tipo_Oficinas.setMaximumSize(QSize(285, 16777215))
        self.label_Tipo_Oficinas.setFont(font1)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 150, 431, 71))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.lineEdit_Nome_Oficinas = QLineEdit(self.frame_5)
        self.lineEdit_Nome_Oficinas.setObjectName(u"lineEdit_Nome_Oficinas")
        self.lineEdit_Nome_Oficinas.setGeometry(QRect(0, 30, 422, 32))
        self.lineEdit_Nome_Oficinas.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;scrollbar-width: thin;\n"
"  scrollbar-color: #F9EDEC;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")
        self.label_Nome_Oficinas = QLabel(self.frame_5)
        self.label_Nome_Oficinas.setObjectName(u"label_Nome_Oficinas")
        self.label_Nome_Oficinas.setGeometry(QRect(10, 0, 51, 24))
        self.label_Nome_Oficinas.setMaximumSize(QSize(285, 16777215))
        self.label_Nome_Oficinas.setFont(font1)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 220, 431, 71))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.lineEdit_Email_Oficinas = QLineEdit(self.frame_6)
        self.lineEdit_Email_Oficinas.setObjectName(u"lineEdit_Email_Oficinas")
        self.lineEdit_Email_Oficinas.setGeometry(QRect(0, 30, 422, 32))
        self.lineEdit_Email_Oficinas.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;scrollbar-width: thin;\n"
"  scrollbar-color: #F9EDEC;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")
        self.label_Email_Oficinas = QLabel(self.frame_6)
        self.label_Email_Oficinas.setObjectName(u"label_Email_Oficinas")
        self.label_Email_Oficinas.setGeometry(QRect(10, 0, 51, 24))
        self.label_Email_Oficinas.setMaximumSize(QSize(285, 16777215))
        self.label_Email_Oficinas.setFont(font1)
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 290, 241, 71))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.lineEdit_Telefone_Oficinas = QLineEdit(self.frame_7)
        self.lineEdit_Telefone_Oficinas.setObjectName(u"lineEdit_Telefone_Oficinas")
        self.lineEdit_Telefone_Oficinas.setGeometry(QRect(0, 30, 232, 32))
        self.lineEdit_Telefone_Oficinas.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;scrollbar-width: thin;\n"
"  scrollbar-color: #F9EDEC;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")
        self.label_Telefone_Oficinas = QLabel(self.frame_7)
        self.label_Telefone_Oficinas.setObjectName(u"label_Telefone_Oficinas")
        self.label_Telefone_Oficinas.setGeometry(QRect(10, 0, 51, 24))
        self.label_Telefone_Oficinas.setMaximumSize(QSize(285, 16777215))
        self.label_Telefone_Oficinas.setFont(font1)
        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(240, 290, 191, 71))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.lineEdit_CPF = QLineEdit(self.frame_8)
        self.lineEdit_CPF.setObjectName(u"lineEdit_CPF")
        self.lineEdit_CPF.setGeometry(QRect(0, 30, 181, 32))
        self.lineEdit_CPF.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;scrollbar-width: thin;\n"
"  scrollbar-color: #F9EDEC;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")
        self.label_CEP_Oficinas = QLabel(self.frame_8)
        self.label_CEP_Oficinas.setObjectName(u"label_CEP_Oficinas")
        self.label_CEP_Oficinas.setGeometry(QRect(10, 0, 51, 24))
        self.label_CEP_Oficinas.setMaximumSize(QSize(285, 16777215))
        self.label_CEP_Oficinas.setFont(font1)
        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 360, 431, 71))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.lineEdit_Rua_Oficinas = QLineEdit(self.frame_9)
        self.lineEdit_Rua_Oficinas.setObjectName(u"lineEdit_Rua_Oficinas")
        self.lineEdit_Rua_Oficinas.setGeometry(QRect(0, 30, 422, 32))
        self.lineEdit_Rua_Oficinas.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;scrollbar-width: thin;\n"
"  scrollbar-color: #F9EDEC;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")
        self.label_Rua_Oficinas = QLabel(self.frame_9)
        self.label_Rua_Oficinas.setObjectName(u"label_Rua_Oficinas")
        self.label_Rua_Oficinas.setGeometry(QRect(10, 0, 51, 24))
        self.label_Rua_Oficinas.setMaximumSize(QSize(285, 16777215))
        self.label_Rua_Oficinas.setFont(font1)
        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(0, 430, 361, 71))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.lineEdit_Bairro_Oficinas = QLineEdit(self.frame_10)
        self.lineEdit_Bairro_Oficinas.setObjectName(u"lineEdit_Bairro_Oficinas")
        self.lineEdit_Bairro_Oficinas.setGeometry(QRect(0, 30, 354, 32))
        self.lineEdit_Bairro_Oficinas.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;scrollbar-width: thin;\n"
"  scrollbar-color: #F9EDEC;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")
        self.label_Bairro_Oficinas = QLabel(self.frame_10)
        self.label_Bairro_Oficinas.setObjectName(u"label_Bairro_Oficinas")
        self.label_Bairro_Oficinas.setGeometry(QRect(10, 0, 51, 24))
        self.label_Bairro_Oficinas.setMaximumSize(QSize(285, 16777215))
        self.label_Bairro_Oficinas.setFont(font1)
        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(0, 500, 361, 71))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.lineEdit_Cidade_Oficinas = QLineEdit(self.frame_11)
        self.lineEdit_Cidade_Oficinas.setObjectName(u"lineEdit_Cidade_Oficinas")
        self.lineEdit_Cidade_Oficinas.setGeometry(QRect(0, 30, 354, 32))
        self.lineEdit_Cidade_Oficinas.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;scrollbar-width: thin;\n"
"  scrollbar-color: #F9EDEC;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")
        self.label_Cidade_Oficinas = QLabel(self.frame_11)
        self.label_Cidade_Oficinas.setObjectName(u"label_Cidade_Oficinas")
        self.label_Cidade_Oficinas.setGeometry(QRect(10, 0, 51, 24))
        self.label_Cidade_Oficinas.setMaximumSize(QSize(285, 16777215))
        self.label_Cidade_Oficinas.setFont(font1)
        self.frame_12 = QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(0, 570, 361, 71))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.lineEdit_Estado_Oficinas = QLineEdit(self.frame_12)
        self.lineEdit_Estado_Oficinas.setObjectName(u"lineEdit_Estado_Oficinas")
        self.lineEdit_Estado_Oficinas.setGeometry(QRect(0, 30, 354, 32))
        self.lineEdit_Estado_Oficinas.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;scrollbar-width: thin;\n"
"  scrollbar-color: #F9EDEC;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")
        self.label_Estado_Oficinas = QLabel(self.frame_12)
        self.label_Estado_Oficinas.setObjectName(u"label_Estado_Oficinas")
        self.label_Estado_Oficinas.setGeometry(QRect(10, 0, 51, 24))
        self.label_Estado_Oficinas.setMaximumSize(QSize(285, 16777215))
        self.label_Estado_Oficinas.setFont(font1)
        self.line_linha_Oficinas = QFrame(self.frame)
        self.line_linha_Oficinas.setObjectName(u"line_linha_Oficinas")
        self.line_linha_Oficinas.setGeometry(QRect(450, 0, 2, 640))
        self.line_linha_Oficinas.setStyleSheet(u"background-color: rgb(236, 132, 140);")
        self.line_linha_Oficinas.setFrameShape(QFrame.VLine)
        self.line_linha_Oficinas.setFrameShadow(QFrame.Sunken)
        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(0, 640, 361, 80))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.pushButton_Adicionar_Oficinas = QPushButton(self.frame_13)
        self.pushButton_Adicionar_Oficinas.setObjectName(u"pushButton_Adicionar_Oficinas")
        self.pushButton_Adicionar_Oficinas.setGeometry(QRect(90, 20, 141, 41))
        font2 = QFont()
        font2.setFamilies([u"Abel"])
        font2.setPointSize(18)
        self.pushButton_Adicionar_Oficinas.setFont(font2)
        self.pushButton_Adicionar_Oficinas.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")
        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(360, 640, 181, 80))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.pushButton_Fechar_Oficinas = QPushButton(self.frame_14)
        self.pushButton_Fechar_Oficinas.setObjectName(u"pushButton_Fechar_Oficinas")
        self.pushButton_Fechar_Oficinas.setGeometry(QRect(30, 20, 141, 41))
        self.pushButton_Fechar_Oficinas.setFont(font2)
        self.pushButton_Fechar_Oficinas.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        self.frame_15 = QFrame(self.frame)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(540, 640, 271, 80))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.pushButton_Remover_Oficinas = QPushButton(self.frame_15)
        self.pushButton_Remover_Oficinas.setObjectName(u"pushButton_Remover_Oficinas")
        self.pushButton_Remover_Oficinas.setGeometry(QRect(120, 20, 141, 41))
        self.pushButton_Remover_Oficinas.setFont(font2)
        self.pushButton_Remover_Oficinas.setStyleSheet(u"QPushButton{color: #fff; background-color: #FF3636; border-radius: 20px;}\n"
"QPushButton:hover{background-color: 	hsl(0, 100%, 64%)}\n"
"QPushButton:focus{outline:0}")
        self.frame_16 = QFrame(self.frame)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(460, 0, 411, 80))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.label_Lista_de_Cadastrados_Oficinas = QLabel(self.frame_16)
        self.label_Lista_de_Cadastrados_Oficinas.setObjectName(u"label_Lista_de_Cadastrados_Oficinas")
        self.label_Lista_de_Cadastrados_Oficinas.setGeometry(QRect(10, 20, 391, 41))
        self.label_Lista_de_Cadastrados_Oficinas.setFont(font)
        self.frame_17 = QFrame(self.frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(520, 80, 311, 201))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.listView_lista_de_cadastrados_Oficinas = QListView(self.frame_17)
        self.listView_lista_de_cadastrados_Oficinas.setObjectName(u"listView_lista_de_cadastrados_Oficinas")
        self.listView_lista_de_cadastrados_Oficinas.setGeometry(QRect(20, 0, 256, 201))
        self.listView_lista_de_cadastrados_Oficinas.setStyleSheet(u"QListView{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;scrollbar-width: thin;\n"
"  scrollbar-color: #F9EDEC;}\n"
"QListView:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 941, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_cadastro_Oficinas.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_CPF_Oficinas.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.label_Tipo_Oficinas.setText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.label_Nome_Oficinas.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_Email_Oficinas.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_Telefone_Oficinas.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.label_CEP_Oficinas.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.label_Rua_Oficinas.setText(QCoreApplication.translate("MainWindow", u"Rua", None))
        self.label_Bairro_Oficinas.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.label_Cidade_Oficinas.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_Estado_Oficinas.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.pushButton_Adicionar_Oficinas.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.pushButton_Fechar_Oficinas.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
        self.pushButton_Remover_Oficinas.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.label_Lista_de_Cadastrados_Oficinas.setText(QCoreApplication.translate("MainWindow", u"Lista de Cadastrados", None))
    # retranslateUi

