# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'telas_abrecioVHjO.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtcore import * 
from icons import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        ############ valida email ##############
        self.validaEmail = QRegularExpressionValidator(QRegularExpression("([a-z0-9]+[.-_])*[a-z0-9]+@[a-z]+(\\.[a-z]{2,})+"))
        ########################################
        
        #MainWindow.resize(2130, 917)
        font = QFont()
        font.setFamilies([u"Abel"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_177 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_177.setObjectName(u"verticalLayout_177")
        self.verticalLayout_177.setContentsMargins(0, 0, 0, 0)
        self.inicio = QStackedWidget(self.centralwidget)
        self.inicio.setObjectName(u"inicio")
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"QWidget { background-color: #F9D9DD\n"
"}")
        self.horizontalLayout_32 = QHBoxLayout(self.login)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalSpacer = QSpacerItem(452, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer)

        self.frame = QFrame(self.login)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(450, 0))
        self.frame.setMaximumSize(QSize(16777215, 498))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.frame)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"QFrame#frame_35 {background-color: #FA5858; border-top-left-radius: 8px; border-top-right-radius: 8px}")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_33 = QSpacerItem(163, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_33)

        self.label_5 = QLabel(self.frame_35)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setFamilies([u"Abel"])
        font1.setPointSize(36)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: #fff; background-color: #FA5858")

        self.horizontalLayout_27.addWidget(self.label_5)

        self.horizontalSpacer_34 = QSpacerItem(163, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_34)


        self.verticalLayout_21.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"QFrame {background-color: #F8EDEB}")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_36)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_9 = QSpacerItem(20, 49, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_9)

        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_35 = QSpacerItem(36, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_35)

        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 0))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_38)
        self.verticalLayout_26.setSpacing(45)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(370, 60))
        self.frame_39.setStyleSheet(u"QFrame#frame_39{background-color: #fff; border-radius: 30px; padding-left: 16px; padding-right: 16px}\n"
"QFrame#frame_39:hover{border: 1px solid #D62828}\n"
"QFrame#frame_39:focus{outline:0; border: 2px solid #D62828}")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_29.setSpacing(16)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.input_usuario_login = QLineEdit(self.frame_39)
        self.input_usuario_login.setObjectName(u"input_usuario_login")
        self.input_usuario_login.setMinimumSize(QSize(0, 0))
        self.input_usuario_login.setMaximumSize(QSize(16777215, 54))
        font2 = QFont()
        font2.setFamilies([u"Abel"])
        font2.setPointSize(20)
        self.input_usuario_login.setFont(font2)
        self.input_usuario_login.setStyleSheet(u"QLineEdit{border-radius: 27px; background-color: #fff}")

        self.horizontalLayout_29.addWidget(self.input_usuario_login)

        self.label_2 = QLabel(self.frame_39)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(25, 25))
        self.label_2.setStyleSheet(u"QLabel{border-radius: 16px; background-color: #fff}")
        self.label_2.setPixmap(QPixmap(u"./icons/pessoas.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.label_2)

        self.horizontalLayout_29.setStretch(0, 8)
        self.horizontalLayout_29.setStretch(1, 1)

        self.verticalLayout_26.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.frame_38)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(370, 60))
        self.frame_40.setStyleSheet(u"QFrame#frame_40{background-color: #fff; border-radius: 30px; padding-left: 16px; padding-right: 16px}\n"
"QFrame#frame_40:hover{border: 1px solid #D62828}\n"
"QFrame#frame_40:focus{outline:0; border: 2px solid #D62828}")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_30.setSpacing(16)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.input_senha_login = QLineEdit(self.frame_40)
        self.input_senha_login.setObjectName(u"input_senha_login")
        self.input_senha_login.setMinimumSize(QSize(0, 0))
        self.input_senha_login.setMaximumSize(QSize(16777215, 54))
        self.input_senha_login.setFont(font2)
        self.input_senha_login.setStyleSheet(u"QLineEdit{border-radius: 27px; background-color: #fff}")

        self.horizontalLayout_30.addWidget(self.input_senha_login)

        self.toolButton = QToolButton(self.frame_40)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton.setStyleSheet(u"background-color: #fff; border: hidden")
        icon = QIcon()
        icon.addFile(u"./icons/olho_fechado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_30.addWidget(self.toolButton)

        self.horizontalLayout_30.setStretch(0, 8)

        self.verticalLayout_26.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.frame_38)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_36 = QSpacerItem(101, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_36)

        self.btn_entrar_login = QPushButton(self.frame_41)
        self.btn_entrar_login.setObjectName(u"btn_entrar_login")
        self.btn_entrar_login.setMinimumSize(QSize(160, 50))
        self.btn_entrar_login.setMaximumSize(QSize(160, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Abel"])
        font3.setPointSize(24)
        self.btn_entrar_login.setFont(font3)
        self.btn_entrar_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_entrar_login.setStyleSheet(u"QPushButton{color: #fff; background-color: #D62828; border-radius: 25px}\n"
"QPushButton:hover{background-color: hsl(0, 69%, 45%)}\n"
"QPushButton:focus{outline: 0}")

        self.horizontalLayout_31.addWidget(self.btn_entrar_login)

        self.horizontalSpacer_37 = QSpacerItem(101, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_37)


        self.verticalLayout_26.addWidget(self.frame_41)


        self.horizontalLayout_28.addWidget(self.frame_38)

        self.horizontalSpacer_38 = QSpacerItem(36, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_38)


        self.verticalLayout_25.addWidget(self.frame_37)

        self.frame_137 = QFrame(self.frame_36)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setFrameShape(QFrame.StyledPanel)
        self.frame_137.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_137)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_47)

        self.btn_esqueci_senha_login = QPushButton(self.frame_137)
        self.btn_esqueci_senha_login.setObjectName(u"btn_esqueci_senha_login")
        self.btn_esqueci_senha_login.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(12)
        font4.setUnderline(True)
        self.btn_esqueci_senha_login.setFont(font4)
        self.btn_esqueci_senha_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_esqueci_senha_login.setStyleSheet(u" QPushButton{background-color: #F8EDEB; text-decoration: underline; border: none; margin-top:0.5em} \n"
" QPushButton: hover{color:#D62828}\n"
"QPushButton:focus{outline: 0} ")

        self.horizontalLayout_60.addWidget(self.btn_esqueci_senha_login)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_46)


        self.verticalLayout_25.addWidget(self.frame_137)

        self.verticalSpacer_10 = QSpacerItem(20, 49, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_10)


        self.verticalLayout_21.addWidget(self.frame_36)

        self.verticalLayout_21.setStretch(0, 1)
        self.verticalLayout_21.setStretch(1, 3)

        self.horizontalLayout_32.addWidget(self.frame)

        self.horizontalSpacer_2 = QSpacerItem(452, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_2)

        self.inicio.addWidget(self.login)
        self.area_principal = QWidget()
        self.area_principal.setObjectName(u"area_principal")
        self.area_principal.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
#"QComboBox{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751}\n"

"QComboBox{color: #A85751; border-radius: 10px; border-width: 1px; border-style: solid; border-color:#A85751; padding-left: 10px;}"
"QComboBox:drop-down:hover{background-color:#fff}"
"QComboBox:drop-down{width: 24px; border-top-right-radius:9px; border-bottom-right-radius:9px; border-top-left-radius:1px; border-bottom-left-radius:1px;}"
"QComboBox:down-arrow{image: url(icons/expand.svg); }"
"")
        self.gridLayout = QGridLayout(self.area_principal)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tipos_acesso = QStackedWidget(self.area_principal)
        self.tipos_acesso.setObjectName(u"tipos_acesso")
        self.assistente_social = QWidget()
        self.assistente_social.setObjectName(u"assistente_social")
        self.verticalLayout = QVBoxLayout(self.assistente_social)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stack_assistente = QStackedWidget(self.assistente_social)
        self.stack_assistente.setObjectName(u"stack_assistente")
        self.home_as = QWidget()
        self.home_as.setObjectName(u"home_as")
        self.horizontalLayout_9 = QHBoxLayout(self.home_as)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.home_as)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(226, 892))
        self.frame_9.setStyleSheet(u"QFrame{background-color: #E33B4E}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setSpacing(16)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_foto_as = QLabel(self.frame_9)
        self.label_foto_as.setObjectName(u"label_foto_as")
        self.label_foto_as.setMinimumSize(QSize(140, 180))
        self.label_foto_as.setLayoutDirection(Qt.RightToLeft)
        self.label_foto_as.setStyleSheet(u"QLabel{margin-top: 42px}")
        self.label_foto_as.setPixmap(QPixmap(u"./icons/Ellipse 1.png"))
        self.label_foto_as.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_foto_as)

        self.label_ola_nome_as = QLabel(self.frame_9)
        self.label_ola_nome_as.setObjectName(u"label_ola_nome_as")
        self.label_ola_nome_as.setFont(font2)
        self.label_ola_nome_as.setStyleSheet(u"color: #fff;margin-bottom: 1em;")
        self.label_ola_nome_as.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_ola_nome_as)

        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 0))
        self.frame_13.setStyleSheet(u"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_43)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 340))
        self.frame_14.setMaximumSize(QSize(16777215, 340))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_14)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 10, 0, 10)
        self.btn_cadastrar_as = QPushButton(self.frame_14)
        self.btn_cadastrar_as.setObjectName(u"btn_cadastrar_as")
        self.btn_cadastrar_as.setMinimumSize(QSize(140, 45))
        self.btn_cadastrar_as.setMaximumSize(QSize(140, 45))
        font5 = QFont()
        font5.setFamilies([u"Six Caps"])
        font5.setPointSize(24)
        self.btn_cadastrar_as.setFont(font5)
        self.btn_cadastrar_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_as.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon1 = QIcon()
        icon1.addFile(u"./icons/cadastro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar_as.setIcon(icon1)
        self.btn_cadastrar_as.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.btn_cadastrar_as)

        self.btn_consulta_as = QPushButton(self.frame_14)
        self.btn_consulta_as.setObjectName(u"btn_consulta_as")
        self.btn_consulta_as.setMinimumSize(QSize(140, 45))
        self.btn_consulta_as.setMaximumSize(QSize(140, 45))
        self.btn_consulta_as.setFont(font5)
        self.btn_consulta_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_consulta_as.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon2 = QIcon()
        icon2.addFile(u"./icons/consultando.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_consulta_as.setIcon(icon2)
        self.btn_consulta_as.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.btn_consulta_as)

        self.btn_agenda_as = QPushButton(self.frame_14)
        self.btn_agenda_as.setObjectName(u"btn_agenda_as")
        self.btn_agenda_as.setMinimumSize(QSize(140, 45))
        self.btn_agenda_as.setMaximumSize(QSize(140, 45))
        self.btn_agenda_as.setFont(font5)
        self.btn_agenda_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agenda_as.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon3 = QIcon()
        icon3.addFile(u"./icons/agenda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agenda_as.setIcon(icon3)
        self.btn_agenda_as.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.btn_agenda_as)

        self.btn_relatorios_as = QPushButton(self.frame_14)
        self.btn_relatorios_as.setObjectName(u"btn_relatorios_as")
        self.btn_relatorios_as.setMinimumSize(QSize(140, 45))
        self.btn_relatorios_as.setMaximumSize(QSize(140, 45))
        self.btn_relatorios_as.setFont(font5)
        self.btn_relatorios_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_relatorios_as.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon4 = QIcon()
        icon4.addFile(u"./icons/relatorio-de-negocios.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_relatorios_as.setIcon(icon4)
        self.btn_relatorios_as.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.btn_relatorios_as)

        self.btn_comunidade_as = QPushButton(self.frame_14)
        self.btn_comunidade_as.setObjectName(u"btn_comunidade_as")
        self.btn_comunidade_as.setMinimumSize(QSize(140, 45))
        self.btn_comunidade_as.setMaximumSize(QSize(140, 45))
        self.btn_comunidade_as.setFont(font5)
        self.btn_comunidade_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_comunidade_as.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px;}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon5 = QIcon()
        icon5.addFile(u"./icons/cliente.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_comunidade_as.setIcon(icon5)
        self.btn_comunidade_as.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.btn_comunidade_as)


        self.horizontalLayout_35.addWidget(self.frame_14)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_44)


        self.verticalLayout_6.addWidget(self.frame_13)

        self.verticalSpacer_3 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.frame_49 = QFrame(self.frame_9)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.frame_11 = QFrame(self.frame_49)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_11)
        self.verticalLayout_34.setSpacing(15)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 15)
        self.btn_voltar_as = QPushButton(self.frame_11)
        self.btn_voltar_as.setObjectName(u"btn_voltar_as")
        self.btn_voltar_as.setMinimumSize(QSize(120, 40))
        self.btn_voltar_as.setMaximumSize(QSize(120, 40))
        self.btn_voltar_as.setFont(font2)
        self.btn_voltar_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.verticalLayout_34.addWidget(self.btn_voltar_as)

        self.btn_sair_as = QPushButton(self.frame_11)
        self.btn_sair_as.setObjectName(u"btn_sair_as")
        self.btn_sair_as.setMinimumSize(QSize(120, 40))
        self.btn_sair_as.setMaximumSize(QSize(120, 40))
        self.btn_sair_as.setFont(font2)
        self.btn_sair_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sair_as.setLayoutDirection(Qt.RightToLeft)
        self.btn_sair_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #FF3636; border-radius: 20px;}\n"
"QPushButton:hover{background-color: 	hsl(0, 100%, 64%)}\n"
"QPushButton:focus{outline:0}")
        icon6 = QIcon()
        icon6.addFile(u"./icons/ligar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sair_as.setIcon(icon6)
        self.btn_sair_as.setIconSize(QSize(24, 24))

        self.verticalLayout_34.addWidget(self.btn_sair_as)


        self.horizontalLayout_10.addWidget(self.frame_11)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)


        self.verticalLayout_6.addWidget(self.frame_49)


        self.horizontalLayout_9.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.home_as)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QFrame{background-color: #F9D9DD}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.frame_10)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_principal_as = QWidget()
        self.page_principal_as.setObjectName(u"page_principal_as")
        self.stackedWidget_2.addWidget(self.page_principal_as)
        self.page_botoes_cadastrar_as = QWidget()
        self.page_botoes_cadastrar_as.setObjectName(u"page_botoes_cadastrar_as")
        self.page_botoes_cadastrar_as.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_40 = QHBoxLayout(self.page_botoes_cadastrar_as)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_29)

        self.frame_32 = QFrame(self.page_botoes_cadastrar_as)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 0))
        self.frame_32.setLayoutDirection(Qt.LeftToRight)
        self.frame_32.setStyleSheet(u"QFrame{padding: 3em;}")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_32)
        self.verticalLayout_23.setSpacing(40)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.btn_cadastrar_cuidador_usuario_as = QPushButton(self.frame_32)
        self.btn_cadastrar_cuidador_usuario_as.setObjectName(u"btn_cadastrar_cuidador_usuario_as")
        self.btn_cadastrar_cuidador_usuario_as.setMinimumSize(QSize(700, 154))
        self.btn_cadastrar_cuidador_usuario_as.setMaximumSize(QSize(700, 154))
        font6 = QFont()
        font6.setFamilies([u"Six Caps"])
        font6.setPointSize(60)
        self.btn_cadastrar_cuidador_usuario_as.setFont(font6)
        self.btn_cadastrar_cuidador_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_cuidador_usuario_as.setLayoutDirection(Qt.RightToLeft)
        self.btn_cadastrar_cuidador_usuario_as.setStyleSheet(u"QPushButton{color: #EC848C; background-color: #FEE4E1; border-radius: 20px ;border: none; padding: 1.5em}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon7 = QIcon()
        icon7.addFile(u"./icons/cuidado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar_cuidador_usuario_as.setIcon(icon7)
        self.btn_cadastrar_cuidador_usuario_as.setIconSize(QSize(80, 80))

        self.verticalLayout_23.addWidget(self.btn_cadastrar_cuidador_usuario_as)

        self.btn_cadastrar_colaborador_as = QPushButton(self.frame_32)
        self.btn_cadastrar_colaborador_as.setObjectName(u"btn_cadastrar_colaborador_as")
        self.btn_cadastrar_colaborador_as.setMinimumSize(QSize(700, 154))
        self.btn_cadastrar_colaborador_as.setMaximumSize(QSize(700, 154))
        self.btn_cadastrar_colaborador_as.setFont(font6)
        self.btn_cadastrar_colaborador_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_colaborador_as.setLayoutDirection(Qt.RightToLeft)
        self.btn_cadastrar_colaborador_as.setStyleSheet(u"QPushButton{color: #EC848C; background-color: #FEE4E1; border-radius: 20px ;border: none; padding: 1.5em}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon8 = QIcon()
        icon8.addFile(u"./icons/unidos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar_colaborador_as.setIcon(icon8)
        self.btn_cadastrar_colaborador_as.setIconSize(QSize(80, 80))

        self.verticalLayout_23.addWidget(self.btn_cadastrar_colaborador_as)

        self.btn_cadastrar_cursos_oficinas_as = QPushButton(self.frame_32)
        self.btn_cadastrar_cursos_oficinas_as.setObjectName(u"btn_cadastrar_cursos_oficinas_as")
        self.btn_cadastrar_cursos_oficinas_as.setMinimumSize(QSize(700, 154))
        self.btn_cadastrar_cursos_oficinas_as.setMaximumSize(QSize(700, 154))
        self.btn_cadastrar_cursos_oficinas_as.setFont(font6)
        self.btn_cadastrar_cursos_oficinas_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_cursos_oficinas_as.setLayoutDirection(Qt.RightToLeft)
        self.btn_cadastrar_cursos_oficinas_as.setStyleSheet(u"QPushButton{color: #EC848C; background-color: #FEE4E1; border-radius: 20px ;border: none; padding: 1.5em}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon9 = QIcon()
        icon9.addFile(u"./icons/certificados.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar_cursos_oficinas_as.setIcon(icon9)
        self.btn_cadastrar_cursos_oficinas_as.setIconSize(QSize(80, 80))

        self.verticalLayout_23.addWidget(self.btn_cadastrar_cursos_oficinas_as)

        self.btn_cadastrar_alterar_dados_as = QPushButton(self.frame_32)
        self.btn_cadastrar_alterar_dados_as.setObjectName(u"btn_cadastrar_alterar_dados_as")
        self.btn_cadastrar_alterar_dados_as.setMinimumSize(QSize(700, 154))
        self.btn_cadastrar_alterar_dados_as.setMaximumSize(QSize(700, 154))
        self.btn_cadastrar_alterar_dados_as.setFont(font6)
        self.btn_cadastrar_alterar_dados_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_alterar_dados_as.setLayoutDirection(Qt.RightToLeft)
        self.btn_cadastrar_alterar_dados_as.setStyleSheet(u"QPushButton{color: #EC848C; background-color: #FEE4E1; border-radius: 20px ;border: none}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon10 = QIcon()
        icon10.addFile(u"./icons/troca.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar_alterar_dados_as.setIcon(icon10)
        self.btn_cadastrar_alterar_dados_as.setIconSize(QSize(80, 80))

        self.verticalLayout_23.addWidget(self.btn_cadastrar_alterar_dados_as)


        self.horizontalLayout_40.addWidget(self.frame_32)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_30)

        self.horizontalLayout_40.setStretch(0, 1)
        self.horizontalLayout_40.setStretch(1, 2)
        self.horizontalLayout_40.setStretch(2, 1)
        self.stackedWidget_2.addWidget(self.page_botoes_cadastrar_as)
        self.page_cadastro_usuario_as = QWidget()
        self.page_cadastro_usuario_as.setObjectName(u"page_cadastro_usuario_as")
        self.verticalLayout_3 = QVBoxLayout(self.page_cadastro_usuario_as)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.page_cadastro_usuario_as)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: #F3B9BF; margin-bottom: 2em")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: #EC848C; padding-top: 1.5em")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_cadastro_usuario_as)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(152, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QLabel{margin-left: 0.25em}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_foto_usuario_as = QPushButton(self.frame_6)
        self.btn_foto_usuario_as.setObjectName(u"btn_foto_usuario_as")
        self.btn_foto_usuario_as.setMinimumSize(QSize(125, 153))
        self.btn_foto_usuario_as.setMaximumSize(QSize(125, 153))
        self.btn_foto_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_foto_usuario_as.setStyleSheet(u"background-color: #F3B9BF; border: none")
        icon11 = QIcon()
        icon11.addFile(u"./icons/adicionar foto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_foto_usuario_as.setIcon(icon11)
        self.btn_foto_usuario_as.setIconSize(QSize(120, 120))

        self.horizontalLayout_6.addWidget(self.btn_foto_usuario_as)

        self.frame_46 = QFrame(self.frame_6)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMaximumSize(QSize(16777215, 200))
        self.frame_46.setStyleSheet(u"")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_46)
        self.verticalLayout_28.setSpacing(5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QFrame(self.frame_46)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMaximumSize(QSize(16777215, 60))
        self.frame_48.setLayoutDirection(Qt.LeftToRight)
        self.frame_48.setStyleSheet(u"")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_61 = QFrame(self.frame_48)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(160, 0))
        self.frame_61.setMaximumSize(QSize(160, 16777215))
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_61)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_matricula_usuario_as = QLabel(self.frame_61)
        self.label_matricula_usuario_as.setObjectName(u"label_matricula_usuario_as")
        self.label_matricula_usuario_as.setMinimumSize(QSize(160, 0))
        self.label_matricula_usuario_as.setMaximumSize(QSize(160, 16777215))
        self.label_matricula_usuario_as.setFont(font)
        self.label_matricula_usuario_as.setStyleSheet(u"")

        self.verticalLayout_29.addWidget(self.label_matricula_usuario_as)

        self.input_matricula_usuario_as = QLineEdit(self.frame_61)
        self.input_matricula_usuario_as.setObjectName(u"input_matricula_usuario_as")
        self.input_matricula_usuario_as.setMinimumSize(QSize(150, 30))
        self.input_matricula_usuario_as.setMaximumSize(QSize(150, 30))
        self.input_matricula_usuario_as.setFont(font)

        self.verticalLayout_29.addWidget(self.input_matricula_usuario_as)


        self.horizontalLayout_7.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.frame_48)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(460, 0))
        self.frame_62.setMaximumSize(QSize(460, 16777215))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_62)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_nome_usuario_as = QLabel(self.frame_62)
        self.label_nome_usuario_as.setObjectName(u"label_nome_usuario_as")
        self.label_nome_usuario_as.setMinimumSize(QSize(460, 0))
        self.label_nome_usuario_as.setMaximumSize(QSize(460, 16777215))
        self.label_nome_usuario_as.setFont(font)
        self.label_nome_usuario_as.setStyleSheet(u"")

        self.verticalLayout_30.addWidget(self.label_nome_usuario_as)

        self.input_nome_usuario_as = QLineEdit(self.frame_62)
        self.input_nome_usuario_as.setObjectName(u"input_nome_usuario_as")
        self.input_nome_usuario_as.setMinimumSize(QSize(450, 30))
        self.input_nome_usuario_as.setMaximumSize(QSize(450, 30))
        self.input_nome_usuario_as.setFont(font)

        self.verticalLayout_30.addWidget(self.input_nome_usuario_as)


        self.horizontalLayout_7.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.frame_48)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(160, 0))
        self.frame_63.setMaximumSize(QSize(160, 16777215))
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_63)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_nascimento_usuario_as = QLabel(self.frame_63)
        self.label_nascimento_usuario_as.setObjectName(u"label_nascimento_usuario_as")
        self.label_nascimento_usuario_as.setMinimumSize(QSize(160, 0))
        self.label_nascimento_usuario_as.setMaximumSize(QSize(160, 16777215))
        self.label_nascimento_usuario_as.setFont(font)
        self.label_nascimento_usuario_as.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_nascimento_usuario_as)

        self.input_nascimento_usuario_as = QLineEdit(self.frame_63)
        self.input_nascimento_usuario_as.setObjectName(u"input_nascimento_usuario_as")
        self.input_nascimento_usuario_as.setMinimumSize(QSize(150, 30))
        self.input_nascimento_usuario_as.setMaximumSize(QSize(150, 30))
        self.input_nascimento_usuario_as.setFont(font)

        self.verticalLayout_31.addWidget(self.input_nascimento_usuario_as)


        self.horizontalLayout_7.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.frame_48)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(195, 50))
        self.frame_64.setMaximumSize(QSize(195, 50))
        self.frame_64.setStyleSheet(u"background-color: #EC848C; border-radius: 10px")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_64)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(15, 0, 0, 0)
        self.label_situacao_usuario_as = QLabel(self.frame_64)
        self.label_situacao_usuario_as.setObjectName(u"label_situacao_usuario_as")
        self.label_situacao_usuario_as.setMaximumSize(QSize(130, 16777215))
        self.label_situacao_usuario_as.setFont(font)

        self.verticalLayout_32.addWidget(self.label_situacao_usuario_as)

        self.frame_65 = QFrame(self.frame_64)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.input_situacao_ativo_usuario_as = QRadioButton(self.frame_65)
        self.input_situacao_ativo_usuario_as.setObjectName(u"input_situacao_ativo_usuario_as")
        self.input_situacao_ativo_usuario_as.setMaximumSize(QSize(80, 16777215))
        font7 = QFont()
        font7.setFamilies([u"Abel"])
        font7.setPointSize(11)
        self.input_situacao_ativo_usuario_as.setFont(font7)
        self.input_situacao_ativo_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_33.addWidget(self.input_situacao_ativo_usuario_as)

        self.input_situacao_inativo_usuario_as = QRadioButton(self.frame_65)
        self.input_situacao_inativo_usuario_as.setObjectName(u"input_situacao_inativo_usuario_as")
        self.input_situacao_inativo_usuario_as.setMaximumSize(QSize(80, 16777215))
        self.input_situacao_inativo_usuario_as.setFont(font7)
        self.input_situacao_inativo_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_33.addWidget(self.input_situacao_inativo_usuario_as)


        self.verticalLayout_32.addWidget(self.frame_65)


        self.horizontalLayout_7.addWidget(self.frame_64)


        self.verticalLayout_28.addWidget(self.frame_48)

        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMaximumSize(QSize(16777215, 60))
        self.frame_47.setStyleSheet(u"")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_34.setSpacing(5)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_66 = QFrame(self.frame_47)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(180, 0))
        self.frame_66.setMaximumSize(QSize(180, 16777215))
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_66)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_cpf_usuario_as = QLabel(self.frame_66)
        self.label_cpf_usuario_as.setObjectName(u"label_cpf_usuario_as")
        self.label_cpf_usuario_as.setMinimumSize(QSize(180, 0))
        self.label_cpf_usuario_as.setMaximumSize(QSize(180, 16777215))
        self.label_cpf_usuario_as.setFont(font)

        self.verticalLayout_33.addWidget(self.label_cpf_usuario_as)

        self.input_cpf_usuario_as = QLineEdit(self.frame_66)
        self.input_cpf_usuario_as.setObjectName(u"input_cpf_usuario_as")
        self.input_cpf_usuario_as.setMinimumSize(QSize(170, 30))
        self.input_cpf_usuario_as.setMaximumSize(QSize(170, 30))
        self.input_cpf_usuario_as.setFont(font)

        self.verticalLayout_33.addWidget(self.input_cpf_usuario_as)


        self.horizontalLayout_34.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.frame_47)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(160, 0))
        self.frame_67.setMaximumSize(QSize(160, 16777215))
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_67)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_rg_usuario_as = QLabel(self.frame_67)
        self.label_rg_usuario_as.setObjectName(u"label_rg_usuario_as")
        self.label_rg_usuario_as.setMinimumSize(QSize(160, 0))
        self.label_rg_usuario_as.setMaximumSize(QSize(160, 16777215))
        self.label_rg_usuario_as.setFont(font)

        self.verticalLayout_40.addWidget(self.label_rg_usuario_as)

        self.input_rg_usuario_as = QLineEdit(self.frame_67)
        self.input_rg_usuario_as.setObjectName(u"input_rg_usuario_as")
        self.input_rg_usuario_as.setMinimumSize(QSize(150, 30))
        self.input_rg_usuario_as.setMaximumSize(QSize(150, 30))
        self.input_rg_usuario_as.setFont(font)

        self.verticalLayout_40.addWidget(self.input_rg_usuario_as)


        self.horizontalLayout_34.addWidget(self.frame_67)

        self.frame_68 = QFrame(self.frame_47)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(155, 0))
        self.frame_68.setMaximumSize(QSize(155, 16777215))
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_68)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_data_emissao_usuario_as = QLabel(self.frame_68)
        self.label_data_emissao_usuario_as.setObjectName(u"label_data_emissao_usuario_as")
        self.label_data_emissao_usuario_as.setMinimumSize(QSize(155, 0))
        self.label_data_emissao_usuario_as.setMaximumSize(QSize(155, 16777215))
        self.label_data_emissao_usuario_as.setFont(font)

        self.verticalLayout_41.addWidget(self.label_data_emissao_usuario_as)

        self.input_data_emissao_usuario_as = QLineEdit(self.frame_68)
        self.input_data_emissao_usuario_as.setObjectName(u"input_data_emissao_usuario_as")
        self.input_data_emissao_usuario_as.setMinimumSize(QSize(145, 30))
        self.input_data_emissao_usuario_as.setMaximumSize(QSize(145, 30))
        self.input_data_emissao_usuario_as.setFont(font)

        self.verticalLayout_41.addWidget(self.input_data_emissao_usuario_as)


        self.horizontalLayout_34.addWidget(self.frame_68)

        self.frame_69 = QFrame(self.frame_47)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(155, 0))
        self.frame_69.setMaximumSize(QSize(155, 16777215))
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_69)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_orgao_expedidor_usuario_as = QLabel(self.frame_69)
        self.label_orgao_expedidor_usuario_as.setObjectName(u"label_orgao_expedidor_usuario_as")
        self.label_orgao_expedidor_usuario_as.setMinimumSize(QSize(155, 0))
        self.label_orgao_expedidor_usuario_as.setMaximumSize(QSize(155, 16777215))
        self.label_orgao_expedidor_usuario_as.setFont(font)

        self.verticalLayout_42.addWidget(self.label_orgao_expedidor_usuario_as)

        self.input_orgao_expedidor_usuario_as = QLineEdit(self.frame_69)
        self.input_orgao_expedidor_usuario_as.setObjectName(u"input_orgao_expedidor_usuario_as")
        self.input_orgao_expedidor_usuario_as.setMinimumSize(QSize(145, 30))
        self.input_orgao_expedidor_usuario_as.setMaximumSize(QSize(145, 30))
        self.input_orgao_expedidor_usuario_as.setFont(font)

        self.verticalLayout_42.addWidget(self.input_orgao_expedidor_usuario_as)


        self.horizontalLayout_34.addWidget(self.frame_69)

        self.frame_70 = QFrame(self.frame_47)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(170, 0))
        self.frame_70.setMaximumSize(QSize(170, 16777215))
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_70)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_nis_usuario_as = QLabel(self.frame_70)
        self.label_nis_usuario_as.setObjectName(u"label_nis_usuario_as")
        self.label_nis_usuario_as.setMinimumSize(QSize(170, 0))
        self.label_nis_usuario_as.setMaximumSize(QSize(170, 16777215))
        self.label_nis_usuario_as.setFont(font)

        self.verticalLayout_43.addWidget(self.label_nis_usuario_as)

        self.input_nis_usuario_as = QLineEdit(self.frame_70)
        self.input_nis_usuario_as.setObjectName(u"input_nis_usuario_as")
        self.input_nis_usuario_as.setMinimumSize(QSize(160, 30))
        self.input_nis_usuario_as.setMaximumSize(QSize(160, 30))
        self.input_nis_usuario_as.setFont(font)

        self.verticalLayout_43.addWidget(self.input_nis_usuario_as)


        self.horizontalLayout_34.addWidget(self.frame_70)

        self.frame_71 = QFrame(self.frame_47)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMinimumSize(QSize(180, 0))
        self.frame_71.setMaximumSize(QSize(180, 16777215))
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_71)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_cns_usuario_as = QLabel(self.frame_71)
        self.label_cns_usuario_as.setObjectName(u"label_cns_usuario_as")
        self.label_cns_usuario_as.setMinimumSize(QSize(180, 0))
        self.label_cns_usuario_as.setMaximumSize(QSize(180, 16777215))
        self.label_cns_usuario_as.setFont(font)

        self.verticalLayout_44.addWidget(self.label_cns_usuario_as)

        self.input_cns_usuario_as = QLineEdit(self.frame_71)
        self.input_cns_usuario_as.setObjectName(u"input_cns_usuario_as")
        self.input_cns_usuario_as.setMinimumSize(QSize(170, 30))
        self.input_cns_usuario_as.setMaximumSize(QSize(170, 30))
        self.input_cns_usuario_as.setFont(font)
        self.input_cns_usuario_as.setInputMethodHints(Qt.ImhNone)

        self.verticalLayout_44.addWidget(self.input_cns_usuario_as)


        self.horizontalLayout_34.addWidget(self.frame_71)


        self.verticalLayout_28.addWidget(self.frame_47)

        self.frame_60 = QFrame(self.frame_46)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMaximumSize(QSize(16777215, 60))
        font8 = QFont()
        font8.setPointSize(7)
        self.frame_60.setFont(font8)
        self.frame_60.setStyleSheet(u"")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_41.setSpacing(5)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_72 = QFrame(self.frame_60)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(155, 0))
        self.frame_72.setMaximumSize(QSize(155, 16777215))
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_72)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_sexo_usuario_as = QLabel(self.frame_72)
        self.label_sexo_usuario_as.setObjectName(u"label_sexo_usuario_as")
        self.label_sexo_usuario_as.setMinimumSize(QSize(155, 0))
        self.label_sexo_usuario_as.setMaximumSize(QSize(155, 16777215))
        self.label_sexo_usuario_as.setFont(font)

        self.verticalLayout_45.addWidget(self.label_sexo_usuario_as)

        self.input_sexo_usuario_as = QLineEdit(self.frame_72)
        self.input_sexo_usuario_as.setObjectName(u"input_sexo_usuario_as")
        self.input_sexo_usuario_as.setMinimumSize(QSize(145, 30))
        self.input_sexo_usuario_as.setMaximumSize(QSize(145, 30))
        self.input_sexo_usuario_as.setFont(font)

        self.verticalLayout_45.addWidget(self.input_sexo_usuario_as)


        self.horizontalLayout_41.addWidget(self.frame_72)

        self.frame_73 = QFrame(self.frame_60)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(155, 0))
        self.frame_73.setMaximumSize(QSize(155, 16777215))
        self.frame_73.setStyleSheet(u"")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_73)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_telefone_usuario_as = QLabel(self.frame_73)
        self.label_telefone_usuario_as.setObjectName(u"label_telefone_usuario_as")
        self.label_telefone_usuario_as.setMinimumSize(QSize(155, 0))
        self.label_telefone_usuario_as.setMaximumSize(QSize(155, 16777215))
        self.label_telefone_usuario_as.setFont(font)

        self.verticalLayout_46.addWidget(self.label_telefone_usuario_as)

        self.input_telefone_usuario_as = QLineEdit(self.frame_73)
        self.input_telefone_usuario_as.setObjectName(u"input_telefone_usuario_as")
        self.input_telefone_usuario_as.setMinimumSize(QSize(145, 30))
        self.input_telefone_usuario_as.setMaximumSize(QSize(145, 30))
        self.input_telefone_usuario_as.setFont(font)

        self.verticalLayout_46.addWidget(self.input_telefone_usuario_as)


        self.horizontalLayout_41.addWidget(self.frame_73)

        self.frame_74 = QFrame(self.frame_60)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMinimumSize(QSize(240, 0))
        self.frame_74.setMaximumSize(QSize(240, 16777215))
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_74)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_email_usuario_as = QLabel(self.frame_74)
        self.label_email_usuario_as.setObjectName(u"label_email_usuario_as")
        self.label_email_usuario_as.setMinimumSize(QSize(240, 0))
        self.label_email_usuario_as.setMaximumSize(QSize(240, 16777215))
        self.label_email_usuario_as.setFont(font)

        self.verticalLayout_47.addWidget(self.label_email_usuario_as)

        self.input_email_usuario_as = QLineEdit(self.frame_74)
        self.input_email_usuario_as.setObjectName(u"input_email_usuario_as")
        self.input_email_usuario_as.setMinimumSize(QSize(230, 30))
        self.input_email_usuario_as.setMaximumSize(QSize(230, 30))
        self.input_email_usuario_as.setFont(font)

        self.verticalLayout_47.addWidget(self.input_email_usuario_as)


        self.horizontalLayout_41.addWidget(self.frame_74)

        self.frame_75 = QFrame(self.frame_60)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(160, 0))
        self.frame_75.setMaximumSize(QSize(160, 16777215))
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_75)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_cep_usuario_as = QLabel(self.frame_75)
        self.label_cep_usuario_as.setObjectName(u"label_cep_usuario_as")
        self.label_cep_usuario_as.setMinimumSize(QSize(160, 0))
        self.label_cep_usuario_as.setMaximumSize(QSize(160, 16777215))
        self.label_cep_usuario_as.setFont(font)

        self.verticalLayout_48.addWidget(self.label_cep_usuario_as)

        self.input_cep_usuario_as = QLineEdit(self.frame_75)
        self.input_cep_usuario_as.setObjectName(u"input_cep_usuario_as")
        self.input_cep_usuario_as.setMinimumSize(QSize(150, 30))
        self.input_cep_usuario_as.setMaximumSize(QSize(150, 30))
        self.input_cep_usuario_as.setFont(font)

        self.verticalLayout_48.addWidget(self.input_cep_usuario_as)


        self.horizontalLayout_41.addWidget(self.frame_75)

        self.frame_128 = QFrame(self.frame_60)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setMinimumSize(QSize(360, 0))
        self.frame_128.setMaximumSize(QSize(360, 16777215))
        self.frame_128.setFrameShape(QFrame.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_128)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.label_logradouro_usuario_as = QLabel(self.frame_128)
        self.label_logradouro_usuario_as.setObjectName(u"label_logradouro_usuario_as")
        self.label_logradouro_usuario_as.setMinimumSize(QSize(360, 0))
        self.label_logradouro_usuario_as.setMaximumSize(QSize(360, 16777215))
        self.label_logradouro_usuario_as.setFont(font)

        self.verticalLayout_87.addWidget(self.label_logradouro_usuario_as)

        self.input_logradouro_usuario_as = QLineEdit(self.frame_128)
        self.input_logradouro_usuario_as.setObjectName(u"input_logradouro_usuario_as")
        self.input_logradouro_usuario_as.setMinimumSize(QSize(350, 30))
        self.input_logradouro_usuario_as.setMaximumSize(QSize(350, 30))
        self.input_logradouro_usuario_as.setFont(font)
        self.input_logradouro_usuario_as.setStyleSheet(u"")

        self.verticalLayout_87.addWidget(self.input_logradouro_usuario_as)


        self.horizontalLayout_41.addWidget(self.frame_128)


        self.verticalLayout_28.addWidget(self.frame_60)


        self.horizontalLayout_6.addWidget(self.frame_46)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 60))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_42.setSpacing(5)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_77 = QFrame(self.frame_7)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(170, 0))
        self.frame_77.setMaximumSize(QSize(170, 16777215))
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_77)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_numero_usuario_as = QLabel(self.frame_77)
        self.label_numero_usuario_as.setObjectName(u"label_numero_usuario_as")
        self.label_numero_usuario_as.setMinimumSize(QSize(170, 0))
        self.label_numero_usuario_as.setMaximumSize(QSize(170, 16777215))
        self.label_numero_usuario_as.setFont(font)

        self.verticalLayout_52.addWidget(self.label_numero_usuario_as)

        self.input_numero_usuario_as = QLineEdit(self.frame_77)
        self.input_numero_usuario_as.setObjectName(u"input_numero_usuario_as")
        self.input_numero_usuario_as.setMinimumSize(QSize(150, 30))
        self.input_numero_usuario_as.setMaximumSize(QSize(150, 30))
        self.input_numero_usuario_as.setFont(font)

        self.verticalLayout_52.addWidget(self.input_numero_usuario_as)


        self.horizontalLayout_42.addWidget(self.frame_77)

        self.frame_80 = QFrame(self.frame_7)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMinimumSize(QSize(230, 0))
        self.frame_80.setMaximumSize(QSize(230, 16777215))
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_80)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_bairro_usuario_as = QLabel(self.frame_80)
        self.label_bairro_usuario_as.setObjectName(u"label_bairro_usuario_as")
        self.label_bairro_usuario_as.setMinimumSize(QSize(230, 0))
        self.label_bairro_usuario_as.setMaximumSize(QSize(230, 16777215))
        self.label_bairro_usuario_as.setFont(font)

        self.verticalLayout_53.addWidget(self.label_bairro_usuario_as)

        self.input_bairro_usuario_as = QLineEdit(self.frame_80)
        self.input_bairro_usuario_as.setObjectName(u"input_bairro_usuario_as")
        self.input_bairro_usuario_as.setMinimumSize(QSize(220, 30))
        self.input_bairro_usuario_as.setMaximumSize(QSize(220, 30))
        self.input_bairro_usuario_as.setFont(font)

        self.verticalLayout_53.addWidget(self.input_bairro_usuario_as)


        self.horizontalLayout_42.addWidget(self.frame_80)

        self.frame_78 = QFrame(self.frame_7)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(240, 0))
        self.frame_78.setMaximumSize(QSize(240, 16777215))
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_78)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_cidade_usuario_as = QLabel(self.frame_78)
        self.label_cidade_usuario_as.setObjectName(u"label_cidade_usuario_as")
        self.label_cidade_usuario_as.setMinimumSize(QSize(240, 0))
        self.label_cidade_usuario_as.setMaximumSize(QSize(240, 16777215))
        self.label_cidade_usuario_as.setFont(font)

        self.verticalLayout_49.addWidget(self.label_cidade_usuario_as)

        self.input_cidade_usuario_as = QLineEdit(self.frame_78)
        self.input_cidade_usuario_as.setObjectName(u"input_cidade_usuario_as")
        self.input_cidade_usuario_as.setMinimumSize(QSize(230, 30))
        self.input_cidade_usuario_as.setMaximumSize(QSize(230, 30))
        self.input_cidade_usuario_as.setFont(font)

        self.verticalLayout_49.addWidget(self.input_cidade_usuario_as)


        self.horizontalLayout_42.addWidget(self.frame_78)

        self.frame_79 = QFrame(self.frame_7)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(80, 0))
        self.frame_79.setMaximumSize(QSize(80, 16777215))
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_79)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_estado_usuario_as = QLabel(self.frame_79)
        self.label_estado_usuario_as.setObjectName(u"label_estado_usuario_as")
        self.label_estado_usuario_as.setMinimumSize(QSize(80, 0))
        self.label_estado_usuario_as.setMaximumSize(QSize(80, 16777215))
        self.label_estado_usuario_as.setFont(font)

        self.verticalLayout_50.addWidget(self.label_estado_usuario_as)

        self.input_estado_usuario_as = QComboBox(self.frame_79)
        self.input_estado_usuario_as.setObjectName(u"input_estado_usuario_as")
        self.input_estado_usuario_as.setMinimumSize(QSize(70, 30))
        self.input_estado_usuario_as.setMaximumSize(QSize(70, 30))
        self.input_estado_usuario_as.setFont(font)
        self.input_estado_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_50.addWidget(self.input_estado_usuario_as)


        self.horizontalLayout_42.addWidget(self.frame_79)

        self.frame_76 = QFrame(self.frame_7)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(210, 0))
        self.frame_76.setMaximumSize(QSize(210, 16777215))
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_76)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_estado_civil_usuario_as = QLabel(self.frame_76)
        self.label_estado_civil_usuario_as.setObjectName(u"label_estado_civil_usuario_as")
        self.label_estado_civil_usuario_as.setMinimumSize(QSize(210, 0))
        self.label_estado_civil_usuario_as.setMaximumSize(QSize(210, 16777215))
        self.label_estado_civil_usuario_as.setFont(font)

        self.verticalLayout_51.addWidget(self.label_estado_civil_usuario_as)

        self.input_estado_civil_usuario_as = QComboBox(self.frame_76)
        self.input_estado_civil_usuario_as.setObjectName(u"input_estado_civil_usuario_as")
        self.input_estado_civil_usuario_as.setMinimumSize(QSize(200, 30))
        self.input_estado_civil_usuario_as.setMaximumSize(QSize(200, 30))
        self.input_estado_civil_usuario_as.setFont(font)
        self.input_estado_civil_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_51.addWidget(self.input_estado_civil_usuario_as)


        self.horizontalLayout_42.addWidget(self.frame_76)

        self.frame_129 = QFrame(self.frame_7)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setMinimumSize(QSize(290, 0))
        self.frame_129.setMaximumSize(QSize(290, 16777215))
        self.frame_129.setFrameShape(QFrame.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_129)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_escolaridade_usuario_as = QLabel(self.frame_129)
        self.label_escolaridade_usuario_as.setObjectName(u"label_escolaridade_usuario_as")
        self.label_escolaridade_usuario_as.setMinimumSize(QSize(290, 0))
        self.label_escolaridade_usuario_as.setMaximumSize(QSize(290, 16777215))
        self.label_escolaridade_usuario_as.setFont(font)

        self.verticalLayout_64.addWidget(self.label_escolaridade_usuario_as)

        self.input_escolaridade_usuario_as = QComboBox(self.frame_129)
        self.input_escolaridade_usuario_as.setObjectName(u"input_escolaridade_usuario_as")
        self.input_escolaridade_usuario_as.setMinimumSize(QSize(280, 30))
        self.input_escolaridade_usuario_as.setMaximumSize(QSize(280, 30))
        self.input_escolaridade_usuario_as.setFont(font)
        self.input_escolaridade_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_64.addWidget(self.input_escolaridade_usuario_as)


        self.horizontalLayout_42.addWidget(self.frame_129)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 60))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_43.setSpacing(5)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_90 = QFrame(self.frame_8)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(150, 0))
        self.frame_90.setMaximumSize(QSize(150, 16777215))
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_90)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.label_pessoa_cdeficiencia_usuario_as = QLabel(self.frame_90)
        self.label_pessoa_cdeficiencia_usuario_as.setObjectName(u"label_pessoa_cdeficiencia_usuario_as")
        self.label_pessoa_cdeficiencia_usuario_as.setMinimumSize(QSize(205, 0))
        self.label_pessoa_cdeficiencia_usuario_as.setMaximumSize(QSize(205, 16777215))
        self.label_pessoa_cdeficiencia_usuario_as.setFont(font)

        self.verticalLayout_88.addWidget(self.label_pessoa_cdeficiencia_usuario_as)

        self.frame_130 = QFrame(self.frame_90)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setMinimumSize(QSize(195, 0))
        self.frame_130.setMaximumSize(QSize(195, 16777215))
        self.frame_130.setFont(font)
        self.frame_130.setFrameShape(QFrame.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_130)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.input_pessoa_cdeficiencia_sim_usuario_as = QRadioButton(self.frame_130)
        self.input_pessoa_cdeficiencia_sim_usuario_as.setObjectName(u"input_pessoa_cdeficiencia_sim_usuario_as")
        self.input_pessoa_cdeficiencia_sim_usuario_as.setFont(font7)

        self.horizontalLayout_58.addWidget(self.input_pessoa_cdeficiencia_sim_usuario_as)

        self.label_pessoa_cdeficiencia_nao_usuario_as = QRadioButton(self.frame_130)
        self.label_pessoa_cdeficiencia_nao_usuario_as.setObjectName(u"label_pessoa_cdeficiencia_nao_usuario_as")
        self.label_pessoa_cdeficiencia_nao_usuario_as.setFont(font7)

        self.horizontalLayout_58.addWidget(self.label_pessoa_cdeficiencia_nao_usuario_as)


        self.verticalLayout_88.addWidget(self.frame_130)


        self.horizontalLayout_43.addWidget(self.frame_90)

        self.frame_81 = QFrame(self.frame_8)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMinimumSize(QSize(260, 0))
        self.frame_81.setMaximumSize(QSize(260, 16777215))
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_81)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_tipo_deficiencia_usuario_as = QLabel(self.frame_81)
        self.label_tipo_deficiencia_usuario_as.setObjectName(u"label_tipo_deficiencia_usuario_as")
        self.label_tipo_deficiencia_usuario_as.setMinimumSize(QSize(260, 0))
        self.label_tipo_deficiencia_usuario_as.setMaximumSize(QSize(260, 16777215))
        self.label_tipo_deficiencia_usuario_as.setFont(font)

        self.verticalLayout_54.addWidget(self.label_tipo_deficiencia_usuario_as)

        self.input_tipo_deficiencia_usuario_as = QLineEdit(self.frame_81)
        self.input_tipo_deficiencia_usuario_as.setObjectName(u"input_tipo_deficiencia_usuario_as")
        self.input_tipo_deficiencia_usuario_as.setMinimumSize(QSize(250, 30))
        self.input_tipo_deficiencia_usuario_as.setMaximumSize(QSize(250, 30))
        self.input_tipo_deficiencia_usuario_as.setFont(font)

        self.verticalLayout_54.addWidget(self.input_tipo_deficiencia_usuario_as)


        self.horizontalLayout_43.addWidget(self.frame_81)

        self.frame_82 = QFrame(self.frame_8)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setMinimumSize(QSize(260, 0))
        self.frame_82.setMaximumSize(QSize(260, 16777215))
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_82)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_renda_familiar_usuario_as = QLabel(self.frame_82)
        self.label_renda_familiar_usuario_as.setObjectName(u"label_renda_familiar_usuario_as")
        self.label_renda_familiar_usuario_as.setMinimumSize(QSize(260, 0))
        self.label_renda_familiar_usuario_as.setMaximumSize(QSize(260, 16777215))
        self.label_renda_familiar_usuario_as.setFont(font)

        self.verticalLayout_55.addWidget(self.label_renda_familiar_usuario_as)

        self.input_renda_familiar_usuario_as = QComboBox(self.frame_82)
        self.input_renda_familiar_usuario_as.setObjectName(u"input_renda_familiar_usuario_as")
        self.input_renda_familiar_usuario_as.setMinimumSize(QSize(250, 30))
        self.input_renda_familiar_usuario_as.setMaximumSize(QSize(250, 30))
        self.input_renda_familiar_usuario_as.setFont(font)
        self.input_renda_familiar_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.input_renda_familiar_usuario_as.setStyleSheet(u"")

        self.verticalLayout_55.addWidget(self.input_renda_familiar_usuario_as)


        self.horizontalLayout_43.addWidget(self.frame_82)

        self.frame_83 = QFrame(self.frame_8)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMinimumSize(QSize(200, 0))
        self.frame_83.setMaximumSize(QSize(200, 16777215))
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_83)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_meio_transporte_usuario_as = QLabel(self.frame_83)
        self.label_meio_transporte_usuario_as.setObjectName(u"label_meio_transporte_usuario_as")
        self.label_meio_transporte_usuario_as.setMinimumSize(QSize(200, 0))
        self.label_meio_transporte_usuario_as.setMaximumSize(QSize(200, 16777215))
        self.label_meio_transporte_usuario_as.setFont(font)

        self.verticalLayout_56.addWidget(self.label_meio_transporte_usuario_as)

        self.input_meio_transporte_usuario_as = QComboBox(self.frame_83)
        self.input_meio_transporte_usuario_as.setObjectName(u"input_meio_transporte_usuario_as")
        self.input_meio_transporte_usuario_as.setMinimumSize(QSize(190, 30))
        self.input_meio_transporte_usuario_as.setMaximumSize(QSize(190, 30))
        self.input_meio_transporte_usuario_as.setFont(font)
        self.input_meio_transporte_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_56.addWidget(self.input_meio_transporte_usuario_as)


        self.horizontalLayout_43.addWidget(self.frame_83)

        self.frame_84 = QFrame(self.frame_8)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMaximumSize(QSize(310, 16777215))
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_84)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_vale_transporte_usuario_as = QLabel(self.frame_84)
        self.label_vale_transporte_usuario_as.setObjectName(u"label_vale_transporte_usuario_as")
        self.label_vale_transporte_usuario_as.setMaximumSize(QSize(310, 16777215))
        self.label_vale_transporte_usuario_as.setFont(font)

        self.verticalLayout_57.addWidget(self.label_vale_transporte_usuario_as)

        self.input_vale_transporte_usuario_as = QComboBox(self.frame_84)
        self.input_vale_transporte_usuario_as.setObjectName(u"input_vale_transporte_usuario_as")
        self.input_vale_transporte_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_vale_transporte_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_vale_transporte_usuario_as.setFont(font)
        self.input_vale_transporte_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_57.addWidget(self.input_vale_transporte_usuario_as)


        self.horizontalLayout_43.addWidget(self.frame_84)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_43 = QFrame(self.frame_5)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMaximumSize(QSize(16777215, 60))
        self.frame_43.setStyleSheet(u"")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_44.setSpacing(5)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_85 = QFrame(self.frame_43)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMinimumSize(QSize(260, 0))
        self.frame_85.setMaximumSize(QSize(260, 16777215))
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_85)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_situacao_trabalho_usuario_as = QLabel(self.frame_85)
        self.label_situacao_trabalho_usuario_as.setObjectName(u"label_situacao_trabalho_usuario_as")
        self.label_situacao_trabalho_usuario_as.setMinimumSize(QSize(260, 0))
        self.label_situacao_trabalho_usuario_as.setMaximumSize(QSize(260, 16777215))
        self.label_situacao_trabalho_usuario_as.setFont(font)

        self.verticalLayout_58.addWidget(self.label_situacao_trabalho_usuario_as)

        self.input_situacao_trabalho_usuario_as = QLineEdit(self.frame_85)
        self.input_situacao_trabalho_usuario_as.setObjectName(u"input_situacao_trabalho_usuario_as")
        self.input_situacao_trabalho_usuario_as.setMinimumSize(QSize(250, 30))
        self.input_situacao_trabalho_usuario_as.setMaximumSize(QSize(250, 30))
        self.input_situacao_trabalho_usuario_as.setFont(font)

        self.verticalLayout_58.addWidget(self.input_situacao_trabalho_usuario_as)


        self.horizontalLayout_44.addWidget(self.frame_85)

        self.frame_91 = QFrame(self.frame_43)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMinimumSize(QSize(260, 0))
        self.frame_91.setMaximumSize(QSize(260, 16777215))
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_91)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_beneficios_usuario_as = QLabel(self.frame_91)
        self.label_beneficios_usuario_as.setObjectName(u"label_beneficios_usuario_as")
        self.label_beneficios_usuario_as.setMinimumSize(QSize(260, 0))
        self.label_beneficios_usuario_as.setMaximumSize(QSize(260, 16777215))
        self.label_beneficios_usuario_as.setFont(font)

        self.verticalLayout_63.addWidget(self.label_beneficios_usuario_as)

        self.input_beneficios_usuario_as = QComboBox(self.frame_91)
        self.input_beneficios_usuario_as.setObjectName(u"input_beneficios_usuario_as")
        self.input_beneficios_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_beneficios_usuario_as.setMaximumSize(QSize(250, 30))
        self.input_beneficios_usuario_as.setFont(font)
        self.input_beneficios_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.input_beneficios_usuario_as.setStyleSheet(u"")

        self.verticalLayout_63.addWidget(self.input_beneficios_usuario_as)


        self.horizontalLayout_44.addWidget(self.frame_91)

        self.frame_89 = QFrame(self.frame_43)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(130, 0))
        self.frame_89.setMaximumSize(QSize(130, 16777215))
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_89)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_tarifa_social_usuario_as = QLabel(self.frame_89)
        self.label_tarifa_social_usuario_as.setObjectName(u"label_tarifa_social_usuario_as")
        self.label_tarifa_social_usuario_as.setMaximumSize(QSize(190, 16777215))
        self.label_tarifa_social_usuario_as.setFont(font)

        self.verticalLayout_65.addWidget(self.label_tarifa_social_usuario_as)

        self.frame_87 = QFrame(self.frame_89)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.input_tarifa_social_sim_usuario_as = QRadioButton(self.frame_87)
        self.input_tarifa_social_sim_usuario_as.setObjectName(u"input_tarifa_social_sim_usuario_as")
        self.input_tarifa_social_sim_usuario_as.setFont(font7)
        self.input_tarifa_social_sim_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_59.addWidget(self.input_tarifa_social_sim_usuario_as)

        self.input_tarifa_social_nao_usuario_as = QRadioButton(self.frame_87)
        self.input_tarifa_social_nao_usuario_as.setObjectName(u"input_tarifa_social_nao_usuario_as")
        self.input_tarifa_social_nao_usuario_as.setFont(font7)
        self.input_tarifa_social_nao_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_59.addWidget(self.input_tarifa_social_nao_usuario_as)


        self.verticalLayout_65.addWidget(self.frame_87)


        self.horizontalLayout_44.addWidget(self.frame_89)

        self.frame_86 = QFrame(self.frame_43)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(260, 0))
        self.frame_86.setMaximumSize(QSize(260, 16777215))
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_86)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_tipo_tratamento_usuario_as = QLabel(self.frame_86)
        self.label_tipo_tratamento_usuario_as.setObjectName(u"label_tipo_tratamento_usuario_as")
        self.label_tipo_tratamento_usuario_as.setMinimumSize(QSize(260, 0))
        self.label_tipo_tratamento_usuario_as.setMaximumSize(QSize(260, 16777215))
        self.label_tipo_tratamento_usuario_as.setFont(font)

        self.verticalLayout_59.addWidget(self.label_tipo_tratamento_usuario_as)

        self.input_tipo_tratamento_usuario_as = QComboBox(self.frame_86)
        self.input_tipo_tratamento_usuario_as.setObjectName(u"input_tipo_tratamento_usuario_as")
        self.input_tipo_tratamento_usuario_as.setMinimumSize(QSize(250, 30))
        self.input_tipo_tratamento_usuario_as.setMaximumSize(QSize(250, 30))
        self.input_tipo_tratamento_usuario_as.setFont(font)
        self.input_tipo_tratamento_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.input_tipo_tratamento_usuario_as.setStyleSheet(u"")

        self.verticalLayout_59.addWidget(self.input_tipo_tratamento_usuario_as)


        self.horizontalLayout_44.addWidget(self.frame_86)

        self.frame_88 = QFrame(self.frame_43)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(330, 0))
        self.frame_88.setMaximumSize(QSize(330, 16777215))
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_88)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.label_local_tratamento_usuario_as = QLabel(self.frame_88)
        self.label_local_tratamento_usuario_as.setObjectName(u"label_local_tratamento_usuario_as")
        self.label_local_tratamento_usuario_as.setMinimumSize(QSize(330, 0))
        self.label_local_tratamento_usuario_as.setMaximumSize(QSize(330, 16777215))
        self.label_local_tratamento_usuario_as.setFont(font)

        self.verticalLayout_60.addWidget(self.label_local_tratamento_usuario_as)

        self.input_local_tratamento_usuario_as = QLineEdit(self.frame_88)
        self.input_local_tratamento_usuario_as.setObjectName(u"input_local_tratamento_usuario_as")
        self.input_local_tratamento_usuario_as.setMinimumSize(QSize(320, 30))
        self.input_local_tratamento_usuario_as.setMaximumSize(QSize(320, 30))
        self.input_local_tratamento_usuario_as.setFont(font)

        self.verticalLayout_60.addWidget(self.input_local_tratamento_usuario_as)


        self.horizontalLayout_44.addWidget(self.frame_88)


        self.verticalLayout_4.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.frame_5)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMaximumSize(QSize(16777215, 60))
        self.frame_44.setStyleSheet(u"")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_45.setSpacing(5)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_92 = QFrame(self.frame_44)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(260, 0))
        self.frame_92.setMaximumSize(QSize(260, 16777215))
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_92)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.label_patologia_base_usuario_as = QLabel(self.frame_92)
        self.label_patologia_base_usuario_as.setObjectName(u"label_patologia_base_usuario_as")
        self.label_patologia_base_usuario_as.setMinimumSize(QSize(260, 0))
        self.label_patologia_base_usuario_as.setMaximumSize(QSize(260, 16777215))
        self.label_patologia_base_usuario_as.setFont(font)

        self.verticalLayout_61.addWidget(self.label_patologia_base_usuario_as)

        self.input_patologia_base_usuario_as = QComboBox(self.frame_92)
        self.input_patologia_base_usuario_as.setObjectName(u"input_patologia_base_usuario_as")
        self.input_patologia_base_usuario_as.setMinimumSize(QSize(250, 30))
        self.input_patologia_base_usuario_as.setMaximumSize(QSize(250, 30))
        self.input_patologia_base_usuario_as.setFont(font)
        self.input_patologia_base_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_61.addWidget(self.input_patologia_base_usuario_as)


        self.horizontalLayout_45.addWidget(self.frame_92)

        self.frame_132 = QFrame(self.frame_44)
        self.frame_132.setObjectName(u"frame_132")
        self.frame_132.setMinimumSize(QSize(160, 0))
        self.frame_132.setMaximumSize(QSize(160, 16777215))
        self.frame_132.setFrameShape(QFrame.StyledPanel)
        self.frame_132.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_132)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_data_inicio_usuario_as = QLabel(self.frame_132)
        self.label_data_inicio_usuario_as.setObjectName(u"label_data_inicio_usuario_as")
        self.label_data_inicio_usuario_as.setMinimumSize(QSize(160, 0))
        self.label_data_inicio_usuario_as.setMaximumSize(QSize(160, 16777215))
        self.label_data_inicio_usuario_as.setFont(font)

        self.verticalLayout_62.addWidget(self.label_data_inicio_usuario_as)

        self.input_data_inicio_usuario_as = QLineEdit(self.frame_132)
        self.input_data_inicio_usuario_as.setObjectName(u"input_data_inicio_usuario_as")
        self.input_data_inicio_usuario_as.setMinimumSize(QSize(150, 30))
        self.input_data_inicio_usuario_as.setMaximumSize(QSize(150, 30))
        self.input_data_inicio_usuario_as.setFont(font)

        self.verticalLayout_62.addWidget(self.input_data_inicio_usuario_as)


        self.horizontalLayout_45.addWidget(self.frame_132)

        self.frame_131 = QFrame(self.frame_44)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setMinimumSize(QSize(250, 0))
        self.frame_131.setMaximumSize(QSize(250, 16777215))
        self.frame_131.setFrameShape(QFrame.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.frame_131)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.label_periodo_usuario_as = QLabel(self.frame_131)
        self.label_periodo_usuario_as.setObjectName(u"label_periodo_usuario_as")
        self.label_periodo_usuario_as.setMinimumSize(QSize(250, 0))
        self.label_periodo_usuario_as.setMaximumSize(QSize(250, 16777215))
        self.label_periodo_usuario_as.setFont(font)

        self.verticalLayout_89.addWidget(self.label_periodo_usuario_as)

        self.input_periodo_usuario_as = QComboBox(self.frame_131)
        self.input_periodo_usuario_as.setObjectName(u"input_periodo_usuario_as")
        self.input_periodo_usuario_as.setMinimumSize(QSize(240, 30))
        self.input_periodo_usuario_as.setMaximumSize(QSize(240, 30))
        self.input_periodo_usuario_as.setFont(font)
        self.input_periodo_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_89.addWidget(self.input_periodo_usuario_as)


        self.horizontalLayout_45.addWidget(self.frame_131)

        self.frame_134 = QFrame(self.frame_44)
        self.frame_134.setObjectName(u"frame_134")
        self.frame_134.setMaximumSize(QSize(600, 16777215))
        self.frame_134.setFrameShape(QFrame.StyledPanel)
        self.frame_134.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_45.addWidget(self.frame_134)


        self.verticalLayout_4.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.frame_5)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_46.setSpacing(5)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_93 = QFrame(self.frame_45)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_46.addWidget(self.frame_93)


        self.verticalLayout_4.addWidget(self.frame_45)


        self.horizontalLayout_4.addWidget(self.frame_5)

        self.horizontalSpacer_7 = QSpacerItem(151, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 8)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.page_cadastro_usuario_as)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(1687, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.btn_proximo_as = QPushButton(self.frame_4)
        self.btn_proximo_as.setObjectName(u"btn_proximo_as")
        self.btn_proximo_as.setMinimumSize(QSize(140, 40))
        font9 = QFont()
        font9.setFamilies([u"Abel"])
        font9.setPointSize(18)
        self.btn_proximo_as.setFont(font9)
        self.btn_proximo_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_proximo_as.setLayoutDirection(Qt.RightToLeft)
        self.btn_proximo_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")
        icon12 = QIcon()
        icon12.addFile(u"./icons/seta-direita.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_proximo_as.setIcon(icon12)

        self.horizontalLayout.addWidget(self.btn_proximo_as)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 8)
        self.verticalLayout_3.setStretch(2, 1)
        self.stackedWidget_2.addWidget(self.page_cadastro_usuario_as)
        self.page_cadastro_cuidador_as = QWidget()
        self.page_cadastro_cuidador_as.setObjectName(u"page_cadastro_cuidador_as")
        self.verticalLayout_66 = QVBoxLayout(self.page_cadastro_cuidador_as)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.frame_97 = QFrame(self.page_cadastro_cuidador_as)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setStyleSheet(u"background-color: #F3B9BF; margin-bottom: 2em")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_97)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.frame_97)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font1)
        self.label_36.setStyleSheet(u"color: #EC848C; padding-top: 1.5em")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.label_36)


        self.verticalLayout_66.addWidget(self.frame_97)

        self.frame_98 = QFrame(self.page_cadastro_cuidador_as)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_39 = QSpacerItem(184, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_39)

        self.frame_100 = QFrame(self.frame_98)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setStyleSheet(u"QLabel{margin-left: 0.25em}")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_100)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(20, 0, 0, 0)
        self.frame_101 = QFrame(self.frame_100)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setMinimumSize(QSize(0, 0))
        self.frame_101.setMaximumSize(QSize(16777215, 60))
        self.frame_101.setStyleSheet(u"")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_49.setSpacing(5)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_94 = QFrame(self.frame_101)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMinimumSize(QSize(160, 0))
        self.frame_94.setMaximumSize(QSize(160, 16777215))
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_94)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.label_matricula_cuidador_as = QLabel(self.frame_94)
        self.label_matricula_cuidador_as.setObjectName(u"label_matricula_cuidador_as")
        self.label_matricula_cuidador_as.setMinimumSize(QSize(160, 0))
        self.label_matricula_cuidador_as.setMaximumSize(QSize(160, 16777215))
        self.label_matricula_cuidador_as.setFont(font)

        self.verticalLayout_90.addWidget(self.label_matricula_cuidador_as)

        self.input_matricula_cuidador_as = QLineEdit(self.frame_94)
        self.input_matricula_cuidador_as.setObjectName(u"input_matricula_cuidador_as")
        self.input_matricula_cuidador_as.setMinimumSize(QSize(150, 30))
        self.input_matricula_cuidador_as.setMaximumSize(QSize(150, 30))
        self.input_matricula_cuidador_as.setFont(font)

        self.verticalLayout_90.addWidget(self.input_matricula_cuidador_as)


        self.horizontalLayout_49.addWidget(self.frame_94)

        self.frame_105 = QFrame(self.frame_101)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setMinimumSize(QSize(460, 0))
        self.frame_105.setMaximumSize(QSize(460, 16777215))
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_105)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.label_nome_cuidador_as = QLabel(self.frame_105)
        self.label_nome_cuidador_as.setObjectName(u"label_nome_cuidador_as")
        self.label_nome_cuidador_as.setMinimumSize(QSize(460, 0))
        self.label_nome_cuidador_as.setMaximumSize(QSize(460, 16777215))
        self.label_nome_cuidador_as.setFont(font)

        self.verticalLayout_69.addWidget(self.label_nome_cuidador_as)

        self.input_nome_cuidador_as = QLineEdit(self.frame_105)
        self.input_nome_cuidador_as.setObjectName(u"input_nome_cuidador_as")
        self.input_nome_cuidador_as.setMinimumSize(QSize(450, 30))
        self.input_nome_cuidador_as.setMaximumSize(QSize(450, 30))
        self.input_nome_cuidador_as.setFont(font)

        self.verticalLayout_69.addWidget(self.input_nome_cuidador_as)


        self.horizontalLayout_49.addWidget(self.frame_105)

        self.frame_106 = QFrame(self.frame_101)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMinimumSize(QSize(180, 0))
        self.frame_106.setMaximumSize(QSize(180, 16777215))
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_106)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.label_cpf_cuidador_as = QLabel(self.frame_106)
        self.label_cpf_cuidador_as.setObjectName(u"label_cpf_cuidador_as")
        self.label_cpf_cuidador_as.setMinimumSize(QSize(180, 0))
        self.label_cpf_cuidador_as.setMaximumSize(QSize(180, 16777215))
        self.label_cpf_cuidador_as.setFont(font)

        self.verticalLayout_70.addWidget(self.label_cpf_cuidador_as)

        self.input_cpf_cuidador_as = QLineEdit(self.frame_106)
        self.input_cpf_cuidador_as.setObjectName(u"input_cpf_cuidador_as")
        self.input_cpf_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_cpf_cuidador_as.setMaximumSize(QSize(170, 16777215))
        self.input_cpf_cuidador_as.setFont(font)

        self.verticalLayout_70.addWidget(self.input_cpf_cuidador_as)


        self.horizontalLayout_49.addWidget(self.frame_106)

        self.frame_107 = QFrame(self.frame_101)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setMinimumSize(QSize(160, 0))
        self.frame_107.setMaximumSize(QSize(160, 16777215))
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_107)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.label_rg_cuidador_as = QLabel(self.frame_107)
        self.label_rg_cuidador_as.setObjectName(u"label_rg_cuidador_as")
        self.label_rg_cuidador_as.setMinimumSize(QSize(160, 0))
        self.label_rg_cuidador_as.setMaximumSize(QSize(160, 16777215))
        self.label_rg_cuidador_as.setFont(font)

        self.verticalLayout_71.addWidget(self.label_rg_cuidador_as)

        self.input_rg_cuidador_as = QLineEdit(self.frame_107)
        self.input_rg_cuidador_as.setObjectName(u"input_rg_cuidador_as")
        self.input_rg_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_rg_cuidador_as.setMaximumSize(QSize(150, 16777215))
        self.input_rg_cuidador_as.setFont(font)

        self.verticalLayout_71.addWidget(self.input_rg_cuidador_as)


        self.horizontalLayout_49.addWidget(self.frame_107)

        self.frame_108 = QFrame(self.frame_101)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setMinimumSize(QSize(155, 0))
        self.frame_108.setMaximumSize(QSize(155, 16777215))
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_108)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.label_data_emissao_cuidador_as = QLabel(self.frame_108)
        self.label_data_emissao_cuidador_as.setObjectName(u"label_data_emissao_cuidador_as")
        self.label_data_emissao_cuidador_as.setMinimumSize(QSize(155, 0))
        self.label_data_emissao_cuidador_as.setMaximumSize(QSize(155, 16777215))
        self.label_data_emissao_cuidador_as.setFont(font)

        self.verticalLayout_72.addWidget(self.label_data_emissao_cuidador_as)

        self.input_data_emissao_cuidador_as = QLineEdit(self.frame_108)
        self.input_data_emissao_cuidador_as.setObjectName(u"input_data_emissao_cuidador_as")
        self.input_data_emissao_cuidador_as.setMinimumSize(QSize(145, 30))
        self.input_data_emissao_cuidador_as.setMaximumSize(QSize(145, 16777215))
        self.input_data_emissao_cuidador_as.setFont(font)

        self.verticalLayout_72.addWidget(self.input_data_emissao_cuidador_as)


        self.horizontalLayout_49.addWidget(self.frame_108)


        self.verticalLayout_67.addWidget(self.frame_101)

        self.frame_102 = QFrame(self.frame_100)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setMinimumSize(QSize(0, 0))
        self.frame_102.setMaximumSize(QSize(16777215, 60))
        self.frame_102.setStyleSheet(u"")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_50.setSpacing(5)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.frame_109 = QFrame(self.frame_102)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setMinimumSize(QSize(155, 0))
        self.frame_109.setMaximumSize(QSize(155, 16777215))
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_109)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.label_orgao_expedidor_cuidador_as = QLabel(self.frame_109)
        self.label_orgao_expedidor_cuidador_as.setObjectName(u"label_orgao_expedidor_cuidador_as")
        self.label_orgao_expedidor_cuidador_as.setMinimumSize(QSize(155, 0))
        self.label_orgao_expedidor_cuidador_as.setMaximumSize(QSize(155, 16777215))
        self.label_orgao_expedidor_cuidador_as.setFont(font)

        self.verticalLayout_73.addWidget(self.label_orgao_expedidor_cuidador_as)

        self.input_orgao_expedidor_cuidador_as = QLineEdit(self.frame_109)
        self.input_orgao_expedidor_cuidador_as.setObjectName(u"input_orgao_expedidor_cuidador_as")
        self.input_orgao_expedidor_cuidador_as.setMaximumSize(QSize(145, 30))
        self.input_orgao_expedidor_cuidador_as.setFont(font)

        self.verticalLayout_73.addWidget(self.input_orgao_expedidor_cuidador_as)


        self.horizontalLayout_50.addWidget(self.frame_109)

        self.frame_95 = QFrame(self.frame_102)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMinimumSize(QSize(155, 0))
        self.frame_95.setMaximumSize(QSize(155, 16777215))
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_95)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.label_sexo_cuidador_as = QLabel(self.frame_95)
        self.label_sexo_cuidador_as.setObjectName(u"label_sexo_cuidador_as")
        self.label_sexo_cuidador_as.setFont(font)

        self.verticalLayout_91.addWidget(self.label_sexo_cuidador_as)

        self.input_sexo_cuidador_as = QLineEdit(self.frame_95)
        self.input_sexo_cuidador_as.setObjectName(u"input_sexo_cuidador_as")
        self.input_sexo_cuidador_as.setMinimumSize(QSize(145, 30))
        self.input_sexo_cuidador_as.setMaximumSize(QSize(145, 30))
        self.input_sexo_cuidador_as.setFont(font)

        self.verticalLayout_91.addWidget(self.input_sexo_cuidador_as)


        self.horizontalLayout_50.addWidget(self.frame_95)

        self.frame_96 = QFrame(self.frame_102)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMinimumSize(QSize(280, 0))
        self.frame_96.setMaximumSize(QSize(280, 16777215))
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_96)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.label_parentesco_cuidador_as = QLabel(self.frame_96)
        self.label_parentesco_cuidador_as.setObjectName(u"label_parentesco_cuidador_as")
        self.label_parentesco_cuidador_as.setFont(font)

        self.verticalLayout_92.addWidget(self.label_parentesco_cuidador_as)

        self.input_parentesco_cuidador_as = QLineEdit(self.frame_96)
        self.input_parentesco_cuidador_as.setObjectName(u"input_parentesco_cuidador_as")
        self.input_parentesco_cuidador_as.setMinimumSize(QSize(270, 0))
        self.input_parentesco_cuidador_as.setMaximumSize(QSize(270, 30))
        self.input_parentesco_cuidador_as.setFont(font)

        self.verticalLayout_92.addWidget(self.input_parentesco_cuidador_as)


        self.horizontalLayout_50.addWidget(self.frame_96)

        self.frame_110 = QFrame(self.frame_102)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setMinimumSize(QSize(155, 0))
        self.frame_110.setMaximumSize(QSize(155, 16777215))
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_110)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.label_telefone_cuidador_as = QLabel(self.frame_110)
        self.label_telefone_cuidador_as.setObjectName(u"label_telefone_cuidador_as")
        self.label_telefone_cuidador_as.setMinimumSize(QSize(155, 0))
        self.label_telefone_cuidador_as.setMaximumSize(QSize(155, 16777215))
        self.label_telefone_cuidador_as.setFont(font)

        self.verticalLayout_74.addWidget(self.label_telefone_cuidador_as)

        self.input_telefone_cuidador_as = QLineEdit(self.frame_110)
        self.input_telefone_cuidador_as.setObjectName(u"input_telefone_cuidador_as")
        self.input_telefone_cuidador_as.setMinimumSize(QSize(145, 30))
        self.input_telefone_cuidador_as.setMaximumSize(QSize(145, 30))
        self.input_telefone_cuidador_as.setFont(font)

        self.verticalLayout_74.addWidget(self.input_telefone_cuidador_as)


        self.horizontalLayout_50.addWidget(self.frame_110)

        self.frame_111 = QFrame(self.frame_102)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setMinimumSize(QSize(240, 0))
        self.frame_111.setMaximumSize(QSize(240, 16777215))
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_111)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.label_email_cuidador_as = QLabel(self.frame_111)
        self.label_email_cuidador_as.setObjectName(u"label_email_cuidador_as")
        self.label_email_cuidador_as.setMinimumSize(QSize(240, 0))
        self.label_email_cuidador_as.setMaximumSize(QSize(240, 16777215))
        self.label_email_cuidador_as.setFont(font)

        self.verticalLayout_75.addWidget(self.label_email_cuidador_as)

        self.input_email_cuidador_as = QLineEdit(self.frame_111)
        self.input_email_cuidador_as.setObjectName(u"input_email_cuidador_as")
        self.input_email_cuidador_as.setMinimumSize(QSize(230, 30))
        self.input_email_cuidador_as.setMaximumSize(QSize(230, 30))
        self.input_email_cuidador_as.setFont(font)

        self.verticalLayout_75.addWidget(self.input_email_cuidador_as)


        self.horizontalLayout_50.addWidget(self.frame_111)

        self.frame_112 = QFrame(self.frame_102)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setMaximumSize(QSize(170, 16777215))
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_112)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.label_cep_cuidador_as = QLabel(self.frame_112)
        self.label_cep_cuidador_as.setObjectName(u"label_cep_cuidador_as")
        self.label_cep_cuidador_as.setMaximumSize(QSize(170, 16777215))
        self.label_cep_cuidador_as.setFont(font)

        self.verticalLayout_76.addWidget(self.label_cep_cuidador_as)

        self.input_cep_cuidador_as = QLineEdit(self.frame_112)
        self.input_cep_cuidador_as.setObjectName(u"input_cep_cuidador_as")
        self.input_cep_cuidador_as.setMinimumSize(QSize(150, 30))
        self.input_cep_cuidador_as.setMaximumSize(QSize(150, 30))
        self.input_cep_cuidador_as.setFont(font)

        self.verticalLayout_76.addWidget(self.input_cep_cuidador_as)


        self.horizontalLayout_50.addWidget(self.frame_112)


        self.verticalLayout_67.addWidget(self.frame_102)

        self.frame_103 = QFrame(self.frame_100)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setMinimumSize(QSize(0, 0))
        self.frame_103.setMaximumSize(QSize(16777215, 60))
        self.frame_103.setStyleSheet(u"")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_103)
        self.horizontalLayout_51.setSpacing(5)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.frame_113 = QFrame(self.frame_103)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setMinimumSize(QSize(360, 0))
        self.frame_113.setMaximumSize(QSize(360, 16777215))
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_113)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.label_logradouro_cuidador_as = QLabel(self.frame_113)
        self.label_logradouro_cuidador_as.setObjectName(u"label_logradouro_cuidador_as")
        self.label_logradouro_cuidador_as.setMinimumSize(QSize(360, 0))
        self.label_logradouro_cuidador_as.setMaximumSize(QSize(360, 16777215))
        self.label_logradouro_cuidador_as.setFont(font)

        self.verticalLayout_77.addWidget(self.label_logradouro_cuidador_as)

        self.input_logradouro_cuidador_as = QLineEdit(self.frame_113)
        self.input_logradouro_cuidador_as.setObjectName(u"input_logradouro_cuidador_as")
        self.input_logradouro_cuidador_as.setMinimumSize(QSize(350, 30))
        self.input_logradouro_cuidador_as.setMaximumSize(QSize(350, 30))
        self.input_logradouro_cuidador_as.setFont(font)

        self.verticalLayout_77.addWidget(self.input_logradouro_cuidador_as)


        self.horizontalLayout_51.addWidget(self.frame_113)

        self.frame_133 = QFrame(self.frame_103)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setMinimumSize(QSize(160, 0))
        self.frame_133.setMaximumSize(QSize(160, 16777215))
        self.frame_133.setFrameShape(QFrame.StyledPanel)
        self.frame_133.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.frame_133)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.label_numero_cuidador_as = QLabel(self.frame_133)
        self.label_numero_cuidador_as.setObjectName(u"label_numero_cuidador_as")
        self.label_numero_cuidador_as.setMinimumSize(QSize(160, 0))
        self.label_numero_cuidador_as.setMaximumSize(QSize(160, 16777215))
        self.label_numero_cuidador_as.setFont(font)

        self.verticalLayout_93.addWidget(self.label_numero_cuidador_as)

        self.input_numero_cuidador_as = QLineEdit(self.frame_133)
        self.input_numero_cuidador_as.setObjectName(u"input_numero_cuidador_as")
        self.input_numero_cuidador_as.setMinimumSize(QSize(150, 30))
        self.input_numero_cuidador_as.setMaximumSize(QSize(150, 30))
        self.input_numero_cuidador_as.setFont(font)

        self.verticalLayout_93.addWidget(self.input_numero_cuidador_as)


        self.horizontalLayout_51.addWidget(self.frame_133)

        self.frame_135 = QFrame(self.frame_103)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setMinimumSize(QSize(230, 0))
        self.frame_135.setMaximumSize(QSize(230, 16777215))
        self.frame_135.setFrameShape(QFrame.StyledPanel)
        self.frame_135.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_135)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.label_bairro_cuidador_as = QLabel(self.frame_135)
        self.label_bairro_cuidador_as.setObjectName(u"label_bairro_cuidador_as")
        self.label_bairro_cuidador_as.setMinimumSize(QSize(230, 0))
        self.label_bairro_cuidador_as.setMaximumSize(QSize(230, 16777215))
        self.label_bairro_cuidador_as.setFont(font)

        self.verticalLayout_94.addWidget(self.label_bairro_cuidador_as)

        self.input_bairro_cuidador_as = QLineEdit(self.frame_135)
        self.input_bairro_cuidador_as.setObjectName(u"input_bairro_cuidador_as")
        self.input_bairro_cuidador_as.setMinimumSize(QSize(220, 30))
        self.input_bairro_cuidador_as.setMaximumSize(QSize(220, 30))
        self.input_bairro_cuidador_as.setFont(font)

        self.verticalLayout_94.addWidget(self.input_bairro_cuidador_as)


        self.horizontalLayout_51.addWidget(self.frame_135)

        self.frame_114 = QFrame(self.frame_103)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setMinimumSize(QSize(240, 0))
        self.frame_114.setMaximumSize(QSize(240, 16777215))
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_114)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.label_cidade_cuidador_as = QLabel(self.frame_114)
        self.label_cidade_cuidador_as.setObjectName(u"label_cidade_cuidador_as")
        self.label_cidade_cuidador_as.setMinimumSize(QSize(240, 0))
        self.label_cidade_cuidador_as.setMaximumSize(QSize(240, 16777215))
        self.label_cidade_cuidador_as.setFont(font)

        self.verticalLayout_78.addWidget(self.label_cidade_cuidador_as)

        self.input_cidade_cuidador_as = QLineEdit(self.frame_114)
        self.input_cidade_cuidador_as.setObjectName(u"input_cidade_cuidador_as")
        self.input_cidade_cuidador_as.setMinimumSize(QSize(230, 30))
        self.input_cidade_cuidador_as.setMaximumSize(QSize(230, 30))
        self.input_cidade_cuidador_as.setFont(font)

        self.verticalLayout_78.addWidget(self.input_cidade_cuidador_as)


        self.horizontalLayout_51.addWidget(self.frame_114)

        self.frame_115 = QFrame(self.frame_103)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setMinimumSize(QSize(80, 0))
        self.frame_115.setMaximumSize(QSize(80, 16777215))
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_115)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.label_estado_cuidador_as = QLabel(self.frame_115)
        self.label_estado_cuidador_as.setObjectName(u"label_estado_cuidador_as")
        self.label_estado_cuidador_as.setMinimumSize(QSize(80, 0))
        self.label_estado_cuidador_as.setMaximumSize(QSize(80, 16777215))
        self.label_estado_cuidador_as.setFont(font)

        self.verticalLayout_79.addWidget(self.label_estado_cuidador_as)

        self.input_estado_cuidador_as = QComboBox(self.frame_115)
        self.input_estado_cuidador_as.setObjectName(u"input_estado_cuidador_as")
        self.input_estado_cuidador_as.setMinimumSize(QSize(70, 30))
        self.input_estado_cuidador_as.setMaximumSize(QSize(70, 30))
        self.input_estado_cuidador_as.setFont(font)

        self.verticalLayout_79.addWidget(self.input_estado_cuidador_as)


        self.horizontalLayout_51.addWidget(self.frame_115)


        self.verticalLayout_67.addWidget(self.frame_103)

        self.frame_104 = QFrame(self.frame_100)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setMinimumSize(QSize(0, 0))
        self.frame_104.setMaximumSize(QSize(16777215, 300))
        self.frame_104.setStyleSheet(u"")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_104)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.label_observacoes_gerais_cuidador_as = QLabel(self.frame_104)
        self.label_observacoes_gerais_cuidador_as.setObjectName(u"label_observacoes_gerais_cuidador_as")
        self.label_observacoes_gerais_cuidador_as.setMaximumSize(QSize(300, 50))
        self.label_observacoes_gerais_cuidador_as.setFont(font)

        self.verticalLayout_68.addWidget(self.label_observacoes_gerais_cuidador_as)

        self.input_informacoes_gerais_as = QTextEdit(self.frame_104)
        self.input_informacoes_gerais_as.setObjectName(u"input_informacoes_gerais_as")
        self.input_informacoes_gerais_as.setMaximumSize(QSize(1185, 235))
        self.input_informacoes_gerais_as.setFont(font)
        self.input_informacoes_gerais_as.setStyleSheet(u"QTextEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QTextEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout_68.addWidget(self.input_informacoes_gerais_as)


        self.verticalLayout_67.addWidget(self.frame_104)


        self.horizontalLayout_5.addWidget(self.frame_100)

        self.horizontalSpacer_40 = QSpacerItem(184, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_40)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 8)
        self.horizontalLayout_5.setStretch(2, 1)

        self.verticalLayout_66.addWidget(self.frame_98)

        self.frame_99 = QFrame(self.page_cadastro_cuidador_as)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setMinimumSize(QSize(0, 0))
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_48.setSpacing(20)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(1770, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_8)

        self.btn_observacoes_sigilo_as = QPushButton(self.frame_99)
        self.btn_observacoes_sigilo_as.setObjectName(u"btn_observacoes_sigilo_as")
        self.btn_observacoes_sigilo_as.setMinimumSize(QSize(0, 40))
        self.btn_observacoes_sigilo_as.setFont(font9)
        self.btn_observacoes_sigilo_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_observacoes_sigilo_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        icon13 = QIcon()
        icon13.addFile(u"./icons/cadeado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_observacoes_sigilo_as.setIcon(icon13)
        self.btn_observacoes_sigilo_as.setIconSize(QSize(28, 28))

        self.horizontalLayout_48.addWidget(self.btn_observacoes_sigilo_as)

        self.btn_finalizar_as = QPushButton(self.frame_99)
        self.btn_finalizar_as.setObjectName(u"btn_finalizar_as")
        self.btn_finalizar_as.setMinimumSize(QSize(140, 40))
        self.btn_finalizar_as.setFont(font9)
        self.btn_finalizar_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_finalizar_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout_48.addWidget(self.btn_finalizar_as)


        self.verticalLayout_66.addWidget(self.frame_99)

        self.verticalLayout_66.setStretch(0, 1)
        self.verticalLayout_66.setStretch(1, 8)
        self.verticalLayout_66.setStretch(2, 1)
        self.stackedWidget_2.addWidget(self.page_cadastro_cuidador_as)
        self.page_observacoes_sigilosas_as = QWidget()
        self.page_observacoes_sigilosas_as.setObjectName(u"page_observacoes_sigilosas_as")
        self.page_observacoes_sigilosas_as.setFont(font1)
        self.verticalLayout_80 = QVBoxLayout(self.page_observacoes_sigilosas_as)
        self.verticalLayout_80.setSpacing(0)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.frame_116 = QFrame(self.page_observacoes_sigilosas_as)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setStyleSheet(u"background-color: #F3B9BF; ")
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_116)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.frame_116)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font1)
        self.label_49.setStyleSheet(u"color: #EC848C;")
        self.label_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.label_49)


        self.verticalLayout_80.addWidget(self.frame_116)

        self.frame_117 = QFrame(self.page_observacoes_sigilosas_as)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setMinimumSize(QSize(0, 0))
        self.frame_117.setStyleSheet(u"QFrame{background-color: #FCE0DF}\n"
"")
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_80.addWidget(self.frame_117)

        self.frame_118 = QFrame(self.page_observacoes_sigilosas_as)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_118)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_42 = QSpacerItem(309, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_42)

        self.frame_120 = QFrame(self.frame_118)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setMinimumSize(QSize(1185, 0))
        self.frame_120.setMaximumSize(QSize(1185, 700))
        self.frame_120.setStyleSheet(u"QLabel{margin-left: 0.25em}")
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_120)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.frame_123 = QFrame(self.frame_120)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setMaximumSize(QSize(16777215, 450))
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_123)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.label_observacoes_obs_sigilosas_as = QLabel(self.frame_123)
        self.label_observacoes_obs_sigilosas_as.setObjectName(u"label_observacoes_obs_sigilosas_as")
        self.label_observacoes_obs_sigilosas_as.setMaximumSize(QSize(300, 50))
        self.label_observacoes_obs_sigilosas_as.setFont(font)

        self.verticalLayout_82.addWidget(self.label_observacoes_obs_sigilosas_as)

        self.input_observacoes_obs_sigilosas_as = QTextEdit(self.frame_123)
        self.input_observacoes_obs_sigilosas_as.setObjectName(u"input_observacoes_obs_sigilosas_as")
        self.input_observacoes_obs_sigilosas_as.setMinimumSize(QSize(0, 250))
        self.input_observacoes_obs_sigilosas_as.setMaximumSize(QSize(1185, 400))
        self.input_observacoes_obs_sigilosas_as.setFont(font)
        self.input_observacoes_obs_sigilosas_as.setStyleSheet(u"QTextEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QTextEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout_82.addWidget(self.input_observacoes_obs_sigilosas_as)


        self.verticalLayout_81.addWidget(self.frame_123)


        self.horizontalLayout_55.addWidget(self.frame_120)

        self.horizontalSpacer_45 = QSpacerItem(309, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_45)

        self.horizontalLayout_55.setStretch(0, 1)
        self.horizontalLayout_55.setStretch(1, 4)
        self.horizontalLayout_55.setStretch(2, 1)

        self.verticalLayout_80.addWidget(self.frame_118)

        self.frame_119 = QFrame(self.page_observacoes_sigilosas_as)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_119)
        self.horizontalLayout_54.setSpacing(40)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(40, 0, 0, 0)
        self.btn_alterar_observacoes_sigilosas_as = QPushButton(self.frame_119)
        self.btn_alterar_observacoes_sigilosas_as.setObjectName(u"btn_alterar_observacoes_sigilosas_as")
        self.btn_alterar_observacoes_sigilosas_as.setMinimumSize(QSize(0, 40))
        self.btn_alterar_observacoes_sigilosas_as.setFont(font9)
        self.btn_alterar_observacoes_sigilosas_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_observacoes_sigilosas_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        self.btn_alterar_observacoes_sigilosas_as.setIcon(icon10)
        self.btn_alterar_observacoes_sigilosas_as.setIconSize(QSize(28, 28))

        self.horizontalLayout_54.addWidget(self.btn_alterar_observacoes_sigilosas_as)

        self.btn_cancelar_observacoes_sigilosas_as = QPushButton(self.frame_119)
        self.btn_cancelar_observacoes_sigilosas_as.setObjectName(u"btn_cancelar_observacoes_sigilosas_as")
        self.btn_cancelar_observacoes_sigilosas_as.setMinimumSize(QSize(0, 40))
        self.btn_cancelar_observacoes_sigilosas_as.setFont(font9)
        self.btn_cancelar_observacoes_sigilosas_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar_observacoes_sigilosas_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        icon14 = QIcon()
        icon14.addFile(u"./icons/cancelar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancelar_observacoes_sigilosas_as.setIcon(icon14)
        self.btn_cancelar_observacoes_sigilosas_as.setIconSize(QSize(28, 28))

        self.horizontalLayout_54.addWidget(self.btn_cancelar_observacoes_sigilosas_as)

        self.btn_salvar_observacoes_sigilosas_as = QPushButton(self.frame_119)
        self.btn_salvar_observacoes_sigilosas_as.setObjectName(u"btn_salvar_observacoes_sigilosas_as")
        self.btn_salvar_observacoes_sigilosas_as.setMinimumSize(QSize(0, 40))
        self.btn_salvar_observacoes_sigilosas_as.setFont(font9)
        self.btn_salvar_observacoes_sigilosas_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar_observacoes_sigilosas_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em;}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        icon15 = QIcon()
        icon15.addFile(u"./icons/salvar-arquivo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salvar_observacoes_sigilosas_as.setIcon(icon15)
        self.btn_salvar_observacoes_sigilosas_as.setIconSize(QSize(28, 28))

        self.horizontalLayout_54.addWidget(self.btn_salvar_observacoes_sigilosas_as)

        self.btn_excluir_observacoes_sigilosas_as = QPushButton(self.frame_119)
        self.btn_excluir_observacoes_sigilosas_as.setObjectName(u"btn_excluir_observacoes_sigilosas_as")
        self.btn_excluir_observacoes_sigilosas_as.setMinimumSize(QSize(0, 40))
        self.btn_excluir_observacoes_sigilosas_as.setFont(font9)
        self.btn_excluir_observacoes_sigilosas_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_observacoes_sigilosas_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        icon16 = QIcon()
        icon16.addFile(u"./icons/lixeira-de-reciclagem.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluir_observacoes_sigilosas_as.setIcon(icon16)
        self.btn_excluir_observacoes_sigilosas_as.setIconSize(QSize(28, 28))

        self.horizontalLayout_54.addWidget(self.btn_excluir_observacoes_sigilosas_as)

        self.horizontalSpacer_41 = QSpacerItem(1433, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_41)


        self.verticalLayout_80.addWidget(self.frame_119)

        self.verticalLayout_80.setStretch(0, 1)
        self.verticalLayout_80.setStretch(2, 7)
        self.verticalLayout_80.setStretch(3, 1)
        self.stackedWidget_2.addWidget(self.page_observacoes_sigilosas_as)
        self.page_cadastro_colaborador_as = QWidget()
        self.page_cadastro_colaborador_as.setObjectName(u"page_cadastro_colaborador_as")
        self.page_cadastro_colaborador_as.setStyleSheet(u"")
        self.verticalLayout_83 = QVBoxLayout(self.page_cadastro_colaborador_as)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.frame_192 = QFrame(self.page_cadastro_colaborador_as)
        self.frame_192.setObjectName(u"frame_192")
        self.frame_192.setStyleSheet(u"background-color: #F3B9BF; margin-bottom: 2em")
        self.frame_192.setFrameShape(QFrame.StyledPanel)
        self.frame_192.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_192)
        self.horizontalLayout_76.setSpacing(0)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.label_cadastro_colaborador_as = QLabel(self.frame_192)
        self.label_cadastro_colaborador_as.setObjectName(u"label_cadastro_colaborador_as")
        self.label_cadastro_colaborador_as.setFont(font1)
        self.label_cadastro_colaborador_as.setStyleSheet(u"color: #EC848C; padding-top: 1.5em")
        self.label_cadastro_colaborador_as.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_76.addWidget(self.label_cadastro_colaborador_as)


        self.verticalLayout_83.addWidget(self.frame_192)

        self.frame_193 = QFrame(self.page_cadastro_colaborador_as)
        self.frame_193.setObjectName(u"frame_193")
        self.frame_193.setFrameShape(QFrame.StyledPanel)
        self.frame_193.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_193)
        self.horizontalLayout_77.setSpacing(0)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.frame_194 = QFrame(self.frame_193)
        self.frame_194.setObjectName(u"frame_194")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_194.sizePolicy().hasHeightForWidth())
        self.frame_194.setSizePolicy(sizePolicy)
        self.frame_194.setStyleSheet(u"QLabel{margin-left: 0.25em}")
        self.frame_194.setFrameShape(QFrame.StyledPanel)
        self.frame_194.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_194)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_241 = QFrame(self.frame_194)
        self.frame_241.setObjectName(u"frame_241")
        self.frame_241.setMinimumSize(QSize(0, 0))
        self.frame_241.setMaximumSize(QSize(16777215, 60))
        self.frame_241.setStyleSheet(u"")
        self.frame_241.setFrameShape(QFrame.StyledPanel)
        self.frame_241.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_241)
        self.horizontalLayout_80.setSpacing(5)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.frame_255 = QFrame(self.frame_241)
        self.frame_255.setObjectName(u"frame_255")
        self.frame_255.setMinimumSize(QSize(150, 0))
        self.frame_255.setMaximumSize(QSize(155, 16777215))
        self.frame_255.setFrameShape(QFrame.StyledPanel)
        self.frame_255.setFrameShadow(QFrame.Raised)
        self.verticalLayout_171 = QVBoxLayout(self.frame_255)
        self.verticalLayout_171.setSpacing(5)
        self.verticalLayout_171.setObjectName(u"verticalLayout_171")
        self.verticalLayout_171.setContentsMargins(0, 0, 0, 0)
        self.label_salario_colaborador_as = QLabel(self.frame_255)
        self.label_salario_colaborador_as.setObjectName(u"label_salario_colaborador_as")
        self.label_salario_colaborador_as.setMinimumSize(QSize(100, 0))
        self.label_salario_colaborador_as.setMaximumSize(QSize(100, 16777215))
        self.label_salario_colaborador_as.setFont(font)

        self.verticalLayout_171.addWidget(self.label_salario_colaborador_as)

        self.input_salario_colaborador_as = QLineEdit(self.frame_255)
        self.input_salario_colaborador_as.setObjectName(u"input_salario_colaborador_as")
        self.input_salario_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_salario_colaborador_as.setMaximumSize(QSize(150, 16777215))
        self.input_salario_colaborador_as.setFont(font)

        self.verticalLayout_171.addWidget(self.input_salario_colaborador_as)


        self.horizontalLayout_80.addWidget(self.frame_255)

        self.frame_249 = QFrame(self.frame_241)
        self.frame_249.setObjectName(u"frame_249")
        self.frame_249.setMinimumSize(QSize(281, 0))
        self.frame_249.setMaximumSize(QSize(281, 16777215))
        self.frame_249.setFrameShape(QFrame.StyledPanel)
        self.frame_249.setFrameShadow(QFrame.Raised)
        self.verticalLayout_166 = QVBoxLayout(self.frame_249)
        self.verticalLayout_166.setSpacing(5)
        self.verticalLayout_166.setObjectName(u"verticalLayout_166")
        self.verticalLayout_166.setContentsMargins(0, 0, 0, 0)
        self.label_descricao_cargo_colaborador_as = QLabel(self.frame_249)
        self.label_descricao_cargo_colaborador_as.setObjectName(u"label_descricao_cargo_colaborador_as")
        self.label_descricao_cargo_colaborador_as.setMinimumSize(QSize(280, 0))
        self.label_descricao_cargo_colaborador_as.setMaximumSize(QSize(280, 16777215))
        self.label_descricao_cargo_colaborador_as.setFont(font)

        self.verticalLayout_166.addWidget(self.label_descricao_cargo_colaborador_as)

        self.input_descricao_cargo_colaborador_as = QLineEdit(self.frame_249)
        self.input_descricao_cargo_colaborador_as.setObjectName(u"input_descricao_cargo_colaborador_as")
        self.input_descricao_cargo_colaborador_as.setMinimumSize(QSize(280, 30))
        self.input_descricao_cargo_colaborador_as.setMaximumSize(QSize(280, 30))
        self.input_descricao_cargo_colaborador_as.setFont(font)

        self.verticalLayout_166.addWidget(self.input_descricao_cargo_colaborador_as)


        self.horizontalLayout_80.addWidget(self.frame_249)

        self.frame_251 = QFrame(self.frame_241)
        self.frame_251.setObjectName(u"frame_251")
        self.frame_251.setMinimumSize(QSize(160, 0))
        self.frame_251.setMaximumSize(QSize(160, 16777215))
        self.frame_251.setFrameShape(QFrame.StyledPanel)
        self.frame_251.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_80.addWidget(self.frame_251)

        self.frame_252 = QFrame(self.frame_241)
        self.frame_252.setObjectName(u"frame_252")
        self.frame_252.setMinimumSize(QSize(230, 0))
        self.frame_252.setMaximumSize(QSize(230, 16777215))
        self.frame_252.setFrameShape(QFrame.StyledPanel)
        self.frame_252.setFrameShadow(QFrame.Raised)
        self.verticalLayout_169 = QVBoxLayout(self.frame_252)
        self.verticalLayout_169.setSpacing(0)
        self.verticalLayout_169.setObjectName(u"verticalLayout_169")
        self.verticalLayout_169.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_80.addWidget(self.frame_252)

        self.frame_253 = QFrame(self.frame_241)
        self.frame_253.setObjectName(u"frame_253")
        self.frame_253.setMinimumSize(QSize(180, 0))
        self.frame_253.setMaximumSize(QSize(180, 16777215))
        self.frame_253.setFrameShape(QFrame.StyledPanel)
        self.frame_253.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_80.addWidget(self.frame_253)

        self.frame_254 = QFrame(self.frame_241)
        self.frame_254.setObjectName(u"frame_254")
        self.frame_254.setMinimumSize(QSize(80, 0))
        self.frame_254.setMaximumSize(QSize(80, 16777215))
        self.frame_254.setFrameShape(QFrame.StyledPanel)
        self.frame_254.setFrameShadow(QFrame.Raised)
        self.verticalLayout_170 = QVBoxLayout(self.frame_254)
        self.verticalLayout_170.setSpacing(0)
        self.verticalLayout_170.setObjectName(u"verticalLayout_170")
        self.verticalLayout_170.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_80.addWidget(self.frame_254)


        self.gridLayout_2.addWidget(self.frame_241, 5, 1, 1, 1)

        self.frame_230 = QFrame(self.frame_194)
        self.frame_230.setObjectName(u"frame_230")
        self.frame_230.setMinimumSize(QSize(0, 0))
        self.frame_230.setMaximumSize(QSize(16777215, 60))
        self.frame_230.setStyleSheet(u"")
        self.frame_230.setFrameShape(QFrame.StyledPanel)
        self.frame_230.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_230)
        self.horizontalLayout_88.setSpacing(5)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.frame_231 = QFrame(self.frame_230)
        self.frame_231.setObjectName(u"frame_231")
        self.frame_231.setMinimumSize(QSize(155, 0))
        self.frame_231.setMaximumSize(QSize(155, 16777215))
        self.frame_231.setFrameShape(QFrame.StyledPanel)
        self.frame_231.setFrameShadow(QFrame.Raised)
        self.verticalLayout_135 = QVBoxLayout(self.frame_231)
        self.verticalLayout_135.setSpacing(5)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.label_estado_civil_colaborador_as = QLabel(self.frame_231)
        self.label_estado_civil_colaborador_as.setObjectName(u"label_estado_civil_colaborador_as")
        self.label_estado_civil_colaborador_as.setMinimumSize(QSize(155, 0))
        self.label_estado_civil_colaborador_as.setMaximumSize(QSize(155, 16777215))
        self.label_estado_civil_colaborador_as.setFont(font)

        self.verticalLayout_135.addWidget(self.label_estado_civil_colaborador_as)

        self.input_estado_civil_colaborador_comboBox_as = QComboBox(self.frame_231)
        self.input_estado_civil_colaborador_comboBox_as.addItem("")
        self.input_estado_civil_colaborador_comboBox_as.addItem("")
        self.input_estado_civil_colaborador_comboBox_as.addItem("")
        self.input_estado_civil_colaborador_comboBox_as.addItem("")
        self.input_estado_civil_colaborador_comboBox_as.addItem("")
        self.input_estado_civil_colaborador_comboBox_as.addItem("")
        self.input_estado_civil_colaborador_comboBox_as.setObjectName(u"input_estado_civil_colaborador_comboBox_as")
        self.input_estado_civil_colaborador_comboBox_as.setMinimumSize(QSize(154, 30))
        self.input_estado_civil_colaborador_comboBox_as.setMaximumSize(QSize(145, 30))
        self.input_estado_civil_colaborador_comboBox_as.setFont(font)

        self.verticalLayout_135.addWidget(self.input_estado_civil_colaborador_comboBox_as)


        self.horizontalLayout_88.addWidget(self.frame_231)

        self.frame_232 = QFrame(self.frame_230)
        self.frame_232.setObjectName(u"frame_232")
        self.frame_232.setMinimumSize(QSize(155, 0))
        self.frame_232.setMaximumSize(QSize(155, 16777215))
        self.frame_232.setFrameShape(QFrame.StyledPanel)
        self.frame_232.setFrameShadow(QFrame.Raised)
        self.verticalLayout_161 = QVBoxLayout(self.frame_232)
        self.verticalLayout_161.setSpacing(5)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalLayout_161.setContentsMargins(0, 0, 0, 0)
        self.frame_238 = QFrame(self.frame_232)
        self.frame_238.setObjectName(u"frame_238")
        self.frame_238.setFrameShape(QFrame.StyledPanel)
        self.frame_238.setFrameShadow(QFrame.Raised)
        self.label_pessoa_cdeficiencia_colaborador_as = QLabel(self.frame_238)
        self.label_pessoa_cdeficiencia_colaborador_as.setObjectName(u"label_pessoa_cdeficiencia_colaborador_as")
        self.label_pessoa_cdeficiencia_colaborador_as.setGeometry(QRect(0, 0, 141, 21))
        self.label_pessoa_cdeficiencia_colaborador_as.setFont(font)

        self.verticalLayout_161.addWidget(self.frame_238)

        self.frame_237 = QFrame(self.frame_232)
        self.frame_237.setObjectName(u"frame_237")
        self.frame_237.setFrameShape(QFrame.StyledPanel)
        self.frame_237.setFrameShadow(QFrame.Raised)
        self.input_pessoa_cdeficiencia_sim_colaborador_as = QRadioButton(self.frame_237)
        self.input_pessoa_cdeficiencia_sim_colaborador_as.setObjectName(u"input_pessoa_cdeficiencia_sim_colaborador_as")
        self.input_pessoa_cdeficiencia_sim_colaborador_as.setGeometry(QRect(20, 0, 41, 20))
        self.input_pessoa_cdeficiencia_nao_colaborador_as = QRadioButton(self.frame_237)
        self.input_pessoa_cdeficiencia_nao_colaborador_as.setObjectName(u"input_pessoa_cdeficiencia_nao_colaborador_as")
        self.input_pessoa_cdeficiencia_nao_colaborador_as.setGeometry(QRect(80, 0, 41, 20))

        self.verticalLayout_161.addWidget(self.frame_237)


        self.horizontalLayout_88.addWidget(self.frame_232)

        self.frame_233 = QFrame(self.frame_230)
        self.frame_233.setObjectName(u"frame_233")
        self.frame_233.setMinimumSize(QSize(251, 0))
        self.frame_233.setMaximumSize(QSize(251, 16777215))
        self.frame_233.setFrameShape(QFrame.StyledPanel)
        self.frame_233.setFrameShadow(QFrame.Raised)
        self.verticalLayout_163 = QVBoxLayout(self.frame_233)
        self.verticalLayout_163.setSpacing(5)
        self.verticalLayout_163.setObjectName(u"verticalLayout_163")
        self.verticalLayout_163.setContentsMargins(0, 0, 0, 0)
        self.label_tipo_deficiencia_colaborador_as = QLabel(self.frame_233)
        self.label_tipo_deficiencia_colaborador_as.setObjectName(u"label_tipo_deficiencia_colaborador_as")
        self.label_tipo_deficiencia_colaborador_as.setFont(font)

        self.verticalLayout_163.addWidget(self.label_tipo_deficiencia_colaborador_as)

        self.input_tipo_deficiencia_colaborador_as = QLineEdit(self.frame_233)
        self.input_tipo_deficiencia_colaborador_as.setObjectName(u"input_tipo_deficiencia_colaborador_as")
        self.input_tipo_deficiencia_colaborador_as.setMinimumSize(QSize(250, 0))
        self.input_tipo_deficiencia_colaborador_as.setMaximumSize(QSize(250, 30))
        self.input_tipo_deficiencia_colaborador_as.setFont(font)

        self.verticalLayout_163.addWidget(self.input_tipo_deficiencia_colaborador_as)


        self.horizontalLayout_88.addWidget(self.frame_233)

        self.frame_234 = QFrame(self.frame_230)
        self.frame_234.setObjectName(u"frame_234")
        self.frame_234.setMinimumSize(QSize(155, 0))
        self.frame_234.setMaximumSize(QSize(155, 16777215))
        self.frame_234.setFrameShape(QFrame.StyledPanel)
        self.frame_234.setFrameShadow(QFrame.Raised)
        self.verticalLayout_162 = QVBoxLayout(self.frame_234)
        self.verticalLayout_162.setSpacing(5)
        self.verticalLayout_162.setObjectName(u"verticalLayout_162")
        self.verticalLayout_162.setContentsMargins(0, 0, 0, 0)
        self.label_escolaridade_colaborador_as = QLabel(self.frame_234)
        self.label_escolaridade_colaborador_as.setObjectName(u"label_escolaridade_colaborador_as")
        self.label_escolaridade_colaborador_as.setMinimumSize(QSize(155, 0))
        self.label_escolaridade_colaborador_as.setMaximumSize(QSize(155, 16777215))
        self.label_escolaridade_colaborador_as.setFont(font)

        self.verticalLayout_162.addWidget(self.label_escolaridade_colaborador_as)

        self.input_escolaridade_colaborador_comboBox_as = QComboBox(self.frame_234)
        self.input_escolaridade_colaborador_comboBox_as.addItem("")
        self.input_escolaridade_colaborador_comboBox_as.addItem("")
        self.input_escolaridade_colaborador_comboBox_as.addItem("")
        self.input_escolaridade_colaborador_comboBox_as.addItem("")
        self.input_escolaridade_colaborador_comboBox_as.addItem("")
        self.input_escolaridade_colaborador_comboBox_as.addItem("")
        self.input_escolaridade_colaborador_comboBox_as.addItem("")
        self.input_escolaridade_colaborador_comboBox_as.setObjectName(u"input_escolaridade_colaborador_comboBox_as")
        self.input_escolaridade_colaborador_comboBox_as.setMinimumSize(QSize(154, 30))
        self.input_escolaridade_colaborador_comboBox_as.setMaximumSize(QSize(154, 30))
        self.input_escolaridade_colaborador_comboBox_as.setFont(font)

        self.verticalLayout_162.addWidget(self.input_escolaridade_colaborador_comboBox_as)


        self.horizontalLayout_88.addWidget(self.frame_234)

        self.frame_235 = QFrame(self.frame_230)
        self.frame_235.setObjectName(u"frame_235")
        self.frame_235.setMinimumSize(QSize(211, 0))
        self.frame_235.setMaximumSize(QSize(146, 16777215))
        self.frame_235.setFrameShape(QFrame.StyledPanel)
        self.frame_235.setFrameShadow(QFrame.Raised)
        self.verticalLayout_165 = QVBoxLayout(self.frame_235)
        self.verticalLayout_165.setSpacing(5)
        self.verticalLayout_165.setObjectName(u"verticalLayout_165")
        self.verticalLayout_165.setContentsMargins(0, 0, 0, 0)
        self.label_cargo_colaborador_as = QLabel(self.frame_235)
        self.label_cargo_colaborador_as.setObjectName(u"label_cargo_colaborador_as")
        self.label_cargo_colaborador_as.setMinimumSize(QSize(240, 0))
        self.label_cargo_colaborador_as.setMaximumSize(QSize(240, 16777215))
        self.label_cargo_colaborador_as.setFont(font)

        self.verticalLayout_165.addWidget(self.label_cargo_colaborador_as)

        self.input_cargo_colaborador_comboBox_as = QComboBox(self.frame_235)
        self.input_cargo_colaborador_comboBox_as.addItem("")
        self.input_cargo_colaborador_comboBox_as.addItem("")
        self.input_cargo_colaborador_comboBox_as.addItem("")
        self.input_cargo_colaborador_comboBox_as.addItem("")
        self.input_cargo_colaborador_comboBox_as.addItem("")
        self.input_cargo_colaborador_comboBox_as.addItem("")
        self.input_cargo_colaborador_comboBox_as.addItem("")
        self.input_cargo_colaborador_comboBox_as.addItem("")
        self.input_cargo_colaborador_comboBox_as.setObjectName(u"input_cargo_colaborador_comboBox_as")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_cargo_colaborador_comboBox_as.sizePolicy().hasHeightForWidth())
        self.input_cargo_colaborador_comboBox_as.setSizePolicy(sizePolicy1)
        self.input_cargo_colaborador_comboBox_as.setMinimumSize(QSize(210, 30))
        self.input_cargo_colaborador_comboBox_as.setMaximumSize(QSize(145, 30))
        self.input_cargo_colaborador_comboBox_as.setFont(font)

        self.verticalLayout_165.addWidget(self.input_cargo_colaborador_comboBox_as)


        self.horizontalLayout_88.addWidget(self.frame_235)

        self.frame_236 = QFrame(self.frame_230)
        self.frame_236.setObjectName(u"frame_236")
        self.frame_236.setMaximumSize(QSize(170, 16777215))
        self.frame_236.setFrameShape(QFrame.StyledPanel)
        self.frame_236.setFrameShadow(QFrame.Raised)
        self.verticalLayout_164 = QVBoxLayout(self.frame_236)
        self.verticalLayout_164.setSpacing(5)
        self.verticalLayout_164.setObjectName(u"verticalLayout_164")
        self.verticalLayout_164.setContentsMargins(0, 0, 0, 0)
        self.label_periodo_colaborador_as = QLabel(self.frame_236)
        self.label_periodo_colaborador_as.setObjectName(u"label_periodo_colaborador_as")
        self.label_periodo_colaborador_as.setMaximumSize(QSize(170, 16777215))
        self.label_periodo_colaborador_as.setFont(font)

        self.verticalLayout_164.addWidget(self.label_periodo_colaborador_as)

        self.input_periodo_colaborador_comboBox_as = QComboBox(self.frame_236)
        self.input_periodo_colaborador_comboBox_as.addItem("")
        self.input_periodo_colaborador_comboBox_as.addItem("")
        self.input_periodo_colaborador_comboBox_as.addItem("")
        self.input_periodo_colaborador_comboBox_as.addItem("")
        self.input_periodo_colaborador_comboBox_as.addItem("")
        self.input_periodo_colaborador_comboBox_as.setObjectName(u"input_periodo_colaborador_comboBox_as")
        self.input_periodo_colaborador_comboBox_as.setMinimumSize(QSize(70, 30))
        self.input_periodo_colaborador_comboBox_as.setMaximumSize(QSize(145, 30))
        self.input_periodo_colaborador_comboBox_as.setFont(font)

        self.verticalLayout_164.addWidget(self.input_periodo_colaborador_comboBox_as)


        self.horizontalLayout_88.addWidget(self.frame_236)


        self.gridLayout_2.addWidget(self.frame_230, 4, 1, 1, 1)

        self.frame_214 = QFrame(self.frame_194)
        self.frame_214.setObjectName(u"frame_214")
        self.frame_214.setMinimumSize(QSize(0, 0))
        self.frame_214.setMaximumSize(QSize(16777215, 300))
        self.frame_214.setStyleSheet(u"")
        self.frame_214.setFrameShape(QFrame.StyledPanel)
        self.frame_214.setFrameShadow(QFrame.Raised)
        self.verticalLayout_172 = QVBoxLayout(self.frame_214)
        self.verticalLayout_172.setObjectName(u"verticalLayout_172")
        self.label_observacoes_gerais_colaborador_as = QLabel(self.frame_214)
        self.label_observacoes_gerais_colaborador_as.setObjectName(u"label_observacoes_gerais_colaborador_as")
        self.label_observacoes_gerais_colaborador_as.setMaximumSize(QSize(300, 50))
        self.label_observacoes_gerais_colaborador_as.setFont(font)

        self.verticalLayout_172.addWidget(self.label_observacoes_gerais_colaborador_as)

        self.input_observacoes_gerais_colaborador_as = QTextEdit(self.frame_214)
        self.input_observacoes_gerais_colaborador_as.setObjectName(u"input_observacoes_gerais_colaborador_as")
        self.input_observacoes_gerais_colaborador_as.setMaximumSize(QSize(1185, 235))
        self.input_observacoes_gerais_colaborador_as.setFont(font)
        self.input_observacoes_gerais_colaborador_as.setStyleSheet(u"QTextEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QTextEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout_172.addWidget(self.input_observacoes_gerais_colaborador_as)


        self.gridLayout_2.addWidget(self.frame_214, 6, 1, 1, 1)

        self.frame_201 = QFrame(self.frame_194)
        self.frame_201.setObjectName(u"frame_201")
        self.frame_201.setMinimumSize(QSize(0, 0))
        self.frame_201.setMaximumSize(QSize(16777215, 60))
        self.frame_201.setStyleSheet(u"")
        self.frame_201.setFrameShape(QFrame.StyledPanel)
        self.frame_201.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_201)
        self.horizontalLayout_79.setSpacing(5)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.frame_202 = QFrame(self.frame_201)
        self.frame_202.setObjectName(u"frame_202")
        self.frame_202.setMinimumSize(QSize(155, 0))
        self.frame_202.setMaximumSize(QSize(155, 16777215))
        self.frame_202.setFrameShape(QFrame.StyledPanel)
        self.frame_202.setFrameShadow(QFrame.Raised)
        self.verticalLayout_141 = QVBoxLayout(self.frame_202)
        self.verticalLayout_141.setSpacing(0)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.verticalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.label_orgao_expedidor_colaborador_as = QLabel(self.frame_202)
        self.label_orgao_expedidor_colaborador_as.setObjectName(u"label_orgao_expedidor_colaborador_as")
        self.label_orgao_expedidor_colaborador_as.setMinimumSize(QSize(155, 0))
        self.label_orgao_expedidor_colaborador_as.setMaximumSize(QSize(155, 16777215))
        self.label_orgao_expedidor_colaborador_as.setFont(font)

        self.verticalLayout_141.addWidget(self.label_orgao_expedidor_colaborador_as)

        self.input_orgao_expedidor_colaborador_as = QLineEdit(self.frame_202)
        self.input_orgao_expedidor_colaborador_as.setObjectName(u"input_orgao_expedidor_colaborador_as")
        self.input_orgao_expedidor_colaborador_as.setMinimumSize(QSize(154, 0))
        self.input_orgao_expedidor_colaborador_as.setMaximumSize(QSize(145, 30))
        self.input_orgao_expedidor_colaborador_as.setFont(font)

        self.verticalLayout_141.addWidget(self.input_orgao_expedidor_colaborador_as)


        self.horizontalLayout_79.addWidget(self.frame_202)

        self.frame_207 = QFrame(self.frame_201)
        self.frame_207.setObjectName(u"frame_207")
        self.frame_207.setMaximumSize(QSize(151, 16777215))
        self.frame_207.setFrameShape(QFrame.StyledPanel)
        self.frame_207.setFrameShadow(QFrame.Raised)
        self.verticalLayout_146 = QVBoxLayout(self.frame_207)
        self.verticalLayout_146.setSpacing(0)
        self.verticalLayout_146.setObjectName(u"verticalLayout_146")
        self.verticalLayout_146.setContentsMargins(0, 0, 0, 0)
        self.label_data_emissao_rg_colaborador_as = QLabel(self.frame_207)
        self.label_data_emissao_rg_colaborador_as.setObjectName(u"label_data_emissao_rg_colaborador_as")
        self.label_data_emissao_rg_colaborador_as.setMaximumSize(QSize(170, 16777215))
        self.label_data_emissao_rg_colaborador_as.setFont(font)

        self.verticalLayout_146.addWidget(self.label_data_emissao_rg_colaborador_as)

        self.input_data_emissao_rg_colaborador_as = QLineEdit(self.frame_207)
        self.input_data_emissao_rg_colaborador_as.setObjectName(u"input_data_emissao_rg_colaborador_as")
        self.input_data_emissao_rg_colaborador_as.setMinimumSize(QSize(150, 30))
        self.input_data_emissao_rg_colaborador_as.setMaximumSize(QSize(150, 30))
        self.input_data_emissao_rg_colaborador_as.setFont(font)

        self.verticalLayout_146.addWidget(self.input_data_emissao_rg_colaborador_as)


        self.horizontalLayout_79.addWidget(self.frame_207)

        self.frame_203 = QFrame(self.frame_201)
        self.frame_203.setObjectName(u"frame_203")
        self.frame_203.setMinimumSize(QSize(220, 0))
        self.frame_203.setMaximumSize(QSize(155, 16777215))
        self.frame_203.setFrameShape(QFrame.StyledPanel)
        self.frame_203.setFrameShadow(QFrame.Raised)
        self.verticalLayout_142 = QVBoxLayout(self.frame_203)
        self.verticalLayout_142.setSpacing(0)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.verticalLayout_142.setContentsMargins(0, 0, 0, 0)
        self.label_pis_colaborador_as = QLabel(self.frame_203)
        self.label_pis_colaborador_as.setObjectName(u"label_pis_colaborador_as")
        self.label_pis_colaborador_as.setFont(font)

        self.verticalLayout_142.addWidget(self.label_pis_colaborador_as)

        self.input_pis_colaborador_as = QLineEdit(self.frame_203)
        self.input_pis_colaborador_as.setObjectName(u"input_pis_colaborador_as")
        self.input_pis_colaborador_as.setMinimumSize(QSize(218, 30))
        self.input_pis_colaborador_as.setMaximumSize(QSize(145, 30))
        self.input_pis_colaborador_as.setFont(font)

        self.verticalLayout_142.addWidget(self.input_pis_colaborador_as)


        self.horizontalLayout_79.addWidget(self.frame_203)

        self.frame_204 = QFrame(self.frame_201)
        self.frame_204.setObjectName(u"frame_204")
        self.frame_204.setMinimumSize(QSize(146, 0))
        self.frame_204.setMaximumSize(QSize(146, 16777215))
        self.frame_204.setFrameShape(QFrame.StyledPanel)
        self.frame_204.setFrameShadow(QFrame.Raised)
        self.verticalLayout_143 = QVBoxLayout(self.frame_204)
        self.verticalLayout_143.setSpacing(5)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.verticalLayout_143.setContentsMargins(0, 0, 0, 0)
        self.label_sexo_colaborador_as = QLabel(self.frame_204)
        self.label_sexo_colaborador_as.setObjectName(u"label_sexo_colaborador_as")
        self.label_sexo_colaborador_as.setFont(font)

        self.verticalLayout_143.addWidget(self.label_sexo_colaborador_as)

        self.input_sexo_colaborador_comboBox_as = QComboBox(self.frame_204)
        self.input_sexo_colaborador_comboBox_as.addItem("")
        self.input_sexo_colaborador_comboBox_as.addItem("")
        self.input_sexo_colaborador_comboBox_as.addItem("")
        self.input_sexo_colaborador_comboBox_as.setObjectName(u"input_sexo_colaborador_comboBox_as")
        self.input_sexo_colaborador_comboBox_as.setMinimumSize(QSize(70, 30))
        self.input_sexo_colaborador_comboBox_as.setMaximumSize(QSize(145, 30))
        self.input_sexo_colaborador_comboBox_as.setFont(font)

        self.verticalLayout_143.addWidget(self.input_sexo_colaborador_comboBox_as)


        self.horizontalLayout_79.addWidget(self.frame_204)

        self.frame_205 = QFrame(self.frame_201)
        self.frame_205.setObjectName(u"frame_205")
        self.frame_205.setMinimumSize(QSize(155, 0))
        self.frame_205.setMaximumSize(QSize(155, 16777215))
        self.frame_205.setFrameShape(QFrame.StyledPanel)
        self.frame_205.setFrameShadow(QFrame.Raised)
        self.verticalLayout_144 = QVBoxLayout(self.frame_205)
        self.verticalLayout_144.setSpacing(0)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.verticalLayout_144.setContentsMargins(0, 0, 0, 0)
        self.label_telefone_colaborador_as = QLabel(self.frame_205)
        self.label_telefone_colaborador_as.setObjectName(u"label_telefone_colaborador_as")
        self.label_telefone_colaborador_as.setMinimumSize(QSize(155, 0))
        self.label_telefone_colaborador_as.setMaximumSize(QSize(155, 16777215))
        self.label_telefone_colaborador_as.setFont(font)

        self.verticalLayout_144.addWidget(self.label_telefone_colaborador_as)

        self.input_telefone_colaborador_as = QLineEdit(self.frame_205)
        self.input_telefone_colaborador_as.setObjectName(u"input_telefone_colaborador_as")
        self.input_telefone_colaborador_as.setMinimumSize(QSize(154, 30))
        self.input_telefone_colaborador_as.setMaximumSize(QSize(145, 30))
        self.input_telefone_colaborador_as.setFont(font)

        self.verticalLayout_144.addWidget(self.input_telefone_colaborador_as)


        self.horizontalLayout_79.addWidget(self.frame_205)

        self.frame_206 = QFrame(self.frame_201)
        self.frame_206.setObjectName(u"frame_206")
        self.frame_206.setMinimumSize(QSize(240, 0))
        self.frame_206.setMaximumSize(QSize(240, 16777215))
        self.frame_206.setFrameShape(QFrame.StyledPanel)
        self.frame_206.setFrameShadow(QFrame.Raised)
        self.verticalLayout_145 = QVBoxLayout(self.frame_206)
        self.verticalLayout_145.setSpacing(0)
        self.verticalLayout_145.setObjectName(u"verticalLayout_145")
        self.verticalLayout_145.setContentsMargins(0, 0, 0, 0)
        self.label_email_colaborador_as = QLabel(self.frame_206)
        self.label_email_colaborador_as.setObjectName(u"label_email_colaborador_as")
        self.label_email_colaborador_as.setMinimumSize(QSize(240, 0))
        self.label_email_colaborador_as.setMaximumSize(QSize(240, 16777215))
        self.label_email_colaborador_as.setFont(font)

        self.verticalLayout_145.addWidget(self.label_email_colaborador_as)

        self.input_email_colaborador_as = QLineEdit(self.frame_206)
        self.input_email_colaborador_as.setObjectName(u"input_email_colaborador_as")
        self.input_email_colaborador_as.setMinimumSize(QSize(239, 30))
        self.input_email_colaborador_as.setMaximumSize(QSize(230, 30))
        self.input_email_colaborador_as.setFont(font)

        self.verticalLayout_145.addWidget(self.input_email_colaborador_as)


        self.horizontalLayout_79.addWidget(self.frame_206)


        self.gridLayout_2.addWidget(self.frame_201, 1, 1, 1, 1)

        self.horizontalSpacer_51 = QSpacerItem(123, 55, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_51, 4, 0, 1, 1)

        self.horizontalSpacer_52 = QSpacerItem(194, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_52, 4, 2, 1, 1)

        self.frame_195 = QFrame(self.frame_194)
        self.frame_195.setObjectName(u"frame_195")
        self.frame_195.setMinimumSize(QSize(0, 0))
        self.frame_195.setMaximumSize(QSize(16777215, 60))
        self.frame_195.setStyleSheet(u"")
        self.frame_195.setFrameShape(QFrame.StyledPanel)
        self.frame_195.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_195)
        self.horizontalLayout_78.setSpacing(5)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.frame_196 = QFrame(self.frame_195)
        self.frame_196.setObjectName(u"frame_196")
        self.frame_196.setMinimumSize(QSize(160, 0))
        self.frame_196.setMaximumSize(QSize(160, 16777215))
        self.frame_196.setFrameShape(QFrame.StyledPanel)
        self.frame_196.setFrameShadow(QFrame.Raised)
        self.verticalLayout_136 = QVBoxLayout(self.frame_196)
        self.verticalLayout_136.setSpacing(0)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.verticalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.label_matricula_colaborador_as = QLabel(self.frame_196)
        self.label_matricula_colaborador_as.setObjectName(u"label_matricula_colaborador_as")
        self.label_matricula_colaborador_as.setMinimumSize(QSize(160, 0))
        self.label_matricula_colaborador_as.setMaximumSize(QSize(160, 16777215))
        self.label_matricula_colaborador_as.setFont(font)

        self.verticalLayout_136.addWidget(self.label_matricula_colaborador_as)

        self.input_matricula_colaborador_as = QLineEdit(self.frame_196)
        self.input_matricula_colaborador_as.setObjectName(u"input_matricula_colaborador_as")
        self.input_matricula_colaborador_as.setMinimumSize(QSize(159, 30))
        self.input_matricula_colaborador_as.setMaximumSize(QSize(150, 30))
        self.input_matricula_colaborador_as.setFont(font)

        self.verticalLayout_136.addWidget(self.input_matricula_colaborador_as)


        self.horizontalLayout_78.addWidget(self.frame_196)

        self.frame_197 = QFrame(self.frame_195)
        self.frame_197.setObjectName(u"frame_197")
        self.frame_197.setMinimumSize(QSize(431, 0))
        self.frame_197.setMaximumSize(QSize(431, 16777215))
        self.frame_197.setFrameShape(QFrame.StyledPanel)
        self.frame_197.setFrameShadow(QFrame.Raised)
        self.verticalLayout_137 = QVBoxLayout(self.frame_197)
        self.verticalLayout_137.setSpacing(0)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.verticalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.label_nome_colaborador_as = QLabel(self.frame_197)
        self.label_nome_colaborador_as.setObjectName(u"label_nome_colaborador_as")
        self.label_nome_colaborador_as.setMinimumSize(QSize(460, 0))
        self.label_nome_colaborador_as.setMaximumSize(QSize(460, 16777215))
        self.label_nome_colaborador_as.setFont(font)

        self.verticalLayout_137.addWidget(self.label_nome_colaborador_as)

        self.input_nome_colaborador_as = QLineEdit(self.frame_197)
        self.input_nome_colaborador_as.setObjectName(u"input_nome_colaborador_as")
        self.input_nome_colaborador_as.setMinimumSize(QSize(430, 30))
        self.input_nome_colaborador_as.setMaximumSize(QSize(430, 30))
        self.input_nome_colaborador_as.setFont(font)

        self.verticalLayout_137.addWidget(self.input_nome_colaborador_as)


        self.horizontalLayout_78.addWidget(self.frame_197)

        self.frame_200 = QFrame(self.frame_195)
        self.frame_200.setObjectName(u"frame_200")
        self.frame_200.setMinimumSize(QSize(155, 0))
        self.frame_200.setMaximumSize(QSize(155, 16777215))
        self.frame_200.setFrameShape(QFrame.StyledPanel)
        self.frame_200.setFrameShadow(QFrame.Raised)
        self.verticalLayout_140 = QVBoxLayout(self.frame_200)
        self.verticalLayout_140.setSpacing(0)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.verticalLayout_140.setContentsMargins(0, 0, 0, 0)
        self.label_data_nascimento_colaborador_as = QLabel(self.frame_200)
        self.label_data_nascimento_colaborador_as.setObjectName(u"label_data_nascimento_colaborador_as")
        self.label_data_nascimento_colaborador_as.setMinimumSize(QSize(155, 0))
        self.label_data_nascimento_colaborador_as.setMaximumSize(QSize(155, 16777215))
        self.label_data_nascimento_colaborador_as.setFont(font)

        self.verticalLayout_140.addWidget(self.label_data_nascimento_colaborador_as)

        self.input_data_nascimento_colaborador_as = QLineEdit(self.frame_200)
        self.input_data_nascimento_colaborador_as.setObjectName(u"input_data_nascimento_colaborador_as")
        self.input_data_nascimento_colaborador_as.setMinimumSize(QSize(154, 30))
        self.input_data_nascimento_colaborador_as.setMaximumSize(QSize(145, 16777215))
        self.input_data_nascimento_colaborador_as.setFont(font)

        self.verticalLayout_140.addWidget(self.input_data_nascimento_colaborador_as)


        self.horizontalLayout_78.addWidget(self.frame_200)

        self.frame_198 = QFrame(self.frame_195)
        self.frame_198.setObjectName(u"frame_198")
        self.frame_198.setMinimumSize(QSize(180, 0))
        self.frame_198.setMaximumSize(QSize(180, 16777215))
        self.frame_198.setFrameShape(QFrame.StyledPanel)
        self.frame_198.setFrameShadow(QFrame.Raised)
        self.verticalLayout_138 = QVBoxLayout(self.frame_198)
        self.verticalLayout_138.setSpacing(0)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.verticalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.label_cpf_colaborador_as = QLabel(self.frame_198)
        self.label_cpf_colaborador_as.setObjectName(u"label_cpf_colaborador_as")
        self.label_cpf_colaborador_as.setMinimumSize(QSize(180, 0))
        self.label_cpf_colaborador_as.setMaximumSize(QSize(180, 16777215))
        self.label_cpf_colaborador_as.setFont(font)

        self.verticalLayout_138.addWidget(self.label_cpf_colaborador_as)

        self.input_cpf_colaborador_as = QLineEdit(self.frame_198)
        self.input_cpf_colaborador_as.setObjectName(u"input_cpf_colaborador_as")
        self.input_cpf_colaborador_as.setMinimumSize(QSize(179, 30))
        self.input_cpf_colaborador_as.setMaximumSize(QSize(170, 16777215))
        self.input_cpf_colaborador_as.setFont(font)

        self.verticalLayout_138.addWidget(self.input_cpf_colaborador_as)


        self.horizontalLayout_78.addWidget(self.frame_198)

        self.frame_199 = QFrame(self.frame_195)
        self.frame_199.setObjectName(u"frame_199")
        self.frame_199.setMinimumSize(QSize(160, 0))
        self.frame_199.setMaximumSize(QSize(160, 16777215))
        self.frame_199.setFrameShape(QFrame.StyledPanel)
        self.frame_199.setFrameShadow(QFrame.Raised)
        self.verticalLayout_139 = QVBoxLayout(self.frame_199)
        self.verticalLayout_139.setSpacing(0)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.verticalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.label_rg_colaborador_as = QLabel(self.frame_199)
        self.label_rg_colaborador_as.setObjectName(u"label_rg_colaborador_as")
        self.label_rg_colaborador_as.setMinimumSize(QSize(160, 0))
        self.label_rg_colaborador_as.setMaximumSize(QSize(160, 16777215))
        self.label_rg_colaborador_as.setFont(font)

        self.verticalLayout_139.addWidget(self.label_rg_colaborador_as)

        self.input_rg_colaborador_as = QLineEdit(self.frame_199)
        self.input_rg_colaborador_as.setObjectName(u"input_rg_colaborador_as")
        self.input_rg_colaborador_as.setMinimumSize(QSize(159, 30))
        self.input_rg_colaborador_as.setMaximumSize(QSize(150, 16777215))
        self.input_rg_colaborador_as.setFont(font)

        self.verticalLayout_139.addWidget(self.input_rg_colaborador_as)


        self.horizontalLayout_78.addWidget(self.frame_199)


        self.gridLayout_2.addWidget(self.frame_195, 0, 1, 1, 1)

        self.frame_208 = QFrame(self.frame_194)
        self.frame_208.setObjectName(u"frame_208")
        self.frame_208.setMinimumSize(QSize(0, 0))
        self.frame_208.setMaximumSize(QSize(16777215, 60))
        self.frame_208.setStyleSheet(u"")
        self.frame_208.setFrameShape(QFrame.StyledPanel)
        self.frame_208.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_208)
        self.horizontalLayout_89.setSpacing(5)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.frame_240 = QFrame(self.frame_208)
        self.frame_240.setObjectName(u"frame_240")
        self.frame_240.setMinimumSize(QSize(150, 0))
        self.frame_240.setMaximumSize(QSize(151, 16777215))
        self.frame_240.setFrameShape(QFrame.StyledPanel)
        self.frame_240.setFrameShadow(QFrame.Raised)
        self.verticalLayout_147 = QVBoxLayout(self.frame_240)
        self.verticalLayout_147.setSpacing(5)
        self.verticalLayout_147.setObjectName(u"verticalLayout_147")
        self.verticalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.label_cep_colaborador_as = QLabel(self.frame_240)
        self.label_cep_colaborador_as.setObjectName(u"label_cep_colaborador_as")
        self.label_cep_colaborador_as.setMinimumSize(QSize(100, 0))
        self.label_cep_colaborador_as.setMaximumSize(QSize(100, 16777215))
        self.label_cep_colaborador_as.setFont(font)

        self.verticalLayout_147.addWidget(self.label_cep_colaborador_as)

        self.input_cep_colaborador_as = QLineEdit(self.frame_240)
        self.input_cep_colaborador_as.setObjectName(u"input_cep_colaborador_as")
        self.input_cep_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_cep_colaborador_as.setMaximumSize(QSize(150, 16777215))
        self.input_cep_colaborador_as.setFont(font)

        self.verticalLayout_147.addWidget(self.input_cep_colaborador_as)


        self.horizontalLayout_89.addWidget(self.frame_240)

        self.frame_209 = QFrame(self.frame_208)
        self.frame_209.setObjectName(u"frame_209")
        self.frame_209.setMinimumSize(QSize(281, 0))
        self.frame_209.setMaximumSize(QSize(281, 16777215))
        self.frame_209.setFrameShape(QFrame.StyledPanel)
        self.frame_209.setFrameShadow(QFrame.Raised)
        self.verticalLayout_174 = QVBoxLayout(self.frame_209)
        self.verticalLayout_174.setSpacing(5)
        self.verticalLayout_174.setObjectName(u"verticalLayout_174")
        self.verticalLayout_174.setContentsMargins(0, 0, 0, 0)
        self.label_logradouro_colaborador_as = QLabel(self.frame_209)
        self.label_logradouro_colaborador_as.setObjectName(u"label_logradouro_colaborador_as")
        self.label_logradouro_colaborador_as.setMinimumSize(QSize(280, 0))
        self.label_logradouro_colaborador_as.setMaximumSize(QSize(280, 16777215))
        self.label_logradouro_colaborador_as.setFont(font)

        self.verticalLayout_174.addWidget(self.label_logradouro_colaborador_as)

        self.input_logradouro_colaborador_as = QLineEdit(self.frame_209)
        self.input_logradouro_colaborador_as.setObjectName(u"input_logradouro_colaborador_as")
        self.input_logradouro_colaborador_as.setMinimumSize(QSize(280, 30))
        self.input_logradouro_colaborador_as.setMaximumSize(QSize(280, 30))
        self.input_logradouro_colaborador_as.setFont(font)

        self.verticalLayout_174.addWidget(self.input_logradouro_colaborador_as)


        self.horizontalLayout_89.addWidget(self.frame_209)

        self.frame_210 = QFrame(self.frame_208)
        self.frame_210.setObjectName(u"frame_210")
        self.frame_210.setMinimumSize(QSize(160, 0))
        self.frame_210.setMaximumSize(QSize(160, 16777215))
        self.frame_210.setFrameShape(QFrame.StyledPanel)
        self.frame_210.setFrameShadow(QFrame.Raised)
        self.verticalLayout_173 = QVBoxLayout(self.frame_210)
        self.verticalLayout_173.setSpacing(5)
        self.verticalLayout_173.setObjectName(u"verticalLayout_173")
        self.verticalLayout_173.setContentsMargins(0, 0, 0, 0)
        self.label_numero_colaborador_as = QLabel(self.frame_210)
        self.label_numero_colaborador_as.setObjectName(u"label_numero_colaborador_as")
        self.label_numero_colaborador_as.setMinimumSize(QSize(160, 0))
        self.label_numero_colaborador_as.setMaximumSize(QSize(160, 16777215))
        self.label_numero_colaborador_as.setFont(font)

        self.verticalLayout_173.addWidget(self.label_numero_colaborador_as)

        self.input_numero_colaborador_as = QLineEdit(self.frame_210)
        self.input_numero_colaborador_as.setObjectName(u"input_numero_colaborador_as")
        self.input_numero_colaborador_as.setMinimumSize(QSize(150, 30))
        self.input_numero_colaborador_as.setMaximumSize(QSize(159, 30))
        self.input_numero_colaborador_as.setFont(font)

        self.verticalLayout_173.addWidget(self.input_numero_colaborador_as)


        self.horizontalLayout_89.addWidget(self.frame_210)

        self.frame_211 = QFrame(self.frame_208)
        self.frame_211.setObjectName(u"frame_211")
        self.frame_211.setMinimumSize(QSize(230, 0))
        self.frame_211.setMaximumSize(QSize(230, 16777215))
        self.frame_211.setFrameShape(QFrame.StyledPanel)
        self.frame_211.setFrameShadow(QFrame.Raised)
        self.verticalLayout_149 = QVBoxLayout(self.frame_211)
        self.verticalLayout_149.setSpacing(0)
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.verticalLayout_149.setContentsMargins(0, 0, 0, 0)
        self.label_bairro_colaborador_as = QLabel(self.frame_211)
        self.label_bairro_colaborador_as.setObjectName(u"label_bairro_colaborador_as")
        self.label_bairro_colaborador_as.setMinimumSize(QSize(230, 0))
        self.label_bairro_colaborador_as.setMaximumSize(QSize(230, 16777215))
        self.label_bairro_colaborador_as.setFont(font)

        self.verticalLayout_149.addWidget(self.label_bairro_colaborador_as)

        self.input_bairro_colaborador_as = QLineEdit(self.frame_211)
        self.input_bairro_colaborador_as.setObjectName(u"input_bairro_colaborador_as")
        self.input_bairro_colaborador_as.setMinimumSize(QSize(220, 30))
        self.input_bairro_colaborador_as.setMaximumSize(QSize(229, 30))
        self.input_bairro_colaborador_as.setFont(font)

        self.verticalLayout_149.addWidget(self.input_bairro_colaborador_as)


        self.horizontalLayout_89.addWidget(self.frame_211)

        self.frame_212 = QFrame(self.frame_208)
        self.frame_212.setObjectName(u"frame_212")
        self.frame_212.setMinimumSize(QSize(180, 0))
        self.frame_212.setMaximumSize(QSize(180, 16777215))
        self.frame_212.setFrameShape(QFrame.StyledPanel)
        self.frame_212.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_212)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_cidade_colaborador_as = QLabel(self.frame_212)
        self.label_cidade_colaborador_as.setObjectName(u"label_cidade_colaborador_as")
        self.label_cidade_colaborador_as.setMinimumSize(QSize(180, 0))
        self.label_cidade_colaborador_as.setMaximumSize(QSize(180, 16777215))
        self.label_cidade_colaborador_as.setFont(font)

        self.verticalLayout_2.addWidget(self.label_cidade_colaborador_as)

        self.input_cidade_colaborador_as = QLineEdit(self.frame_212)
        self.input_cidade_colaborador_as.setObjectName(u"input_cidade_colaborador_as")
        self.input_cidade_colaborador_as.setMinimumSize(QSize(179, 30))
        self.input_cidade_colaborador_as.setMaximumSize(QSize(179, 30))
        self.input_cidade_colaborador_as.setFont(font)

        self.verticalLayout_2.addWidget(self.input_cidade_colaborador_as)


        self.horizontalLayout_89.addWidget(self.frame_212)

        self.frame_213 = QFrame(self.frame_208)
        self.frame_213.setObjectName(u"frame_213")
        self.frame_213.setMinimumSize(QSize(80, 0))
        self.frame_213.setMaximumSize(QSize(80, 16777215))
        self.frame_213.setFrameShape(QFrame.StyledPanel)
        self.frame_213.setFrameShadow(QFrame.Raised)
        self.verticalLayout_148 = QVBoxLayout(self.frame_213)
        self.verticalLayout_148.setSpacing(5)
        self.verticalLayout_148.setObjectName(u"verticalLayout_148")
        self.verticalLayout_148.setContentsMargins(0, 0, 0, 0)
        self.label_estado_colaborador_as = QLabel(self.frame_213)
        self.label_estado_colaborador_as.setObjectName(u"label_estado_colaborador_as")
        self.label_estado_colaborador_as.setMinimumSize(QSize(80, 0))
        self.label_estado_colaborador_as.setMaximumSize(QSize(80, 16777215))
        self.label_estado_colaborador_as.setFont(font)

        self.verticalLayout_148.addWidget(self.label_estado_colaborador_as)

        self.input_estado_colaborador_as = QLineEdit(self.frame_213)
        self.input_estado_colaborador_as.setObjectName(u"input_estado_colaborador_as")
        self.input_estado_colaborador_as.setMinimumSize(QSize(75, 30))
        self.input_estado_colaborador_as.setMaximumSize(QSize(75, 16777215))
        self.input_estado_colaborador_as.setFont(font)

        self.verticalLayout_148.addWidget(self.input_estado_colaborador_as)


        self.horizontalLayout_89.addWidget(self.frame_213)


        self.gridLayout_2.addWidget(self.frame_208, 2, 1, 1, 1)

        self.frame_258 = QFrame(self.frame_194)
        self.frame_258.setObjectName(u"frame_258")
        self.frame_258.setMinimumSize(QSize(125, 200))
        self.frame_258.setMaximumSize(QSize(125, 200))
        self.frame_258.setFrameShape(QFrame.StyledPanel)
        self.frame_258.setFrameShadow(QFrame.Raised)
        self.verticalLayout_179 = QVBoxLayout(self.frame_258)
        self.verticalLayout_179.setSpacing(0)
        self.verticalLayout_179.setObjectName(u"verticalLayout_179")
        self.verticalLayout_179.setContentsMargins(0, 0, 0, 0)
        self.input_foto_colaborador_as = QPushButton(self.frame_258)
        self.input_foto_colaborador_as.setObjectName(u"input_foto_colaborador_as")
        self.input_foto_colaborador_as.setMinimumSize(QSize(125, 153))
        self.input_foto_colaborador_as.setMaximumSize(QSize(125, 153))
        self.input_foto_colaborador_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.input_foto_colaborador_as.setStyleSheet(u"background-color: #F3B9BF; border: none")
        self.input_foto_colaborador_as.setIcon(icon11)
        self.input_foto_colaborador_as.setIconSize(QSize(120, 120))

        self.verticalLayout_179.addWidget(self.input_foto_colaborador_as)

        self.frame_259 = QFrame(self.frame_258)
        self.frame_259.setObjectName(u"frame_259")
        self.frame_259.setStyleSheet(u"background-color: rgb(243, 185, 191);")
        self.frame_259.setFrameShape(QFrame.StyledPanel)
        self.frame_259.setFrameShadow(QFrame.Raised)
        self.verticalLayout_178 = QVBoxLayout(self.frame_259)
        self.verticalLayout_178.setObjectName(u"verticalLayout_178")
        self.verticalLayout_178.setContentsMargins(0, 0, 0, 0)
        self.label_adicionar_foto__colaborador_as = QLabel(self.frame_259)
        self.label_adicionar_foto__colaborador_as.setObjectName(u"label_adicionar_foto__colaborador_as")
        self.label_adicionar_foto__colaborador_as.setMinimumSize(QSize(125, 0))
        self.label_adicionar_foto__colaborador_as.setMaximumSize(QSize(125, 16777215))
        self.label_adicionar_foto__colaborador_as.setFont(font)
        self.label_adicionar_foto__colaborador_as.setStyleSheet(u"background-color: rgb(243, 185, 191);")

        self.verticalLayout_178.addWidget(self.label_adicionar_foto__colaborador_as)


        self.verticalLayout_179.addWidget(self.frame_259)

        self.verticalSpacer = QSpacerItem(20, 19, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_179.addItem(self.verticalSpacer)


        self.gridLayout_2.addWidget(self.frame_258, 0, 0, 3, 1, Qt.AlignRight|Qt.AlignTop)

        self.frame_260 = QFrame(self.frame_194)
        self.frame_260.setObjectName(u"frame_260")
        self.frame_260.setFrameShape(QFrame.StyledPanel)
        self.frame_260.setFrameShadow(QFrame.Raised)
        self.verticalLayout_181 = QVBoxLayout(self.frame_260)
        self.verticalLayout_181.setSpacing(0)
        self.verticalLayout_181.setObjectName(u"verticalLayout_181")
        self.verticalLayout_181.setContentsMargins(0, 0, 0, 0)
        self.frame_261 = QFrame(self.frame_260)
        self.frame_261.setObjectName(u"frame_261")
        self.frame_261.setMinimumSize(QSize(195, 50))
        self.frame_261.setMaximumSize(QSize(195, 50))
        self.frame_261.setStyleSheet(u"background-color: #EC848C; border-radius: 10px")
        self.frame_261.setFrameShape(QFrame.StyledPanel)
        self.frame_261.setFrameShadow(QFrame.Raised)
        self.verticalLayout_180 = QVBoxLayout(self.frame_261)
        self.verticalLayout_180.setSpacing(0)
        self.verticalLayout_180.setObjectName(u"verticalLayout_180")
        self.verticalLayout_180.setContentsMargins(15, 0, 0, 0)
        self.label_situacao_colaborador_as = QLabel(self.frame_261)
        self.label_situacao_colaborador_as.setObjectName(u"label_situacao_colaborador_as")
        self.label_situacao_colaborador_as.setMaximumSize(QSize(130, 16777215))
        self.label_situacao_colaborador_as.setFont(font)

        self.verticalLayout_180.addWidget(self.label_situacao_colaborador_as)

        self.frame_262 = QFrame(self.frame_261)
        self.frame_262.setObjectName(u"frame_262")
        self.frame_262.setFrameShape(QFrame.StyledPanel)
        self.frame_262.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_262)
        self.horizontalLayout_90.setSpacing(0)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.input_situacao_ativo_colaborador_as = QRadioButton(self.frame_262)
        self.input_situacao_ativo_colaborador_as.setObjectName(u"input_situacao_ativo_colaborador_as")
        self.input_situacao_ativo_colaborador_as.setMaximumSize(QSize(80, 16777215))
        self.input_situacao_ativo_colaborador_as.setFont(font7)
        self.input_situacao_ativo_colaborador_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_90.addWidget(self.input_situacao_ativo_colaborador_as)

        self.input_situacao_inativo_colaborador_as = QRadioButton(self.frame_262)
        self.input_situacao_inativo_colaborador_as.setObjectName(u"input_situacao_inativo_colaborador_as")
        self.input_situacao_inativo_colaborador_as.setMaximumSize(QSize(80, 16777215))
        self.input_situacao_inativo_colaborador_as.setFont(font7)
        self.input_situacao_inativo_colaborador_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_90.addWidget(self.input_situacao_inativo_colaborador_as)


        self.verticalLayout_180.addWidget(self.frame_262)


        self.verticalLayout_181.addWidget(self.frame_261)


        self.gridLayout_2.addWidget(self.frame_260, 0, 2, 1, 1)


        self.horizontalLayout_77.addWidget(self.frame_194)


        self.verticalLayout_83.addWidget(self.frame_193)

        self.frame_215 = QFrame(self.page_cadastro_colaborador_as)
        self.frame_215.setObjectName(u"frame_215")
        self.frame_215.setMinimumSize(QSize(0, 0))
        self.frame_215.setFrameShape(QFrame.StyledPanel)
        self.frame_215.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_215)
        self.horizontalLayout_81.setSpacing(10)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_57 = QSpacerItem(280, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_57)

        self.frame_239 = QFrame(self.frame_215)
        self.frame_239.setObjectName(u"frame_239")
        self.frame_239.setMinimumSize(QSize(281, 0))
        self.frame_239.setMaximumSize(QSize(281, 16777215))
        self.frame_239.setFrameShape(QFrame.StyledPanel)
        self.frame_239.setFrameShadow(QFrame.Raised)
        self.verticalLayout_175 = QVBoxLayout(self.frame_239)
        self.verticalLayout_175.setSpacing(5)
        self.verticalLayout_175.setObjectName(u"verticalLayout_175")
        self.verticalLayout_175.setContentsMargins(0, 0, 0, 0)
        self.label_usuario_colaborador_as = QLabel(self.frame_239)
        self.label_usuario_colaborador_as.setObjectName(u"label_usuario_colaborador_as")
        self.label_usuario_colaborador_as.setMinimumSize(QSize(280, 0))
        self.label_usuario_colaborador_as.setMaximumSize(QSize(280, 16777215))
        self.label_usuario_colaborador_as.setFont(font)

        self.verticalLayout_175.addWidget(self.label_usuario_colaborador_as)

        self.input_usuario_colaborador_as = QLineEdit(self.frame_239)
        self.input_usuario_colaborador_as.setObjectName(u"input_usuario_colaborador_as")
        self.input_usuario_colaborador_as.setMinimumSize(QSize(280, 30))
        self.input_usuario_colaborador_as.setMaximumSize(QSize(280, 30))
        self.input_usuario_colaborador_as.setFont(font)

        self.verticalLayout_175.addWidget(self.input_usuario_colaborador_as)


        self.horizontalLayout_81.addWidget(self.frame_239)

        self.frame_250 = QFrame(self.frame_215)
        self.frame_250.setObjectName(u"frame_250")
        self.frame_250.setMinimumSize(QSize(230, 0))
        self.frame_250.setMaximumSize(QSize(230, 16777215))
        self.frame_250.setFrameShape(QFrame.StyledPanel)
        self.frame_250.setFrameShadow(QFrame.Raised)
        self.verticalLayout_168 = QVBoxLayout(self.frame_250)
        self.verticalLayout_168.setSpacing(0)
        self.verticalLayout_168.setObjectName(u"verticalLayout_168")
        self.verticalLayout_168.setContentsMargins(0, 0, 0, 0)
        self.label_senha_colaborador_as = QLabel(self.frame_250)
        self.label_senha_colaborador_as.setObjectName(u"label_senha_colaborador_as")
        self.label_senha_colaborador_as.setMinimumSize(QSize(230, 0))
        self.label_senha_colaborador_as.setMaximumSize(QSize(230, 16777215))
        self.label_senha_colaborador_as.setFont(font)

        self.verticalLayout_168.addWidget(self.label_senha_colaborador_as)

        self.input_senha_colaborador_as = QLineEdit(self.frame_250)
        self.input_senha_colaborador_as.setObjectName(u"input_senha_colaborador_as")
        self.input_senha_colaborador_as.setMinimumSize(QSize(220, 30))
        self.input_senha_colaborador_as.setMaximumSize(QSize(229, 30))
        self.input_senha_colaborador_as.setFont(font)

        self.verticalLayout_168.addWidget(self.input_senha_colaborador_as)


        self.horizontalLayout_81.addWidget(self.frame_250)

        self.frame_256 = QFrame(self.frame_215)
        self.frame_256.setObjectName(u"frame_256")
        self.frame_256.setMinimumSize(QSize(230, 0))
        self.frame_256.setMaximumSize(QSize(230, 16777215))
        self.frame_256.setFrameShape(QFrame.StyledPanel)
        self.frame_256.setFrameShadow(QFrame.Raised)
        self.verticalLayout_176 = QVBoxLayout(self.frame_256)
        self.verticalLayout_176.setSpacing(0)
        self.verticalLayout_176.setObjectName(u"verticalLayout_176")
        self.verticalLayout_176.setContentsMargins(0, 0, 0, 0)
        self.label_confirmar_senha_colaborador_as = QLabel(self.frame_256)
        self.label_confirmar_senha_colaborador_as.setObjectName(u"label_confirmar_senha_colaborador_as")
        self.label_confirmar_senha_colaborador_as.setMinimumSize(QSize(230, 0))
        self.label_confirmar_senha_colaborador_as.setMaximumSize(QSize(230, 16777215))
        self.label_confirmar_senha_colaborador_as.setFont(font)

        self.verticalLayout_176.addWidget(self.label_confirmar_senha_colaborador_as)

        self.input_confirmar_senha_colaborador_as = QLineEdit(self.frame_256)
        self.input_confirmar_senha_colaborador_as.setObjectName(u"input_confirmar_senha_colaborador_as")
        self.input_confirmar_senha_colaborador_as.setMinimumSize(QSize(220, 30))
        self.input_confirmar_senha_colaborador_as.setMaximumSize(QSize(229, 30))
        self.input_confirmar_senha_colaborador_as.setFont(font)

        self.verticalLayout_176.addWidget(self.input_confirmar_senha_colaborador_as)


        self.horizontalLayout_81.addWidget(self.frame_256)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_53)

        self.frame_257 = QFrame(self.frame_215)
        self.frame_257.setObjectName(u"frame_257")
        self.frame_257.setFrameShape(QFrame.StyledPanel)
        self.frame_257.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_257)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 27, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.btn_concluir_cadastro_colaborador_as = QPushButton(self.frame_257)
        self.btn_concluir_cadastro_colaborador_as.setObjectName(u"btn_concluir_cadastro_colaborador_as")
        self.btn_concluir_cadastro_colaborador_as.setMinimumSize(QSize(140, 40))
        self.btn_concluir_cadastro_colaborador_as.setMaximumSize(QSize(140, 40))
        self.btn_concluir_cadastro_colaborador_as.setFont(font9)
        self.btn_concluir_cadastro_colaborador_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.verticalLayout_5.addWidget(self.btn_concluir_cadastro_colaborador_as)


        self.horizontalLayout_81.addWidget(self.frame_257, 0, Qt.AlignRight)


        self.verticalLayout_83.addWidget(self.frame_215)

        self.stackedWidget_2.addWidget(self.page_cadastro_colaborador_as)
        self.page_cadastrar_cursos_e_oficinas_as = QWidget()
        self.page_cadastrar_cursos_e_oficinas_as.setObjectName(u"page_cadastrar_cursos_e_oficinas_as")
        self.verticalLayout_84 = QVBoxLayout(self.page_cadastrar_cursos_e_oficinas_as)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.frame_121 = QFrame(self.page_cadastrar_cursos_e_oficinas_as)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setStyleSheet(u"background-color: #F3B9BF; margin-bottom: 2em")
        self.frame_121.setFrameShape(QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_121)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_121)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: #EC848C; padding-top: 1.5em")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.label_3)


        self.verticalLayout_84.addWidget(self.frame_121)

        self.frame_122 = QFrame(self.page_cadastrar_cursos_e_oficinas_as)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_122)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_49 = QSpacerItem(185, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_49)

        self.frame_125 = QFrame(self.frame_122)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setStyleSheet(u"QLabel{margin-left: 0.25em}")
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_125)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(20, 0, 0, 0)
        self.frame_126 = QFrame(self.frame_125)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setMaximumSize(QSize(16777215, 60))
        self.frame_126.setFrameShape(QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_126)
        self.horizontalLayout_62.setSpacing(5)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.frame_141 = QFrame(self.frame_126)
        self.frame_141.setObjectName(u"frame_141")
        self.frame_141.setMinimumSize(QSize(160, 0))
        self.frame_141.setMaximumSize(QSize(160, 16777215))
        self.frame_141.setFrameShape(QFrame.StyledPanel)
        self.frame_141.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_141)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.label_data_inclusao_cursos_as = QLabel(self.frame_141)
        self.label_data_inclusao_cursos_as.setObjectName(u"label_data_inclusao_cursos_as")
        self.label_data_inclusao_cursos_as.setMinimumSize(QSize(160, 0))
        self.label_data_inclusao_cursos_as.setMaximumSize(QSize(160, 16777215))
        self.label_data_inclusao_cursos_as.setFont(font)

        self.verticalLayout_86.addWidget(self.label_data_inclusao_cursos_as)

        self.input_data_inclusao_cursos_as = QLineEdit(self.frame_141)
        self.input_data_inclusao_cursos_as.setObjectName(u"input_data_inclusao_cursos_as")
        self.input_data_inclusao_cursos_as.setMinimumSize(QSize(150, 30))
        self.input_data_inclusao_cursos_as.setMaximumSize(QSize(150, 30))
        self.input_data_inclusao_cursos_as.setFont(font)

        self.verticalLayout_86.addWidget(self.input_data_inclusao_cursos_as)


        self.horizontalLayout_62.addWidget(self.frame_141)

        self.frame_142 = QFrame(self.frame_126)
        self.frame_142.setObjectName(u"frame_142")
        self.frame_142.setMinimumSize(QSize(460, 0))
        self.frame_142.setMaximumSize(QSize(460, 16777215))
        self.frame_142.setFrameShape(QFrame.StyledPanel)
        self.frame_142.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_142)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.label_nome_cursos_as = QLabel(self.frame_142)
        self.label_nome_cursos_as.setObjectName(u"label_nome_cursos_as")
        self.label_nome_cursos_as.setMinimumSize(QSize(460, 0))
        self.label_nome_cursos_as.setMaximumSize(QSize(460, 16777215))
        self.label_nome_cursos_as.setFont(font)

        self.verticalLayout_95.addWidget(self.label_nome_cursos_as)

        self.input_nome_cursos_as = QLineEdit(self.frame_142)
        self.input_nome_cursos_as.setObjectName(u"input_nome_cursos_as")
        self.input_nome_cursos_as.setMinimumSize(QSize(450, 30))
        self.input_nome_cursos_as.setMaximumSize(QSize(450, 30))
        self.input_nome_cursos_as.setFont(font)

        self.verticalLayout_95.addWidget(self.input_nome_cursos_as)


        self.horizontalLayout_62.addWidget(self.frame_142)

        self.frame_143 = QFrame(self.frame_126)
        self.frame_143.setObjectName(u"frame_143")
        self.frame_143.setMinimumSize(QSize(185, 0))
        self.frame_143.setMaximumSize(QSize(185, 16777215))
        self.frame_143.setFrameShape(QFrame.StyledPanel)
        self.frame_143.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.frame_143)
        self.verticalLayout_96.setSpacing(0)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.label_tipo_cursos_as = QLabel(self.frame_143)
        self.label_tipo_cursos_as.setObjectName(u"label_tipo_cursos_as")
        self.label_tipo_cursos_as.setMinimumSize(QSize(185, 0))
        self.label_tipo_cursos_as.setMaximumSize(QSize(185, 16777215))
        self.label_tipo_cursos_as.setFont(font)

        self.verticalLayout_96.addWidget(self.label_tipo_cursos_as)

        self.input_tipo_cursos_as = QComboBox(self.frame_143)
        self.input_tipo_cursos_as.setObjectName(u"input_tipo_cursos_as")
        self.input_tipo_cursos_as.setMinimumSize(QSize(175, 30))
        self.input_tipo_cursos_as.setMaximumSize(QSize(175, 30))
        self.input_tipo_cursos_as.setFont(font)

        self.verticalLayout_96.addWidget(self.input_tipo_cursos_as)


        self.horizontalLayout_62.addWidget(self.frame_143)

        self.frame_144 = QFrame(self.frame_126)
        self.frame_144.setObjectName(u"frame_144")
        self.frame_144.setMinimumSize(QSize(195, 50))
        self.frame_144.setMaximumSize(QSize(195, 50))
        self.frame_144.setStyleSheet(u"background-color: #EC848C; border-radius: 10px")
        self.frame_144.setFrameShape(QFrame.StyledPanel)
        self.frame_144.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_144)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(15, 0, 0, 0)
        self.label_situacao_cursos_as = QLabel(self.frame_144)
        self.label_situacao_cursos_as.setObjectName(u"label_situacao_cursos_as")
        self.label_situacao_cursos_as.setFont(font)

        self.verticalLayout_97.addWidget(self.label_situacao_cursos_as)

        self.frame_145 = QFrame(self.frame_144)
        self.frame_145.setObjectName(u"frame_145")
        self.frame_145.setFrameShape(QFrame.StyledPanel)
        self.frame_145.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_145)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.input_ativo_cursos_as = QRadioButton(self.frame_145)
        self.input_ativo_cursos_as.setObjectName(u"input_ativo_cursos_as")
        self.input_ativo_cursos_as.setFont(font7)
        self.input_ativo_cursos_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_63.addWidget(self.input_ativo_cursos_as)

        self.input_inativo_cursos_as = QRadioButton(self.frame_145)
        self.input_inativo_cursos_as.setObjectName(u"input_inativo_cursos_as")
        self.input_inativo_cursos_as.setFont(font7)
        self.input_inativo_cursos_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_63.addWidget(self.input_inativo_cursos_as)


        self.verticalLayout_97.addWidget(self.frame_145)


        self.horizontalLayout_62.addWidget(self.frame_144)


        self.verticalLayout_85.addWidget(self.frame_126)

        self.frame_127 = QFrame(self.frame_125)
        self.frame_127.setObjectName(u"frame_127")
        self.frame_127.setMaximumSize(QSize(16777215, 100))
        self.frame_127.setFrameShape(QFrame.StyledPanel)
        self.frame_127.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_127)
        self.horizontalLayout_64.setSpacing(5)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.frame_146 = QFrame(self.frame_127)
        self.frame_146.setObjectName(u"frame_146")
        self.frame_146.setMinimumSize(QSize(360, 0))
        self.frame_146.setMaximumSize(QSize(360, 16777215))
        self.frame_146.setFrameShape(QFrame.StyledPanel)
        self.frame_146.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_146)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.label_responsavel_cursos_as = QLabel(self.frame_146)
        self.label_responsavel_cursos_as.setObjectName(u"label_responsavel_cursos_as")
        self.label_responsavel_cursos_as.setMinimumSize(QSize(360, 0))
        self.label_responsavel_cursos_as.setMaximumSize(QSize(360, 16777215))
        self.label_responsavel_cursos_as.setFont(font)

        self.verticalLayout_98.addWidget(self.label_responsavel_cursos_as)

        self.input_responsavel_cursos_as = QLineEdit(self.frame_146)
        self.input_responsavel_cursos_as.setObjectName(u"input_responsavel_cursos_as")
        self.input_responsavel_cursos_as.setMinimumSize(QSize(350, 30))
        self.input_responsavel_cursos_as.setMaximumSize(QSize(350, 30))
        self.input_responsavel_cursos_as.setFont(font)

        self.verticalLayout_98.addWidget(self.input_responsavel_cursos_as)


        self.horizontalLayout_64.addWidget(self.frame_146)

        self.frame_147 = QFrame(self.frame_127)
        self.frame_147.setObjectName(u"frame_147")
        self.frame_147.setMinimumSize(QSize(160, 0))
        self.frame_147.setMaximumSize(QSize(160, 16777215))
        self.frame_147.setFrameShape(QFrame.StyledPanel)
        self.frame_147.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.frame_147)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.label_data_inicio_cursos_as = QLabel(self.frame_147)
        self.label_data_inicio_cursos_as.setObjectName(u"label_data_inicio_cursos_as")
        self.label_data_inicio_cursos_as.setMinimumSize(QSize(160, 0))
        self.label_data_inicio_cursos_as.setMaximumSize(QSize(160, 16777215))
        self.label_data_inicio_cursos_as.setFont(font)

        self.verticalLayout_99.addWidget(self.label_data_inicio_cursos_as)

        self.input_data_inicio_cursos_as = QLineEdit(self.frame_147)
        self.input_data_inicio_cursos_as.setObjectName(u"input_data_inicio_cursos_as")
        self.input_data_inicio_cursos_as.setMinimumSize(QSize(150, 30))
        self.input_data_inicio_cursos_as.setMaximumSize(QSize(150, 30))
        self.input_data_inicio_cursos_as.setFont(font)

        self.verticalLayout_99.addWidget(self.input_data_inicio_cursos_as)


        self.horizontalLayout_64.addWidget(self.frame_147)

        self.frame_148 = QFrame(self.frame_127)
        self.frame_148.setObjectName(u"frame_148")
        self.frame_148.setMinimumSize(QSize(160, 0))
        self.frame_148.setMaximumSize(QSize(160, 16777215))
        self.frame_148.setFrameShape(QFrame.StyledPanel)
        self.frame_148.setFrameShadow(QFrame.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.frame_148)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.label_data_termino_cursos_as = QLabel(self.frame_148)
        self.label_data_termino_cursos_as.setObjectName(u"label_data_termino_cursos_as")
        self.label_data_termino_cursos_as.setMinimumSize(QSize(160, 0))
        self.label_data_termino_cursos_as.setMaximumSize(QSize(160, 16777215))
        self.label_data_termino_cursos_as.setFont(font)

        self.verticalLayout_100.addWidget(self.label_data_termino_cursos_as)

        self.input_data_termino_cursos_as = QLineEdit(self.frame_148)
        self.input_data_termino_cursos_as.setObjectName(u"input_data_termino_cursos_as")
        self.input_data_termino_cursos_as.setMinimumSize(QSize(150, 30))
        self.input_data_termino_cursos_as.setMaximumSize(QSize(150, 30))
        self.input_data_termino_cursos_as.setFont(font)

        self.verticalLayout_100.addWidget(self.input_data_termino_cursos_as)


        self.horizontalLayout_64.addWidget(self.frame_148)

        self.frame_149 = QFrame(self.frame_127)
        self.frame_149.setObjectName(u"frame_149")
        self.frame_149.setMaximumSize(QSize(400, 16777215))
        self.frame_149.setFrameShape(QFrame.StyledPanel)
        self.frame_149.setFrameShadow(QFrame.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.frame_149)
        self.verticalLayout_101.setSpacing(0)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.label_dias_aulas_cursos_as = QLabel(self.frame_149)
        self.label_dias_aulas_cursos_as.setObjectName(u"label_dias_aulas_cursos_as")
        self.label_dias_aulas_cursos_as.setFont(font)

        self.verticalLayout_101.addWidget(self.label_dias_aulas_cursos_as)

        self.frame_150 = QFrame(self.frame_149)
        self.frame_150.setObjectName(u"frame_150")
        self.frame_150.setMaximumSize(QSize(395, 16777215))
        self.frame_150.setFrameShape(QFrame.StyledPanel)
        self.frame_150.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_150)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(10, 0, 0, 0)
        self.frame_151 = QFrame(self.frame_150)
        self.frame_151.setObjectName(u"frame_151")
        self.frame_151.setMaximumSize(QSize(125, 16777215))
        self.frame_151.setFrameShape(QFrame.StyledPanel)
        self.frame_151.setFrameShadow(QFrame.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.frame_151)
        self.verticalLayout_102.setSpacing(5)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.btn_segunda_cursos_as = QPushButton(self.frame_151)
        self.btn_segunda_cursos_as.setObjectName(u"btn_segunda_cursos_as")
        self.btn_segunda_cursos_as.setMinimumSize(QSize(120, 30))
        self.btn_segunda_cursos_as.setMaximumSize(QSize(120, 30))
        self.btn_segunda_cursos_as.setFont(font7)
        self.btn_segunda_cursos_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_segunda_cursos_as.setStyleSheet(u"background-color: #F3B9BF; border: none; border-radius: 5px")

        self.verticalLayout_102.addWidget(self.btn_segunda_cursos_as)

        self.btn_quinta_cursos_as = QPushButton(self.frame_151)
        self.btn_quinta_cursos_as.setObjectName(u"btn_quinta_cursos_as")
        self.btn_quinta_cursos_as.setMinimumSize(QSize(120, 30))
        self.btn_quinta_cursos_as.setMaximumSize(QSize(120, 30))
        self.btn_quinta_cursos_as.setFont(font7)
        self.btn_quinta_cursos_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_quinta_cursos_as.setStyleSheet(u"background-color: #F3B9BF; border: none; border-radius: 5px")

        self.verticalLayout_102.addWidget(self.btn_quinta_cursos_as)


        self.horizontalLayout_65.addWidget(self.frame_151)

        self.frame_152 = QFrame(self.frame_150)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setMaximumSize(QSize(125, 16777215))
        self.frame_152.setFrameShape(QFrame.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.frame_152)
        self.verticalLayout_103.setSpacing(5)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.btn_terca_cursos_as = QPushButton(self.frame_152)
        self.btn_terca_cursos_as.setObjectName(u"btn_terca_cursos_as")
        self.btn_terca_cursos_as.setMinimumSize(QSize(120, 30))
        self.btn_terca_cursos_as.setMaximumSize(QSize(120, 30))
        self.btn_terca_cursos_as.setFont(font7)
        self.btn_terca_cursos_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_terca_cursos_as.setStyleSheet(u"background-color: #F3B9BF; border: none; border-radius: 5px")

        self.verticalLayout_103.addWidget(self.btn_terca_cursos_as)

        self.btn_sexta_cursos_as = QPushButton(self.frame_152)
        self.btn_sexta_cursos_as.setObjectName(u"btn_sexta_cursos_as")
        self.btn_sexta_cursos_as.setMinimumSize(QSize(120, 30))
        self.btn_sexta_cursos_as.setMaximumSize(QSize(120, 30))
        self.btn_sexta_cursos_as.setFont(font7)
        self.btn_sexta_cursos_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sexta_cursos_as.setStyleSheet(u"background-color: #F3B9BF; border: none; border-radius: 5px")

        self.verticalLayout_103.addWidget(self.btn_sexta_cursos_as)


        self.horizontalLayout_65.addWidget(self.frame_152)

        self.frame_153 = QFrame(self.frame_150)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setMaximumSize(QSize(125, 16777215))
        self.frame_153.setFrameShape(QFrame.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.frame_153)
        self.verticalLayout_104.setSpacing(5)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.btn_quarta_cursos_as = QPushButton(self.frame_153)
        self.btn_quarta_cursos_as.setObjectName(u"btn_quarta_cursos_as")
        self.btn_quarta_cursos_as.setMinimumSize(QSize(120, 30))
        self.btn_quarta_cursos_as.setMaximumSize(QSize(120, 30))
        self.btn_quarta_cursos_as.setFont(font7)
        self.btn_quarta_cursos_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_quarta_cursos_as.setStyleSheet(u"background-color: #F3B9BF; border: none; border-radius: 5px")

        self.verticalLayout_104.addWidget(self.btn_quarta_cursos_as)

        self.btn_sabado_cursos_as = QPushButton(self.frame_153)
        self.btn_sabado_cursos_as.setObjectName(u"btn_sabado_cursos_as")
        self.btn_sabado_cursos_as.setMinimumSize(QSize(120, 30))
        self.btn_sabado_cursos_as.setMaximumSize(QSize(120, 30))
        self.btn_sabado_cursos_as.setFont(font7)
        self.btn_sabado_cursos_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sabado_cursos_as.setStyleSheet(u"background-color: #F3B9BF; border: none; border-radius: 5px")

        self.verticalLayout_104.addWidget(self.btn_sabado_cursos_as)


        self.horizontalLayout_65.addWidget(self.frame_153)


        self.verticalLayout_101.addWidget(self.frame_150)


        self.horizontalLayout_64.addWidget(self.frame_149)


        self.verticalLayout_85.addWidget(self.frame_127)

        self.frame_136 = QFrame(self.frame_125)
        self.frame_136.setObjectName(u"frame_136")
        self.frame_136.setMaximumSize(QSize(16777215, 60))
        self.frame_136.setFrameShape(QFrame.StyledPanel)
        self.frame_136.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_136)
        self.horizontalLayout_66.setSpacing(5)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.frame_154 = QFrame(self.frame_136)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setMaximumSize(QSize(90, 16777215))
        self.frame_154.setFrameShape(QFrame.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_154)
        self.verticalLayout_105.setSpacing(0)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.label_horario_cursos_as = QLabel(self.frame_154)
        self.label_horario_cursos_as.setObjectName(u"label_horario_cursos_as")
        self.label_horario_cursos_as.setMaximumSize(QSize(90, 16777215))
        self.label_horario_cursos_as.setFont(font)
        self.label_horario_cursos_as.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_105.addWidget(self.label_horario_cursos_as)

        self.input_horario_cursos_as = QLineEdit(self.frame_154)
        self.input_horario_cursos_as.setObjectName(u"input_horario_cursos_as")
        self.input_horario_cursos_as.setMinimumSize(QSize(80, 0))
        self.input_horario_cursos_as.setMaximumSize(QSize(80, 30))
        self.input_horario_cursos_as.setFont(font)

        self.verticalLayout_105.addWidget(self.input_horario_cursos_as)


        self.horizontalLayout_66.addWidget(self.frame_154)

        self.widget = QWidget(self.frame_136)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(90, 16777215))
        self.verticalLayout_106 = QVBoxLayout(self.widget)
        self.verticalLayout_106.setSpacing(0)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.label_as_cursos_as = QLabel(self.widget)
        self.label_as_cursos_as.setObjectName(u"label_as_cursos_as")
        self.label_as_cursos_as.setMaximumSize(QSize(90, 16777215))
        self.label_as_cursos_as.setFont(font)
        self.label_as_cursos_as.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_106.addWidget(self.label_as_cursos_as)

        self.input_as_cursos_as = QLineEdit(self.widget)
        self.input_as_cursos_as.setObjectName(u"input_as_cursos_as")
        self.input_as_cursos_as.setMinimumSize(QSize(80, 30))
        self.input_as_cursos_as.setMaximumSize(QSize(80, 30))
        self.input_as_cursos_as.setFont(font)

        self.verticalLayout_106.addWidget(self.input_as_cursos_as)


        self.horizontalLayout_66.addWidget(self.widget)

        self.frame_155 = QFrame(self.frame_136)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setMinimumSize(QSize(250, 0))
        self.frame_155.setMaximumSize(QSize(250, 16777215))
        self.frame_155.setFrameShape(QFrame.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.frame_155)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.label_periodo_cursos_as = QLabel(self.frame_155)
        self.label_periodo_cursos_as.setObjectName(u"label_periodo_cursos_as")
        self.label_periodo_cursos_as.setMinimumSize(QSize(250, 0))
        self.label_periodo_cursos_as.setMaximumSize(QSize(250, 16777215))
        self.label_periodo_cursos_as.setFont(font)

        self.verticalLayout_107.addWidget(self.label_periodo_cursos_as)

        self.input_periodo_cursos_as = QComboBox(self.frame_155)
        self.input_periodo_cursos_as.setObjectName(u"input_periodo_cursos_as")
        self.input_periodo_cursos_as.setMinimumSize(QSize(240, 30))
        self.input_periodo_cursos_as.setMaximumSize(QSize(240, 30))
        self.input_periodo_cursos_as.setFont(font)

        self.verticalLayout_107.addWidget(self.input_periodo_cursos_as)


        self.horizontalLayout_66.addWidget(self.frame_155)

        self.frame_156 = QFrame(self.frame_136)
        self.frame_156.setObjectName(u"frame_156")
        self.frame_156.setMaximumSize(QSize(100, 16777215))
        self.frame_156.setFrameShape(QFrame.StyledPanel)
        self.frame_156.setFrameShadow(QFrame.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.frame_156)
        self.verticalLayout_108.setSpacing(0)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.label_vagas_cursos_as = QLabel(self.frame_156)
        self.label_vagas_cursos_as.setObjectName(u"label_vagas_cursos_as")
        self.label_vagas_cursos_as.setMaximumSize(QSize(100, 16777215))
        self.label_vagas_cursos_as.setFont(font)

        self.verticalLayout_108.addWidget(self.label_vagas_cursos_as)

        self.input_vagas_cursos_as = QLineEdit(self.frame_156)
        self.input_vagas_cursos_as.setObjectName(u"input_vagas_cursos_as")
        self.input_vagas_cursos_as.setMinimumSize(QSize(90, 30))
        self.input_vagas_cursos_as.setMaximumSize(QSize(90, 30))
        self.input_vagas_cursos_as.setFont(font)

        self.verticalLayout_108.addWidget(self.input_vagas_cursos_as)


        self.horizontalLayout_66.addWidget(self.frame_156)

        self.frame_157 = QFrame(self.frame_136)
        self.frame_157.setObjectName(u"frame_157")
        self.frame_157.setMinimumSize(QSize(160, 0))
        self.frame_157.setMaximumSize(QSize(160, 16777215))
        self.frame_157.setFrameShape(QFrame.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Raised)
        self.verticalLayout_109 = QVBoxLayout(self.frame_157)
        self.verticalLayout_109.setSpacing(0)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.label_cep_cursos_as = QLabel(self.frame_157)
        self.label_cep_cursos_as.setObjectName(u"label_cep_cursos_as")
        self.label_cep_cursos_as.setMinimumSize(QSize(160, 0))
        self.label_cep_cursos_as.setMaximumSize(QSize(160, 16777215))
        self.label_cep_cursos_as.setFont(font)

        self.verticalLayout_109.addWidget(self.label_cep_cursos_as)

        self.input_cep_cursos_as = QLineEdit(self.frame_157)
        self.input_cep_cursos_as.setObjectName(u"input_cep_cursos_as")
        self.input_cep_cursos_as.setMinimumSize(QSize(150, 30))
        self.input_cep_cursos_as.setMaximumSize(QSize(150, 30))
        self.input_cep_cursos_as.setFont(font)

        self.verticalLayout_109.addWidget(self.input_cep_cursos_as)


        self.horizontalLayout_66.addWidget(self.frame_157)

        self.frame_158 = QFrame(self.frame_136)
        self.frame_158.setObjectName(u"frame_158")
        self.frame_158.setMinimumSize(QSize(360, 0))
        self.frame_158.setMaximumSize(QSize(360, 16777215))
        self.frame_158.setFrameShape(QFrame.StyledPanel)
        self.frame_158.setFrameShadow(QFrame.Raised)
        self.verticalLayout_110 = QVBoxLayout(self.frame_158)
        self.verticalLayout_110.setSpacing(0)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.label_logradouro_cursos_as = QLabel(self.frame_158)
        self.label_logradouro_cursos_as.setObjectName(u"label_logradouro_cursos_as")
        self.label_logradouro_cursos_as.setMinimumSize(QSize(360, 0))
        self.label_logradouro_cursos_as.setMaximumSize(QSize(360, 16777215))
        self.label_logradouro_cursos_as.setFont(font)

        self.verticalLayout_110.addWidget(self.label_logradouro_cursos_as)

        self.input_logradouro_cursos_as = QLineEdit(self.frame_158)
        self.input_logradouro_cursos_as.setObjectName(u"input_logradouro_cursos_as")
        self.input_logradouro_cursos_as.setMinimumSize(QSize(350, 30))
        self.input_logradouro_cursos_as.setMaximumSize(QSize(350, 30))
        self.input_logradouro_cursos_as.setFont(font)

        self.verticalLayout_110.addWidget(self.input_logradouro_cursos_as)


        self.horizontalLayout_66.addWidget(self.frame_158)


        self.verticalLayout_85.addWidget(self.frame_136)

        self.frame_139 = QFrame(self.frame_125)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setMaximumSize(QSize(16777215, 60))
        self.frame_139.setFrameShape(QFrame.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_139)
        self.horizontalLayout_67.setSpacing(5)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.frame_159 = QFrame(self.frame_139)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setMinimumSize(QSize(160, 0))
        self.frame_159.setMaximumSize(QSize(160, 16777215))
        self.frame_159.setFrameShape(QFrame.StyledPanel)
        self.frame_159.setFrameShadow(QFrame.Raised)
        self.verticalLayout_111 = QVBoxLayout(self.frame_159)
        self.verticalLayout_111.setSpacing(0)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.label_numero_cursos_as = QLabel(self.frame_159)
        self.label_numero_cursos_as.setObjectName(u"label_numero_cursos_as")
        self.label_numero_cursos_as.setMinimumSize(QSize(160, 0))
        self.label_numero_cursos_as.setMaximumSize(QSize(160, 16777215))
        self.label_numero_cursos_as.setFont(font)

        self.verticalLayout_111.addWidget(self.label_numero_cursos_as)

        self.input_numero_cursos_as = QLineEdit(self.frame_159)
        self.input_numero_cursos_as.setObjectName(u"input_numero_cursos_as")
        self.input_numero_cursos_as.setMinimumSize(QSize(150, 30))
        self.input_numero_cursos_as.setMaximumSize(QSize(150, 30))
        self.input_numero_cursos_as.setFont(font)

        self.verticalLayout_111.addWidget(self.input_numero_cursos_as)


        self.horizontalLayout_67.addWidget(self.frame_159)

        self.frame_160 = QFrame(self.frame_139)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setMinimumSize(QSize(230, 0))
        self.frame_160.setMaximumSize(QSize(230, 16777215))
        self.frame_160.setFrameShape(QFrame.StyledPanel)
        self.frame_160.setFrameShadow(QFrame.Raised)
        self.verticalLayout_112 = QVBoxLayout(self.frame_160)
        self.verticalLayout_112.setSpacing(0)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.label_bairro_cursos_as = QLabel(self.frame_160)
        self.label_bairro_cursos_as.setObjectName(u"label_bairro_cursos_as")
        self.label_bairro_cursos_as.setMinimumSize(QSize(230, 0))
        self.label_bairro_cursos_as.setMaximumSize(QSize(230, 16777215))
        self.label_bairro_cursos_as.setFont(font)

        self.verticalLayout_112.addWidget(self.label_bairro_cursos_as)

        self.input_bairro_cursos_as = QLineEdit(self.frame_160)
        self.input_bairro_cursos_as.setObjectName(u"input_bairro_cursos_as")
        self.input_bairro_cursos_as.setMinimumSize(QSize(220, 30))
        self.input_bairro_cursos_as.setMaximumSize(QSize(220, 30))
        self.input_bairro_cursos_as.setFont(font)

        self.verticalLayout_112.addWidget(self.input_bairro_cursos_as)


        self.horizontalLayout_67.addWidget(self.frame_160)

        self.frame_161 = QFrame(self.frame_139)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setMinimumSize(QSize(240, 0))
        self.frame_161.setMaximumSize(QSize(240, 16777215))
        self.frame_161.setFrameShape(QFrame.StyledPanel)
        self.frame_161.setFrameShadow(QFrame.Raised)
        self.verticalLayout_113 = QVBoxLayout(self.frame_161)
        self.verticalLayout_113.setSpacing(0)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.label_cidade_cursos_as = QLabel(self.frame_161)
        self.label_cidade_cursos_as.setObjectName(u"label_cidade_cursos_as")
        self.label_cidade_cursos_as.setMinimumSize(QSize(240, 0))
        self.label_cidade_cursos_as.setMaximumSize(QSize(240, 16777215))
        self.label_cidade_cursos_as.setFont(font)

        self.verticalLayout_113.addWidget(self.label_cidade_cursos_as)

        self.input_cidade_cursos_as = QLineEdit(self.frame_161)
        self.input_cidade_cursos_as.setObjectName(u"input_cidade_cursos_as")
        self.input_cidade_cursos_as.setMinimumSize(QSize(230, 30))
        self.input_cidade_cursos_as.setMaximumSize(QSize(230, 30))
        self.input_cidade_cursos_as.setFont(font)

        self.verticalLayout_113.addWidget(self.input_cidade_cursos_as)


        self.horizontalLayout_67.addWidget(self.frame_161)

        self.frame_162 = QFrame(self.frame_139)
        self.frame_162.setObjectName(u"frame_162")
        self.frame_162.setMinimumSize(QSize(80, 0))
        self.frame_162.setMaximumSize(QSize(80, 16777215))
        self.frame_162.setFrameShape(QFrame.StyledPanel)
        self.frame_162.setFrameShadow(QFrame.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.frame_162)
        self.verticalLayout_114.setSpacing(0)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.label_estado_cursos_as = QLabel(self.frame_162)
        self.label_estado_cursos_as.setObjectName(u"label_estado_cursos_as")
        self.label_estado_cursos_as.setMinimumSize(QSize(80, 0))
        self.label_estado_cursos_as.setMaximumSize(QSize(80, 16777215))
        self.label_estado_cursos_as.setFont(font)

        self.verticalLayout_114.addWidget(self.label_estado_cursos_as)

        self.input_estado_cursos_as = QComboBox(self.frame_162)
        self.input_estado_cursos_as.setObjectName(u"input_estado_cursos_as")
        self.input_estado_cursos_as.setMinimumSize(QSize(70, 30))
        self.input_estado_cursos_as.setMaximumSize(QSize(70, 30))

        self.verticalLayout_114.addWidget(self.input_estado_cursos_as)


        self.horizontalLayout_67.addWidget(self.frame_162)

        self.frame_163 = QFrame(self.frame_139)
        self.frame_163.setObjectName(u"frame_163")
        self.frame_163.setFrameShape(QFrame.StyledPanel)
        self.frame_163.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_67.addWidget(self.frame_163)


        self.verticalLayout_85.addWidget(self.frame_139)

        self.frame_140 = QFrame(self.frame_125)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setFrameShape(QFrame.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.frame_140)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.label_descricao_cursos_as = QLabel(self.frame_140)
        self.label_descricao_cursos_as.setObjectName(u"label_descricao_cursos_as")
        self.label_descricao_cursos_as.setFont(font)

        self.verticalLayout_115.addWidget(self.label_descricao_cursos_as)

        self.input_descricao_atividade_cursos_as = QTextEdit(self.frame_140)
        self.input_descricao_atividade_cursos_as.setObjectName(u"input_descricao_atividade_cursos_as")
        self.input_descricao_atividade_cursos_as.setMaximumSize(QSize(1400, 16777215))
        self.input_descricao_atividade_cursos_as.setFont(font)
        self.input_descricao_atividade_cursos_as.setStyleSheet(u"QTextEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QTextEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout_115.addWidget(self.input_descricao_atividade_cursos_as)


        self.verticalLayout_85.addWidget(self.frame_140)

        self.frame_138 = QFrame(self.frame_125)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setFrameShape(QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Raised)

        self.verticalLayout_85.addWidget(self.frame_138)


        self.horizontalLayout_61.addWidget(self.frame_125)

        self.horizontalSpacer_50 = QSpacerItem(185, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_50)

        self.horizontalLayout_61.setStretch(0, 1)
        self.horizontalLayout_61.setStretch(1, 8)
        self.horizontalLayout_61.setStretch(2, 1)

        self.verticalLayout_84.addWidget(self.frame_122)

        self.frame_124 = QFrame(self.page_cadastrar_cursos_e_oficinas_as)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setFrameShape(QFrame.StyledPanel)
        self.frame_124.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_124)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(20, 0, 0, 0)
        self.btn_lista_pessoas_cursos_as = QPushButton(self.frame_124)
        self.btn_lista_pessoas_cursos_as.setObjectName(u"btn_lista_pessoas_cursos_as")
        self.btn_lista_pessoas_cursos_as.setMinimumSize(QSize(0, 40))
        self.btn_lista_pessoas_cursos_as.setMaximumSize(QSize(16777215, 40))
        self.btn_lista_pessoas_cursos_as.setFont(font9)
        self.btn_lista_pessoas_cursos_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lista_pessoas_cursos_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        icon17 = QIcon()
        icon17.addFile(u"./icons/adicionar-amigo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lista_pessoas_cursos_as.setIcon(icon17)
        self.btn_lista_pessoas_cursos_as.setIconSize(QSize(25, 25))

        self.horizontalLayout_57.addWidget(self.btn_lista_pessoas_cursos_as)

        self.horizontalSpacer_48 = QSpacerItem(1441, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_48)

        self.btn_concluir_cursos_as = QPushButton(self.frame_124)
        self.btn_concluir_cursos_as.setObjectName(u"btn_concluir_cursos_as")
        self.btn_concluir_cursos_as.setMinimumSize(QSize(140, 40))
        self.btn_concluir_cursos_as.setMaximumSize(QSize(140, 40))
        self.btn_concluir_cursos_as.setFont(font9)
        self.btn_concluir_cursos_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_concluir_cursos_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout_57.addWidget(self.btn_concluir_cursos_as)


        self.verticalLayout_84.addWidget(self.frame_124)

        self.verticalLayout_84.setStretch(0, 1)
        self.verticalLayout_84.setStretch(1, 8)
        self.verticalLayout_84.setStretch(2, 1)
        self.stackedWidget_2.addWidget(self.page_cadastrar_cursos_e_oficinas_as)

        self.horizontalLayout_11.addWidget(self.stackedWidget_2)


        self.horizontalLayout_9.addWidget(self.frame_10)

        self.horizontalLayout_9.setStretch(1, 6)
        self.stack_assistente.addWidget(self.home_as)
        self.stack = QWidget()
        self.stack.setObjectName(u"stack")
        self.stack_assistente.addWidget(self.stack)

        self.verticalLayout.addWidget(self.stack_assistente)

        self.tipos_acesso.addWidget(self.assistente_social)
        self.farmaceutica = QWidget()
        self.farmaceutica.setObjectName(u"farmaceutica")
        self.verticalLayout_13 = QVBoxLayout(self.farmaceutica)
        self.verticalLayout_13.setSpacing(16)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.stack_farmaceutica = QStackedWidget(self.farmaceutica)
        self.stack_farmaceutica.setObjectName(u"stack_farmaceutica")
        self.home_farm = QWidget()
        self.home_farm.setObjectName(u"home_farm")
        self.horizontalLayout_17 = QHBoxLayout(self.home_farm)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.home_farm)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(226, 892))
        self.frame_20.setStyleSheet(u"QFrame{background-color: #E33B4E}")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_20)
        self.verticalLayout_14.setSpacing(16)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_foto_farm = QLabel(self.frame_20)
        self.label_foto_farm.setObjectName(u"label_foto_farm")
        self.label_foto_farm.setMinimumSize(QSize(140, 180))
        self.label_foto_farm.setStyleSheet(u"QLabel{margin-top: 42px}")
        self.label_foto_farm.setPixmap(QPixmap(u"./icons/Ellipse 1.png"))
        self.label_foto_farm.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_foto_farm)

        self.label_ola_nome_farm = QLabel(self.frame_20)
        self.label_ola_nome_farm.setObjectName(u"label_ola_nome_farm")
        self.label_ola_nome_farm.setFont(font2)
        self.label_ola_nome_farm.setStyleSheet(u"color: #fff; margin-bottom: 1em;")
        self.label_ola_nome_farm.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_ola_nome_farm)

        self.frame_51 = QFrame(self.frame_20)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_17)

        self.frame_52 = QFrame(self.frame_51)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setStyleSheet(u"")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_52)
        self.verticalLayout_35.setSpacing(20)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 10, 0, 10)
        self.btn_cadastrar_farm = QPushButton(self.frame_52)
        self.btn_cadastrar_farm.setObjectName(u"btn_cadastrar_farm")
        self.btn_cadastrar_farm.setMinimumSize(QSize(140, 45))
        self.btn_cadastrar_farm.setFont(font5)
        self.btn_cadastrar_farm.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_farm.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon18 = QIcon()
        icon18.addFile(u"./icons/remedio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar_farm.setIcon(icon18)
        self.btn_cadastrar_farm.setIconSize(QSize(30, 30))

        self.verticalLayout_35.addWidget(self.btn_cadastrar_farm)

        self.btn_retirar_farm = QPushButton(self.frame_52)
        self.btn_retirar_farm.setObjectName(u"btn_retirar_farm")
        self.btn_retirar_farm.setMinimumSize(QSize(140, 45))
        self.btn_retirar_farm.setFont(font5)
        self.btn_retirar_farm.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_retirar_farm.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon19 = QIcon()
        icon19.addFile(u"./icons/medicamento.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_retirar_farm.setIcon(icon19)
        self.btn_retirar_farm.setIconSize(QSize(30, 30))

        self.verticalLayout_35.addWidget(self.btn_retirar_farm)

        self.btn_estoque_farm = QPushButton(self.frame_52)
        self.btn_estoque_farm.setObjectName(u"btn_estoque_farm")
        self.btn_estoque_farm.setMinimumSize(QSize(140, 45))
        self.btn_estoque_farm.setFont(font5)
        self.btn_estoque_farm.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_estoque_farm.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon20 = QIcon()
        icon20.addFile(u"./icons/estoque-pronto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_estoque_farm.setIcon(icon20)
        self.btn_estoque_farm.setIconSize(QSize(30, 30))

        self.verticalLayout_35.addWidget(self.btn_estoque_farm)


        self.horizontalLayout_36.addWidget(self.frame_52)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_18)


        self.verticalLayout_14.addWidget(self.frame_51)

        self.verticalSpacer_5 = QSpacerItem(20, 240, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_21.setStyleSheet(u"")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_15)

        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"QFrame{background-color: #E33B4E}")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_23)
        self.verticalLayout_15.setSpacing(15)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 15)
        self.btn_voltar_farm = QPushButton(self.frame_23)
        self.btn_voltar_farm.setObjectName(u"btn_voltar_farm")
        self.btn_voltar_farm.setMinimumSize(QSize(120, 40))
        self.btn_voltar_farm.setFont(font2)
        self.btn_voltar_farm.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_farm.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.verticalLayout_15.addWidget(self.btn_voltar_farm)

        self.btn_sair_farm = QPushButton(self.frame_23)
        self.btn_sair_farm.setObjectName(u"btn_sair_farm")
        self.btn_sair_farm.setMinimumSize(QSize(120, 40))
        self.btn_sair_farm.setFont(font2)
        self.btn_sair_farm.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sair_farm.setLayoutDirection(Qt.RightToLeft)
        self.btn_sair_farm.setStyleSheet(u"QPushButton{color: #fff; background-color: #FF3636; border-radius: 20px;}\n"
"QPushButton:hover{background-color: 	hsl(0, 100%, 64%)}\n"
"QPushButton:focus{outline:0}")
        self.btn_sair_farm.setIcon(icon6)
        self.btn_sair_farm.setIconSize(QSize(24, 24))

        self.verticalLayout_15.addWidget(self.btn_sair_farm)


        self.horizontalLayout_15.addWidget(self.frame_23)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_16)


        self.verticalLayout_14.addWidget(self.frame_21)


        self.horizontalLayout_17.addWidget(self.frame_20)

        self.frame_22 = QFrame(self.home_farm)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"QFrame{background-color:#F9D9DD}")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_4 = QStackedWidget(self.frame_22)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.page_principal_farm = QWidget()
        self.page_principal_farm.setObjectName(u"page_principal_farm")
        self.stackedWidget_4.addWidget(self.page_principal_farm)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.stackedWidget_4.addWidget(self.page_10)

        self.horizontalLayout_16.addWidget(self.stackedWidget_4)


        self.horizontalLayout_17.addWidget(self.frame_22)

        self.horizontalLayout_17.setStretch(1, 6)
        self.stack_farmaceutica.addWidget(self.home_farm)

        self.verticalLayout_13.addWidget(self.stack_farmaceutica)

        self.tipos_acesso.addWidget(self.farmaceutica)
        self.fisioterapeuta = QWidget()
        self.fisioterapeuta.setObjectName(u"fisioterapeuta")
        self.verticalLayout_19 = QVBoxLayout(self.fisioterapeuta)
        self.verticalLayout_19.setSpacing(16)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.stack_fisioterapeuta = QStackedWidget(self.fisioterapeuta)
        self.stack_fisioterapeuta.setObjectName(u"stack_fisioterapeuta")
        self.home_fisio = QWidget()
        self.home_fisio.setObjectName(u"home_fisio")
        self.horizontalLayout_23 = QHBoxLayout(self.home_fisio)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.home_fisio)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(226, 892))
        self.frame_19.setStyleSheet(u"QFrame{background-color: #E33B4E}")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_19)
        self.verticalLayout_11.setSpacing(16)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_foto_fisio = QLabel(self.frame_19)
        self.label_foto_fisio.setObjectName(u"label_foto_fisio")
        self.label_foto_fisio.setMinimumSize(QSize(140, 180))
        self.label_foto_fisio.setStyleSheet(u"QLabel{margin-top: 42px}")
        self.label_foto_fisio.setPixmap(QPixmap(u"./icons/Ellipse 1.png"))
        self.label_foto_fisio.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_foto_fisio)

        self.label_ola_nome_fisio = QLabel(self.frame_19)
        self.label_ola_nome_fisio.setObjectName(u"label_ola_nome_fisio")
        self.label_ola_nome_fisio.setFont(font2)
        self.label_ola_nome_fisio.setStyleSheet(u"color: #fff; margin-bottom: 1em;")
        self.label_ola_nome_fisio.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_ola_nome_fisio)

        self.frame_30 = QFrame(self.frame_19)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_19)

        self.frame_53 = QFrame(self.frame_30)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setStyleSheet(u"")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_53)
        self.verticalLayout_20.setSpacing(20)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 10, 0, 10)
        self.btn_consulta_fisio = QPushButton(self.frame_53)
        self.btn_consulta_fisio.setObjectName(u"btn_consulta_fisio")
        self.btn_consulta_fisio.setMinimumSize(QSize(140, 45))
        self.btn_consulta_fisio.setFont(font5)
        self.btn_consulta_fisio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_consulta_fisio.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_consulta_fisio.setIcon(icon2)
        self.btn_consulta_fisio.setIconSize(QSize(30, 30))

        self.verticalLayout_20.addWidget(self.btn_consulta_fisio)

        self.btn_relatorios_fisio = QPushButton(self.frame_53)
        self.btn_relatorios_fisio.setObjectName(u"btn_relatorios_fisio")
        self.btn_relatorios_fisio.setMinimumSize(QSize(140, 45))
        self.btn_relatorios_fisio.setFont(font5)
        self.btn_relatorios_fisio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_relatorios_fisio.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_relatorios_fisio.setIcon(icon4)
        self.btn_relatorios_fisio.setIconSize(QSize(30, 30))

        self.verticalLayout_20.addWidget(self.btn_relatorios_fisio)


        self.horizontalLayout_37.addWidget(self.frame_53)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_20)


        self.verticalLayout_11.addWidget(self.frame_30)

        self.verticalSpacer_7 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_7)

        self.frame_28 = QFrame(self.frame_19)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_25)

        self.frame_54 = QFrame(self.frame_28)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setStyleSheet(u"")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_54)
        self.verticalLayout_36.setSpacing(15)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 15)
        self.btn_voltar_fisio = QPushButton(self.frame_54)
        self.btn_voltar_fisio.setObjectName(u"btn_voltar_fisio")
        self.btn_voltar_fisio.setMinimumSize(QSize(120, 40))
        self.btn_voltar_fisio.setFont(font2)
        self.btn_voltar_fisio.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.verticalLayout_36.addWidget(self.btn_voltar_fisio)

        self.btn_sair_fisio = QPushButton(self.frame_54)
        self.btn_sair_fisio.setObjectName(u"btn_sair_fisio")
        self.btn_sair_fisio.setMinimumSize(QSize(120, 40))
        self.btn_sair_fisio.setFont(font2)
        self.btn_sair_fisio.setLayoutDirection(Qt.RightToLeft)
        self.btn_sair_fisio.setStyleSheet(u"QPushButton{color: #fff; background-color: #FF3636; border-radius: 20px;}\n"
"QPushButton:hover{background-color: 	hsl(0, 100%, 64%)}\n"
"QPushButton:focus{outline:0}")
        self.btn_sair_fisio.setIcon(icon6)
        self.btn_sair_fisio.setIconSize(QSize(24, 24))

        self.verticalLayout_36.addWidget(self.btn_sair_fisio)


        self.horizontalLayout_21.addWidget(self.frame_54)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_26)


        self.verticalLayout_11.addWidget(self.frame_28)


        self.horizontalLayout_23.addWidget(self.frame_19)

        self.frame_29 = QFrame(self.home_fisio)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"QFrame{background-color:#F9D9DD}")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_5 = QStackedWidget(self.frame_29)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.page_principal_fisio = QWidget()
        self.page_principal_fisio.setObjectName(u"page_principal_fisio")
        self.stackedWidget_5.addWidget(self.page_principal_fisio)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.stackedWidget_5.addWidget(self.page_8)

        self.horizontalLayout_22.addWidget(self.stackedWidget_5)


        self.horizontalLayout_23.addWidget(self.frame_29)

        self.horizontalLayout_23.setStretch(1, 6)
        self.stack_fisioterapeuta.addWidget(self.home_fisio)

        self.verticalLayout_19.addWidget(self.stack_fisioterapeuta)

        self.tipos_acesso.addWidget(self.fisioterapeuta)
        self.nutricionista = QWidget()
        self.nutricionista.setObjectName(u"nutricionista")
        self.verticalLayout_16 = QVBoxLayout(self.nutricionista)
        self.verticalLayout_16.setSpacing(16)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.stack_nutricionista = QStackedWidget(self.nutricionista)
        self.stack_nutricionista.setObjectName(u"stack_nutricionista")
        self.home_nutri = QWidget()
        self.home_nutri.setObjectName(u"home_nutri")
        self.horizontalLayout_20 = QHBoxLayout(self.home_nutri)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.home_nutri)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(226, 892))
        self.frame_24.setStyleSheet(u"QFrame{background-color: #E33B4E}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_24)
        self.verticalLayout_17.setSpacing(16)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_foto_nutri = QLabel(self.frame_24)
        self.label_foto_nutri.setObjectName(u"label_foto_nutri")
        self.label_foto_nutri.setMinimumSize(QSize(140, 180))
        self.label_foto_nutri.setStyleSheet(u"QLabel{margin-top: 42px}")
        self.label_foto_nutri.setPixmap(QPixmap(u"./icons/Ellipse 1.png"))
        self.label_foto_nutri.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_foto_nutri)

        self.label_ola_nutri = QLabel(self.frame_24)
        self.label_ola_nutri.setObjectName(u"label_ola_nutri")
        self.label_ola_nutri.setFont(font2)
        self.label_ola_nutri.setStyleSheet(u"color: #fff; margin-bottom: 1em;")
        self.label_ola_nutri.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_ola_nutri)

        self.frame_27 = QFrame(self.frame_24)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_23)

        self.frame_56 = QFrame(self.frame_27)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_56)
        self.verticalLayout_37.setSpacing(20)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 10, 0, 10)
        self.btn_plano_alimentar_nutri = QPushButton(self.frame_56)
        self.btn_plano_alimentar_nutri.setObjectName(u"btn_plano_alimentar_nutri")
        self.btn_plano_alimentar_nutri.setMinimumSize(QSize(140, 45))
        font10 = QFont()
        font10.setFamilies([u"Six Caps"])
        font10.setPointSize(20)
        self.btn_plano_alimentar_nutri.setFont(font10)
        self.btn_plano_alimentar_nutri.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_plano_alimentar_nutri.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon21 = QIcon()
        icon21.addFile(u"./icons/seguranca-alimentar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_plano_alimentar_nutri.setIcon(icon21)
        self.btn_plano_alimentar_nutri.setIconSize(QSize(30, 30))

        self.verticalLayout_37.addWidget(self.btn_plano_alimentar_nutri)

        self.btn_consulta_nutri = QPushButton(self.frame_56)
        self.btn_consulta_nutri.setObjectName(u"btn_consulta_nutri")
        self.btn_consulta_nutri.setMinimumSize(QSize(140, 45))
        self.btn_consulta_nutri.setFont(font5)
        self.btn_consulta_nutri.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_consulta_nutri.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_consulta_nutri.setIcon(icon2)
        self.btn_consulta_nutri.setIconSize(QSize(30, 30))

        self.verticalLayout_37.addWidget(self.btn_consulta_nutri)

        self.btn_relatorios_nutri = QPushButton(self.frame_56)
        self.btn_relatorios_nutri.setObjectName(u"btn_relatorios_nutri")
        self.btn_relatorios_nutri.setMinimumSize(QSize(140, 45))
        self.btn_relatorios_nutri.setFont(font5)
        self.btn_relatorios_nutri.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_relatorios_nutri.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_relatorios_nutri.setIcon(icon4)
        self.btn_relatorios_nutri.setIconSize(QSize(30, 30))

        self.verticalLayout_37.addWidget(self.btn_relatorios_nutri)


        self.horizontalLayout_38.addWidget(self.frame_56)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_24)


        self.verticalLayout_17.addWidget(self.frame_27)

        self.verticalSpacer_6 = QSpacerItem(20, 220, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_6)

        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_21)

        self.frame_55 = QFrame(self.frame_25)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setStyleSheet(u"")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_55)
        self.verticalLayout_18.setSpacing(15)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 15)
        self.btn_voltar_nutri = QPushButton(self.frame_55)
        self.btn_voltar_nutri.setObjectName(u"btn_voltar_nutri")
        self.btn_voltar_nutri.setMinimumSize(QSize(120, 40))
        self.btn_voltar_nutri.setFont(font2)
        self.btn_voltar_nutri.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_nutri.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.verticalLayout_18.addWidget(self.btn_voltar_nutri)

        self.btn_sair_nutri = QPushButton(self.frame_55)
        self.btn_sair_nutri.setObjectName(u"btn_sair_nutri")
        self.btn_sair_nutri.setMinimumSize(QSize(120, 40))
        self.btn_sair_nutri.setMaximumSize(QSize(16777215, 16777215))
        self.btn_sair_nutri.setFont(font2)
        self.btn_sair_nutri.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sair_nutri.setLayoutDirection(Qt.RightToLeft)
        self.btn_sair_nutri.setStyleSheet(u"QPushButton{color: #fff; background-color: #FF3636; border-radius: 20px;}\n"
"QPushButton:hover{background-color: 	hsl(0, 100%, 64%)}\n"
"QPushButton:focus{outline:0}")
        self.btn_sair_nutri.setIcon(icon6)
        self.btn_sair_nutri.setIconSize(QSize(24, 24))

        self.verticalLayout_18.addWidget(self.btn_sair_nutri)


        self.horizontalLayout_18.addWidget(self.frame_55)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_22)


        self.verticalLayout_17.addWidget(self.frame_25)


        self.horizontalLayout_20.addWidget(self.frame_24)

        self.frame_26 = QFrame(self.home_nutri)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"QFrame{background-color:#F9D9DD}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_6 = QStackedWidget(self.frame_26)
        self.stackedWidget_6.setObjectName(u"stackedWidget_6")
        self.page_principal_nutri = QWidget()
        self.page_principal_nutri.setObjectName(u"page_principal_nutri")
        self.stackedWidget_6.addWidget(self.page_principal_nutri)
        self.page_plano_alimentar = QWidget()
        self.page_plano_alimentar.setObjectName(u"page_plano_alimentar")
        self.horizontalLayout_2 = QHBoxLayout(self.page_plano_alimentar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(526, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.frame_42 = QFrame(self.page_plano_alimentar)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(0, 0))
        self.frame_42.setStyleSheet(u"QFrame{padding: 3em;}")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_42)
        self.verticalLayout_27.setSpacing(40)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.btn_plano_alimentar_cadastrar_nutri = QPushButton(self.frame_42)
        self.btn_plano_alimentar_cadastrar_nutri.setObjectName(u"btn_plano_alimentar_cadastrar_nutri")
        self.btn_plano_alimentar_cadastrar_nutri.setMinimumSize(QSize(700, 154))
        self.btn_plano_alimentar_cadastrar_nutri.setMaximumSize(QSize(700, 154))
        self.btn_plano_alimentar_cadastrar_nutri.setFont(font6)
        self.btn_plano_alimentar_cadastrar_nutri.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_plano_alimentar_cadastrar_nutri.setLayoutDirection(Qt.RightToLeft)
        self.btn_plano_alimentar_cadastrar_nutri.setStyleSheet(u"QPushButton{color: #EC848C; background-color: #FEE4E1; border-radius: 20px ;border: none}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_plano_alimentar_cadastrar_nutri.setIcon(icon1)
        self.btn_plano_alimentar_cadastrar_nutri.setIconSize(QSize(80, 80))

        self.verticalLayout_27.addWidget(self.btn_plano_alimentar_cadastrar_nutri)

        self.btn_plano_alimentar_buscar_nutri = QPushButton(self.frame_42)
        self.btn_plano_alimentar_buscar_nutri.setObjectName(u"btn_plano_alimentar_buscar_nutri")
        self.btn_plano_alimentar_buscar_nutri.setMinimumSize(QSize(700, 154))
        self.btn_plano_alimentar_buscar_nutri.setMaximumSize(QSize(700, 154))
        self.btn_plano_alimentar_buscar_nutri.setFont(font6)
        self.btn_plano_alimentar_buscar_nutri.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_plano_alimentar_buscar_nutri.setLayoutDirection(Qt.RightToLeft)
        self.btn_plano_alimentar_buscar_nutri.setStyleSheet(u"QPushButton{color: #EC848C; background-color: #FEE4E1; border-radius: 20px ;border: none}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_plano_alimentar_buscar_nutri.setIcon(icon4)
        self.btn_plano_alimentar_buscar_nutri.setIconSize(QSize(80, 80))

        self.verticalLayout_27.addWidget(self.btn_plano_alimentar_buscar_nutri)


        self.horizontalLayout_2.addWidget(self.frame_42)

        self.horizontalSpacer_4 = QSpacerItem(526, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.stackedWidget_6.addWidget(self.page_plano_alimentar)

        self.horizontalLayout_19.addWidget(self.stackedWidget_6)


        self.horizontalLayout_20.addWidget(self.frame_26)

        self.horizontalLayout_20.setStretch(1, 6)
        self.stack_nutricionista.addWidget(self.home_nutri)

        self.verticalLayout_16.addWidget(self.stack_nutricionista)

        self.tipos_acesso.addWidget(self.nutricionista)
        self.psicologa = QWidget()
        self.psicologa.setObjectName(u"psicologa")
        self.verticalLayout_22 = QVBoxLayout(self.psicologa)
        self.verticalLayout_22.setSpacing(16)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.stack_psicologa = QStackedWidget(self.psicologa)
        self.stack_psicologa.setObjectName(u"stack_psicologa")
        self.home_psi = QWidget()
        self.home_psi.setObjectName(u"home_psi")
        self.horizontalLayout_26 = QHBoxLayout(self.home_psi)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.home_psi)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(226, 892))
        self.frame_33.setStyleSheet(u"QFrame{background-color: #E33B4E}")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_33)
        self.verticalLayout_24.setSpacing(16)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_foto_psi = QLabel(self.frame_33)
        self.label_foto_psi.setObjectName(u"label_foto_psi")
        self.label_foto_psi.setMinimumSize(QSize(140, 180))
        self.label_foto_psi.setStyleSheet(u"QLabel{margin-top: 42px}")
        self.label_foto_psi.setPixmap(QPixmap(u"./icons/Ellipse 1.png"))
        self.label_foto_psi.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_foto_psi)

        self.label_ola_nome_psi = QLabel(self.frame_33)
        self.label_ola_nome_psi.setObjectName(u"label_ola_nome_psi")
        self.label_ola_nome_psi.setFont(font2)
        self.label_ola_nome_psi.setStyleSheet(u"color: #fff; margin-bottom: 1em;")
        self.label_ola_nome_psi.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_ola_nome_psi)

        self.frame_58 = QFrame(self.frame_33)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setStyleSheet(u"")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_31)

        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFont(font10)
        self.frame_59.setStyleSheet(u"")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_59)
        self.verticalLayout_39.setSpacing(20)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 10, 0, 10)
        self.btn_consulta_psi = QPushButton(self.frame_59)
        self.btn_consulta_psi.setObjectName(u"btn_consulta_psi")
        self.btn_consulta_psi.setMinimumSize(QSize(140, 45))
        self.btn_consulta_psi.setFont(font5)
        self.btn_consulta_psi.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_consulta_psi.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_consulta_psi.setIcon(icon2)
        self.btn_consulta_psi.setIconSize(QSize(30, 30))

        self.verticalLayout_39.addWidget(self.btn_consulta_psi)

        self.btn_relatorios_psi = QPushButton(self.frame_59)
        self.btn_relatorios_psi.setObjectName(u"btn_relatorios_psi")
        self.btn_relatorios_psi.setMinimumSize(QSize(140, 45))
        self.btn_relatorios_psi.setFont(font5)
        self.btn_relatorios_psi.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_relatorios_psi.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_relatorios_psi.setIcon(icon4)
        self.btn_relatorios_psi.setIconSize(QSize(30, 30))

        self.verticalLayout_39.addWidget(self.btn_relatorios_psi)


        self.horizontalLayout_39.addWidget(self.frame_59)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_32)


        self.verticalLayout_24.addWidget(self.frame_58)

        self.verticalSpacer_8 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_8)

        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_27)

        self.frame_57 = QFrame(self.frame_34)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setStyleSheet(u"")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_57)
        self.verticalLayout_38.setSpacing(15)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 15)
        self.btn_voltar_psi = QPushButton(self.frame_57)
        self.btn_voltar_psi.setObjectName(u"btn_voltar_psi")
        self.btn_voltar_psi.setMinimumSize(QSize(120, 40))
        self.btn_voltar_psi.setFont(font2)
        self.btn_voltar_psi.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_psi.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.verticalLayout_38.addWidget(self.btn_voltar_psi)

        self.btn_sair_psi = QPushButton(self.frame_57)
        self.btn_sair_psi.setObjectName(u"btn_sair_psi")
        self.btn_sair_psi.setMinimumSize(QSize(120, 40))
        self.btn_sair_psi.setFont(font2)
        self.btn_sair_psi.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sair_psi.setLayoutDirection(Qt.RightToLeft)
        self.btn_sair_psi.setStyleSheet(u"QPushButton{color: #fff; background-color: #FF3636; border-radius: 20px;}\n"
"QPushButton:hover{background-color: 	hsl(0, 100%, 64%)}\n"
"QPushButton:focus{outline:0}")
        self.btn_sair_psi.setIcon(icon6)
        self.btn_sair_psi.setIconSize(QSize(24, 24))

        self.verticalLayout_38.addWidget(self.btn_sair_psi)


        self.horizontalLayout_25.addWidget(self.frame_57)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_28)


        self.verticalLayout_24.addWidget(self.frame_34)


        self.horizontalLayout_26.addWidget(self.frame_33)

        self.frame_31 = QFrame(self.home_psi)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"QFrame{background-color:#F9D9DD}")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_7 = QStackedWidget(self.frame_31)
        self.stackedWidget_7.setObjectName(u"stackedWidget_7")
        self.page_principal_psi = QWidget()
        self.page_principal_psi.setObjectName(u"page_principal_psi")
        self.stackedWidget_7.addWidget(self.page_principal_psi)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.stackedWidget_7.addWidget(self.page_14)

        self.horizontalLayout_24.addWidget(self.stackedWidget_7)


        self.horizontalLayout_26.addWidget(self.frame_31)

        self.horizontalLayout_26.setStretch(1, 6)
        self.stack_psicologa.addWidget(self.home_psi)

        self.verticalLayout_22.addWidget(self.stack_psicologa)

        self.tipos_acesso.addWidget(self.psicologa)
        self.secretaria = QWidget()
        self.secretaria.setObjectName(u"secretaria")
        self.secretaria.setMinimumSize(QSize(0, 0))
        self.secretaria.setFont(font2)
        self.secretaria.setCursor(QCursor(Qt.PointingHandCursor))
        self.secretaria.setLayoutDirection(Qt.LeftToRight)
        self.secretaria.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.secretaria)
        self.verticalLayout_9.setSpacing(16)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stack_secretaria = QStackedWidget(self.secretaria)
        self.stack_secretaria.setObjectName(u"stack_secretaria")
        self.home_sec = QWidget()
        self.home_sec.setObjectName(u"home_sec")
        self.horizontalLayout_8 = QHBoxLayout(self.home_sec)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.home_sec)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(226, 892))
        self.frame_15.setStyleSheet(u"QFrame{background-color: #E33B4E}")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_15)
        self.verticalLayout_10.setSpacing(16)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_foto_secret = QLabel(self.frame_15)
        self.label_foto_secret.setObjectName(u"label_foto_secret")
        self.label_foto_secret.setMinimumSize(QSize(140, 180))
        self.label_foto_secret.setStyleSheet(u"QLabel{margin-top: 42px}")
        self.label_foto_secret.setPixmap(QPixmap(u"./icons/Ellipse 1.png"))
        self.label_foto_secret.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_foto_secret)

        self.label_ola_nome_secret = QLabel(self.frame_15)
        self.label_ola_nome_secret.setObjectName(u"label_ola_nome_secret")
        self.label_ola_nome_secret.setFont(font2)
        self.label_ola_nome_secret.setStyleSheet(u"color: #fff; margin-bottom: 1em;")
        self.label_ola_nome_secret.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_ola_nome_secret)

        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)

        self.frame_50 = QFrame(self.frame_18)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setStyleSheet(u"")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_50)
        self.verticalLayout_12.setSpacing(20)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 10, 0, 10)
        self.btn_agenda_sec = QPushButton(self.frame_50)
        self.btn_agenda_sec.setObjectName(u"btn_agenda_sec")
        self.btn_agenda_sec.setMinimumSize(QSize(140, 45))
        self.btn_agenda_sec.setFont(font5)
        self.btn_agenda_sec.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agenda_sec.setLayoutDirection(Qt.LeftToRight)
        self.btn_agenda_sec.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_agenda_sec.setIcon(icon3)
        self.btn_agenda_sec.setIconSize(QSize(30, 30))

        self.verticalLayout_12.addWidget(self.btn_agenda_sec)

        self.btn_eventos_sec = QPushButton(self.frame_50)
        self.btn_eventos_sec.setObjectName(u"btn_eventos_sec")
        self.btn_eventos_sec.setMinimumSize(QSize(140, 45))
        self.btn_eventos_sec.setFont(font5)
        self.btn_eventos_sec.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_eventos_sec.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon22 = QIcon()
        icon22.addFile(u"./icons/festa-de-aniversario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_eventos_sec.setIcon(icon22)
        self.btn_eventos_sec.setIconSize(QSize(30, 30))

        self.verticalLayout_12.addWidget(self.btn_eventos_sec)

        self.btn_relatorios_sec = QPushButton(self.frame_50)
        self.btn_relatorios_sec.setObjectName(u"btn_relatorios_sec")
        self.btn_relatorios_sec.setMinimumSize(QSize(140, 45))
        self.btn_relatorios_sec.setFont(font5)
        self.btn_relatorios_sec.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_relatorios_sec.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_relatorios_sec.setIcon(icon4)
        self.btn_relatorios_sec.setIconSize(QSize(30, 30))

        self.verticalLayout_12.addWidget(self.btn_relatorios_sec)


        self.horizontalLayout_13.addWidget(self.frame_50)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)


        self.verticalLayout_10.addWidget(self.frame_18)

        self.verticalSpacer_4 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 0))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_11)

        self.frame_12 = QFrame(self.frame_17)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 15)
        self.btn_voltar_sec = QPushButton(self.frame_12)
        self.btn_voltar_sec.setObjectName(u"btn_voltar_sec")
        self.btn_voltar_sec.setMinimumSize(QSize(120, 40))
        self.btn_voltar_sec.setFont(font2)
        self.btn_voltar_sec.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_sec.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.verticalLayout_8.addWidget(self.btn_voltar_sec)

        self.btn_sair_sec = QPushButton(self.frame_12)
        self.btn_sair_sec.setObjectName(u"btn_sair_sec")
        self.btn_sair_sec.setMinimumSize(QSize(120, 40))
        self.btn_sair_sec.setFont(font2)
        self.btn_sair_sec.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sair_sec.setLayoutDirection(Qt.RightToLeft)
        self.btn_sair_sec.setStyleSheet(u"QPushButton{color: #fff; background-color: #FF3636; border-radius: 20px;}\n"
"QPushButton:hover{background-color: 	hsl(0, 100%, 64%)}\n"
"QPushButton:focus{outline:0}")
        self.btn_sair_sec.setIcon(icon6)
        self.btn_sair_sec.setIconSize(QSize(24, 24))

        self.verticalLayout_8.addWidget(self.btn_sair_sec)


        self.horizontalLayout_12.addWidget(self.frame_12)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)


        self.verticalLayout_10.addWidget(self.frame_17)


        self.horizontalLayout_8.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.home_sec)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"QFrame{background-color:#F9D9DD}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_3 = QStackedWidget(self.frame_16)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.page_principal_sec = QWidget()
        self.page_principal_sec.setObjectName(u"page_principal_sec")
        self.stackedWidget_3.addWidget(self.page_principal_sec)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget_3.addWidget(self.page_4)

        self.horizontalLayout_14.addWidget(self.stackedWidget_3)


        self.horizontalLayout_8.addWidget(self.frame_16)

        self.horizontalLayout_8.setStretch(1, 6)
        self.stack_secretaria.addWidget(self.home_sec)

        self.verticalLayout_9.addWidget(self.stack_secretaria)

        self.tipos_acesso.addWidget(self.secretaria)

        self.gridLayout.addWidget(self.tipos_acesso, 0, 0, 1, 1)

        self.inicio.addWidget(self.area_principal)

        self.verticalLayout_177.addWidget(self.inicio)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.inicio.setCurrentIndex(0)
        self.tipos_acesso.setCurrentIndex(0)
        self.stack_assistente.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stack_farmaceutica.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(0)
        self.stack_fisioterapeuta.setCurrentIndex(0)
        self.stackedWidget_5.setCurrentIndex(0)
        self.stack_nutricionista.setCurrentIndex(0)
        self.stackedWidget_6.setCurrentIndex(0)
        self.stack_psicologa.setCurrentIndex(0)
        self.stackedWidget_7.setCurrentIndex(0)
        self.stack_secretaria.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ABREC", None))
        self.input_usuario_login.setText("")
        self.input_usuario_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.label_2.setText("")
        self.input_senha_login.setText("")
        self.input_senha_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.toolButton.setText("")
        self.btn_entrar_login.setText(QCoreApplication.translate("MainWindow", u"ENTRAR", None))
        self.btn_esqueci_senha_login.setText(QCoreApplication.translate("MainWindow", u"Esqueci Senha", None))
        self.label_foto_as.setText("")
        self.label_ola_nome_as.setText(QCoreApplication.translate("MainWindow", u"Ol\u00e1, _ _ _ _ _ _", None))
        self.btn_cadastrar_as.setText(QCoreApplication.translate("MainWindow", u"  CADASTRAR", None))
        self.btn_consulta_as.setText(QCoreApplication.translate("MainWindow", u"   CONSULTA", None))
        self.btn_agenda_as.setText(QCoreApplication.translate("MainWindow", u"      AGENDA", None))
        self.btn_relatorios_as.setText(QCoreApplication.translate("MainWindow", u" RELAT\u00d3RIOS", None))
        self.btn_comunidade_as.setText(QCoreApplication.translate("MainWindow", u" COMUNIDADE", None))
        self.btn_voltar_as.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_sair_as.setText(QCoreApplication.translate("MainWindow", u"SAIR  ", None))
        self.btn_cadastrar_cuidador_usuario_as.setText(QCoreApplication.translate("MainWindow", u"CUIDADOR E USU\u00c1RIO                     ", None))
        self.btn_cadastrar_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"COLABORADOR                               ", None))
        self.btn_cadastrar_cursos_oficinas_as.setText(QCoreApplication.translate("MainWindow", u"CURSOS E OFICINAS                         ", None))
        self.btn_cadastrar_alterar_dados_as.setText(QCoreApplication.translate("MainWindow", u"ALTERAR DADOS CADASTRADOS        ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DO USU\u00c1RIO", None))
        self.btn_foto_usuario_as.setText("")
        self.label_matricula_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula", None))
        self.label_nome_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Nome do usu\u00e1rio", None))
        self.label_nascimento_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Data de nascimento", None))
        self.label_situacao_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Situa\u00e7\u00e3o", None))
        self.input_situacao_ativo_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Ativo", None))
        self.input_situacao_inativo_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Inativo", None))
        self.label_cpf_usuario_as.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.label_rg_usuario_as.setText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.label_data_emissao_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Data de emiss\u00e3o", None))
        self.label_orgao_expedidor_usuario_as.setText(QCoreApplication.translate("MainWindow", u"\u00d3rg\u00e3o expedidor", None))
        self.label_nis_usuario_as.setText(QCoreApplication.translate("MainWindow", u"NIS", None))
        self.label_cns_usuario_as.setText(QCoreApplication.translate("MainWindow", u"CNS", None))
        self.label_sexo_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.label_telefone_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.label_email_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_cep_usuario_as.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.label_logradouro_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.label_numero_usuario_as.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.label_bairro_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.label_cidade_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_estado_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.label_estado_civil_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Estado civil", None))
        self.label_escolaridade_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Escolaridade", None))
        self.label_pessoa_cdeficiencia_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Pessoa c/ defici\u00eancia", None))
        self.input_pessoa_cdeficiencia_sim_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.label_pessoa_cdeficiencia_nao_usuario_as.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_tipo_deficiencia_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Tipo de defici\u00eancia", None))
        self.label_renda_familiar_usuario_as.setText(QCoreApplication.translate("MainWindow", u"M\u00e9dia de renda familiar", None))
        self.label_meio_transporte_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Meio de transporte", None))
        self.label_vale_transporte_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Vale transporte", None))
        self.label_situacao_trabalho_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Situa\u00e7\u00e3o de trabalho", None))
        self.label_beneficios_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Benef\u00edcios", None))
        self.label_tarifa_social_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Tarifa social", None))
        self.input_tarifa_social_sim_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.input_tarifa_social_nao_usuario_as.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_tipo_tratamento_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Tipo de tratamento", None))
        self.label_local_tratamento_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Local de tratamento", None))
        self.label_patologia_base_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Patologia base", None))
        self.label_data_inicio_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Data de in\u00edcio", None))
        self.label_periodo_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo", None))
        self.btn_proximo_as.setText(QCoreApplication.translate("MainWindow", u"PR\u00d3XIMO", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DO CUIDADOR", None))
        self.label_matricula_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Matricula", None))
        self.label_nome_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Nome cuidador", None))
        self.input_nome_cuidador_as.setText("")
        self.label_cpf_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.input_cpf_cuidador_as.setText("")
        self.label_rg_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.input_rg_cuidador_as.setText("")
        self.label_data_emissao_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Data de emiss\u00e3o", None))
        self.input_data_emissao_cuidador_as.setText("")
        self.label_orgao_expedidor_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"\u00d3rg\u00e3o expedidor", None))
        self.label_sexo_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.label_parentesco_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Parentesco", None))
        self.label_telefone_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.label_email_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_cep_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.label_logradouro_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.label_numero_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.label_bairro_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.label_cidade_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_estado_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.label_observacoes_gerais_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es gerais Usu\u00e1rio e Cuidador", None))
        self.btn_observacoes_sigilo_as.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es em sigilo", None))
        self.btn_finalizar_as.setText(QCoreApplication.translate("MainWindow", u"FINALIZAR", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"OBSERVA\u00c7\u00d5ES SIGILOSAS", None))
        self.label_observacoes_obs_sigilosas_as.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es/informa\u00e7\u00f5es gerais", None))
        self.btn_alterar_observacoes_sigilosas_as.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_cancelar_observacoes_sigilosas_as.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.btn_salvar_observacoes_sigilosas_as.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_excluir_observacoes_sigilosas_as.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.label_cadastro_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DO COLABORADOR", None))
        self.label_salario_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Sal\u00e1rio", None))
        self.input_salario_colaborador_as.setText("")
        self.label_descricao_cargo_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o do cargo", None))
        self.label_estado_civil_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Estado civil", None))
        self.input_estado_civil_colaborador_comboBox_as.setItemText(0, QCoreApplication.translate("MainWindow", u"---", None))
        self.input_estado_civil_colaborador_comboBox_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Solteiro", None))
        self.input_estado_civil_colaborador_comboBox_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Casado", None))
        self.input_estado_civil_colaborador_comboBox_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Divorciado", None))
        self.input_estado_civil_colaborador_comboBox_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Vi\u00favo", None))
        self.input_estado_civil_colaborador_comboBox_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Separado", None))

        self.label_pessoa_cdeficiencia_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Pessoa c/ defici\u00eancia", None))
        self.input_pessoa_cdeficiencia_sim_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.input_pessoa_cdeficiencia_nao_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_tipo_deficiencia_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Tipo de defici\u00eancia", None))
        self.label_escolaridade_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Escolaridade", None))
        self.input_escolaridade_colaborador_comboBox_as.setItemText(0, QCoreApplication.translate("MainWindow", u"---", None))
        self.input_escolaridade_colaborador_comboBox_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Fundamental", None))
        self.input_escolaridade_colaborador_comboBox_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Fundamental incompleto", None))
        self.input_escolaridade_colaborador_comboBox_as.setItemText(3, QCoreApplication.translate("MainWindow", u"M\u00e9dio", None))
        self.input_escolaridade_colaborador_comboBox_as.setItemText(4, QCoreApplication.translate("MainWindow", u"M\u00e9dio incompleto", None))
        self.input_escolaridade_colaborador_comboBox_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Superior completo", None))
        self.input_escolaridade_colaborador_comboBox_as.setItemText(6, QCoreApplication.translate("MainWindow", u"Superior incompleto", None))

        self.label_cargo_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Cargo", None))
        self.input_cargo_colaborador_comboBox_as.setItemText(0, QCoreApplication.translate("MainWindow", u"---", None))
        self.input_cargo_colaborador_comboBox_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Recepcionista", None))
        self.input_cargo_colaborador_comboBox_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Assistente Social", None))
        self.input_cargo_colaborador_comboBox_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Farmac\u00eautico (a)", None))
        self.input_cargo_colaborador_comboBox_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Psic\u00f3logo (a)", None))
        self.input_cargo_colaborador_comboBox_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Fisioterapeuta", None))
        self.input_cargo_colaborador_comboBox_as.setItemText(6, QCoreApplication.translate("MainWindow", u"Nutricionista", None))
        self.input_cargo_colaborador_comboBox_as.setItemText(7, "")

        self.label_periodo_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo", None))
        self.input_periodo_colaborador_comboBox_as.setItemText(0, QCoreApplication.translate("MainWindow", u"---", None))
        self.input_periodo_colaborador_comboBox_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Matutino", None))
        self.input_periodo_colaborador_comboBox_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Vespertino", None))
        self.input_periodo_colaborador_comboBox_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Noturno", None))
        self.input_periodo_colaborador_comboBox_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Integral", None))

        self.label_observacoes_gerais_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es/informa\u00e7\u00f5es gerais", None))
        self.label_orgao_expedidor_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"\u00d3rg\u00e3o expedidor", None))
        self.label_data_emissao_rg_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Data de emiss\u00e3o", None))
        self.label_pis_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"PIS", None))
        self.label_sexo_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.input_sexo_colaborador_comboBox_as.setItemText(0, QCoreApplication.translate("MainWindow", u"---", None))
        self.input_sexo_colaborador_comboBox_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.input_sexo_colaborador_comboBox_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Feminino", None))

        self.label_telefone_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.label_email_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_matricula_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Matricula", None))
        self.label_nome_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Nome colaborador", None))
        self.input_nome_colaborador_as.setText("")
        self.label_data_nascimento_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Data de nascimento", None))
        self.input_data_nascimento_colaborador_as.setText("")
        self.label_cpf_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.input_cpf_colaborador_as.setText("")
        self.label_rg_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.input_rg_colaborador_as.setText("")
        self.label_cep_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.input_cep_colaborador_as.setText("")
        self.label_logradouro_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.label_numero_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.label_bairro_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.label_cidade_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_estado_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.input_estado_colaborador_as.setText("")
        self.input_foto_colaborador_as.setText("")
        self.label_adicionar_foto__colaborador_as.setText(QCoreApplication.translate("MainWindow", u"ADICIONAR FOTO", None))
        self.label_situacao_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Situa\u00e7\u00e3o", None))
        self.input_situacao_ativo_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Ativo", None))
        self.input_situacao_inativo_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Inativo", None))
        self.label_usuario_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.label_senha_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_confirmar_senha_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Confirmar Senha", None))
        self.btn_concluir_cadastro_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"CONCLUIR", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DE CURSOS E OFICINAS", None))
        self.label_data_inclusao_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Data de inclus\u00e3o", None))
        self.label_nome_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_tipo_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.label_situacao_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Situa\u00e7\u00e3o", None))
        self.input_ativo_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Ativo", None))
        self.input_inativo_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Inativo", None))
        self.label_responsavel_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Respons\u00e1vel", None))
        self.label_data_inicio_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Data de in\u00edcio", None))
        self.label_data_termino_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Data de t\u00e9rmino", None))
        self.label_dias_aulas_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Dias das aulas", None))
        self.btn_segunda_cursos_as.setText(QCoreApplication.translate("MainWindow", u"segunda-feira", None))
        self.btn_quinta_cursos_as.setText(QCoreApplication.translate("MainWindow", u"quinta-feira", None))
        self.btn_terca_cursos_as.setText(QCoreApplication.translate("MainWindow", u"ter\u00e7a-feira", None))
        self.btn_sexta_cursos_as.setText(QCoreApplication.translate("MainWindow", u"sexta-feira", None))
        self.btn_quarta_cursos_as.setText(QCoreApplication.translate("MainWindow", u"quarta-feira", None))
        self.btn_sabado_cursos_as.setText(QCoreApplication.translate("MainWindow", u"s\u00e1bado", None))
        self.label_horario_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Hor\u00e1rio", None))
        self.label_as_cursos_as.setText(QCoreApplication.translate("MainWindow", u"\u00e0s:", None))
        self.label_periodo_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo", None))
        self.label_vagas_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Vagas", None))
        self.label_cep_cursos_as.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.label_logradouro_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.label_numero_cursos_as.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.input_numero_cursos_as.setText("")
        self.label_bairro_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.input_bairro_cursos_as.setText("")
        self.label_cidade_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.input_cidade_cursos_as.setText("")
        self.label_estado_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.label_descricao_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o da atividade", None))
        self.btn_lista_pessoas_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Lista pessoas cadastradas", None))
        self.btn_concluir_cursos_as.setText(QCoreApplication.translate("MainWindow", u"CONCLUIR", None))
        self.label_foto_farm.setText("")
        self.label_ola_nome_farm.setText(QCoreApplication.translate("MainWindow", u"Ol\u00e1, _ _ _ _ _ _", None))
        self.btn_cadastrar_farm.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.btn_retirar_farm.setText(QCoreApplication.translate("MainWindow", u"   RETIRAR", None))
        self.btn_estoque_farm.setText(QCoreApplication.translate("MainWindow", u"   ESTOQUE", None))
        self.btn_voltar_farm.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_sair_farm.setText(QCoreApplication.translate("MainWindow", u"SAIR  ", None))
        self.label_foto_fisio.setText("")
        self.label_ola_nome_fisio.setText(QCoreApplication.translate("MainWindow", u"Ol\u00e1, _ _ _ _ _ _", None))
        self.btn_consulta_fisio.setText(QCoreApplication.translate("MainWindow", u"    CONSULTA", None))
        self.btn_relatorios_fisio.setText(QCoreApplication.translate("MainWindow", u"  RELAT\u00d3RIOS", None))
        self.btn_voltar_fisio.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_sair_fisio.setText(QCoreApplication.translate("MainWindow", u"SAIR  ", None))
        self.label_foto_nutri.setText("")
        self.label_ola_nutri.setText(QCoreApplication.translate("MainWindow", u"Ol\u00e1, _ _ _ _ _ _", None))
        self.btn_plano_alimentar_nutri.setText(QCoreApplication.translate("MainWindow", u" PLANO ALIMENTAR", None))
        self.btn_consulta_nutri.setText(QCoreApplication.translate("MainWindow", u"    CONSULTA", None))
        self.btn_relatorios_nutri.setText(QCoreApplication.translate("MainWindow", u"  RELAT\u00d3RIOS", None))
        self.btn_voltar_nutri.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_sair_nutri.setText(QCoreApplication.translate("MainWindow", u"SAIR  ", None))
        self.btn_plano_alimentar_cadastrar_nutri.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR                 ", None))
        self.btn_plano_alimentar_buscar_nutri.setText(QCoreApplication.translate("MainWindow", u"BUSCAR                    ", None))
        self.label_foto_psi.setText("")
        self.label_ola_nome_psi.setText(QCoreApplication.translate("MainWindow", u"Ol\u00e1, _ _ _ _ _ _", None))
        self.btn_consulta_psi.setText(QCoreApplication.translate("MainWindow", u"   CONSULTA", None))
        self.btn_relatorios_psi.setText(QCoreApplication.translate("MainWindow", u"  RELAT\u00d3RIOS", None))
        self.btn_voltar_psi.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_sair_psi.setText(QCoreApplication.translate("MainWindow", u"SAIR  ", None))
        self.label_foto_secret.setText("")
        self.label_ola_nome_secret.setText(QCoreApplication.translate("MainWindow", u"Ol\u00e1, _ _ _ _ _ _", None))
        self.btn_agenda_sec.setText(QCoreApplication.translate("MainWindow", u"    AGENDA", None))
        self.btn_eventos_sec.setText(QCoreApplication.translate("MainWindow", u"   EVENTOS", None))
        self.btn_relatorios_sec.setText(QCoreApplication.translate("MainWindow", u" RELAT\u00d3RIOS", None))
        self.btn_voltar_sec.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_sair_sec.setText(QCoreApplication.translate("MainWindow", u"SAIR  ", None))
    # retranslateUi

