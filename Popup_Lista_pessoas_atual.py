# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Popup_Lista_pessoas_atualojGKoN.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(920, 924)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #FEE2E6;border-radius: 15px;border: 1px solid #E58893")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{background-color: #FEE2E6;border-top-left-radius: 15px; border-bottom-left-radius: 15px; border-top-right-radius: 15px; border-bottom-right-radius: 15px; border: none}\n"
"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"QComboBox{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;scrollbar-width: thin;\n"
"  scrollbar-color: #F9EDEC;}\n"
"QComboBox:focus{outline:0; border: 2px solid #A85751}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_16 = QFrame(self.frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.line_linha_Oficinas_as_2 = QFrame(self.frame_16)
        self.line_linha_Oficinas_as_2.setObjectName(u"line_linha_Oficinas_as_2")
        self.line_linha_Oficinas_as_2.setStyleSheet(u"background-color: rgb(236, 132, 140);\n"
"border:0px;")
        self.line_linha_Oficinas_as_2.setFrameShape(QFrame.VLine)
        self.line_linha_Oficinas_as_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_linha_Oficinas_as_2)


        self.gridLayout.addWidget(self.frame_16, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label_cadastro_popup_oficinas_as = QLabel(self.frame_14)
        self.label_cadastro_popup_oficinas_as.setObjectName(u"label_cadastro_popup_oficinas_as")
        font = QFont()
        font.setFamilies([u"Abel"])
        font.setPointSize(36)
        self.label_cadastro_popup_oficinas_as.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_cadastro_popup_oficinas_as)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.gridLayout_2.addWidget(self.frame_14, 0, 0, 1, 2)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_cpf_popup_oficinas_as = QLabel(self.frame_4)
        self.label_cpf_popup_oficinas_as.setObjectName(u"label_cpf_popup_oficinas_as")
        font1 = QFont()
        font1.setFamilies([u"Abel"])
        font1.setPointSize(16)
        self.label_cpf_popup_oficinas_as.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_cpf_popup_oficinas_as)

        self.input_cpf_popup_oficinas_as = QLineEdit(self.frame_4)
        self.input_cpf_popup_oficinas_as.setObjectName(u"input_cpf_popup_oficinas_as")
        self.input_cpf_popup_oficinas_as.setMinimumSize(QSize(0, 35))
        self.input_cpf_popup_oficinas_as.setMaximumSize(QSize(16777215, 35))
        self.input_cpf_popup_oficinas_as.setFont(font1)
        self.input_cpf_popup_oficinas_as.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.input_cpf_popup_oficinas_as)


        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_tipo_popup_oficinas_as = QLabel(self.frame_5)
        self.label_tipo_popup_oficinas_as.setObjectName(u"label_tipo_popup_oficinas_as")
        self.label_tipo_popup_oficinas_as.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_tipo_popup_oficinas_as)

        self.comboBox_tipo_popup_oficinas_as = QComboBox(self.frame_5)
        self.comboBox_tipo_popup_oficinas_as.setObjectName(u"comboBox_tipo_popup_oficinas_as")
        self.comboBox_tipo_popup_oficinas_as.setMinimumSize(QSize(192, 35))
        font2 = QFont()
        font2.setFamilies([u"Abel"])
        self.comboBox_tipo_popup_oficinas_as.setFont(font2)
        self.comboBox_tipo_popup_oficinas_as.setStyleSheet(u"")
        self.comboBox_tipo_popup_oficinas_as.setEditable(False)

        self.verticalLayout_4.addWidget(self.comboBox_tipo_popup_oficinas_as)


        self.gridLayout_2.addWidget(self.frame_5, 1, 1, 1, 1)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_nome_popup_oficinas_as = QLabel(self.frame_6)
        self.label_nome_popup_oficinas_as.setObjectName(u"label_nome_popup_oficinas_as")
        self.label_nome_popup_oficinas_as.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_nome_popup_oficinas_as)

        self.input_nome_popup_oficinas_as = QLineEdit(self.frame_6)
        self.input_nome_popup_oficinas_as.setObjectName(u"input_nome_popup_oficinas_as")
        self.input_nome_popup_oficinas_as.setMinimumSize(QSize(0, 35))
        self.input_nome_popup_oficinas_as.setMaximumSize(QSize(16777215, 35))
        self.input_nome_popup_oficinas_as.setFont(font1)
        self.input_nome_popup_oficinas_as.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.input_nome_popup_oficinas_as)


        self.gridLayout_2.addWidget(self.frame_6, 2, 0, 1, 2)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_Email_popup_oficinas_as = QLabel(self.frame_7)
        self.label_Email_popup_oficinas_as.setObjectName(u"label_Email_popup_oficinas_as")
        self.label_Email_popup_oficinas_as.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_Email_popup_oficinas_as)

        self.input_Email_popup_oficinas_as = QLineEdit(self.frame_7)
        self.input_Email_popup_oficinas_as.setObjectName(u"input_Email_popup_oficinas_as")
        self.input_Email_popup_oficinas_as.setMinimumSize(QSize(0, 35))
        self.input_Email_popup_oficinas_as.setMaximumSize(QSize(16777215, 35))
        self.input_Email_popup_oficinas_as.setFont(font1)
        self.input_Email_popup_oficinas_as.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.input_Email_popup_oficinas_as)


        self.gridLayout_2.addWidget(self.frame_7, 3, 0, 1, 2)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_Telefone_popup_oficinas_as = QLabel(self.frame_8)
        self.label_Telefone_popup_oficinas_as.setObjectName(u"label_Telefone_popup_oficinas_as")
        self.label_Telefone_popup_oficinas_as.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_Telefone_popup_oficinas_as)

        self.input_Telefone_popup_oficinas_as = QLineEdit(self.frame_8)
        self.input_Telefone_popup_oficinas_as.setObjectName(u"input_Telefone_popup_oficinas_as")
        self.input_Telefone_popup_oficinas_as.setMinimumSize(QSize(0, 35))
        self.input_Telefone_popup_oficinas_as.setMaximumSize(QSize(16777215, 35))
        self.input_Telefone_popup_oficinas_as.setFont(font1)
        self.input_Telefone_popup_oficinas_as.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.input_Telefone_popup_oficinas_as)


        self.gridLayout_2.addWidget(self.frame_8, 4, 0, 1, 1)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_cep_popup_oficinas_as = QLabel(self.frame_9)
        self.label_cep_popup_oficinas_as.setObjectName(u"label_cep_popup_oficinas_as")
        self.label_cep_popup_oficinas_as.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_cep_popup_oficinas_as)

        self.input_cep_popup_oficinas_as = QLineEdit(self.frame_9)
        self.input_cep_popup_oficinas_as.setObjectName(u"input_cep_popup_oficinas_as")
        self.input_cep_popup_oficinas_as.setMinimumSize(QSize(0, 35))
        self.input_cep_popup_oficinas_as.setMaximumSize(QSize(16777215, 35))
        self.input_cep_popup_oficinas_as.setFont(font1)
        self.input_cep_popup_oficinas_as.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.input_cep_popup_oficinas_as)


        self.gridLayout_2.addWidget(self.frame_9, 4, 1, 1, 1)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_rua_popup_oficinas_as = QLabel(self.frame_10)
        self.label_rua_popup_oficinas_as.setObjectName(u"label_rua_popup_oficinas_as")
        self.label_rua_popup_oficinas_as.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_rua_popup_oficinas_as)

        self.input_rua_popup_oficinas_as = QLineEdit(self.frame_10)
        self.input_rua_popup_oficinas_as.setObjectName(u"input_rua_popup_oficinas_as")
        self.input_rua_popup_oficinas_as.setMinimumSize(QSize(0, 35))
        self.input_rua_popup_oficinas_as.setMaximumSize(QSize(16777215, 35))
        self.input_rua_popup_oficinas_as.setFont(font1)
        self.input_rua_popup_oficinas_as.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.input_rua_popup_oficinas_as)


        self.gridLayout_2.addWidget(self.frame_10, 5, 0, 1, 2)

        self.frame_11 = QFrame(self.frame_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_bairro_popup_oficinas_as = QLabel(self.frame_11)
        self.label_bairro_popup_oficinas_as.setObjectName(u"label_bairro_popup_oficinas_as")
        self.label_bairro_popup_oficinas_as.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_bairro_popup_oficinas_as)

        self.input_bairro_popup_oficinas_as = QLineEdit(self.frame_11)
        self.input_bairro_popup_oficinas_as.setObjectName(u"input_bairro_popup_oficinas_as")
        self.input_bairro_popup_oficinas_as.setMinimumSize(QSize(0, 35))
        self.input_bairro_popup_oficinas_as.setMaximumSize(QSize(16777215, 35))
        self.input_bairro_popup_oficinas_as.setFont(font1)
        self.input_bairro_popup_oficinas_as.setStyleSheet(u"")

        self.verticalLayout_10.addWidget(self.input_bairro_popup_oficinas_as)


        self.gridLayout_2.addWidget(self.frame_11, 6, 0, 1, 2)

        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_cidade_popup_oficinas_as_2 = QLabel(self.frame_12)
        self.label_cidade_popup_oficinas_as_2.setObjectName(u"label_cidade_popup_oficinas_as_2")
        self.label_cidade_popup_oficinas_as_2.setFont(font1)

        self.verticalLayout_11.addWidget(self.label_cidade_popup_oficinas_as_2)

        self.input_cidade_popup_oficinas_as = QLineEdit(self.frame_12)
        self.input_cidade_popup_oficinas_as.setObjectName(u"input_cidade_popup_oficinas_as")
        self.input_cidade_popup_oficinas_as.setMinimumSize(QSize(0, 35))
        self.input_cidade_popup_oficinas_as.setMaximumSize(QSize(16777215, 35))
        self.input_cidade_popup_oficinas_as.setFont(font1)
        self.input_cidade_popup_oficinas_as.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.input_cidade_popup_oficinas_as)


        self.gridLayout_2.addWidget(self.frame_12, 7, 0, 1, 2)

        self.frame_13 = QFrame(self.frame_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_13)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_estado_popup_oficinas_as_3 = QLabel(self.frame_13)
        self.label_estado_popup_oficinas_as_3.setObjectName(u"label_estado_popup_oficinas_as_3")
        self.label_estado_popup_oficinas_as_3.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_estado_popup_oficinas_as_3)

        self.input_estado_popup_oficinas_as_3 = QLineEdit(self.frame_13)
        self.input_estado_popup_oficinas_as_3.setObjectName(u"input_estado_popup_oficinas_as_3")
        self.input_estado_popup_oficinas_as_3.setMinimumSize(QSize(0, 35))
        self.input_estado_popup_oficinas_as_3.setMaximumSize(QSize(16777215, 35))
        self.input_estado_popup_oficinas_as_3.setFont(font1)
        self.input_estado_popup_oficinas_as_3.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.input_estado_popup_oficinas_as_3)


        self.gridLayout_2.addWidget(self.frame_13, 8, 0, 1, 2)


        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_15 = QFrame(self.frame_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.btn_fechar_popup_oficinas_as_2 = QPushButton(self.frame_15)
        self.btn_fechar_popup_oficinas_as_2.setObjectName(u"btn_fechar_popup_oficinas_as_2")
        self.btn_fechar_popup_oficinas_as_2.setMinimumSize(QSize(120, 40))
        self.btn_fechar_popup_oficinas_as_2.setMaximumSize(QSize(120, 40))
        font3 = QFont()
        font3.setFamilies([u"Abel"])
        font3.setPointSize(20)
        self.btn_fechar_popup_oficinas_as_2.setFont(font3)
        self.btn_fechar_popup_oficinas_as_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_fechar_popup_oficinas_as_2.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px; border: none}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout_7.addWidget(self.btn_fechar_popup_oficinas_as_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.btn_remover_popup_oficinas_as_2 = QPushButton(self.frame_15)
        self.btn_remover_popup_oficinas_as_2.setObjectName(u"btn_remover_popup_oficinas_as_2")
        self.btn_remover_popup_oficinas_as_2.setMinimumSize(QSize(120, 40))
        self.btn_remover_popup_oficinas_as_2.setMaximumSize(QSize(120, 40))
        self.btn_remover_popup_oficinas_as_2.setFont(font3)
        self.btn_remover_popup_oficinas_as_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remover_popup_oficinas_as_2.setStyleSheet(u"QPushButton{color: #fff; background-color: #F7B0B5; border-radius: 20px; border: none}\n"
"QPushButton:hover{background-color: #EC848C}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout_7.addWidget(self.btn_remover_popup_oficinas_as_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.btn_adicionar_popup_oficinas_as_2 = QPushButton(self.frame_15)
        self.btn_adicionar_popup_oficinas_as_2.setObjectName(u"btn_adicionar_popup_oficinas_as_2")
        self.btn_adicionar_popup_oficinas_as_2.setMinimumSize(QSize(120, 40))
        self.btn_adicionar_popup_oficinas_as_2.setMaximumSize(QSize(120, 40))
        self.btn_adicionar_popup_oficinas_as_2.setFont(font3)
        self.btn_adicionar_popup_oficinas_as_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adicionar_popup_oficinas_as_2.setStyleSheet(u"QPushButton{color: #fff; background-color: #FF3636; border-radius: 20px; border: none}\n"
"QPushButton:hover{background-color: #EC848C}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout_7.addWidget(self.btn_adicionar_popup_oficinas_as_2)


        self.gridLayout.addWidget(self.frame_15, 1, 0, 1, 3)

        self.frame_17 = QFrame(self.frame_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_17)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_20 = QFrame(self.frame_17)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.label_Lista_de_Convidados_popup_oficinas_as = QLabel(self.frame_20)
        self.label_Lista_de_Convidados_popup_oficinas_as.setObjectName(u"label_Lista_de_Convidados_popup_oficinas_as")
        self.label_Lista_de_Convidados_popup_oficinas_as.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_Lista_de_Convidados_popup_oficinas_as)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)


        self.verticalLayout_13.addWidget(self.frame_20)

        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_18)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.tabela_lista_de_cadastro_Oficinas_as = QTableWidget(self.frame_18)
        if (self.tabela_lista_de_cadastro_Oficinas_as.columnCount() < 6):
            self.tabela_lista_de_cadastro_Oficinas_as.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setBackground(QColor(255, 198, 201));
        self.tabela_lista_de_cadastro_Oficinas_as.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        __qtablewidgetitem1.setBackground(QColor(255, 198, 201));
        self.tabela_lista_de_cadastro_Oficinas_as.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        __qtablewidgetitem2.setBackground(QColor(255, 198, 201));
        self.tabela_lista_de_cadastro_Oficinas_as.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tabela_lista_de_cadastro_Oficinas_as.rowCount() < 5):
            self.tabela_lista_de_cadastro_Oficinas_as.setRowCount(5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setItem(0, 0, __qtablewidgetitem11)
        self.tabela_lista_de_cadastro_Oficinas_as.setObjectName(u"tabela_lista_de_cadastro_Oficinas_as")
        self.tabela_lista_de_cadastro_Oficinas_as.setFont(font1)
        self.tabela_lista_de_cadastro_Oficinas_as.setStyleSheet(u"QTableWidget{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;scrollbar-width: thin;\n"
"  scrollbar-color: #F9EDEC;}\n"
"QTableWidgetfocus{outline:0; border: 2px solid #A85751}\n"
"")
        self.tabela_lista_de_cadastro_Oficinas_as.setFrameShadow(QFrame.Sunken)
        self.tabela_lista_de_cadastro_Oficinas_as.setLineWidth(1)
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tabela_lista_de_cadastro_Oficinas_as.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabela_lista_de_cadastro_Oficinas_as.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tabela_lista_de_cadastro_Oficinas_as.setAlternatingRowColors(True)
        self.tabela_lista_de_cadastro_Oficinas_as.setShowGrid(True)
        self.tabela_lista_de_cadastro_Oficinas_as.setGridStyle(Qt.SolidLine)
        self.tabela_lista_de_cadastro_Oficinas_as.setSortingEnabled(False)
        self.tabela_lista_de_cadastro_Oficinas_as.setWordWrap(False)
        self.tabela_lista_de_cadastro_Oficinas_as.setCornerButtonEnabled(False)
        self.tabela_lista_de_cadastro_Oficinas_as.verticalHeader().setHighlightSections(True)
        self.tabela_lista_de_cadastro_Oficinas_as.verticalHeader().setProperty("showSortIndicator", True)
        self.tabela_lista_de_cadastro_Oficinas_as.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_15.addWidget(self.tabela_lista_de_cadastro_Oficinas_as)


        self.verticalLayout_13.addWidget(self.frame_18)


        self.gridLayout.addWidget(self.frame_17, 0, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_cadastro_popup_oficinas_as.setText(QCoreApplication.translate("Dialog", u"Cadastro", None))
        self.label_cpf_popup_oficinas_as.setText(QCoreApplication.translate("Dialog", u"CPF", None))
        self.label_tipo_popup_oficinas_as.setText(QCoreApplication.translate("Dialog", u"Tipo", None))
        self.label_nome_popup_oficinas_as.setText(QCoreApplication.translate("Dialog", u"Nome", None))
        self.label_Email_popup_oficinas_as.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.label_Telefone_popup_oficinas_as.setText(QCoreApplication.translate("Dialog", u"Telefone", None))
        self.input_Telefone_popup_oficinas_as.setText("")
        self.label_cep_popup_oficinas_as.setText(QCoreApplication.translate("Dialog", u"CEP", None))
        self.label_rua_popup_oficinas_as.setText(QCoreApplication.translate("Dialog", u"Rua", None))
        self.label_bairro_popup_oficinas_as.setText(QCoreApplication.translate("Dialog", u"Bairro", None))
        self.label_cidade_popup_oficinas_as_2.setText(QCoreApplication.translate("Dialog", u"Cidade", None))
        self.label_estado_popup_oficinas_as_3.setText(QCoreApplication.translate("Dialog", u"Estado", None))
        self.btn_fechar_popup_oficinas_as_2.setText(QCoreApplication.translate("Dialog", u"Fechar", None))
        self.btn_remover_popup_oficinas_as_2.setText(QCoreApplication.translate("Dialog", u"Remover", None))
        self.btn_adicionar_popup_oficinas_as_2.setText(QCoreApplication.translate("Dialog", u"Adicionar", None))
        self.label_Lista_de_Convidados_popup_oficinas_as.setText(QCoreApplication.translate("Dialog", u"Lista de Convidados", None))
        ___qtablewidgetitem = self.tabela_lista_de_cadastro_Oficinas_as.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Nome", None));
        ___qtablewidgetitem1 = self.tabela_lista_de_cadastro_Oficinas_as.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"CPF", None));
        ___qtablewidgetitem2 = self.tabela_lista_de_cadastro_Oficinas_as.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Tipo", None));

        __sortingEnabled = self.tabela_lista_de_cadastro_Oficinas_as.isSortingEnabled()
        self.tabela_lista_de_cadastro_Oficinas_as.setSortingEnabled(False)
        self.tabela_lista_de_cadastro_Oficinas_as.setSortingEnabled(__sortingEnabled)

    # retranslateUi

