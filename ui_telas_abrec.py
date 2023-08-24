# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'telas_abrecUxIhue.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QDateEdit, QDateTimeEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QTimeEdit, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2062, 986)
        font = QFont()
        font.setFamilies([u"Abel"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
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

        self.label_Logo_ABREC = QLabel(self.frame_35)
        self.label_Logo_ABREC.setObjectName(u"label_Logo_ABREC")
        font1 = QFont()
        font1.setFamilies([u"Abel"])
        font1.setPointSize(36)
        self.label_Logo_ABREC.setFont(font1)
        self.label_Logo_ABREC.setStyleSheet(u"color: #fff; background-color: #FA5858")
        self.label_Logo_ABREC.setPixmap(QPixmap(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/Logo ABREC.png"))
        self.label_Logo_ABREC.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.label_Logo_ABREC)

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
        self.label_2.setPixmap(QPixmap(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/pessoas.png"))
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
        icon.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/olho_fechado.png", QSize(), QIcon.Normal, QIcon.Off)
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

        self.frame_164 = QFrame(self.login)
        self.frame_164.setObjectName(u"frame_164")
        self.frame_164.setFrameShape(QFrame.StyledPanel)
        self.frame_164.setFrameShadow(QFrame.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.frame_164)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.verticalSpacer_11 = QSpacerItem(20, 786, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_116.addItem(self.verticalSpacer_11)

        self.label_Abrec_Logo_Paint = QLabel(self.frame_164)
        self.label_Abrec_Logo_Paint.setObjectName(u"label_Abrec_Logo_Paint")
        self.label_Abrec_Logo_Paint.setMaximumSize(QSize(75, 75))
        self.label_Abrec_Logo_Paint.setPixmap(QPixmap(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/Abrec logo paint-02 (2).png"))
        self.label_Abrec_Logo_Paint.setScaledContents(True)

        self.verticalLayout_116.addWidget(self.label_Abrec_Logo_Paint)


        self.horizontalLayout_32.addWidget(self.frame_164)

        self.inicio.addWidget(self.login)
        self.area_principal = QWidget()
        self.area_principal.setObjectName(u"area_principal")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(8)
        self.area_principal.setFont(font5)
        self.area_principal.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"QComboBox{color: #A85751; border-radius: 10px; border-width: 1px; border-style: solid; border-color:#A85751; padding-left: 10px;}\n"
"QComboBox:drop-down:hover{background-color:#fff}\n"
"QComboBox:drop-down{width: 24px; border-top-right-radius:9px; border-bottom-right-radius:9px; border-top-left-radius:1px; border-bottom-left-radius:1px;}\n"
"QComboBox:down-arrow{image: url(icons/expand.svg); }")
        self.gridLayout = QGridLayout(self.area_principal)
        self.gridLayout.setSpacing(0)
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
        self.btn_alterar_foto_senha_as = QPushButton(self.frame_9)
        self.btn_alterar_foto_senha_as.setObjectName(u"btn_alterar_foto_senha_as")
        self.btn_alterar_foto_senha_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_foto_senha_as.setStyleSheet(u"QPushButton{background-color: #E33B4E; border: none}")
        icon1 = QIcon()
        icon1.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/Ellipse 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar_foto_senha_as.setIcon(icon1)
        self.btn_alterar_foto_senha_as.setIconSize(QSize(140, 180))

        self.verticalLayout_6.addWidget(self.btn_alterar_foto_senha_as)

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
        font6 = QFont()
        font6.setFamilies([u"Six Caps"])
        font6.setPointSize(24)
        self.btn_cadastrar_as.setFont(font6)
        self.btn_cadastrar_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_as.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon2 = QIcon()
        icon2.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/cadastro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar_as.setIcon(icon2)
        self.btn_cadastrar_as.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.btn_cadastrar_as)

        self.btn_consulta_as = QPushButton(self.frame_14)
        self.btn_consulta_as.setObjectName(u"btn_consulta_as")
        self.btn_consulta_as.setMinimumSize(QSize(140, 45))
        self.btn_consulta_as.setMaximumSize(QSize(140, 45))
        self.btn_consulta_as.setFont(font6)
        self.btn_consulta_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_consulta_as.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon3 = QIcon()
        icon3.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/consultando.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_consulta_as.setIcon(icon3)
        self.btn_consulta_as.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.btn_consulta_as)

        self.btn_agenda_as = QPushButton(self.frame_14)
        self.btn_agenda_as.setObjectName(u"btn_agenda_as")
        self.btn_agenda_as.setMinimumSize(QSize(140, 45))
        self.btn_agenda_as.setMaximumSize(QSize(140, 45))
        self.btn_agenda_as.setFont(font6)
        self.btn_agenda_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agenda_as.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon4 = QIcon()
        icon4.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/agenda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agenda_as.setIcon(icon4)
        self.btn_agenda_as.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.btn_agenda_as)

        self.btn_relatorios_as = QPushButton(self.frame_14)
        self.btn_relatorios_as.setObjectName(u"btn_relatorios_as")
        self.btn_relatorios_as.setMinimumSize(QSize(140, 45))
        self.btn_relatorios_as.setMaximumSize(QSize(140, 45))
        self.btn_relatorios_as.setFont(font6)
        self.btn_relatorios_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_relatorios_as.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon5 = QIcon()
        icon5.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/relatorio-de-negocios.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_relatorios_as.setIcon(icon5)
        self.btn_relatorios_as.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.btn_relatorios_as)


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
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 20)
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
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 30)
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
        icon6.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/ligar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sair_as.setIcon(icon6)
        self.btn_sair_as.setIconSize(QSize(24, 24))

        self.verticalLayout_34.addWidget(self.btn_sair_as)

        self.frame_191 = QFrame(self.frame_11)
        self.frame_191.setObjectName(u"frame_191")
        self.frame_191.setMinimumSize(QSize(0, 30))
        self.frame_191.setMaximumSize(QSize(16777215, 30))
        self.frame_191.setFrameShape(QFrame.StyledPanel)
        self.frame_191.setFrameShadow(QFrame.Raised)

        self.verticalLayout_34.addWidget(self.frame_191)


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
        self.gridLayout_4 = QGridLayout(self.frame_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 8, 0)
        self.stackedWidget_2 = QStackedWidget(self.frame_10)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy)
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
        font7 = QFont()
        font7.setFamilies([u"Six Caps"])
        font7.setPointSize(60)
        self.btn_cadastrar_cuidador_usuario_as.setFont(font7)
        self.btn_cadastrar_cuidador_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_cuidador_usuario_as.setLayoutDirection(Qt.RightToLeft)
        self.btn_cadastrar_cuidador_usuario_as.setStyleSheet(u"QPushButton{color: #EC848C; background-color: #FEE4E1; border-radius: 20px ;border: none; padding: 1.5em}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon7 = QIcon()
        icon7.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/cuidado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar_cuidador_usuario_as.setIcon(icon7)
        self.btn_cadastrar_cuidador_usuario_as.setIconSize(QSize(80, 80))

        self.verticalLayout_23.addWidget(self.btn_cadastrar_cuidador_usuario_as)

        self.btn_cadastrar_colaborador_as = QPushButton(self.frame_32)
        self.btn_cadastrar_colaborador_as.setObjectName(u"btn_cadastrar_colaborador_as")
        self.btn_cadastrar_colaborador_as.setMinimumSize(QSize(700, 154))
        self.btn_cadastrar_colaborador_as.setMaximumSize(QSize(700, 154))
        self.btn_cadastrar_colaborador_as.setFont(font7)
        self.btn_cadastrar_colaborador_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_colaborador_as.setLayoutDirection(Qt.RightToLeft)
        self.btn_cadastrar_colaborador_as.setStyleSheet(u"QPushButton{color: #EC848C; background-color: #FEE4E1; border-radius: 20px ;border: none; padding: 1.5em}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon8 = QIcon()
        icon8.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/unidos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar_colaborador_as.setIcon(icon8)
        self.btn_cadastrar_colaborador_as.setIconSize(QSize(80, 80))

        self.verticalLayout_23.addWidget(self.btn_cadastrar_colaborador_as)

        self.btn_cadastrar_cursos_oficinas_as = QPushButton(self.frame_32)
        self.btn_cadastrar_cursos_oficinas_as.setObjectName(u"btn_cadastrar_cursos_oficinas_as")
        self.btn_cadastrar_cursos_oficinas_as.setMinimumSize(QSize(700, 154))
        self.btn_cadastrar_cursos_oficinas_as.setMaximumSize(QSize(700, 154))
        self.btn_cadastrar_cursos_oficinas_as.setFont(font7)
        self.btn_cadastrar_cursos_oficinas_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_cursos_oficinas_as.setLayoutDirection(Qt.RightToLeft)
        self.btn_cadastrar_cursos_oficinas_as.setStyleSheet(u"QPushButton{color: #EC848C; background-color: #FEE4E1; border-radius: 20px ;border: none; padding: 1.5em}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon9 = QIcon()
        icon9.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/certificados.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar_cursos_oficinas_as.setIcon(icon9)
        self.btn_cadastrar_cursos_oficinas_as.setIconSize(QSize(80, 80))

        self.verticalLayout_23.addWidget(self.btn_cadastrar_cursos_oficinas_as)

        self.btn_cadastrar_alterar_dados_as = QPushButton(self.frame_32)
        self.btn_cadastrar_alterar_dados_as.setObjectName(u"btn_cadastrar_alterar_dados_as")
        self.btn_cadastrar_alterar_dados_as.setMinimumSize(QSize(700, 154))
        self.btn_cadastrar_alterar_dados_as.setMaximumSize(QSize(700, 154))
        self.btn_cadastrar_alterar_dados_as.setFont(font7)
        self.btn_cadastrar_alterar_dados_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_alterar_dados_as.setLayoutDirection(Qt.RightToLeft)
        self.btn_cadastrar_alterar_dados_as.setStyleSheet(u"QPushButton{color: #EC848C; background-color: #FEE4E1; border-radius: 20px ;border: none}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon10 = QIcon()
        icon10.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/troca.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon11.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/adicionar foto.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.frame_61.setMinimumSize(QSize(0, 0))
        self.frame_61.setMaximumSize(QSize(160, 16777215))
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_61)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_matricula_usuario_as = QLabel(self.frame_61)
        self.label_matricula_usuario_as.setObjectName(u"label_matricula_usuario_as")
        self.label_matricula_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_matricula_usuario_as.setMaximumSize(QSize(160, 16777215))
        self.label_matricula_usuario_as.setFont(font)
        self.label_matricula_usuario_as.setStyleSheet(u"")

        self.verticalLayout_29.addWidget(self.label_matricula_usuario_as)

        self.input_matricula_usuario_as = QLineEdit(self.frame_61)
        self.input_matricula_usuario_as.setObjectName(u"input_matricula_usuario_as")
        self.input_matricula_usuario_as.setEnabled(False)
        self.input_matricula_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_matricula_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_matricula_usuario_as.setFont(font)

        self.verticalLayout_29.addWidget(self.input_matricula_usuario_as)


        self.horizontalLayout_7.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.frame_48)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(0, 0))
        self.frame_62.setMaximumSize(QSize(460, 16777215))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_62)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_nome_usuario_as = QLabel(self.frame_62)
        self.label_nome_usuario_as.setObjectName(u"label_nome_usuario_as")
        self.label_nome_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_nome_usuario_as.setMaximumSize(QSize(460, 16777215))
        self.label_nome_usuario_as.setFont(font)
        self.label_nome_usuario_as.setStyleSheet(u"")

        self.verticalLayout_30.addWidget(self.label_nome_usuario_as)

        self.input_nome_usuario_as = QLineEdit(self.frame_62)
        self.input_nome_usuario_as.setObjectName(u"input_nome_usuario_as")
        self.input_nome_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_nome_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_nome_usuario_as.setFont(font)

        self.verticalLayout_30.addWidget(self.input_nome_usuario_as)


        self.horizontalLayout_7.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.frame_48)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(0, 0))
        self.frame_63.setMaximumSize(QSize(160, 16777215))
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_63)
        self.verticalLayout_31.setSpacing(5)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_nascimento_usuario_as = QLabel(self.frame_63)
        self.label_nascimento_usuario_as.setObjectName(u"label_nascimento_usuario_as")
        self.label_nascimento_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_nascimento_usuario_as.setMaximumSize(QSize(160, 16777215))
        self.label_nascimento_usuario_as.setFont(font)
        self.label_nascimento_usuario_as.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_nascimento_usuario_as)

        self.input_nascimento_usuario_as = QDateEdit(self.frame_63)
        self.input_nascimento_usuario_as.setObjectName(u"input_nascimento_usuario_as")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_nascimento_usuario_as.sizePolicy().hasHeightForWidth())
        self.input_nascimento_usuario_as.setSizePolicy(sizePolicy1)
        self.input_nascimento_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_nascimento_usuario_as.setMaximumSize(QSize(16777215, 16777215))
        font8 = QFont()
        font8.setFamilies([u"Abel"])
        font8.setPointSize(11)
        self.input_nascimento_usuario_as.setFont(font8)
        self.input_nascimento_usuario_as.setFocusPolicy(Qt.WheelFocus)
        self.input_nascimento_usuario_as.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.input_nascimento_usuario_as.setLayoutDirection(Qt.LeftToRight)
        self.input_nascimento_usuario_as.setAutoFillBackground(False)
        self.input_nascimento_usuario_as.setStyleSheet(u"QDateEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QDateEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_nascimento_usuario_as.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.input_nascimento_usuario_as.setAlignment(Qt.AlignCenter)
        self.input_nascimento_usuario_as.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.input_nascimento_usuario_as.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.input_nascimento_usuario_as.setCurrentSection(QDateTimeEdit.DaySection)
        self.input_nascimento_usuario_as.setCalendarPopup(False)
        self.input_nascimento_usuario_as.setCurrentSectionIndex(0)

        self.verticalLayout_31.addWidget(self.input_nascimento_usuario_as, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.frame_48)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(195, 50))
        self.frame_64.setMaximumSize(QSize(195, 50))
        self.frame_64.setStyleSheet(u"background-color: #EC848C; border-radius: 10px")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_64)
        self.verticalLayout_32.setSpacing(6)
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
        self.input_situacao_ativo_usuario_as.setFont(font8)
        self.input_situacao_ativo_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_33.addWidget(self.input_situacao_ativo_usuario_as)

        self.input_situacao_inativo_usuario_as = QRadioButton(self.frame_65)
        self.input_situacao_inativo_usuario_as.setObjectName(u"input_situacao_inativo_usuario_as")
        self.input_situacao_inativo_usuario_as.setMaximumSize(QSize(80, 16777215))
        self.input_situacao_inativo_usuario_as.setFont(font8)
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
        self.frame_66.setMinimumSize(QSize(0, 0))
        self.frame_66.setMaximumSize(QSize(180, 16777215))
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_66)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_cpf_usuario_as = QLabel(self.frame_66)
        self.label_cpf_usuario_as.setObjectName(u"label_cpf_usuario_as")
        self.label_cpf_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_cpf_usuario_as.setMaximumSize(QSize(180, 16777215))
        self.label_cpf_usuario_as.setFont(font)

        self.verticalLayout_33.addWidget(self.label_cpf_usuario_as)

        self.input_cpf_usuario_as = QLineEdit(self.frame_66)
        self.input_cpf_usuario_as.setObjectName(u"input_cpf_usuario_as")
        self.input_cpf_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_cpf_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_cpf_usuario_as.setFont(font)

        self.verticalLayout_33.addWidget(self.input_cpf_usuario_as)


        self.horizontalLayout_34.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.frame_47)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(0, 0))
        self.frame_67.setMaximumSize(QSize(160, 16777215))
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_67)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_rg_usuario_as = QLabel(self.frame_67)
        self.label_rg_usuario_as.setObjectName(u"label_rg_usuario_as")
        self.label_rg_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_rg_usuario_as.setMaximumSize(QSize(160, 16777215))
        self.label_rg_usuario_as.setFont(font)

        self.verticalLayout_40.addWidget(self.label_rg_usuario_as)

        self.input_rg_usuario_as = QLineEdit(self.frame_67)
        self.input_rg_usuario_as.setObjectName(u"input_rg_usuario_as")
        self.input_rg_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_rg_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_rg_usuario_as.setFont(font)

        self.verticalLayout_40.addWidget(self.input_rg_usuario_as)


        self.horizontalLayout_34.addWidget(self.frame_67)

        self.frame_68 = QFrame(self.frame_47)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(0, 0))
        self.frame_68.setMaximumSize(QSize(155, 16777215))
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_68)
        self.verticalLayout_41.setSpacing(5)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_data_emissao_usuario_as = QLabel(self.frame_68)
        self.label_data_emissao_usuario_as.setObjectName(u"label_data_emissao_usuario_as")
        self.label_data_emissao_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_data_emissao_usuario_as.setMaximumSize(QSize(155, 16777215))
        self.label_data_emissao_usuario_as.setFont(font)

        self.verticalLayout_41.addWidget(self.label_data_emissao_usuario_as)

        self.input_data_emissao_usuario_as = QDateEdit(self.frame_68)
        self.input_data_emissao_usuario_as.setObjectName(u"input_data_emissao_usuario_as")
        sizePolicy1.setHeightForWidth(self.input_data_emissao_usuario_as.sizePolicy().hasHeightForWidth())
        self.input_data_emissao_usuario_as.setSizePolicy(sizePolicy1)
        self.input_data_emissao_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_data_emissao_usuario_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_data_emissao_usuario_as.setFont(font8)
        self.input_data_emissao_usuario_as.setFocusPolicy(Qt.WheelFocus)
        self.input_data_emissao_usuario_as.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.input_data_emissao_usuario_as.setLayoutDirection(Qt.LeftToRight)
        self.input_data_emissao_usuario_as.setAutoFillBackground(False)
        self.input_data_emissao_usuario_as.setStyleSheet(u"QDateEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QDateEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_data_emissao_usuario_as.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.input_data_emissao_usuario_as.setAlignment(Qt.AlignCenter)
        self.input_data_emissao_usuario_as.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.input_data_emissao_usuario_as.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.input_data_emissao_usuario_as.setCurrentSection(QDateTimeEdit.DaySection)
        self.input_data_emissao_usuario_as.setCalendarPopup(False)
        self.input_data_emissao_usuario_as.setCurrentSectionIndex(0)

        self.verticalLayout_41.addWidget(self.input_data_emissao_usuario_as, 0, Qt.AlignHCenter)


        self.horizontalLayout_34.addWidget(self.frame_68)

        self.frame_69 = QFrame(self.frame_47)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(0, 0))
        self.frame_69.setMaximumSize(QSize(155, 16777215))
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_69)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_orgao_expedidor_usuario_as = QLabel(self.frame_69)
        self.label_orgao_expedidor_usuario_as.setObjectName(u"label_orgao_expedidor_usuario_as")
        self.label_orgao_expedidor_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_orgao_expedidor_usuario_as.setMaximumSize(QSize(155, 16777215))
        self.label_orgao_expedidor_usuario_as.setFont(font)

        self.verticalLayout_42.addWidget(self.label_orgao_expedidor_usuario_as)

        self.input_orgao_expedidor_usuario_as = QLineEdit(self.frame_69)
        self.input_orgao_expedidor_usuario_as.setObjectName(u"input_orgao_expedidor_usuario_as")
        self.input_orgao_expedidor_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_orgao_expedidor_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_orgao_expedidor_usuario_as.setFont(font)

        self.verticalLayout_42.addWidget(self.input_orgao_expedidor_usuario_as)


        self.horizontalLayout_34.addWidget(self.frame_69)

        self.frame_70 = QFrame(self.frame_47)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(0, 0))
        self.frame_70.setMaximumSize(QSize(170, 16777215))
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_70)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_nis_usuario_as = QLabel(self.frame_70)
        self.label_nis_usuario_as.setObjectName(u"label_nis_usuario_as")
        self.label_nis_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_nis_usuario_as.setMaximumSize(QSize(170, 16777215))
        self.label_nis_usuario_as.setFont(font)

        self.verticalLayout_43.addWidget(self.label_nis_usuario_as)

        self.input_nis_usuario_as = QLineEdit(self.frame_70)
        self.input_nis_usuario_as.setObjectName(u"input_nis_usuario_as")
        self.input_nis_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_nis_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_nis_usuario_as.setFont(font)

        self.verticalLayout_43.addWidget(self.input_nis_usuario_as)


        self.horizontalLayout_34.addWidget(self.frame_70)

        self.frame_71 = QFrame(self.frame_47)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMinimumSize(QSize(0, 0))
        self.frame_71.setMaximumSize(QSize(180, 16777215))
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_71)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_cns_usuario_as = QLabel(self.frame_71)
        self.label_cns_usuario_as.setObjectName(u"label_cns_usuario_as")
        self.label_cns_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_cns_usuario_as.setMaximumSize(QSize(180, 16777215))
        self.label_cns_usuario_as.setFont(font)

        self.verticalLayout_44.addWidget(self.label_cns_usuario_as)

        self.input_cns_usuario_as = QLineEdit(self.frame_71)
        self.input_cns_usuario_as.setObjectName(u"input_cns_usuario_as")
        self.input_cns_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_cns_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_cns_usuario_as.setFont(font)
        self.input_cns_usuario_as.setInputMethodHints(Qt.ImhNone)

        self.verticalLayout_44.addWidget(self.input_cns_usuario_as)


        self.horizontalLayout_34.addWidget(self.frame_71)


        self.verticalLayout_28.addWidget(self.frame_47)

        self.frame_60 = QFrame(self.frame_46)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMaximumSize(QSize(16777215, 60))
        font9 = QFont()
        font9.setPointSize(7)
        self.frame_60.setFont(font9)
        self.frame_60.setStyleSheet(u"")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_41.setSpacing(5)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_72 = QFrame(self.frame_60)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(0, 0))
        self.frame_72.setMaximumSize(QSize(155, 16777215))
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_72)
        self.verticalLayout_45.setSpacing(5)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_sexo_usuario_as = QLabel(self.frame_72)
        self.label_sexo_usuario_as.setObjectName(u"label_sexo_usuario_as")
        self.label_sexo_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_sexo_usuario_as.setMaximumSize(QSize(155, 16777215))
        self.label_sexo_usuario_as.setFont(font)

        self.verticalLayout_45.addWidget(self.label_sexo_usuario_as)

        self.input_sexo_usuario_as = QComboBox(self.frame_72)
        self.input_sexo_usuario_as.addItem("")
        self.input_sexo_usuario_as.addItem("")
        self.input_sexo_usuario_as.addItem("")
        self.input_sexo_usuario_as.setObjectName(u"input_sexo_usuario_as")
        self.input_sexo_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_sexo_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_sexo_usuario_as.setFont(font)

        self.verticalLayout_45.addWidget(self.input_sexo_usuario_as)


        self.horizontalLayout_41.addWidget(self.frame_72)

        self.frame_73 = QFrame(self.frame_60)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(0, 0))
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
        self.label_telefone_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_telefone_usuario_as.setMaximumSize(QSize(155, 16777215))
        self.label_telefone_usuario_as.setFont(font)

        self.verticalLayout_46.addWidget(self.label_telefone_usuario_as)

        self.input_telefone_usuario_as = QLineEdit(self.frame_73)
        self.input_telefone_usuario_as.setObjectName(u"input_telefone_usuario_as")
        self.input_telefone_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_telefone_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_telefone_usuario_as.setFont(font)

        self.verticalLayout_46.addWidget(self.input_telefone_usuario_as)


        self.horizontalLayout_41.addWidget(self.frame_73)

        self.frame_74 = QFrame(self.frame_60)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMinimumSize(QSize(0, 0))
        self.frame_74.setMaximumSize(QSize(240, 16777215))
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_74)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_email_usuario_as = QLabel(self.frame_74)
        self.label_email_usuario_as.setObjectName(u"label_email_usuario_as")
        self.label_email_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_email_usuario_as.setMaximumSize(QSize(240, 16777215))
        self.label_email_usuario_as.setFont(font)

        self.verticalLayout_47.addWidget(self.label_email_usuario_as)

        self.input_email_usuario_as = QLineEdit(self.frame_74)
        self.input_email_usuario_as.setObjectName(u"input_email_usuario_as")
        self.input_email_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_email_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_email_usuario_as.setFont(font)

        self.verticalLayout_47.addWidget(self.input_email_usuario_as)


        self.horizontalLayout_41.addWidget(self.frame_74)

        self.frame_75 = QFrame(self.frame_60)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(0, 0))
        self.frame_75.setMaximumSize(QSize(160, 16777215))
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_75)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.frame_417 = QFrame(self.frame_75)
        self.frame_417.setObjectName(u"frame_417")
        self.frame_417.setMinimumSize(QSize(0, 0))
        self.frame_417.setMaximumSize(QSize(170, 16777215))
        self.frame_417.setFrameShape(QFrame.StyledPanel)
        self.frame_417.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_123 = QHBoxLayout(self.frame_417)
        self.horizontalLayout_123.setSpacing(0)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.frame_418 = QFrame(self.frame_417)
        self.frame_418.setObjectName(u"frame_418")
        self.frame_418.setMinimumSize(QSize(160, 61))
        self.frame_418.setMaximumSize(QSize(150, 61))
        self.frame_418.setFrameShape(QFrame.StyledPanel)
        self.frame_418.setFrameShadow(QFrame.Raised)
        self.verticalLayout_285 = QVBoxLayout(self.frame_418)
        self.verticalLayout_285.setSpacing(0)
        self.verticalLayout_285.setObjectName(u"verticalLayout_285")
        self.verticalLayout_285.setContentsMargins(0, 0, 0, 0)
        self.label_cep_usuario_as = QLabel(self.frame_418)
        self.label_cep_usuario_as.setObjectName(u"label_cep_usuario_as")
        self.label_cep_usuario_as.setMinimumSize(QSize(50, 15))
        self.label_cep_usuario_as.setMaximumSize(QSize(50, 15))
        self.label_cep_usuario_as.setFont(font)

        self.verticalLayout_285.addWidget(self.label_cep_usuario_as)

        self.input_cep_usuario_as = QLineEdit(self.frame_418)
        self.input_cep_usuario_as.setObjectName(u"input_cep_usuario_as")
        self.input_cep_usuario_as.setMinimumSize(QSize(154, 30))
        self.input_cep_usuario_as.setMaximumSize(QSize(145, 16777215))
        self.input_cep_usuario_as.setFont(font)
        self.input_cep_usuario_as.setStyleSheet(u"")
        self.input_cep_usuario_as.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_285.addWidget(self.input_cep_usuario_as)


        self.horizontalLayout_123.addWidget(self.frame_418)

        self.frame_419 = QFrame(self.frame_417)
        self.frame_419.setObjectName(u"frame_419")
        self.frame_419.setMinimumSize(QSize(22, 61))
        self.frame_419.setMaximumSize(QSize(31, 61))
        self.frame_419.setFrameShape(QFrame.StyledPanel)
        self.frame_419.setFrameShadow(QFrame.Raised)
        self.verticalLayout_286 = QVBoxLayout(self.frame_419)
        self.verticalLayout_286.setSpacing(0)
        self.verticalLayout_286.setObjectName(u"verticalLayout_286")
        self.verticalLayout_286.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_17 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_286.addItem(self.verticalSpacer_17)

        self.btn_cep_buscar_usuario_as = QPushButton(self.frame_419)
        self.btn_cep_buscar_usuario_as.setObjectName(u"btn_cep_buscar_usuario_as")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_cep_buscar_usuario_as.sizePolicy().hasHeightForWidth())
        self.btn_cep_buscar_usuario_as.setSizePolicy(sizePolicy2)
        self.btn_cep_buscar_usuario_as.setMinimumSize(QSize(0, 31))
        self.btn_cep_buscar_usuario_as.setMaximumSize(QSize(25, 31))
        self.btn_cep_buscar_usuario_as.setStyleSheet(u"QPushButton{\n"
"        background: rgb(243, 185, 191);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        background: rgb(255, 194, 201);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"        background: rgb(180, 106, 102);\n"
"        border: 2px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/lupa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cep_buscar_usuario_as.setIcon(icon12)

        self.verticalLayout_286.addWidget(self.btn_cep_buscar_usuario_as)


        self.horizontalLayout_123.addWidget(self.frame_419)


        self.verticalLayout_48.addWidget(self.frame_417)


        self.horizontalLayout_41.addWidget(self.frame_75)

        self.frame_128 = QFrame(self.frame_60)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setMinimumSize(QSize(0, 0))
        self.frame_128.setMaximumSize(QSize(360, 16777215))
        self.frame_128.setFrameShape(QFrame.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_128)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.label_logradouro_usuario_as = QLabel(self.frame_128)
        self.label_logradouro_usuario_as.setObjectName(u"label_logradouro_usuario_as")
        self.label_logradouro_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_logradouro_usuario_as.setMaximumSize(QSize(360, 16777215))
        self.label_logradouro_usuario_as.setFont(font)

        self.verticalLayout_87.addWidget(self.label_logradouro_usuario_as)

        self.input_logradouro_usuario_as = QLineEdit(self.frame_128)
        self.input_logradouro_usuario_as.setObjectName(u"input_logradouro_usuario_as")
        self.input_logradouro_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_logradouro_usuario_as.setMaximumSize(QSize(16777215, 30))
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
        self.frame_77.setMinimumSize(QSize(0, 0))
        self.frame_77.setMaximumSize(QSize(170, 16777215))
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_77)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_numero_usuario_as = QLabel(self.frame_77)
        self.label_numero_usuario_as.setObjectName(u"label_numero_usuario_as")
        self.label_numero_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_numero_usuario_as.setMaximumSize(QSize(170, 16777215))
        self.label_numero_usuario_as.setFont(font)

        self.verticalLayout_52.addWidget(self.label_numero_usuario_as)

        self.input_numero_usuario_as = QLineEdit(self.frame_77)
        self.input_numero_usuario_as.setObjectName(u"input_numero_usuario_as")
        self.input_numero_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_numero_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_numero_usuario_as.setFont(font)

        self.verticalLayout_52.addWidget(self.input_numero_usuario_as)


        self.horizontalLayout_42.addWidget(self.frame_77)

        self.frame_80 = QFrame(self.frame_7)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMinimumSize(QSize(0, 0))
        self.frame_80.setMaximumSize(QSize(230, 16777215))
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_80)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_bairro_usuario_as = QLabel(self.frame_80)
        self.label_bairro_usuario_as.setObjectName(u"label_bairro_usuario_as")
        self.label_bairro_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_bairro_usuario_as.setMaximumSize(QSize(230, 16777215))
        self.label_bairro_usuario_as.setFont(font)

        self.verticalLayout_53.addWidget(self.label_bairro_usuario_as)

        self.input_bairro_usuario_as = QLineEdit(self.frame_80)
        self.input_bairro_usuario_as.setObjectName(u"input_bairro_usuario_as")
        self.input_bairro_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_bairro_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_bairro_usuario_as.setFont(font)

        self.verticalLayout_53.addWidget(self.input_bairro_usuario_as)


        self.horizontalLayout_42.addWidget(self.frame_80)

        self.frame_78 = QFrame(self.frame_7)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(0, 0))
        self.frame_78.setMaximumSize(QSize(240, 16777215))
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_78)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_cidade_usuario_as = QLabel(self.frame_78)
        self.label_cidade_usuario_as.setObjectName(u"label_cidade_usuario_as")
        self.label_cidade_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_cidade_usuario_as.setMaximumSize(QSize(240, 16777215))
        self.label_cidade_usuario_as.setFont(font)

        self.verticalLayout_49.addWidget(self.label_cidade_usuario_as)

        self.input_cidade_usuario_as = QLineEdit(self.frame_78)
        self.input_cidade_usuario_as.setObjectName(u"input_cidade_usuario_as")
        self.input_cidade_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_cidade_usuario_as.setMaximumSize(QSize(16777215, 30))
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

        self.input_estado_usuario_as = QLineEdit(self.frame_79)
        self.input_estado_usuario_as.setObjectName(u"input_estado_usuario_as")
        self.input_estado_usuario_as.setMinimumSize(QSize(70, 30))
        self.input_estado_usuario_as.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_50.addWidget(self.input_estado_usuario_as)


        self.horizontalLayout_42.addWidget(self.frame_79)

        self.frame_76 = QFrame(self.frame_7)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(0, 0))
        self.frame_76.setMaximumSize(QSize(210, 16777215))
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_76)
        self.verticalLayout_51.setSpacing(5)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_estado_civil_usuario_as = QLabel(self.frame_76)
        self.label_estado_civil_usuario_as.setObjectName(u"label_estado_civil_usuario_as")
        self.label_estado_civil_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_estado_civil_usuario_as.setMaximumSize(QSize(210, 16777215))
        self.label_estado_civil_usuario_as.setFont(font)

        self.verticalLayout_51.addWidget(self.label_estado_civil_usuario_as)

        self.input_estado_civil_usuario_as = QComboBox(self.frame_76)
        self.input_estado_civil_usuario_as.addItem("")
        self.input_estado_civil_usuario_as.addItem("")
        self.input_estado_civil_usuario_as.addItem("")
        self.input_estado_civil_usuario_as.addItem("")
        self.input_estado_civil_usuario_as.addItem("")
        self.input_estado_civil_usuario_as.addItem("")
        self.input_estado_civil_usuario_as.setObjectName(u"input_estado_civil_usuario_as")
        self.input_estado_civil_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_estado_civil_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_estado_civil_usuario_as.setFont(font)

        self.verticalLayout_51.addWidget(self.input_estado_civil_usuario_as)


        self.horizontalLayout_42.addWidget(self.frame_76)

        self.frame_129 = QFrame(self.frame_7)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setMinimumSize(QSize(0, 0))
        self.frame_129.setMaximumSize(QSize(290, 16777215))
        self.frame_129.setFrameShape(QFrame.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_129)
        self.verticalLayout_64.setSpacing(5)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_escolaridade_usuario_as = QLabel(self.frame_129)
        self.label_escolaridade_usuario_as.setObjectName(u"label_escolaridade_usuario_as")
        self.label_escolaridade_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_escolaridade_usuario_as.setMaximumSize(QSize(290, 16777215))
        self.label_escolaridade_usuario_as.setFont(font)

        self.verticalLayout_64.addWidget(self.label_escolaridade_usuario_as)

        self.input_escolaridade_usuario_comboBox_as = QComboBox(self.frame_129)
        self.input_escolaridade_usuario_comboBox_as.addItem("")
        self.input_escolaridade_usuario_comboBox_as.addItem("")
        self.input_escolaridade_usuario_comboBox_as.addItem("")
        self.input_escolaridade_usuario_comboBox_as.addItem("")
        self.input_escolaridade_usuario_comboBox_as.addItem("")
        self.input_escolaridade_usuario_comboBox_as.addItem("")
        self.input_escolaridade_usuario_comboBox_as.addItem("")
        self.input_escolaridade_usuario_comboBox_as.setObjectName(u"input_escolaridade_usuario_comboBox_as")
        self.input_escolaridade_usuario_comboBox_as.setMinimumSize(QSize(0, 30))
        self.input_escolaridade_usuario_comboBox_as.setMaximumSize(QSize(16777215, 30))
        self.input_escolaridade_usuario_comboBox_as.setFont(font)

        self.verticalLayout_64.addWidget(self.input_escolaridade_usuario_comboBox_as)


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
        self.label_pessoa_cdeficiencia_usuario_as.setMinimumSize(QSize(0, 0))
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
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.input_pessoa_cdeficiencia_sim_usuario_as = QRadioButton(self.frame_130)
        self.input_pessoa_cdeficiencia_sim_usuario_as.setObjectName(u"input_pessoa_cdeficiencia_sim_usuario_as")
        self.input_pessoa_cdeficiencia_sim_usuario_as.setFont(font8)

        self.horizontalLayout_58.addWidget(self.input_pessoa_cdeficiencia_sim_usuario_as)

        self.label_pessoa_cdeficiencia_nao_usuario_as = QRadioButton(self.frame_130)
        self.label_pessoa_cdeficiencia_nao_usuario_as.setObjectName(u"label_pessoa_cdeficiencia_nao_usuario_as")
        self.label_pessoa_cdeficiencia_nao_usuario_as.setFont(font8)

        self.horizontalLayout_58.addWidget(self.label_pessoa_cdeficiencia_nao_usuario_as)


        self.verticalLayout_88.addWidget(self.frame_130)


        self.horizontalLayout_43.addWidget(self.frame_90)

        self.frame_81 = QFrame(self.frame_8)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMinimumSize(QSize(0, 0))
        self.frame_81.setMaximumSize(QSize(260, 16777215))
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_81)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_tipo_deficiencia_usuario_as = QLabel(self.frame_81)
        self.label_tipo_deficiencia_usuario_as.setObjectName(u"label_tipo_deficiencia_usuario_as")
        self.label_tipo_deficiencia_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_tipo_deficiencia_usuario_as.setMaximumSize(QSize(260, 16777215))
        self.label_tipo_deficiencia_usuario_as.setFont(font)

        self.verticalLayout_54.addWidget(self.label_tipo_deficiencia_usuario_as)

        self.input_tipo_deficiencia_usuario_as = QComboBox(self.frame_81)
        self.input_tipo_deficiencia_usuario_as.addItem("")
        self.input_tipo_deficiencia_usuario_as.addItem("")
        self.input_tipo_deficiencia_usuario_as.addItem("")
        self.input_tipo_deficiencia_usuario_as.addItem("")
        self.input_tipo_deficiencia_usuario_as.addItem("")
        self.input_tipo_deficiencia_usuario_as.addItem("")
        self.input_tipo_deficiencia_usuario_as.setObjectName(u"input_tipo_deficiencia_usuario_as")
        self.input_tipo_deficiencia_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_tipo_deficiencia_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_tipo_deficiencia_usuario_as.setFont(font)

        self.verticalLayout_54.addWidget(self.input_tipo_deficiencia_usuario_as)


        self.horizontalLayout_43.addWidget(self.frame_81)

        self.frame_82 = QFrame(self.frame_8)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setMinimumSize(QSize(0, 0))
        self.frame_82.setMaximumSize(QSize(260, 16777215))
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_82)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_renda_familiar_usuario_as = QLabel(self.frame_82)
        self.label_renda_familiar_usuario_as.setObjectName(u"label_renda_familiar_usuario_as")
        self.label_renda_familiar_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_renda_familiar_usuario_as.setMaximumSize(QSize(260, 16777215))
        self.label_renda_familiar_usuario_as.setFont(font)

        self.verticalLayout_55.addWidget(self.label_renda_familiar_usuario_as)

        self.input_renda_familiar_usuario_as = QComboBox(self.frame_82)
        self.input_renda_familiar_usuario_as.addItem("")
        self.input_renda_familiar_usuario_as.addItem("")
        self.input_renda_familiar_usuario_as.addItem("")
        self.input_renda_familiar_usuario_as.addItem("")
        self.input_renda_familiar_usuario_as.addItem("")
        self.input_renda_familiar_usuario_as.setObjectName(u"input_renda_familiar_usuario_as")
        self.input_renda_familiar_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_renda_familiar_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_renda_familiar_usuario_as.setFont(font)
        self.input_renda_familiar_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.input_renda_familiar_usuario_as.setStyleSheet(u"")

        self.verticalLayout_55.addWidget(self.input_renda_familiar_usuario_as)


        self.horizontalLayout_43.addWidget(self.frame_82)

        self.frame_83 = QFrame(self.frame_8)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMinimumSize(QSize(0, 0))
        self.frame_83.setMaximumSize(QSize(200, 16777215))
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_83)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_meio_transporte_usuario_as = QLabel(self.frame_83)
        self.label_meio_transporte_usuario_as.setObjectName(u"label_meio_transporte_usuario_as")
        self.label_meio_transporte_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_meio_transporte_usuario_as.setMaximumSize(QSize(200, 16777215))
        self.label_meio_transporte_usuario_as.setFont(font)

        self.verticalLayout_56.addWidget(self.label_meio_transporte_usuario_as)

        self.input_meio_transporte_usuario_as = QComboBox(self.frame_83)
        self.input_meio_transporte_usuario_as.addItem("")
        self.input_meio_transporte_usuario_as.addItem("")
        self.input_meio_transporte_usuario_as.addItem("")
        self.input_meio_transporte_usuario_as.addItem("")
        self.input_meio_transporte_usuario_as.addItem("")
        self.input_meio_transporte_usuario_as.addItem("")
        self.input_meio_transporte_usuario_as.addItem("")
        self.input_meio_transporte_usuario_as.addItem("")
        self.input_meio_transporte_usuario_as.setObjectName(u"input_meio_transporte_usuario_as")
        self.input_meio_transporte_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_meio_transporte_usuario_as.setMaximumSize(QSize(16777215, 30))
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
        self.input_vale_transporte_usuario_as.addItem("")
        self.input_vale_transporte_usuario_as.addItem("")
        self.input_vale_transporte_usuario_as.addItem("")
        self.input_vale_transporte_usuario_as.addItem("")
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
        self.frame_85.setMinimumSize(QSize(0, 0))
        self.frame_85.setMaximumSize(QSize(260, 16777215))
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_85)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_situacao_trabalho_usuario_as = QLabel(self.frame_85)
        self.label_situacao_trabalho_usuario_as.setObjectName(u"label_situacao_trabalho_usuario_as")
        self.label_situacao_trabalho_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_situacao_trabalho_usuario_as.setMaximumSize(QSize(260, 16777215))
        self.label_situacao_trabalho_usuario_as.setFont(font)

        self.verticalLayout_58.addWidget(self.label_situacao_trabalho_usuario_as)

        self.input_situacao_trabalho_usuario_as = QComboBox(self.frame_85)
        self.input_situacao_trabalho_usuario_as.addItem("")
        self.input_situacao_trabalho_usuario_as.addItem("")
        self.input_situacao_trabalho_usuario_as.addItem("")
        self.input_situacao_trabalho_usuario_as.addItem("")
        self.input_situacao_trabalho_usuario_as.addItem("")
        self.input_situacao_trabalho_usuario_as.addItem("")
        self.input_situacao_trabalho_usuario_as.addItem("")
        self.input_situacao_trabalho_usuario_as.addItem("")
        self.input_situacao_trabalho_usuario_as.addItem("")
        self.input_situacao_trabalho_usuario_as.addItem("")
        self.input_situacao_trabalho_usuario_as.setObjectName(u"input_situacao_trabalho_usuario_as")
        self.input_situacao_trabalho_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_situacao_trabalho_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_situacao_trabalho_usuario_as.setFont(font)
        self.input_situacao_trabalho_usuario_as.setToolTipDuration(-1)

        self.verticalLayout_58.addWidget(self.input_situacao_trabalho_usuario_as)


        self.horizontalLayout_44.addWidget(self.frame_85)

        self.frame_438 = QFrame(self.frame_43)
        self.frame_438.setObjectName(u"frame_438")
        self.frame_438.setEnabled(False)
        self.frame_438.setMinimumSize(QSize(145, 0))
        self.frame_438.setMaximumSize(QSize(145, 16777215))
        self.frame_438.setFrameShape(QFrame.StyledPanel)
        self.frame_438.setFrameShadow(QFrame.Raised)
        self.verticalLayout_305 = QVBoxLayout(self.frame_438)
        self.verticalLayout_305.setSpacing(0)
        self.verticalLayout_305.setObjectName(u"verticalLayout_305")
        self.verticalLayout_305.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_305.addItem(self.verticalSpacer_15)

        self.input_situacao_trabalho_outros_usuario_as = QLineEdit(self.frame_438)
        self.input_situacao_trabalho_outros_usuario_as.setObjectName(u"input_situacao_trabalho_outros_usuario_as")
        self.input_situacao_trabalho_outros_usuario_as.setEnabled(False)
        self.input_situacao_trabalho_outros_usuario_as.setMinimumSize(QSize(140, 0))
        self.input_situacao_trabalho_outros_usuario_as.setMaximumSize(QSize(140, 16777215))
        font10 = QFont()
        font10.setFamilies([u"Abel"])
        self.input_situacao_trabalho_outros_usuario_as.setFont(font10)
        self.input_situacao_trabalho_outros_usuario_as.setStyleSheet(u"    border: none;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"")

        self.verticalLayout_305.addWidget(self.input_situacao_trabalho_outros_usuario_as)


        self.horizontalLayout_44.addWidget(self.frame_438)

        self.frame_91 = QFrame(self.frame_43)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMinimumSize(QSize(0, 0))
        self.frame_91.setMaximumSize(QSize(260, 16777215))
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_91)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_beneficios_usuario_as = QLabel(self.frame_91)
        self.label_beneficios_usuario_as.setObjectName(u"label_beneficios_usuario_as")
        self.label_beneficios_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_beneficios_usuario_as.setMaximumSize(QSize(260, 16777215))
        self.label_beneficios_usuario_as.setFont(font)

        self.verticalLayout_63.addWidget(self.label_beneficios_usuario_as)

        self.input_beneficios_usuario_as = QComboBox(self.frame_91)
        self.input_beneficios_usuario_as.addItem("")
        self.input_beneficios_usuario_as.addItem("")
        self.input_beneficios_usuario_as.addItem("")
        self.input_beneficios_usuario_as.addItem("")
        self.input_beneficios_usuario_as.addItem("")
        self.input_beneficios_usuario_as.setObjectName(u"input_beneficios_usuario_as")
        self.input_beneficios_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_beneficios_usuario_as.setMaximumSize(QSize(16777215, 30))
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
        self.input_tarifa_social_sim_usuario_as.setFont(font8)
        self.input_tarifa_social_sim_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_59.addWidget(self.input_tarifa_social_sim_usuario_as)

        self.input_tarifa_social_nao_usuario_as = QRadioButton(self.frame_87)
        self.input_tarifa_social_nao_usuario_as.setObjectName(u"input_tarifa_social_nao_usuario_as")
        self.input_tarifa_social_nao_usuario_as.setFont(font8)
        self.input_tarifa_social_nao_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_59.addWidget(self.input_tarifa_social_nao_usuario_as)


        self.verticalLayout_65.addWidget(self.frame_87)


        self.horizontalLayout_44.addWidget(self.frame_89)

        self.frame_86 = QFrame(self.frame_43)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(0, 0))
        self.frame_86.setMaximumSize(QSize(260, 16777215))
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_86)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_tipo_tratamento_usuario_as = QLabel(self.frame_86)
        self.label_tipo_tratamento_usuario_as.setObjectName(u"label_tipo_tratamento_usuario_as")
        self.label_tipo_tratamento_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_tipo_tratamento_usuario_as.setMaximumSize(QSize(260, 16777215))
        self.label_tipo_tratamento_usuario_as.setFont(font)

        self.verticalLayout_59.addWidget(self.label_tipo_tratamento_usuario_as)

        self.input_tipo_tratamento_usuario_as = QComboBox(self.frame_86)
        self.input_tipo_tratamento_usuario_as.addItem("")
        self.input_tipo_tratamento_usuario_as.addItem("")
        self.input_tipo_tratamento_usuario_as.addItem("")
        self.input_tipo_tratamento_usuario_as.addItem("")
        self.input_tipo_tratamento_usuario_as.setObjectName(u"input_tipo_tratamento_usuario_as")
        self.input_tipo_tratamento_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_tipo_tratamento_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_tipo_tratamento_usuario_as.setFont(font)
        self.input_tipo_tratamento_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.input_tipo_tratamento_usuario_as.setStyleSheet(u"")

        self.verticalLayout_59.addWidget(self.input_tipo_tratamento_usuario_as)


        self.horizontalLayout_44.addWidget(self.frame_86)

        self.horizontalSpacer_72 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_72)


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
        self.frame_88 = QFrame(self.frame_44)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(0, 0))
        self.frame_88.setMaximumSize(QSize(330, 16777215))
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_88)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.label_local_tratamento_usuario_as = QLabel(self.frame_88)
        self.label_local_tratamento_usuario_as.setObjectName(u"label_local_tratamento_usuario_as")
        self.label_local_tratamento_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_local_tratamento_usuario_as.setMaximumSize(QSize(330, 16777215))
        self.label_local_tratamento_usuario_as.setFont(font)

        self.verticalLayout_60.addWidget(self.label_local_tratamento_usuario_as)

        self.input_local_tratamento_usuario_as = QLineEdit(self.frame_88)
        self.input_local_tratamento_usuario_as.setObjectName(u"input_local_tratamento_usuario_as")
        self.input_local_tratamento_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_local_tratamento_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_local_tratamento_usuario_as.setFont(font)

        self.verticalLayout_60.addWidget(self.input_local_tratamento_usuario_as)


        self.horizontalLayout_45.addWidget(self.frame_88)

        self.frame_92 = QFrame(self.frame_44)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(0, 0))
        self.frame_92.setMaximumSize(QSize(260, 16777215))
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_92)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.label_patologia_base_usuario_as = QLabel(self.frame_92)
        self.label_patologia_base_usuario_as.setObjectName(u"label_patologia_base_usuario_as")
        self.label_patologia_base_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_patologia_base_usuario_as.setMaximumSize(QSize(260, 16777215))
        self.label_patologia_base_usuario_as.setFont(font)

        self.verticalLayout_61.addWidget(self.label_patologia_base_usuario_as)

        self.input_patologia_base_usuario_as = QComboBox(self.frame_92)
        self.input_patologia_base_usuario_as.addItem("")
        self.input_patologia_base_usuario_as.addItem("")
        self.input_patologia_base_usuario_as.addItem("")
        self.input_patologia_base_usuario_as.addItem("")
        self.input_patologia_base_usuario_as.addItem("")
        self.input_patologia_base_usuario_as.addItem("")
        self.input_patologia_base_usuario_as.addItem("")
        self.input_patologia_base_usuario_as.setObjectName(u"input_patologia_base_usuario_as")
        self.input_patologia_base_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_patologia_base_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_patologia_base_usuario_as.setFont(font)
        self.input_patologia_base_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_61.addWidget(self.input_patologia_base_usuario_as)


        self.horizontalLayout_45.addWidget(self.frame_92)

        self.frame_132 = QFrame(self.frame_44)
        self.frame_132.setObjectName(u"frame_132")
        self.frame_132.setMinimumSize(QSize(0, 0))
        self.frame_132.setMaximumSize(QSize(160, 16777215))
        self.frame_132.setFrameShape(QFrame.StyledPanel)
        self.frame_132.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_132)
        self.verticalLayout_62.setSpacing(5)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_data_inicio_usuario_as = QLabel(self.frame_132)
        self.label_data_inicio_usuario_as.setObjectName(u"label_data_inicio_usuario_as")
        self.label_data_inicio_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_data_inicio_usuario_as.setMaximumSize(QSize(160, 16777215))
        self.label_data_inicio_usuario_as.setFont(font)

        self.verticalLayout_62.addWidget(self.label_data_inicio_usuario_as, 0, Qt.AlignHCenter)

        self.input_data_inicio_usuario_as = QDateEdit(self.frame_132)
        self.input_data_inicio_usuario_as.setObjectName(u"input_data_inicio_usuario_as")
        sizePolicy1.setHeightForWidth(self.input_data_inicio_usuario_as.sizePolicy().hasHeightForWidth())
        self.input_data_inicio_usuario_as.setSizePolicy(sizePolicy1)
        self.input_data_inicio_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_data_inicio_usuario_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_data_inicio_usuario_as.setFont(font8)
        self.input_data_inicio_usuario_as.setFocusPolicy(Qt.WheelFocus)
        self.input_data_inicio_usuario_as.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.input_data_inicio_usuario_as.setLayoutDirection(Qt.LeftToRight)
        self.input_data_inicio_usuario_as.setAutoFillBackground(False)
        self.input_data_inicio_usuario_as.setStyleSheet(u"QDateEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QDateEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_data_inicio_usuario_as.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.input_data_inicio_usuario_as.setAlignment(Qt.AlignCenter)
        self.input_data_inicio_usuario_as.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.input_data_inicio_usuario_as.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.input_data_inicio_usuario_as.setCurrentSection(QDateTimeEdit.DaySection)
        self.input_data_inicio_usuario_as.setCalendarPopup(False)
        self.input_data_inicio_usuario_as.setCurrentSectionIndex(0)

        self.verticalLayout_62.addWidget(self.input_data_inicio_usuario_as, 0, Qt.AlignHCenter)


        self.horizontalLayout_45.addWidget(self.frame_132)

        self.frame_131 = QFrame(self.frame_44)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setMinimumSize(QSize(0, 0))
        self.frame_131.setMaximumSize(QSize(250, 16777215))
        self.frame_131.setFrameShape(QFrame.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.frame_131)
        self.verticalLayout_89.setSpacing(5)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.label_periodo_usuario_as = QLabel(self.frame_131)
        self.label_periodo_usuario_as.setObjectName(u"label_periodo_usuario_as")
        self.label_periodo_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_periodo_usuario_as.setMaximumSize(QSize(250, 16777215))
        self.label_periodo_usuario_as.setFont(font)

        self.verticalLayout_89.addWidget(self.label_periodo_usuario_as)

        self.input_periodo_usuario_as = QComboBox(self.frame_131)
        self.input_periodo_usuario_as.addItem("")
        self.input_periodo_usuario_as.addItem("")
        self.input_periodo_usuario_as.addItem("")
        self.input_periodo_usuario_as.addItem("")
        self.input_periodo_usuario_as.setObjectName(u"input_periodo_usuario_as")
        self.input_periodo_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_periodo_usuario_as.setMaximumSize(QSize(16777215, 30))
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
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, 0, 0)
        self.btn_voltar_usuario_as = QPushButton(self.frame_4)
        self.btn_voltar_usuario_as.setObjectName(u"btn_voltar_usuario_as")
        self.btn_voltar_usuario_as.setMinimumSize(QSize(100, 40))
        self.btn_voltar_usuario_as.setMaximumSize(QSize(100, 40))
        font11 = QFont()
        font11.setFamilies([u"Abel"])
        font11.setPointSize(18)
        self.btn_voltar_usuario_as.setFont(font11)
        self.btn_voltar_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_usuario_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout.addWidget(self.btn_voltar_usuario_as)

        self.horizontalSpacer_5 = QSpacerItem(1687, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.btn_observacoes_sigilo_as = QPushButton(self.frame_4)
        self.btn_observacoes_sigilo_as.setObjectName(u"btn_observacoes_sigilo_as")
        self.btn_observacoes_sigilo_as.setMinimumSize(QSize(0, 40))
        self.btn_observacoes_sigilo_as.setFont(font11)
        self.btn_observacoes_sigilo_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_observacoes_sigilo_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        icon13 = QIcon()
        icon13.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/cadeado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_observacoes_sigilo_as.setIcon(icon13)
        self.btn_observacoes_sigilo_as.setIconSize(QSize(28, 28))

        self.horizontalLayout.addWidget(self.btn_observacoes_sigilo_as)

        self.btn_salvar_usuario_as = QPushButton(self.frame_4)
        self.btn_salvar_usuario_as.setObjectName(u"btn_salvar_usuario_as")
        self.btn_salvar_usuario_as.setMinimumSize(QSize(140, 40))
        self.btn_salvar_usuario_as.setFont(font11)
        self.btn_salvar_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar_usuario_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout.addWidget(self.btn_salvar_usuario_as)

        self.btn_proximo_as = QPushButton(self.frame_4)
        self.btn_proximo_as.setObjectName(u"btn_proximo_as")
        self.btn_proximo_as.setMinimumSize(QSize(140, 40))
        self.btn_proximo_as.setFont(font11)
        self.btn_proximo_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_proximo_as.setLayoutDirection(Qt.RightToLeft)
        self.btn_proximo_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

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
        sizePolicy.setHeightForWidth(self.frame_101.sizePolicy().hasHeightForWidth())
        self.frame_101.setSizePolicy(sizePolicy)
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
        self.frame_94.setMinimumSize(QSize(0, 0))
        self.frame_94.setMaximumSize(QSize(110, 16777215))
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_94)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.label_matricula_cuidador_as = QLabel(self.frame_94)
        self.label_matricula_cuidador_as.setObjectName(u"label_matricula_cuidador_as")
        self.label_matricula_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_matricula_cuidador_as.setMaximumSize(QSize(160, 16777215))
        self.label_matricula_cuidador_as.setFont(font)

        self.verticalLayout_90.addWidget(self.label_matricula_cuidador_as)

        self.input_matricula_cuidador_as = QLineEdit(self.frame_94)
        self.input_matricula_cuidador_as.setObjectName(u"input_matricula_cuidador_as")
        self.input_matricula_cuidador_as.setEnabled(False)
        self.input_matricula_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_matricula_cuidador_as.setMaximumSize(QSize(110, 30))
        self.input_matricula_cuidador_as.setFont(font)

        self.verticalLayout_90.addWidget(self.input_matricula_cuidador_as)


        self.horizontalLayout_49.addWidget(self.frame_94)

        self.frame_105 = QFrame(self.frame_101)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setMinimumSize(QSize(0, 0))
        self.frame_105.setMaximumSize(QSize(360, 16777215))
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_105)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.label_nome_cuidador_as = QLabel(self.frame_105)
        self.label_nome_cuidador_as.setObjectName(u"label_nome_cuidador_as")
        self.label_nome_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_nome_cuidador_as.setMaximumSize(QSize(460, 16777215))
        self.label_nome_cuidador_as.setFont(font)

        self.verticalLayout_69.addWidget(self.label_nome_cuidador_as)

        self.input_nome_cuidador_as = QLineEdit(self.frame_105)
        self.input_nome_cuidador_as.setObjectName(u"input_nome_cuidador_as")
        self.input_nome_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_nome_cuidador_as.setMaximumSize(QSize(360, 30))
        self.input_nome_cuidador_as.setFont(font)

        self.verticalLayout_69.addWidget(self.input_nome_cuidador_as)


        self.horizontalLayout_49.addWidget(self.frame_105)

        self.frame_232 = QFrame(self.frame_101)
        self.frame_232.setObjectName(u"frame_232")
        self.frame_232.setMaximumSize(QSize(155, 16777215))
        self.frame_232.setFrameShape(QFrame.StyledPanel)
        self.frame_232.setFrameShadow(QFrame.Raised)
        self.verticalLayout_146 = QVBoxLayout(self.frame_232)
        self.verticalLayout_146.setSpacing(0)
        self.verticalLayout_146.setObjectName(u"verticalLayout_146")
        self.verticalLayout_146.setContentsMargins(12, 0, 12, 0)
        self.label_data_nascimento_cuidador_as = QLabel(self.frame_232)
        self.label_data_nascimento_cuidador_as.setObjectName(u"label_data_nascimento_cuidador_as")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_data_nascimento_cuidador_as.sizePolicy().hasHeightForWidth())
        self.label_data_nascimento_cuidador_as.setSizePolicy(sizePolicy3)
        self.label_data_nascimento_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_data_nascimento_cuidador_as.setMaximumSize(QSize(155, 16777215))
        self.label_data_nascimento_cuidador_as.setFont(font)
        self.label_data_nascimento_cuidador_as.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_146.addWidget(self.label_data_nascimento_cuidador_as)

        self.input_data_nascimento_cuidador_as = QDateEdit(self.frame_232)
        self.input_data_nascimento_cuidador_as.setObjectName(u"input_data_nascimento_cuidador_as")
        sizePolicy1.setHeightForWidth(self.input_data_nascimento_cuidador_as.sizePolicy().hasHeightForWidth())
        self.input_data_nascimento_cuidador_as.setSizePolicy(sizePolicy1)
        self.input_data_nascimento_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_data_nascimento_cuidador_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_data_nascimento_cuidador_as.setFont(font8)
        self.input_data_nascimento_cuidador_as.setFocusPolicy(Qt.WheelFocus)
        self.input_data_nascimento_cuidador_as.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.input_data_nascimento_cuidador_as.setLayoutDirection(Qt.LeftToRight)
        self.input_data_nascimento_cuidador_as.setAutoFillBackground(False)
        self.input_data_nascimento_cuidador_as.setStyleSheet(u"QDateEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QDateEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_data_nascimento_cuidador_as.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.input_data_nascimento_cuidador_as.setAlignment(Qt.AlignCenter)
        self.input_data_nascimento_cuidador_as.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.input_data_nascimento_cuidador_as.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.input_data_nascimento_cuidador_as.setCurrentSection(QDateTimeEdit.DaySection)
        self.input_data_nascimento_cuidador_as.setCalendarPopup(False)
        self.input_data_nascimento_cuidador_as.setCurrentSectionIndex(0)

        self.verticalLayout_146.addWidget(self.input_data_nascimento_cuidador_as)


        self.horizontalLayout_49.addWidget(self.frame_232)

        self.frame_106 = QFrame(self.frame_101)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMinimumSize(QSize(0, 0))
        self.frame_106.setMaximumSize(QSize(180, 16777215))
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_106)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.label_cpf_cuidador_as = QLabel(self.frame_106)
        self.label_cpf_cuidador_as.setObjectName(u"label_cpf_cuidador_as")
        self.label_cpf_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_cpf_cuidador_as.setMaximumSize(QSize(180, 16777215))
        self.label_cpf_cuidador_as.setFont(font)

        self.verticalLayout_70.addWidget(self.label_cpf_cuidador_as)

        self.input_cpf_cuidador_as = QLineEdit(self.frame_106)
        self.input_cpf_cuidador_as.setObjectName(u"input_cpf_cuidador_as")
        self.input_cpf_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_cpf_cuidador_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_cpf_cuidador_as.setFont(font)

        self.verticalLayout_70.addWidget(self.input_cpf_cuidador_as)


        self.horizontalLayout_49.addWidget(self.frame_106)

        self.frame_107 = QFrame(self.frame_101)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setMinimumSize(QSize(0, 0))
        self.frame_107.setMaximumSize(QSize(160, 16777215))
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_107)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.label_rg_cuidador_as = QLabel(self.frame_107)
        self.label_rg_cuidador_as.setObjectName(u"label_rg_cuidador_as")
        self.label_rg_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_rg_cuidador_as.setMaximumSize(QSize(160, 16777215))
        self.label_rg_cuidador_as.setFont(font)

        self.verticalLayout_71.addWidget(self.label_rg_cuidador_as)

        self.input_rg_cuidador_as = QLineEdit(self.frame_107)
        self.input_rg_cuidador_as.setObjectName(u"input_rg_cuidador_as")
        self.input_rg_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_rg_cuidador_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_rg_cuidador_as.setFont(font)

        self.verticalLayout_71.addWidget(self.input_rg_cuidador_as)


        self.horizontalLayout_49.addWidget(self.frame_107)

        self.frame_108 = QFrame(self.frame_101)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setMinimumSize(QSize(0, 0))
        self.frame_108.setMaximumSize(QSize(155, 16777215))
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_108)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(15, 0, 15, 0)
        self.label_data_emissao_cuidador_as = QLabel(self.frame_108)
        self.label_data_emissao_cuidador_as.setObjectName(u"label_data_emissao_cuidador_as")
        self.label_data_emissao_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_data_emissao_cuidador_as.setMaximumSize(QSize(155, 16777215))
        self.label_data_emissao_cuidador_as.setFont(font)
        self.label_data_emissao_cuidador_as.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_72.addWidget(self.label_data_emissao_cuidador_as, 0, Qt.AlignHCenter)

        self.input_data_emissao_cuidador_as = QDateEdit(self.frame_108)
        self.input_data_emissao_cuidador_as.setObjectName(u"input_data_emissao_cuidador_as")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.input_data_emissao_cuidador_as.sizePolicy().hasHeightForWidth())
        self.input_data_emissao_cuidador_as.setSizePolicy(sizePolicy4)
        self.input_data_emissao_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_data_emissao_cuidador_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_data_emissao_cuidador_as.setFont(font8)
        self.input_data_emissao_cuidador_as.setFocusPolicy(Qt.WheelFocus)
        self.input_data_emissao_cuidador_as.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.input_data_emissao_cuidador_as.setLayoutDirection(Qt.LeftToRight)
        self.input_data_emissao_cuidador_as.setAutoFillBackground(False)
        self.input_data_emissao_cuidador_as.setStyleSheet(u"QDateEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QDateEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_data_emissao_cuidador_as.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.input_data_emissao_cuidador_as.setAlignment(Qt.AlignCenter)
        self.input_data_emissao_cuidador_as.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.input_data_emissao_cuidador_as.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.input_data_emissao_cuidador_as.setCurrentSection(QDateTimeEdit.DaySection)
        self.input_data_emissao_cuidador_as.setCalendarPopup(False)
        self.input_data_emissao_cuidador_as.setCurrentSectionIndex(0)

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
        self.frame_109.setMinimumSize(QSize(80, 0))
        self.frame_109.setMaximumSize(QSize(125, 16777215))
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_109)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.label_orgao_expedidor_cuidador_as = QLabel(self.frame_109)
        self.label_orgao_expedidor_cuidador_as.setObjectName(u"label_orgao_expedidor_cuidador_as")
        self.label_orgao_expedidor_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_orgao_expedidor_cuidador_as.setMaximumSize(QSize(155, 16777215))
        self.label_orgao_expedidor_cuidador_as.setFont(font)

        self.verticalLayout_73.addWidget(self.label_orgao_expedidor_cuidador_as)

        self.input_orgao_expedidor_cuidador_as = QLineEdit(self.frame_109)
        self.input_orgao_expedidor_cuidador_as.setObjectName(u"input_orgao_expedidor_cuidador_as")
        self.input_orgao_expedidor_cuidador_as.setMaximumSize(QSize(120, 30))
        self.input_orgao_expedidor_cuidador_as.setFont(font)

        self.verticalLayout_73.addWidget(self.input_orgao_expedidor_cuidador_as)


        self.horizontalLayout_50.addWidget(self.frame_109)

        self.frame_95 = QFrame(self.frame_102)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMinimumSize(QSize(120, 0))
        self.frame_95.setMaximumSize(QSize(120, 16777215))
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

        self.input_sexo_cuidador_as = QComboBox(self.frame_95)
        self.input_sexo_cuidador_as.addItem("")
        self.input_sexo_cuidador_as.addItem("")
        self.input_sexo_cuidador_as.addItem("")
        self.input_sexo_cuidador_as.setObjectName(u"input_sexo_cuidador_as")
        self.input_sexo_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_sexo_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_sexo_cuidador_as.setFont(font)

        self.verticalLayout_91.addWidget(self.input_sexo_cuidador_as)


        self.horizontalLayout_50.addWidget(self.frame_95)

        self.frame_237 = QFrame(self.frame_102)
        self.frame_237.setObjectName(u"frame_237")
        self.frame_237.setMinimumSize(QSize(190, 0))
        self.frame_237.setMaximumSize(QSize(330, 16777215))
        self.frame_237.setFrameShape(QFrame.StyledPanel)
        self.frame_237.setFrameShadow(QFrame.Raised)
        self.verticalLayout_160 = QVBoxLayout(self.frame_237)
        self.verticalLayout_160.setSpacing(0)
        self.verticalLayout_160.setObjectName(u"verticalLayout_160")
        self.verticalLayout_160.setContentsMargins(0, 0, 0, 0)
        self.label_usuario_cuidador_as = QLabel(self.frame_237)
        self.label_usuario_cuidador_as.setObjectName(u"label_usuario_cuidador_as")
        self.label_usuario_cuidador_as.setFont(font)

        self.verticalLayout_160.addWidget(self.label_usuario_cuidador_as)

        self.input_usuario_cuidador_as = QComboBox(self.frame_237)
        self.input_usuario_cuidador_as.addItem("")
        self.input_usuario_cuidador_as.addItem("")
        self.input_usuario_cuidador_as.addItem("")
        self.input_usuario_cuidador_as.setObjectName(u"input_usuario_cuidador_as")
        self.input_usuario_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_usuario_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_usuario_cuidador_as.setFont(font)

        self.verticalLayout_160.addWidget(self.input_usuario_cuidador_as)


        self.horizontalLayout_50.addWidget(self.frame_237)

        self.frame_96 = QFrame(self.frame_102)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMinimumSize(QSize(155, 0))
        self.frame_96.setMaximumSize(QSize(160, 16777215))
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
        self.input_parentesco_cuidador_as.setMinimumSize(QSize(0, 0))
        self.input_parentesco_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_parentesco_cuidador_as.setFont(font)

        self.verticalLayout_92.addWidget(self.input_parentesco_cuidador_as)


        self.horizontalLayout_50.addWidget(self.frame_96)

        self.frame_110 = QFrame(self.frame_102)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setMinimumSize(QSize(0, 0))
        self.frame_110.setMaximumSize(QSize(155, 16777215))
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_110)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.label_telefone_cuidador_as = QLabel(self.frame_110)
        self.label_telefone_cuidador_as.setObjectName(u"label_telefone_cuidador_as")
        self.label_telefone_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_telefone_cuidador_as.setMaximumSize(QSize(155, 16777215))
        self.label_telefone_cuidador_as.setFont(font)

        self.verticalLayout_74.addWidget(self.label_telefone_cuidador_as)

        self.input_telefone_cuidador_as = QLineEdit(self.frame_110)
        self.input_telefone_cuidador_as.setObjectName(u"input_telefone_cuidador_as")
        self.input_telefone_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_telefone_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_telefone_cuidador_as.setFont(font)

        self.verticalLayout_74.addWidget(self.input_telefone_cuidador_as)


        self.horizontalLayout_50.addWidget(self.frame_110)

        self.frame_111 = QFrame(self.frame_102)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setMinimumSize(QSize(0, 0))
        self.frame_111.setMaximumSize(QSize(240, 16777215))
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_111)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.label_email_cuidador_as = QLabel(self.frame_111)
        self.label_email_cuidador_as.setObjectName(u"label_email_cuidador_as")
        self.label_email_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_email_cuidador_as.setMaximumSize(QSize(240, 16777215))
        self.label_email_cuidador_as.setFont(font)

        self.verticalLayout_75.addWidget(self.label_email_cuidador_as)

        self.input_email_cuidador_as = QLineEdit(self.frame_111)
        self.input_email_cuidador_as.setObjectName(u"input_email_cuidador_as")
        self.input_email_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_email_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_email_cuidador_as.setFont(font)

        self.verticalLayout_75.addWidget(self.input_email_cuidador_as)


        self.horizontalLayout_50.addWidget(self.frame_111)


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
        self.frame_112 = QFrame(self.frame_103)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setMaximumSize(QSize(130, 16777215))
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_122 = QHBoxLayout(self.frame_112)
        self.horizontalLayout_122.setSpacing(0)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.horizontalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.frame_415 = QFrame(self.frame_112)
        self.frame_415.setObjectName(u"frame_415")
        self.frame_415.setMinimumSize(QSize(160, 61))
        self.frame_415.setMaximumSize(QSize(150, 61))
        self.frame_415.setFrameShape(QFrame.StyledPanel)
        self.frame_415.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_415)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.label_cep_cuidador_as = QLabel(self.frame_415)
        self.label_cep_cuidador_as.setObjectName(u"label_cep_cuidador_as")
        self.label_cep_cuidador_as.setMinimumSize(QSize(50, 15))
        self.label_cep_cuidador_as.setMaximumSize(QSize(50, 15))
        self.label_cep_cuidador_as.setFont(font)

        self.verticalLayout_76.addWidget(self.label_cep_cuidador_as)

        self.input_cep_cuidador_as = QLineEdit(self.frame_415)
        self.input_cep_cuidador_as.setObjectName(u"input_cep_cuidador_as")
        self.input_cep_cuidador_as.setMinimumSize(QSize(120, 30))
        self.input_cep_cuidador_as.setMaximumSize(QSize(120, 16777215))
        self.input_cep_cuidador_as.setFont(font)
        self.input_cep_cuidador_as.setStyleSheet(u"")
        self.input_cep_cuidador_as.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_76.addWidget(self.input_cep_cuidador_as)


        self.horizontalLayout_122.addWidget(self.frame_415)

        self.frame_416 = QFrame(self.frame_112)
        self.frame_416.setObjectName(u"frame_416")
        self.frame_416.setMinimumSize(QSize(22, 61))
        self.frame_416.setMaximumSize(QSize(31, 61))
        self.frame_416.setFrameShape(QFrame.StyledPanel)
        self.frame_416.setFrameShadow(QFrame.Raised)
        self.verticalLayout_284 = QVBoxLayout(self.frame_416)
        self.verticalLayout_284.setSpacing(0)
        self.verticalLayout_284.setObjectName(u"verticalLayout_284")
        self.verticalLayout_284.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_16 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_284.addItem(self.verticalSpacer_16)

        self.btn_cep_buscar_cuidador_as = QPushButton(self.frame_416)
        self.btn_cep_buscar_cuidador_as.setObjectName(u"btn_cep_buscar_cuidador_as")
        sizePolicy2.setHeightForWidth(self.btn_cep_buscar_cuidador_as.sizePolicy().hasHeightForWidth())
        self.btn_cep_buscar_cuidador_as.setSizePolicy(sizePolicy2)
        self.btn_cep_buscar_cuidador_as.setMinimumSize(QSize(0, 31))
        self.btn_cep_buscar_cuidador_as.setMaximumSize(QSize(25, 31))
        self.btn_cep_buscar_cuidador_as.setStyleSheet(u"QPushButton{\n"
"        background: rgb(243, 185, 191);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        background: rgb(255, 194, 201);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"        background: rgb(180, 106, 102);\n"
"        border: 2px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}")
        self.btn_cep_buscar_cuidador_as.setIcon(icon12)

        self.verticalLayout_284.addWidget(self.btn_cep_buscar_cuidador_as)


        self.horizontalLayout_122.addWidget(self.frame_416)


        self.horizontalLayout_51.addWidget(self.frame_112)

        self.frame_113 = QFrame(self.frame_103)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setMinimumSize(QSize(0, 0))
        self.frame_113.setMaximumSize(QSize(305, 16777215))
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_113)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.label_logradouro_cuidador_as = QLabel(self.frame_113)
        self.label_logradouro_cuidador_as.setObjectName(u"label_logradouro_cuidador_as")
        self.label_logradouro_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_logradouro_cuidador_as.setMaximumSize(QSize(360, 16777215))
        self.label_logradouro_cuidador_as.setFont(font)

        self.verticalLayout_77.addWidget(self.label_logradouro_cuidador_as)

        self.input_logradouro_cuidador_as = QLineEdit(self.frame_113)
        self.input_logradouro_cuidador_as.setObjectName(u"input_logradouro_cuidador_as")
        self.input_logradouro_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_logradouro_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_logradouro_cuidador_as.setFont(font)

        self.verticalLayout_77.addWidget(self.input_logradouro_cuidador_as)


        self.horizontalLayout_51.addWidget(self.frame_113)

        self.frame_133 = QFrame(self.frame_103)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setMinimumSize(QSize(0, 0))
        self.frame_133.setMaximumSize(QSize(125, 16777215))
        self.frame_133.setFrameShape(QFrame.StyledPanel)
        self.frame_133.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.frame_133)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.label_numero_cuidador_as = QLabel(self.frame_133)
        self.label_numero_cuidador_as.setObjectName(u"label_numero_cuidador_as")
        self.label_numero_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_numero_cuidador_as.setMaximumSize(QSize(160, 16777215))
        self.label_numero_cuidador_as.setFont(font)

        self.verticalLayout_93.addWidget(self.label_numero_cuidador_as)

        self.input_numero_cuidador_as = QLineEdit(self.frame_133)
        self.input_numero_cuidador_as.setObjectName(u"input_numero_cuidador_as")
        sizePolicy4.setHeightForWidth(self.input_numero_cuidador_as.sizePolicy().hasHeightForWidth())
        self.input_numero_cuidador_as.setSizePolicy(sizePolicy4)
        self.input_numero_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_numero_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_numero_cuidador_as.setFont(font)

        self.verticalLayout_93.addWidget(self.input_numero_cuidador_as)


        self.horizontalLayout_51.addWidget(self.frame_133)

        self.frame_135 = QFrame(self.frame_103)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setMinimumSize(QSize(0, 0))
        self.frame_135.setMaximumSize(QSize(250, 16777215))
        self.frame_135.setFrameShape(QFrame.StyledPanel)
        self.frame_135.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_135)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.label_bairro_cuidador_as = QLabel(self.frame_135)
        self.label_bairro_cuidador_as.setObjectName(u"label_bairro_cuidador_as")
        self.label_bairro_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_bairro_cuidador_as.setMaximumSize(QSize(230, 16777215))
        self.label_bairro_cuidador_as.setFont(font)

        self.verticalLayout_94.addWidget(self.label_bairro_cuidador_as)

        self.input_bairro_cuidador_as = QLineEdit(self.frame_135)
        self.input_bairro_cuidador_as.setObjectName(u"input_bairro_cuidador_as")
        self.input_bairro_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_bairro_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_bairro_cuidador_as.setFont(font)

        self.verticalLayout_94.addWidget(self.input_bairro_cuidador_as)


        self.horizontalLayout_51.addWidget(self.frame_135)

        self.frame_114 = QFrame(self.frame_103)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setMinimumSize(QSize(0, 0))
        self.frame_114.setMaximumSize(QSize(240, 16777215))
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_114)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.label_cidade_cuidador_as = QLabel(self.frame_114)
        self.label_cidade_cuidador_as.setObjectName(u"label_cidade_cuidador_as")
        self.label_cidade_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_cidade_cuidador_as.setMaximumSize(QSize(240, 16777215))
        self.label_cidade_cuidador_as.setFont(font)

        self.verticalLayout_78.addWidget(self.label_cidade_cuidador_as)

        self.input_cidade_cuidador_as = QLineEdit(self.frame_114)
        self.input_cidade_cuidador_as.setObjectName(u"input_cidade_cuidador_as")
        self.input_cidade_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_cidade_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_cidade_cuidador_as.setFont(font)

        self.verticalLayout_78.addWidget(self.input_cidade_cuidador_as)


        self.horizontalLayout_51.addWidget(self.frame_114)

        self.frame_115 = QFrame(self.frame_103)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setMinimumSize(QSize(0, 0))
        self.frame_115.setMaximumSize(QSize(80, 16777215))
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_115)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.label_estado_cuidador_as = QLabel(self.frame_115)
        self.label_estado_cuidador_as.setObjectName(u"label_estado_cuidador_as")
        self.label_estado_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_estado_cuidador_as.setMaximumSize(QSize(80, 16777215))
        self.label_estado_cuidador_as.setFont(font)

        self.verticalLayout_79.addWidget(self.label_estado_cuidador_as)

        self.input_estado_cuidador_as = QLineEdit(self.frame_115)
        self.input_estado_cuidador_as.setObjectName(u"input_estado_cuidador_as")
        self.input_estado_cuidador_as.setMinimumSize(QSize(70, 30))
        self.input_estado_cuidador_as.setMaximumSize(QSize(16777215, 30))
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
        self.verticalLayout_68.setContentsMargins(17, 0, 0, 0)
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
        self.horizontalLayout_48.setContentsMargins(20, 0, 0, 0)
        self.btn_voltar_cuidador_as = QPushButton(self.frame_99)
        self.btn_voltar_cuidador_as.setObjectName(u"btn_voltar_cuidador_as")
        self.btn_voltar_cuidador_as.setMinimumSize(QSize(100, 40))
        self.btn_voltar_cuidador_as.setMaximumSize(QSize(100, 40))
        self.btn_voltar_cuidador_as.setFont(font11)
        self.btn_voltar_cuidador_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_cuidador_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout_48.addWidget(self.btn_voltar_cuidador_as)

        self.horizontalSpacer_8 = QSpacerItem(1770, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_8)

        self.btn_finalizar_as = QPushButton(self.frame_99)
        self.btn_finalizar_as.setObjectName(u"btn_finalizar_as")
        self.btn_finalizar_as.setMinimumSize(QSize(120, 40))
        self.btn_finalizar_as.setFont(font11)
        self.btn_finalizar_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_finalizar_as.setLayoutDirection(Qt.RightToLeft)
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
        self.verticalLayout_3051 = QVBoxLayout(self.frame_120)
        self.verticalLayout_3051.setSpacing(0)
        self.verticalLayout_3051.setObjectName(u"verticalLayout_3051")
        self.verticalLayout_3051.setContentsMargins(0, 0, 0, 0)
        self.frame_423 = QFrame(self.frame_120)
        self.frame_423.setObjectName(u"frame_423")
        self.frame_423.setMinimumSize(QSize(0, 50))
        self.frame_423.setMaximumSize(QSize(160, 50))
        self.frame_423.setStyleSheet(u"background-color: #EC848C; border-radius: 10px")
        self.frame_423.setFrameShape(QFrame.StyledPanel)
        self.frame_423.setFrameShadow(QFrame.Raised)
        self.verticalLayout_290 = QVBoxLayout(self.frame_423)
        self.verticalLayout_290.setSpacing(6)
        self.verticalLayout_290.setObjectName(u"verticalLayout_290")
        self.verticalLayout_290.setContentsMargins(15, 0, 0, 0)
        self.label_obito_paciente_as = QLabel(self.frame_423)
        self.label_obito_paciente_as.setObjectName(u"label_obito_paciente_as")
        self.label_obito_paciente_as.setMaximumSize(QSize(130, 16777215))
        self.label_obito_paciente_as.setFont(font)

        self.verticalLayout_290.addWidget(self.label_obito_paciente_as)

        self.frame_425 = QFrame(self.frame_423)
        self.frame_425.setObjectName(u"frame_425")
        self.frame_425.setFrameShape(QFrame.StyledPanel)
        self.frame_425.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_126 = QHBoxLayout(self.frame_425)
        self.horizontalLayout_126.setSpacing(0)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.input_obito_paciente_sim_as = QRadioButton(self.frame_425)
        self.input_obito_paciente_sim_as.setObjectName(u"input_obito_paciente_sim_as")
        self.input_obito_paciente_sim_as.setMaximumSize(QSize(80, 16777215))
        self.input_obito_paciente_sim_as.setFont(font8)
        self.input_obito_paciente_sim_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_126.addWidget(self.input_obito_paciente_sim_as)

        self.input_obito_paciente_nao_as = QRadioButton(self.frame_425)
        self.input_obito_paciente_nao_as.setObjectName(u"input_obito_paciente_nao_as")
        self.input_obito_paciente_nao_as.setMaximumSize(QSize(80, 16777215))
        self.input_obito_paciente_nao_as.setFont(font8)
        self.input_obito_paciente_nao_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_126.addWidget(self.input_obito_paciente_nao_as)


        self.verticalLayout_290.addWidget(self.frame_425)


        self.verticalLayout_3051.addWidget(self.frame_423)

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


        self.verticalLayout_3051.addWidget(self.frame_123)

        self.frame_437 = QFrame(self.frame_120)
        self.frame_437.setObjectName(u"frame_437")
        self.frame_437.setMaximumSize(QSize(16777215, 450))
        self.frame_437.setFrameShape(QFrame.StyledPanel)
        self.frame_437.setFrameShadow(QFrame.Raised)
        self.verticalLayout_291 = QVBoxLayout(self.frame_437)
        self.verticalLayout_291.setSpacing(0)
        self.verticalLayout_291.setObjectName(u"verticalLayout_291")
        self.verticalLayout_291.setContentsMargins(0, 0, 0, 0)
        self.label_tabela_de_observacoes_obs_sigilosas_as = QLabel(self.frame_437)
        self.label_tabela_de_observacoes_obs_sigilosas_as.setObjectName(u"label_tabela_de_observacoes_obs_sigilosas_as")
        self.label_tabela_de_observacoes_obs_sigilosas_as.setMaximumSize(QSize(300, 50))
        self.label_tabela_de_observacoes_obs_sigilosas_as.setFont(font)

        self.verticalLayout_291.addWidget(self.label_tabela_de_observacoes_obs_sigilosas_as)

        self.input_TableWidget_observacoes_sigilosas_as = QTableWidget(self.frame_437)
        if (self.input_TableWidget_observacoes_sigilosas_as.columnCount() < 2):
            self.input_TableWidget_observacoes_sigilosas_as.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.input_TableWidget_observacoes_sigilosas_as.rowCount() < 14):
            self.input_TableWidget_observacoes_sigilosas_as.setRowCount(14)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setVerticalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setVerticalHeaderItem(10, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setVerticalHeaderItem(11, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setVerticalHeaderItem(12, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setVerticalHeaderItem(13, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setItem(0, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setItem(0, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.input_TableWidget_observacoes_sigilosas_as.setItem(1, 0, __qtablewidgetitem18)
        self.input_TableWidget_observacoes_sigilosas_as.setObjectName(u"input_TableWidget_observacoes_sigilosas_as")
        self.input_TableWidget_observacoes_sigilosas_as.setFont(font)
        self.input_TableWidget_observacoes_sigilosas_as.setLayoutDirection(Qt.LeftToRight)
        self.input_TableWidget_observacoes_sigilosas_as.setAutoFillBackground(False)
        self.input_TableWidget_observacoes_sigilosas_as.setInputMethodHints(Qt.ImhDate|Qt.ImhSensitiveData|Qt.ImhTime)
        self.input_TableWidget_observacoes_sigilosas_as.setLineWidth(2222)
        self.input_TableWidget_observacoes_sigilosas_as.setMidLineWidth(10)
        self.input_TableWidget_observacoes_sigilosas_as.setAlternatingRowColors(True)
        self.input_TableWidget_observacoes_sigilosas_as.setSelectionMode(QAbstractItemView.MultiSelection)
        self.input_TableWidget_observacoes_sigilosas_as.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.input_TableWidget_observacoes_sigilosas_as.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.input_TableWidget_observacoes_sigilosas_as.setGridStyle(Qt.SolidLine)
        self.input_TableWidget_observacoes_sigilosas_as.setSortingEnabled(True)
        self.input_TableWidget_observacoes_sigilosas_as.setWordWrap(True)
        self.input_TableWidget_observacoes_sigilosas_as.horizontalHeader().setCascadingSectionResizes(True)
        self.input_TableWidget_observacoes_sigilosas_as.horizontalHeader().setDefaultSectionSize(130)
        self.input_TableWidget_observacoes_sigilosas_as.horizontalHeader().setStretchLastSection(True)
        self.input_TableWidget_observacoes_sigilosas_as.verticalHeader().setVisible(False)
        self.input_TableWidget_observacoes_sigilosas_as.verticalHeader().setDefaultSectionSize(50)

        self.verticalLayout_291.addWidget(self.input_TableWidget_observacoes_sigilosas_as)


        self.verticalLayout_3051.addWidget(self.frame_437)


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
        self.horizontalLayout_54.setContentsMargins(20, 0, 0, 0)
        self.btn_voltar_observacoes_sigilosas_as = QPushButton(self.frame_119)
        self.btn_voltar_observacoes_sigilosas_as.setObjectName(u"btn_voltar_observacoes_sigilosas_as")
        self.btn_voltar_observacoes_sigilosas_as.setMinimumSize(QSize(100, 40))
        self.btn_voltar_observacoes_sigilosas_as.setMaximumSize(QSize(100, 40))
        self.btn_voltar_observacoes_sigilosas_as.setFont(font11)
        self.btn_voltar_observacoes_sigilosas_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_observacoes_sigilosas_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout_54.addWidget(self.btn_voltar_observacoes_sigilosas_as)

        self.btn_alterar_observacoes_sigilosas_as = QPushButton(self.frame_119)
        self.btn_alterar_observacoes_sigilosas_as.setObjectName(u"btn_alterar_observacoes_sigilosas_as")
        self.btn_alterar_observacoes_sigilosas_as.setMinimumSize(QSize(0, 40))
        self.btn_alterar_observacoes_sigilosas_as.setFont(font11)
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
        self.btn_cancelar_observacoes_sigilosas_as.setFont(font11)
        self.btn_cancelar_observacoes_sigilosas_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar_observacoes_sigilosas_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        icon14 = QIcon()
        icon14.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/cancelar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancelar_observacoes_sigilosas_as.setIcon(icon14)
        self.btn_cancelar_observacoes_sigilosas_as.setIconSize(QSize(28, 28))

        self.horizontalLayout_54.addWidget(self.btn_cancelar_observacoes_sigilosas_as)

        self.btn_salvar_observacoes_sigilosas_as = QPushButton(self.frame_119)
        self.btn_salvar_observacoes_sigilosas_as.setObjectName(u"btn_salvar_observacoes_sigilosas_as")
        self.btn_salvar_observacoes_sigilosas_as.setMinimumSize(QSize(0, 40))
        self.btn_salvar_observacoes_sigilosas_as.setFont(font11)
        self.btn_salvar_observacoes_sigilosas_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar_observacoes_sigilosas_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em;}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        icon15 = QIcon()
        icon15.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/salvar-arquivo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salvar_observacoes_sigilosas_as.setIcon(icon15)
        self.btn_salvar_observacoes_sigilosas_as.setIconSize(QSize(28, 28))

        self.horizontalLayout_54.addWidget(self.btn_salvar_observacoes_sigilosas_as)

        self.btn_excluir_observacoes_sigilosas_as = QPushButton(self.frame_119)
        self.btn_excluir_observacoes_sigilosas_as.setObjectName(u"btn_excluir_observacoes_sigilosas_as")
        self.btn_excluir_observacoes_sigilosas_as.setMinimumSize(QSize(0, 40))
        self.btn_excluir_observacoes_sigilosas_as.setFont(font11)
        self.btn_excluir_observacoes_sigilosas_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_observacoes_sigilosas_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        icon16 = QIcon()
        icon16.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/lixeira-de-reciclagem.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.frame_192 = QFrame(self.page_cadastro_colaborador_as)
        self.frame_192.setObjectName(u"frame_192")
        sizePolicy.setHeightForWidth(self.frame_192.sizePolicy().hasHeightForWidth())
        self.frame_192.setSizePolicy(sizePolicy)
        self.frame_192.setMinimumSize(QSize(1826, 92))
        self.frame_192.setMaximumSize(QSize(16777215, 92))
        self.frame_192.setStyleSheet(u"background-color: #F3B9BF; ")
        self.frame_192.setFrameShape(QFrame.StyledPanel)
        self.frame_192.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_192)
        self.horizontalLayout_76.setSpacing(0)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.label_cadastro_colaborador_as = QLabel(self.frame_192)
        self.label_cadastro_colaborador_as.setObjectName(u"label_cadastro_colaborador_as")
        self.label_cadastro_colaborador_as.setMinimumSize(QSize(1800, 90))
        self.label_cadastro_colaborador_as.setMaximumSize(QSize(16777215, 90))
        self.label_cadastro_colaborador_as.setFont(font1)
        self.label_cadastro_colaborador_as.setStyleSheet(u"color: #EC848C;")
        self.label_cadastro_colaborador_as.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_76.addWidget(self.label_cadastro_colaborador_as)


        self.verticalLayout_83.addWidget(self.frame_192)

        self.frame_193 = QFrame(self.page_cadastro_colaborador_as)
        self.frame_193.setObjectName(u"frame_193")
        sizePolicy.setHeightForWidth(self.frame_193.sizePolicy().hasHeightForWidth())
        self.frame_193.setSizePolicy(sizePolicy)
        self.frame_193.setFrameShape(QFrame.StyledPanel)
        self.frame_193.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_193)
        self.horizontalLayout_77.setSpacing(0)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.frame_194 = QFrame(self.frame_193)
        self.frame_194.setObjectName(u"frame_194")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_194.sizePolicy().hasHeightForWidth())
        self.frame_194.setSizePolicy(sizePolicy5)
        self.frame_194.setMinimumSize(QSize(360, 0))
        self.frame_194.setMaximumSize(QSize(16777215, 360))
        self.frame_194.setStyleSheet(u"QLabel{margin-left: 0.25em}")
        self.frame_194.setFrameShape(QFrame.StyledPanel)
        self.frame_194.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_194)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_51 = QSpacerItem(123, 55, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_51, 4, 0, 1, 1)

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
        self.input_situacao_ativo_colaborador_as.setFont(font8)
        self.input_situacao_ativo_colaborador_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_90.addWidget(self.input_situacao_ativo_colaborador_as)

        self.input_situacao_inativo_colaborador_as = QRadioButton(self.frame_262)
        self.input_situacao_inativo_colaborador_as.setObjectName(u"input_situacao_inativo_colaborador_as")
        self.input_situacao_inativo_colaborador_as.setMaximumSize(QSize(80, 16777215))
        self.input_situacao_inativo_colaborador_as.setFont(font8)
        self.input_situacao_inativo_colaborador_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_90.addWidget(self.input_situacao_inativo_colaborador_as)


        self.verticalLayout_180.addWidget(self.frame_262)


        self.verticalLayout_181.addWidget(self.frame_261)


        self.gridLayout_2.addWidget(self.frame_260, 0, 2, 1, 1)

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
        self.frame_196.setMinimumSize(QSize(0, 0))
        self.frame_196.setMaximumSize(QSize(160, 16777215))
        self.frame_196.setFrameShape(QFrame.StyledPanel)
        self.frame_196.setFrameShadow(QFrame.Raised)
        self.verticalLayout_136 = QVBoxLayout(self.frame_196)
        self.verticalLayout_136.setSpacing(0)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.verticalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.label_matricula_colaborador_as = QLabel(self.frame_196)
        self.label_matricula_colaborador_as.setObjectName(u"label_matricula_colaborador_as")
        self.label_matricula_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_matricula_colaborador_as.setMaximumSize(QSize(160, 16777215))
        self.label_matricula_colaborador_as.setFont(font)

        self.verticalLayout_136.addWidget(self.label_matricula_colaborador_as)

        self.input_matricula_colaborador_as = QLineEdit(self.frame_196)
        self.input_matricula_colaborador_as.setObjectName(u"input_matricula_colaborador_as")
        self.input_matricula_colaborador_as.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.input_matricula_colaborador_as.sizePolicy().hasHeightForWidth())
        self.input_matricula_colaborador_as.setSizePolicy(sizePolicy4)
        self.input_matricula_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_matricula_colaborador_as.setMaximumSize(QSize(110, 30))
        self.input_matricula_colaborador_as.setFont(font)

        self.verticalLayout_136.addWidget(self.input_matricula_colaborador_as)


        self.horizontalLayout_78.addWidget(self.frame_196)

        self.frame_197 = QFrame(self.frame_195)
        self.frame_197.setObjectName(u"frame_197")
        self.frame_197.setMinimumSize(QSize(0, 0))
        self.frame_197.setMaximumSize(QSize(431, 16777215))
        self.frame_197.setFrameShape(QFrame.StyledPanel)
        self.frame_197.setFrameShadow(QFrame.Raised)
        self.verticalLayout_137 = QVBoxLayout(self.frame_197)
        self.verticalLayout_137.setSpacing(0)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.verticalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.label_nome_colaborador_as = QLabel(self.frame_197)
        self.label_nome_colaborador_as.setObjectName(u"label_nome_colaborador_as")
        self.label_nome_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_nome_colaborador_as.setMaximumSize(QSize(460, 16777215))
        self.label_nome_colaborador_as.setFont(font)

        self.verticalLayout_137.addWidget(self.label_nome_colaborador_as)

        self.input_nome_colaborador_as = QLineEdit(self.frame_197)
        self.input_nome_colaborador_as.setObjectName(u"input_nome_colaborador_as")
        self.input_nome_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_nome_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_nome_colaborador_as.setFont(font)

        self.verticalLayout_137.addWidget(self.input_nome_colaborador_as)


        self.horizontalLayout_78.addWidget(self.frame_197)

        self.frame_200 = QFrame(self.frame_195)
        self.frame_200.setObjectName(u"frame_200")
        self.frame_200.setMinimumSize(QSize(0, 0))
        self.frame_200.setMaximumSize(QSize(155, 16777215))
        self.frame_200.setFrameShape(QFrame.StyledPanel)
        self.frame_200.setFrameShadow(QFrame.Raised)
        self.verticalLayout_140 = QVBoxLayout(self.frame_200)
        self.verticalLayout_140.setSpacing(0)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.verticalLayout_140.setContentsMargins(0, 0, 0, 0)
        self.label_data_nascimento_colaborador_as = QLabel(self.frame_200)
        self.label_data_nascimento_colaborador_as.setObjectName(u"label_data_nascimento_colaborador_as")
        self.label_data_nascimento_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_data_nascimento_colaborador_as.setMaximumSize(QSize(155, 16777215))
        self.label_data_nascimento_colaborador_as.setFont(font)

        self.verticalLayout_140.addWidget(self.label_data_nascimento_colaborador_as)

        self.input_data_nascimento_colaborador_as = QDateEdit(self.frame_200)
        self.input_data_nascimento_colaborador_as.setObjectName(u"input_data_nascimento_colaborador_as")
        sizePolicy1.setHeightForWidth(self.input_data_nascimento_colaborador_as.sizePolicy().hasHeightForWidth())
        self.input_data_nascimento_colaborador_as.setSizePolicy(sizePolicy1)
        self.input_data_nascimento_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_data_nascimento_colaborador_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_data_nascimento_colaborador_as.setFont(font8)
        self.input_data_nascimento_colaborador_as.setFocusPolicy(Qt.WheelFocus)
        self.input_data_nascimento_colaborador_as.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.input_data_nascimento_colaborador_as.setLayoutDirection(Qt.LeftToRight)
        self.input_data_nascimento_colaborador_as.setAutoFillBackground(False)
        self.input_data_nascimento_colaborador_as.setStyleSheet(u"QDateEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QDateEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_data_nascimento_colaborador_as.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.input_data_nascimento_colaborador_as.setAlignment(Qt.AlignCenter)
        self.input_data_nascimento_colaborador_as.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.input_data_nascimento_colaborador_as.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.input_data_nascimento_colaborador_as.setCurrentSection(QDateTimeEdit.DaySection)
        self.input_data_nascimento_colaborador_as.setCalendarPopup(False)
        self.input_data_nascimento_colaborador_as.setCurrentSectionIndex(0)

        self.verticalLayout_140.addWidget(self.input_data_nascimento_colaborador_as, 0, Qt.AlignHCenter)


        self.horizontalLayout_78.addWidget(self.frame_200)

        self.frame_198 = QFrame(self.frame_195)
        self.frame_198.setObjectName(u"frame_198")
        self.frame_198.setMinimumSize(QSize(0, 0))
        self.frame_198.setMaximumSize(QSize(180, 16777215))
        self.frame_198.setFrameShape(QFrame.StyledPanel)
        self.frame_198.setFrameShadow(QFrame.Raised)
        self.verticalLayout_138 = QVBoxLayout(self.frame_198)
        self.verticalLayout_138.setSpacing(0)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.verticalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.label_cpf_colaborador_as = QLabel(self.frame_198)
        self.label_cpf_colaborador_as.setObjectName(u"label_cpf_colaborador_as")
        self.label_cpf_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_cpf_colaborador_as.setMaximumSize(QSize(180, 16777215))
        self.label_cpf_colaborador_as.setFont(font)

        self.verticalLayout_138.addWidget(self.label_cpf_colaborador_as)

        self.input_cpf_colaborador_as = QLineEdit(self.frame_198)
        self.input_cpf_colaborador_as.setObjectName(u"input_cpf_colaborador_as")
        self.input_cpf_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_cpf_colaborador_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_cpf_colaborador_as.setFont(font)

        self.verticalLayout_138.addWidget(self.input_cpf_colaborador_as)


        self.horizontalLayout_78.addWidget(self.frame_198)

        self.frame_199 = QFrame(self.frame_195)
        self.frame_199.setObjectName(u"frame_199")
        self.frame_199.setMinimumSize(QSize(0, 0))
        self.frame_199.setMaximumSize(QSize(160, 16777215))
        self.frame_199.setFrameShape(QFrame.StyledPanel)
        self.frame_199.setFrameShadow(QFrame.Raised)
        self.verticalLayout_139 = QVBoxLayout(self.frame_199)
        self.verticalLayout_139.setSpacing(0)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.verticalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.label_rg_colaborador_as = QLabel(self.frame_199)
        self.label_rg_colaborador_as.setObjectName(u"label_rg_colaborador_as")
        self.label_rg_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_rg_colaborador_as.setMaximumSize(QSize(160, 16777215))
        self.label_rg_colaborador_as.setFont(font)

        self.verticalLayout_139.addWidget(self.label_rg_colaborador_as)

        self.input_rg_colaborador_as = QLineEdit(self.frame_199)
        self.input_rg_colaborador_as.setObjectName(u"input_rg_colaborador_as")
        self.input_rg_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_rg_colaborador_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_rg_colaborador_as.setFont(font)

        self.verticalLayout_139.addWidget(self.input_rg_colaborador_as)


        self.horizontalLayout_78.addWidget(self.frame_199)


        self.gridLayout_2.addWidget(self.frame_195, 0, 1, 1, 1)

        self.frame_208 = QFrame(self.frame_194)
        self.frame_208.setObjectName(u"frame_208")
        self.frame_208.setMinimumSize(QSize(0, 50))
        self.frame_208.setMaximumSize(QSize(16777215, 65))
        self.frame_208.setStyleSheet(u"")
        self.frame_208.setFrameShape(QFrame.StyledPanel)
        self.frame_208.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_208)
        self.horizontalLayout_89.setSpacing(5)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.frame_240 = QFrame(self.frame_208)
        self.frame_240.setObjectName(u"frame_240")
        self.frame_240.setMinimumSize(QSize(0, 0))
        self.frame_240.setMaximumSize(QSize(151, 16777215))
        self.frame_240.setFrameShape(QFrame.StyledPanel)
        self.frame_240.setFrameShadow(QFrame.Raised)
        self.verticalLayout_288 = QVBoxLayout(self.frame_240)
        self.verticalLayout_288.setSpacing(0)
        self.verticalLayout_288.setObjectName(u"verticalLayout_288")
        self.verticalLayout_288.setContentsMargins(0, 0, 0, 0)
        self.frame_420 = QFrame(self.frame_240)
        self.frame_420.setObjectName(u"frame_420")
        self.frame_420.setMaximumSize(QSize(170, 16777215))
        self.frame_420.setFrameShape(QFrame.StyledPanel)
        self.frame_420.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_124 = QHBoxLayout(self.frame_420)
        self.horizontalLayout_124.setSpacing(0)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.frame_421 = QFrame(self.frame_420)
        self.frame_421.setObjectName(u"frame_421")
        self.frame_421.setMinimumSize(QSize(160, 62))
        self.frame_421.setMaximumSize(QSize(150, 62))
        self.frame_421.setFrameShape(QFrame.StyledPanel)
        self.frame_421.setFrameShadow(QFrame.Raised)
        self.verticalLayout_147 = QVBoxLayout(self.frame_421)
        self.verticalLayout_147.setSpacing(2)
        self.verticalLayout_147.setObjectName(u"verticalLayout_147")
        self.verticalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.label_cep_colaborador_as = QLabel(self.frame_421)
        self.label_cep_colaborador_as.setObjectName(u"label_cep_colaborador_as")
        self.label_cep_colaborador_as.setMinimumSize(QSize(50, 15))
        self.label_cep_colaborador_as.setMaximumSize(QSize(50, 24))
        self.label_cep_colaborador_as.setFont(font)

        self.verticalLayout_147.addWidget(self.label_cep_colaborador_as)

        self.input_cep_colaborador_as = QLineEdit(self.frame_421)
        self.input_cep_colaborador_as.setObjectName(u"input_cep_colaborador_as")
        self.input_cep_colaborador_as.setMinimumSize(QSize(145, 30))
        self.input_cep_colaborador_as.setMaximumSize(QSize(146, 30))
        self.input_cep_colaborador_as.setFont(font)
        self.input_cep_colaborador_as.setStyleSheet(u"")
        self.input_cep_colaborador_as.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_147.addWidget(self.input_cep_colaborador_as)


        self.horizontalLayout_124.addWidget(self.frame_421)

        self.frame_422 = QFrame(self.frame_420)
        self.frame_422.setObjectName(u"frame_422")
        self.frame_422.setMinimumSize(QSize(22, 61))
        self.frame_422.setMaximumSize(QSize(31, 61))
        self.frame_422.setFrameShape(QFrame.StyledPanel)
        self.frame_422.setFrameShadow(QFrame.Raised)
        self.verticalLayout_287 = QVBoxLayout(self.frame_422)
        self.verticalLayout_287.setSpacing(0)
        self.verticalLayout_287.setObjectName(u"verticalLayout_287")
        self.verticalLayout_287.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_18 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_287.addItem(self.verticalSpacer_18)

        self.btn_cep_buscar_colaborador_as = QPushButton(self.frame_422)
        self.btn_cep_buscar_colaborador_as.setObjectName(u"btn_cep_buscar_colaborador_as")
        sizePolicy2.setHeightForWidth(self.btn_cep_buscar_colaborador_as.sizePolicy().hasHeightForWidth())
        self.btn_cep_buscar_colaborador_as.setSizePolicy(sizePolicy2)
        self.btn_cep_buscar_colaborador_as.setMinimumSize(QSize(0, 30))
        self.btn_cep_buscar_colaborador_as.setMaximumSize(QSize(25, 30))
        self.btn_cep_buscar_colaborador_as.setStyleSheet(u"QPushButton{\n"
"        background: rgb(243, 185, 191);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        background: rgb(255, 194, 201);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"        background: rgb(180, 106, 102);\n"
"        border: 2px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}")
        self.btn_cep_buscar_colaborador_as.setIcon(icon12)

        self.verticalLayout_287.addWidget(self.btn_cep_buscar_colaborador_as)


        self.horizontalLayout_124.addWidget(self.frame_422)


        self.verticalLayout_288.addWidget(self.frame_420)


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
        self.label_logradouro_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_logradouro_colaborador_as.setMaximumSize(QSize(280, 16777215))
        self.label_logradouro_colaborador_as.setFont(font)

        self.verticalLayout_174.addWidget(self.label_logradouro_colaborador_as)

        self.input_logradouro_colaborador_as = QLineEdit(self.frame_209)
        self.input_logradouro_colaborador_as.setObjectName(u"input_logradouro_colaborador_as")
        self.input_logradouro_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_logradouro_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_logradouro_colaborador_as.setFont(font)

        self.verticalLayout_174.addWidget(self.input_logradouro_colaborador_as)


        self.horizontalLayout_89.addWidget(self.frame_209)

        self.frame_210 = QFrame(self.frame_208)
        self.frame_210.setObjectName(u"frame_210")
        self.frame_210.setMinimumSize(QSize(0, 0))
        self.frame_210.setMaximumSize(QSize(120, 16777215))
        self.frame_210.setFrameShape(QFrame.StyledPanel)
        self.frame_210.setFrameShadow(QFrame.Raised)
        self.verticalLayout_173 = QVBoxLayout(self.frame_210)
        self.verticalLayout_173.setSpacing(0)
        self.verticalLayout_173.setObjectName(u"verticalLayout_173")
        self.verticalLayout_173.setContentsMargins(0, 0, 0, 0)
        self.label_numero_colaborador_as = QLabel(self.frame_210)
        self.label_numero_colaborador_as.setObjectName(u"label_numero_colaborador_as")
        self.label_numero_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_numero_colaborador_as.setMaximumSize(QSize(60, 16777215))
        self.label_numero_colaborador_as.setFont(font)

        self.verticalLayout_173.addWidget(self.label_numero_colaborador_as)

        self.input_numero_colaborador_as = QLineEdit(self.frame_210)
        self.input_numero_colaborador_as.setObjectName(u"input_numero_colaborador_as")
        self.input_numero_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_numero_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_numero_colaborador_as.setFont(font)

        self.verticalLayout_173.addWidget(self.input_numero_colaborador_as)


        self.horizontalLayout_89.addWidget(self.frame_210)

        self.frame_211 = QFrame(self.frame_208)
        self.frame_211.setObjectName(u"frame_211")
        self.frame_211.setMinimumSize(QSize(0, 0))
        self.frame_211.setMaximumSize(QSize(230, 16777215))
        self.frame_211.setFrameShape(QFrame.StyledPanel)
        self.frame_211.setFrameShadow(QFrame.Raised)
        self.verticalLayout_149 = QVBoxLayout(self.frame_211)
        self.verticalLayout_149.setSpacing(0)
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.verticalLayout_149.setContentsMargins(0, 0, 0, 0)
        self.label_bairro_colaborador_as = QLabel(self.frame_211)
        self.label_bairro_colaborador_as.setObjectName(u"label_bairro_colaborador_as")
        self.label_bairro_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_bairro_colaborador_as.setMaximumSize(QSize(230, 16777215))
        self.label_bairro_colaborador_as.setFont(font)

        self.verticalLayout_149.addWidget(self.label_bairro_colaborador_as)

        self.input_bairro_colaborador_as = QLineEdit(self.frame_211)
        self.input_bairro_colaborador_as.setObjectName(u"input_bairro_colaborador_as")
        self.input_bairro_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_bairro_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_bairro_colaborador_as.setFont(font)

        self.verticalLayout_149.addWidget(self.input_bairro_colaborador_as)


        self.horizontalLayout_89.addWidget(self.frame_211)

        self.frame_212 = QFrame(self.frame_208)
        self.frame_212.setObjectName(u"frame_212")
        self.frame_212.setMinimumSize(QSize(0, 0))
        self.frame_212.setMaximumSize(QSize(180, 16777215))
        self.frame_212.setFrameShape(QFrame.StyledPanel)
        self.frame_212.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_212)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_cidade_colaborador_as = QLabel(self.frame_212)
        self.label_cidade_colaborador_as.setObjectName(u"label_cidade_colaborador_as")
        self.label_cidade_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_cidade_colaborador_as.setMaximumSize(QSize(180, 16777215))
        self.label_cidade_colaborador_as.setFont(font)

        self.verticalLayout_2.addWidget(self.label_cidade_colaborador_as)

        self.input_cidade_colaborador_as = QLineEdit(self.frame_212)
        self.input_cidade_colaborador_as.setObjectName(u"input_cidade_colaborador_as")
        self.input_cidade_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_cidade_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_cidade_colaborador_as.setFont(font)

        self.verticalLayout_2.addWidget(self.input_cidade_colaborador_as)


        self.horizontalLayout_89.addWidget(self.frame_212)

        self.frame_213 = QFrame(self.frame_208)
        self.frame_213.setObjectName(u"frame_213")
        self.frame_213.setMinimumSize(QSize(0, 0))
        self.frame_213.setMaximumSize(QSize(80, 16777215))
        self.frame_213.setFrameShape(QFrame.StyledPanel)
        self.frame_213.setFrameShadow(QFrame.Raised)
        self.verticalLayout_148 = QVBoxLayout(self.frame_213)
        self.verticalLayout_148.setSpacing(0)
        self.verticalLayout_148.setObjectName(u"verticalLayout_148")
        self.verticalLayout_148.setContentsMargins(0, 0, 0, 0)
        self.label_estado_colaborador_as = QLabel(self.frame_213)
        self.label_estado_colaborador_as.setObjectName(u"label_estado_colaborador_as")
        self.label_estado_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_estado_colaborador_as.setMaximumSize(QSize(80, 16777215))
        self.label_estado_colaborador_as.setFont(font)

        self.verticalLayout_148.addWidget(self.label_estado_colaborador_as)

        self.input_estado_colaborador_as = QLineEdit(self.frame_213)
        self.input_estado_colaborador_as.setObjectName(u"input_estado_colaborador_as")
        self.input_estado_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_estado_colaborador_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_estado_colaborador_as.setFont(font)

        self.verticalLayout_148.addWidget(self.input_estado_colaborador_as)


        self.horizontalLayout_89.addWidget(self.frame_213)


        self.gridLayout_2.addWidget(self.frame_208, 2, 1, 1, 1)

        self.horizontalSpacer_52 = QSpacerItem(194, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_52, 4, 2, 1, 1)

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
        self.frame_202.setMinimumSize(QSize(0, 0))
        self.frame_202.setMaximumSize(QSize(155, 16777215))
        self.frame_202.setFrameShape(QFrame.StyledPanel)
        self.frame_202.setFrameShadow(QFrame.Raised)
        self.verticalLayout_141 = QVBoxLayout(self.frame_202)
        self.verticalLayout_141.setSpacing(0)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.verticalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.label_orgao_expedidor_colaborador_as = QLabel(self.frame_202)
        self.label_orgao_expedidor_colaborador_as.setObjectName(u"label_orgao_expedidor_colaborador_as")
        self.label_orgao_expedidor_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_orgao_expedidor_colaborador_as.setMaximumSize(QSize(155, 16777215))
        self.label_orgao_expedidor_colaborador_as.setFont(font)

        self.verticalLayout_141.addWidget(self.label_orgao_expedidor_colaborador_as)

        self.input_orgao_expedidor_colaborador_as = QLineEdit(self.frame_202)
        self.input_orgao_expedidor_colaborador_as.setObjectName(u"input_orgao_expedidor_colaborador_as")
        self.input_orgao_expedidor_colaborador_as.setMinimumSize(QSize(0, 0))
        self.input_orgao_expedidor_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_orgao_expedidor_colaborador_as.setFont(font)

        self.verticalLayout_141.addWidget(self.input_orgao_expedidor_colaborador_as)


        self.horizontalLayout_79.addWidget(self.frame_202)

        self.frame_207 = QFrame(self.frame_201)
        self.frame_207.setObjectName(u"frame_207")
        self.frame_207.setMaximumSize(QSize(151, 16777215))
        self.frame_207.setFrameShape(QFrame.StyledPanel)
        self.frame_207.setFrameShadow(QFrame.Raised)
        self.verticalLayout_111 = QVBoxLayout(self.frame_207)
        self.verticalLayout_111.setSpacing(0)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(9, 0, 9, 0)
        self.label_data_emissao_rg_colaborador_as = QLabel(self.frame_207)
        self.label_data_emissao_rg_colaborador_as.setObjectName(u"label_data_emissao_rg_colaborador_as")
        self.label_data_emissao_rg_colaborador_as.setMaximumSize(QSize(170, 16777215))
        self.label_data_emissao_rg_colaborador_as.setFont(font)

        self.verticalLayout_111.addWidget(self.label_data_emissao_rg_colaborador_as)

        self.input_data_emissao_rg_colaborador_as = QDateEdit(self.frame_207)
        self.input_data_emissao_rg_colaborador_as.setObjectName(u"input_data_emissao_rg_colaborador_as")
        sizePolicy1.setHeightForWidth(self.input_data_emissao_rg_colaborador_as.sizePolicy().hasHeightForWidth())
        self.input_data_emissao_rg_colaborador_as.setSizePolicy(sizePolicy1)
        self.input_data_emissao_rg_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_data_emissao_rg_colaborador_as.setMaximumSize(QSize(150, 16777215))
        self.input_data_emissao_rg_colaborador_as.setFont(font8)
        self.input_data_emissao_rg_colaborador_as.setFocusPolicy(Qt.WheelFocus)
        self.input_data_emissao_rg_colaborador_as.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.input_data_emissao_rg_colaborador_as.setLayoutDirection(Qt.LeftToRight)
        self.input_data_emissao_rg_colaborador_as.setAutoFillBackground(False)
        self.input_data_emissao_rg_colaborador_as.setStyleSheet(u"QDateEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QDateEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_data_emissao_rg_colaborador_as.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.input_data_emissao_rg_colaborador_as.setAlignment(Qt.AlignCenter)
        self.input_data_emissao_rg_colaborador_as.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.input_data_emissao_rg_colaborador_as.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.input_data_emissao_rg_colaborador_as.setCurrentSection(QDateTimeEdit.DaySection)
        self.input_data_emissao_rg_colaborador_as.setCalendarPopup(False)
        self.input_data_emissao_rg_colaborador_as.setCurrentSectionIndex(0)

        self.verticalLayout_111.addWidget(self.input_data_emissao_rg_colaborador_as)


        self.horizontalLayout_79.addWidget(self.frame_207)

        self.frame_203 = QFrame(self.frame_201)
        self.frame_203.setObjectName(u"frame_203")
        self.frame_203.setMinimumSize(QSize(0, 0))
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
        self.input_pis_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_pis_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_pis_colaborador_as.setFont(font)

        self.verticalLayout_142.addWidget(self.input_pis_colaborador_as)


        self.horizontalLayout_79.addWidget(self.frame_203)

        self.frame_204 = QFrame(self.frame_201)
        self.frame_204.setObjectName(u"frame_204")
        self.frame_204.setMinimumSize(QSize(0, 0))
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
        self.input_sexo_colaborador_comboBox_as.setMinimumSize(QSize(0, 30))
        self.input_sexo_colaborador_comboBox_as.setMaximumSize(QSize(16777215, 30))
        self.input_sexo_colaborador_comboBox_as.setFont(font)

        self.verticalLayout_143.addWidget(self.input_sexo_colaborador_comboBox_as)


        self.horizontalLayout_79.addWidget(self.frame_204)

        self.frame_205 = QFrame(self.frame_201)
        self.frame_205.setObjectName(u"frame_205")
        self.frame_205.setMinimumSize(QSize(0, 0))
        self.frame_205.setMaximumSize(QSize(155, 16777215))
        self.frame_205.setFrameShape(QFrame.StyledPanel)
        self.frame_205.setFrameShadow(QFrame.Raised)
        self.verticalLayout_144 = QVBoxLayout(self.frame_205)
        self.verticalLayout_144.setSpacing(0)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.verticalLayout_144.setContentsMargins(0, 0, 0, 0)
        self.label_telefone_colaborador_as = QLabel(self.frame_205)
        self.label_telefone_colaborador_as.setObjectName(u"label_telefone_colaborador_as")
        self.label_telefone_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_telefone_colaborador_as.setMaximumSize(QSize(155, 16777215))
        self.label_telefone_colaborador_as.setFont(font)

        self.verticalLayout_144.addWidget(self.label_telefone_colaborador_as)

        self.input_telefone_colaborador_as = QLineEdit(self.frame_205)
        self.input_telefone_colaborador_as.setObjectName(u"input_telefone_colaborador_as")
        self.input_telefone_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_telefone_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_telefone_colaborador_as.setFont(font)

        self.verticalLayout_144.addWidget(self.input_telefone_colaborador_as)


        self.horizontalLayout_79.addWidget(self.frame_205)

        self.frame_206 = QFrame(self.frame_201)
        self.frame_206.setObjectName(u"frame_206")
        self.frame_206.setMinimumSize(QSize(0, 0))
        self.frame_206.setMaximumSize(QSize(240, 16777215))
        self.frame_206.setFrameShape(QFrame.StyledPanel)
        self.frame_206.setFrameShadow(QFrame.Raised)
        self.verticalLayout_145 = QVBoxLayout(self.frame_206)
        self.verticalLayout_145.setSpacing(0)
        self.verticalLayout_145.setObjectName(u"verticalLayout_145")
        self.verticalLayout_145.setContentsMargins(0, 0, 0, 0)
        self.label_email_colaborador_as = QLabel(self.frame_206)
        self.label_email_colaborador_as.setObjectName(u"label_email_colaborador_as")
        self.label_email_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_email_colaborador_as.setMaximumSize(QSize(240, 16777215))
        self.label_email_colaborador_as.setFont(font)

        self.verticalLayout_145.addWidget(self.label_email_colaborador_as)

        self.input_email_colaborador_as = QLineEdit(self.frame_206)
        self.input_email_colaborador_as.setObjectName(u"input_email_colaborador_as")
        self.input_email_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_email_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_email_colaborador_as.setFont(font)

        self.verticalLayout_145.addWidget(self.input_email_colaborador_as)


        self.horizontalLayout_79.addWidget(self.frame_206)


        self.gridLayout_2.addWidget(self.frame_201, 1, 1, 1, 1)

        self.frame_241 = QFrame(self.frame_194)
        self.frame_241.setObjectName(u"frame_241")
        self.frame_241.setMinimumSize(QSize(0, 0))
        self.frame_241.setMaximumSize(QSize(16777215, 60))
        self.frame_241.setStyleSheet(u"")
        self.frame_241.setFrameShape(QFrame.StyledPanel)
        self.frame_241.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_241)
        self.horizontalLayout_80.setSpacing(0)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.frame_378 = QFrame(self.frame_241)
        self.frame_378.setObjectName(u"frame_378")
        self.frame_378.setMinimumSize(QSize(282, 0))
        self.frame_378.setMaximumSize(QSize(281, 16777215))
        self.frame_378.setFrameShape(QFrame.StyledPanel)
        self.frame_378.setFrameShadow(QFrame.Raised)
        self.verticalLayout_187 = QVBoxLayout(self.frame_378)
        self.verticalLayout_187.setSpacing(5)
        self.verticalLayout_187.setObjectName(u"verticalLayout_187")
        self.verticalLayout_187.setContentsMargins(0, 0, 0, 0)
        self.label_usuario_colaborador_as_2 = QLabel(self.frame_378)
        self.label_usuario_colaborador_as_2.setObjectName(u"label_usuario_colaborador_as_2")
        self.label_usuario_colaborador_as_2.setMinimumSize(QSize(0, 0))
        self.label_usuario_colaborador_as_2.setMaximumSize(QSize(280, 16777215))
        self.label_usuario_colaborador_as_2.setFont(font)

        self.verticalLayout_187.addWidget(self.label_usuario_colaborador_as_2)

        self.input_usuario_colaborador_as_2 = QLineEdit(self.frame_378)
        self.input_usuario_colaborador_as_2.setObjectName(u"input_usuario_colaborador_as_2")
        self.input_usuario_colaborador_as_2.setMinimumSize(QSize(0, 30))
        self.input_usuario_colaborador_as_2.setMaximumSize(QSize(280, 30))
        self.input_usuario_colaborador_as_2.setFont(font)

        self.verticalLayout_187.addWidget(self.input_usuario_colaborador_as_2)


        self.horizontalLayout_80.addWidget(self.frame_378)

        self.frame_386 = QFrame(self.frame_241)
        self.frame_386.setObjectName(u"frame_386")
        self.frame_386.setMinimumSize(QSize(231, 0))
        self.frame_386.setMaximumSize(QSize(230, 16777215))
        self.frame_386.setFrameShape(QFrame.StyledPanel)
        self.frame_386.setFrameShadow(QFrame.Raised)
        self.verticalLayout_262 = QVBoxLayout(self.frame_386)
        self.verticalLayout_262.setSpacing(0)
        self.verticalLayout_262.setObjectName(u"verticalLayout_262")
        self.verticalLayout_262.setContentsMargins(0, 0, 0, 0)
        self.label_senha_colaborador_as_2 = QLabel(self.frame_386)
        self.label_senha_colaborador_as_2.setObjectName(u"label_senha_colaborador_as_2")
        self.label_senha_colaborador_as_2.setMinimumSize(QSize(0, 0))
        self.label_senha_colaborador_as_2.setMaximumSize(QSize(230, 16777215))
        self.label_senha_colaborador_as_2.setFont(font)

        self.verticalLayout_262.addWidget(self.label_senha_colaborador_as_2)

        self.input_senha_colaborador_as_2 = QLineEdit(self.frame_386)
        self.input_senha_colaborador_as_2.setObjectName(u"input_senha_colaborador_as_2")
        self.input_senha_colaborador_as_2.setMinimumSize(QSize(0, 30))
        self.input_senha_colaborador_as_2.setMaximumSize(QSize(229, 30))
        self.input_senha_colaborador_as_2.setFont(font)

        self.verticalLayout_262.addWidget(self.input_senha_colaborador_as_2)


        self.horizontalLayout_80.addWidget(self.frame_386)

        self.frame_387 = QFrame(self.frame_241)
        self.frame_387.setObjectName(u"frame_387")
        self.frame_387.setMinimumSize(QSize(231, 0))
        self.frame_387.setMaximumSize(QSize(230, 16777215))
        self.frame_387.setFrameShape(QFrame.StyledPanel)
        self.frame_387.setFrameShadow(QFrame.Raised)
        self.verticalLayout_266 = QVBoxLayout(self.frame_387)
        self.verticalLayout_266.setSpacing(0)
        self.verticalLayout_266.setObjectName(u"verticalLayout_266")
        self.verticalLayout_266.setContentsMargins(0, 0, 0, 0)
        self.label_confirmar_senha_colaborador_as_2 = QLabel(self.frame_387)
        self.label_confirmar_senha_colaborador_as_2.setObjectName(u"label_confirmar_senha_colaborador_as_2")
        self.label_confirmar_senha_colaborador_as_2.setMinimumSize(QSize(0, 0))
        self.label_confirmar_senha_colaborador_as_2.setMaximumSize(QSize(230, 16777215))
        self.label_confirmar_senha_colaborador_as_2.setFont(font)

        self.verticalLayout_266.addWidget(self.label_confirmar_senha_colaborador_as_2)

        self.input_confirmar_senha_colaborador_as_2 = QLineEdit(self.frame_387)
        self.input_confirmar_senha_colaborador_as_2.setObjectName(u"input_confirmar_senha_colaborador_as_2")
        self.input_confirmar_senha_colaborador_as_2.setMinimumSize(QSize(0, 30))
        self.input_confirmar_senha_colaborador_as_2.setMaximumSize(QSize(229, 30))
        self.input_confirmar_senha_colaborador_as_2.setFont(font)

        self.verticalLayout_266.addWidget(self.input_confirmar_senha_colaborador_as_2)


        self.horizontalLayout_80.addWidget(self.frame_387)

        self.horizontalSpacer_81 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_80.addItem(self.horizontalSpacer_81)


        self.gridLayout_2.addWidget(self.frame_241, 5, 1, 1, 1)

        self.frame_230 = QFrame(self.frame_194)
        self.frame_230.setObjectName(u"frame_230")
        self.frame_230.setMinimumSize(QSize(1019, 0))
        self.frame_230.setMaximumSize(QSize(1019, 60))
        self.frame_230.setStyleSheet(u"")
        self.frame_230.setFrameShape(QFrame.StyledPanel)
        self.frame_230.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_230)
        self.horizontalLayout_88.setSpacing(0)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.frame_231 = QFrame(self.frame_230)
        self.frame_231.setObjectName(u"frame_231")
        self.frame_231.setMinimumSize(QSize(149, 0))
        self.frame_231.setMaximumSize(QSize(149, 58))
        self.frame_231.setFrameShape(QFrame.StyledPanel)
        self.frame_231.setFrameShadow(QFrame.Raised)
        self.verticalLayout_135 = QVBoxLayout(self.frame_231)
        self.verticalLayout_135.setSpacing(0)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.label_estado_civil_colaborador_as = QLabel(self.frame_231)
        self.label_estado_civil_colaborador_as.setObjectName(u"label_estado_civil_colaborador_as")
        self.label_estado_civil_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_estado_civil_colaborador_as.setMaximumSize(QSize(90, 26))
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
        self.input_estado_civil_colaborador_comboBox_as.setMinimumSize(QSize(0, 30))
        self.input_estado_civil_colaborador_comboBox_as.setMaximumSize(QSize(145, 30))
        self.input_estado_civil_colaborador_comboBox_as.setFont(font)

        self.verticalLayout_135.addWidget(self.input_estado_civil_colaborador_comboBox_as)


        self.horizontalLayout_88.addWidget(self.frame_231)

        self.frame_255 = QFrame(self.frame_230)
        self.frame_255.setObjectName(u"frame_255")
        self.frame_255.setMinimumSize(QSize(125, 58))
        self.frame_255.setMaximumSize(QSize(125, 58))
        self.frame_255.setFrameShape(QFrame.StyledPanel)
        self.frame_255.setFrameShadow(QFrame.Raised)
        self.verticalLayout_171 = QVBoxLayout(self.frame_255)
        self.verticalLayout_171.setSpacing(5)
        self.verticalLayout_171.setObjectName(u"verticalLayout_171")
        self.verticalLayout_171.setContentsMargins(0, 0, 0, 0)
        self.label_salario_colaborador_as = QLabel(self.frame_255)
        self.label_salario_colaborador_as.setObjectName(u"label_salario_colaborador_as")
        self.label_salario_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_salario_colaborador_as.setMaximumSize(QSize(100, 16777215))
        self.label_salario_colaborador_as.setFont(font)

        self.verticalLayout_171.addWidget(self.label_salario_colaborador_as)

        self.input_salario_colaborador_as = QLineEdit(self.frame_255)
        self.input_salario_colaborador_as.setObjectName(u"input_salario_colaborador_as")
        self.input_salario_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_salario_colaborador_as.setMaximumSize(QSize(123, 30))
        self.input_salario_colaborador_as.setFont(font)

        self.verticalLayout_171.addWidget(self.input_salario_colaborador_as)


        self.horizontalLayout_88.addWidget(self.frame_255)

        self.frame_233 = QFrame(self.frame_230)
        self.frame_233.setObjectName(u"frame_233")
        self.frame_233.setMinimumSize(QSize(120, 58))
        self.frame_233.setMaximumSize(QSize(120, 58))
        self.frame_233.setFrameShape(QFrame.StyledPanel)
        self.frame_233.setFrameShadow(QFrame.Raised)
        self.verticalLayout_163 = QVBoxLayout(self.frame_233)
        self.verticalLayout_163.setSpacing(0)
        self.verticalLayout_163.setObjectName(u"verticalLayout_163")
        self.verticalLayout_163.setContentsMargins(0, 0, 0, 0)
        self.label_Data_de_admissao_colaborador_as = QLabel(self.frame_233)
        self.label_Data_de_admissao_colaborador_as.setObjectName(u"label_Data_de_admissao_colaborador_as")
        self.label_Data_de_admissao_colaborador_as.setMinimumSize(QSize(114, 0))
        self.label_Data_de_admissao_colaborador_as.setMaximumSize(QSize(118, 16777215))
        self.label_Data_de_admissao_colaborador_as.setFont(font)

        self.verticalLayout_163.addWidget(self.label_Data_de_admissao_colaborador_as)

        self.input_data_admissao_colaborador_as_5 = QDateEdit(self.frame_233)
        self.input_data_admissao_colaborador_as_5.setObjectName(u"input_data_admissao_colaborador_as_5")
        sizePolicy1.setHeightForWidth(self.input_data_admissao_colaborador_as_5.sizePolicy().hasHeightForWidth())
        self.input_data_admissao_colaborador_as_5.setSizePolicy(sizePolicy1)
        self.input_data_admissao_colaborador_as_5.setMinimumSize(QSize(0, 30))
        self.input_data_admissao_colaborador_as_5.setMaximumSize(QSize(150, 16777215))
        self.input_data_admissao_colaborador_as_5.setFont(font8)
        self.input_data_admissao_colaborador_as_5.setFocusPolicy(Qt.WheelFocus)
        self.input_data_admissao_colaborador_as_5.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.input_data_admissao_colaborador_as_5.setLayoutDirection(Qt.LeftToRight)
        self.input_data_admissao_colaborador_as_5.setAutoFillBackground(False)
        self.input_data_admissao_colaborador_as_5.setStyleSheet(u"QDateEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QDateEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_data_admissao_colaborador_as_5.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.input_data_admissao_colaborador_as_5.setAlignment(Qt.AlignCenter)
        self.input_data_admissao_colaborador_as_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.input_data_admissao_colaborador_as_5.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.input_data_admissao_colaborador_as_5.setCurrentSection(QDateTimeEdit.DaySection)
        self.input_data_admissao_colaborador_as_5.setCalendarPopup(False)
        self.input_data_admissao_colaborador_as_5.setCurrentSectionIndex(0)

        self.verticalLayout_163.addWidget(self.input_data_admissao_colaborador_as_5, 0, Qt.AlignHCenter)


        self.horizontalLayout_88.addWidget(self.frame_233)

        self.frame_234 = QFrame(self.frame_230)
        self.frame_234.setObjectName(u"frame_234")
        self.frame_234.setMinimumSize(QSize(190, 58))
        self.frame_234.setMaximumSize(QSize(190, 58))
        self.frame_234.setFrameShape(QFrame.StyledPanel)
        self.frame_234.setFrameShadow(QFrame.Raised)
        self.verticalLayout_162 = QVBoxLayout(self.frame_234)
        self.verticalLayout_162.setSpacing(5)
        self.verticalLayout_162.setObjectName(u"verticalLayout_162")
        self.verticalLayout_162.setContentsMargins(0, 0, 0, 0)
        self.label_escolaridade_colaborador_as = QLabel(self.frame_234)
        self.label_escolaridade_colaborador_as.setObjectName(u"label_escolaridade_colaborador_as")
        self.label_escolaridade_colaborador_as.setMinimumSize(QSize(0, 0))
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
        self.input_escolaridade_colaborador_comboBox_as.setMinimumSize(QSize(0, 30))
        self.input_escolaridade_colaborador_comboBox_as.setMaximumSize(QSize(16777215, 30))
        self.input_escolaridade_colaborador_comboBox_as.setFont(font)

        self.verticalLayout_162.addWidget(self.input_escolaridade_colaborador_comboBox_as)


        self.horizontalLayout_88.addWidget(self.frame_234)

        self.frame_235 = QFrame(self.frame_230)
        self.frame_235.setObjectName(u"frame_235")
        self.frame_235.setMinimumSize(QSize(144, 58))
        self.frame_235.setMaximumSize(QSize(145, 58))
        self.frame_235.setFrameShape(QFrame.StyledPanel)
        self.frame_235.setFrameShadow(QFrame.Raised)
        self.verticalLayout_165 = QVBoxLayout(self.frame_235)
        self.verticalLayout_165.setSpacing(5)
        self.verticalLayout_165.setObjectName(u"verticalLayout_165")
        self.verticalLayout_165.setContentsMargins(0, 0, 0, 0)
        self.label_cargo_colaborador_as = QLabel(self.frame_235)
        self.label_cargo_colaborador_as.setObjectName(u"label_cargo_colaborador_as")
        self.label_cargo_colaborador_as.setMinimumSize(QSize(130, 0))
        self.label_cargo_colaborador_as.setMaximumSize(QSize(130, 16777215))
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
        sizePolicy1.setHeightForWidth(self.input_cargo_colaborador_comboBox_as.sizePolicy().hasHeightForWidth())
        self.input_cargo_colaborador_comboBox_as.setSizePolicy(sizePolicy1)
        self.input_cargo_colaborador_comboBox_as.setMinimumSize(QSize(138, 30))
        self.input_cargo_colaborador_comboBox_as.setMaximumSize(QSize(138, 30))
        self.input_cargo_colaborador_comboBox_as.setFont(font)

        self.verticalLayout_165.addWidget(self.input_cargo_colaborador_comboBox_as)


        self.horizontalLayout_88.addWidget(self.frame_235)

        self.frame_236 = QFrame(self.frame_230)
        self.frame_236.setObjectName(u"frame_236")
        self.frame_236.setMinimumSize(QSize(153, 58))
        self.frame_236.setMaximumSize(QSize(150, 58))
        self.frame_236.setFrameShape(QFrame.StyledPanel)
        self.frame_236.setFrameShadow(QFrame.Raised)
        self.verticalLayout_164 = QVBoxLayout(self.frame_236)
        self.verticalLayout_164.setSpacing(5)
        self.verticalLayout_164.setObjectName(u"verticalLayout_164")
        self.verticalLayout_164.setContentsMargins(0, 0, 0, 0)
        self.label_periodo_colaborador_as = QLabel(self.frame_236)
        self.label_periodo_colaborador_as.setObjectName(u"label_periodo_colaborador_as")
        self.label_periodo_colaborador_as.setMinimumSize(QSize(130, 0))
        self.label_periodo_colaborador_as.setMaximumSize(QSize(130, 16777215))
        self.label_periodo_colaborador_as.setFont(font)

        self.verticalLayout_164.addWidget(self.label_periodo_colaborador_as)

        self.input_periodo_colaborador_comboBox_as = QComboBox(self.frame_236)
        self.input_periodo_colaborador_comboBox_as.addItem("")
        self.input_periodo_colaborador_comboBox_as.addItem("")
        self.input_periodo_colaborador_comboBox_as.addItem("")
        self.input_periodo_colaborador_comboBox_as.addItem("")
        self.input_periodo_colaborador_comboBox_as.addItem("")
        self.input_periodo_colaborador_comboBox_as.setObjectName(u"input_periodo_colaborador_comboBox_as")
        self.input_periodo_colaborador_comboBox_as.setMinimumSize(QSize(130, 30))
        self.input_periodo_colaborador_comboBox_as.setMaximumSize(QSize(150, 30))
        self.input_periodo_colaborador_comboBox_as.setFont(font)

        self.verticalLayout_164.addWidget(self.input_periodo_colaborador_comboBox_as)


        self.horizontalLayout_88.addWidget(self.frame_236)

        self.horizontalSpacer_82 = QSpacerItem(104, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_88.addItem(self.horizontalSpacer_82)


        self.gridLayout_2.addWidget(self.frame_230, 4, 1, 1, 1)

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

        self.verticalLayout_179.addWidget(self.frame_259)

        self.verticalSpacer = QSpacerItem(20, 19, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_179.addItem(self.verticalSpacer)


        self.gridLayout_2.addWidget(self.frame_258, 0, 0, 3, 1, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_77.addWidget(self.frame_194)


        self.verticalLayout_83.addWidget(self.frame_193)

        self.frame_215 = QFrame(self.page_cadastro_colaborador_as)
        self.frame_215.setObjectName(u"frame_215")
        self.frame_215.setMinimumSize(QSize(0, 0))
        self.frame_215.setFrameShape(QFrame.StyledPanel)
        self.frame_215.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_215)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.frame_269 = QFrame(self.frame_215)
        self.frame_269.setObjectName(u"frame_269")
        sizePolicy.setHeightForWidth(self.frame_269.sizePolicy().hasHeightForWidth())
        self.frame_269.setSizePolicy(sizePolicy)
        self.frame_269.setFrameShape(QFrame.StyledPanel)
        self.frame_269.setFrameShadow(QFrame.Raised)
        self.verticalLayout_168 = QVBoxLayout(self.frame_269)
        self.verticalLayout_168.setSpacing(0)
        self.verticalLayout_168.setObjectName(u"verticalLayout_168")
        self.verticalLayout_168.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_168.addItem(self.verticalSpacer_2)

        self.frame_250 = QFrame(self.frame_269)
        self.frame_250.setObjectName(u"frame_250")
        self.frame_250.setFrameShape(QFrame.StyledPanel)
        self.frame_250.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_250)
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.frame_272 = QFrame(self.frame_250)
        self.frame_272.setObjectName(u"frame_272")
        self.frame_272.setMinimumSize(QSize(130, 60))
        self.frame_272.setMaximumSize(QSize(130, 60))
        self.frame_272.setFrameShape(QFrame.StyledPanel)
        self.frame_272.setFrameShadow(QFrame.Raised)
        self.verticalLayout_167 = QVBoxLayout(self.frame_272)
        self.verticalLayout_167.setSpacing(0)
        self.verticalLayout_167.setObjectName(u"verticalLayout_167")
        self.verticalLayout_167.setContentsMargins(0, 0, 0, 0)
        self.btn_voltar_cadastro_colaborador_as = QPushButton(self.frame_272)
        self.btn_voltar_cadastro_colaborador_as.setObjectName(u"btn_voltar_cadastro_colaborador_as")
        self.btn_voltar_cadastro_colaborador_as.setMinimumSize(QSize(100, 40))
        self.btn_voltar_cadastro_colaborador_as.setMaximumSize(QSize(100, 40))
        self.btn_voltar_cadastro_colaborador_as.setFont(font11)
        self.btn_voltar_cadastro_colaborador_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_cadastro_colaborador_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.verticalLayout_167.addWidget(self.btn_voltar_cadastro_colaborador_as)


        self.horizontalLayout_94.addWidget(self.frame_272)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_94.addItem(self.horizontalSpacer_53)

        self.frame_239 = QFrame(self.frame_250)
        self.frame_239.setObjectName(u"frame_239")
        self.frame_239.setMinimumSize(QSize(130, 60))
        self.frame_239.setMaximumSize(QSize(150, 60))
        self.frame_239.setFrameShape(QFrame.StyledPanel)
        self.frame_239.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_239)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_concluir_cadastro_colaborador_as = QPushButton(self.frame_239)
        self.btn_concluir_cadastro_colaborador_as.setObjectName(u"btn_concluir_cadastro_colaborador_as")
        self.btn_concluir_cadastro_colaborador_as.setMinimumSize(QSize(140, 40))
        self.btn_concluir_cadastro_colaborador_as.setMaximumSize(QSize(140, 40))
        self.btn_concluir_cadastro_colaborador_as.setFont(font11)
        self.btn_concluir_cadastro_colaborador_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_concluir_cadastro_colaborador_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}\n"
"\n"
"")

        self.verticalLayout_5.addWidget(self.btn_concluir_cadastro_colaborador_as)


        self.horizontalLayout_94.addWidget(self.frame_239)


        self.verticalLayout_168.addWidget(self.frame_250)


        self.horizontalLayout_81.addWidget(self.frame_269)


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
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_125.sizePolicy().hasHeightForWidth())
        self.frame_125.setSizePolicy(sizePolicy6)
        self.frame_125.setMinimumSize(QSize(1271, 0))
        self.frame_125.setStyleSheet(u"QLabel{margin-left: 0.25em}")
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_125)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.frame_126 = QFrame(self.frame_125)
        self.frame_126.setObjectName(u"frame_126")
        sizePolicy6.setHeightForWidth(self.frame_126.sizePolicy().hasHeightForWidth())
        self.frame_126.setSizePolicy(sizePolicy6)
        self.frame_126.setMinimumSize(QSize(1270, 65))
        self.frame_126.setMaximumSize(QSize(1270, 60))
        self.frame_126.setFrameShape(QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_126)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.frame_141 = QFrame(self.frame_126)
        self.frame_141.setObjectName(u"frame_141")
        sizePolicy6.setHeightForWidth(self.frame_141.sizePolicy().hasHeightForWidth())
        self.frame_141.setSizePolicy(sizePolicy6)
        self.frame_141.setMinimumSize(QSize(150, 52))
        self.frame_141.setMaximumSize(QSize(140, 52))
        self.frame_141.setFrameShape(QFrame.StyledPanel)
        self.frame_141.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_141)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.label_data_inclusao_cursos_as = QLabel(self.frame_141)
        self.label_data_inclusao_cursos_as.setObjectName(u"label_data_inclusao_cursos_as")
        self.label_data_inclusao_cursos_as.setMinimumSize(QSize(130, 20))
        self.label_data_inclusao_cursos_as.setMaximumSize(QSize(130, 20))
        self.label_data_inclusao_cursos_as.setFont(font)

        self.verticalLayout_86.addWidget(self.label_data_inclusao_cursos_as)

        self.input_data_inclusao_cursos_as = QLineEdit(self.frame_141)
        self.input_data_inclusao_cursos_as.setObjectName(u"input_data_inclusao_cursos_as")
        self.input_data_inclusao_cursos_as.setMinimumSize(QSize(135, 30))
        self.input_data_inclusao_cursos_as.setMaximumSize(QSize(135, 30))
        self.input_data_inclusao_cursos_as.setFont(font)

        self.verticalLayout_86.addWidget(self.input_data_inclusao_cursos_as)


        self.horizontalLayout_62.addWidget(self.frame_141)

        self.horizontalSpacer_87 = QSpacerItem(49, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_87)

        self.frame_142 = QFrame(self.frame_126)
        self.frame_142.setObjectName(u"frame_142")
        self.frame_142.setMinimumSize(QSize(470, 55))
        self.frame_142.setMaximumSize(QSize(470, 55))
        self.frame_142.setFrameShape(QFrame.StyledPanel)
        self.frame_142.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_142)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.label_nome_cursos_as = QLabel(self.frame_142)
        self.label_nome_cursos_as.setObjectName(u"label_nome_cursos_as")
        self.label_nome_cursos_as.setMinimumSize(QSize(400, 20))
        self.label_nome_cursos_as.setMaximumSize(QSize(400, 20))
        self.label_nome_cursos_as.setFont(font)

        self.verticalLayout_95.addWidget(self.label_nome_cursos_as)

        self.input_nome_cursos_as = QLineEdit(self.frame_142)
        self.input_nome_cursos_as.setObjectName(u"input_nome_cursos_as")
        self.input_nome_cursos_as.setMinimumSize(QSize(450, 30))
        self.input_nome_cursos_as.setMaximumSize(QSize(450, 30))
        self.input_nome_cursos_as.setFont(font)

        self.verticalLayout_95.addWidget(self.input_nome_cursos_as)


        self.horizontalLayout_62.addWidget(self.frame_142)

        self.horizontalSpacer_88 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_88)

        self.frame_143 = QFrame(self.frame_126)
        self.frame_143.setObjectName(u"frame_143")
        self.frame_143.setMinimumSize(QSize(188, 55))
        self.frame_143.setMaximumSize(QSize(190, 55))
        self.frame_143.setFrameShape(QFrame.StyledPanel)
        self.frame_143.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.frame_143)
        self.verticalLayout_96.setSpacing(0)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.label_tipo_cursos_as = QLabel(self.frame_143)
        self.label_tipo_cursos_as.setObjectName(u"label_tipo_cursos_as")
        self.label_tipo_cursos_as.setMinimumSize(QSize(170, 20))
        self.label_tipo_cursos_as.setMaximumSize(QSize(170, 20))
        self.label_tipo_cursos_as.setFont(font)

        self.verticalLayout_96.addWidget(self.label_tipo_cursos_as)

        self.input_tipo_cursos_as = QComboBox(self.frame_143)
        self.input_tipo_cursos_as.addItem("")
        self.input_tipo_cursos_as.addItem("")
        self.input_tipo_cursos_as.addItem("")
        self.input_tipo_cursos_as.setObjectName(u"input_tipo_cursos_as")
        self.input_tipo_cursos_as.setMinimumSize(QSize(170, 30))
        self.input_tipo_cursos_as.setMaximumSize(QSize(170, 30))
        self.input_tipo_cursos_as.setFont(font)

        self.verticalLayout_96.addWidget(self.input_tipo_cursos_as)


        self.horizontalLayout_62.addWidget(self.frame_143)

        self.horizontalSpacer_84 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_84)

        self.frame_144 = QFrame(self.frame_126)
        self.frame_144.setObjectName(u"frame_144")
        self.frame_144.setMinimumSize(QSize(200, 50))
        self.frame_144.setMaximumSize(QSize(200, 50))
        self.frame_144.setStyleSheet(u"background-color: #EC848C; border-radius: 10px")
        self.frame_144.setFrameShape(QFrame.StyledPanel)
        self.frame_144.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_144)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(33, 0, 0, 0)
        self.label_situacao_cursos_as = QLabel(self.frame_144)
        self.label_situacao_cursos_as.setObjectName(u"label_situacao_cursos_as")
        self.label_situacao_cursos_as.setMinimumSize(QSize(140, 25))
        self.label_situacao_cursos_as.setMaximumSize(QSize(140, 25))
        self.label_situacao_cursos_as.setFont(font)

        self.verticalLayout_97.addWidget(self.label_situacao_cursos_as)

        self.frame_145 = QFrame(self.frame_144)
        self.frame_145.setObjectName(u"frame_145")
        self.frame_145.setMinimumSize(QSize(140, 20))
        self.frame_145.setMaximumSize(QSize(140, 20))
        self.frame_145.setFrameShape(QFrame.StyledPanel)
        self.frame_145.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_145)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.input_ativo_cursos_as = QRadioButton(self.frame_145)
        self.input_ativo_cursos_as.setObjectName(u"input_ativo_cursos_as")
        self.input_ativo_cursos_as.setMinimumSize(QSize(85, 19))
        self.input_ativo_cursos_as.setMaximumSize(QSize(85, 19))
        self.input_ativo_cursos_as.setFont(font8)
        self.input_ativo_cursos_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_63.addWidget(self.input_ativo_cursos_as)

        self.input_inativo_cursos_as = QRadioButton(self.frame_145)
        self.input_inativo_cursos_as.setObjectName(u"input_inativo_cursos_as")
        self.input_inativo_cursos_as.setMinimumSize(QSize(85, 19))
        self.input_inativo_cursos_as.setMaximumSize(QSize(85, 19))
        self.input_inativo_cursos_as.setFont(font8)
        self.input_inativo_cursos_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_63.addWidget(self.input_inativo_cursos_as)


        self.verticalLayout_97.addWidget(self.frame_145)


        self.horizontalLayout_62.addWidget(self.frame_144)

        self.horizontalSpacer_85 = QSpacerItem(48, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_85)


        self.verticalLayout_85.addWidget(self.frame_126)

        self.frame_127 = QFrame(self.frame_125)
        self.frame_127.setObjectName(u"frame_127")
        self.frame_127.setMaximumSize(QSize(16777215, 100))
        self.frame_127.setFrameShape(QFrame.StyledPanel)
        self.frame_127.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_127)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.frame_146 = QFrame(self.frame_127)
        self.frame_146.setObjectName(u"frame_146")
        self.frame_146.setMinimumSize(QSize(0, 60))
        self.frame_146.setMaximumSize(QSize(360, 60))
        self.frame_146.setFrameShape(QFrame.StyledPanel)
        self.frame_146.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_146)
        self.verticalLayout_98.setSpacing(0)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.label_responsavel_cursos_as = QLabel(self.frame_146)
        self.label_responsavel_cursos_as.setObjectName(u"label_responsavel_cursos_as")
        self.label_responsavel_cursos_as.setMinimumSize(QSize(200, 30))
        self.label_responsavel_cursos_as.setMaximumSize(QSize(200, 30))
        self.label_responsavel_cursos_as.setFont(font)

        self.verticalLayout_98.addWidget(self.label_responsavel_cursos_as)

        self.input_responsavel_cursos_as = QLineEdit(self.frame_146)
        self.input_responsavel_cursos_as.setObjectName(u"input_responsavel_cursos_as")
        self.input_responsavel_cursos_as.setMinimumSize(QSize(0, 30))
        self.input_responsavel_cursos_as.setMaximumSize(QSize(16777215, 30))
        self.input_responsavel_cursos_as.setFont(font)

        self.verticalLayout_98.addWidget(self.input_responsavel_cursos_as)


        self.horizontalLayout_64.addWidget(self.frame_146)

        self.horizontalSpacer_90 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_90)

        self.frame_147 = QFrame(self.frame_127)
        self.frame_147.setObjectName(u"frame_147")
        self.frame_147.setMinimumSize(QSize(160, 60))
        self.frame_147.setMaximumSize(QSize(160, 60))
        self.frame_147.setFrameShape(QFrame.StyledPanel)
        self.frame_147.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.frame_147)
        self.verticalLayout_99.setSpacing(0)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.label_data_inicio_cursos_as = QLabel(self.frame_147)
        self.label_data_inicio_cursos_as.setObjectName(u"label_data_inicio_cursos_as")
        self.label_data_inicio_cursos_as.setMinimumSize(QSize(120, 30))
        self.label_data_inicio_cursos_as.setMaximumSize(QSize(120, 30))
        self.label_data_inicio_cursos_as.setFont(font)
        self.label_data_inicio_cursos_as.setAlignment(Qt.AlignCenter)

        self.verticalLayout_99.addWidget(self.label_data_inicio_cursos_as, 0, Qt.AlignHCenter)

        self.input_data_inicio_cursos_as = QDateEdit(self.frame_147)
        self.input_data_inicio_cursos_as.setObjectName(u"input_data_inicio_cursos_as")
        sizePolicy1.setHeightForWidth(self.input_data_inicio_cursos_as.sizePolicy().hasHeightForWidth())
        self.input_data_inicio_cursos_as.setSizePolicy(sizePolicy1)
        self.input_data_inicio_cursos_as.setMinimumSize(QSize(0, 30))
        self.input_data_inicio_cursos_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_data_inicio_cursos_as.setFont(font8)
        self.input_data_inicio_cursos_as.setFocusPolicy(Qt.WheelFocus)
        self.input_data_inicio_cursos_as.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.input_data_inicio_cursos_as.setLayoutDirection(Qt.LeftToRight)
        self.input_data_inicio_cursos_as.setAutoFillBackground(False)
        self.input_data_inicio_cursos_as.setStyleSheet(u"QDateEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QDateEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_data_inicio_cursos_as.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.input_data_inicio_cursos_as.setAlignment(Qt.AlignCenter)
        self.input_data_inicio_cursos_as.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.input_data_inicio_cursos_as.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.input_data_inicio_cursos_as.setCurrentSection(QDateTimeEdit.DaySection)
        self.input_data_inicio_cursos_as.setCalendarPopup(False)
        self.input_data_inicio_cursos_as.setCurrentSectionIndex(0)

        self.verticalLayout_99.addWidget(self.input_data_inicio_cursos_as, 0, Qt.AlignHCenter)


        self.horizontalLayout_64.addWidget(self.frame_147)

        self.frame_148 = QFrame(self.frame_127)
        self.frame_148.setObjectName(u"frame_148")
        self.frame_148.setMinimumSize(QSize(160, 60))
        self.frame_148.setMaximumSize(QSize(160, 60))
        self.frame_148.setFrameShape(QFrame.StyledPanel)
        self.frame_148.setFrameShadow(QFrame.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.frame_148)
        self.verticalLayout_100.setSpacing(0)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.label_data_termino_cursos_as = QLabel(self.frame_148)
        self.label_data_termino_cursos_as.setObjectName(u"label_data_termino_cursos_as")
        self.label_data_termino_cursos_as.setMinimumSize(QSize(0, 0))
        self.label_data_termino_cursos_as.setMaximumSize(QSize(160, 16777215))
        self.label_data_termino_cursos_as.setFont(font)
        self.label_data_termino_cursos_as.setAlignment(Qt.AlignCenter)

        self.verticalLayout_100.addWidget(self.label_data_termino_cursos_as, 0, Qt.AlignHCenter)

        self.input_data_termino_cursos_as = QDateEdit(self.frame_148)
        self.input_data_termino_cursos_as.setObjectName(u"input_data_termino_cursos_as")
        sizePolicy1.setHeightForWidth(self.input_data_termino_cursos_as.sizePolicy().hasHeightForWidth())
        self.input_data_termino_cursos_as.setSizePolicy(sizePolicy1)
        self.input_data_termino_cursos_as.setMinimumSize(QSize(0, 30))
        self.input_data_termino_cursos_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_data_termino_cursos_as.setFont(font8)
        self.input_data_termino_cursos_as.setFocusPolicy(Qt.WheelFocus)
        self.input_data_termino_cursos_as.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.input_data_termino_cursos_as.setLayoutDirection(Qt.LeftToRight)
        self.input_data_termino_cursos_as.setAutoFillBackground(False)
        self.input_data_termino_cursos_as.setStyleSheet(u"QDateEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QDateEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_data_termino_cursos_as.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.input_data_termino_cursos_as.setAlignment(Qt.AlignCenter)
        self.input_data_termino_cursos_as.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.input_data_termino_cursos_as.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.input_data_termino_cursos_as.setCurrentSection(QDateTimeEdit.DaySection)
        self.input_data_termino_cursos_as.setCalendarPopup(False)
        self.input_data_termino_cursos_as.setCurrentSectionIndex(0)

        self.verticalLayout_100.addWidget(self.input_data_termino_cursos_as, 0, Qt.AlignHCenter)


        self.horizontalLayout_64.addWidget(self.frame_148)

        self.horizontalSpacer_93 = QSpacerItem(96, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_93)

        self.frame_149 = QFrame(self.frame_127)
        self.frame_149.setObjectName(u"frame_149")
        self.frame_149.setMaximumSize(QSize(400, 16777215))
        self.frame_149.setFrameShape(QFrame.StyledPanel)
        self.frame_149.setFrameShadow(QFrame.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.frame_149)
        self.verticalLayout_101.setSpacing(5)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.label_dias_aulas_cursos_as = QLabel(self.frame_149)
        self.label_dias_aulas_cursos_as.setObjectName(u"label_dias_aulas_cursos_as")
        self.label_dias_aulas_cursos_as.setMinimumSize(QSize(120, 0))
        self.label_dias_aulas_cursos_as.setMaximumSize(QSize(120, 16777215))
        self.label_dias_aulas_cursos_as.setFont(font)

        self.verticalLayout_101.addWidget(self.label_dias_aulas_cursos_as)

        self.frame_150 = QFrame(self.frame_149)
        self.frame_150.setObjectName(u"frame_150")
        self.frame_150.setMaximumSize(QSize(400, 16777215))
        self.frame_150.setFrameShape(QFrame.StyledPanel)
        self.frame_150.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_150)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.frame_151 = QFrame(self.frame_150)
        self.frame_151.setObjectName(u"frame_151")
        self.frame_151.setMinimumSize(QSize(0, 70))
        self.frame_151.setMaximumSize(QSize(125, 16777215))
        self.frame_151.setFrameShape(QFrame.StyledPanel)
        self.frame_151.setFrameShadow(QFrame.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.frame_151)
        self.verticalLayout_102.setSpacing(5)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.frame_4151 = QFrame(self.frame_151)
        self.frame_4151.setObjectName(u"frame_4151")
        self.frame_4151.setMinimumSize(QSize(0, 30))
        self.frame_4151.setStyleSheet(u"background-color: #F3B9BF; border: none; border-radius: 5px")
        self.frame_4151.setFrameShape(QFrame.StyledPanel)
        self.frame_4151.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.frame_4151)
        self.verticalLayout_104.setSpacing(5)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(5, 0, 0, 0)
        self.input_segunda_cursos_as = QCheckBox(self.frame_4151)
        self.input_segunda_cursos_as.setObjectName(u"input_segunda_cursos_as")

        self.verticalLayout_104.addWidget(self.input_segunda_cursos_as, 0, Qt.AlignHCenter)


        self.verticalLayout_102.addWidget(self.frame_4151)

        self.frame_4161 = QFrame(self.frame_151)
        self.frame_4161.setObjectName(u"frame_4161")
        self.frame_4161.setMinimumSize(QSize(0, 30))
        self.frame_4161.setStyleSheet(u"background-color: #F3B9BF; border: none; border-radius: 5px")
        self.frame_4161.setFrameShape(QFrame.StyledPanel)
        self.frame_4161.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.frame_4161)
        self.verticalLayout_103.setSpacing(5)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.input_terca_cursos_as = QCheckBox(self.frame_4161)
        self.input_terca_cursos_as.setObjectName(u"input_terca_cursos_as")

        self.verticalLayout_103.addWidget(self.input_terca_cursos_as, 0, Qt.AlignHCenter)


        self.verticalLayout_102.addWidget(self.frame_4161)


        self.horizontalLayout_65.addWidget(self.frame_151)

        self.frame_152 = QFrame(self.frame_150)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setMinimumSize(QSize(0, 70))
        self.frame_152.setMaximumSize(QSize(125, 16777215))
        self.frame_152.setFrameShape(QFrame.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2841 = QVBoxLayout(self.frame_152)
        self.verticalLayout_2841.setSpacing(5)
        self.verticalLayout_2841.setObjectName(u"verticalLayout_2841")
        self.verticalLayout_2841.setContentsMargins(0, 0, 0, 0)
        self.frame_4171 = QFrame(self.frame_152)
        self.frame_4171.setObjectName(u"frame_4171")
        self.frame_4171.setMinimumSize(QSize(0, 30))
        self.frame_4171.setStyleSheet(u"background-color: #F3B9BF; border: none; border-radius: 5px")
        self.frame_4171.setFrameShape(QFrame.StyledPanel)
        self.frame_4171.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2851 = QVBoxLayout(self.frame_4171)
        self.verticalLayout_2851.setSpacing(5)
        self.verticalLayout_2851.setObjectName(u"verticalLayout_2851")
        self.verticalLayout_2851.setContentsMargins(5, 0, 0, 0)
        self.input_quarta_cursos_as = QCheckBox(self.frame_4171)
        self.input_quarta_cursos_as.setObjectName(u"input_quarta_cursos_as")

        self.verticalLayout_2851.addWidget(self.input_quarta_cursos_as, 0, Qt.AlignHCenter)


        self.verticalLayout_2841.addWidget(self.frame_4171)

        self.frame_4181 = QFrame(self.frame_152)
        self.frame_4181.setObjectName(u"frame_4181")
        self.frame_4181.setMinimumSize(QSize(0, 30))
        self.frame_4181.setStyleSheet(u"background-color: #F3B9BF; border: none; border-radius: 5px")
        self.frame_4181.setFrameShape(QFrame.StyledPanel)
        self.frame_4181.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2861 = QVBoxLayout(self.frame_4181)
        self.verticalLayout_2861.setSpacing(5)
        self.verticalLayout_2861.setObjectName(u"verticalLayout_2861")
        self.verticalLayout_2861.setContentsMargins(5, 0, 0, 0)
        self.input_quinta_cursos_as = QCheckBox(self.frame_4181)
        self.input_quinta_cursos_as.setObjectName(u"input_quinta_cursos_as")

        self.verticalLayout_2861.addWidget(self.input_quinta_cursos_as, 0, Qt.AlignHCenter)


        self.verticalLayout_2841.addWidget(self.frame_4181)


        self.horizontalLayout_65.addWidget(self.frame_152)

        self.frame_153 = QFrame(self.frame_150)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setMinimumSize(QSize(125, 70))
        self.frame_153.setMaximumSize(QSize(125, 16777215))
        self.frame_153.setFrameShape(QFrame.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2871 = QVBoxLayout(self.frame_153)
        self.verticalLayout_2871.setSpacing(5)
        self.verticalLayout_2871.setObjectName(u"verticalLayout_2871")
        self.verticalLayout_2871.setContentsMargins(0, 0, 0, 0)
        self.frame_4191 = QFrame(self.frame_153)
        self.frame_4191.setObjectName(u"frame_4191")
        self.frame_4191.setMinimumSize(QSize(117, 30))
        self.frame_4191.setMaximumSize(QSize(170, 30))
        self.frame_4191.setStyleSheet(u"background-color: #F3B9BF; border: none; border-radius: 5px")
        self.frame_4191.setFrameShape(QFrame.StyledPanel)
        self.frame_4191.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2881 = QVBoxLayout(self.frame_4191)
        self.verticalLayout_2881.setSpacing(5)
        self.verticalLayout_2881.setObjectName(u"verticalLayout_2881")
        self.verticalLayout_2881.setContentsMargins(5, 0, 0, 0)
        self.input_sexta_cursos_as = QCheckBox(self.frame_4191)
        self.input_sexta_cursos_as.setObjectName(u"input_sexta_cursos_as")

        self.verticalLayout_2881.addWidget(self.input_sexta_cursos_as, 0, Qt.AlignHCenter)


        self.verticalLayout_2871.addWidget(self.frame_4191)

        self.frame_4201 = QFrame(self.frame_153)
        self.frame_4201.setObjectName(u"frame_4201")
        self.frame_4201.setMinimumSize(QSize(123, 30))
        self.frame_4201.setMaximumSize(QSize(123, 30))
        self.frame_4201.setStyleSheet(u"background-color: #F3B9BF; border: none; border-radius: 5px")
        self.frame_4201.setFrameShape(QFrame.StyledPanel)
        self.frame_4201.setFrameShadow(QFrame.Raised)
        self.verticalLayout_289 = QVBoxLayout(self.frame_4201)
        self.verticalLayout_289.setSpacing(5)
        self.verticalLayout_289.setObjectName(u"verticalLayout_289")
        self.verticalLayout_289.setContentsMargins(0, 0, 0, 0)
        self.input_sabado_cursos_as = QCheckBox(self.frame_4201)
        self.input_sabado_cursos_as.setObjectName(u"input_sabado_cursos_as")

        self.verticalLayout_289.addWidget(self.input_sabado_cursos_as, 0, Qt.AlignHCenter)


        self.verticalLayout_2871.addWidget(self.frame_4201)


        self.horizontalLayout_65.addWidget(self.frame_153)


        self.verticalLayout_101.addWidget(self.frame_150)


        self.horizontalLayout_64.addWidget(self.frame_149)

        self.horizontalSpacer_83 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_83)


        self.verticalLayout_85.addWidget(self.frame_127)

        self.frame_136 = QFrame(self.frame_125)
        self.frame_136.setObjectName(u"frame_136")
        sizePolicy6.setHeightForWidth(self.frame_136.sizePolicy().hasHeightForWidth())
        self.frame_136.setSizePolicy(sizePolicy6)
        self.frame_136.setMinimumSize(QSize(1270, 60))
        self.frame_136.setMaximumSize(QSize(1285, 60))
        self.frame_136.setFrameShape(QFrame.StyledPanel)
        self.frame_136.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_136)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.frame_154 = QFrame(self.frame_136)
        self.frame_154.setObjectName(u"frame_154")
        sizePolicy.setHeightForWidth(self.frame_154.sizePolicy().hasHeightForWidth())
        self.frame_154.setSizePolicy(sizePolicy)
        self.frame_154.setMinimumSize(QSize(140, 60))
        self.frame_154.setMaximumSize(QSize(120, 60))
        self.frame_154.setFrameShape(QFrame.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_154)
        self.verticalLayout_105.setSpacing(0)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.label_horario_inicio_cursos_as = QLabel(self.frame_154)
        self.label_horario_inicio_cursos_as.setObjectName(u"label_horario_inicio_cursos_as")
        self.label_horario_inicio_cursos_as.setMinimumSize(QSize(90, 25))
        self.label_horario_inicio_cursos_as.setMaximumSize(QSize(90, 25))
        self.label_horario_inicio_cursos_as.setFont(font)
        self.label_horario_inicio_cursos_as.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_105.addWidget(self.label_horario_inicio_cursos_as)

        self.input_horario_inicio_cursos_as = QTimeEdit(self.frame_154)
        self.input_horario_inicio_cursos_as.setObjectName(u"input_horario_inicio_cursos_as")
        self.input_horario_inicio_cursos_as.setMinimumSize(QSize(130, 30))
        self.input_horario_inicio_cursos_as.setMaximumSize(QSize(130, 30))
        self.input_horario_inicio_cursos_as.setFont(font)
        self.input_horario_inicio_cursos_as.setStyleSheet(u"QTimeEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QTimeEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_horario_inicio_cursos_as.setInputMethodHints(Qt.ImhPreferNumbers|Qt.ImhTime)
        self.input_horario_inicio_cursos_as.setAlignment(Qt.AlignCenter)
        self.input_horario_inicio_cursos_as.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.verticalLayout_105.addWidget(self.input_horario_inicio_cursos_as)


        self.horizontalLayout_66.addWidget(self.frame_154)

        self.horizontalSpacer_86 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_66.addItem(self.horizontalSpacer_86)

        self.widget = QWidget(self.frame_136)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(140, 55))
        self.widget.setMaximumSize(QSize(140, 55))
        self.verticalLayout_106 = QVBoxLayout(self.widget)
        self.verticalLayout_106.setSpacing(0)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.label_horario_termino_cursos_as = QLabel(self.widget)
        self.label_horario_termino_cursos_as.setObjectName(u"label_horario_termino_cursos_as")
        self.label_horario_termino_cursos_as.setMinimumSize(QSize(110, 25))
        self.label_horario_termino_cursos_as.setMaximumSize(QSize(90, 25))
        self.label_horario_termino_cursos_as.setFont(font)
        self.label_horario_termino_cursos_as.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.label_horario_termino_cursos_as.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_106.addWidget(self.label_horario_termino_cursos_as)

        self.input_horario_termino_cursos_as = QTimeEdit(self.widget)
        self.input_horario_termino_cursos_as.setObjectName(u"input_horario_termino_cursos_as")
        self.input_horario_termino_cursos_as.setMinimumSize(QSize(130, 30))
        self.input_horario_termino_cursos_as.setMaximumSize(QSize(120, 30))
        self.input_horario_termino_cursos_as.setFont(font)
        self.input_horario_termino_cursos_as.setStyleSheet(u"QTimeEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QTimeEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_horario_termino_cursos_as.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.input_horario_termino_cursos_as.setInputMethodHints(Qt.ImhPreferNumbers|Qt.ImhTime)
        self.input_horario_termino_cursos_as.setAlignment(Qt.AlignCenter)
        self.input_horario_termino_cursos_as.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.verticalLayout_106.addWidget(self.input_horario_termino_cursos_as)


        self.horizontalLayout_66.addWidget(self.widget)

        self.horizontalSpacer_89 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_66.addItem(self.horizontalSpacer_89)

        self.frame_155 = QFrame(self.frame_136)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setMinimumSize(QSize(250, 60))
        self.frame_155.setMaximumSize(QSize(250, 60))
        self.frame_155.setFrameShape(QFrame.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.frame_155)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.label_periodo_cursos_as = QLabel(self.frame_155)
        self.label_periodo_cursos_as.setObjectName(u"label_periodo_cursos_as")
        self.label_periodo_cursos_as.setMinimumSize(QSize(200, 20))
        self.label_periodo_cursos_as.setMaximumSize(QSize(200, 20))
        self.label_periodo_cursos_as.setFont(font)

        self.verticalLayout_107.addWidget(self.label_periodo_cursos_as)

        self.input_periodo_cursos_as = QComboBox(self.frame_155)
        self.input_periodo_cursos_as.addItem("")
        self.input_periodo_cursos_as.addItem("")
        self.input_periodo_cursos_as.addItem("")
        self.input_periodo_cursos_as.addItem("")
        self.input_periodo_cursos_as.setObjectName(u"input_periodo_cursos_as")
        self.input_periodo_cursos_as.setMinimumSize(QSize(200, 30))
        self.input_periodo_cursos_as.setMaximumSize(QSize(200, 30))
        self.input_periodo_cursos_as.setFont(font)

        self.verticalLayout_107.addWidget(self.input_periodo_cursos_as)


        self.horizontalLayout_66.addWidget(self.frame_155)

        self.frame_156 = QFrame(self.frame_136)
        self.frame_156.setObjectName(u"frame_156")
        self.frame_156.setMinimumSize(QSize(120, 60))
        self.frame_156.setMaximumSize(QSize(120, 60))
        self.frame_156.setFrameShape(QFrame.StyledPanel)
        self.frame_156.setFrameShadow(QFrame.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.frame_156)
        self.verticalLayout_108.setSpacing(0)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.label_vagas_cursos_as = QLabel(self.frame_156)
        self.label_vagas_cursos_as.setObjectName(u"label_vagas_cursos_as")
        self.label_vagas_cursos_as.setMinimumSize(QSize(90, 20))
        self.label_vagas_cursos_as.setMaximumSize(QSize(90, 20))
        self.label_vagas_cursos_as.setFont(font)

        self.verticalLayout_108.addWidget(self.label_vagas_cursos_as)

        self.input_vagas_cursos_as = QLineEdit(self.frame_156)
        self.input_vagas_cursos_as.setObjectName(u"input_vagas_cursos_as")
        self.input_vagas_cursos_as.setMinimumSize(QSize(115, 30))
        self.input_vagas_cursos_as.setMaximumSize(QSize(115, 30))
        self.input_vagas_cursos_as.setFont(font)

        self.verticalLayout_108.addWidget(self.input_vagas_cursos_as)


        self.horizontalLayout_66.addWidget(self.frame_156)

        self.horizontalSpacer_92 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_66.addItem(self.horizontalSpacer_92)


        self.verticalLayout_85.addWidget(self.frame_136)

        self.frame_140 = QFrame(self.frame_125)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setMinimumSize(QSize(1270, 0))
        self.frame_140.setMaximumSize(QSize(1270, 16777215))
        self.frame_140.setFrameShape(QFrame.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.frame_140)
        self.verticalLayout_115.setSpacing(0)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_115.addItem(self.verticalSpacer_26)

        self.input_descricao_atividade_cursos_as = QTextEdit(self.frame_140)
        self.input_descricao_atividade_cursos_as.setObjectName(u"input_descricao_atividade_cursos_as")
        self.input_descricao_atividade_cursos_as.setMinimumSize(QSize(1225, 0))
        self.input_descricao_atividade_cursos_as.setMaximumSize(QSize(1225, 16777215))
        self.input_descricao_atividade_cursos_as.setFont(font)
        self.input_descricao_atividade_cursos_as.setStyleSheet(u"QTextEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QTextEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout_115.addWidget(self.input_descricao_atividade_cursos_as)


        self.verticalLayout_85.addWidget(self.frame_140)


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
        self.horizontalLayout_57.setSpacing(20)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(20, 0, 0, 0)
        self.btn_voltar_cursos_as = QPushButton(self.frame_124)
        self.btn_voltar_cursos_as.setObjectName(u"btn_voltar_cursos_as")
        self.btn_voltar_cursos_as.setMinimumSize(QSize(100, 40))
        self.btn_voltar_cursos_as.setMaximumSize(QSize(100, 40))
        self.btn_voltar_cursos_as.setFont(font11)
        self.btn_voltar_cursos_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_cursos_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout_57.addWidget(self.btn_voltar_cursos_as)

        self.btn_lista_pessoas_cursos_as = QPushButton(self.frame_124)
        self.btn_lista_pessoas_cursos_as.setObjectName(u"btn_lista_pessoas_cursos_as")
        self.btn_lista_pessoas_cursos_as.setMinimumSize(QSize(0, 40))
        self.btn_lista_pessoas_cursos_as.setMaximumSize(QSize(16777215, 40))
        self.btn_lista_pessoas_cursos_as.setFont(font11)
        self.btn_lista_pessoas_cursos_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lista_pessoas_cursos_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        icon17 = QIcon()
        icon17.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/adicionar-amigo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lista_pessoas_cursos_as.setIcon(icon17)
        self.btn_lista_pessoas_cursos_as.setIconSize(QSize(25, 25))

        self.horizontalLayout_57.addWidget(self.btn_lista_pessoas_cursos_as)

        self.horizontalSpacer_48 = QSpacerItem(1441, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_48)

        self.btn_concluir_cursos_as = QPushButton(self.frame_124)
        self.btn_concluir_cursos_as.setObjectName(u"btn_concluir_cursos_as")
        self.btn_concluir_cursos_as.setMinimumSize(QSize(140, 40))
        self.btn_concluir_cursos_as.setMaximumSize(QSize(140, 40))
        self.btn_concluir_cursos_as.setFont(font11)
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
        self.page_consulta_as = QWidget()
        self.page_consulta_as.setObjectName(u"page_consulta_as")
        self.page_consulta_as.setStyleSheet(u"color: #EC848C;")
        self.verticalLayout_117 = QVBoxLayout(self.page_consulta_as)
        self.verticalLayout_117.setSpacing(0)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.frame_165 = QFrame(self.page_consulta_as)
        self.frame_165.setObjectName(u"frame_165")
        self.frame_165.setStyleSheet(u"background-color: #F3B9BF;")
        self.frame_165.setFrameShape(QFrame.StyledPanel)
        self.frame_165.setFrameShadow(QFrame.Raised)
        self.verticalLayout_118 = QVBoxLayout(self.frame_165)
        self.verticalLayout_118.setSpacing(0)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.label_consulta_consulta_as = QLabel(self.frame_165)
        self.label_consulta_consulta_as.setObjectName(u"label_consulta_consulta_as")
        self.label_consulta_consulta_as.setFont(font1)
        self.label_consulta_consulta_as.setStyleSheet(u"background-color: rgb(243, 185, 191);")
        self.label_consulta_consulta_as.setAlignment(Qt.AlignCenter)

        self.verticalLayout_118.addWidget(self.label_consulta_consulta_as)


        self.verticalLayout_117.addWidget(self.frame_165)

        self.frame_166 = QFrame(self.page_consulta_as)
        self.frame_166.setObjectName(u"frame_166")
        self.frame_166.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"QLabel{margin-left: 0.25em}")
        self.frame_166.setFrameShape(QFrame.StyledPanel)
        self.frame_166.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_166)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(30, 20, 5, 5)
        self.frame_168 = QFrame(self.frame_166)
        self.frame_168.setObjectName(u"frame_168")
        self.frame_168.setStyleSheet(u"background-color: #EC848C; border-radius: 10px; color: #000")
        self.frame_168.setFrameShape(QFrame.StyledPanel)
        self.frame_168.setFrameShadow(QFrame.Raised)
        self.verticalLayout_119 = QVBoxLayout(self.frame_168)
        self.verticalLayout_119.setSpacing(0)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.frame_170 = QFrame(self.frame_168)
        self.frame_170.setObjectName(u"frame_170")
        self.frame_170.setFrameShape(QFrame.StyledPanel)
        self.frame_170.setFrameShadow(QFrame.Raised)
        self.verticalLayout_120 = QVBoxLayout(self.frame_170)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.label_buscar_consulta_as = QLabel(self.frame_170)
        self.label_buscar_consulta_as.setObjectName(u"label_buscar_consulta_as")
        font12 = QFont()
        font12.setFamilies([u"Abel"])
        font12.setPointSize(16)
        self.label_buscar_consulta_as.setFont(font12)
        self.label_buscar_consulta_as.setStyleSheet(u"")
        self.label_buscar_consulta_as.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_120.addWidget(self.label_buscar_consulta_as)


        self.verticalLayout_119.addWidget(self.frame_170)

        self.frame_172 = QFrame(self.frame_168)
        self.frame_172.setObjectName(u"frame_172")
        self.frame_172.setFrameShape(QFrame.StyledPanel)
        self.frame_172.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_172)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(20, 0, 0, 0)
        self.input_nome_radio_consulta_as = QRadioButton(self.frame_172)
        self.input_nome_radio_consulta_as.setObjectName(u"input_nome_radio_consulta_as")
        font13 = QFont()
        font13.setFamilies([u"Abel"])
        font13.setPointSize(14)
        self.input_nome_radio_consulta_as.setFont(font13)

        self.horizontalLayout_69.addWidget(self.input_nome_radio_consulta_as)

        self.input_cpf_radio_consulta_as = QRadioButton(self.frame_172)
        self.input_cpf_radio_consulta_as.setObjectName(u"input_cpf_radio_consulta_as")
        self.input_cpf_radio_consulta_as.setFont(font13)

        self.horizontalLayout_69.addWidget(self.input_cpf_radio_consulta_as)

        self.input_matricula_radio_consulta_as = QRadioButton(self.frame_172)
        self.input_matricula_radio_consulta_as.setObjectName(u"input_matricula_radio_consulta_as")
        self.input_matricula_radio_consulta_as.setFont(font13)

        self.horizontalLayout_69.addWidget(self.input_matricula_radio_consulta_as)


        self.verticalLayout_119.addWidget(self.frame_172)

        self.frame_171 = QFrame(self.frame_168)
        self.frame_171.setObjectName(u"frame_171")
        self.frame_171.setFrameShape(QFrame.StyledPanel)
        self.frame_171.setFrameShadow(QFrame.Raised)
        self.verticalLayout_121 = QVBoxLayout(self.frame_171)
        self.verticalLayout_121.setSpacing(0)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(10, 0, 10, 10)
        self.input_buscar_consulta_as = QLineEdit(self.frame_171)
        self.input_buscar_consulta_as.setObjectName(u"input_buscar_consulta_as")
        self.input_buscar_consulta_as.setMinimumSize(QSize(0, 30))
        self.input_buscar_consulta_as.setMaximumSize(QSize(16777215, 30))
        self.input_buscar_consulta_as.setFont(font)
        self.input_buscar_consulta_as.setStyleSheet(u"background-color: #fff")

        self.verticalLayout_121.addWidget(self.input_buscar_consulta_as)


        self.verticalLayout_119.addWidget(self.frame_171)


        self.horizontalLayout_68.addWidget(self.frame_168)

        self.frame_169 = QFrame(self.frame_166)
        self.frame_169.setObjectName(u"frame_169")
        self.frame_169.setStyleSheet(u"color: #000")
        self.frame_169.setFrameShape(QFrame.StyledPanel)
        self.frame_169.setFrameShadow(QFrame.Raised)
        self.verticalLayout_122 = QVBoxLayout(self.frame_169)
        self.verticalLayout_122.setSpacing(0)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.frame_173 = QFrame(self.frame_169)
        self.frame_173.setObjectName(u"frame_173")
        self.frame_173.setFrameShape(QFrame.StyledPanel)
        self.frame_173.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_173)
        self.horizontalLayout_70.setSpacing(5)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(30, 0, 0, 0)
        self.frame_175 = QFrame(self.frame_173)
        self.frame_175.setObjectName(u"frame_175")
        self.frame_175.setMaximumSize(QSize(160, 16777215))
        self.frame_175.setFont(font)
        self.frame_175.setFrameShape(QFrame.StyledPanel)
        self.frame_175.setFrameShadow(QFrame.Raised)
        self.verticalLayout_125 = QVBoxLayout(self.frame_175)
        self.verticalLayout_125.setSpacing(0)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.verticalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.label_matricula_consulta_as = QLabel(self.frame_175)
        self.label_matricula_consulta_as.setObjectName(u"label_matricula_consulta_as")
        self.label_matricula_consulta_as.setMaximumSize(QSize(160, 16777215))
        self.label_matricula_consulta_as.setFont(font)

        self.verticalLayout_125.addWidget(self.label_matricula_consulta_as)

        self.input_matricula_consulta_as = QLineEdit(self.frame_175)
        self.input_matricula_consulta_as.setObjectName(u"input_matricula_consulta_as")
        self.input_matricula_consulta_as.setEnabled(False)
        self.input_matricula_consulta_as.setMinimumSize(QSize(150, 30))
        self.input_matricula_consulta_as.setMaximumSize(QSize(150, 30))
        self.input_matricula_consulta_as.setFont(font)

        self.verticalLayout_125.addWidget(self.input_matricula_consulta_as)


        self.horizontalLayout_70.addWidget(self.frame_175)

        self.frame_176 = QFrame(self.frame_173)
        self.frame_176.setObjectName(u"frame_176")
        self.frame_176.setMaximumSize(QSize(460, 16777215))
        self.frame_176.setFrameShape(QFrame.StyledPanel)
        self.frame_176.setFrameShadow(QFrame.Raised)
        self.verticalLayout_123 = QVBoxLayout(self.frame_176)
        self.verticalLayout_123.setSpacing(0)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.label_nome_consulta_as = QLabel(self.frame_176)
        self.label_nome_consulta_as.setObjectName(u"label_nome_consulta_as")
        self.label_nome_consulta_as.setMaximumSize(QSize(460, 16777215))
        self.label_nome_consulta_as.setFont(font)

        self.verticalLayout_123.addWidget(self.label_nome_consulta_as)

        self.input_nome_consulta_as = QLineEdit(self.frame_176)
        self.input_nome_consulta_as.setObjectName(u"input_nome_consulta_as")
        self.input_nome_consulta_as.setMinimumSize(QSize(450, 30))
        self.input_nome_consulta_as.setMaximumSize(QSize(450, 30))
        self.input_nome_consulta_as.setFont(font)

        self.verticalLayout_123.addWidget(self.input_nome_consulta_as)


        self.horizontalLayout_70.addWidget(self.frame_176)

        self.frame_177 = QFrame(self.frame_173)
        self.frame_177.setObjectName(u"frame_177")
        self.frame_177.setMaximumSize(QSize(180, 16777215))
        self.frame_177.setFrameShape(QFrame.StyledPanel)
        self.frame_177.setFrameShadow(QFrame.Raised)
        self.verticalLayout_124 = QVBoxLayout(self.frame_177)
        self.verticalLayout_124.setSpacing(0)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.label_cpf_consulta_as = QLabel(self.frame_177)
        self.label_cpf_consulta_as.setObjectName(u"label_cpf_consulta_as")
        self.label_cpf_consulta_as.setMaximumSize(QSize(180, 16777215))
        self.label_cpf_consulta_as.setFont(font)

        self.verticalLayout_124.addWidget(self.label_cpf_consulta_as)

        self.input_cpf_consulta_as = QLineEdit(self.frame_177)
        self.input_cpf_consulta_as.setObjectName(u"input_cpf_consulta_as")
        self.input_cpf_consulta_as.setMinimumSize(QSize(170, 30))
        self.input_cpf_consulta_as.setMaximumSize(QSize(170, 30))
        self.input_cpf_consulta_as.setFont(font)

        self.verticalLayout_124.addWidget(self.input_cpf_consulta_as)


        self.horizontalLayout_70.addWidget(self.frame_177)

        self.frame_182 = QFrame(self.frame_173)
        self.frame_182.setObjectName(u"frame_182")
        self.frame_182.setMaximumSize(QSize(300, 16777215))
        self.frame_182.setFrameShape(QFrame.StyledPanel)
        self.frame_182.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_70.addWidget(self.frame_182)


        self.verticalLayout_122.addWidget(self.frame_173)

        self.frame_174 = QFrame(self.frame_169)
        self.frame_174.setObjectName(u"frame_174")
        self.frame_174.setFrameShape(QFrame.StyledPanel)
        self.frame_174.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_174)
        self.horizontalLayout_71.setSpacing(5)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(30, 0, 30, 0)
        self.frame_178 = QFrame(self.frame_174)
        self.frame_178.setObjectName(u"frame_178")
        self.frame_178.setMaximumSize(QSize(160, 16777215))
        self.frame_178.setFrameShape(QFrame.StyledPanel)
        self.frame_178.setFrameShadow(QFrame.Raised)
        self.verticalLayout_126 = QVBoxLayout(self.frame_178)
        self.verticalLayout_126.setSpacing(0)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.verticalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.label_nascimento_consulta_as = QLabel(self.frame_178)
        self.label_nascimento_consulta_as.setObjectName(u"label_nascimento_consulta_as")
        self.label_nascimento_consulta_as.setMaximumSize(QSize(160, 16777215))
        self.label_nascimento_consulta_as.setFont(font)

        self.verticalLayout_126.addWidget(self.label_nascimento_consulta_as)

        self.input_nascimento_consulta_as = QLineEdit(self.frame_178)
        self.input_nascimento_consulta_as.setObjectName(u"input_nascimento_consulta_as")
        self.input_nascimento_consulta_as.setMaximumSize(QSize(150, 30))
        self.input_nascimento_consulta_as.setFont(font)

        self.verticalLayout_126.addWidget(self.input_nascimento_consulta_as)


        self.horizontalLayout_71.addWidget(self.frame_178)

        self.frame_179 = QFrame(self.frame_174)
        self.frame_179.setObjectName(u"frame_179")
        self.frame_179.setMaximumSize(QSize(240, 16777215))
        self.frame_179.setFrameShape(QFrame.StyledPanel)
        self.frame_179.setFrameShadow(QFrame.Raised)
        self.verticalLayout_127 = QVBoxLayout(self.frame_179)
        self.verticalLayout_127.setSpacing(0)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.verticalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.label_cidade_consulta_as = QLabel(self.frame_179)
        self.label_cidade_consulta_as.setObjectName(u"label_cidade_consulta_as")
        self.label_cidade_consulta_as.setFont(font)

        self.verticalLayout_127.addWidget(self.label_cidade_consulta_as)

        self.input_cidade_consulta_as = QLineEdit(self.frame_179)
        self.input_cidade_consulta_as.setObjectName(u"input_cidade_consulta_as")
        self.input_cidade_consulta_as.setMinimumSize(QSize(230, 30))
        self.input_cidade_consulta_as.setMaximumSize(QSize(230, 30))
        self.input_cidade_consulta_as.setFont(font)

        self.verticalLayout_127.addWidget(self.input_cidade_consulta_as)


        self.horizontalLayout_71.addWidget(self.frame_179)

        self.frame_180 = QFrame(self.frame_174)
        self.frame_180.setObjectName(u"frame_180")
        self.frame_180.setMaximumSize(QSize(80, 16777215))
        self.frame_180.setFrameShape(QFrame.StyledPanel)
        self.frame_180.setFrameShadow(QFrame.Raised)
        self.verticalLayout_128 = QVBoxLayout(self.frame_180)
        self.verticalLayout_128.setSpacing(0)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.verticalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.label_estado_consulta_as = QLabel(self.frame_180)
        self.label_estado_consulta_as.setObjectName(u"label_estado_consulta_as")
        self.label_estado_consulta_as.setMaximumSize(QSize(80, 16777215))
        self.label_estado_consulta_as.setFont(font)

        self.verticalLayout_128.addWidget(self.label_estado_consulta_as)

        self.input_estado_consulta_as = QLineEdit(self.frame_180)
        self.input_estado_consulta_as.setObjectName(u"input_estado_consulta_as")
        self.input_estado_consulta_as.setMaximumSize(QSize(70, 30))
        self.input_estado_consulta_as.setFont(font)

        self.verticalLayout_128.addWidget(self.input_estado_consulta_as)


        self.horizontalLayout_71.addWidget(self.frame_180)

        self.frame_181 = QFrame(self.frame_174)
        self.frame_181.setObjectName(u"frame_181")
        self.frame_181.setMaximumSize(QSize(460, 16777215))
        self.frame_181.setFrameShape(QFrame.StyledPanel)
        self.frame_181.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_71.addWidget(self.frame_181)

        self.btn_buscar_consulta_as = QPushButton(self.frame_174)
        self.btn_buscar_consulta_as.setObjectName(u"btn_buscar_consulta_as")
        self.btn_buscar_consulta_as.setMaximumSize(QSize(50, 16777215))
        self.btn_buscar_consulta_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_buscar_consulta_as.setStyleSheet(u"background-color: #F9D9DD; border: none")
        icon18 = QIcon()
        icon18.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/marca-de-verificacao.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_buscar_consulta_as.setIcon(icon18)
        self.btn_buscar_consulta_as.setIconSize(QSize(40, 40))

        self.horizontalLayout_71.addWidget(self.btn_buscar_consulta_as)


        self.verticalLayout_122.addWidget(self.frame_174)


        self.horizontalLayout_68.addWidget(self.frame_169)

        self.horizontalLayout_68.setStretch(0, 1)
        self.horizontalLayout_68.setStretch(1, 3)

        self.verticalLayout_117.addWidget(self.frame_166)

        self.frame_167 = QFrame(self.page_consulta_as)
        self.frame_167.setObjectName(u"frame_167")
        self.frame_167.setFrameShape(QFrame.StyledPanel)
        self.frame_167.setFrameShadow(QFrame.Raised)
        self.verticalLayout_129 = QVBoxLayout(self.frame_167)
        self.verticalLayout_129.setSpacing(0)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.verticalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_167)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_consulta_antes = QWidget()
        self.page_consulta_antes.setObjectName(u"page_consulta_antes")
        self.stackedWidget.addWidget(self.page_consulta_antes)
        self.page_consulta_depois = QWidget()
        self.page_consulta_depois.setObjectName(u"page_consulta_depois")
        self.page_consulta_depois.setStyleSheet(u"QLabel{margin-left: 0.25em}")
        self.verticalLayout_130 = QVBoxLayout(self.page_consulta_depois)
        self.verticalLayout_130.setSpacing(0)
        self.verticalLayout_130.setObjectName(u"verticalLayout_130")
        self.verticalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.frame_183 = QFrame(self.page_consulta_depois)
        self.frame_183.setObjectName(u"frame_183")
        self.frame_183.setStyleSheet(u"QLineEdit{color: #000;}\n"
"QLabel{margin-left: 0.25em;color: #000;}")
        self.frame_183.setFrameShape(QFrame.StyledPanel)
        self.frame_183.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_183)
        self.horizontalLayout_72.setSpacing(5)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(30, 0, 0, 0)
        self.frame_185 = QFrame(self.frame_183)
        self.frame_185.setObjectName(u"frame_185")
        self.frame_185.setMaximumSize(QSize(160, 16777215))
        self.frame_185.setFrameShape(QFrame.StyledPanel)
        self.frame_185.setFrameShadow(QFrame.Raised)
        self.verticalLayout_131 = QVBoxLayout(self.frame_185)
        self.verticalLayout_131.setSpacing(0)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.label_matricula_consulta_as_2 = QLabel(self.frame_185)
        self.label_matricula_consulta_as_2.setObjectName(u"label_matricula_consulta_as_2")
        self.label_matricula_consulta_as_2.setMaximumSize(QSize(160, 16777215))
        self.label_matricula_consulta_as_2.setFont(font)

        self.verticalLayout_131.addWidget(self.label_matricula_consulta_as_2)

        self.input_matricula_consulta_as_2 = QLineEdit(self.frame_185)
        self.input_matricula_consulta_as_2.setObjectName(u"input_matricula_consulta_as_2")
        self.input_matricula_consulta_as_2.setMaximumSize(QSize(150, 30))
        self.input_matricula_consulta_as_2.setFont(font)

        self.verticalLayout_131.addWidget(self.input_matricula_consulta_as_2)


        self.horizontalLayout_72.addWidget(self.frame_185)

        self.frame_186 = QFrame(self.frame_183)
        self.frame_186.setObjectName(u"frame_186")
        self.frame_186.setMaximumSize(QSize(460, 16777215))
        self.frame_186.setFrameShape(QFrame.StyledPanel)
        self.frame_186.setFrameShadow(QFrame.Raised)
        self.verticalLayout_132 = QVBoxLayout(self.frame_186)
        self.verticalLayout_132.setSpacing(0)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.verticalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.label_nome_usuario_consulta_as = QLabel(self.frame_186)
        self.label_nome_usuario_consulta_as.setObjectName(u"label_nome_usuario_consulta_as")
        self.label_nome_usuario_consulta_as.setMaximumSize(QSize(460, 16777215))
        self.label_nome_usuario_consulta_as.setFont(font)

        self.verticalLayout_132.addWidget(self.label_nome_usuario_consulta_as)

        self.input_nome_usuario_consulta_as = QLineEdit(self.frame_186)
        self.input_nome_usuario_consulta_as.setObjectName(u"input_nome_usuario_consulta_as")
        self.input_nome_usuario_consulta_as.setMinimumSize(QSize(450, 0))
        self.input_nome_usuario_consulta_as.setMaximumSize(QSize(450, 30))
        self.input_nome_usuario_consulta_as.setFont(font)

        self.verticalLayout_132.addWidget(self.input_nome_usuario_consulta_as)


        self.horizontalLayout_72.addWidget(self.frame_186)

        self.frame_187 = QFrame(self.frame_183)
        self.frame_187.setObjectName(u"frame_187")
        self.frame_187.setMaximumSize(QSize(180, 16777215))
        self.frame_187.setFrameShape(QFrame.StyledPanel)
        self.frame_187.setFrameShadow(QFrame.Raised)
        self.verticalLayout_133 = QVBoxLayout(self.frame_187)
        self.verticalLayout_133.setSpacing(0)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.verticalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.label_cpf_consulta_as_2 = QLabel(self.frame_187)
        self.label_cpf_consulta_as_2.setObjectName(u"label_cpf_consulta_as_2")
        self.label_cpf_consulta_as_2.setMaximumSize(QSize(180, 16777215))
        self.label_cpf_consulta_as_2.setFont(font)

        self.verticalLayout_133.addWidget(self.label_cpf_consulta_as_2)

        self.input_cpf_consulta_as_2 = QLineEdit(self.frame_187)
        self.input_cpf_consulta_as_2.setObjectName(u"input_cpf_consulta_as_2")
        self.input_cpf_consulta_as_2.setMaximumSize(QSize(170, 30))
        self.input_cpf_consulta_as_2.setFont(font)

        self.verticalLayout_133.addWidget(self.input_cpf_consulta_as_2)


        self.horizontalLayout_72.addWidget(self.frame_187)

        self.frame_188 = QFrame(self.frame_183)
        self.frame_188.setObjectName(u"frame_188")
        self.frame_188.setMaximumSize(QSize(160, 16777215))
        self.frame_188.setFrameShape(QFrame.StyledPanel)
        self.frame_188.setFrameShadow(QFrame.Raised)
        self.verticalLayout_134 = QVBoxLayout(self.frame_188)
        self.verticalLayout_134.setSpacing(0)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.verticalLayout_134.setContentsMargins(0, 0, 0, 0)
        self.label_ultima_consulta_consulta_as = QLabel(self.frame_188)
        self.label_ultima_consulta_consulta_as.setObjectName(u"label_ultima_consulta_consulta_as")
        self.label_ultima_consulta_consulta_as.setMaximumSize(QSize(160, 16777215))
        self.label_ultima_consulta_consulta_as.setFont(font)

        self.verticalLayout_134.addWidget(self.label_ultima_consulta_consulta_as)

        self.input_ultima_consulta_consulta_as = QLineEdit(self.frame_188)
        self.input_ultima_consulta_consulta_as.setObjectName(u"input_ultima_consulta_consulta_as")
        self.input_ultima_consulta_consulta_as.setMaximumSize(QSize(150, 30))
        self.input_ultima_consulta_consulta_as.setFont(font)

        self.verticalLayout_134.addWidget(self.input_ultima_consulta_consulta_as)


        self.horizontalLayout_72.addWidget(self.frame_188)


        self.verticalLayout_130.addWidget(self.frame_183)

        self.frame_184 = QFrame(self.page_consulta_depois)
        self.frame_184.setObjectName(u"frame_184")
        self.frame_184.setFrameShape(QFrame.StyledPanel)
        self.frame_184.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_184)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.frame_189 = QFrame(self.frame_184)
        self.frame_189.setObjectName(u"frame_189")
        self.frame_189.setStyleSheet(u"QLabel{margin-left: 0.25em}")
        self.frame_189.setFrameShape(QFrame.StyledPanel)
        self.frame_189.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_189)
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(20, 20, 0, 0)
        self.input_anotacoes_consulta_as = QTextEdit(self.frame_189)
        self.input_anotacoes_consulta_as.setObjectName(u"input_anotacoes_consulta_as")
        self.input_anotacoes_consulta_as.setMaximumSize(QSize(800, 16777215))
        self.input_anotacoes_consulta_as.setFont(font)
        self.input_anotacoes_consulta_as.setStyleSheet(u"background-color: #fff; color: #000")

        self.horizontalLayout_74.addWidget(self.input_anotacoes_consulta_as)


        self.horizontalLayout_73.addWidget(self.frame_189)

        self.frame_190 = QFrame(self.frame_184)
        self.frame_190.setObjectName(u"frame_190")
        self.frame_190.setFrameShape(QFrame.StyledPanel)
        self.frame_190.setFrameShadow(QFrame.Raised)
        self.verticalLayout_150 = QVBoxLayout(self.frame_190)
        self.verticalLayout_150.setSpacing(15)
        self.verticalLayout_150.setObjectName(u"verticalLayout_150")
        self.verticalLayout_150.setContentsMargins(0, 0, 20, 20)
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_150.addItem(self.verticalSpacer_12)

        self.btn_imprimir_consulta_as = QPushButton(self.frame_190)
        self.btn_imprimir_consulta_as.setObjectName(u"btn_imprimir_consulta_as")
        self.btn_imprimir_consulta_as.setMinimumSize(QSize(140, 40))
        self.btn_imprimir_consulta_as.setMaximumSize(QSize(140, 40))
        self.btn_imprimir_consulta_as.setFont(font11)
        self.btn_imprimir_consulta_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_imprimir_consulta_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        icon19 = QIcon()
        icon19.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/imprimir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_imprimir_consulta_as.setIcon(icon19)
        self.btn_imprimir_consulta_as.setIconSize(QSize(25, 25))

        self.verticalLayout_150.addWidget(self.btn_imprimir_consulta_as)

        self.btn_alterar_consulta_as = QPushButton(self.frame_190)
        self.btn_alterar_consulta_as.setObjectName(u"btn_alterar_consulta_as")
        self.btn_alterar_consulta_as.setMinimumSize(QSize(140, 40))
        self.btn_alterar_consulta_as.setMaximumSize(QSize(140, 40))
        self.btn_alterar_consulta_as.setFont(font11)
        self.btn_alterar_consulta_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_consulta_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        self.btn_alterar_consulta_as.setIcon(icon10)
        self.btn_alterar_consulta_as.setIconSize(QSize(25, 25))

        self.verticalLayout_150.addWidget(self.btn_alterar_consulta_as)

        self.btn_concluir_consulta_as = QPushButton(self.frame_190)
        self.btn_concluir_consulta_as.setObjectName(u"btn_concluir_consulta_as")
        self.btn_concluir_consulta_as.setMinimumSize(QSize(140, 40))
        self.btn_concluir_consulta_as.setMaximumSize(QSize(140, 40))
        self.btn_concluir_consulta_as.setFont(font11)
        self.btn_concluir_consulta_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_concluir_consulta_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.verticalLayout_150.addWidget(self.btn_concluir_consulta_as)


        self.horizontalLayout_73.addWidget(self.frame_190)

        self.horizontalLayout_73.setStretch(0, 8)
        self.horizontalLayout_73.setStretch(1, 1)

        self.verticalLayout_130.addWidget(self.frame_184)

        self.verticalLayout_130.setStretch(0, 1)
        self.verticalLayout_130.setStretch(1, 8)
        self.stackedWidget.addWidget(self.page_consulta_depois)

        self.verticalLayout_129.addWidget(self.stackedWidget)

        self.frame_221 = QFrame(self.frame_167)
        self.frame_221.setObjectName(u"frame_221")
        self.frame_221.setFrameShape(QFrame.StyledPanel)
        self.frame_221.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_221)
        self.horizontalLayout_75.setSpacing(20)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(20, 0, 0, 0)
        self.btn_voltar_consulta_as = QPushButton(self.frame_221)
        self.btn_voltar_consulta_as.setObjectName(u"btn_voltar_consulta_as")
        self.btn_voltar_consulta_as.setMinimumSize(QSize(100, 40))
        self.btn_voltar_consulta_as.setMaximumSize(QSize(100, 40))
        self.btn_voltar_consulta_as.setFont(font11)
        self.btn_voltar_consulta_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_consulta_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout_75.addWidget(self.btn_voltar_consulta_as)

        self.horizontalSpacer_54 = QSpacerItem(1413, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_75.addItem(self.horizontalSpacer_54)


        self.verticalLayout_129.addWidget(self.frame_221)

        self.verticalLayout_129.setStretch(0, 14)
        self.verticalLayout_129.setStretch(1, 2)

        self.verticalLayout_117.addWidget(self.frame_167)

        self.verticalLayout_117.setStretch(0, 1)
        self.verticalLayout_117.setStretch(1, 2)
        self.verticalLayout_117.setStretch(2, 8)
        self.stackedWidget_2.addWidget(self.page_consulta_as)
        self.page_relatorios_as = QWidget()
        self.page_relatorios_as.setObjectName(u"page_relatorios_as")
        self.verticalLayout_151 = QVBoxLayout(self.page_relatorios_as)
        self.verticalLayout_151.setSpacing(0)
        self.verticalLayout_151.setObjectName(u"verticalLayout_151")
        self.verticalLayout_151.setContentsMargins(0, 0, 0, 0)
        self.frame_222 = QFrame(self.page_relatorios_as)
        self.frame_222.setObjectName(u"frame_222")
        self.frame_222.setFrameShape(QFrame.StyledPanel)
        self.frame_222.setFrameShadow(QFrame.Raised)
        self.frame_224 = QFrame(self.frame_222)
        self.frame_224.setObjectName(u"frame_224")
        self.frame_224.setGeometry(QRect(10, 96, 1600, 150))
        self.frame_224.setMinimumSize(QSize(1600, 150))
        self.frame_224.setMaximumSize(QSize(1600, 150))
        self.frame_224.setFrameShape(QFrame.StyledPanel)
        self.frame_224.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_224)
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_74 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_74)

        self.frame_227 = QFrame(self.frame_224)
        self.frame_227.setObjectName(u"frame_227")
        self.frame_227.setMinimumSize(QSize(800, 130))
        self.frame_227.setMaximumSize(QSize(1580, 130))
        self.frame_227.setFrameShape(QFrame.StyledPanel)
        self.frame_227.setFrameShadow(QFrame.Raised)
        self.verticalLayout_155 = QVBoxLayout(self.frame_227)
        self.verticalLayout_155.setObjectName(u"verticalLayout_155")
        self.frame_228 = QFrame(self.frame_227)
        self.frame_228.setObjectName(u"frame_228")
        self.frame_228.setMinimumSize(QSize(870, 60))
        self.frame_228.setMaximumSize(QSize(870, 60))
        self.frame_228.setFrameShape(QFrame.StyledPanel)
        self.frame_228.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_228)
        self.horizontalLayout_84.setSpacing(0)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_76 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_84.addItem(self.horizontalSpacer_76)

        self.frame_243 = QFrame(self.frame_228)
        self.frame_243.setObjectName(u"frame_243")
        self.frame_243.setMinimumSize(QSize(125, 60))
        self.frame_243.setMaximumSize(QSize(120, 60))
        self.frame_243.setFrameShape(QFrame.StyledPanel)
        self.frame_243.setFrameShadow(QFrame.Raised)
        self.verticalLayout_1601 = QVBoxLayout(self.frame_243)
        self.verticalLayout_1601.setSpacing(0)
        self.verticalLayout_1601.setObjectName(u"verticalLayout_1601")
        self.verticalLayout_1601.setContentsMargins(0, 0, 0, 0)
        self.label_inicio_periodo_relatorio_as = QLabel(self.frame_243)
        self.label_inicio_periodo_relatorio_as.setObjectName(u"label_inicio_periodo_relatorio_as")
        self.label_inicio_periodo_relatorio_as.setMinimumSize(QSize(60, 20))
        self.label_inicio_periodo_relatorio_as.setMaximumSize(QSize(60, 20))
        self.label_inicio_periodo_relatorio_as.setFont(font13)

        self.verticalLayout_1601.addWidget(self.label_inicio_periodo_relatorio_as)

        self.input_inicio_periodo_relatorio_as = QDateEdit(self.frame_243)
        self.input_inicio_periodo_relatorio_as.setObjectName(u"input_inicio_periodo_relatorio_as")
        sizePolicy1.setHeightForWidth(self.input_inicio_periodo_relatorio_as.sizePolicy().hasHeightForWidth())
        self.input_inicio_periodo_relatorio_as.setSizePolicy(sizePolicy1)
        self.input_inicio_periodo_relatorio_as.setMinimumSize(QSize(0, 30))
        self.input_inicio_periodo_relatorio_as.setMaximumSize(QSize(120, 30))
        self.input_inicio_periodo_relatorio_as.setFont(font8)
        self.input_inicio_periodo_relatorio_as.setFocusPolicy(Qt.WheelFocus)
        self.input_inicio_periodo_relatorio_as.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.input_inicio_periodo_relatorio_as.setLayoutDirection(Qt.LeftToRight)
        self.input_inicio_periodo_relatorio_as.setAutoFillBackground(False)
        self.input_inicio_periodo_relatorio_as.setStyleSheet(u"QDateEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QDateEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_inicio_periodo_relatorio_as.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.input_inicio_periodo_relatorio_as.setAlignment(Qt.AlignCenter)
        self.input_inicio_periodo_relatorio_as.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.input_inicio_periodo_relatorio_as.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.input_inicio_periodo_relatorio_as.setCurrentSection(QDateTimeEdit.DaySection)
        self.input_inicio_periodo_relatorio_as.setCalendarPopup(False)
        self.input_inicio_periodo_relatorio_as.setCurrentSectionIndex(0)

        self.verticalLayout_1601.addWidget(self.input_inicio_periodo_relatorio_as)


        self.horizontalLayout_84.addWidget(self.frame_243)

        self.frame_2321 = QFrame(self.frame_228)
        self.frame_2321.setObjectName(u"frame_2321")
        self.frame_2321.setMinimumSize(QSize(0, 60))
        self.frame_2321.setMaximumSize(QSize(120, 60))
        self.frame_2321.setFrameShape(QFrame.StyledPanel)
        self.frame_2321.setFrameShadow(QFrame.Raised)
        self.verticalLayout_1461 = QVBoxLayout(self.frame_2321)
        self.verticalLayout_1461.setObjectName(u"verticalLayout_1461")
        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_1461.addItem(self.verticalSpacer_25)

        self.label_6 = QLabel(self.frame_2321)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(20, 20))
        self.label_6.setMaximumSize(QSize(40, 20))
        self.label_6.setFont(font13)

        self.verticalLayout_1461.addWidget(self.label_6)


        self.horizontalLayout_84.addWidget(self.frame_2321)

        self.frame_244 = QFrame(self.frame_228)
        self.frame_244.setObjectName(u"frame_244")
        self.frame_244.setMinimumSize(QSize(125, 30))
        self.frame_244.setMaximumSize(QSize(120, 60))
        self.frame_244.setFrameShape(QFrame.StyledPanel)
        self.frame_244.setFrameShadow(QFrame.Raised)
        self.verticalLayout_161 = QVBoxLayout(self.frame_244)
        self.verticalLayout_161.setSpacing(0)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalLayout_161.setContentsMargins(0, 0, 0, 0)
        self.label_final_periodo_relatorio_as = QLabel(self.frame_244)
        self.label_final_periodo_relatorio_as.setObjectName(u"label_final_periodo_relatorio_as")
        self.label_final_periodo_relatorio_as.setMinimumSize(QSize(20, 20))
        self.label_final_periodo_relatorio_as.setMaximumSize(QSize(60, 20))
        self.label_final_periodo_relatorio_as.setFont(font13)

        self.verticalLayout_161.addWidget(self.label_final_periodo_relatorio_as)

        self.input_final_periodo_relatorio_as = QDateEdit(self.frame_244)
        self.input_final_periodo_relatorio_as.setObjectName(u"input_final_periodo_relatorio_as")
        sizePolicy1.setHeightForWidth(self.input_final_periodo_relatorio_as.sizePolicy().hasHeightForWidth())
        self.input_final_periodo_relatorio_as.setSizePolicy(sizePolicy1)
        self.input_final_periodo_relatorio_as.setMinimumSize(QSize(0, 30))
        self.input_final_periodo_relatorio_as.setMaximumSize(QSize(120, 30))
        self.input_final_periodo_relatorio_as.setFont(font8)
        self.input_final_periodo_relatorio_as.setFocusPolicy(Qt.WheelFocus)
        self.input_final_periodo_relatorio_as.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.input_final_periodo_relatorio_as.setLayoutDirection(Qt.LeftToRight)
        self.input_final_periodo_relatorio_as.setAutoFillBackground(False)
        self.input_final_periodo_relatorio_as.setStyleSheet(u"QDateEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QDateEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_final_periodo_relatorio_as.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.input_final_periodo_relatorio_as.setAlignment(Qt.AlignCenter)
        self.input_final_periodo_relatorio_as.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.input_final_periodo_relatorio_as.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.input_final_periodo_relatorio_as.setCurrentSection(QDateTimeEdit.DaySection)
        self.input_final_periodo_relatorio_as.setCalendarPopup(False)
        self.input_final_periodo_relatorio_as.setCurrentSectionIndex(0)

        self.verticalLayout_161.addWidget(self.input_final_periodo_relatorio_as)


        self.horizontalLayout_84.addWidget(self.frame_244)

        self.frame_245 = QFrame(self.frame_228)
        self.frame_245.setObjectName(u"frame_245")
        self.frame_245.setMinimumSize(QSize(130, 55))
        self.frame_245.setMaximumSize(QSize(130, 55))
        self.frame_245.setFrameShape(QFrame.StyledPanel)
        self.frame_245.setFrameShadow(QFrame.Raised)
        self.verticalLayout_166 = QVBoxLayout(self.frame_245)
        self.verticalLayout_166.setSpacing(0)
        self.verticalLayout_166.setObjectName(u"verticalLayout_166")
        self.verticalLayout_166.setContentsMargins(0, 0, 0, 0)
        self.label_escolha_relatorio_as = QLabel(self.frame_245)
        self.label_escolha_relatorio_as.setObjectName(u"label_escolha_relatorio_as")
        self.label_escolha_relatorio_as.setMinimumSize(QSize(100, 20))
        self.label_escolha_relatorio_as.setMaximumSize(QSize(76, 25))
        self.label_escolha_relatorio_as.setFont(font13)

        self.verticalLayout_166.addWidget(self.label_escolha_relatorio_as)

        self.input_escolha_relatorio_as = QComboBox(self.frame_245)
        self.input_escolha_relatorio_as.addItem("")
        self.input_escolha_relatorio_as.addItem("")
        self.input_escolha_relatorio_as.addItem("")
        self.input_escolha_relatorio_as.addItem("")
        self.input_escolha_relatorio_as.addItem("")
        self.input_escolha_relatorio_as.addItem("")
        self.input_escolha_relatorio_as.addItem("")
        self.input_escolha_relatorio_as.addItem("")
        self.input_escolha_relatorio_as.setObjectName(u"input_escolha_relatorio_as")
        self.input_escolha_relatorio_as.setMinimumSize(QSize(0, 30))
        self.input_escolha_relatorio_as.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_166.addWidget(self.input_escolha_relatorio_as)


        self.horizontalLayout_84.addWidget(self.frame_245)

        self.frame_2371 = QFrame(self.frame_228)
        self.frame_2371.setObjectName(u"frame_2371")
        self.frame_2371.setEnabled(False)
        self.frame_2371.setMinimumSize(QSize(130, 60))
        self.frame_2371.setMaximumSize(QSize(130, 60))
        self.frame_2371.setFrameShape(QFrame.StyledPanel)
        self.frame_2371.setFrameShadow(QFrame.Raised)
        self.verticalLayout_153 = QVBoxLayout(self.frame_2371)
        self.verticalLayout_153.setSpacing(0)
        self.verticalLayout_153.setObjectName(u"verticalLayout_153")
        self.verticalLayout_153.setContentsMargins(0, 0, 0, 0)
        self.label_idade_relatorio_as = QLabel(self.frame_2371)
        self.label_idade_relatorio_as.setObjectName(u"label_idade_relatorio_as")
        self.label_idade_relatorio_as.setEnabled(False)
        self.label_idade_relatorio_as.setMinimumSize(QSize(40, 15))
        self.label_idade_relatorio_as.setMaximumSize(QSize(40, 15))
        self.label_idade_relatorio_as.setSizeIncrement(QSize(0, 20))
        self.label_idade_relatorio_as.setFont(font13)

        self.verticalLayout_153.addWidget(self.label_idade_relatorio_as)

        self.frame_246 = QFrame(self.frame_2371)
        self.frame_246.setObjectName(u"frame_246")
        self.frame_246.setEnabled(False)
        self.frame_246.setMinimumSize(QSize(127, 35))
        self.frame_246.setMaximumSize(QSize(110, 35))
        self.frame_246.setSizeIncrement(QSize(0, 20))
        font14 = QFont()
        font14.setFamilies([u"Abel"])
        font14.setPointSize(11)
        font14.setKerning(False)
        self.frame_246.setFont(font14)
        self.frame_246.setFrameShape(QFrame.StyledPanel)
        self.frame_246.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_246)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.input_idade_inicial_relatorio_as = QLineEdit(self.frame_246)
        self.input_idade_inicial_relatorio_as.setObjectName(u"input_idade_inicial_relatorio_as")
        self.input_idade_inicial_relatorio_as.setEnabled(False)
        self.input_idade_inicial_relatorio_as.setMinimumSize(QSize(45, 25))
        self.input_idade_inicial_relatorio_as.setMaximumSize(QSize(34, 16))
        self.input_idade_inicial_relatorio_as.setStyleSheet(u"\n"
"    border: none;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"\n"
"")

        self.horizontalLayout_11.addWidget(self.input_idade_inicial_relatorio_as)

        self.label_a_relatorio_as = QLabel(self.frame_246)
        self.label_a_relatorio_as.setObjectName(u"label_a_relatorio_as")
        self.label_a_relatorio_as.setMinimumSize(QSize(16, 16))
        self.label_a_relatorio_as.setMaximumSize(QSize(16, 16))
        font15 = QFont()
        font15.setFamilies([u"Abel"])
        font15.setPointSize(13)
        self.label_a_relatorio_as.setFont(font15)
        self.label_a_relatorio_as.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.label_a_relatorio_as)

        self.input_idade_final_relatorio_as = QLineEdit(self.frame_246)
        self.input_idade_final_relatorio_as.setObjectName(u"input_idade_final_relatorio_as")
        self.input_idade_final_relatorio_as.setEnabled(False)
        self.input_idade_final_relatorio_as.setMinimumSize(QSize(45, 25))
        self.input_idade_final_relatorio_as.setMaximumSize(QSize(34, 16))
        self.input_idade_final_relatorio_as.setStyleSheet(u"\n"
"    border: none;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"\n"
"")

        self.horizontalLayout_11.addWidget(self.input_idade_final_relatorio_as)


        self.verticalLayout_153.addWidget(self.frame_246)


        self.horizontalLayout_84.addWidget(self.frame_2371)

        self.frame_249 = QFrame(self.frame_228)
        self.frame_249.setObjectName(u"frame_249")
        self.frame_249.setEnabled(False)
        self.frame_249.setMinimumSize(QSize(100, 0))
        self.frame_249.setMaximumSize(QSize(100, 16777215))
        self.frame_249.setFrameShape(QFrame.StyledPanel)
        self.frame_249.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_84.addWidget(self.frame_249)

        self.frame_391 = QFrame(self.frame_228)
        self.frame_391.setObjectName(u"frame_391")
        self.frame_391.setMinimumSize(QSize(50, 50))
        self.frame_391.setMaximumSize(QSize(50, 50))
        self.frame_391.setFont(font13)
        self.frame_391.setFrameShape(QFrame.StyledPanel)
        self.frame_391.setFrameShadow(QFrame.Raised)
        self.verticalLayout_152 = QVBoxLayout(self.frame_391)
        self.verticalLayout_152.setObjectName(u"verticalLayout_152")
        self.btn_buscar_relatorio_as = QPushButton(self.frame_391)
        self.btn_buscar_relatorio_as.setObjectName(u"btn_buscar_relatorio_as")
        sizePolicy2.setHeightForWidth(self.btn_buscar_relatorio_as.sizePolicy().hasHeightForWidth())
        self.btn_buscar_relatorio_as.setSizePolicy(sizePolicy2)
        self.btn_buscar_relatorio_as.setMinimumSize(QSize(40, 40))
        self.btn_buscar_relatorio_as.setMaximumSize(QSize(40, 40))
        self.btn_buscar_relatorio_as.setStyleSheet(u"QPushButton{\n"
"        background: rgb(243, 185, 191);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 20px;\n"
"		border-bottom-right-radius: 20px;\n"
"		border-bottom-left-radius: 20px;\n"
"		border-top-left-radius: 20px;\n"
"        color: rgb(249, 217, 221);   \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        background: rgb(255, 194, 201);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 20px;\n"
"		border-bottom-right-radius: 20px;\n"
"		border-bottom-right-radius: 20px;\n"
"		border-bottom-left-radius: 20px;\n"
"        color: rgb(249, 217, 221); \n"
"		border-bottom-right-radius: 20px;\n"
"		border-bottom-left-radius: 20px;  \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"        background: rgb(180, 106, 102);\n"
"        border: 2px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 20px;\n"
"		border-bottom-right-radius: 20px;\n"
"        colo"
                        "r: rgb(249, 217, 221);   \n"
"}")
        self.btn_buscar_relatorio_as.setIcon(icon12)

        self.verticalLayout_152.addWidget(self.btn_buscar_relatorio_as)


        self.horizontalLayout_84.addWidget(self.frame_391)

        self.horizontalSpacer_77 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_84.addItem(self.horizontalSpacer_77)


        self.verticalLayout_155.addWidget(self.frame_228)

        self.frame_229 = QFrame(self.frame_227)
        self.frame_229.setObjectName(u"frame_229")
        self.frame_229.setMinimumSize(QSize(0, 60))
        self.frame_229.setMaximumSize(QSize(870, 60))
        self.frame_229.setFrameShape(QFrame.StyledPanel)
        self.frame_229.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_229)
        self.horizontalLayout_85.setSpacing(0)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_78 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_78)

        self.input_buscar_dados_relatorio_as = QLineEdit(self.frame_229)
        self.input_buscar_dados_relatorio_as.setObjectName(u"input_buscar_dados_relatorio_as")
        self.input_buscar_dados_relatorio_as.setMinimumSize(QSize(700, 30))
        self.input_buscar_dados_relatorio_as.setMaximumSize(QSize(700, 30))

        self.horizontalLayout_85.addWidget(self.input_buscar_dados_relatorio_as)

        self.horizontalSpacer_79 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_79)


        self.verticalLayout_155.addWidget(self.frame_229)


        self.horizontalLayout_83.addWidget(self.frame_227)

        self.horizontalSpacer_75 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_75)

        self.frame_226 = QFrame(self.frame_222)
        self.frame_226.setObjectName(u"frame_226")
        self.frame_226.setGeometry(QRect(10, 252, 1600, 570))
        self.frame_226.setMinimumSize(QSize(1600, 570))
        self.frame_226.setMaximumSize(QSize(1600, 570))
        self.frame_226.setFrameShape(QFrame.StyledPanel)
        self.frame_226.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_226)
        self.horizontalLayout_86.setSpacing(0)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_80 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_80)

        self.frame_238 = QFrame(self.frame_226)
        self.frame_238.setObjectName(u"frame_238")
        self.frame_238.setMinimumSize(QSize(1230, 540))
        self.frame_238.setFrameShape(QFrame.StyledPanel)
        self.frame_238.setFrameShadow(QFrame.Raised)
        self.verticalLayout_310 = QVBoxLayout(self.frame_238)
        self.verticalLayout_310.setSpacing(0)
        self.verticalLayout_310.setObjectName(u"verticalLayout_310")
        self.verticalLayout_310.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_relatorio_as = QTableWidget(self.frame_238)
        if (self.tableWidget_relatorio_as.columnCount() < 1):
            self.tableWidget_relatorio_as.setColumnCount(1)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_relatorio_as.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        if (self.tableWidget_relatorio_as.rowCount() < 1):
            self.tableWidget_relatorio_as.setRowCount(1)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_relatorio_as.setVerticalHeaderItem(0, __qtablewidgetitem20)
        self.tableWidget_relatorio_as.setObjectName(u"tableWidget_relatorio_as")
        self.tableWidget_relatorio_as.setMinimumSize(QSize(1200, 530))
        self.tableWidget_relatorio_as.setMaximumSize(QSize(1200, 530))

        self.verticalLayout_310.addWidget(self.tableWidget_relatorio_as)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_310.addItem(self.verticalSpacer_23)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_310.addItem(self.verticalSpacer_24)


        self.horizontalLayout_86.addWidget(self.frame_238)

        self.frame_242 = QFrame(self.frame_226)
        self.frame_242.setObjectName(u"frame_242")
        self.frame_242.setMinimumSize(QSize(150, 540))
        self.frame_242.setMaximumSize(QSize(150, 540))
        self.frame_242.setFrameShape(QFrame.StyledPanel)
        self.frame_242.setFrameShadow(QFrame.Raised)
        self.verticalLayout_309 = QVBoxLayout(self.frame_242)
        self.verticalLayout_309.setSpacing(0)
        self.verticalLayout_309.setObjectName(u"verticalLayout_309")
        self.verticalLayout_309.setContentsMargins(0, 0, 0, 0)
        self.frame_251 = QFrame(self.frame_242)
        self.frame_251.setObjectName(u"frame_251")
        self.frame_251.setMinimumSize(QSize(130, 250))
        self.frame_251.setMaximumSize(QSize(130, 280))
        self.frame_251.setFrameShape(QFrame.StyledPanel)
        self.frame_251.setFrameShadow(QFrame.Raised)
        self.verticalLayout_308 = QVBoxLayout(self.frame_251)
        self.verticalLayout_308.setSpacing(15)
        self.verticalLayout_308.setObjectName(u"verticalLayout_308")
        self.verticalLayout_308.setContentsMargins(0, 0, 20, 20)
        self.btn_gerar_excel_relatorio_as = QPushButton(self.frame_251)
        self.btn_gerar_excel_relatorio_as.setObjectName(u"btn_gerar_excel_relatorio_as")
        sizePolicy2.setHeightForWidth(self.btn_gerar_excel_relatorio_as.sizePolicy().hasHeightForWidth())
        self.btn_gerar_excel_relatorio_as.setSizePolicy(sizePolicy2)
        self.btn_gerar_excel_relatorio_as.setMinimumSize(QSize(125, 40))
        self.btn_gerar_excel_relatorio_as.setMaximumSize(QSize(40, 40))
        font16 = QFont()
        font16.setFamilies([u"Abel"])
        font16.setPointSize(15)
        self.btn_gerar_excel_relatorio_as.setFont(font16)
        self.btn_gerar_excel_relatorio_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        self.btn_gerar_excel_relatorio_as.setIcon(icon12)

        self.verticalLayout_308.addWidget(self.btn_gerar_excel_relatorio_as)

        self.btn_gerar_pdf_relatorio_as = QPushButton(self.frame_251)
        self.btn_gerar_pdf_relatorio_as.setObjectName(u"btn_gerar_pdf_relatorio_as")
        sizePolicy2.setHeightForWidth(self.btn_gerar_pdf_relatorio_as.sizePolicy().hasHeightForWidth())
        self.btn_gerar_pdf_relatorio_as.setSizePolicy(sizePolicy2)
        self.btn_gerar_pdf_relatorio_as.setMinimumSize(QSize(125, 40))
        self.btn_gerar_pdf_relatorio_as.setMaximumSize(QSize(40, 40))
        self.btn_gerar_pdf_relatorio_as.setFont(font16)
        self.btn_gerar_pdf_relatorio_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        self.btn_gerar_pdf_relatorio_as.setIcon(icon12)

        self.verticalLayout_308.addWidget(self.btn_gerar_pdf_relatorio_as)

        self.btn_imprimir_relatorio_as = QPushButton(self.frame_251)
        self.btn_imprimir_relatorio_as.setObjectName(u"btn_imprimir_relatorio_as")
        self.btn_imprimir_relatorio_as.setMinimumSize(QSize(125, 40))
        self.btn_imprimir_relatorio_as.setMaximumSize(QSize(140, 40))
        self.btn_imprimir_relatorio_as.setFont(font)
        self.btn_imprimir_relatorio_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_imprimir_relatorio_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        self.btn_imprimir_relatorio_as.setIcon(icon19)
        self.btn_imprimir_relatorio_as.setIconSize(QSize(25, 25))

        self.verticalLayout_308.addWidget(self.btn_imprimir_relatorio_as)

        self.btn_excluir_relatorio_as = QPushButton(self.frame_251)
        self.btn_excluir_relatorio_as.setObjectName(u"btn_excluir_relatorio_as")
        self.btn_excluir_relatorio_as.setMinimumSize(QSize(125, 40))
        self.btn_excluir_relatorio_as.setMaximumSize(QSize(125, 40))
        self.btn_excluir_relatorio_as.setFont(font11)
        self.btn_excluir_relatorio_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_relatorio_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.verticalLayout_308.addWidget(self.btn_excluir_relatorio_as)


        self.verticalLayout_309.addWidget(self.frame_251)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_309.addItem(self.verticalSpacer_31)


        self.horizontalLayout_86.addWidget(self.frame_242)

        self.frame_248 = QFrame(self.frame_222)
        self.frame_248.setObjectName(u"frame_248")
        self.frame_248.setGeometry(QRect(10, 828, 120, 50))
        self.frame_248.setMinimumSize(QSize(120, 45))
        self.frame_248.setMaximumSize(QSize(120, 50))
        self.frame_248.setFrameShape(QFrame.StyledPanel)
        self.frame_248.setFrameShadow(QFrame.Raised)
        self.verticalLayout_154 = QVBoxLayout(self.frame_248)
        self.verticalLayout_154.setObjectName(u"verticalLayout_154")
        self.btn_voltar_relatorios_as = QPushButton(self.frame_248)
        self.btn_voltar_relatorios_as.setObjectName(u"btn_voltar_relatorios_as")
        self.btn_voltar_relatorios_as.setMinimumSize(QSize(100, 40))
        self.btn_voltar_relatorios_as.setMaximumSize(QSize(100, 40))
        self.btn_voltar_relatorios_as.setFont(font11)
        self.btn_voltar_relatorios_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_relatorios_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.verticalLayout_154.addWidget(self.btn_voltar_relatorios_as)

        self.frame_223 = QFrame(self.frame_222)
        self.frame_223.setObjectName(u"frame_223")
        self.frame_223.setGeometry(QRect(0, 0, 1826, 80))
        self.frame_223.setMinimumSize(QSize(1826, 80))
        self.frame_223.setMaximumSize(QSize(1600, 80))
        self.frame_223.setStyleSheet(u"background-color: rgb(243, 185, 191);")
        self.frame_223.setFrameShape(QFrame.StyledPanel)
        self.frame_223.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_223)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_82.addItem(self.horizontalSpacer_55)

        self.frame_225 = QFrame(self.frame_223)
        self.frame_225.setObjectName(u"frame_225")
        self.frame_225.setMinimumSize(QSize(467, 61))
        self.frame_225.setMaximumSize(QSize(300, 16777215))
        self.frame_225.setFrameShape(QFrame.StyledPanel)
        self.frame_225.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_225)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.label_relatorio_as = QLabel(self.frame_225)
        self.label_relatorio_as.setObjectName(u"label_relatorio_as")
        self.label_relatorio_as.setMinimumSize(QSize(300, 0))
        self.label_relatorio_as.setMaximumSize(QSize(300, 16777215))
        font17 = QFont()
        font17.setFamilies([u"Abel"])
        font17.setPointSize(35)
        self.label_relatorio_as.setFont(font17)
        self.label_relatorio_as.setStyleSheet(u"background-color: rgb(243, 185, 191);\n"
"color: rgb(236, 132, 140);")

        self.horizontalLayout_87.addWidget(self.label_relatorio_as)


        self.horizontalLayout_82.addWidget(self.frame_225)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_82.addItem(self.horizontalSpacer_56)


        self.verticalLayout_151.addWidget(self.frame_222)

        self.stackedWidget_2.addWidget(self.page_relatorios_as)
        self.page_agenda_as = QWidget()
        self.page_agenda_as.setObjectName(u"page_agenda_as")
        self.verticalLayout_109 = QVBoxLayout(self.page_agenda_as)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.frame_247 = QFrame(self.page_agenda_as)
        self.frame_247.setObjectName(u"frame_247")
        self.frame_247.setStyleSheet(u"background-color: #F3B9BF")
        self.frame_247.setFrameShape(QFrame.StyledPanel)
        self.frame_247.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_247)
        self.horizontalLayout_91.setSpacing(0)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_247)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"color: #EC848C")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_91.addWidget(self.label_10)


        self.verticalLayout_109.addWidget(self.frame_247)

        self.frame_264 = QFrame(self.page_agenda_as)
        self.frame_264.setObjectName(u"frame_264")
        self.frame_264.setFrameShape(QFrame.StyledPanel)
        self.frame_264.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_264)
        self.horizontalLayout_93.setSpacing(0)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.frame_266 = QFrame(self.frame_264)
        self.frame_266.setObjectName(u"frame_266")
        self.frame_266.setFrameShape(QFrame.StyledPanel)
        self.frame_266.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_138 = QHBoxLayout(self.frame_266)
        self.horizontalLayout_138.setSpacing(0)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_91 = QSpacerItem(150, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_138.addItem(self.horizontalSpacer_91)

        self.frame_263 = QFrame(self.frame_266)
        self.frame_263.setObjectName(u"frame_263")
        self.frame_263.setMinimumSize(QSize(200, 0))
        self.frame_263.setFrameShape(QFrame.StyledPanel)
        self.frame_263.setFrameShadow(QFrame.Raised)
        self.verticalLayout_157 = QVBoxLayout(self.frame_263)
        self.verticalLayout_157.setSpacing(0)
        self.verticalLayout_157.setObjectName(u"verticalLayout_157")
        self.verticalLayout_157.setContentsMargins(0, 0, 0, 0)
        self.frame_271 = QFrame(self.frame_263)
        self.frame_271.setObjectName(u"frame_271")
        self.frame_271.setFrameShape(QFrame.StyledPanel)
        self.frame_271.setFrameShadow(QFrame.Raised)
        self.verticalLayout_158 = QVBoxLayout(self.frame_271)
        self.verticalLayout_158.setSpacing(0)
        self.verticalLayout_158.setObjectName(u"verticalLayout_158")
        self.verticalLayout_158.setContentsMargins(0, 0, 0, 0)
        self.frame_267 = QFrame(self.frame_271)
        self.frame_267.setObjectName(u"frame_267")
        self.frame_267.setFrameShape(QFrame.StyledPanel)
        self.frame_267.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_139 = QHBoxLayout(self.frame_267)
        self.horizontalLayout_139.setSpacing(0)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.horizontalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.frame_442 = QFrame(self.frame_267)
        self.frame_442.setObjectName(u"frame_442")
        self.frame_442.setFrameShape(QFrame.StyledPanel)
        self.frame_442.setFrameShadow(QFrame.Raised)
        self.verticalLayout_182 = QVBoxLayout(self.frame_442)
        self.verticalLayout_182.setObjectName(u"verticalLayout_182")
        self.label_cpf_agendamento_as = QLabel(self.frame_442)
        self.label_cpf_agendamento_as.setObjectName(u"label_cpf_agendamento_as")
        self.label_cpf_agendamento_as.setFont(font)

        self.verticalLayout_182.addWidget(self.label_cpf_agendamento_as)

        self.input_cpf_agendamento_as = QLineEdit(self.frame_442)
        self.input_cpf_agendamento_as.setObjectName(u"input_cpf_agendamento_as")
        self.input_cpf_agendamento_as.setMinimumSize(QSize(0, 30))
        self.input_cpf_agendamento_as.setMaximumSize(QSize(16777215, 30))
        self.input_cpf_agendamento_as.setFont(font)

        self.verticalLayout_182.addWidget(self.input_cpf_agendamento_as)


        self.horizontalLayout_139.addWidget(self.frame_442)

        self.btn_buscar_agendamento_as = QPushButton(self.frame_267)
        self.btn_buscar_agendamento_as.setObjectName(u"btn_buscar_agendamento_as")
        sizePolicy2.setHeightForWidth(self.btn_buscar_agendamento_as.sizePolicy().hasHeightForWidth())
        self.btn_buscar_agendamento_as.setSizePolicy(sizePolicy2)
        self.btn_buscar_agendamento_as.setMinimumSize(QSize(40, 40))
        self.btn_buscar_agendamento_as.setMaximumSize(QSize(40, 40))
        self.btn_buscar_agendamento_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_buscar_agendamento_as.setStyleSheet(u"QPushButton{\n"
"        background: rgb(243, 185, 191);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 20px;\n"
"		border-bottom-right-radius: 20px;\n"
"		border-bottom-left-radius: 20px;\n"
"		border-top-left-radius: 20px;\n"
"        color: rgb(249, 217, 221);   \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        background: rgb(255, 194, 201);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 20px;\n"
"		border-bottom-right-radius: 20px;\n"
"		border-bottom-right-radius: 20px;\n"
"		border-bottom-left-radius: 20px;\n"
"        color: rgb(249, 217, 221); \n"
"		border-bottom-right-radius: 20px;\n"
"		border-bottom-left-radius: 20px;  \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"        background: rgb(180, 106, 102);\n"
"        border: 2px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 20px;\n"
"		border-bottom-right-radius: 20px;\n"
"        colo"
                        "r: rgb(249, 217, 221);   \n"
"}")
        icon20 = QIcon()
        icon20.addFile(u"./icons/lupa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_buscar_agendamento_as.setIcon(icon20)

        self.horizontalLayout_139.addWidget(self.btn_buscar_agendamento_as)


        self.verticalLayout_158.addWidget(self.frame_267)

        self.frame_392 = QFrame(self.frame_271)
        self.frame_392.setObjectName(u"frame_392")
        self.frame_392.setFrameShape(QFrame.StyledPanel)
        self.frame_392.setFrameShadow(QFrame.Raised)
        self.verticalLayout_267 = QVBoxLayout(self.frame_392)
        self.verticalLayout_267.setObjectName(u"verticalLayout_267")
        self.label_nome_agendamento_as = QLabel(self.frame_392)
        self.label_nome_agendamento_as.setObjectName(u"label_nome_agendamento_as")
        self.label_nome_agendamento_as.setFont(font)

        self.verticalLayout_267.addWidget(self.label_nome_agendamento_as)

        self.input_nome_agendamento_as = QLineEdit(self.frame_392)
        self.input_nome_agendamento_as.setObjectName(u"input_nome_agendamento_as")
        self.input_nome_agendamento_as.setMinimumSize(QSize(0, 30))
        self.input_nome_agendamento_as.setMaximumSize(QSize(16777215, 30))
        self.input_nome_agendamento_as.setFont(font)

        self.verticalLayout_267.addWidget(self.input_nome_agendamento_as)


        self.verticalLayout_158.addWidget(self.frame_392)

        self.frame_440 = QFrame(self.frame_271)
        self.frame_440.setObjectName(u"frame_440")
        self.frame_440.setFrameShape(QFrame.StyledPanel)
        self.frame_440.setFrameShadow(QFrame.Raised)
        self.verticalLayout_307 = QVBoxLayout(self.frame_440)
        self.verticalLayout_307.setObjectName(u"verticalLayout_307")
        self.label_telefone_agendamento_as = QLabel(self.frame_440)
        self.label_telefone_agendamento_as.setObjectName(u"label_telefone_agendamento_as")
        self.label_telefone_agendamento_as.setFont(font)

        self.verticalLayout_307.addWidget(self.label_telefone_agendamento_as)

        self.input_telefone_agendamento_as = QLineEdit(self.frame_440)
        self.input_telefone_agendamento_as.setObjectName(u"input_telefone_agendamento_as")
        self.input_telefone_agendamento_as.setMinimumSize(QSize(0, 30))
        self.input_telefone_agendamento_as.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_307.addWidget(self.input_telefone_agendamento_as)


        self.verticalLayout_158.addWidget(self.frame_440)

        self.frame_441 = QFrame(self.frame_271)
        self.frame_441.setObjectName(u"frame_441")
        self.frame_441.setFrameShape(QFrame.StyledPanel)
        self.frame_441.setFrameShadow(QFrame.Raised)
        self.verticalLayout_311 = QVBoxLayout(self.frame_441)
        self.verticalLayout_311.setObjectName(u"verticalLayout_311")
        self.verticalLayout_311.setContentsMargins(0, 0, 0, 0)
        self.label_profissional_agendamento_as = QLabel(self.frame_441)
        self.label_profissional_agendamento_as.setObjectName(u"label_profissional_agendamento_as")
        self.label_profissional_agendamento_as.setFont(font)

        self.verticalLayout_311.addWidget(self.label_profissional_agendamento_as)

        self.frame_443 = QFrame(self.frame_441)
        self.frame_443.setObjectName(u"frame_443")
        self.frame_443.setFrameShape(QFrame.StyledPanel)
        self.frame_443.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_145 = QHBoxLayout(self.frame_443)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.input_profissional_as_agendamento_as = QRadioButton(self.frame_443)
        self.input_profissional_as_agendamento_as.setObjectName(u"input_profissional_as_agendamento_as")
        self.input_profissional_as_agendamento_as.setFont(font8)

        self.horizontalLayout_145.addWidget(self.input_profissional_as_agendamento_as)

        self.input_profissional_nutri_agendamento_as = QRadioButton(self.frame_443)
        self.input_profissional_nutri_agendamento_as.setObjectName(u"input_profissional_nutri_agendamento_as")
        self.input_profissional_nutri_agendamento_as.setFont(font8)

        self.horizontalLayout_145.addWidget(self.input_profissional_nutri_agendamento_as)

        self.input_profissional_psi_agendamento_as = QRadioButton(self.frame_443)
        self.input_profissional_psi_agendamento_as.setObjectName(u"input_profissional_psi_agendamento_as")
        self.input_profissional_psi_agendamento_as.setFont(font8)

        self.horizontalLayout_145.addWidget(self.input_profissional_psi_agendamento_as)


        self.verticalLayout_311.addWidget(self.frame_443)


        self.verticalLayout_158.addWidget(self.frame_441)

        self.frame_444 = QFrame(self.frame_271)
        self.frame_444.setObjectName(u"frame_444")
        self.frame_444.setFrameShape(QFrame.StyledPanel)
        self.frame_444.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_150 = QHBoxLayout(self.frame_444)
        self.horizontalLayout_150.setSpacing(0)
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.horizontalLayout_150.setContentsMargins(0, 0, 0, 0)
        self.frame_446 = QFrame(self.frame_444)
        self.frame_446.setObjectName(u"frame_446")
        self.frame_446.setMaximumSize(QSize(140, 16777215))
        self.frame_446.setFrameShape(QFrame.StyledPanel)
        self.frame_446.setFrameShadow(QFrame.Raised)
        self.verticalLayout_312 = QVBoxLayout(self.frame_446)
        self.verticalLayout_312.setSpacing(0)
        self.verticalLayout_312.setObjectName(u"verticalLayout_312")
        self.verticalLayout_312.setContentsMargins(0, 0, 0, 0)
        self.label_data_agendamento_as = QLabel(self.frame_446)
        self.label_data_agendamento_as.setObjectName(u"label_data_agendamento_as")
        self.label_data_agendamento_as.setMaximumSize(QSize(140, 16777215))
        self.label_data_agendamento_as.setFont(font)

        self.verticalLayout_312.addWidget(self.label_data_agendamento_as)

        self.input_data_agendamento_as = QDateEdit(self.frame_446)
        self.input_data_agendamento_as.setObjectName(u"input_data_agendamento_as")
        sizePolicy1.setHeightForWidth(self.input_data_agendamento_as.sizePolicy().hasHeightForWidth())
        self.input_data_agendamento_as.setSizePolicy(sizePolicy1)
        self.input_data_agendamento_as.setMinimumSize(QSize(0, 30))
        self.input_data_agendamento_as.setMaximumSize(QSize(130, 30))
        self.input_data_agendamento_as.setFont(font8)
        self.input_data_agendamento_as.setFocusPolicy(Qt.WheelFocus)
        self.input_data_agendamento_as.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.input_data_agendamento_as.setLayoutDirection(Qt.LeftToRight)
        self.input_data_agendamento_as.setAutoFillBackground(False)
        self.input_data_agendamento_as.setStyleSheet(u"QDateEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QDateEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_data_agendamento_as.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.input_data_agendamento_as.setAlignment(Qt.AlignCenter)
        self.input_data_agendamento_as.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.input_data_agendamento_as.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.input_data_agendamento_as.setCurrentSection(QDateTimeEdit.DaySection)
        self.input_data_agendamento_as.setCalendarPopup(False)
        self.input_data_agendamento_as.setCurrentSectionIndex(0)

        self.verticalLayout_312.addWidget(self.input_data_agendamento_as)


        self.horizontalLayout_150.addWidget(self.frame_446)

        self.frame_447 = QFrame(self.frame_444)
        self.frame_447.setObjectName(u"frame_447")
        self.frame_447.setMaximumSize(QSize(140, 16777215))
        self.frame_447.setFrameShape(QFrame.StyledPanel)
        self.frame_447.setFrameShadow(QFrame.Raised)
        self.verticalLayout_313 = QVBoxLayout(self.frame_447)
        self.verticalLayout_313.setSpacing(0)
        self.verticalLayout_313.setObjectName(u"verticalLayout_313")
        self.verticalLayout_313.setContentsMargins(0, 0, 0, 0)
        self.label_hora_agendamento_as = QLabel(self.frame_447)
        self.label_hora_agendamento_as.setObjectName(u"label_hora_agendamento_as")
        self.label_hora_agendamento_as.setMaximumSize(QSize(140, 16777215))
        self.label_hora_agendamento_as.setFont(font)

        self.verticalLayout_313.addWidget(self.label_hora_agendamento_as)

        self.input_hora_agendamento_as = QTimeEdit(self.frame_447)
        self.input_hora_agendamento_as.setObjectName(u"input_hora_agendamento_as")
        self.input_hora_agendamento_as.setMinimumSize(QSize(120, 30))
        self.input_hora_agendamento_as.setMaximumSize(QSize(120, 30))
        self.input_hora_agendamento_as.setFont(font)
        self.input_hora_agendamento_as.setStyleSheet(u"QTimeEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QTimeEdit:focus{outline:0; border: 2px solid #A85751}")

        self.verticalLayout_313.addWidget(self.input_hora_agendamento_as)


        self.horizontalLayout_150.addWidget(self.frame_447)


        self.verticalLayout_158.addWidget(self.frame_444)

        self.frame_445 = QFrame(self.frame_271)
        self.frame_445.setObjectName(u"frame_445")
        self.frame_445.setFrameShape(QFrame.StyledPanel)
        self.frame_445.setFrameShadow(QFrame.Raised)
        self.verticalLayout_314 = QVBoxLayout(self.frame_445)
        self.verticalLayout_314.setObjectName(u"verticalLayout_314")
        self.label_clinica_agendamento_as = QLabel(self.frame_445)
        self.label_clinica_agendamento_as.setObjectName(u"label_clinica_agendamento_as")
        self.label_clinica_agendamento_as.setFont(font)

        self.verticalLayout_314.addWidget(self.label_clinica_agendamento_as)

        self.input_clinica_agendamento_as = QLineEdit(self.frame_445)
        self.input_clinica_agendamento_as.setObjectName(u"input_clinica_agendamento_as")
        self.input_clinica_agendamento_as.setMinimumSize(QSize(0, 30))
        self.input_clinica_agendamento_as.setMaximumSize(QSize(16777215, 30))
        self.input_clinica_agendamento_as.setFont(font)

        self.verticalLayout_314.addWidget(self.input_clinica_agendamento_as)


        self.verticalLayout_158.addWidget(self.frame_445)


        self.verticalLayout_157.addWidget(self.frame_271)


        self.horizontalLayout_138.addWidget(self.frame_263)

        self.horizontalSpacer_94 = QSpacerItem(150, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_138.addItem(self.horizontalSpacer_94)


        self.horizontalLayout_93.addWidget(self.frame_266)

        self.frame_268 = QFrame(self.frame_264)
        self.frame_268.setObjectName(u"frame_268")
        self.frame_268.setFrameShape(QFrame.StyledPanel)
        self.frame_268.setFrameShadow(QFrame.Raised)
        self.verticalLayout_159 = QVBoxLayout(self.frame_268)
        self.verticalLayout_159.setObjectName(u"verticalLayout_159")
        self.frame_448 = QFrame(self.frame_268)
        self.frame_448.setObjectName(u"frame_448")
        self.frame_448.setMinimumSize(QSize(0, 100))
        self.frame_448.setFrameShape(QFrame.StyledPanel)
        self.frame_448.setFrameShadow(QFrame.Raised)
        self.verticalLayout_315 = QVBoxLayout(self.frame_448)
        self.verticalLayout_315.setObjectName(u"verticalLayout_315")
        self.label_filtro_agendamento_as = QLabel(self.frame_448)
        self.label_filtro_agendamento_as.setObjectName(u"label_filtro_agendamento_as")
        self.label_filtro_agendamento_as.setFont(font15)

        self.verticalLayout_315.addWidget(self.label_filtro_agendamento_as)

        self.input_TableWidget_agendamento_as = QTableWidget(self.frame_448)
        if (self.input_TableWidget_agendamento_as.columnCount() < 3):
            self.input_TableWidget_agendamento_as.setColumnCount(3)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        if (self.input_TableWidget_agendamento_as.rowCount() < 14):
            self.input_TableWidget_agendamento_as.setRowCount(14)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setVerticalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setVerticalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setVerticalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setVerticalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setVerticalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setVerticalHeaderItem(5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setVerticalHeaderItem(6, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setVerticalHeaderItem(7, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setVerticalHeaderItem(8, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setVerticalHeaderItem(9, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setVerticalHeaderItem(10, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setVerticalHeaderItem(11, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setVerticalHeaderItem(12, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setVerticalHeaderItem(13, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setItem(0, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setItem(0, 1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.input_TableWidget_agendamento_as.setItem(1, 0, __qtablewidgetitem40)
        self.input_TableWidget_agendamento_as.setObjectName(u"input_TableWidget_agendamento_as")
        self.input_TableWidget_agendamento_as.setFont(font)
        self.input_TableWidget_agendamento_as.setLayoutDirection(Qt.LeftToRight)
        self.input_TableWidget_agendamento_as.setAutoFillBackground(False)
        self.input_TableWidget_agendamento_as.setStyleSheet(u"QTableEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QTableEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_TableWidget_agendamento_as.setInputMethodHints(Qt.ImhDate|Qt.ImhSensitiveData|Qt.ImhTime)
        self.input_TableWidget_agendamento_as.setLineWidth(2222)
        self.input_TableWidget_agendamento_as.setMidLineWidth(10)
        self.input_TableWidget_agendamento_as.setAlternatingRowColors(True)
        self.input_TableWidget_agendamento_as.setSelectionMode(QAbstractItemView.MultiSelection)
        self.input_TableWidget_agendamento_as.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.input_TableWidget_agendamento_as.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.input_TableWidget_agendamento_as.setGridStyle(Qt.SolidLine)
        self.input_TableWidget_agendamento_as.setSortingEnabled(True)
        self.input_TableWidget_agendamento_as.setWordWrap(True)
        self.input_TableWidget_agendamento_as.horizontalHeader().setCascadingSectionResizes(True)
        self.input_TableWidget_agendamento_as.horizontalHeader().setDefaultSectionSize(130)
        self.input_TableWidget_agendamento_as.horizontalHeader().setStretchLastSection(True)
        self.input_TableWidget_agendamento_as.verticalHeader().setVisible(False)
        self.input_TableWidget_agendamento_as.verticalHeader().setDefaultSectionSize(50)

        self.verticalLayout_315.addWidget(self.input_TableWidget_agendamento_as)

        self.input_filtro_agendamento_as = QLineEdit(self.frame_448)
        self.input_filtro_agendamento_as.setObjectName(u"input_filtro_agendamento_as")
        self.input_filtro_agendamento_as.setFont(font15)

        self.verticalLayout_315.addWidget(self.input_filtro_agendamento_as)


        self.verticalLayout_159.addWidget(self.frame_448)


        self.horizontalLayout_93.addWidget(self.frame_268)

        self.horizontalLayout_93.setStretch(1, 4)

        self.verticalLayout_109.addWidget(self.frame_264)

        self.frame_265 = QFrame(self.page_agenda_as)
        self.frame_265.setObjectName(u"frame_265")
        self.frame_265.setFrameShape(QFrame.StyledPanel)
        self.frame_265.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_265)
        self.horizontalLayout_92.setSpacing(20)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(20, 0, 0, 0)
        self.btn_voltar_agenda_as = QPushButton(self.frame_265)
        self.btn_voltar_agenda_as.setObjectName(u"btn_voltar_agenda_as")
        self.btn_voltar_agenda_as.setMinimumSize(QSize(120, 40))
        self.btn_voltar_agenda_as.setMaximumSize(QSize(120, 40))
        self.btn_voltar_agenda_as.setFont(font11)
        self.btn_voltar_agenda_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_agenda_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout_92.addWidget(self.btn_voltar_agenda_as)

        self.horizontalSpacer_58 = QSpacerItem(955, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_58)

        self.btn_alterar_agenda_as = QPushButton(self.frame_265)
        self.btn_alterar_agenda_as.setObjectName(u"btn_alterar_agenda_as")
        self.btn_alterar_agenda_as.setMinimumSize(QSize(120, 40))
        self.btn_alterar_agenda_as.setMaximumSize(QSize(120, 40))
        self.btn_alterar_agenda_as.setFont(font12)
        self.btn_alterar_agenda_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_agenda_as.setAutoFillBackground(False)
        self.btn_alterar_agenda_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        icon21 = QIcon()
        icon21.addFile(u"./icons/troca.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar_agenda_as.setIcon(icon21)
        self.btn_alterar_agenda_as.setIconSize(QSize(24, 24))

        self.horizontalLayout_92.addWidget(self.btn_alterar_agenda_as)

        self.btn_cancelar_agenda_as = QPushButton(self.frame_265)
        self.btn_cancelar_agenda_as.setObjectName(u"btn_cancelar_agenda_as")
        self.btn_cancelar_agenda_as.setMinimumSize(QSize(120, 40))
        self.btn_cancelar_agenda_as.setMaximumSize(QSize(120, 40))
        self.btn_cancelar_agenda_as.setFont(font12)
        self.btn_cancelar_agenda_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar_agenda_as.setAutoFillBackground(False)
        self.btn_cancelar_agenda_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        icon22 = QIcon()
        icon22.addFile(u"./icons/cancelar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancelar_agenda_as.setIcon(icon22)
        self.btn_cancelar_agenda_as.setIconSize(QSize(24, 24))

        self.horizontalLayout_92.addWidget(self.btn_cancelar_agenda_as)

        self.btn_concluir_agenda_as = QPushButton(self.frame_265)
        self.btn_concluir_agenda_as.setObjectName(u"btn_concluir_agenda_as")
        self.btn_concluir_agenda_as.setMinimumSize(QSize(140, 40))
        self.btn_concluir_agenda_as.setMaximumSize(QSize(140, 40))
        self.btn_concluir_agenda_as.setFont(font11)
        self.btn_concluir_agenda_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_concluir_agenda_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout_92.addWidget(self.btn_concluir_agenda_as)


        self.verticalLayout_109.addWidget(self.frame_265)

        self.stackedWidget_2.addWidget(self.page_agenda_as)
        self.page_cadastro_clinica_as = QWidget()
        self.page_cadastro_clinica_as.setObjectName(u"page_cadastro_clinica_as")
        self.horizontalLayout_140 = QHBoxLayout(self.page_cadastro_clinica_as)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.frame_138 = QFrame(self.page_cadastro_clinica_as)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setFrameShape(QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_141 = QHBoxLayout(self.frame_138)
        self.horizontalLayout_141.setSpacing(0)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.horizontalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.frame_159 = QFrame(self.frame_138)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setMaximumSize(QSize(200, 16777215))
        self.frame_159.setFrameShape(QFrame.StyledPanel)
        self.frame_159.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_141.addWidget(self.frame_159)

        self.frame_160 = QFrame(self.frame_138)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setStyleSheet(u"\n"
"background-color: rgb(249, 217, 221);")
        self.frame_160.setFrameShape(QFrame.StyledPanel)
        self.frame_160.setFrameShadow(QFrame.Raised)
        self.verticalLayout_321 = QVBoxLayout(self.frame_160)
        self.verticalLayout_321.setSpacing(0)
        self.verticalLayout_321.setObjectName(u"verticalLayout_321")
        self.verticalLayout_321.setContentsMargins(0, 0, 0, 0)
        self.frame_163 = QFrame(self.frame_160)
        self.frame_163.setObjectName(u"frame_163")
        self.frame_163.setStyleSheet(u"background-color: #F3B9BF; margin-bottom: 2em")
        self.frame_163.setFrameShape(QFrame.StyledPanel)
        self.frame_163.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_142 = QHBoxLayout(self.frame_163)
        self.horizontalLayout_142.setSpacing(0)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalLayout_142.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.frame_163)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font1)
        self.label_37.setStyleSheet(u"color: #EC848C; padding-top: 1.5em")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_142.addWidget(self.label_37)


        self.verticalLayout_321.addWidget(self.frame_163)

        self.frame_214 = QFrame(self.frame_160)
        self.frame_214.setObjectName(u"frame_214")
        self.frame_214.setStyleSheet(u"background-color: rgb(249, 217, 221);")
        self.frame_214.setFrameShape(QFrame.StyledPanel)
        self.frame_214.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_143 = QHBoxLayout(self.frame_214)
        self.horizontalLayout_143.setSpacing(0)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalLayout_143.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_851 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_143.addItem(self.horizontalSpacer_851)

        self.frame_252 = QFrame(self.frame_214)
        self.frame_252.setObjectName(u"frame_252")
        self.frame_252.setStyleSheet(u"QLabel{margin-left: 0.25em}")
        self.frame_252.setFrameShape(QFrame.StyledPanel)
        self.frame_252.setFrameShadow(QFrame.Raised)
        self.verticalLayout_112 = QVBoxLayout(self.frame_252)
        self.verticalLayout_112.setSpacing(0)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_112.setContentsMargins(20, 0, 0, 0)
        self.frame_253 = QFrame(self.frame_252)
        self.frame_253.setObjectName(u"frame_253")
        sizePolicy.setHeightForWidth(self.frame_253.sizePolicy().hasHeightForWidth())
        self.frame_253.setSizePolicy(sizePolicy)
        self.frame_253.setMinimumSize(QSize(0, 0))
        self.frame_253.setMaximumSize(QSize(16777215, 60))
        self.frame_253.setStyleSheet(u"")
        self.frame_253.setFrameShape(QFrame.StyledPanel)
        self.frame_253.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_144 = QHBoxLayout(self.frame_253)
        self.horizontalLayout_144.setSpacing(5)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.horizontalLayout_144.setContentsMargins(0, 0, 0, 0)
        self.frame_254 = QFrame(self.frame_253)
        self.frame_254.setObjectName(u"frame_254")
        self.frame_254.setMinimumSize(QSize(0, 0))
        self.frame_254.setMaximumSize(QSize(16777215, 16777215))
        self.frame_254.setFrameShape(QFrame.StyledPanel)
        self.frame_254.setFrameShadow(QFrame.Raised)
        self.verticalLayout_113 = QVBoxLayout(self.frame_254)
        self.verticalLayout_113.setSpacing(0)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.label_codigo_cadastro_clinica_as = QLabel(self.frame_254)
        self.label_codigo_cadastro_clinica_as.setObjectName(u"label_codigo_cadastro_clinica_as")
        self.label_codigo_cadastro_clinica_as.setMinimumSize(QSize(0, 0))
        self.label_codigo_cadastro_clinica_as.setMaximumSize(QSize(160, 16777215))
        self.label_codigo_cadastro_clinica_as.setFont(font)

        self.verticalLayout_113.addWidget(self.label_codigo_cadastro_clinica_as)

        self.input_codigo_cadastro_clinica_as = QLineEdit(self.frame_254)
        self.input_codigo_cadastro_clinica_as.setObjectName(u"input_codigo_cadastro_clinica_as")
        self.input_codigo_cadastro_clinica_as.setEnabled(False)
        self.input_codigo_cadastro_clinica_as.setMinimumSize(QSize(0, 30))
        self.input_codigo_cadastro_clinica_as.setMaximumSize(QSize(110, 30))
        self.input_codigo_cadastro_clinica_as.setFont(font)
        self.input_codigo_cadastro_clinica_as.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout_113.addWidget(self.input_codigo_cadastro_clinica_as)


        self.horizontalLayout_144.addWidget(self.frame_254)

        self.frame_270 = QFrame(self.frame_253)
        self.frame_270.setObjectName(u"frame_270")
        self.frame_270.setMinimumSize(QSize(0, 0))
        self.frame_270.setMaximumSize(QSize(16777215, 16777215))
        self.frame_270.setFrameShape(QFrame.StyledPanel)
        self.frame_270.setFrameShadow(QFrame.Raised)
        self.verticalLayout_172 = QVBoxLayout(self.frame_270)
        self.verticalLayout_172.setSpacing(0)
        self.verticalLayout_172.setObjectName(u"verticalLayout_172")
        self.verticalLayout_172.setContentsMargins(0, 0, 0, 0)
        self.label_cnpj_cadastro_clinica_as = QLabel(self.frame_270)
        self.label_cnpj_cadastro_clinica_as.setObjectName(u"label_cnpj_cadastro_clinica_as")
        self.label_cnpj_cadastro_clinica_as.setMinimumSize(QSize(0, 0))
        self.label_cnpj_cadastro_clinica_as.setMaximumSize(QSize(180, 16777215))
        self.label_cnpj_cadastro_clinica_as.setFont(font)

        self.verticalLayout_172.addWidget(self.label_cnpj_cadastro_clinica_as)

        self.input_cnpj_cadastro_clinica_as = QLineEdit(self.frame_270)
        self.input_cnpj_cadastro_clinica_as.setObjectName(u"input_cnpj_cadastro_clinica_as")
        self.input_cnpj_cadastro_clinica_as.setMinimumSize(QSize(0, 30))
        self.input_cnpj_cadastro_clinica_as.setMaximumSize(QSize(16777215, 30))
        self.input_cnpj_cadastro_clinica_as.setFont(font)
        self.input_cnpj_cadastro_clinica_as.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout_172.addWidget(self.input_cnpj_cadastro_clinica_as)


        self.horizontalLayout_144.addWidget(self.frame_270)

        self.frame_256 = QFrame(self.frame_253)
        self.frame_256.setObjectName(u"frame_256")
        self.frame_256.setMinimumSize(QSize(0, 0))
        self.frame_256.setMaximumSize(QSize(16777215, 16777215))
        self.frame_256.setFrameShape(QFrame.StyledPanel)
        self.frame_256.setFrameShadow(QFrame.Raised)
        self.verticalLayout_169 = QVBoxLayout(self.frame_256)
        self.verticalLayout_169.setSpacing(0)
        self.verticalLayout_169.setObjectName(u"verticalLayout_169")
        self.verticalLayout_169.setContentsMargins(0, 0, 0, 0)
        self.label_razao_social_cadastro_clinica_as = QLabel(self.frame_256)
        self.label_razao_social_cadastro_clinica_as.setObjectName(u"label_razao_social_cadastro_clinica_as")
        self.label_razao_social_cadastro_clinica_as.setMinimumSize(QSize(0, 0))
        self.label_razao_social_cadastro_clinica_as.setMaximumSize(QSize(16777215, 16777215))
        self.label_razao_social_cadastro_clinica_as.setFont(font)

        self.verticalLayout_169.addWidget(self.label_razao_social_cadastro_clinica_as)

        self.input_razao_social_cadastro_clinica_as = QLineEdit(self.frame_256)
        self.input_razao_social_cadastro_clinica_as.setObjectName(u"input_razao_social_cadastro_clinica_as")
        self.input_razao_social_cadastro_clinica_as.setMinimumSize(QSize(0, 30))
        self.input_razao_social_cadastro_clinica_as.setMaximumSize(QSize(16777215, 30))
        self.input_razao_social_cadastro_clinica_as.setFont(font)
        self.input_razao_social_cadastro_clinica_as.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout_169.addWidget(self.input_razao_social_cadastro_clinica_as)


        self.horizontalLayout_144.addWidget(self.frame_256)

        self.frame_257 = QFrame(self.frame_253)
        self.frame_257.setObjectName(u"frame_257")
        self.frame_257.setMinimumSize(QSize(0, 0))
        self.frame_257.setMaximumSize(QSize(16777215, 16777215))
        self.frame_257.setFrameShape(QFrame.StyledPanel)
        self.frame_257.setFrameShadow(QFrame.Raised)
        self.verticalLayout_170 = QVBoxLayout(self.frame_257)
        self.verticalLayout_170.setSpacing(0)
        self.verticalLayout_170.setObjectName(u"verticalLayout_170")
        self.verticalLayout_170.setContentsMargins(0, 0, 0, 0)
        self.label_nome_fantasia_cadastro_clinica_as = QLabel(self.frame_257)
        self.label_nome_fantasia_cadastro_clinica_as.setObjectName(u"label_nome_fantasia_cadastro_clinica_as")
        self.label_nome_fantasia_cadastro_clinica_as.setMinimumSize(QSize(0, 0))
        self.label_nome_fantasia_cadastro_clinica_as.setMaximumSize(QSize(16777215, 16777215))
        self.label_nome_fantasia_cadastro_clinica_as.setFont(font)

        self.verticalLayout_170.addWidget(self.label_nome_fantasia_cadastro_clinica_as)

        self.input_nome_fantasia_cadastro_clinica_as = QLineEdit(self.frame_257)
        self.input_nome_fantasia_cadastro_clinica_as.setObjectName(u"input_nome_fantasia_cadastro_clinica_as")
        self.input_nome_fantasia_cadastro_clinica_as.setMinimumSize(QSize(0, 30))
        self.input_nome_fantasia_cadastro_clinica_as.setMaximumSize(QSize(16777215, 30))
        self.input_nome_fantasia_cadastro_clinica_as.setFont(font)
        self.input_nome_fantasia_cadastro_clinica_as.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout_170.addWidget(self.input_nome_fantasia_cadastro_clinica_as)


        self.horizontalLayout_144.addWidget(self.frame_257)

        self.horizontalLayout_144.setStretch(0, 1)
        self.horizontalLayout_144.setStretch(1, 2)
        self.horizontalLayout_144.setStretch(2, 3)
        self.horizontalLayout_144.setStretch(3, 3)

        self.verticalLayout_112.addWidget(self.frame_253)

        self.frame_451 = QFrame(self.frame_252)
        self.frame_451.setObjectName(u"frame_451")
        self.frame_451.setMinimumSize(QSize(0, 0))
        self.frame_451.setMaximumSize(QSize(16777215, 60))
        self.frame_451.setStyleSheet(u"")
        self.frame_451.setFrameShape(QFrame.StyledPanel)
        self.frame_451.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_148 = QHBoxLayout(self.frame_451)
        self.horizontalLayout_148.setSpacing(5)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.horizontalLayout_148.setContentsMargins(0, 0, 0, 0)
        self.frame_456 = QFrame(self.frame_451)
        self.frame_456.setObjectName(u"frame_456")
        self.frame_456.setMinimumSize(QSize(0, 0))
        self.frame_456.setMaximumSize(QSize(16777215, 16777215))
        self.frame_456.setFrameShape(QFrame.StyledPanel)
        self.frame_456.setFrameShadow(QFrame.Raised)
        self.verticalLayout_317 = QVBoxLayout(self.frame_456)
        self.verticalLayout_317.setSpacing(0)
        self.verticalLayout_317.setObjectName(u"verticalLayout_317")
        self.verticalLayout_317.setContentsMargins(0, 0, 0, 0)
        self.label_telefone_clinica_as = QLabel(self.frame_456)
        self.label_telefone_clinica_as.setObjectName(u"label_telefone_clinica_as")
        self.label_telefone_clinica_as.setMinimumSize(QSize(0, 0))
        self.label_telefone_clinica_as.setMaximumSize(QSize(16777215, 16777215))
        self.label_telefone_clinica_as.setFont(font)

        self.verticalLayout_317.addWidget(self.label_telefone_clinica_as)

        self.input_telefone_clinica_as = QLineEdit(self.frame_456)
        self.input_telefone_clinica_as.setObjectName(u"input_telefone_clinica_as")
        self.input_telefone_clinica_as.setMinimumSize(QSize(0, 30))
        self.input_telefone_clinica_as.setMaximumSize(QSize(16777215, 30))
        self.input_telefone_clinica_as.setFont(font)
        self.input_telefone_clinica_as.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout_317.addWidget(self.input_telefone_clinica_as)


        self.horizontalLayout_148.addWidget(self.frame_456)

        self.frame_457 = QFrame(self.frame_451)
        self.frame_457.setObjectName(u"frame_457")
        self.frame_457.setMinimumSize(QSize(0, 0))
        self.frame_457.setMaximumSize(QSize(16777215, 16777215))
        self.frame_457.setFrameShape(QFrame.StyledPanel)
        self.frame_457.setFrameShadow(QFrame.Raised)
        self.verticalLayout_318 = QVBoxLayout(self.frame_457)
        self.verticalLayout_318.setSpacing(0)
        self.verticalLayout_318.setObjectName(u"verticalLayout_318")
        self.verticalLayout_318.setContentsMargins(0, 0, 0, 0)
        self.label_email_clinica_as = QLabel(self.frame_457)
        self.label_email_clinica_as.setObjectName(u"label_email_clinica_as")
        self.label_email_clinica_as.setMinimumSize(QSize(0, 0))
        self.label_email_clinica_as.setMaximumSize(QSize(16777215, 16777215))
        self.label_email_clinica_as.setFont(font)

        self.verticalLayout_318.addWidget(self.label_email_clinica_as)

        self.input_email_clinica_as = QLineEdit(self.frame_457)
        self.input_email_clinica_as.setObjectName(u"input_email_clinica_as")
        self.input_email_clinica_as.setMinimumSize(QSize(0, 30))
        self.input_email_clinica_as.setMaximumSize(QSize(16777215, 30))
        self.input_email_clinica_as.setFont(font)
        self.input_email_clinica_as.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout_318.addWidget(self.input_email_clinica_as)


        self.horizontalLayout_148.addWidget(self.frame_457)

        self.frame_449 = QFrame(self.frame_451)
        self.frame_449.setObjectName(u"frame_449")
        self.frame_449.setMinimumSize(QSize(0, 0))
        self.frame_449.setMaximumSize(QSize(151, 16777215))
        self.frame_449.setFrameShape(QFrame.StyledPanel)
        self.frame_449.setFrameShadow(QFrame.Raised)
        self.verticalLayout_320 = QVBoxLayout(self.frame_449)
        self.verticalLayout_320.setSpacing(0)
        self.verticalLayout_320.setObjectName(u"verticalLayout_320")
        self.verticalLayout_320.setContentsMargins(0, 0, 0, 0)
        self.frame_454 = QFrame(self.frame_449)
        self.frame_454.setObjectName(u"frame_454")
        self.frame_454.setMaximumSize(QSize(170, 55))
        self.frame_454.setFrameShape(QFrame.StyledPanel)
        self.frame_454.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_147 = QHBoxLayout(self.frame_454)
        self.horizontalLayout_147.setSpacing(0)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.horizontalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.frame_455 = QFrame(self.frame_454)
        self.frame_455.setObjectName(u"frame_455")
        self.frame_455.setMinimumSize(QSize(160, 55))
        self.frame_455.setMaximumSize(QSize(150, 55))
        self.frame_455.setFrameShape(QFrame.StyledPanel)
        self.frame_455.setFrameShadow(QFrame.Raised)
        self.verticalLayout_176 = QVBoxLayout(self.frame_455)
        self.verticalLayout_176.setSpacing(2)
        self.verticalLayout_176.setObjectName(u"verticalLayout_176")
        self.verticalLayout_176.setContentsMargins(0, 0, 0, 0)
        self.label_cep_clinica_as = QLabel(self.frame_455)
        self.label_cep_clinica_as.setObjectName(u"label_cep_clinica_as")
        self.label_cep_clinica_as.setMinimumSize(QSize(50, 15))
        self.label_cep_clinica_as.setMaximumSize(QSize(50, 24))
        self.label_cep_clinica_as.setFont(font)

        self.verticalLayout_176.addWidget(self.label_cep_clinica_as)

        self.input_cep_clinica_as = QLineEdit(self.frame_455)
        self.input_cep_clinica_as.setObjectName(u"input_cep_clinica_as")
        self.input_cep_clinica_as.setMinimumSize(QSize(145, 30))
        self.input_cep_clinica_as.setMaximumSize(QSize(146, 30))
        self.input_cep_clinica_as.setFont(font)
        self.input_cep_clinica_as.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")
        self.input_cep_clinica_as.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_176.addWidget(self.input_cep_clinica_as)


        self.horizontalLayout_147.addWidget(self.frame_455)

        self.frame_459 = QFrame(self.frame_454)
        self.frame_459.setObjectName(u"frame_459")
        self.frame_459.setMinimumSize(QSize(22, 61))
        self.frame_459.setMaximumSize(QSize(31, 61))
        self.frame_459.setFrameShape(QFrame.StyledPanel)
        self.frame_459.setFrameShadow(QFrame.Raised)
        self.verticalLayout_328 = QVBoxLayout(self.frame_459)
        self.verticalLayout_328.setSpacing(0)
        self.verticalLayout_328.setObjectName(u"verticalLayout_328")
        self.verticalLayout_328.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_28 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_328.addItem(self.verticalSpacer_28)

        self.btn_cep_buscar_colaborador_as_3 = QPushButton(self.frame_459)
        self.btn_cep_buscar_colaborador_as_3.setObjectName(u"btn_cep_buscar_colaborador_as_3")
        sizePolicy2.setHeightForWidth(self.btn_cep_buscar_colaborador_as_3.sizePolicy().hasHeightForWidth())
        self.btn_cep_buscar_colaborador_as_3.setSizePolicy(sizePolicy2)
        self.btn_cep_buscar_colaborador_as_3.setMinimumSize(QSize(0, 30))
        self.btn_cep_buscar_colaborador_as_3.setMaximumSize(QSize(25, 30))
        self.btn_cep_buscar_colaborador_as_3.setStyleSheet(u"QPushButton{\n"
"        background: rgb(243, 185, 191);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        background: rgb(255, 194, 201);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"        background: rgb(180, 106, 102);\n"
"        border: 2px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}")
        self.btn_cep_buscar_colaborador_as_3.setIcon(icon20)

        self.verticalLayout_328.addWidget(self.btn_cep_buscar_colaborador_as_3)


        self.horizontalLayout_147.addWidget(self.frame_459)


        self.verticalLayout_320.addWidget(self.frame_454)


        self.horizontalLayout_148.addWidget(self.frame_449)

        self.frame_462 = QFrame(self.frame_451)
        self.frame_462.setObjectName(u"frame_462")
        self.frame_462.setMinimumSize(QSize(0, 0))
        self.frame_462.setMaximumSize(QSize(16777215, 16777215))
        self.frame_462.setFrameShape(QFrame.StyledPanel)
        self.frame_462.setFrameShadow(QFrame.Raised)
        self.verticalLayout_177 = QVBoxLayout(self.frame_462)
        self.verticalLayout_177.setSpacing(5)
        self.verticalLayout_177.setObjectName(u"verticalLayout_177")
        self.verticalLayout_177.setContentsMargins(0, 0, 0, 0)
        self.label_logradouro_clinica_as = QLabel(self.frame_462)
        self.label_logradouro_clinica_as.setObjectName(u"label_logradouro_clinica_as")
        self.label_logradouro_clinica_as.setMinimumSize(QSize(0, 0))
        self.label_logradouro_clinica_as.setMaximumSize(QSize(16777215, 16777215))
        self.label_logradouro_clinica_as.setFont(font)

        self.verticalLayout_177.addWidget(self.label_logradouro_clinica_as)

        self.input_logradouro_clinica_as = QLineEdit(self.frame_462)
        self.input_logradouro_clinica_as.setObjectName(u"input_logradouro_clinica_as")
        self.input_logradouro_clinica_as.setMinimumSize(QSize(0, 30))
        self.input_logradouro_clinica_as.setMaximumSize(QSize(16777215, 30))
        self.input_logradouro_clinica_as.setFont(font)
        self.input_logradouro_clinica_as.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout_177.addWidget(self.input_logradouro_clinica_as)


        self.horizontalLayout_148.addWidget(self.frame_462)

        self.horizontalLayout_148.setStretch(0, 2)
        self.horizontalLayout_148.setStretch(1, 3)
        self.horizontalLayout_148.setStretch(2, 1)
        self.horizontalLayout_148.setStretch(3, 3)

        self.verticalLayout_112.addWidget(self.frame_451)

        self.frame_458 = QFrame(self.frame_252)
        self.frame_458.setObjectName(u"frame_458")
        self.frame_458.setMinimumSize(QSize(0, 0))
        self.frame_458.setMaximumSize(QSize(16777215, 60))
        self.frame_458.setStyleSheet(u"")
        self.frame_458.setFrameShape(QFrame.StyledPanel)
        self.frame_458.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_146 = QHBoxLayout(self.frame_458)
        self.horizontalLayout_146.setSpacing(5)
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.horizontalLayout_146.setContentsMargins(0, 0, 0, 0)
        self.frame_463 = QFrame(self.frame_458)
        self.frame_463.setObjectName(u"frame_463")
        self.frame_463.setMinimumSize(QSize(0, 0))
        self.frame_463.setMaximumSize(QSize(16777215, 16777215))
        self.frame_463.setFrameShape(QFrame.StyledPanel)
        self.frame_463.setFrameShadow(QFrame.Raised)
        self.verticalLayout_322 = QVBoxLayout(self.frame_463)
        self.verticalLayout_322.setSpacing(0)
        self.verticalLayout_322.setObjectName(u"verticalLayout_322")
        self.verticalLayout_322.setContentsMargins(0, 0, 0, 0)
        self.label_numero_clinica_as = QLabel(self.frame_463)
        self.label_numero_clinica_as.setObjectName(u"label_numero_clinica_as")
        self.label_numero_clinica_as.setMinimumSize(QSize(0, 0))
        self.label_numero_clinica_as.setMaximumSize(QSize(16777215, 16777215))
        self.label_numero_clinica_as.setFont(font)

        self.verticalLayout_322.addWidget(self.label_numero_clinica_as)

        self.input_numero_clinica_as = QLineEdit(self.frame_463)
        self.input_numero_clinica_as.setObjectName(u"input_numero_clinica_as")
        sizePolicy4.setHeightForWidth(self.input_numero_clinica_as.sizePolicy().hasHeightForWidth())
        self.input_numero_clinica_as.setSizePolicy(sizePolicy4)
        self.input_numero_clinica_as.setMinimumSize(QSize(0, 30))
        self.input_numero_clinica_as.setMaximumSize(QSize(16777215, 30))
        self.input_numero_clinica_as.setFont(font)
        self.input_numero_clinica_as.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout_322.addWidget(self.input_numero_clinica_as)


        self.horizontalLayout_146.addWidget(self.frame_463)

        self.frame_464 = QFrame(self.frame_458)
        self.frame_464.setObjectName(u"frame_464")
        self.frame_464.setMinimumSize(QSize(0, 0))
        self.frame_464.setMaximumSize(QSize(16777215, 16777215))
        self.frame_464.setFrameShape(QFrame.StyledPanel)
        self.frame_464.setFrameShadow(QFrame.Raised)
        self.verticalLayout_323 = QVBoxLayout(self.frame_464)
        self.verticalLayout_323.setSpacing(0)
        self.verticalLayout_323.setObjectName(u"verticalLayout_323")
        self.verticalLayout_323.setContentsMargins(0, 0, 0, 0)
        self.label_bairro_clinica_as = QLabel(self.frame_464)
        self.label_bairro_clinica_as.setObjectName(u"label_bairro_clinica_as")
        self.label_bairro_clinica_as.setMinimumSize(QSize(0, 0))
        self.label_bairro_clinica_as.setMaximumSize(QSize(16777215, 16777215))
        self.label_bairro_clinica_as.setFont(font)

        self.verticalLayout_323.addWidget(self.label_bairro_clinica_as)

        self.input_bairro_clinica_as = QLineEdit(self.frame_464)
        self.input_bairro_clinica_as.setObjectName(u"input_bairro_clinica_as")
        self.input_bairro_clinica_as.setMinimumSize(QSize(0, 30))
        self.input_bairro_clinica_as.setMaximumSize(QSize(16777215, 30))
        self.input_bairro_clinica_as.setFont(font)
        self.input_bairro_clinica_as.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout_323.addWidget(self.input_bairro_clinica_as)


        self.horizontalLayout_146.addWidget(self.frame_464)

        self.frame_465 = QFrame(self.frame_458)
        self.frame_465.setObjectName(u"frame_465")
        self.frame_465.setMinimumSize(QSize(0, 0))
        self.frame_465.setMaximumSize(QSize(16777215, 16777215))
        self.frame_465.setFrameShape(QFrame.StyledPanel)
        self.frame_465.setFrameShadow(QFrame.Raised)
        self.verticalLayout_324 = QVBoxLayout(self.frame_465)
        self.verticalLayout_324.setSpacing(0)
        self.verticalLayout_324.setObjectName(u"verticalLayout_324")
        self.verticalLayout_324.setContentsMargins(0, 0, 0, 0)
        self.label_cidade_clinica_as = QLabel(self.frame_465)
        self.label_cidade_clinica_as.setObjectName(u"label_cidade_clinica_as")
        self.label_cidade_clinica_as.setMinimumSize(QSize(0, 0))
        self.label_cidade_clinica_as.setMaximumSize(QSize(16777215, 16777215))
        self.label_cidade_clinica_as.setFont(font)

        self.verticalLayout_324.addWidget(self.label_cidade_clinica_as)

        self.input_cidade_clinica_as = QLineEdit(self.frame_465)
        self.input_cidade_clinica_as.setObjectName(u"input_cidade_clinica_as")
        self.input_cidade_clinica_as.setMinimumSize(QSize(0, 30))
        self.input_cidade_clinica_as.setMaximumSize(QSize(16777215, 30))
        self.input_cidade_clinica_as.setFont(font)
        self.input_cidade_clinica_as.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout_324.addWidget(self.input_cidade_clinica_as)


        self.horizontalLayout_146.addWidget(self.frame_465)

        self.frame_466 = QFrame(self.frame_458)
        self.frame_466.setObjectName(u"frame_466")
        self.frame_466.setMinimumSize(QSize(0, 0))
        self.frame_466.setMaximumSize(QSize(80, 16777215))
        self.frame_466.setFrameShape(QFrame.StyledPanel)
        self.frame_466.setFrameShadow(QFrame.Raised)
        self.verticalLayout_325 = QVBoxLayout(self.frame_466)
        self.verticalLayout_325.setSpacing(0)
        self.verticalLayout_325.setObjectName(u"verticalLayout_325")
        self.verticalLayout_325.setContentsMargins(0, 0, 0, 0)
        self.label_estado_clinica__as = QLabel(self.frame_466)
        self.label_estado_clinica__as.setObjectName(u"label_estado_clinica__as")
        self.label_estado_clinica__as.setMinimumSize(QSize(0, 0))
        self.label_estado_clinica__as.setMaximumSize(QSize(80, 16777215))
        self.label_estado_clinica__as.setFont(font)

        self.verticalLayout_325.addWidget(self.label_estado_clinica__as)

        self.input_estado_clinica_as = QLineEdit(self.frame_466)
        self.input_estado_clinica_as.setObjectName(u"input_estado_clinica_as")
        self.input_estado_clinica_as.setMinimumSize(QSize(70, 30))
        self.input_estado_clinica_as.setMaximumSize(QSize(80, 30))
        self.input_estado_clinica_as.setFont(font)
        self.input_estado_clinica_as.setStyleSheet(u"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout_325.addWidget(self.input_estado_clinica_as)


        self.horizontalLayout_146.addWidget(self.frame_466)

        self.horizontalLayout_146.setStretch(0, 1)
        self.horizontalLayout_146.setStretch(1, 3)
        self.horizontalLayout_146.setStretch(2, 3)
        self.horizontalLayout_146.setStretch(3, 1)

        self.verticalLayout_112.addWidget(self.frame_458)

        self.frame_467 = QFrame(self.frame_252)
        self.frame_467.setObjectName(u"frame_467")
        self.frame_467.setMinimumSize(QSize(0, 0))
        self.frame_467.setMaximumSize(QSize(16777215, 300))
        self.frame_467.setStyleSheet(u"")
        self.frame_467.setFrameShape(QFrame.StyledPanel)
        self.frame_467.setFrameShadow(QFrame.Raised)
        self.verticalLayout_183 = QVBoxLayout(self.frame_467)
        self.verticalLayout_183.setObjectName(u"verticalLayout_183")
        self.label_informacoes_gerais_clinica_as = QLabel(self.frame_467)
        self.label_informacoes_gerais_clinica_as.setObjectName(u"label_informacoes_gerais_clinica_as")
        self.label_informacoes_gerais_clinica_as.setMaximumSize(QSize(16777215, 50))
        self.label_informacoes_gerais_clinica_as.setFont(font)

        self.verticalLayout_183.addWidget(self.label_informacoes_gerais_clinica_as)

        self.input_informacoes_gerais_clinica_as = QTextEdit(self.frame_467)
        self.input_informacoes_gerais_clinica_as.setObjectName(u"input_informacoes_gerais_clinica_as")
        self.input_informacoes_gerais_clinica_as.setMaximumSize(QSize(16777215, 235))
        self.input_informacoes_gerais_clinica_as.setFont(font)
        self.input_informacoes_gerais_clinica_as.setStyleSheet(u"QTextEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QTextEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout_183.addWidget(self.input_informacoes_gerais_clinica_as)


        self.verticalLayout_112.addWidget(self.frame_467)


        self.horizontalLayout_143.addWidget(self.frame_252)

        self.horizontalSpacer_861 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_143.addItem(self.horizontalSpacer_861)

        self.horizontalLayout_143.setStretch(0, 1)
        self.horizontalLayout_143.setStretch(2, 1)

        self.verticalLayout_321.addWidget(self.frame_214)

        self.frame_460 = QFrame(self.frame_160)
        self.frame_460.setObjectName(u"frame_460")
        self.frame_460.setMinimumSize(QSize(0, 0))
        self.frame_460.setStyleSheet(u"background-color: rgb(249, 217, 221);")
        self.frame_460.setFrameShape(QFrame.StyledPanel)
        self.frame_460.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_149 = QHBoxLayout(self.frame_460)
        self.horizontalLayout_149.setSpacing(20)
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.horizontalLayout_149.setContentsMargins(20, 0, 0, 0)
        self.btn_voltar_as = QPushButton(self.frame_460)
        self.btn_voltar_as.setObjectName(u"btn_voltar_as")
        self.btn_voltar_as.setMinimumSize(QSize(100, 40))
        self.btn_voltar_as.setMaximumSize(QSize(100, 40))
        self.btn_voltar_as.setFont(font11)
        self.btn_voltar_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout_149.addWidget(self.btn_voltar_as)

        self.horizontalSpacer_871 = QSpacerItem(1770, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_149.addItem(self.horizontalSpacer_871)

        self.btn_finalizar_as_2 = QPushButton(self.frame_460)
        self.btn_finalizar_as_2.setObjectName(u"btn_finalizar_as_2")
        self.btn_finalizar_as_2.setMinimumSize(QSize(125, 40))
        self.btn_finalizar_as_2.setFont(font11)
        self.btn_finalizar_as_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_finalizar_as_2.setLayoutDirection(Qt.RightToLeft)
        self.btn_finalizar_as_2.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout_149.addWidget(self.btn_finalizar_as_2)


        self.verticalLayout_321.addWidget(self.frame_460)


        self.horizontalLayout_141.addWidget(self.frame_160)

        self.frame_161 = QFrame(self.frame_138)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setMaximumSize(QSize(200, 16777215))
        self.frame_161.setFrameShape(QFrame.StyledPanel)
        self.frame_161.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_141.addWidget(self.frame_161)


        self.horizontalLayout_140.addWidget(self.frame_138)

        self.stackedWidget_2.addWidget(self.page_cadastro_clinica_as)
        self.page_alterar_dados_as = QWidget()
        self.page_alterar_dados_as.setObjectName(u"page_alterar_dados_as")
        self.verticalLayout_283 = QVBoxLayout(self.page_alterar_dados_as)
        self.verticalLayout_283.setSpacing(0)
        self.verticalLayout_283.setObjectName(u"verticalLayout_283")
        self.verticalLayout_283.setContentsMargins(0, 0, 0, 0)
        self.frame_273 = QFrame(self.page_alterar_dados_as)
        self.frame_273.setObjectName(u"frame_273")
        self.frame_273.setFont(font10)
        self.frame_273.setFrameShape(QFrame.StyledPanel)
        self.frame_273.setFrameShadow(QFrame.Raised)
        self.verticalLayout_185 = QVBoxLayout(self.frame_273)
        self.verticalLayout_185.setSpacing(0)
        self.verticalLayout_185.setObjectName(u"verticalLayout_185")
        self.verticalLayout_185.setContentsMargins(0, 0, 0, 0)
        self.frame_274 = QFrame(self.frame_273)
        self.frame_274.setObjectName(u"frame_274")
        self.frame_274.setMinimumSize(QSize(0, 62))
        self.frame_274.setMaximumSize(QSize(16777215, 62))
        self.frame_274.setStyleSheet(u"background-color: rgb(243, 185, 191);")
        self.frame_274.setFrameShape(QFrame.StyledPanel)
        self.frame_274.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.frame_274)
        self.horizontalLayout_95.setSpacing(0)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, -1, 0, 0)
        self.label_altercao_de_dados = QLabel(self.frame_274)
        self.label_altercao_de_dados.setObjectName(u"label_altercao_de_dados")
        self.label_altercao_de_dados.setMinimumSize(QSize(852, 45))
        self.label_altercao_de_dados.setMaximumSize(QSize(852, 450))
        font18 = QFont()
        font18.setFamilies([u"Abel"])
        font18.setPointSize(30)
        self.label_altercao_de_dados.setFont(font18)
        self.label_altercao_de_dados.setStyleSheet(u"color: rgb(236, 132, 140);")
        self.label_altercao_de_dados.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_95.addWidget(self.label_altercao_de_dados)


        self.verticalLayout_185.addWidget(self.frame_274)

        self.frame_275 = QFrame(self.frame_273)
        self.frame_275.setObjectName(u"frame_275")
        self.frame_275.setMinimumSize(QSize(0, 88))
        self.frame_275.setMaximumSize(QSize(5555, 88))
        self.frame_275.setFrameShape(QFrame.StyledPanel)
        self.frame_275.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.frame_275)
        self.horizontalLayout_96.setSpacing(0)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.frame_276 = QFrame(self.frame_275)
        self.frame_276.setObjectName(u"frame_276")
        self.frame_276.setMinimumSize(QSize(272, 70))
        self.frame_276.setMaximumSize(QSize(272, 70))
        self.frame_276.setFont(font)
        self.frame_276.setFrameShape(QFrame.StyledPanel)
        self.frame_276.setFrameShadow(QFrame.Raised)
        self.verticalLayout_186 = QVBoxLayout(self.frame_276)
        self.verticalLayout_186.setSpacing(0)
        self.verticalLayout_186.setObjectName(u"verticalLayout_186")
        self.verticalLayout_186.setContentsMargins(0, 0, 0, 0)
        self.label_tipo_alterar_cadastros_as = QLabel(self.frame_276)
        self.label_tipo_alterar_cadastros_as.setObjectName(u"label_tipo_alterar_cadastros_as")
        self.label_tipo_alterar_cadastros_as.setMinimumSize(QSize(200, 20))
        self.label_tipo_alterar_cadastros_as.setMaximumSize(QSize(200, 20))
        self.label_tipo_alterar_cadastros_as.setSizeIncrement(QSize(126, 20))
        self.label_tipo_alterar_cadastros_as.setFont(font11)

        self.verticalLayout_186.addWidget(self.label_tipo_alterar_cadastros_as)

        self.comboBox_tipos_alterar_cadastros_as = QComboBox(self.frame_276)
        self.comboBox_tipos_alterar_cadastros_as.addItem("")
        self.comboBox_tipos_alterar_cadastros_as.addItem("")
        self.comboBox_tipos_alterar_cadastros_as.addItem("")
        self.comboBox_tipos_alterar_cadastros_as.addItem("")
        self.comboBox_tipos_alterar_cadastros_as.setObjectName(u"comboBox_tipos_alterar_cadastros_as")
        self.comboBox_tipos_alterar_cadastros_as.setMinimumSize(QSize(0, 30))
        self.comboBox_tipos_alterar_cadastros_as.setMaximumSize(QSize(16777215, 30))
        self.comboBox_tipos_alterar_cadastros_as.setFont(font11)

        self.verticalLayout_186.addWidget(self.comboBox_tipos_alterar_cadastros_as)


        self.horizontalLayout_96.addWidget(self.frame_276)

        self.frame_278 = QFrame(self.frame_275)
        self.frame_278.setObjectName(u"frame_278")
        self.frame_278.setMinimumSize(QSize(230, 70))
        self.frame_278.setMaximumSize(QSize(230, 70))
        self.frame_278.setFrameShape(QFrame.StyledPanel)
        self.frame_278.setFrameShadow(QFrame.Raised)
        self.verticalLayout_274 = QVBoxLayout(self.frame_278)
        self.verticalLayout_274.setSpacing(0)
        self.verticalLayout_274.setObjectName(u"verticalLayout_274")
        self.verticalLayout_274.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_cpf_cnpj_as = QLabel(self.frame_278)
        self.label_alterar_cpf_cnpj_as.setObjectName(u"label_alterar_cpf_cnpj_as")
        self.label_alterar_cpf_cnpj_as.setMinimumSize(QSize(126, 20))
        self.label_alterar_cpf_cnpj_as.setMaximumSize(QSize(126, 20))
        self.label_alterar_cpf_cnpj_as.setSizeIncrement(QSize(126, 20))
        self.label_alterar_cpf_cnpj_as.setFont(font11)

        self.verticalLayout_274.addWidget(self.label_alterar_cpf_cnpj_as)

        self.lineEdit_alterar_buscar_cpf_cnpj_as = QLineEdit(self.frame_278)
        self.lineEdit_alterar_buscar_cpf_cnpj_as.setObjectName(u"lineEdit_alterar_buscar_cpf_cnpj_as")
        self.lineEdit_alterar_buscar_cpf_cnpj_as.setMinimumSize(QSize(225, 30))
        self.lineEdit_alterar_buscar_cpf_cnpj_as.setMaximumSize(QSize(225, 30))
        self.lineEdit_alterar_buscar_cpf_cnpj_as.setFont(font10)

        self.verticalLayout_274.addWidget(self.lineEdit_alterar_buscar_cpf_cnpj_as)


        self.horizontalLayout_96.addWidget(self.frame_278)

        self.frame_279 = QFrame(self.frame_275)
        self.frame_279.setObjectName(u"frame_279")
        self.frame_279.setMinimumSize(QSize(80, 60))
        self.frame_279.setMaximumSize(QSize(60, 60))
        self.frame_279.setFont(font13)
        self.frame_279.setFrameShape(QFrame.StyledPanel)
        self.frame_279.setFrameShadow(QFrame.Raised)
        self.btn_buscar_alterar_as = QPushButton(self.frame_279)
        self.btn_buscar_alterar_as.setObjectName(u"btn_buscar_alterar_as")
        self.btn_buscar_alterar_as.setGeometry(QRect(20, 10, 40, 40))
        sizePolicy2.setHeightForWidth(self.btn_buscar_alterar_as.sizePolicy().hasHeightForWidth())
        self.btn_buscar_alterar_as.setSizePolicy(sizePolicy2)
        self.btn_buscar_alterar_as.setMinimumSize(QSize(40, 40))
        self.btn_buscar_alterar_as.setMaximumSize(QSize(40, 40))
        self.btn_buscar_alterar_as.setStyleSheet(u"QPushButton{\n"
"        background: rgb(243, 185, 191);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 20px;\n"
"		border-bottom-right-radius: 20px;\n"
"		border-bottom-left-radius: 20px;\n"
"		border-top-left-radius: 20px;\n"
"        color: rgb(249, 217, 221);   \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        background: rgb(255, 194, 201);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 20px;\n"
"		border-bottom-right-radius: 20px;\n"
"		border-bottom-right-radius: 20px;\n"
"		border-bottom-left-radius: 20px;\n"
"        color: rgb(249, 217, 221); \n"
"		border-bottom-right-radius: 20px;\n"
"		border-bottom-left-radius: 20px;  \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"        background: rgb(180, 106, 102);\n"
"        border: 2px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 20px;\n"
"		border-bottom-right-radius: 20px;\n"
"        colo"
                        "r: rgb(249, 217, 221);   \n"
"}")
        self.btn_buscar_alterar_as.setIcon(icon12)

        self.horizontalLayout_96.addWidget(self.frame_279)


        self.verticalLayout_185.addWidget(self.frame_275)

        self.frame_280 = QFrame(self.frame_273)
        self.frame_280.setObjectName(u"frame_280")
        self.frame_280.setFrameShape(QFrame.StyledPanel)
        self.frame_280.setFrameShadow(QFrame.Raised)
        self.verticalLayout_188 = QVBoxLayout(self.frame_280)
        self.verticalLayout_188.setSpacing(0)
        self.verticalLayout_188.setObjectName(u"verticalLayout_188")
        self.verticalLayout_188.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_8 = QStackedWidget(self.frame_280)
        self.stackedWidget_8.setObjectName(u"stackedWidget_8")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_272 = QVBoxLayout(self.page_2)
        self.verticalLayout_272.setSpacing(0)
        self.verticalLayout_272.setObjectName(u"verticalLayout_272")
        self.verticalLayout_272.setContentsMargins(0, 0, 0, 0)
        self.frame_400 = QFrame(self.page_2)
        self.frame_400.setObjectName(u"frame_400")
        self.frame_400.setFrameShape(QFrame.StyledPanel)
        self.frame_400.setFrameShadow(QFrame.Raised)

        self.verticalLayout_272.addWidget(self.frame_400)

        self.stackedWidget_8.addWidget(self.page_2)
        self.page_alterar_cuidador = QWidget()
        self.page_alterar_cuidador.setObjectName(u"page_alterar_cuidador")
        self.verticalLayout_253 = QVBoxLayout(self.page_alterar_cuidador)
        self.verticalLayout_253.setSpacing(0)
        self.verticalLayout_253.setObjectName(u"verticalLayout_253")
        self.verticalLayout_253.setContentsMargins(0, 0, 0, 0)
        self.frame_281 = QFrame(self.page_alterar_cuidador)
        self.frame_281.setObjectName(u"frame_281")
        self.frame_281.setFrameShape(QFrame.StyledPanel)
        self.frame_281.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.frame_281)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalSpacer_57 = QSpacerItem(184, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_57)

        self.frame_282 = QFrame(self.frame_281)
        self.frame_282.setObjectName(u"frame_282")
        self.frame_282.setFrameShape(QFrame.StyledPanel)
        self.frame_282.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_103 = QHBoxLayout(self.frame_282)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalSpacer_61 = QSpacerItem(184, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_103.addItem(self.horizontalSpacer_61)

        self.frame_284 = QFrame(self.frame_282)
        self.frame_284.setObjectName(u"frame_284")
        self.frame_284.setFrameShape(QFrame.StyledPanel)
        self.frame_284.setFrameShadow(QFrame.Raised)
        self.verticalLayout_207 = QVBoxLayout(self.frame_284)
        self.verticalLayout_207.setObjectName(u"verticalLayout_207")
        self.frame_285 = QFrame(self.frame_284)
        self.frame_285.setObjectName(u"frame_285")
        self.frame_285.setStyleSheet(u"QLabel{margin-left: 0.25em}")
        self.frame_285.setFrameShape(QFrame.StyledPanel)
        self.frame_285.setFrameShadow(QFrame.Raised)
        self.verticalLayout_189 = QVBoxLayout(self.frame_285)
        self.verticalLayout_189.setSpacing(0)
        self.verticalLayout_189.setObjectName(u"verticalLayout_189")
        self.verticalLayout_189.setContentsMargins(20, 0, 0, 0)
        self.frame_286 = QFrame(self.frame_285)
        self.frame_286.setObjectName(u"frame_286")
        self.frame_286.setMinimumSize(QSize(0, 0))
        self.frame_286.setMaximumSize(QSize(16777215, 60))
        self.frame_286.setStyleSheet(u"")
        self.frame_286.setFrameShape(QFrame.StyledPanel)
        self.frame_286.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.frame_286)
        self.horizontalLayout_98.setSpacing(5)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.frame_287 = QFrame(self.frame_286)
        self.frame_287.setObjectName(u"frame_287")
        self.frame_287.setMinimumSize(QSize(0, 0))
        self.frame_287.setMaximumSize(QSize(160, 16777215))
        self.frame_287.setFrameShape(QFrame.StyledPanel)
        self.frame_287.setFrameShadow(QFrame.Raised)
        self.verticalLayout_190 = QVBoxLayout(self.frame_287)
        self.verticalLayout_190.setSpacing(0)
        self.verticalLayout_190.setObjectName(u"verticalLayout_190")
        self.verticalLayout_190.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_matricula_cuidador_as = QLabel(self.frame_287)
        self.label_alterar_matricula_cuidador_as.setObjectName(u"label_alterar_matricula_cuidador_as")
        self.label_alterar_matricula_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_matricula_cuidador_as.setMaximumSize(QSize(160, 16777215))
        self.label_alterar_matricula_cuidador_as.setFont(font)

        self.verticalLayout_190.addWidget(self.label_alterar_matricula_cuidador_as)

        self.input_alterar_matricula_cuidador_as = QLineEdit(self.frame_287)
        self.input_alterar_matricula_cuidador_as.setObjectName(u"input_alterar_matricula_cuidador_as")
        self.input_alterar_matricula_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_matricula_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_matricula_cuidador_as.setFont(font)

        self.verticalLayout_190.addWidget(self.input_alterar_matricula_cuidador_as)


        self.horizontalLayout_98.addWidget(self.frame_287)

        self.frame_288 = QFrame(self.frame_286)
        self.frame_288.setObjectName(u"frame_288")
        self.frame_288.setMinimumSize(QSize(0, 0))
        self.frame_288.setMaximumSize(QSize(460, 16777215))
        self.frame_288.setFrameShape(QFrame.StyledPanel)
        self.frame_288.setFrameShadow(QFrame.Raised)
        self.verticalLayout_191 = QVBoxLayout(self.frame_288)
        self.verticalLayout_191.setSpacing(0)
        self.verticalLayout_191.setObjectName(u"verticalLayout_191")
        self.verticalLayout_191.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_nome_cuidador_as = QLabel(self.frame_288)
        self.label_alterar_nome_cuidador_as.setObjectName(u"label_alterar_nome_cuidador_as")
        self.label_alterar_nome_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_nome_cuidador_as.setMaximumSize(QSize(460, 16777215))
        self.label_alterar_nome_cuidador_as.setFont(font)

        self.verticalLayout_191.addWidget(self.label_alterar_nome_cuidador_as)

        self.input_alterar_nome_cuidador_as = QLineEdit(self.frame_288)
        self.input_alterar_nome_cuidador_as.setObjectName(u"input_alterar_nome_cuidador_as")
        self.input_alterar_nome_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_nome_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_nome_cuidador_as.setFont(font)

        self.verticalLayout_191.addWidget(self.input_alterar_nome_cuidador_as)


        self.horizontalLayout_98.addWidget(self.frame_288)

        self.frame_289 = QFrame(self.frame_286)
        self.frame_289.setObjectName(u"frame_289")
        self.frame_289.setMinimumSize(QSize(0, 0))
        self.frame_289.setMaximumSize(QSize(180, 16777215))
        self.frame_289.setFrameShape(QFrame.StyledPanel)
        self.frame_289.setFrameShadow(QFrame.Raised)
        self.verticalLayout_192 = QVBoxLayout(self.frame_289)
        self.verticalLayout_192.setSpacing(0)
        self.verticalLayout_192.setObjectName(u"verticalLayout_192")
        self.verticalLayout_192.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_cpf_cuidador_as = QLabel(self.frame_289)
        self.label_alterar_cpf_cuidador_as.setObjectName(u"label_alterar_cpf_cuidador_as")
        self.label_alterar_cpf_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_cpf_cuidador_as.setMaximumSize(QSize(180, 16777215))
        self.label_alterar_cpf_cuidador_as.setFont(font)

        self.verticalLayout_192.addWidget(self.label_alterar_cpf_cuidador_as)

        self.input_alterar_cpf_cuidador_as = QLineEdit(self.frame_289)
        self.input_alterar_cpf_cuidador_as.setObjectName(u"input_alterar_cpf_cuidador_as")
        self.input_alterar_cpf_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_cpf_cuidador_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_alterar_cpf_cuidador_as.setFont(font)

        self.verticalLayout_192.addWidget(self.input_alterar_cpf_cuidador_as)


        self.horizontalLayout_98.addWidget(self.frame_289)

        self.frame_290 = QFrame(self.frame_286)
        self.frame_290.setObjectName(u"frame_290")
        self.frame_290.setMinimumSize(QSize(0, 0))
        self.frame_290.setMaximumSize(QSize(160, 16777215))
        self.frame_290.setFrameShape(QFrame.StyledPanel)
        self.frame_290.setFrameShadow(QFrame.Raised)
        self.verticalLayout_193 = QVBoxLayout(self.frame_290)
        self.verticalLayout_193.setSpacing(0)
        self.verticalLayout_193.setObjectName(u"verticalLayout_193")
        self.verticalLayout_193.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_rg_cuidador_as = QLabel(self.frame_290)
        self.label_alterar_rg_cuidador_as.setObjectName(u"label_alterar_rg_cuidador_as")
        self.label_alterar_rg_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_rg_cuidador_as.setMaximumSize(QSize(160, 16777215))
        self.label_alterar_rg_cuidador_as.setFont(font)

        self.verticalLayout_193.addWidget(self.label_alterar_rg_cuidador_as)

        self.input_alterar_rg_cuidador_as = QLineEdit(self.frame_290)
        self.input_alterar_rg_cuidador_as.setObjectName(u"input_alterar_rg_cuidador_as")
        self.input_alterar_rg_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_rg_cuidador_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_alterar_rg_cuidador_as.setFont(font)

        self.verticalLayout_193.addWidget(self.input_alterar_rg_cuidador_as)


        self.horizontalLayout_98.addWidget(self.frame_290)

        self.frame_291 = QFrame(self.frame_286)
        self.frame_291.setObjectName(u"frame_291")
        self.frame_291.setMinimumSize(QSize(0, 0))
        self.frame_291.setMaximumSize(QSize(155, 16777215))
        self.frame_291.setFrameShape(QFrame.StyledPanel)
        self.frame_291.setFrameShadow(QFrame.Raised)
        self.verticalLayout_194 = QVBoxLayout(self.frame_291)
        self.verticalLayout_194.setSpacing(5)
        self.verticalLayout_194.setObjectName(u"verticalLayout_194")
        self.verticalLayout_194.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_data_emissao_cuidador_as = QLabel(self.frame_291)
        self.label_alterar_data_emissao_cuidador_as.setObjectName(u"label_alterar_data_emissao_cuidador_as")
        self.label_alterar_data_emissao_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_data_emissao_cuidador_as.setMaximumSize(QSize(155, 16777215))
        self.label_alterar_data_emissao_cuidador_as.setFont(font)

        self.verticalLayout_194.addWidget(self.label_alterar_data_emissao_cuidador_as, 0, Qt.AlignHCenter)

        self.input_alterar_data_emissao_cuidador_as = QDateEdit(self.frame_291)
        self.input_alterar_data_emissao_cuidador_as.setObjectName(u"input_alterar_data_emissao_cuidador_as")
        sizePolicy1.setHeightForWidth(self.input_alterar_data_emissao_cuidador_as.sizePolicy().hasHeightForWidth())
        self.input_alterar_data_emissao_cuidador_as.setSizePolicy(sizePolicy1)
        self.input_alterar_data_emissao_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_data_emissao_cuidador_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_alterar_data_emissao_cuidador_as.setFont(font8)
        self.input_alterar_data_emissao_cuidador_as.setFocusPolicy(Qt.WheelFocus)
        self.input_alterar_data_emissao_cuidador_as.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.input_alterar_data_emissao_cuidador_as.setLayoutDirection(Qt.LeftToRight)
        self.input_alterar_data_emissao_cuidador_as.setAutoFillBackground(False)
        self.input_alterar_data_emissao_cuidador_as.setStyleSheet(u"QDateEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QDateEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_alterar_data_emissao_cuidador_as.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.input_alterar_data_emissao_cuidador_as.setAlignment(Qt.AlignCenter)
        self.input_alterar_data_emissao_cuidador_as.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.input_alterar_data_emissao_cuidador_as.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.input_alterar_data_emissao_cuidador_as.setCurrentSection(QDateTimeEdit.DaySection)
        self.input_alterar_data_emissao_cuidador_as.setCalendarPopup(False)
        self.input_alterar_data_emissao_cuidador_as.setCurrentSectionIndex(0)

        self.verticalLayout_194.addWidget(self.input_alterar_data_emissao_cuidador_as, 0, Qt.AlignHCenter)


        self.horizontalLayout_98.addWidget(self.frame_291)


        self.verticalLayout_189.addWidget(self.frame_286)

        self.frame_292 = QFrame(self.frame_285)
        self.frame_292.setObjectName(u"frame_292")
        self.frame_292.setMinimumSize(QSize(0, 0))
        self.frame_292.setMaximumSize(QSize(16777215, 60))
        self.frame_292.setStyleSheet(u"")
        self.frame_292.setFrameShape(QFrame.StyledPanel)
        self.frame_292.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_99 = QHBoxLayout(self.frame_292)
        self.horizontalLayout_99.setSpacing(5)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.frame_293 = QFrame(self.frame_292)
        self.frame_293.setObjectName(u"frame_293")
        self.frame_293.setMinimumSize(QSize(155, 0))
        self.frame_293.setMaximumSize(QSize(155, 16777215))
        self.frame_293.setFrameShape(QFrame.StyledPanel)
        self.frame_293.setFrameShadow(QFrame.Raised)
        self.verticalLayout_195 = QVBoxLayout(self.frame_293)
        self.verticalLayout_195.setSpacing(0)
        self.verticalLayout_195.setObjectName(u"verticalLayout_195")
        self.verticalLayout_195.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_orgao_expedidor_cuidador_as = QLabel(self.frame_293)
        self.label_alterar_orgao_expedidor_cuidador_as.setObjectName(u"label_alterar_orgao_expedidor_cuidador_as")
        self.label_alterar_orgao_expedidor_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_orgao_expedidor_cuidador_as.setMaximumSize(QSize(155, 16777215))
        self.label_alterar_orgao_expedidor_cuidador_as.setFont(font)

        self.verticalLayout_195.addWidget(self.label_alterar_orgao_expedidor_cuidador_as)

        self.input_alterar_orgao_expedidor_cuidador_as = QLineEdit(self.frame_293)
        self.input_alterar_orgao_expedidor_cuidador_as.setObjectName(u"input_alterar_orgao_expedidor_cuidador_as")
        self.input_alterar_orgao_expedidor_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_orgao_expedidor_cuidador_as.setFont(font)

        self.verticalLayout_195.addWidget(self.input_alterar_orgao_expedidor_cuidador_as)


        self.horizontalLayout_99.addWidget(self.frame_293)

        self.frame_294 = QFrame(self.frame_292)
        self.frame_294.setObjectName(u"frame_294")
        self.frame_294.setMinimumSize(QSize(155, 0))
        self.frame_294.setMaximumSize(QSize(155, 16777215))
        self.frame_294.setFrameShape(QFrame.StyledPanel)
        self.frame_294.setFrameShadow(QFrame.Raised)
        self.verticalLayout_196 = QVBoxLayout(self.frame_294)
        self.verticalLayout_196.setSpacing(5)
        self.verticalLayout_196.setObjectName(u"verticalLayout_196")
        self.verticalLayout_196.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_sexo_cuidador_as = QLabel(self.frame_294)
        self.label_alterar_sexo_cuidador_as.setObjectName(u"label_alterar_sexo_cuidador_as")
        self.label_alterar_sexo_cuidador_as.setFont(font)

        self.verticalLayout_196.addWidget(self.label_alterar_sexo_cuidador_as)

        self.input_alterar_sexo_cuidador_as = QComboBox(self.frame_294)
        self.input_alterar_sexo_cuidador_as.addItem("")
        self.input_alterar_sexo_cuidador_as.addItem("")
        self.input_alterar_sexo_cuidador_as.addItem("")
        self.input_alterar_sexo_cuidador_as.setObjectName(u"input_alterar_sexo_cuidador_as")
        self.input_alterar_sexo_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_sexo_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_sexo_cuidador_as.setFont(font)

        self.verticalLayout_196.addWidget(self.input_alterar_sexo_cuidador_as)


        self.horizontalLayout_99.addWidget(self.frame_294)

        self.frame_295 = QFrame(self.frame_292)
        self.frame_295.setObjectName(u"frame_295")
        self.frame_295.setMinimumSize(QSize(0, 0))
        self.frame_295.setMaximumSize(QSize(280, 16777215))
        self.frame_295.setFrameShape(QFrame.StyledPanel)
        self.frame_295.setFrameShadow(QFrame.Raised)
        self.verticalLayout_197 = QVBoxLayout(self.frame_295)
        self.verticalLayout_197.setSpacing(0)
        self.verticalLayout_197.setObjectName(u"verticalLayout_197")
        self.verticalLayout_197.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_parentesco_cuidador_as = QLabel(self.frame_295)
        self.label_alterar_parentesco_cuidador_as.setObjectName(u"label_alterar_parentesco_cuidador_as")
        self.label_alterar_parentesco_cuidador_as.setFont(font)

        self.verticalLayout_197.addWidget(self.label_alterar_parentesco_cuidador_as)

        self.input_alterar_parentesco_cuidador_as = QLineEdit(self.frame_295)
        self.input_alterar_parentesco_cuidador_as.setObjectName(u"input_alterar_parentesco_cuidador_as")
        self.input_alterar_parentesco_cuidador_as.setMinimumSize(QSize(0, 0))
        self.input_alterar_parentesco_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_parentesco_cuidador_as.setFont(font)

        self.verticalLayout_197.addWidget(self.input_alterar_parentesco_cuidador_as)


        self.horizontalLayout_99.addWidget(self.frame_295)

        self.frame_296 = QFrame(self.frame_292)
        self.frame_296.setObjectName(u"frame_296")
        self.frame_296.setMinimumSize(QSize(0, 0))
        self.frame_296.setMaximumSize(QSize(155, 16777215))
        self.frame_296.setFrameShape(QFrame.StyledPanel)
        self.frame_296.setFrameShadow(QFrame.Raised)
        self.verticalLayout_198 = QVBoxLayout(self.frame_296)
        self.verticalLayout_198.setSpacing(0)
        self.verticalLayout_198.setObjectName(u"verticalLayout_198")
        self.verticalLayout_198.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_telefone_cuidador_as = QLabel(self.frame_296)
        self.label_alterar_telefone_cuidador_as.setObjectName(u"label_alterar_telefone_cuidador_as")
        self.label_alterar_telefone_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_telefone_cuidador_as.setMaximumSize(QSize(155, 16777215))
        self.label_alterar_telefone_cuidador_as.setFont(font)

        self.verticalLayout_198.addWidget(self.label_alterar_telefone_cuidador_as)

        self.input_alterar_telefone_cuidador_as = QLineEdit(self.frame_296)
        self.input_alterar_telefone_cuidador_as.setObjectName(u"input_alterar_telefone_cuidador_as")
        self.input_alterar_telefone_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_telefone_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_telefone_cuidador_as.setFont(font)

        self.verticalLayout_198.addWidget(self.input_alterar_telefone_cuidador_as)


        self.horizontalLayout_99.addWidget(self.frame_296)

        self.frame_297 = QFrame(self.frame_292)
        self.frame_297.setObjectName(u"frame_297")
        self.frame_297.setMinimumSize(QSize(0, 0))
        self.frame_297.setMaximumSize(QSize(240, 16777215))
        self.frame_297.setFrameShape(QFrame.StyledPanel)
        self.frame_297.setFrameShadow(QFrame.Raised)
        self.verticalLayout_199 = QVBoxLayout(self.frame_297)
        self.verticalLayout_199.setSpacing(0)
        self.verticalLayout_199.setObjectName(u"verticalLayout_199")
        self.verticalLayout_199.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_email_cuidador_as = QLabel(self.frame_297)
        self.label_alterar_email_cuidador_as.setObjectName(u"label_alterar_email_cuidador_as")
        self.label_alterar_email_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_email_cuidador_as.setMaximumSize(QSize(240, 16777215))
        self.label_alterar_email_cuidador_as.setFont(font)

        self.verticalLayout_199.addWidget(self.label_alterar_email_cuidador_as)

        self.input_alterar_email_cuidador_as = QLineEdit(self.frame_297)
        self.input_alterar_email_cuidador_as.setObjectName(u"input_alterar_email_cuidador_as")
        self.input_alterar_email_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_email_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_email_cuidador_as.setFont(font)

        self.verticalLayout_199.addWidget(self.input_alterar_email_cuidador_as)


        self.horizontalLayout_99.addWidget(self.frame_297)

        self.frame_298 = QFrame(self.frame_292)
        self.frame_298.setObjectName(u"frame_298")
        self.frame_298.setMaximumSize(QSize(170, 16777215))
        self.frame_298.setFrameShape(QFrame.StyledPanel)
        self.frame_298.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_125 = QHBoxLayout(self.frame_298)
        self.horizontalLayout_125.setSpacing(0)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.frame_424 = QFrame(self.frame_298)
        self.frame_424.setObjectName(u"frame_424")
        self.frame_424.setMinimumSize(QSize(160, 61))
        self.frame_424.setMaximumSize(QSize(150, 61))
        self.frame_424.setFrameShape(QFrame.StyledPanel)
        self.frame_424.setFrameShadow(QFrame.Raised)
        self.verticalLayout_200 = QVBoxLayout(self.frame_424)
        self.verticalLayout_200.setSpacing(2)
        self.verticalLayout_200.setObjectName(u"verticalLayout_200")
        self.verticalLayout_200.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_cep_cuidador_as = QLabel(self.frame_424)
        self.label_alterar_cep_cuidador_as.setObjectName(u"label_alterar_cep_cuidador_as")
        self.label_alterar_cep_cuidador_as.setMinimumSize(QSize(50, 15))
        self.label_alterar_cep_cuidador_as.setMaximumSize(QSize(50, 15))
        self.label_alterar_cep_cuidador_as.setFont(font)

        self.verticalLayout_200.addWidget(self.label_alterar_cep_cuidador_as)

        self.input_alterar_cep_cuidador_as = QLineEdit(self.frame_424)
        self.input_alterar_cep_cuidador_as.setObjectName(u"input_alterar_cep_cuidador_as")
        self.input_alterar_cep_cuidador_as.setMinimumSize(QSize(158, 30))
        self.input_alterar_cep_cuidador_as.setMaximumSize(QSize(145, 16777215))
        self.input_alterar_cep_cuidador_as.setFont(font)
        self.input_alterar_cep_cuidador_as.setStyleSheet(u"")
        self.input_alterar_cep_cuidador_as.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_200.addWidget(self.input_alterar_cep_cuidador_as)


        self.horizontalLayout_125.addWidget(self.frame_424)

        self.frame_426 = QFrame(self.frame_298)
        self.frame_426.setObjectName(u"frame_426")
        self.frame_426.setMinimumSize(QSize(22, 61))
        self.frame_426.setMaximumSize(QSize(31, 61))
        self.frame_426.setFrameShape(QFrame.StyledPanel)
        self.frame_426.setFrameShadow(QFrame.Raised)
        self.verticalLayout_292 = QVBoxLayout(self.frame_426)
        self.verticalLayout_292.setSpacing(0)
        self.verticalLayout_292.setObjectName(u"verticalLayout_292")
        self.verticalLayout_292.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_19 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_292.addItem(self.verticalSpacer_19)

        self.btn_alterar_cep_buscar_cuidador_as = QPushButton(self.frame_426)
        self.btn_alterar_cep_buscar_cuidador_as.setObjectName(u"btn_alterar_cep_buscar_cuidador_as")
        sizePolicy2.setHeightForWidth(self.btn_alterar_cep_buscar_cuidador_as.sizePolicy().hasHeightForWidth())
        self.btn_alterar_cep_buscar_cuidador_as.setSizePolicy(sizePolicy2)
        self.btn_alterar_cep_buscar_cuidador_as.setMinimumSize(QSize(0, 31))
        self.btn_alterar_cep_buscar_cuidador_as.setMaximumSize(QSize(25, 31))
        self.btn_alterar_cep_buscar_cuidador_as.setStyleSheet(u"QPushButton{\n"
"        background: rgb(243, 185, 191);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        background: rgb(255, 194, 201);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"        background: rgb(180, 106, 102);\n"
"        border: 2px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}")
        self.btn_alterar_cep_buscar_cuidador_as.setIcon(icon12)

        self.verticalLayout_292.addWidget(self.btn_alterar_cep_buscar_cuidador_as)


        self.horizontalLayout_125.addWidget(self.frame_426)


        self.horizontalLayout_99.addWidget(self.frame_298)


        self.verticalLayout_189.addWidget(self.frame_292)

        self.frame_299 = QFrame(self.frame_285)
        self.frame_299.setObjectName(u"frame_299")
        self.frame_299.setMinimumSize(QSize(0, 0))
        self.frame_299.setMaximumSize(QSize(16777215, 60))
        self.frame_299.setStyleSheet(u"")
        self.frame_299.setFrameShape(QFrame.StyledPanel)
        self.frame_299.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.frame_299)
        self.horizontalLayout_100.setSpacing(5)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.frame_300 = QFrame(self.frame_299)
        self.frame_300.setObjectName(u"frame_300")
        self.frame_300.setMinimumSize(QSize(0, 0))
        self.frame_300.setMaximumSize(QSize(360, 16777215))
        self.frame_300.setFrameShape(QFrame.StyledPanel)
        self.frame_300.setFrameShadow(QFrame.Raised)
        self.verticalLayout_201 = QVBoxLayout(self.frame_300)
        self.verticalLayout_201.setSpacing(0)
        self.verticalLayout_201.setObjectName(u"verticalLayout_201")
        self.verticalLayout_201.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_logradouro_cuidador_as = QLabel(self.frame_300)
        self.label_alterar_logradouro_cuidador_as.setObjectName(u"label_alterar_logradouro_cuidador_as")
        self.label_alterar_logradouro_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_logradouro_cuidador_as.setMaximumSize(QSize(360, 16777215))
        self.label_alterar_logradouro_cuidador_as.setFont(font)

        self.verticalLayout_201.addWidget(self.label_alterar_logradouro_cuidador_as)

        self.input_alterar_logradouro_cuidador_as = QLineEdit(self.frame_300)
        self.input_alterar_logradouro_cuidador_as.setObjectName(u"input_alterar_logradouro_cuidador_as")
        self.input_alterar_logradouro_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_logradouro_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_logradouro_cuidador_as.setFont(font)

        self.verticalLayout_201.addWidget(self.input_alterar_logradouro_cuidador_as)


        self.horizontalLayout_100.addWidget(self.frame_300)

        self.frame_301 = QFrame(self.frame_299)
        self.frame_301.setObjectName(u"frame_301")
        self.frame_301.setMinimumSize(QSize(0, 0))
        self.frame_301.setMaximumSize(QSize(150, 16777215))
        self.frame_301.setFrameShape(QFrame.StyledPanel)
        self.frame_301.setFrameShadow(QFrame.Raised)
        self.verticalLayout_202 = QVBoxLayout(self.frame_301)
        self.verticalLayout_202.setSpacing(0)
        self.verticalLayout_202.setObjectName(u"verticalLayout_202")
        self.verticalLayout_202.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_numero_cuidador_as = QLabel(self.frame_301)
        self.label_alterar_numero_cuidador_as.setObjectName(u"label_alterar_numero_cuidador_as")
        self.label_alterar_numero_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_numero_cuidador_as.setMaximumSize(QSize(160, 16777215))
        self.label_alterar_numero_cuidador_as.setFont(font)

        self.verticalLayout_202.addWidget(self.label_alterar_numero_cuidador_as)

        self.input_alterar_numero_cuidador_as = QLineEdit(self.frame_301)
        self.input_alterar_numero_cuidador_as.setObjectName(u"input_alterar_numero_cuidador_as")
        sizePolicy4.setHeightForWidth(self.input_alterar_numero_cuidador_as.sizePolicy().hasHeightForWidth())
        self.input_alterar_numero_cuidador_as.setSizePolicy(sizePolicy4)
        self.input_alterar_numero_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_numero_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_numero_cuidador_as.setFont(font)

        self.verticalLayout_202.addWidget(self.input_alterar_numero_cuidador_as)


        self.horizontalLayout_100.addWidget(self.frame_301)

        self.frame_302 = QFrame(self.frame_299)
        self.frame_302.setObjectName(u"frame_302")
        self.frame_302.setMinimumSize(QSize(0, 0))
        self.frame_302.setMaximumSize(QSize(250, 16777215))
        self.frame_302.setFrameShape(QFrame.StyledPanel)
        self.frame_302.setFrameShadow(QFrame.Raised)
        self.verticalLayout_203 = QVBoxLayout(self.frame_302)
        self.verticalLayout_203.setSpacing(0)
        self.verticalLayout_203.setObjectName(u"verticalLayout_203")
        self.verticalLayout_203.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_bairro_cuidador_as = QLabel(self.frame_302)
        self.label_alterar_bairro_cuidador_as.setObjectName(u"label_alterar_bairro_cuidador_as")
        self.label_alterar_bairro_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_bairro_cuidador_as.setMaximumSize(QSize(230, 16777215))
        self.label_alterar_bairro_cuidador_as.setFont(font)

        self.verticalLayout_203.addWidget(self.label_alterar_bairro_cuidador_as)

        self.input_alterar_bairro_cuidador_as = QLineEdit(self.frame_302)
        self.input_alterar_bairro_cuidador_as.setObjectName(u"input_alterar_bairro_cuidador_as")
        self.input_alterar_bairro_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_bairro_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_bairro_cuidador_as.setFont(font)

        self.verticalLayout_203.addWidget(self.input_alterar_bairro_cuidador_as)


        self.horizontalLayout_100.addWidget(self.frame_302)

        self.frame_303 = QFrame(self.frame_299)
        self.frame_303.setObjectName(u"frame_303")
        self.frame_303.setMinimumSize(QSize(0, 0))
        self.frame_303.setMaximumSize(QSize(240, 16777215))
        self.frame_303.setFrameShape(QFrame.StyledPanel)
        self.frame_303.setFrameShadow(QFrame.Raised)
        self.verticalLayout_204 = QVBoxLayout(self.frame_303)
        self.verticalLayout_204.setSpacing(0)
        self.verticalLayout_204.setObjectName(u"verticalLayout_204")
        self.verticalLayout_204.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_cidade_cuidador_as = QLabel(self.frame_303)
        self.label_alterar_cidade_cuidador_as.setObjectName(u"label_alterar_cidade_cuidador_as")
        self.label_alterar_cidade_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_cidade_cuidador_as.setMaximumSize(QSize(240, 16777215))
        self.label_alterar_cidade_cuidador_as.setFont(font)

        self.verticalLayout_204.addWidget(self.label_alterar_cidade_cuidador_as)

        self.input_alterar_cidade_cuidador_as = QLineEdit(self.frame_303)
        self.input_alterar_cidade_cuidador_as.setObjectName(u"input_alterar_cidade_cuidador_as")
        self.input_alterar_cidade_cuidador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_cidade_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_cidade_cuidador_as.setFont(font)

        self.verticalLayout_204.addWidget(self.input_alterar_cidade_cuidador_as)


        self.horizontalLayout_100.addWidget(self.frame_303)

        self.frame_304 = QFrame(self.frame_299)
        self.frame_304.setObjectName(u"frame_304")
        self.frame_304.setMinimumSize(QSize(0, 0))
        self.frame_304.setMaximumSize(QSize(80, 16777215))
        self.frame_304.setFrameShape(QFrame.StyledPanel)
        self.frame_304.setFrameShadow(QFrame.Raised)
        self.verticalLayout_205 = QVBoxLayout(self.frame_304)
        self.verticalLayout_205.setSpacing(0)
        self.verticalLayout_205.setObjectName(u"verticalLayout_205")
        self.verticalLayout_205.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_estado_cuidador_as = QLabel(self.frame_304)
        self.label_alterar_estado_cuidador_as.setObjectName(u"label_alterar_estado_cuidador_as")
        self.label_alterar_estado_cuidador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_estado_cuidador_as.setMaximumSize(QSize(80, 16777215))
        self.label_alterar_estado_cuidador_as.setFont(font)

        self.verticalLayout_205.addWidget(self.label_alterar_estado_cuidador_as)

        self.input_alterar_estado_cuidador_as = QLineEdit(self.frame_304)
        self.input_alterar_estado_cuidador_as.setObjectName(u"input_alterar_estado_cuidador_as")
        self.input_alterar_estado_cuidador_as.setMinimumSize(QSize(70, 30))
        self.input_alterar_estado_cuidador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_estado_cuidador_as.setFont(font)

        self.verticalLayout_205.addWidget(self.input_alterar_estado_cuidador_as)


        self.horizontalLayout_100.addWidget(self.frame_304)

        self.input_alterar_id_endereco_cuidador_as = QLineEdit(self.frame_299)
        self.input_alterar_id_endereco_cuidador_as.setObjectName(u"input_alterar_id_endereco_cuidador_as")
        self.input_alterar_id_endereco_cuidador_as.setEnabled(False)
        self.input_alterar_id_endereco_cuidador_as.setStyleSheet(u"background-color:transparent;\n"
"border-color: transparent;")

        self.horizontalLayout_100.addWidget(self.input_alterar_id_endereco_cuidador_as)


        self.verticalLayout_189.addWidget(self.frame_299)

        self.frame_305 = QFrame(self.frame_285)
        self.frame_305.setObjectName(u"frame_305")
        self.frame_305.setMinimumSize(QSize(0, 0))
        self.frame_305.setMaximumSize(QSize(16777215, 300))
        self.frame_305.setStyleSheet(u"")
        self.frame_305.setFrameShape(QFrame.StyledPanel)
        self.frame_305.setFrameShadow(QFrame.Raised)
        self.verticalLayout_206 = QVBoxLayout(self.frame_305)
        self.verticalLayout_206.setSpacing(0)
        self.verticalLayout_206.setObjectName(u"verticalLayout_206")
        self.verticalLayout_206.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_observacoes_gerais_cuidador_as = QLabel(self.frame_305)
        self.label_alterar_observacoes_gerais_cuidador_as.setObjectName(u"label_alterar_observacoes_gerais_cuidador_as")
        self.label_alterar_observacoes_gerais_cuidador_as.setMaximumSize(QSize(300, 50))
        self.label_alterar_observacoes_gerais_cuidador_as.setFont(font)

        self.verticalLayout_206.addWidget(self.label_alterar_observacoes_gerais_cuidador_as)

        self.input_alterar_informacoes_gerais_as = QTextEdit(self.frame_305)
        self.input_alterar_informacoes_gerais_as.setObjectName(u"input_alterar_informacoes_gerais_as")
        self.input_alterar_informacoes_gerais_as.setMaximumSize(QSize(1185, 235))
        self.input_alterar_informacoes_gerais_as.setFont(font)
        self.input_alterar_informacoes_gerais_as.setStyleSheet(u"QTextEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751;}\n"
"QTextEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")

        self.verticalLayout_206.addWidget(self.input_alterar_informacoes_gerais_as)


        self.verticalLayout_189.addWidget(self.frame_305)


        self.verticalLayout_207.addWidget(self.frame_285)

        self.frame_306 = QFrame(self.frame_284)
        self.frame_306.setObjectName(u"frame_306")
        self.frame_306.setMinimumSize(QSize(0, 0))
        self.frame_306.setFrameShape(QFrame.StyledPanel)
        self.frame_306.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_101 = QHBoxLayout(self.frame_306)
        self.horizontalLayout_101.setSpacing(20)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(20, 0, 0, 0)
        self.btn_alterar_voltar_cuidador_as = QPushButton(self.frame_306)
        self.btn_alterar_voltar_cuidador_as.setObjectName(u"btn_alterar_voltar_cuidador_as")
        self.btn_alterar_voltar_cuidador_as.setMinimumSize(QSize(100, 40))
        self.btn_alterar_voltar_cuidador_as.setMaximumSize(QSize(100, 40))
        self.btn_alterar_voltar_cuidador_as.setFont(font11)
        self.btn_alterar_voltar_cuidador_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_voltar_cuidador_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout_101.addWidget(self.btn_alterar_voltar_cuidador_as)

        self.horizontalSpacer_60 = QSpacerItem(1770, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_101.addItem(self.horizontalSpacer_60)

        self.btn_alterar_salvar_as = QPushButton(self.frame_306)
        self.btn_alterar_salvar_as.setObjectName(u"btn_alterar_salvar_as")
        self.btn_alterar_salvar_as.setMinimumSize(QSize(120, 40))
        self.btn_alterar_salvar_as.setFont(font11)
        self.btn_alterar_salvar_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_salvar_as.setLayoutDirection(Qt.RightToLeft)
        self.btn_alterar_salvar_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout_101.addWidget(self.btn_alterar_salvar_as)


        self.verticalLayout_207.addWidget(self.frame_306)


        self.horizontalLayout_103.addWidget(self.frame_284)


        self.horizontalLayout_97.addWidget(self.frame_282)

        self.horizontalSpacer_59 = QSpacerItem(184, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_59)


        self.verticalLayout_253.addWidget(self.frame_281)

        self.stackedWidget_8.addWidget(self.page_alterar_cuidador)
        self.page_alterar_usuario = QWidget()
        self.page_alterar_usuario.setObjectName(u"page_alterar_usuario")
        self.verticalLayout_218 = QVBoxLayout(self.page_alterar_usuario)
        self.verticalLayout_218.setSpacing(0)
        self.verticalLayout_218.setObjectName(u"verticalLayout_218")
        self.verticalLayout_218.setContentsMargins(0, 0, 0, 0)
        self.frame_283 = QFrame(self.page_alterar_usuario)
        self.frame_283.setObjectName(u"frame_283")
        self.frame_283.setFrameShape(QFrame.StyledPanel)
        self.frame_283.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_102 = QHBoxLayout(self.frame_283)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_102.addItem(self.horizontalSpacer_62)

        self.frame_307 = QFrame(self.frame_283)
        self.frame_307.setObjectName(u"frame_307")
        self.frame_307.setFrameShape(QFrame.StyledPanel)
        self.frame_307.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_307)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.frame_308 = QFrame(self.frame_307)
        self.frame_308.setObjectName(u"frame_308")
        self.frame_308.setFrameShape(QFrame.StyledPanel)
        self.frame_308.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_117 = QHBoxLayout(self.frame_308)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.frame_310 = QFrame(self.frame_308)
        self.frame_310.setObjectName(u"frame_310")
        self.frame_310.setFrameShape(QFrame.StyledPanel)
        self.frame_310.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_104 = QHBoxLayout(self.frame_310)
        self.horizontalLayout_104.setSpacing(0)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_64 = QSpacerItem(152, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_104.addItem(self.horizontalSpacer_64)

        self.frame_311 = QFrame(self.frame_310)
        self.frame_311.setObjectName(u"frame_311")
        self.frame_311.setStyleSheet(u"QLabel{margin-left: 0.25em}")
        self.frame_311.setFrameShape(QFrame.StyledPanel)
        self.frame_311.setFrameShadow(QFrame.Raised)
        self.verticalLayout_208 = QVBoxLayout(self.frame_311)
        self.verticalLayout_208.setSpacing(0)
        self.verticalLayout_208.setObjectName(u"verticalLayout_208")
        self.verticalLayout_208.setContentsMargins(20, 0, 0, 0)
        self.frame_312 = QFrame(self.frame_311)
        self.frame_312.setObjectName(u"frame_312")
        self.frame_312.setStyleSheet(u"")
        self.frame_312.setFrameShape(QFrame.StyledPanel)
        self.frame_312.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_105 = QHBoxLayout(self.frame_312)
        self.horizontalLayout_105.setSpacing(5)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.btn_alterar_foto_usuario_as = QPushButton(self.frame_312)
        self.btn_alterar_foto_usuario_as.setObjectName(u"btn_alterar_foto_usuario_as")
        self.btn_alterar_foto_usuario_as.setMinimumSize(QSize(125, 153))
        self.btn_alterar_foto_usuario_as.setMaximumSize(QSize(125, 153))
        self.btn_alterar_foto_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_foto_usuario_as.setStyleSheet(u"background-color: #F3B9BF; border: none")
        self.btn_alterar_foto_usuario_as.setIcon(icon11)
        self.btn_alterar_foto_usuario_as.setIconSize(QSize(120, 120))

        self.horizontalLayout_105.addWidget(self.btn_alterar_foto_usuario_as)

        self.frame_313 = QFrame(self.frame_312)
        self.frame_313.setObjectName(u"frame_313")
        self.frame_313.setMaximumSize(QSize(16777215, 200))
        self.frame_313.setStyleSheet(u"")
        self.frame_313.setFrameShape(QFrame.StyledPanel)
        self.frame_313.setFrameShadow(QFrame.Raised)
        self.verticalLayout_209 = QVBoxLayout(self.frame_313)
        self.verticalLayout_209.setSpacing(5)
        self.verticalLayout_209.setObjectName(u"verticalLayout_209")
        self.verticalLayout_209.setContentsMargins(0, 0, 0, 0)
        self.frame_314 = QFrame(self.frame_313)
        self.frame_314.setObjectName(u"frame_314")
        self.frame_314.setMaximumSize(QSize(16777215, 60))
        self.frame_314.setLayoutDirection(Qt.LeftToRight)
        self.frame_314.setStyleSheet(u"")
        self.frame_314.setFrameShape(QFrame.StyledPanel)
        self.frame_314.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_106 = QHBoxLayout(self.frame_314)
        self.horizontalLayout_106.setSpacing(5)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.frame_315 = QFrame(self.frame_314)
        self.frame_315.setObjectName(u"frame_315")
        self.frame_315.setMinimumSize(QSize(0, 0))
        self.frame_315.setMaximumSize(QSize(160, 16777215))
        self.frame_315.setFrameShape(QFrame.StyledPanel)
        self.frame_315.setFrameShadow(QFrame.Raised)
        self.verticalLayout_210 = QVBoxLayout(self.frame_315)
        self.verticalLayout_210.setSpacing(0)
        self.verticalLayout_210.setObjectName(u"verticalLayout_210")
        self.verticalLayout_210.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_matricula_usuario_as = QLabel(self.frame_315)
        self.label_alterar_matricula_usuario_as.setObjectName(u"label_alterar_matricula_usuario_as")
        self.label_alterar_matricula_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_matricula_usuario_as.setMaximumSize(QSize(160, 16777215))
        self.label_alterar_matricula_usuario_as.setFont(font)
        self.label_alterar_matricula_usuario_as.setStyleSheet(u"")

        self.verticalLayout_210.addWidget(self.label_alterar_matricula_usuario_as)

        self.input_alterar_matricula_usuario_as = QLineEdit(self.frame_315)
        self.input_alterar_matricula_usuario_as.setObjectName(u"input_alterar_matricula_usuario_as")
        self.input_alterar_matricula_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_matricula_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_matricula_usuario_as.setFont(font)

        self.verticalLayout_210.addWidget(self.input_alterar_matricula_usuario_as)


        self.horizontalLayout_106.addWidget(self.frame_315)

        self.frame_316 = QFrame(self.frame_314)
        self.frame_316.setObjectName(u"frame_316")
        self.frame_316.setMinimumSize(QSize(0, 0))
        self.frame_316.setMaximumSize(QSize(460, 16777215))
        self.frame_316.setFrameShape(QFrame.StyledPanel)
        self.frame_316.setFrameShadow(QFrame.Raised)
        self.verticalLayout_211 = QVBoxLayout(self.frame_316)
        self.verticalLayout_211.setSpacing(0)
        self.verticalLayout_211.setObjectName(u"verticalLayout_211")
        self.verticalLayout_211.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_nome_usuario_as = QLabel(self.frame_316)
        self.label_alterar_nome_usuario_as.setObjectName(u"label_alterar_nome_usuario_as")
        self.label_alterar_nome_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_nome_usuario_as.setMaximumSize(QSize(460, 16777215))
        self.label_alterar_nome_usuario_as.setFont(font)
        self.label_alterar_nome_usuario_as.setStyleSheet(u"")

        self.verticalLayout_211.addWidget(self.label_alterar_nome_usuario_as)

        self.input_alterar_nome_usuario_as = QLineEdit(self.frame_316)
        self.input_alterar_nome_usuario_as.setObjectName(u"input_alterar_nome_usuario_as")
        self.input_alterar_nome_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_nome_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_nome_usuario_as.setFont(font)

        self.verticalLayout_211.addWidget(self.input_alterar_nome_usuario_as)


        self.horizontalLayout_106.addWidget(self.frame_316)

        self.frame_317 = QFrame(self.frame_314)
        self.frame_317.setObjectName(u"frame_317")
        self.frame_317.setMinimumSize(QSize(0, 0))
        self.frame_317.setMaximumSize(QSize(160, 16777215))
        self.frame_317.setFrameShape(QFrame.StyledPanel)
        self.frame_317.setFrameShadow(QFrame.Raised)
        self.verticalLayout_212 = QVBoxLayout(self.frame_317)
        self.verticalLayout_212.setSpacing(5)
        self.verticalLayout_212.setObjectName(u"verticalLayout_212")
        self.verticalLayout_212.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_nascimento_usuario_as = QLabel(self.frame_317)
        self.label_alterar_nascimento_usuario_as.setObjectName(u"label_alterar_nascimento_usuario_as")
        self.label_alterar_nascimento_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_nascimento_usuario_as.setMaximumSize(QSize(160, 16777215))
        self.label_alterar_nascimento_usuario_as.setFont(font)
        self.label_alterar_nascimento_usuario_as.setStyleSheet(u"")

        self.verticalLayout_212.addWidget(self.label_alterar_nascimento_usuario_as)

        self.input_alterar_nascimento_usuario_as = QDateEdit(self.frame_317)
        self.input_alterar_nascimento_usuario_as.setObjectName(u"input_alterar_nascimento_usuario_as")
        sizePolicy1.setHeightForWidth(self.input_alterar_nascimento_usuario_as.sizePolicy().hasHeightForWidth())
        self.input_alterar_nascimento_usuario_as.setSizePolicy(sizePolicy1)
        self.input_alterar_nascimento_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_nascimento_usuario_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_alterar_nascimento_usuario_as.setFont(font8)
        self.input_alterar_nascimento_usuario_as.setFocusPolicy(Qt.WheelFocus)
        self.input_alterar_nascimento_usuario_as.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.input_alterar_nascimento_usuario_as.setLayoutDirection(Qt.LeftToRight)
        self.input_alterar_nascimento_usuario_as.setAutoFillBackground(False)
        self.input_alterar_nascimento_usuario_as.setStyleSheet(u"QDateEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QDateEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_alterar_nascimento_usuario_as.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.input_alterar_nascimento_usuario_as.setAlignment(Qt.AlignCenter)
        self.input_alterar_nascimento_usuario_as.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.input_alterar_nascimento_usuario_as.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.input_alterar_nascimento_usuario_as.setCurrentSection(QDateTimeEdit.DaySection)
        self.input_alterar_nascimento_usuario_as.setCalendarPopup(False)
        self.input_alterar_nascimento_usuario_as.setCurrentSectionIndex(0)

        self.verticalLayout_212.addWidget(self.input_alterar_nascimento_usuario_as, 0, Qt.AlignHCenter)


        self.horizontalLayout_106.addWidget(self.frame_317)

        self.frame_318 = QFrame(self.frame_314)
        self.frame_318.setObjectName(u"frame_318")
        self.frame_318.setMinimumSize(QSize(195, 50))
        self.frame_318.setMaximumSize(QSize(195, 50))
        self.frame_318.setStyleSheet(u"background-color: #EC848C; border-radius: 10px")
        self.frame_318.setFrameShape(QFrame.StyledPanel)
        self.frame_318.setFrameShadow(QFrame.Raised)
        self.verticalLayout_213 = QVBoxLayout(self.frame_318)
        self.verticalLayout_213.setSpacing(6)
        self.verticalLayout_213.setObjectName(u"verticalLayout_213")
        self.verticalLayout_213.setContentsMargins(15, 0, 0, 0)
        self.label_alterar_situacao_usuario_as = QLabel(self.frame_318)
        self.label_alterar_situacao_usuario_as.setObjectName(u"label_alterar_situacao_usuario_as")
        self.label_alterar_situacao_usuario_as.setMaximumSize(QSize(130, 16777215))
        self.label_alterar_situacao_usuario_as.setFont(font)

        self.verticalLayout_213.addWidget(self.label_alterar_situacao_usuario_as)

        self.frame_319 = QFrame(self.frame_318)
        self.frame_319.setObjectName(u"frame_319")
        self.frame_319.setFrameShape(QFrame.StyledPanel)
        self.frame_319.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.frame_319)
        self.horizontalLayout_107.setSpacing(0)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.input_alterar_situacao_ativo_usuario_as = QRadioButton(self.frame_319)
        self.input_alterar_situacao_ativo_usuario_as.setObjectName(u"input_alterar_situacao_ativo_usuario_as")
        self.input_alterar_situacao_ativo_usuario_as.setMaximumSize(QSize(80, 16777215))
        self.input_alterar_situacao_ativo_usuario_as.setFont(font8)
        self.input_alterar_situacao_ativo_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_107.addWidget(self.input_alterar_situacao_ativo_usuario_as)

        self.input_alterar_situacao_inativo_usuario_as = QRadioButton(self.frame_319)
        self.input_alterar_situacao_inativo_usuario_as.setObjectName(u"input_alterar_situacao_inativo_usuario_as")
        self.input_alterar_situacao_inativo_usuario_as.setMaximumSize(QSize(80, 16777215))
        self.input_alterar_situacao_inativo_usuario_as.setFont(font8)
        self.input_alterar_situacao_inativo_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_107.addWidget(self.input_alterar_situacao_inativo_usuario_as)


        self.verticalLayout_213.addWidget(self.frame_319)


        self.horizontalLayout_106.addWidget(self.frame_318)


        self.verticalLayout_209.addWidget(self.frame_314)

        self.frame_320 = QFrame(self.frame_313)
        self.frame_320.setObjectName(u"frame_320")
        self.frame_320.setMaximumSize(QSize(16777215, 60))
        self.frame_320.setStyleSheet(u"")
        self.frame_320.setFrameShape(QFrame.StyledPanel)
        self.frame_320.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_108 = QHBoxLayout(self.frame_320)
        self.horizontalLayout_108.setSpacing(5)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.frame_321 = QFrame(self.frame_320)
        self.frame_321.setObjectName(u"frame_321")
        self.frame_321.setMinimumSize(QSize(0, 0))
        self.frame_321.setMaximumSize(QSize(180, 16777215))
        self.frame_321.setFrameShape(QFrame.StyledPanel)
        self.frame_321.setFrameShadow(QFrame.Raised)
        self.verticalLayout_214 = QVBoxLayout(self.frame_321)
        self.verticalLayout_214.setSpacing(0)
        self.verticalLayout_214.setObjectName(u"verticalLayout_214")
        self.verticalLayout_214.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_cpf_usuario_as = QLabel(self.frame_321)
        self.label_alterar_cpf_usuario_as.setObjectName(u"label_alterar_cpf_usuario_as")
        self.label_alterar_cpf_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_cpf_usuario_as.setMaximumSize(QSize(180, 16777215))
        self.label_alterar_cpf_usuario_as.setFont(font)

        self.verticalLayout_214.addWidget(self.label_alterar_cpf_usuario_as)

        self.input_alterar_cpf_usuario_as = QLineEdit(self.frame_321)
        self.input_alterar_cpf_usuario_as.setObjectName(u"input_alterar_cpf_usuario_as")
        self.input_alterar_cpf_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_cpf_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_cpf_usuario_as.setFont(font)

        self.verticalLayout_214.addWidget(self.input_alterar_cpf_usuario_as)


        self.horizontalLayout_108.addWidget(self.frame_321)

        self.frame_322 = QFrame(self.frame_320)
        self.frame_322.setObjectName(u"frame_322")
        self.frame_322.setMinimumSize(QSize(0, 0))
        self.frame_322.setMaximumSize(QSize(160, 16777215))
        self.frame_322.setFrameShape(QFrame.StyledPanel)
        self.frame_322.setFrameShadow(QFrame.Raised)
        self.verticalLayout_215 = QVBoxLayout(self.frame_322)
        self.verticalLayout_215.setSpacing(0)
        self.verticalLayout_215.setObjectName(u"verticalLayout_215")
        self.verticalLayout_215.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_rg_usuario_as = QLabel(self.frame_322)
        self.label_alterar_rg_usuario_as.setObjectName(u"label_alterar_rg_usuario_as")
        self.label_alterar_rg_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_rg_usuario_as.setMaximumSize(QSize(160, 16777215))
        self.label_alterar_rg_usuario_as.setFont(font)

        self.verticalLayout_215.addWidget(self.label_alterar_rg_usuario_as)

        self.input_alterar_rg_usuario_as = QLineEdit(self.frame_322)
        self.input_alterar_rg_usuario_as.setObjectName(u"input_alterar_rg_usuario_as")
        self.input_alterar_rg_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_rg_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_rg_usuario_as.setFont(font)

        self.verticalLayout_215.addWidget(self.input_alterar_rg_usuario_as)


        self.horizontalLayout_108.addWidget(self.frame_322)

        self.frame_323 = QFrame(self.frame_320)
        self.frame_323.setObjectName(u"frame_323")
        self.frame_323.setMinimumSize(QSize(0, 0))
        self.frame_323.setMaximumSize(QSize(155, 16777215))
        self.frame_323.setFrameShape(QFrame.StyledPanel)
        self.frame_323.setFrameShadow(QFrame.Raised)
        self.verticalLayout_216 = QVBoxLayout(self.frame_323)
        self.verticalLayout_216.setSpacing(5)
        self.verticalLayout_216.setObjectName(u"verticalLayout_216")
        self.verticalLayout_216.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_data_emissao_usuario_as = QLabel(self.frame_323)
        self.label_alterar_data_emissao_usuario_as.setObjectName(u"label_alterar_data_emissao_usuario_as")
        self.label_alterar_data_emissao_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_data_emissao_usuario_as.setMaximumSize(QSize(155, 16777215))
        self.label_alterar_data_emissao_usuario_as.setFont(font)

        self.verticalLayout_216.addWidget(self.label_alterar_data_emissao_usuario_as)

        self.input_alterar_data_emissao_usuario_as = QDateEdit(self.frame_323)
        self.input_alterar_data_emissao_usuario_as.setObjectName(u"input_alterar_data_emissao_usuario_as")
        sizePolicy1.setHeightForWidth(self.input_alterar_data_emissao_usuario_as.sizePolicy().hasHeightForWidth())
        self.input_alterar_data_emissao_usuario_as.setSizePolicy(sizePolicy1)
        self.input_alterar_data_emissao_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_data_emissao_usuario_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_alterar_data_emissao_usuario_as.setFont(font8)
        self.input_alterar_data_emissao_usuario_as.setFocusPolicy(Qt.WheelFocus)
        self.input_alterar_data_emissao_usuario_as.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.input_alterar_data_emissao_usuario_as.setLayoutDirection(Qt.LeftToRight)
        self.input_alterar_data_emissao_usuario_as.setAutoFillBackground(False)
        self.input_alterar_data_emissao_usuario_as.setStyleSheet(u"QDateEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QDateEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_alterar_data_emissao_usuario_as.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.input_alterar_data_emissao_usuario_as.setAlignment(Qt.AlignCenter)
        self.input_alterar_data_emissao_usuario_as.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.input_alterar_data_emissao_usuario_as.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.input_alterar_data_emissao_usuario_as.setCurrentSection(QDateTimeEdit.DaySection)
        self.input_alterar_data_emissao_usuario_as.setCalendarPopup(False)
        self.input_alterar_data_emissao_usuario_as.setCurrentSectionIndex(0)

        self.verticalLayout_216.addWidget(self.input_alterar_data_emissao_usuario_as, 0, Qt.AlignHCenter)


        self.horizontalLayout_108.addWidget(self.frame_323)

        self.frame_324 = QFrame(self.frame_320)
        self.frame_324.setObjectName(u"frame_324")
        self.frame_324.setMinimumSize(QSize(0, 0))
        self.frame_324.setMaximumSize(QSize(155, 16777215))
        self.frame_324.setFrameShape(QFrame.StyledPanel)
        self.frame_324.setFrameShadow(QFrame.Raised)
        self.verticalLayout_217 = QVBoxLayout(self.frame_324)
        self.verticalLayout_217.setSpacing(0)
        self.verticalLayout_217.setObjectName(u"verticalLayout_217")
        self.verticalLayout_217.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_orgao_expedidor_usuario_as = QLabel(self.frame_324)
        self.label_alterar_orgao_expedidor_usuario_as.setObjectName(u"label_alterar_orgao_expedidor_usuario_as")
        self.label_alterar_orgao_expedidor_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_orgao_expedidor_usuario_as.setMaximumSize(QSize(155, 16777215))
        self.label_alterar_orgao_expedidor_usuario_as.setFont(font)

        self.verticalLayout_217.addWidget(self.label_alterar_orgao_expedidor_usuario_as)

        self.input_alterar_orgao_expedidor_usuario_as = QLineEdit(self.frame_324)
        self.input_alterar_orgao_expedidor_usuario_as.setObjectName(u"input_alterar_orgao_expedidor_usuario_as")
        self.input_alterar_orgao_expedidor_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_orgao_expedidor_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_orgao_expedidor_usuario_as.setFont(font)

        self.verticalLayout_217.addWidget(self.input_alterar_orgao_expedidor_usuario_as)


        self.horizontalLayout_108.addWidget(self.frame_324)

        self.frame_325 = QFrame(self.frame_320)
        self.frame_325.setObjectName(u"frame_325")
        self.frame_325.setMinimumSize(QSize(0, 0))
        self.frame_325.setMaximumSize(QSize(170, 16777215))
        self.frame_325.setFrameShape(QFrame.StyledPanel)
        self.frame_325.setFrameShadow(QFrame.Raised)
        self.verticalLayout_219 = QVBoxLayout(self.frame_325)
        self.verticalLayout_219.setSpacing(0)
        self.verticalLayout_219.setObjectName(u"verticalLayout_219")
        self.verticalLayout_219.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_nis_usuario_as = QLabel(self.frame_325)
        self.label_alterar_nis_usuario_as.setObjectName(u"label_alterar_nis_usuario_as")
        self.label_alterar_nis_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_nis_usuario_as.setMaximumSize(QSize(170, 16777215))
        self.label_alterar_nis_usuario_as.setFont(font)

        self.verticalLayout_219.addWidget(self.label_alterar_nis_usuario_as)

        self.input_alterar_nis_usuario_as = QLineEdit(self.frame_325)
        self.input_alterar_nis_usuario_as.setObjectName(u"input_alterar_nis_usuario_as")
        self.input_alterar_nis_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_nis_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_nis_usuario_as.setFont(font)

        self.verticalLayout_219.addWidget(self.input_alterar_nis_usuario_as)


        self.horizontalLayout_108.addWidget(self.frame_325)

        self.frame_326 = QFrame(self.frame_320)
        self.frame_326.setObjectName(u"frame_326")
        self.frame_326.setMinimumSize(QSize(0, 0))
        self.frame_326.setMaximumSize(QSize(180, 16777215))
        self.frame_326.setFrameShape(QFrame.StyledPanel)
        self.frame_326.setFrameShadow(QFrame.Raised)
        self.verticalLayout_220 = QVBoxLayout(self.frame_326)
        self.verticalLayout_220.setSpacing(0)
        self.verticalLayout_220.setObjectName(u"verticalLayout_220")
        self.verticalLayout_220.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_cns_usuario_as = QLabel(self.frame_326)
        self.label_alterar_cns_usuario_as.setObjectName(u"label_alterar_cns_usuario_as")
        self.label_alterar_cns_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_cns_usuario_as.setMaximumSize(QSize(180, 16777215))
        self.label_alterar_cns_usuario_as.setFont(font)

        self.verticalLayout_220.addWidget(self.label_alterar_cns_usuario_as)

        self.input_alterar_cns_usuario_as = QLineEdit(self.frame_326)
        self.input_alterar_cns_usuario_as.setObjectName(u"input_alterar_cns_usuario_as")
        self.input_alterar_cns_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_cns_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_cns_usuario_as.setFont(font)
        self.input_alterar_cns_usuario_as.setInputMethodHints(Qt.ImhNone)

        self.verticalLayout_220.addWidget(self.input_alterar_cns_usuario_as)


        self.horizontalLayout_108.addWidget(self.frame_326)


        self.verticalLayout_209.addWidget(self.frame_320)

        self.frame_327 = QFrame(self.frame_313)
        self.frame_327.setObjectName(u"frame_327")
        self.frame_327.setMaximumSize(QSize(16777215, 60))
        self.frame_327.setFont(font9)
        self.frame_327.setStyleSheet(u"")
        self.frame_327.setFrameShape(QFrame.StyledPanel)
        self.frame_327.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_109 = QHBoxLayout(self.frame_327)
        self.horizontalLayout_109.setSpacing(5)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.frame_328 = QFrame(self.frame_327)
        self.frame_328.setObjectName(u"frame_328")
        self.frame_328.setMinimumSize(QSize(0, 0))
        self.frame_328.setMaximumSize(QSize(155, 16777215))
        self.frame_328.setFrameShape(QFrame.StyledPanel)
        self.frame_328.setFrameShadow(QFrame.Raised)
        self.verticalLayout_221 = QVBoxLayout(self.frame_328)
        self.verticalLayout_221.setSpacing(5)
        self.verticalLayout_221.setObjectName(u"verticalLayout_221")
        self.verticalLayout_221.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_sexo_usuario_as = QLabel(self.frame_328)
        self.label_alterar_sexo_usuario_as.setObjectName(u"label_alterar_sexo_usuario_as")
        self.label_alterar_sexo_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_sexo_usuario_as.setMaximumSize(QSize(155, 16777215))
        self.label_alterar_sexo_usuario_as.setFont(font)

        self.verticalLayout_221.addWidget(self.label_alterar_sexo_usuario_as)

        self.input_alterar_sexo_usuario_as = QComboBox(self.frame_328)
        self.input_alterar_sexo_usuario_as.addItem("")
        self.input_alterar_sexo_usuario_as.addItem("")
        self.input_alterar_sexo_usuario_as.addItem("")
        self.input_alterar_sexo_usuario_as.setObjectName(u"input_alterar_sexo_usuario_as")
        self.input_alterar_sexo_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_sexo_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_sexo_usuario_as.setFont(font)

        self.verticalLayout_221.addWidget(self.input_alterar_sexo_usuario_as)


        self.horizontalLayout_109.addWidget(self.frame_328)

        self.frame_329 = QFrame(self.frame_327)
        self.frame_329.setObjectName(u"frame_329")
        self.frame_329.setMinimumSize(QSize(0, 0))
        self.frame_329.setMaximumSize(QSize(155, 16777215))
        self.frame_329.setStyleSheet(u"")
        self.frame_329.setFrameShape(QFrame.StyledPanel)
        self.frame_329.setFrameShadow(QFrame.Raised)
        self.verticalLayout_222 = QVBoxLayout(self.frame_329)
        self.verticalLayout_222.setSpacing(0)
        self.verticalLayout_222.setObjectName(u"verticalLayout_222")
        self.verticalLayout_222.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_telefone_usuario_as = QLabel(self.frame_329)
        self.label_alterar_telefone_usuario_as.setObjectName(u"label_alterar_telefone_usuario_as")
        self.label_alterar_telefone_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_telefone_usuario_as.setMaximumSize(QSize(155, 16777215))
        self.label_alterar_telefone_usuario_as.setFont(font)

        self.verticalLayout_222.addWidget(self.label_alterar_telefone_usuario_as)

        self.input_alterar_telefone_usuario_as = QLineEdit(self.frame_329)
        self.input_alterar_telefone_usuario_as.setObjectName(u"input_alterar_telefone_usuario_as")
        self.input_alterar_telefone_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_telefone_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_telefone_usuario_as.setFont(font)

        self.verticalLayout_222.addWidget(self.input_alterar_telefone_usuario_as)


        self.horizontalLayout_109.addWidget(self.frame_329)

        self.frame_330 = QFrame(self.frame_327)
        self.frame_330.setObjectName(u"frame_330")
        self.frame_330.setMinimumSize(QSize(0, 0))
        self.frame_330.setMaximumSize(QSize(240, 16777215))
        self.frame_330.setFrameShape(QFrame.StyledPanel)
        self.frame_330.setFrameShadow(QFrame.Raised)
        self.verticalLayout_223 = QVBoxLayout(self.frame_330)
        self.verticalLayout_223.setSpacing(0)
        self.verticalLayout_223.setObjectName(u"verticalLayout_223")
        self.verticalLayout_223.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_email_usuario_as = QLabel(self.frame_330)
        self.label_alterar_email_usuario_as.setObjectName(u"label_alterar_email_usuario_as")
        self.label_alterar_email_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_email_usuario_as.setMaximumSize(QSize(240, 16777215))
        self.label_alterar_email_usuario_as.setFont(font)

        self.verticalLayout_223.addWidget(self.label_alterar_email_usuario_as)

        self.input_alterar_email_usuario_as = QLineEdit(self.frame_330)
        self.input_alterar_email_usuario_as.setObjectName(u"input_alterar_email_usuario_as")
        self.input_alterar_email_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_email_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_email_usuario_as.setFont(font)

        self.verticalLayout_223.addWidget(self.input_alterar_email_usuario_as)


        self.horizontalLayout_109.addWidget(self.frame_330)

        self.frame_331 = QFrame(self.frame_327)
        self.frame_331.setObjectName(u"frame_331")
        self.frame_331.setMinimumSize(QSize(0, 0))
        self.frame_331.setMaximumSize(QSize(160, 16777215))
        self.frame_331.setFrameShape(QFrame.StyledPanel)
        self.frame_331.setFrameShadow(QFrame.Raised)
        self.verticalLayout_224 = QVBoxLayout(self.frame_331)
        self.verticalLayout_224.setSpacing(0)
        self.verticalLayout_224.setObjectName(u"verticalLayout_224")
        self.verticalLayout_224.setContentsMargins(0, 0, 0, 0)
        self.frame_427 = QFrame(self.frame_331)
        self.frame_427.setObjectName(u"frame_427")
        self.frame_427.setMinimumSize(QSize(0, 0))
        self.frame_427.setMaximumSize(QSize(170, 16777215))
        self.frame_427.setFrameShape(QFrame.StyledPanel)
        self.frame_427.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_127 = QHBoxLayout(self.frame_427)
        self.horizontalLayout_127.setSpacing(0)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.frame_428 = QFrame(self.frame_427)
        self.frame_428.setObjectName(u"frame_428")
        self.frame_428.setMinimumSize(QSize(160, 61))
        self.frame_428.setMaximumSize(QSize(150, 61))
        self.frame_428.setFrameShape(QFrame.StyledPanel)
        self.frame_428.setFrameShadow(QFrame.Raised)
        self.verticalLayout_293 = QVBoxLayout(self.frame_428)
        self.verticalLayout_293.setSpacing(0)
        self.verticalLayout_293.setObjectName(u"verticalLayout_293")
        self.verticalLayout_293.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_cep_usuario_as = QLabel(self.frame_428)
        self.label_alterar_cep_usuario_as.setObjectName(u"label_alterar_cep_usuario_as")
        self.label_alterar_cep_usuario_as.setMinimumSize(QSize(50, 15))
        self.label_alterar_cep_usuario_as.setMaximumSize(QSize(50, 15))
        self.label_alterar_cep_usuario_as.setFont(font)

        self.verticalLayout_293.addWidget(self.label_alterar_cep_usuario_as)

        self.input_alterar_cep_usuario_as = QLineEdit(self.frame_428)
        self.input_alterar_cep_usuario_as.setObjectName(u"input_alterar_cep_usuario_as")
        self.input_alterar_cep_usuario_as.setMinimumSize(QSize(154, 30))
        self.input_alterar_cep_usuario_as.setMaximumSize(QSize(145, 16777215))
        self.input_alterar_cep_usuario_as.setFont(font)
        self.input_alterar_cep_usuario_as.setStyleSheet(u"")
        self.input_alterar_cep_usuario_as.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_293.addWidget(self.input_alterar_cep_usuario_as)


        self.horizontalLayout_127.addWidget(self.frame_428)

        self.frame_429 = QFrame(self.frame_427)
        self.frame_429.setObjectName(u"frame_429")
        self.frame_429.setMinimumSize(QSize(22, 61))
        self.frame_429.setMaximumSize(QSize(31, 61))
        self.frame_429.setFrameShape(QFrame.StyledPanel)
        self.frame_429.setFrameShadow(QFrame.Raised)
        self.verticalLayout_294 = QVBoxLayout(self.frame_429)
        self.verticalLayout_294.setSpacing(0)
        self.verticalLayout_294.setObjectName(u"verticalLayout_294")
        self.verticalLayout_294.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_20 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_294.addItem(self.verticalSpacer_20)

        self.btn_alterar_cep_buscar_usuario_as = QPushButton(self.frame_429)
        self.btn_alterar_cep_buscar_usuario_as.setObjectName(u"btn_alterar_cep_buscar_usuario_as")
        sizePolicy2.setHeightForWidth(self.btn_alterar_cep_buscar_usuario_as.sizePolicy().hasHeightForWidth())
        self.btn_alterar_cep_buscar_usuario_as.setSizePolicy(sizePolicy2)
        self.btn_alterar_cep_buscar_usuario_as.setMinimumSize(QSize(0, 31))
        self.btn_alterar_cep_buscar_usuario_as.setMaximumSize(QSize(25, 31))
        self.btn_alterar_cep_buscar_usuario_as.setStyleSheet(u"QPushButton{\n"
"        background: rgb(243, 185, 191);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        background: rgb(255, 194, 201);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"        background: rgb(180, 106, 102);\n"
"        border: 2px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}")
        self.btn_alterar_cep_buscar_usuario_as.setIcon(icon12)

        self.verticalLayout_294.addWidget(self.btn_alterar_cep_buscar_usuario_as)


        self.horizontalLayout_127.addWidget(self.frame_429)


        self.verticalLayout_224.addWidget(self.frame_427)


        self.horizontalLayout_109.addWidget(self.frame_331)

        self.frame_332 = QFrame(self.frame_327)
        self.frame_332.setObjectName(u"frame_332")
        self.frame_332.setMinimumSize(QSize(0, 0))
        self.frame_332.setMaximumSize(QSize(360, 16777215))
        self.frame_332.setFrameShape(QFrame.StyledPanel)
        self.frame_332.setFrameShadow(QFrame.Raised)
        self.verticalLayout_225 = QVBoxLayout(self.frame_332)
        self.verticalLayout_225.setSpacing(0)
        self.verticalLayout_225.setObjectName(u"verticalLayout_225")
        self.verticalLayout_225.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_logradouro_usuario_as = QLabel(self.frame_332)
        self.label_alterar_logradouro_usuario_as.setObjectName(u"label_alterar_logradouro_usuario_as")
        self.label_alterar_logradouro_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_logradouro_usuario_as.setMaximumSize(QSize(360, 16777215))
        self.label_alterar_logradouro_usuario_as.setFont(font)

        self.verticalLayout_225.addWidget(self.label_alterar_logradouro_usuario_as)

        self.input_alterar_logradouro_usuario_as = QLineEdit(self.frame_332)
        self.input_alterar_logradouro_usuario_as.setObjectName(u"input_alterar_logradouro_usuario_as")
        self.input_alterar_logradouro_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_logradouro_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_logradouro_usuario_as.setFont(font)
        self.input_alterar_logradouro_usuario_as.setStyleSheet(u"")

        self.verticalLayout_225.addWidget(self.input_alterar_logradouro_usuario_as)


        self.horizontalLayout_109.addWidget(self.frame_332)


        self.verticalLayout_209.addWidget(self.frame_327)


        self.horizontalLayout_105.addWidget(self.frame_313)


        self.verticalLayout_208.addWidget(self.frame_312)

        self.frame_333 = QFrame(self.frame_311)
        self.frame_333.setObjectName(u"frame_333")
        self.frame_333.setMaximumSize(QSize(16777215, 60))
        self.frame_333.setStyleSheet(u"")
        self.frame_333.setFrameShape(QFrame.StyledPanel)
        self.frame_333.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_110 = QHBoxLayout(self.frame_333)
        self.horizontalLayout_110.setSpacing(5)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.frame_334 = QFrame(self.frame_333)
        self.frame_334.setObjectName(u"frame_334")
        self.frame_334.setMinimumSize(QSize(0, 0))
        self.frame_334.setMaximumSize(QSize(170, 16777215))
        self.frame_334.setFrameShape(QFrame.StyledPanel)
        self.frame_334.setFrameShadow(QFrame.Raised)
        self.verticalLayout_226 = QVBoxLayout(self.frame_334)
        self.verticalLayout_226.setSpacing(0)
        self.verticalLayout_226.setObjectName(u"verticalLayout_226")
        self.verticalLayout_226.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_numero_usuario_as = QLabel(self.frame_334)
        self.label_alterar_numero_usuario_as.setObjectName(u"label_alterar_numero_usuario_as")
        self.label_alterar_numero_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_numero_usuario_as.setMaximumSize(QSize(170, 16777215))
        self.label_alterar_numero_usuario_as.setFont(font)

        self.verticalLayout_226.addWidget(self.label_alterar_numero_usuario_as)

        self.input_alterar_numero_usuario_as = QLineEdit(self.frame_334)
        self.input_alterar_numero_usuario_as.setObjectName(u"input_alterar_numero_usuario_as")
        self.input_alterar_numero_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_numero_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_numero_usuario_as.setFont(font)

        self.verticalLayout_226.addWidget(self.input_alterar_numero_usuario_as)


        self.horizontalLayout_110.addWidget(self.frame_334)

        self.frame_335 = QFrame(self.frame_333)
        self.frame_335.setObjectName(u"frame_335")
        self.frame_335.setMinimumSize(QSize(0, 0))
        self.frame_335.setMaximumSize(QSize(230, 16777215))
        self.frame_335.setFrameShape(QFrame.StyledPanel)
        self.frame_335.setFrameShadow(QFrame.Raised)
        self.verticalLayout_227 = QVBoxLayout(self.frame_335)
        self.verticalLayout_227.setSpacing(0)
        self.verticalLayout_227.setObjectName(u"verticalLayout_227")
        self.verticalLayout_227.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_bairro_usuario_as = QLabel(self.frame_335)
        self.label_alterar_bairro_usuario_as.setObjectName(u"label_alterar_bairro_usuario_as")
        self.label_alterar_bairro_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_bairro_usuario_as.setMaximumSize(QSize(230, 16777215))
        self.label_alterar_bairro_usuario_as.setFont(font)

        self.verticalLayout_227.addWidget(self.label_alterar_bairro_usuario_as)

        self.input_alterar_bairro_usuario_as = QLineEdit(self.frame_335)
        self.input_alterar_bairro_usuario_as.setObjectName(u"input_alterar_bairro_usuario_as")
        self.input_alterar_bairro_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_bairro_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_bairro_usuario_as.setFont(font)

        self.verticalLayout_227.addWidget(self.input_alterar_bairro_usuario_as)


        self.horizontalLayout_110.addWidget(self.frame_335)

        self.frame_336 = QFrame(self.frame_333)
        self.frame_336.setObjectName(u"frame_336")
        self.frame_336.setMinimumSize(QSize(0, 0))
        self.frame_336.setMaximumSize(QSize(240, 16777215))
        self.frame_336.setFrameShape(QFrame.StyledPanel)
        self.frame_336.setFrameShadow(QFrame.Raised)
        self.verticalLayout_228 = QVBoxLayout(self.frame_336)
        self.verticalLayout_228.setSpacing(0)
        self.verticalLayout_228.setObjectName(u"verticalLayout_228")
        self.verticalLayout_228.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_cidade_usuario_as = QLabel(self.frame_336)
        self.label_alterar_cidade_usuario_as.setObjectName(u"label_alterar_cidade_usuario_as")
        self.label_alterar_cidade_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_cidade_usuario_as.setMaximumSize(QSize(240, 16777215))
        self.label_alterar_cidade_usuario_as.setFont(font)

        self.verticalLayout_228.addWidget(self.label_alterar_cidade_usuario_as)

        self.input_alterar_cidade_usuario_as = QLineEdit(self.frame_336)
        self.input_alterar_cidade_usuario_as.setObjectName(u"input_alterar_cidade_usuario_as")
        self.input_alterar_cidade_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_cidade_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_cidade_usuario_as.setFont(font)

        self.verticalLayout_228.addWidget(self.input_alterar_cidade_usuario_as)


        self.horizontalLayout_110.addWidget(self.frame_336)

        self.frame_337 = QFrame(self.frame_333)
        self.frame_337.setObjectName(u"frame_337")
        self.frame_337.setMinimumSize(QSize(80, 0))
        self.frame_337.setMaximumSize(QSize(80, 16777215))
        self.frame_337.setFrameShape(QFrame.StyledPanel)
        self.frame_337.setFrameShadow(QFrame.Raised)
        self.verticalLayout_229 = QVBoxLayout(self.frame_337)
        self.verticalLayout_229.setSpacing(0)
        self.verticalLayout_229.setObjectName(u"verticalLayout_229")
        self.verticalLayout_229.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_estado_usuario_as = QLabel(self.frame_337)
        self.label_alterar_estado_usuario_as.setObjectName(u"label_alterar_estado_usuario_as")
        self.label_alterar_estado_usuario_as.setMinimumSize(QSize(80, 0))
        self.label_alterar_estado_usuario_as.setMaximumSize(QSize(80, 16777215))
        self.label_alterar_estado_usuario_as.setFont(font)

        self.verticalLayout_229.addWidget(self.label_alterar_estado_usuario_as)

        self.input_alterar_estado_usuario_as = QLineEdit(self.frame_337)
        self.input_alterar_estado_usuario_as.setObjectName(u"input_alterar_estado_usuario_as")
        self.input_alterar_estado_usuario_as.setMinimumSize(QSize(70, 30))
        self.input_alterar_estado_usuario_as.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_229.addWidget(self.input_alterar_estado_usuario_as)


        self.horizontalLayout_110.addWidget(self.frame_337)

        self.frame_338 = QFrame(self.frame_333)
        self.frame_338.setObjectName(u"frame_338")
        self.frame_338.setMinimumSize(QSize(0, 0))
        self.frame_338.setMaximumSize(QSize(210, 16777215))
        self.frame_338.setFrameShape(QFrame.StyledPanel)
        self.frame_338.setFrameShadow(QFrame.Raised)
        self.verticalLayout_230 = QVBoxLayout(self.frame_338)
        self.verticalLayout_230.setSpacing(5)
        self.verticalLayout_230.setObjectName(u"verticalLayout_230")
        self.verticalLayout_230.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_estado_civil_usuario_as = QLabel(self.frame_338)
        self.label_alterar_estado_civil_usuario_as.setObjectName(u"label_alterar_estado_civil_usuario_as")
        self.label_alterar_estado_civil_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_estado_civil_usuario_as.setMaximumSize(QSize(210, 16777215))
        self.label_alterar_estado_civil_usuario_as.setFont(font)

        self.verticalLayout_230.addWidget(self.label_alterar_estado_civil_usuario_as)

        self.input_alterar_estado_civil_usuario_as = QComboBox(self.frame_338)
        self.input_alterar_estado_civil_usuario_as.addItem("")
        self.input_alterar_estado_civil_usuario_as.addItem("")
        self.input_alterar_estado_civil_usuario_as.addItem("")
        self.input_alterar_estado_civil_usuario_as.addItem("")
        self.input_alterar_estado_civil_usuario_as.addItem("")
        self.input_alterar_estado_civil_usuario_as.addItem("")
        self.input_alterar_estado_civil_usuario_as.setObjectName(u"input_alterar_estado_civil_usuario_as")
        self.input_alterar_estado_civil_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_estado_civil_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_estado_civil_usuario_as.setFont(font)

        self.verticalLayout_230.addWidget(self.input_alterar_estado_civil_usuario_as)


        self.horizontalLayout_110.addWidget(self.frame_338)

        self.frame_339 = QFrame(self.frame_333)
        self.frame_339.setObjectName(u"frame_339")
        self.frame_339.setMinimumSize(QSize(0, 0))
        self.frame_339.setMaximumSize(QSize(290, 16777215))
        self.frame_339.setFrameShape(QFrame.StyledPanel)
        self.frame_339.setFrameShadow(QFrame.Raised)
        self.verticalLayout_231 = QVBoxLayout(self.frame_339)
        self.verticalLayout_231.setSpacing(5)
        self.verticalLayout_231.setObjectName(u"verticalLayout_231")
        self.verticalLayout_231.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_escolaridade_usuario_as = QLabel(self.frame_339)
        self.label_alterar_escolaridade_usuario_as.setObjectName(u"label_alterar_escolaridade_usuario_as")
        self.label_alterar_escolaridade_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_escolaridade_usuario_as.setMaximumSize(QSize(290, 16777215))
        self.label_alterar_escolaridade_usuario_as.setFont(font)

        self.verticalLayout_231.addWidget(self.label_alterar_escolaridade_usuario_as)

        self.input_alterar_escolaridade_usuario_comboBox_as = QComboBox(self.frame_339)
        self.input_alterar_escolaridade_usuario_comboBox_as.addItem("")
        self.input_alterar_escolaridade_usuario_comboBox_as.addItem("")
        self.input_alterar_escolaridade_usuario_comboBox_as.addItem("")
        self.input_alterar_escolaridade_usuario_comboBox_as.addItem("")
        self.input_alterar_escolaridade_usuario_comboBox_as.addItem("")
        self.input_alterar_escolaridade_usuario_comboBox_as.addItem("")
        self.input_alterar_escolaridade_usuario_comboBox_as.addItem("")
        self.input_alterar_escolaridade_usuario_comboBox_as.setObjectName(u"input_alterar_escolaridade_usuario_comboBox_as")
        self.input_alterar_escolaridade_usuario_comboBox_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_escolaridade_usuario_comboBox_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_escolaridade_usuario_comboBox_as.setFont(font)

        self.verticalLayout_231.addWidget(self.input_alterar_escolaridade_usuario_comboBox_as)


        self.horizontalLayout_110.addWidget(self.frame_339)


        self.verticalLayout_208.addWidget(self.frame_333)

        self.frame_340 = QFrame(self.frame_311)
        self.frame_340.setObjectName(u"frame_340")
        self.frame_340.setMaximumSize(QSize(16777215, 60))
        self.frame_340.setStyleSheet(u"")
        self.frame_340.setFrameShape(QFrame.StyledPanel)
        self.frame_340.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_111 = QHBoxLayout(self.frame_340)
        self.horizontalLayout_111.setSpacing(5)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.frame_341 = QFrame(self.frame_340)
        self.frame_341.setObjectName(u"frame_341")
        self.frame_341.setMinimumSize(QSize(150, 0))
        self.frame_341.setMaximumSize(QSize(150, 16777215))
        self.frame_341.setFrameShape(QFrame.StyledPanel)
        self.frame_341.setFrameShadow(QFrame.Raised)
        self.verticalLayout_232 = QVBoxLayout(self.frame_341)
        self.verticalLayout_232.setSpacing(0)
        self.verticalLayout_232.setObjectName(u"verticalLayout_232")
        self.verticalLayout_232.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_pessoa_cdeficiencia_usuario_as = QLabel(self.frame_341)
        self.label_alterar_pessoa_cdeficiencia_usuario_as.setObjectName(u"label_alterar_pessoa_cdeficiencia_usuario_as")
        self.label_alterar_pessoa_cdeficiencia_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_pessoa_cdeficiencia_usuario_as.setMaximumSize(QSize(205, 16777215))
        self.label_alterar_pessoa_cdeficiencia_usuario_as.setFont(font)

        self.verticalLayout_232.addWidget(self.label_alterar_pessoa_cdeficiencia_usuario_as)

        self.frame_342 = QFrame(self.frame_341)
        self.frame_342.setObjectName(u"frame_342")
        self.frame_342.setMinimumSize(QSize(195, 0))
        self.frame_342.setMaximumSize(QSize(195, 16777215))
        self.frame_342.setFont(font)
        self.frame_342.setFrameShape(QFrame.StyledPanel)
        self.frame_342.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_112 = QHBoxLayout(self.frame_342)
        self.horizontalLayout_112.setSpacing(0)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.input_alterar_pessoa_cdeficiencia_sim_usuario_as = QRadioButton(self.frame_342)
        self.input_alterar_pessoa_cdeficiencia_sim_usuario_as.setObjectName(u"input_alterar_pessoa_cdeficiencia_sim_usuario_as")
        self.input_alterar_pessoa_cdeficiencia_sim_usuario_as.setFont(font8)

        self.horizontalLayout_112.addWidget(self.input_alterar_pessoa_cdeficiencia_sim_usuario_as)

        self.label_alterar_pessoa_cdeficiencia_nao_usuario_as = QRadioButton(self.frame_342)
        self.label_alterar_pessoa_cdeficiencia_nao_usuario_as.setObjectName(u"label_alterar_pessoa_cdeficiencia_nao_usuario_as")
        self.label_alterar_pessoa_cdeficiencia_nao_usuario_as.setFont(font8)

        self.horizontalLayout_112.addWidget(self.label_alterar_pessoa_cdeficiencia_nao_usuario_as)


        self.verticalLayout_232.addWidget(self.frame_342)


        self.horizontalLayout_111.addWidget(self.frame_341)

        self.frame_343 = QFrame(self.frame_340)
        self.frame_343.setObjectName(u"frame_343")
        self.frame_343.setMinimumSize(QSize(0, 0))
        self.frame_343.setMaximumSize(QSize(260, 16777215))
        self.frame_343.setFrameShape(QFrame.StyledPanel)
        self.frame_343.setFrameShadow(QFrame.Raised)
        self.verticalLayout_233 = QVBoxLayout(self.frame_343)
        self.verticalLayout_233.setSpacing(0)
        self.verticalLayout_233.setObjectName(u"verticalLayout_233")
        self.verticalLayout_233.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_tipo_deficiencia_usuario_as = QLabel(self.frame_343)
        self.label_alterar_tipo_deficiencia_usuario_as.setObjectName(u"label_alterar_tipo_deficiencia_usuario_as")
        self.label_alterar_tipo_deficiencia_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_tipo_deficiencia_usuario_as.setMaximumSize(QSize(260, 16777215))
        self.label_alterar_tipo_deficiencia_usuario_as.setFont(font)

        self.verticalLayout_233.addWidget(self.label_alterar_tipo_deficiencia_usuario_as)

        self.input_alterar_tipo_deficiencia_usuario_as = QComboBox(self.frame_343)
        self.input_alterar_tipo_deficiencia_usuario_as.addItem("")
        self.input_alterar_tipo_deficiencia_usuario_as.addItem("")
        self.input_alterar_tipo_deficiencia_usuario_as.addItem("")
        self.input_alterar_tipo_deficiencia_usuario_as.addItem("")
        self.input_alterar_tipo_deficiencia_usuario_as.addItem("")
        self.input_alterar_tipo_deficiencia_usuario_as.addItem("")
        self.input_alterar_tipo_deficiencia_usuario_as.setObjectName(u"input_alterar_tipo_deficiencia_usuario_as")
        self.input_alterar_tipo_deficiencia_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_tipo_deficiencia_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_tipo_deficiencia_usuario_as.setFont(font)

        self.verticalLayout_233.addWidget(self.input_alterar_tipo_deficiencia_usuario_as)


        self.horizontalLayout_111.addWidget(self.frame_343)

        self.frame_344 = QFrame(self.frame_340)
        self.frame_344.setObjectName(u"frame_344")
        self.frame_344.setMinimumSize(QSize(0, 0))
        self.frame_344.setMaximumSize(QSize(260, 16777215))
        self.frame_344.setFrameShape(QFrame.StyledPanel)
        self.frame_344.setFrameShadow(QFrame.Raised)
        self.verticalLayout_234 = QVBoxLayout(self.frame_344)
        self.verticalLayout_234.setSpacing(0)
        self.verticalLayout_234.setObjectName(u"verticalLayout_234")
        self.verticalLayout_234.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_renda_familiar_usuario_as = QLabel(self.frame_344)
        self.label_alterar_renda_familiar_usuario_as.setObjectName(u"label_alterar_renda_familiar_usuario_as")
        self.label_alterar_renda_familiar_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_renda_familiar_usuario_as.setMaximumSize(QSize(260, 16777215))
        self.label_alterar_renda_familiar_usuario_as.setFont(font)

        self.verticalLayout_234.addWidget(self.label_alterar_renda_familiar_usuario_as)

        self.input_alterar_renda_familiar_usuario_as = QComboBox(self.frame_344)
        self.input_alterar_renda_familiar_usuario_as.addItem("")
        self.input_alterar_renda_familiar_usuario_as.addItem("")
        self.input_alterar_renda_familiar_usuario_as.addItem("")
        self.input_alterar_renda_familiar_usuario_as.addItem("")
        self.input_alterar_renda_familiar_usuario_as.addItem("")
        self.input_alterar_renda_familiar_usuario_as.setObjectName(u"input_alterar_renda_familiar_usuario_as")
        self.input_alterar_renda_familiar_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_renda_familiar_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_renda_familiar_usuario_as.setFont(font)
        self.input_alterar_renda_familiar_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.input_alterar_renda_familiar_usuario_as.setStyleSheet(u"")

        self.verticalLayout_234.addWidget(self.input_alterar_renda_familiar_usuario_as)


        self.horizontalLayout_111.addWidget(self.frame_344)

        self.frame_345 = QFrame(self.frame_340)
        self.frame_345.setObjectName(u"frame_345")
        self.frame_345.setMinimumSize(QSize(0, 0))
        self.frame_345.setMaximumSize(QSize(200, 16777215))
        self.frame_345.setFrameShape(QFrame.StyledPanel)
        self.frame_345.setFrameShadow(QFrame.Raised)
        self.verticalLayout_235 = QVBoxLayout(self.frame_345)
        self.verticalLayout_235.setSpacing(0)
        self.verticalLayout_235.setObjectName(u"verticalLayout_235")
        self.verticalLayout_235.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_meio_transporte_usuario_as = QLabel(self.frame_345)
        self.label_alterar_meio_transporte_usuario_as.setObjectName(u"label_alterar_meio_transporte_usuario_as")
        self.label_alterar_meio_transporte_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_meio_transporte_usuario_as.setMaximumSize(QSize(200, 16777215))
        self.label_alterar_meio_transporte_usuario_as.setFont(font)

        self.verticalLayout_235.addWidget(self.label_alterar_meio_transporte_usuario_as)

        self.input_alterar_meio_transporte_usuario_as = QComboBox(self.frame_345)
        self.input_alterar_meio_transporte_usuario_as.addItem("")
        self.input_alterar_meio_transporte_usuario_as.addItem("")
        self.input_alterar_meio_transporte_usuario_as.addItem("")
        self.input_alterar_meio_transporte_usuario_as.addItem("")
        self.input_alterar_meio_transporte_usuario_as.addItem("")
        self.input_alterar_meio_transporte_usuario_as.addItem("")
        self.input_alterar_meio_transporte_usuario_as.addItem("")
        self.input_alterar_meio_transporte_usuario_as.addItem("")
        self.input_alterar_meio_transporte_usuario_as.setObjectName(u"input_alterar_meio_transporte_usuario_as")
        self.input_alterar_meio_transporte_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_meio_transporte_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_meio_transporte_usuario_as.setFont(font)
        self.input_alterar_meio_transporte_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_235.addWidget(self.input_alterar_meio_transporte_usuario_as)


        self.horizontalLayout_111.addWidget(self.frame_345)

        self.frame_346 = QFrame(self.frame_340)
        self.frame_346.setObjectName(u"frame_346")
        self.frame_346.setMaximumSize(QSize(310, 16777215))
        self.frame_346.setFrameShape(QFrame.StyledPanel)
        self.frame_346.setFrameShadow(QFrame.Raised)
        self.verticalLayout_236 = QVBoxLayout(self.frame_346)
        self.verticalLayout_236.setSpacing(0)
        self.verticalLayout_236.setObjectName(u"verticalLayout_236")
        self.verticalLayout_236.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_vale_transporte_usuario_as = QLabel(self.frame_346)
        self.label_alterar_vale_transporte_usuario_as.setObjectName(u"label_alterar_vale_transporte_usuario_as")
        self.label_alterar_vale_transporte_usuario_as.setMaximumSize(QSize(310, 16777215))
        self.label_alterar_vale_transporte_usuario_as.setFont(font)

        self.verticalLayout_236.addWidget(self.label_alterar_vale_transporte_usuario_as)

        self.input_alterar_vale_transporte_usuario_as = QComboBox(self.frame_346)
        self.input_alterar_vale_transporte_usuario_as.addItem("")
        self.input_alterar_vale_transporte_usuario_as.addItem("")
        self.input_alterar_vale_transporte_usuario_as.addItem("")
        self.input_alterar_vale_transporte_usuario_as.addItem("")
        self.input_alterar_vale_transporte_usuario_as.setObjectName(u"input_alterar_vale_transporte_usuario_as")
        self.input_alterar_vale_transporte_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_vale_transporte_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_vale_transporte_usuario_as.setFont(font)
        self.input_alterar_vale_transporte_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_236.addWidget(self.input_alterar_vale_transporte_usuario_as)


        self.horizontalLayout_111.addWidget(self.frame_346)


        self.verticalLayout_208.addWidget(self.frame_340)

        self.frame_347 = QFrame(self.frame_311)
        self.frame_347.setObjectName(u"frame_347")
        self.frame_347.setMaximumSize(QSize(16777215, 60))
        self.frame_347.setStyleSheet(u"")
        self.frame_347.setFrameShape(QFrame.StyledPanel)
        self.frame_347.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_113 = QHBoxLayout(self.frame_347)
        self.horizontalLayout_113.setSpacing(5)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.frame_348 = QFrame(self.frame_347)
        self.frame_348.setObjectName(u"frame_348")
        self.frame_348.setMinimumSize(QSize(0, 0))
        self.frame_348.setMaximumSize(QSize(260, 16777215))
        self.frame_348.setFrameShape(QFrame.StyledPanel)
        self.frame_348.setFrameShadow(QFrame.Raised)
        self.verticalLayout_237 = QVBoxLayout(self.frame_348)
        self.verticalLayout_237.setSpacing(0)
        self.verticalLayout_237.setObjectName(u"verticalLayout_237")
        self.verticalLayout_237.setContentsMargins(0, 0, 0, 0)
        self.label_situacao_trabalho_alterar_usuario_as = QLabel(self.frame_348)
        self.label_situacao_trabalho_alterar_usuario_as.setObjectName(u"label_situacao_trabalho_alterar_usuario_as")
        self.label_situacao_trabalho_alterar_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_situacao_trabalho_alterar_usuario_as.setMaximumSize(QSize(260, 16777215))
        self.label_situacao_trabalho_alterar_usuario_as.setFont(font)

        self.verticalLayout_237.addWidget(self.label_situacao_trabalho_alterar_usuario_as)

        self.input_situacao_trabalho_alterar_usuario_as = QComboBox(self.frame_348)
        self.input_situacao_trabalho_alterar_usuario_as.addItem("")
        self.input_situacao_trabalho_alterar_usuario_as.addItem("")
        self.input_situacao_trabalho_alterar_usuario_as.addItem("")
        self.input_situacao_trabalho_alterar_usuario_as.addItem("")
        self.input_situacao_trabalho_alterar_usuario_as.addItem("")
        self.input_situacao_trabalho_alterar_usuario_as.addItem("")
        self.input_situacao_trabalho_alterar_usuario_as.addItem("")
        self.input_situacao_trabalho_alterar_usuario_as.addItem("")
        self.input_situacao_trabalho_alterar_usuario_as.addItem("")
        self.input_situacao_trabalho_alterar_usuario_as.addItem("")
        self.input_situacao_trabalho_alterar_usuario_as.setObjectName(u"input_situacao_trabalho_alterar_usuario_as")
        self.input_situacao_trabalho_alterar_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_situacao_trabalho_alterar_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_situacao_trabalho_alterar_usuario_as.setFont(font)

        self.verticalLayout_237.addWidget(self.input_situacao_trabalho_alterar_usuario_as)


        self.horizontalLayout_113.addWidget(self.frame_348)

        self.frame_439 = QFrame(self.frame_347)
        self.frame_439.setObjectName(u"frame_439")
        self.frame_439.setEnabled(False)
        self.frame_439.setMinimumSize(QSize(145, 0))
        self.frame_439.setMaximumSize(QSize(145, 16777215))
        self.frame_439.setStyleSheet(u"QWidget frame_439 {\n"
"    border: none;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"")
        self.frame_439.setFrameShape(QFrame.StyledPanel)
        self.frame_439.setFrameShadow(QFrame.Raised)
        self.verticalLayout_306 = QVBoxLayout(self.frame_439)
        self.verticalLayout_306.setSpacing(0)
        self.verticalLayout_306.setObjectName(u"verticalLayout_306")
        self.verticalLayout_306.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_306.addItem(self.verticalSpacer_22)

        self.input_situacao_trabalho_outros_alterar_usuario_as = QLineEdit(self.frame_439)
        self.input_situacao_trabalho_outros_alterar_usuario_as.setObjectName(u"input_situacao_trabalho_outros_alterar_usuario_as")
        self.input_situacao_trabalho_outros_alterar_usuario_as.setEnabled(False)
        self.input_situacao_trabalho_outros_alterar_usuario_as.setMinimumSize(QSize(140, 0))
        self.input_situacao_trabalho_outros_alterar_usuario_as.setMaximumSize(QSize(140, 16777215))
        self.input_situacao_trabalho_outros_alterar_usuario_as.setFont(font10)
        self.input_situacao_trabalho_outros_alterar_usuario_as.setStyleSheet(u"\n"
"    border: none;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"\n"
"")

        self.verticalLayout_306.addWidget(self.input_situacao_trabalho_outros_alterar_usuario_as)


        self.horizontalLayout_113.addWidget(self.frame_439)

        self.frame_349 = QFrame(self.frame_347)
        self.frame_349.setObjectName(u"frame_349")
        self.frame_349.setMinimumSize(QSize(0, 0))
        self.frame_349.setMaximumSize(QSize(260, 16777215))
        self.frame_349.setFrameShape(QFrame.StyledPanel)
        self.frame_349.setFrameShadow(QFrame.Raised)
        self.verticalLayout_238 = QVBoxLayout(self.frame_349)
        self.verticalLayout_238.setSpacing(0)
        self.verticalLayout_238.setObjectName(u"verticalLayout_238")
        self.verticalLayout_238.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_beneficios_usuario_as = QLabel(self.frame_349)
        self.label_alterar_beneficios_usuario_as.setObjectName(u"label_alterar_beneficios_usuario_as")
        self.label_alterar_beneficios_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_beneficios_usuario_as.setMaximumSize(QSize(260, 16777215))
        self.label_alterar_beneficios_usuario_as.setFont(font)

        self.verticalLayout_238.addWidget(self.label_alterar_beneficios_usuario_as)

        self.input_alterar_beneficios_usuario_as = QComboBox(self.frame_349)
        self.input_alterar_beneficios_usuario_as.addItem("")
        self.input_alterar_beneficios_usuario_as.addItem("")
        self.input_alterar_beneficios_usuario_as.addItem("")
        self.input_alterar_beneficios_usuario_as.addItem("")
        self.input_alterar_beneficios_usuario_as.addItem("")
        self.input_alterar_beneficios_usuario_as.setObjectName(u"input_alterar_beneficios_usuario_as")
        self.input_alterar_beneficios_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_beneficios_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_beneficios_usuario_as.setFont(font)
        self.input_alterar_beneficios_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.input_alterar_beneficios_usuario_as.setStyleSheet(u"")

        self.verticalLayout_238.addWidget(self.input_alterar_beneficios_usuario_as)


        self.horizontalLayout_113.addWidget(self.frame_349)

        self.frame_350 = QFrame(self.frame_347)
        self.frame_350.setObjectName(u"frame_350")
        self.frame_350.setMinimumSize(QSize(130, 0))
        self.frame_350.setMaximumSize(QSize(130, 16777215))
        self.frame_350.setFrameShape(QFrame.StyledPanel)
        self.frame_350.setFrameShadow(QFrame.Raised)
        self.verticalLayout_239 = QVBoxLayout(self.frame_350)
        self.verticalLayout_239.setSpacing(0)
        self.verticalLayout_239.setObjectName(u"verticalLayout_239")
        self.verticalLayout_239.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_tarifa_social_usuario_as = QLabel(self.frame_350)
        self.label_alterar_tarifa_social_usuario_as.setObjectName(u"label_alterar_tarifa_social_usuario_as")
        self.label_alterar_tarifa_social_usuario_as.setMaximumSize(QSize(190, 16777215))
        self.label_alterar_tarifa_social_usuario_as.setFont(font)

        self.verticalLayout_239.addWidget(self.label_alterar_tarifa_social_usuario_as)

        self.frame_351 = QFrame(self.frame_350)
        self.frame_351.setObjectName(u"frame_351")
        self.frame_351.setFrameShape(QFrame.StyledPanel)
        self.frame_351.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_114 = QHBoxLayout(self.frame_351)
        self.horizontalLayout_114.setSpacing(0)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.input_alterar_tarifa_social_sim_usuario_as = QRadioButton(self.frame_351)
        self.input_alterar_tarifa_social_sim_usuario_as.setObjectName(u"input_alterar_tarifa_social_sim_usuario_as")
        self.input_alterar_tarifa_social_sim_usuario_as.setFont(font8)
        self.input_alterar_tarifa_social_sim_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_114.addWidget(self.input_alterar_tarifa_social_sim_usuario_as)

        self.input_alterar_tarifa_social_nao_usuario_as = QRadioButton(self.frame_351)
        self.input_alterar_tarifa_social_nao_usuario_as.setObjectName(u"input_alterar_tarifa_social_nao_usuario_as")
        self.input_alterar_tarifa_social_nao_usuario_as.setFont(font8)
        self.input_alterar_tarifa_social_nao_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_114.addWidget(self.input_alterar_tarifa_social_nao_usuario_as)


        self.verticalLayout_239.addWidget(self.frame_351)


        self.horizontalLayout_113.addWidget(self.frame_350)

        self.frame_352 = QFrame(self.frame_347)
        self.frame_352.setObjectName(u"frame_352")
        self.frame_352.setMinimumSize(QSize(0, 0))
        self.frame_352.setMaximumSize(QSize(260, 16777215))
        self.frame_352.setFrameShape(QFrame.StyledPanel)
        self.frame_352.setFrameShadow(QFrame.Raised)
        self.verticalLayout_240 = QVBoxLayout(self.frame_352)
        self.verticalLayout_240.setSpacing(0)
        self.verticalLayout_240.setObjectName(u"verticalLayout_240")
        self.verticalLayout_240.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_tipo_tratamento_usuario_as = QLabel(self.frame_352)
        self.label_alterar_tipo_tratamento_usuario_as.setObjectName(u"label_alterar_tipo_tratamento_usuario_as")
        self.label_alterar_tipo_tratamento_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_tipo_tratamento_usuario_as.setMaximumSize(QSize(260, 16777215))
        self.label_alterar_tipo_tratamento_usuario_as.setFont(font)

        self.verticalLayout_240.addWidget(self.label_alterar_tipo_tratamento_usuario_as)

        self.input_alterar_tipo_tratamento_usuario_as = QComboBox(self.frame_352)
        self.input_alterar_tipo_tratamento_usuario_as.addItem("")
        self.input_alterar_tipo_tratamento_usuario_as.addItem("")
        self.input_alterar_tipo_tratamento_usuario_as.addItem("")
        self.input_alterar_tipo_tratamento_usuario_as.addItem("")
        self.input_alterar_tipo_tratamento_usuario_as.setObjectName(u"input_alterar_tipo_tratamento_usuario_as")
        self.input_alterar_tipo_tratamento_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_tipo_tratamento_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_tipo_tratamento_usuario_as.setFont(font)
        self.input_alterar_tipo_tratamento_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.input_alterar_tipo_tratamento_usuario_as.setStyleSheet(u"")

        self.verticalLayout_240.addWidget(self.input_alterar_tipo_tratamento_usuario_as)


        self.horizontalLayout_113.addWidget(self.frame_352)

        self.horizontalSpacer_73 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_113.addItem(self.horizontalSpacer_73)


        self.verticalLayout_208.addWidget(self.frame_347)

        self.frame_354 = QFrame(self.frame_311)
        self.frame_354.setObjectName(u"frame_354")
        self.frame_354.setMaximumSize(QSize(16777215, 60))
        self.frame_354.setStyleSheet(u"")
        self.frame_354.setFrameShape(QFrame.StyledPanel)
        self.frame_354.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_115 = QHBoxLayout(self.frame_354)
        self.horizontalLayout_115.setSpacing(5)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.frame_353 = QFrame(self.frame_354)
        self.frame_353.setObjectName(u"frame_353")
        self.frame_353.setMinimumSize(QSize(0, 0))
        self.frame_353.setMaximumSize(QSize(330, 16777215))
        self.frame_353.setFrameShape(QFrame.StyledPanel)
        self.frame_353.setFrameShadow(QFrame.Raised)
        self.verticalLayout_241 = QVBoxLayout(self.frame_353)
        self.verticalLayout_241.setSpacing(0)
        self.verticalLayout_241.setObjectName(u"verticalLayout_241")
        self.verticalLayout_241.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_local_tratamento_usuario_as = QLabel(self.frame_353)
        self.label_alterar_local_tratamento_usuario_as.setObjectName(u"label_alterar_local_tratamento_usuario_as")
        self.label_alterar_local_tratamento_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_local_tratamento_usuario_as.setMaximumSize(QSize(330, 16777215))
        self.label_alterar_local_tratamento_usuario_as.setFont(font)

        self.verticalLayout_241.addWidget(self.label_alterar_local_tratamento_usuario_as)

        self.input_alterar_local_tratamento_usuario_as = QLineEdit(self.frame_353)
        self.input_alterar_local_tratamento_usuario_as.setObjectName(u"input_alterar_local_tratamento_usuario_as")
        self.input_alterar_local_tratamento_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_local_tratamento_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_local_tratamento_usuario_as.setFont(font)

        self.verticalLayout_241.addWidget(self.input_alterar_local_tratamento_usuario_as)


        self.horizontalLayout_115.addWidget(self.frame_353)

        self.frame_355 = QFrame(self.frame_354)
        self.frame_355.setObjectName(u"frame_355")
        self.frame_355.setMinimumSize(QSize(0, 0))
        self.frame_355.setMaximumSize(QSize(260, 16777215))
        self.frame_355.setFrameShape(QFrame.StyledPanel)
        self.frame_355.setFrameShadow(QFrame.Raised)
        self.verticalLayout_242 = QVBoxLayout(self.frame_355)
        self.verticalLayout_242.setSpacing(0)
        self.verticalLayout_242.setObjectName(u"verticalLayout_242")
        self.verticalLayout_242.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_patologia_base_usuario_as = QLabel(self.frame_355)
        self.label_alterar_patologia_base_usuario_as.setObjectName(u"label_alterar_patologia_base_usuario_as")
        self.label_alterar_patologia_base_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_patologia_base_usuario_as.setMaximumSize(QSize(260, 16777215))
        self.label_alterar_patologia_base_usuario_as.setFont(font)

        self.verticalLayout_242.addWidget(self.label_alterar_patologia_base_usuario_as)

        self.input_alterar_patologia_base_usuario_as = QComboBox(self.frame_355)
        self.input_alterar_patologia_base_usuario_as.addItem("")
        self.input_alterar_patologia_base_usuario_as.addItem("")
        self.input_alterar_patologia_base_usuario_as.addItem("")
        self.input_alterar_patologia_base_usuario_as.addItem("")
        self.input_alterar_patologia_base_usuario_as.addItem("")
        self.input_alterar_patologia_base_usuario_as.addItem("")
        self.input_alterar_patologia_base_usuario_as.addItem("")
        self.input_alterar_patologia_base_usuario_as.setObjectName(u"input_alterar_patologia_base_usuario_as")
        self.input_alterar_patologia_base_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_patologia_base_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_patologia_base_usuario_as.setFont(font)
        self.input_alterar_patologia_base_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_242.addWidget(self.input_alterar_patologia_base_usuario_as)


        self.horizontalLayout_115.addWidget(self.frame_355)

        self.frame_356 = QFrame(self.frame_354)
        self.frame_356.setObjectName(u"frame_356")
        self.frame_356.setMinimumSize(QSize(0, 0))
        self.frame_356.setMaximumSize(QSize(160, 16777215))
        self.frame_356.setFrameShape(QFrame.StyledPanel)
        self.frame_356.setFrameShadow(QFrame.Raised)
        self.verticalLayout_243 = QVBoxLayout(self.frame_356)
        self.verticalLayout_243.setSpacing(5)
        self.verticalLayout_243.setObjectName(u"verticalLayout_243")
        self.verticalLayout_243.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_data_inicio_usuario_as = QLabel(self.frame_356)
        self.label_alterar_data_inicio_usuario_as.setObjectName(u"label_alterar_data_inicio_usuario_as")
        self.label_alterar_data_inicio_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_data_inicio_usuario_as.setMaximumSize(QSize(160, 16777215))
        self.label_alterar_data_inicio_usuario_as.setFont(font)

        self.verticalLayout_243.addWidget(self.label_alterar_data_inicio_usuario_as, 0, Qt.AlignHCenter)

        self.input_alterar_data_inicio_usuario_as = QDateEdit(self.frame_356)
        self.input_alterar_data_inicio_usuario_as.setObjectName(u"input_alterar_data_inicio_usuario_as")
        sizePolicy1.setHeightForWidth(self.input_alterar_data_inicio_usuario_as.sizePolicy().hasHeightForWidth())
        self.input_alterar_data_inicio_usuario_as.setSizePolicy(sizePolicy1)
        self.input_alterar_data_inicio_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_data_inicio_usuario_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_alterar_data_inicio_usuario_as.setFont(font8)
        self.input_alterar_data_inicio_usuario_as.setFocusPolicy(Qt.WheelFocus)
        self.input_alterar_data_inicio_usuario_as.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.input_alterar_data_inicio_usuario_as.setLayoutDirection(Qt.LeftToRight)
        self.input_alterar_data_inicio_usuario_as.setAutoFillBackground(False)
        self.input_alterar_data_inicio_usuario_as.setStyleSheet(u"QDateEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QDateEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_alterar_data_inicio_usuario_as.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.input_alterar_data_inicio_usuario_as.setAlignment(Qt.AlignCenter)
        self.input_alterar_data_inicio_usuario_as.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.input_alterar_data_inicio_usuario_as.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.input_alterar_data_inicio_usuario_as.setCurrentSection(QDateTimeEdit.DaySection)
        self.input_alterar_data_inicio_usuario_as.setCalendarPopup(False)
        self.input_alterar_data_inicio_usuario_as.setCurrentSectionIndex(0)

        self.verticalLayout_243.addWidget(self.input_alterar_data_inicio_usuario_as, 0, Qt.AlignHCenter)


        self.horizontalLayout_115.addWidget(self.frame_356)

        self.frame_357 = QFrame(self.frame_354)
        self.frame_357.setObjectName(u"frame_357")
        self.frame_357.setMinimumSize(QSize(0, 0))
        self.frame_357.setMaximumSize(QSize(250, 16777215))
        self.frame_357.setFrameShape(QFrame.StyledPanel)
        self.frame_357.setFrameShadow(QFrame.Raised)
        self.verticalLayout_244 = QVBoxLayout(self.frame_357)
        self.verticalLayout_244.setSpacing(5)
        self.verticalLayout_244.setObjectName(u"verticalLayout_244")
        self.verticalLayout_244.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_periodo_usuario_as = QLabel(self.frame_357)
        self.label_alterar_periodo_usuario_as.setObjectName(u"label_alterar_periodo_usuario_as")
        self.label_alterar_periodo_usuario_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_periodo_usuario_as.setMaximumSize(QSize(250, 16777215))
        self.label_alterar_periodo_usuario_as.setFont(font)

        self.verticalLayout_244.addWidget(self.label_alterar_periodo_usuario_as)

        self.input_alterar_periodo_usuario_as = QComboBox(self.frame_357)
        self.input_alterar_periodo_usuario_as.addItem("")
        self.input_alterar_periodo_usuario_as.addItem("")
        self.input_alterar_periodo_usuario_as.addItem("")
        self.input_alterar_periodo_usuario_as.addItem("")
        self.input_alterar_periodo_usuario_as.setObjectName(u"input_alterar_periodo_usuario_as")
        self.input_alterar_periodo_usuario_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_periodo_usuario_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_periodo_usuario_as.setFont(font)
        self.input_alterar_periodo_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_244.addWidget(self.input_alterar_periodo_usuario_as)


        self.horizontalLayout_115.addWidget(self.frame_357)

        self.frame_358 = QFrame(self.frame_354)
        self.frame_358.setObjectName(u"frame_358")
        self.frame_358.setMaximumSize(QSize(600, 16777215))
        self.frame_358.setFrameShape(QFrame.StyledPanel)
        self.frame_358.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_131 = QHBoxLayout(self.frame_358)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.input_alterar_id_endereco_usuario_as = QLineEdit(self.frame_358)
        self.input_alterar_id_endereco_usuario_as.setObjectName(u"input_alterar_id_endereco_usuario_as")
        self.input_alterar_id_endereco_usuario_as.setEnabled(False)
        self.input_alterar_id_endereco_usuario_as.setStyleSheet(u"background-color:transparent;\n"
"border-color: transparent;")

        self.horizontalLayout_131.addWidget(self.input_alterar_id_endereco_usuario_as)

        self.input_alterar_id_matricula_usuario_as = QLineEdit(self.frame_358)
        self.input_alterar_id_matricula_usuario_as.setObjectName(u"input_alterar_id_matricula_usuario_as")
        self.input_alterar_id_matricula_usuario_as.setEnabled(False)
        self.input_alterar_id_matricula_usuario_as.setStyleSheet(u"background-color:transparent;\n"
"border-color: transparent;")

        self.horizontalLayout_131.addWidget(self.input_alterar_id_matricula_usuario_as)


        self.horizontalLayout_115.addWidget(self.frame_358)


        self.verticalLayout_208.addWidget(self.frame_354)

        self.frame_359 = QFrame(self.frame_311)
        self.frame_359.setObjectName(u"frame_359")
        self.frame_359.setStyleSheet(u"")
        self.frame_359.setFrameShape(QFrame.StyledPanel)
        self.frame_359.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_116 = QHBoxLayout(self.frame_359)
        self.horizontalLayout_116.setSpacing(5)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.frame_360 = QFrame(self.frame_359)
        self.frame_360.setObjectName(u"frame_360")
        self.frame_360.setFrameShape(QFrame.StyledPanel)
        self.frame_360.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_116.addWidget(self.frame_360)


        self.verticalLayout_208.addWidget(self.frame_359)


        self.horizontalLayout_104.addWidget(self.frame_311)

        self.horizontalSpacer_65 = QSpacerItem(151, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_104.addItem(self.horizontalSpacer_65)

        self.horizontalLayout_104.setStretch(0, 1)
        self.horizontalLayout_104.setStretch(1, 8)

        self.horizontalLayout_117.addWidget(self.frame_310)


        self.verticalLayout_81.addWidget(self.frame_308)

        self.frame_309 = QFrame(self.frame_307)
        self.frame_309.setObjectName(u"frame_309")
        self.frame_309.setMinimumSize(QSize(0, 20))
        self.frame_309.setMaximumSize(QSize(16777215, 71))
        self.frame_309.setFrameShape(QFrame.StyledPanel)
        self.frame_309.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_119 = QHBoxLayout(self.frame_309)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.frame_361 = QFrame(self.frame_309)
        self.frame_361.setObjectName(u"frame_361")
        self.frame_361.setFrameShape(QFrame.StyledPanel)
        self.frame_361.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_118 = QHBoxLayout(self.frame_361)
        self.horizontalLayout_118.setSpacing(20)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.horizontalLayout_118.setContentsMargins(20, 0, 0, 0)
        self.btn_alterar_voltar_usuario_as = QPushButton(self.frame_361)
        self.btn_alterar_voltar_usuario_as.setObjectName(u"btn_alterar_voltar_usuario_as")
        self.btn_alterar_voltar_usuario_as.setMinimumSize(QSize(100, 40))
        self.btn_alterar_voltar_usuario_as.setMaximumSize(QSize(100, 40))
        self.btn_alterar_voltar_usuario_as.setFont(font11)
        self.btn_alterar_voltar_usuario_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_voltar_usuario_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout_118.addWidget(self.btn_alterar_voltar_usuario_as)

        self.horizontalSpacer_66 = QSpacerItem(1687, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_118.addItem(self.horizontalSpacer_66)

        self.btn_alterar_observacoes_sigilo_as = QPushButton(self.frame_361)
        self.btn_alterar_observacoes_sigilo_as.setObjectName(u"btn_alterar_observacoes_sigilo_as")
        self.btn_alterar_observacoes_sigilo_as.setMinimumSize(QSize(0, 40))
        self.btn_alterar_observacoes_sigilo_as.setFont(font11)
        self.btn_alterar_observacoes_sigilo_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_observacoes_sigilo_as.setStyleSheet(u"QPushButton{color: #000; background-color: #EC848C; border-radius: 20px; padding-right: 0.5em; padding-left: 0.5em}\n"
"QPushButton:hover{background-color: #F89198}\n"
"QPushButton:focus{outline:0}")
        self.btn_alterar_observacoes_sigilo_as.setIcon(icon13)
        self.btn_alterar_observacoes_sigilo_as.setIconSize(QSize(28, 28))

        self.horizontalLayout_118.addWidget(self.btn_alterar_observacoes_sigilo_as)

        self.btn_alterar_proximo_as = QPushButton(self.frame_361)
        self.btn_alterar_proximo_as.setObjectName(u"btn_alterar_proximo_as")
        self.btn_alterar_proximo_as.setMinimumSize(QSize(140, 40))
        self.btn_alterar_proximo_as.setFont(font11)
        self.btn_alterar_proximo_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_proximo_as.setLayoutDirection(Qt.RightToLeft)
        self.btn_alterar_proximo_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout_118.addWidget(self.btn_alterar_proximo_as)

        self.btn_alterar_finalizar_as = QPushButton(self.frame_361)
        self.btn_alterar_finalizar_as.setObjectName(u"btn_alterar_finalizar_as")
        self.btn_alterar_finalizar_as.setMinimumSize(QSize(140, 40))
        self.btn_alterar_finalizar_as.setFont(font11)
        self.btn_alterar_finalizar_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_finalizar_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout_118.addWidget(self.btn_alterar_finalizar_as)


        self.horizontalLayout_119.addWidget(self.frame_361)


        self.verticalLayout_81.addWidget(self.frame_309)


        self.horizontalLayout_102.addWidget(self.frame_307)

        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_102.addItem(self.horizontalSpacer_63)


        self.verticalLayout_218.addWidget(self.frame_283)

        self.stackedWidget_8.addWidget(self.page_alterar_usuario)
        self.page_alterar_colaborador_as = QWidget()
        self.page_alterar_colaborador_as.setObjectName(u"page_alterar_colaborador_as")
        self.verticalLayout_251 = QVBoxLayout(self.page_alterar_colaborador_as)
        self.verticalLayout_251.setSpacing(0)
        self.verticalLayout_251.setObjectName(u"verticalLayout_251")
        self.verticalLayout_251.setContentsMargins(0, 0, 0, 0)
        self.frame_362 = QFrame(self.page_alterar_colaborador_as)
        self.frame_362.setObjectName(u"frame_362")
        self.frame_362.setFrameShape(QFrame.StyledPanel)
        self.frame_362.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_120 = QHBoxLayout(self.frame_362)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalSpacer_67 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_120.addItem(self.horizontalSpacer_67)

        self.frame_363 = QFrame(self.frame_362)
        self.frame_363.setObjectName(u"frame_363")
        self.frame_363.setFrameShape(QFrame.StyledPanel)
        self.frame_363.setFrameShadow(QFrame.Raised)
        self.verticalLayout_245 = QVBoxLayout(self.frame_363)
        self.verticalLayout_245.setObjectName(u"verticalLayout_245")
        self.frame_364 = QFrame(self.frame_363)
        self.frame_364.setObjectName(u"frame_364")
        self.frame_364.setFrameShape(QFrame.StyledPanel)
        self.frame_364.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_137 = QHBoxLayout(self.frame_364)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.frame_374 = QFrame(self.frame_364)
        self.frame_374.setObjectName(u"frame_374")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_374.sizePolicy().hasHeightForWidth())
        self.frame_374.setSizePolicy(sizePolicy7)
        self.frame_374.setStyleSheet(u"QLabel{margin-left: 0.25em}")
        self.frame_374.setFrameShape(QFrame.StyledPanel)
        self.frame_374.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_374)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_382 = QFrame(self.frame_374)
        self.frame_382.setObjectName(u"frame_382")
        self.frame_382.setMinimumSize(QSize(0, 0))
        self.frame_382.setMaximumSize(QSize(16777215, 60))
        self.frame_382.setStyleSheet(u"")
        self.frame_382.setFrameShape(QFrame.StyledPanel)
        self.frame_382.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_130 = QHBoxLayout(self.frame_382)
        self.horizontalLayout_130.setSpacing(5)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.frame_383 = QFrame(self.frame_382)
        self.frame_383.setObjectName(u"frame_383")
        self.frame_383.setMinimumSize(QSize(0, 0))
        self.frame_383.setMaximumSize(QSize(155, 16777215))
        self.frame_383.setFrameShape(QFrame.StyledPanel)
        self.frame_383.setFrameShadow(QFrame.Raised)
        self.verticalLayout_259 = QVBoxLayout(self.frame_383)
        self.verticalLayout_259.setSpacing(5)
        self.verticalLayout_259.setObjectName(u"verticalLayout_259")
        self.verticalLayout_259.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_estado_civil_colaborador_as = QLabel(self.frame_383)
        self.label_alterar_estado_civil_colaborador_as.setObjectName(u"label_alterar_estado_civil_colaborador_as")
        self.label_alterar_estado_civil_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_estado_civil_colaborador_as.setMaximumSize(QSize(155, 16777215))
        self.label_alterar_estado_civil_colaborador_as.setFont(font)

        self.verticalLayout_259.addWidget(self.label_alterar_estado_civil_colaborador_as)

        self.input_alterar_estado_civil_colaborador_comboBox_as = QComboBox(self.frame_383)
        self.input_alterar_estado_civil_colaborador_comboBox_as.addItem("")
        self.input_alterar_estado_civil_colaborador_comboBox_as.addItem("")
        self.input_alterar_estado_civil_colaborador_comboBox_as.addItem("")
        self.input_alterar_estado_civil_colaborador_comboBox_as.addItem("")
        self.input_alterar_estado_civil_colaborador_comboBox_as.addItem("")
        self.input_alterar_estado_civil_colaborador_comboBox_as.addItem("")
        self.input_alterar_estado_civil_colaborador_comboBox_as.setObjectName(u"input_alterar_estado_civil_colaborador_comboBox_as")
        self.input_alterar_estado_civil_colaborador_comboBox_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_estado_civil_colaborador_comboBox_as.setMaximumSize(QSize(145, 30))
        self.input_alterar_estado_civil_colaborador_comboBox_as.setFont(font)

        self.verticalLayout_259.addWidget(self.input_alterar_estado_civil_colaborador_comboBox_as)


        self.horizontalLayout_130.addWidget(self.frame_383)

        self.frame_384 = QFrame(self.frame_382)
        self.frame_384.setObjectName(u"frame_384")
        self.frame_384.setMinimumSize(QSize(0, 0))
        self.frame_384.setMaximumSize(QSize(155, 16777215))
        self.frame_384.setFrameShape(QFrame.StyledPanel)
        self.frame_384.setFrameShadow(QFrame.Raised)
        self.verticalLayout_260 = QVBoxLayout(self.frame_384)
        self.verticalLayout_260.setSpacing(5)
        self.verticalLayout_260.setObjectName(u"verticalLayout_260")
        self.verticalLayout_260.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_salario_colaborador_as_2 = QLabel(self.frame_384)
        self.label_alterar_salario_colaborador_as_2.setObjectName(u"label_alterar_salario_colaborador_as_2")
        self.label_alterar_salario_colaborador_as_2.setMinimumSize(QSize(0, 0))
        self.label_alterar_salario_colaborador_as_2.setMaximumSize(QSize(100, 16777215))
        self.label_alterar_salario_colaborador_as_2.setFont(font)

        self.verticalLayout_260.addWidget(self.label_alterar_salario_colaborador_as_2)

        self.input_alterar_salario_colaborador_as_2 = QLineEdit(self.frame_384)
        self.input_alterar_salario_colaborador_as_2.setObjectName(u"input_alterar_salario_colaborador_as_2")
        self.input_alterar_salario_colaborador_as_2.setMinimumSize(QSize(0, 30))
        self.input_alterar_salario_colaborador_as_2.setMaximumSize(QSize(16777215, 16777215))
        self.input_alterar_salario_colaborador_as_2.setFont(font)

        self.verticalLayout_260.addWidget(self.input_alterar_salario_colaborador_as_2)


        self.horizontalLayout_130.addWidget(self.frame_384)

        self.frame_388 = QFrame(self.frame_382)
        self.frame_388.setObjectName(u"frame_388")
        self.frame_388.setMinimumSize(QSize(0, 0))
        self.frame_388.setMaximumSize(QSize(155, 16777215))
        self.frame_388.setFrameShape(QFrame.StyledPanel)
        self.frame_388.setFrameShadow(QFrame.Raised)
        self.verticalLayout_263 = QVBoxLayout(self.frame_388)
        self.verticalLayout_263.setSpacing(5)
        self.verticalLayout_263.setObjectName(u"verticalLayout_263")
        self.verticalLayout_263.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_escolaridade_colaborador_as = QLabel(self.frame_388)
        self.label_alterar_escolaridade_colaborador_as.setObjectName(u"label_alterar_escolaridade_colaborador_as")
        self.label_alterar_escolaridade_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_escolaridade_colaborador_as.setMaximumSize(QSize(155, 16777215))
        self.label_alterar_escolaridade_colaborador_as.setFont(font)

        self.verticalLayout_263.addWidget(self.label_alterar_escolaridade_colaborador_as)

        self.input_alterar_escolaridade_colaborador_comboBox_as = QComboBox(self.frame_388)
        self.input_alterar_escolaridade_colaborador_comboBox_as.addItem("")
        self.input_alterar_escolaridade_colaborador_comboBox_as.addItem("")
        self.input_alterar_escolaridade_colaborador_comboBox_as.addItem("")
        self.input_alterar_escolaridade_colaborador_comboBox_as.addItem("")
        self.input_alterar_escolaridade_colaborador_comboBox_as.addItem("")
        self.input_alterar_escolaridade_colaborador_comboBox_as.addItem("")
        self.input_alterar_escolaridade_colaborador_comboBox_as.addItem("")
        self.input_alterar_escolaridade_colaborador_comboBox_as.setObjectName(u"input_alterar_escolaridade_colaborador_comboBox_as")
        self.input_alterar_escolaridade_colaborador_comboBox_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_escolaridade_colaborador_comboBox_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_escolaridade_colaborador_comboBox_as.setFont(font)

        self.verticalLayout_263.addWidget(self.input_alterar_escolaridade_colaborador_comboBox_as)


        self.horizontalLayout_130.addWidget(self.frame_388)

        self.frame_389 = QFrame(self.frame_382)
        self.frame_389.setObjectName(u"frame_389")
        self.frame_389.setMinimumSize(QSize(0, 0))
        self.frame_389.setMaximumSize(QSize(146, 16777215))
        self.frame_389.setFrameShape(QFrame.StyledPanel)
        self.frame_389.setFrameShadow(QFrame.Raised)
        self.verticalLayout_264 = QVBoxLayout(self.frame_389)
        self.verticalLayout_264.setSpacing(5)
        self.verticalLayout_264.setObjectName(u"verticalLayout_264")
        self.verticalLayout_264.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_cargo_colaborador_as = QLabel(self.frame_389)
        self.label_alterar_cargo_colaborador_as.setObjectName(u"label_alterar_cargo_colaborador_as")
        self.label_alterar_cargo_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_cargo_colaborador_as.setMaximumSize(QSize(240, 16777215))
        self.label_alterar_cargo_colaborador_as.setFont(font)

        self.verticalLayout_264.addWidget(self.label_alterar_cargo_colaborador_as)

        self.input_alterar_cargo_colaborador_comboBox_as = QComboBox(self.frame_389)
        self.input_alterar_cargo_colaborador_comboBox_as.addItem("")
        self.input_alterar_cargo_colaborador_comboBox_as.addItem("")
        self.input_alterar_cargo_colaborador_comboBox_as.addItem("")
        self.input_alterar_cargo_colaborador_comboBox_as.addItem("")
        self.input_alterar_cargo_colaborador_comboBox_as.addItem("")
        self.input_alterar_cargo_colaborador_comboBox_as.addItem("")
        self.input_alterar_cargo_colaborador_comboBox_as.addItem("")
        self.input_alterar_cargo_colaborador_comboBox_as.addItem("")
        self.input_alterar_cargo_colaborador_comboBox_as.setObjectName(u"input_alterar_cargo_colaborador_comboBox_as")
        sizePolicy1.setHeightForWidth(self.input_alterar_cargo_colaborador_comboBox_as.sizePolicy().hasHeightForWidth())
        self.input_alterar_cargo_colaborador_comboBox_as.setSizePolicy(sizePolicy1)
        self.input_alterar_cargo_colaborador_comboBox_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_cargo_colaborador_comboBox_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_cargo_colaborador_comboBox_as.setFont(font)

        self.verticalLayout_264.addWidget(self.input_alterar_cargo_colaborador_comboBox_as)


        self.horizontalLayout_130.addWidget(self.frame_389)

        self.frame_390 = QFrame(self.frame_382)
        self.frame_390.setObjectName(u"frame_390")
        self.frame_390.setMaximumSize(QSize(170, 16777215))
        self.frame_390.setFrameShape(QFrame.StyledPanel)
        self.frame_390.setFrameShadow(QFrame.Raised)
        self.verticalLayout_265 = QVBoxLayout(self.frame_390)
        self.verticalLayout_265.setSpacing(5)
        self.verticalLayout_265.setObjectName(u"verticalLayout_265")
        self.verticalLayout_265.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_periodo_colaborador_as = QLabel(self.frame_390)
        self.label_alterar_periodo_colaborador_as.setObjectName(u"label_alterar_periodo_colaborador_as")
        self.label_alterar_periodo_colaborador_as.setMaximumSize(QSize(170, 16777215))
        self.label_alterar_periodo_colaborador_as.setFont(font)

        self.verticalLayout_265.addWidget(self.label_alterar_periodo_colaborador_as)

        self.input_alterar_periodo_colaborador_comboBox_as = QComboBox(self.frame_390)
        self.input_alterar_periodo_colaborador_comboBox_as.addItem("")
        self.input_alterar_periodo_colaborador_comboBox_as.addItem("")
        self.input_alterar_periodo_colaborador_comboBox_as.addItem("")
        self.input_alterar_periodo_colaborador_comboBox_as.addItem("")
        self.input_alterar_periodo_colaborador_comboBox_as.addItem("")
        self.input_alterar_periodo_colaborador_comboBox_as.setObjectName(u"input_alterar_periodo_colaborador_comboBox_as")
        self.input_alterar_periodo_colaborador_comboBox_as.setMinimumSize(QSize(70, 30))
        self.input_alterar_periodo_colaborador_comboBox_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_periodo_colaborador_comboBox_as.setFont(font)

        self.verticalLayout_265.addWidget(self.input_alterar_periodo_colaborador_comboBox_as)


        self.horizontalLayout_130.addWidget(self.frame_390)

        self.frame_277 = QFrame(self.frame_382)
        self.frame_277.setObjectName(u"frame_277")
        self.frame_277.setFrameShape(QFrame.StyledPanel)
        self.frame_277.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_130.addWidget(self.frame_277)


        self.gridLayout_3.addWidget(self.frame_382, 4, 1, 1, 1)

        self.frame_393 = QFrame(self.frame_374)
        self.frame_393.setObjectName(u"frame_393")
        self.frame_393.setMinimumSize(QSize(0, 0))
        self.frame_393.setMaximumSize(QSize(16777215, 60))
        self.frame_393.setStyleSheet(u"")
        self.frame_393.setFrameShape(QFrame.StyledPanel)
        self.frame_393.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_132 = QHBoxLayout(self.frame_393)
        self.horizontalLayout_132.setSpacing(5)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.frame_394 = QFrame(self.frame_393)
        self.frame_394.setObjectName(u"frame_394")
        self.frame_394.setMinimumSize(QSize(0, 0))
        self.frame_394.setMaximumSize(QSize(155, 16777215))
        self.frame_394.setFrameShape(QFrame.StyledPanel)
        self.frame_394.setFrameShadow(QFrame.Raised)
        self.verticalLayout_268 = QVBoxLayout(self.frame_394)
        self.verticalLayout_268.setSpacing(0)
        self.verticalLayout_268.setObjectName(u"verticalLayout_268")
        self.verticalLayout_268.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_orgao_expedidor_colaborador_as = QLabel(self.frame_394)
        self.label_alterar_orgao_expedidor_colaborador_as.setObjectName(u"label_alterar_orgao_expedidor_colaborador_as")
        self.label_alterar_orgao_expedidor_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_orgao_expedidor_colaborador_as.setMaximumSize(QSize(155, 16777215))
        self.label_alterar_orgao_expedidor_colaborador_as.setFont(font)

        self.verticalLayout_268.addWidget(self.label_alterar_orgao_expedidor_colaborador_as)

        self.input_alterar_orgao_expedidor_colaborador_as = QLineEdit(self.frame_394)
        self.input_alterar_orgao_expedidor_colaborador_as.setObjectName(u"input_alterar_orgao_expedidor_colaborador_as")
        self.input_alterar_orgao_expedidor_colaborador_as.setMinimumSize(QSize(0, 0))
        self.input_alterar_orgao_expedidor_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_orgao_expedidor_colaborador_as.setFont(font)

        self.verticalLayout_268.addWidget(self.input_alterar_orgao_expedidor_colaborador_as)


        self.horizontalLayout_132.addWidget(self.frame_394)

        self.frame_395 = QFrame(self.frame_393)
        self.frame_395.setObjectName(u"frame_395")
        self.frame_395.setMaximumSize(QSize(151, 16777215))
        self.frame_395.setFrameShape(QFrame.StyledPanel)
        self.frame_395.setFrameShadow(QFrame.Raised)
        self.verticalLayout_269 = QVBoxLayout(self.frame_395)
        self.verticalLayout_269.setSpacing(0)
        self.verticalLayout_269.setObjectName(u"verticalLayout_269")
        self.verticalLayout_269.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_data_emissao_rg_colaborador_as = QLabel(self.frame_395)
        self.label_alterar_data_emissao_rg_colaborador_as.setObjectName(u"label_alterar_data_emissao_rg_colaborador_as")
        self.label_alterar_data_emissao_rg_colaborador_as.setMaximumSize(QSize(170, 16777215))
        self.label_alterar_data_emissao_rg_colaborador_as.setFont(font)

        self.verticalLayout_269.addWidget(self.label_alterar_data_emissao_rg_colaborador_as)

        self.input_alterar_data_emissao_rg_colaborador_as = QLineEdit(self.frame_395)
        self.input_alterar_data_emissao_rg_colaborador_as.setObjectName(u"input_alterar_data_emissao_rg_colaborador_as")
        self.input_alterar_data_emissao_rg_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_data_emissao_rg_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_data_emissao_rg_colaborador_as.setFont(font)

        self.verticalLayout_269.addWidget(self.input_alterar_data_emissao_rg_colaborador_as)


        self.horizontalLayout_132.addWidget(self.frame_395)

        self.frame_396 = QFrame(self.frame_393)
        self.frame_396.setObjectName(u"frame_396")
        self.frame_396.setMinimumSize(QSize(0, 0))
        self.frame_396.setMaximumSize(QSize(155, 16777215))
        self.frame_396.setFrameShape(QFrame.StyledPanel)
        self.frame_396.setFrameShadow(QFrame.Raised)
        self.verticalLayout_270 = QVBoxLayout(self.frame_396)
        self.verticalLayout_270.setSpacing(0)
        self.verticalLayout_270.setObjectName(u"verticalLayout_270")
        self.verticalLayout_270.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_pis_colaborador_as = QLabel(self.frame_396)
        self.label_alterar_pis_colaborador_as.setObjectName(u"label_alterar_pis_colaborador_as")
        self.label_alterar_pis_colaborador_as.setFont(font)

        self.verticalLayout_270.addWidget(self.label_alterar_pis_colaborador_as)

        self.input_alterar_pis_colaborador_as = QLineEdit(self.frame_396)
        self.input_alterar_pis_colaborador_as.setObjectName(u"input_alterar_pis_colaborador_as")
        self.input_alterar_pis_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_pis_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_pis_colaborador_as.setFont(font)

        self.verticalLayout_270.addWidget(self.input_alterar_pis_colaborador_as)


        self.horizontalLayout_132.addWidget(self.frame_396)

        self.frame_397 = QFrame(self.frame_393)
        self.frame_397.setObjectName(u"frame_397")
        self.frame_397.setMinimumSize(QSize(0, 0))
        self.frame_397.setMaximumSize(QSize(146, 16777215))
        self.frame_397.setFrameShape(QFrame.StyledPanel)
        self.frame_397.setFrameShadow(QFrame.Raised)
        self.verticalLayout_271 = QVBoxLayout(self.frame_397)
        self.verticalLayout_271.setSpacing(5)
        self.verticalLayout_271.setObjectName(u"verticalLayout_271")
        self.verticalLayout_271.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_sexo_colaborador_as = QLabel(self.frame_397)
        self.label_alterar_sexo_colaborador_as.setObjectName(u"label_alterar_sexo_colaborador_as")
        self.label_alterar_sexo_colaborador_as.setFont(font)

        self.verticalLayout_271.addWidget(self.label_alterar_sexo_colaborador_as)

        self.input_alterar_sexo_colaborador_comboBox_as = QComboBox(self.frame_397)
        self.input_alterar_sexo_colaborador_comboBox_as.addItem("")
        self.input_alterar_sexo_colaborador_comboBox_as.addItem("")
        self.input_alterar_sexo_colaborador_comboBox_as.addItem("")
        self.input_alterar_sexo_colaborador_comboBox_as.setObjectName(u"input_alterar_sexo_colaborador_comboBox_as")
        self.input_alterar_sexo_colaborador_comboBox_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_sexo_colaborador_comboBox_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_sexo_colaborador_comboBox_as.setFont(font)

        self.verticalLayout_271.addWidget(self.input_alterar_sexo_colaborador_comboBox_as)


        self.horizontalLayout_132.addWidget(self.frame_397)

        self.frame_398 = QFrame(self.frame_393)
        self.frame_398.setObjectName(u"frame_398")
        self.frame_398.setMinimumSize(QSize(0, 0))
        self.frame_398.setMaximumSize(QSize(155, 16777215))
        self.frame_398.setFrameShape(QFrame.StyledPanel)
        self.frame_398.setFrameShadow(QFrame.Raised)
        self.verticalLayout_273 = QVBoxLayout(self.frame_398)
        self.verticalLayout_273.setSpacing(0)
        self.verticalLayout_273.setObjectName(u"verticalLayout_273")
        self.verticalLayout_273.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_telefone_colaborador_as = QLabel(self.frame_398)
        self.label_alterar_telefone_colaborador_as.setObjectName(u"label_alterar_telefone_colaborador_as")
        self.label_alterar_telefone_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_telefone_colaborador_as.setMaximumSize(QSize(155, 16777215))
        self.label_alterar_telefone_colaborador_as.setFont(font)

        self.verticalLayout_273.addWidget(self.label_alterar_telefone_colaborador_as)

        self.input_alterar_telefone_colaborador_as = QLineEdit(self.frame_398)
        self.input_alterar_telefone_colaborador_as.setObjectName(u"input_alterar_telefone_colaborador_as")
        self.input_alterar_telefone_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_telefone_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_telefone_colaborador_as.setFont(font)

        self.verticalLayout_273.addWidget(self.input_alterar_telefone_colaborador_as)


        self.horizontalLayout_132.addWidget(self.frame_398)

        self.frame_399 = QFrame(self.frame_393)
        self.frame_399.setObjectName(u"frame_399")
        self.frame_399.setMinimumSize(QSize(0, 0))
        self.frame_399.setMaximumSize(QSize(240, 16777215))
        self.frame_399.setFrameShape(QFrame.StyledPanel)
        self.frame_399.setFrameShadow(QFrame.Raised)
        self.verticalLayout_275 = QVBoxLayout(self.frame_399)
        self.verticalLayout_275.setSpacing(0)
        self.verticalLayout_275.setObjectName(u"verticalLayout_275")
        self.verticalLayout_275.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_email_colaborador_as = QLabel(self.frame_399)
        self.label_alterar_email_colaborador_as.setObjectName(u"label_alterar_email_colaborador_as")
        self.label_alterar_email_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_email_colaborador_as.setMaximumSize(QSize(240, 16777215))
        self.label_alterar_email_colaborador_as.setFont(font)

        self.verticalLayout_275.addWidget(self.label_alterar_email_colaborador_as)

        self.input_alterar_email_colaborador_as = QLineEdit(self.frame_399)
        self.input_alterar_email_colaborador_as.setObjectName(u"input_alterar_email_colaborador_as")
        self.input_alterar_email_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_email_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_email_colaborador_as.setFont(font)

        self.verticalLayout_275.addWidget(self.input_alterar_email_colaborador_as)


        self.horizontalLayout_132.addWidget(self.frame_399)


        self.gridLayout_3.addWidget(self.frame_393, 1, 1, 1, 1)

        self.frame_434 = QFrame(self.frame_374)
        self.frame_434.setObjectName(u"frame_434")
        self.frame_434.setFrameShape(QFrame.StyledPanel)
        self.frame_434.setFrameShadow(QFrame.Raised)
        self.verticalLayout_303 = QVBoxLayout(self.frame_434)
        self.verticalLayout_303.setSpacing(0)
        self.verticalLayout_303.setObjectName(u"verticalLayout_303")
        self.verticalLayout_303.setContentsMargins(0, 0, 0, 0)
        self.frame_435 = QFrame(self.frame_434)
        self.frame_435.setObjectName(u"frame_435")
        self.frame_435.setMinimumSize(QSize(195, 50))
        self.frame_435.setMaximumSize(QSize(195, 50))
        self.frame_435.setStyleSheet(u"background-color: #EC848C; border-radius: 10px")
        self.frame_435.setFrameShape(QFrame.StyledPanel)
        self.frame_435.setFrameShadow(QFrame.Raised)
        self.verticalLayout_304 = QVBoxLayout(self.frame_435)
        self.verticalLayout_304.setSpacing(0)
        self.verticalLayout_304.setObjectName(u"verticalLayout_304")
        self.verticalLayout_304.setContentsMargins(15, 0, 0, 0)
        self.label_alterar_situacao_colaborador_as = QLabel(self.frame_435)
        self.label_alterar_situacao_colaborador_as.setObjectName(u"label_alterar_situacao_colaborador_as")
        self.label_alterar_situacao_colaborador_as.setMaximumSize(QSize(130, 16777215))
        self.label_alterar_situacao_colaborador_as.setFont(font)

        self.verticalLayout_304.addWidget(self.label_alterar_situacao_colaborador_as)

        self.frame_436 = QFrame(self.frame_435)
        self.frame_436.setObjectName(u"frame_436")
        self.frame_436.setFrameShape(QFrame.StyledPanel)
        self.frame_436.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_136 = QHBoxLayout(self.frame_436)
        self.horizontalLayout_136.setSpacing(0)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.horizontalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.input_alterar_situacao_ativo_colaborador_as = QRadioButton(self.frame_436)
        self.input_alterar_situacao_ativo_colaborador_as.setObjectName(u"input_alterar_situacao_ativo_colaborador_as")
        self.input_alterar_situacao_ativo_colaborador_as.setMaximumSize(QSize(80, 16777215))
        self.input_alterar_situacao_ativo_colaborador_as.setFont(font8)
        self.input_alterar_situacao_ativo_colaborador_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_136.addWidget(self.input_alterar_situacao_ativo_colaborador_as)

        self.input_alterar_situacao_inativo_colaborador_as = QRadioButton(self.frame_436)
        self.input_alterar_situacao_inativo_colaborador_as.setObjectName(u"input_alterar_situacao_inativo_colaborador_as")
        self.input_alterar_situacao_inativo_colaborador_as.setMaximumSize(QSize(80, 16777215))
        self.input_alterar_situacao_inativo_colaborador_as.setFont(font8)
        self.input_alterar_situacao_inativo_colaborador_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_136.addWidget(self.input_alterar_situacao_inativo_colaborador_as)


        self.verticalLayout_304.addWidget(self.frame_436)


        self.verticalLayout_303.addWidget(self.frame_435)


        self.gridLayout_3.addWidget(self.frame_434, 0, 2, 1, 1)

        self.frame_401 = QFrame(self.frame_374)
        self.frame_401.setObjectName(u"frame_401")
        self.frame_401.setMinimumSize(QSize(0, 0))
        self.frame_401.setMaximumSize(QSize(16777215, 60))
        self.frame_401.setStyleSheet(u"")
        self.frame_401.setFrameShape(QFrame.StyledPanel)
        self.frame_401.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_133 = QHBoxLayout(self.frame_401)
        self.horizontalLayout_133.setSpacing(5)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.horizontalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.frame_402 = QFrame(self.frame_401)
        self.frame_402.setObjectName(u"frame_402")
        self.frame_402.setMinimumSize(QSize(0, 0))
        self.frame_402.setMaximumSize(QSize(160, 16777215))
        self.frame_402.setFrameShape(QFrame.StyledPanel)
        self.frame_402.setFrameShadow(QFrame.Raised)
        self.verticalLayout_276 = QVBoxLayout(self.frame_402)
        self.verticalLayout_276.setSpacing(0)
        self.verticalLayout_276.setObjectName(u"verticalLayout_276")
        self.verticalLayout_276.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_matricula_colaborador_as = QLabel(self.frame_402)
        self.label_alterar_matricula_colaborador_as.setObjectName(u"label_alterar_matricula_colaborador_as")
        self.label_alterar_matricula_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_matricula_colaborador_as.setMaximumSize(QSize(160, 16777215))
        self.label_alterar_matricula_colaborador_as.setFont(font)

        self.verticalLayout_276.addWidget(self.label_alterar_matricula_colaborador_as)

        self.input_alterar_matricula_colaborador_as = QLineEdit(self.frame_402)
        self.input_alterar_matricula_colaborador_as.setObjectName(u"input_alterar_matricula_colaborador_as")
        self.input_alterar_matricula_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_matricula_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_matricula_colaborador_as.setFont(font)

        self.verticalLayout_276.addWidget(self.input_alterar_matricula_colaborador_as)


        self.horizontalLayout_133.addWidget(self.frame_402)

        self.frame_403 = QFrame(self.frame_401)
        self.frame_403.setObjectName(u"frame_403")
        self.frame_403.setMinimumSize(QSize(0, 0))
        self.frame_403.setMaximumSize(QSize(431, 16777215))
        self.frame_403.setFrameShape(QFrame.StyledPanel)
        self.frame_403.setFrameShadow(QFrame.Raised)
        self.verticalLayout_277 = QVBoxLayout(self.frame_403)
        self.verticalLayout_277.setSpacing(0)
        self.verticalLayout_277.setObjectName(u"verticalLayout_277")
        self.verticalLayout_277.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_nome_colaborador_as = QLabel(self.frame_403)
        self.label_alterar_nome_colaborador_as.setObjectName(u"label_alterar_nome_colaborador_as")
        self.label_alterar_nome_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_nome_colaborador_as.setMaximumSize(QSize(460, 16777215))
        self.label_alterar_nome_colaborador_as.setFont(font)

        self.verticalLayout_277.addWidget(self.label_alterar_nome_colaborador_as)

        self.input_alterar_nome_colaborador_as = QLineEdit(self.frame_403)
        self.input_alterar_nome_colaborador_as.setObjectName(u"input_alterar_nome_colaborador_as")
        self.input_alterar_nome_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_nome_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_nome_colaborador_as.setFont(font)

        self.verticalLayout_277.addWidget(self.input_alterar_nome_colaborador_as)


        self.horizontalLayout_133.addWidget(self.frame_403)

        self.frame_404 = QFrame(self.frame_401)
        self.frame_404.setObjectName(u"frame_404")
        self.frame_404.setMinimumSize(QSize(0, 0))
        self.frame_404.setMaximumSize(QSize(155, 16777215))
        self.frame_404.setFrameShape(QFrame.StyledPanel)
        self.frame_404.setFrameShadow(QFrame.Raised)
        self.verticalLayout_278 = QVBoxLayout(self.frame_404)
        self.verticalLayout_278.setSpacing(5)
        self.verticalLayout_278.setObjectName(u"verticalLayout_278")
        self.verticalLayout_278.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_data_nascimento_colaborador_as = QLabel(self.frame_404)
        self.label_alterar_data_nascimento_colaborador_as.setObjectName(u"label_alterar_data_nascimento_colaborador_as")
        self.label_alterar_data_nascimento_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_data_nascimento_colaborador_as.setMaximumSize(QSize(155, 16777215))
        self.label_alterar_data_nascimento_colaborador_as.setFont(font)

        self.verticalLayout_278.addWidget(self.label_alterar_data_nascimento_colaborador_as)

        self.input_alterar_data_nascimento_colaborador_as = QDateEdit(self.frame_404)
        self.input_alterar_data_nascimento_colaborador_as.setObjectName(u"input_alterar_data_nascimento_colaborador_as")
        sizePolicy1.setHeightForWidth(self.input_alterar_data_nascimento_colaborador_as.sizePolicy().hasHeightForWidth())
        self.input_alterar_data_nascimento_colaborador_as.setSizePolicy(sizePolicy1)
        self.input_alterar_data_nascimento_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_data_nascimento_colaborador_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_alterar_data_nascimento_colaborador_as.setFont(font8)
        self.input_alterar_data_nascimento_colaborador_as.setFocusPolicy(Qt.WheelFocus)
        self.input_alterar_data_nascimento_colaborador_as.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.input_alterar_data_nascimento_colaborador_as.setLayoutDirection(Qt.LeftToRight)
        self.input_alterar_data_nascimento_colaborador_as.setAutoFillBackground(False)
        self.input_alterar_data_nascimento_colaborador_as.setStyleSheet(u"QDateEdit{background-color: #fff; border-radius: 10px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QDateEdit:focus{outline:0; border: 2px solid #A85751}")
        self.input_alterar_data_nascimento_colaborador_as.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.input_alterar_data_nascimento_colaborador_as.setAlignment(Qt.AlignCenter)
        self.input_alterar_data_nascimento_colaborador_as.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.input_alterar_data_nascimento_colaborador_as.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.input_alterar_data_nascimento_colaborador_as.setCurrentSection(QDateTimeEdit.DaySection)
        self.input_alterar_data_nascimento_colaborador_as.setCalendarPopup(False)
        self.input_alterar_data_nascimento_colaborador_as.setCurrentSectionIndex(0)

        self.verticalLayout_278.addWidget(self.input_alterar_data_nascimento_colaborador_as, 0, Qt.AlignHCenter)


        self.horizontalLayout_133.addWidget(self.frame_404)

        self.frame_405 = QFrame(self.frame_401)
        self.frame_405.setObjectName(u"frame_405")
        self.frame_405.setMinimumSize(QSize(0, 0))
        self.frame_405.setMaximumSize(QSize(180, 16777215))
        self.frame_405.setFrameShape(QFrame.StyledPanel)
        self.frame_405.setFrameShadow(QFrame.Raised)
        self.verticalLayout_279 = QVBoxLayout(self.frame_405)
        self.verticalLayout_279.setSpacing(0)
        self.verticalLayout_279.setObjectName(u"verticalLayout_279")
        self.verticalLayout_279.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_cpf_colaborador_as = QLabel(self.frame_405)
        self.label_alterar_cpf_colaborador_as.setObjectName(u"label_alterar_cpf_colaborador_as")
        self.label_alterar_cpf_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_cpf_colaborador_as.setMaximumSize(QSize(180, 16777215))
        self.label_alterar_cpf_colaborador_as.setFont(font)

        self.verticalLayout_279.addWidget(self.label_alterar_cpf_colaborador_as)

        self.input_alterar_cpf_colaborador_as = QLineEdit(self.frame_405)
        self.input_alterar_cpf_colaborador_as.setObjectName(u"input_alterar_cpf_colaborador_as")
        self.input_alterar_cpf_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_cpf_colaborador_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_alterar_cpf_colaborador_as.setFont(font)

        self.verticalLayout_279.addWidget(self.input_alterar_cpf_colaborador_as)


        self.horizontalLayout_133.addWidget(self.frame_405)

        self.frame_406 = QFrame(self.frame_401)
        self.frame_406.setObjectName(u"frame_406")
        self.frame_406.setMinimumSize(QSize(0, 0))
        self.frame_406.setMaximumSize(QSize(160, 16777215))
        self.frame_406.setFrameShape(QFrame.StyledPanel)
        self.frame_406.setFrameShadow(QFrame.Raised)
        self.verticalLayout_280 = QVBoxLayout(self.frame_406)
        self.verticalLayout_280.setSpacing(0)
        self.verticalLayout_280.setObjectName(u"verticalLayout_280")
        self.verticalLayout_280.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_rg_colaborador_as = QLabel(self.frame_406)
        self.label_alterar_rg_colaborador_as.setObjectName(u"label_alterar_rg_colaborador_as")
        self.label_alterar_rg_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_rg_colaborador_as.setMaximumSize(QSize(160, 16777215))
        self.label_alterar_rg_colaborador_as.setFont(font)

        self.verticalLayout_280.addWidget(self.label_alterar_rg_colaborador_as)

        self.input_alterar_rg_colaborador_as = QLineEdit(self.frame_406)
        self.input_alterar_rg_colaborador_as.setObjectName(u"input_alterar_rg_colaborador_as")
        self.input_alterar_rg_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_rg_colaborador_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_alterar_rg_colaborador_as.setFont(font)

        self.verticalLayout_280.addWidget(self.input_alterar_rg_colaborador_as)


        self.horizontalLayout_133.addWidget(self.frame_406)


        self.gridLayout_3.addWidget(self.frame_401, 0, 1, 1, 1)

        self.horizontalSpacer_71 = QSpacerItem(194, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_71, 4, 2, 1, 1)

        self.horizontalSpacer_70 = QSpacerItem(123, 55, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_70, 4, 0, 1, 1)

        self.frame_375 = QFrame(self.frame_374)
        self.frame_375.setObjectName(u"frame_375")
        self.frame_375.setMinimumSize(QSize(0, 0))
        self.frame_375.setMaximumSize(QSize(16777215, 60))
        self.frame_375.setStyleSheet(u"")
        self.frame_375.setFrameShape(QFrame.StyledPanel)
        self.frame_375.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_129 = QHBoxLayout(self.frame_375)
        self.horizontalLayout_129.setSpacing(5)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.frame_385 = QFrame(self.frame_375)
        self.frame_385.setObjectName(u"frame_385")
        self.frame_385.setMinimumSize(QSize(282, 0))
        self.frame_385.setMaximumSize(QSize(281, 16777215))
        self.frame_385.setFrameShape(QFrame.StyledPanel)
        self.frame_385.setFrameShadow(QFrame.Raised)
        self.verticalLayout_256 = QVBoxLayout(self.frame_385)
        self.verticalLayout_256.setSpacing(5)
        self.verticalLayout_256.setObjectName(u"verticalLayout_256")
        self.verticalLayout_256.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_usuario_colaborador_as_2 = QLabel(self.frame_385)
        self.label_alterar_usuario_colaborador_as_2.setObjectName(u"label_alterar_usuario_colaborador_as_2")
        self.label_alterar_usuario_colaborador_as_2.setMinimumSize(QSize(0, 0))
        self.label_alterar_usuario_colaborador_as_2.setMaximumSize(QSize(280, 16777215))
        self.label_alterar_usuario_colaborador_as_2.setFont(font)

        self.verticalLayout_256.addWidget(self.label_alterar_usuario_colaborador_as_2)

        self.input_alterar_usuario_colaborador_as_2 = QLineEdit(self.frame_385)
        self.input_alterar_usuario_colaborador_as_2.setObjectName(u"input_alterar_usuario_colaborador_as_2")
        self.input_alterar_usuario_colaborador_as_2.setMinimumSize(QSize(0, 30))
        self.input_alterar_usuario_colaborador_as_2.setMaximumSize(QSize(280, 30))
        self.input_alterar_usuario_colaborador_as_2.setFont(font)

        self.verticalLayout_256.addWidget(self.input_alterar_usuario_colaborador_as_2)


        self.horizontalLayout_129.addWidget(self.frame_385)

        self.frame_376 = QFrame(self.frame_375)
        self.frame_376.setObjectName(u"frame_376")
        self.frame_376.setMinimumSize(QSize(231, 0))
        self.frame_376.setMaximumSize(QSize(230, 16777215))
        self.frame_376.setFrameShape(QFrame.StyledPanel)
        self.frame_376.setFrameShadow(QFrame.Raised)
        self.verticalLayout_255 = QVBoxLayout(self.frame_376)
        self.verticalLayout_255.setSpacing(0)
        self.verticalLayout_255.setObjectName(u"verticalLayout_255")
        self.verticalLayout_255.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_senha_colaborador_as_2 = QLabel(self.frame_376)
        self.label_alterar_senha_colaborador_as_2.setObjectName(u"label_alterar_senha_colaborador_as_2")
        self.label_alterar_senha_colaborador_as_2.setMinimumSize(QSize(0, 0))
        self.label_alterar_senha_colaborador_as_2.setMaximumSize(QSize(230, 16777215))
        self.label_alterar_senha_colaborador_as_2.setFont(font)

        self.verticalLayout_255.addWidget(self.label_alterar_senha_colaborador_as_2)

        self.input_alterar_senha_colaborador_as_2 = QLineEdit(self.frame_376)
        self.input_alterar_senha_colaborador_as_2.setObjectName(u"input_alterar_senha_colaborador_as_2")
        self.input_alterar_senha_colaborador_as_2.setMinimumSize(QSize(0, 30))
        self.input_alterar_senha_colaborador_as_2.setMaximumSize(QSize(229, 30))
        self.input_alterar_senha_colaborador_as_2.setFont(font)

        self.verticalLayout_255.addWidget(self.input_alterar_senha_colaborador_as_2)


        self.horizontalLayout_129.addWidget(self.frame_376)

        self.frame_377 = QFrame(self.frame_375)
        self.frame_377.setObjectName(u"frame_377")
        self.frame_377.setMinimumSize(QSize(231, 0))
        self.frame_377.setMaximumSize(QSize(230, 16777215))
        self.frame_377.setFrameShape(QFrame.StyledPanel)
        self.frame_377.setFrameShadow(QFrame.Raised)
        self.verticalLayout_261 = QVBoxLayout(self.frame_377)
        self.verticalLayout_261.setSpacing(0)
        self.verticalLayout_261.setObjectName(u"verticalLayout_261")
        self.verticalLayout_261.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_confirmar_senha_colaborador_as_2 = QLabel(self.frame_377)
        self.label_alterar_confirmar_senha_colaborador_as_2.setObjectName(u"label_alterar_confirmar_senha_colaborador_as_2")
        self.label_alterar_confirmar_senha_colaborador_as_2.setMinimumSize(QSize(0, 0))
        self.label_alterar_confirmar_senha_colaborador_as_2.setMaximumSize(QSize(230, 16777215))
        self.label_alterar_confirmar_senha_colaborador_as_2.setFont(font)

        self.verticalLayout_261.addWidget(self.label_alterar_confirmar_senha_colaborador_as_2)

        self.input_alterar_confirmar_senha_colaborador_as_2 = QLineEdit(self.frame_377)
        self.input_alterar_confirmar_senha_colaborador_as_2.setObjectName(u"input_alterar_confirmar_senha_colaborador_as_2")
        self.input_alterar_confirmar_senha_colaborador_as_2.setMinimumSize(QSize(0, 30))
        self.input_alterar_confirmar_senha_colaborador_as_2.setMaximumSize(QSize(229, 30))
        self.input_alterar_confirmar_senha_colaborador_as_2.setFont(font)

        self.verticalLayout_261.addWidget(self.input_alterar_confirmar_senha_colaborador_as_2)


        self.horizontalLayout_129.addWidget(self.frame_377)

        self.frame_379 = QFrame(self.frame_375)
        self.frame_379.setObjectName(u"frame_379")
        self.frame_379.setMinimumSize(QSize(0, 0))
        self.frame_379.setMaximumSize(QSize(230, 16777215))
        self.frame_379.setFrameShape(QFrame.StyledPanel)
        self.frame_379.setFrameShadow(QFrame.Raised)
        self.verticalLayout_257 = QVBoxLayout(self.frame_379)
        self.verticalLayout_257.setSpacing(0)
        self.verticalLayout_257.setObjectName(u"verticalLayout_257")
        self.verticalLayout_257.setContentsMargins(0, 0, 0, 0)
        self.input_alterar_id_endereco_colaborador_as = QLineEdit(self.frame_379)
        self.input_alterar_id_endereco_colaborador_as.setObjectName(u"input_alterar_id_endereco_colaborador_as")
        self.input_alterar_id_endereco_colaborador_as.setEnabled(False)
        self.input_alterar_id_endereco_colaborador_as.setStyleSheet(u"background-color:transparent;\n"
"border-color: transparent;")

        self.verticalLayout_257.addWidget(self.input_alterar_id_endereco_colaborador_as)


        self.horizontalLayout_129.addWidget(self.frame_379)

        self.frame_380 = QFrame(self.frame_375)
        self.frame_380.setObjectName(u"frame_380")
        self.frame_380.setMinimumSize(QSize(0, 0))
        self.frame_380.setMaximumSize(QSize(180, 16777215))
        self.frame_380.setFrameShape(QFrame.StyledPanel)
        self.frame_380.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_941 = QHBoxLayout(self.frame_380)
        self.horizontalLayout_941.setObjectName(u"horizontalLayout_941")
        self.input_alterar_id_matricula_colaborador_as = QLineEdit(self.frame_380)
        self.input_alterar_id_matricula_colaborador_as.setObjectName(u"input_alterar_id_matricula_colaborador_as")
        self.input_alterar_id_matricula_colaborador_as.setEnabled(False)
        self.input_alterar_id_matricula_colaborador_as.setStyleSheet(u"background-color:transparent;\n"
"border-color: transparent;")

        self.horizontalLayout_941.addWidget(self.input_alterar_id_matricula_colaborador_as)


        self.horizontalLayout_129.addWidget(self.frame_380)

        self.frame_381 = QFrame(self.frame_375)
        self.frame_381.setObjectName(u"frame_381")
        self.frame_381.setMinimumSize(QSize(0, 0))
        self.frame_381.setMaximumSize(QSize(80, 16777215))
        self.frame_381.setFrameShape(QFrame.StyledPanel)
        self.frame_381.setFrameShadow(QFrame.Raised)
        self.verticalLayout_258 = QVBoxLayout(self.frame_381)
        self.verticalLayout_258.setSpacing(0)
        self.verticalLayout_258.setObjectName(u"verticalLayout_258")
        self.verticalLayout_258.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_129.addWidget(self.frame_381)


        self.gridLayout_3.addWidget(self.frame_375, 5, 1, 1, 1)

        self.frame_407 = QFrame(self.frame_374)
        self.frame_407.setObjectName(u"frame_407")
        self.frame_407.setMinimumSize(QSize(0, 50))
        self.frame_407.setMaximumSize(QSize(16777215, 65))
        self.frame_407.setStyleSheet(u"")
        self.frame_407.setFrameShape(QFrame.StyledPanel)
        self.frame_407.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_134 = QHBoxLayout(self.frame_407)
        self.horizontalLayout_134.setSpacing(5)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_134.setContentsMargins(0, 0, 0, 0)
        self.frame_408 = QFrame(self.frame_407)
        self.frame_408.setObjectName(u"frame_408")
        self.frame_408.setMinimumSize(QSize(0, 0))
        self.frame_408.setMaximumSize(QSize(151, 16777215))
        self.frame_408.setFrameShape(QFrame.StyledPanel)
        self.frame_408.setFrameShadow(QFrame.Raised)
        self.verticalLayout_295 = QVBoxLayout(self.frame_408)
        self.verticalLayout_295.setSpacing(0)
        self.verticalLayout_295.setObjectName(u"verticalLayout_295")
        self.verticalLayout_295.setContentsMargins(0, 0, 0, 0)
        self.frame_430 = QFrame(self.frame_408)
        self.frame_430.setObjectName(u"frame_430")
        self.frame_430.setMaximumSize(QSize(170, 16777215))
        self.frame_430.setFrameShape(QFrame.StyledPanel)
        self.frame_430.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_135 = QHBoxLayout(self.frame_430)
        self.horizontalLayout_135.setSpacing(0)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.horizontalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.frame_431 = QFrame(self.frame_430)
        self.frame_431.setObjectName(u"frame_431")
        self.frame_431.setMinimumSize(QSize(160, 62))
        self.frame_431.setMaximumSize(QSize(150, 62))
        self.frame_431.setFrameShape(QFrame.StyledPanel)
        self.frame_431.setFrameShadow(QFrame.Raised)
        self.verticalLayout_281 = QVBoxLayout(self.frame_431)
        self.verticalLayout_281.setSpacing(2)
        self.verticalLayout_281.setObjectName(u"verticalLayout_281")
        self.verticalLayout_281.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_cep_colaborador_as = QLabel(self.frame_431)
        self.label_alterar_cep_colaborador_as.setObjectName(u"label_alterar_cep_colaborador_as")
        self.label_alterar_cep_colaborador_as.setMinimumSize(QSize(50, 15))
        self.label_alterar_cep_colaborador_as.setMaximumSize(QSize(50, 24))
        self.label_alterar_cep_colaborador_as.setFont(font)

        self.verticalLayout_281.addWidget(self.label_alterar_cep_colaborador_as)

        self.input_alterar_cep_colaborador_as = QLineEdit(self.frame_431)
        self.input_alterar_cep_colaborador_as.setObjectName(u"input_alterar_cep_colaborador_as")
        self.input_alterar_cep_colaborador_as.setMinimumSize(QSize(145, 30))
        self.input_alterar_cep_colaborador_as.setMaximumSize(QSize(146, 30))
        self.input_alterar_cep_colaborador_as.setFont(font)
        self.input_alterar_cep_colaborador_as.setStyleSheet(u"")
        self.input_alterar_cep_colaborador_as.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_281.addWidget(self.input_alterar_cep_colaborador_as)


        self.horizontalLayout_135.addWidget(self.frame_431)

        self.frame_432 = QFrame(self.frame_430)
        self.frame_432.setObjectName(u"frame_432")
        self.frame_432.setMinimumSize(QSize(22, 61))
        self.frame_432.setMaximumSize(QSize(31, 61))
        self.frame_432.setFrameShape(QFrame.StyledPanel)
        self.frame_432.setFrameShadow(QFrame.Raised)
        self.verticalLayout_296 = QVBoxLayout(self.frame_432)
        self.verticalLayout_296.setSpacing(0)
        self.verticalLayout_296.setObjectName(u"verticalLayout_296")
        self.verticalLayout_296.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_21 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_296.addItem(self.verticalSpacer_21)

        self.btn_alterar_cep_buscar_colaborador_as = QPushButton(self.frame_432)
        self.btn_alterar_cep_buscar_colaborador_as.setObjectName(u"btn_alterar_cep_buscar_colaborador_as")
        sizePolicy2.setHeightForWidth(self.btn_alterar_cep_buscar_colaborador_as.sizePolicy().hasHeightForWidth())
        self.btn_alterar_cep_buscar_colaborador_as.setSizePolicy(sizePolicy2)
        self.btn_alterar_cep_buscar_colaborador_as.setMinimumSize(QSize(0, 30))
        self.btn_alterar_cep_buscar_colaborador_as.setMaximumSize(QSize(25, 30))
        self.btn_alterar_cep_buscar_colaborador_as.setStyleSheet(u"QPushButton{\n"
"        background: rgb(243, 185, 191);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        background: rgb(255, 194, 201);\n"
"        border: 1px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"        background: rgb(180, 106, 102);\n"
"        border: 2px  solid rgb(180, 106, 102);\n"
"        border-width: 2px;\n"
"		border-top-right-radius: 10px;\n"
"		border-bottom-right-radius: 10px;\n"
"        color: rgb(249, 217, 221);   \n"
"}")
        self.btn_alterar_cep_buscar_colaborador_as.setIcon(icon12)

        self.verticalLayout_296.addWidget(self.btn_alterar_cep_buscar_colaborador_as)


        self.horizontalLayout_135.addWidget(self.frame_432)


        self.verticalLayout_295.addWidget(self.frame_430)


        self.horizontalLayout_134.addWidget(self.frame_408)

        self.frame_409 = QFrame(self.frame_407)
        self.frame_409.setObjectName(u"frame_409")
        self.frame_409.setMinimumSize(QSize(281, 0))
        self.frame_409.setMaximumSize(QSize(281, 16777215))
        self.frame_409.setFrameShape(QFrame.StyledPanel)
        self.frame_409.setFrameShadow(QFrame.Raised)
        self.verticalLayout_282 = QVBoxLayout(self.frame_409)
        self.verticalLayout_282.setSpacing(5)
        self.verticalLayout_282.setObjectName(u"verticalLayout_282")
        self.verticalLayout_282.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_logradouro_colaborador_as = QLabel(self.frame_409)
        self.label_alterar_logradouro_colaborador_as.setObjectName(u"label_alterar_logradouro_colaborador_as")
        self.label_alterar_logradouro_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_logradouro_colaborador_as.setMaximumSize(QSize(280, 16777215))
        self.label_alterar_logradouro_colaborador_as.setFont(font)

        self.verticalLayout_282.addWidget(self.label_alterar_logradouro_colaborador_as)

        self.input_alterar_logradouro_colaborador_as = QLineEdit(self.frame_409)
        self.input_alterar_logradouro_colaborador_as.setObjectName(u"input_alterar_logradouro_colaborador_as")
        self.input_alterar_logradouro_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_logradouro_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_logradouro_colaborador_as.setFont(font)

        self.verticalLayout_282.addWidget(self.input_alterar_logradouro_colaborador_as)


        self.horizontalLayout_134.addWidget(self.frame_409)

        self.frame_410 = QFrame(self.frame_407)
        self.frame_410.setObjectName(u"frame_410")
        self.frame_410.setMinimumSize(QSize(0, 0))
        self.frame_410.setMaximumSize(QSize(120, 16777215))
        self.frame_410.setFrameShape(QFrame.StyledPanel)
        self.frame_410.setFrameShadow(QFrame.Raised)
        self.verticalLayout_297 = QVBoxLayout(self.frame_410)
        self.verticalLayout_297.setSpacing(5)
        self.verticalLayout_297.setObjectName(u"verticalLayout_297")
        self.verticalLayout_297.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_numero_colaborador_as = QLabel(self.frame_410)
        self.label_alterar_numero_colaborador_as.setObjectName(u"label_alterar_numero_colaborador_as")
        self.label_alterar_numero_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_numero_colaborador_as.setMaximumSize(QSize(60, 16777215))
        self.label_alterar_numero_colaborador_as.setFont(font)

        self.verticalLayout_297.addWidget(self.label_alterar_numero_colaborador_as)

        self.input_alterar_numero_colaborador_as = QLineEdit(self.frame_410)
        self.input_alterar_numero_colaborador_as.setObjectName(u"input_alterar_numero_colaborador_as")
        self.input_alterar_numero_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_numero_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_numero_colaborador_as.setFont(font)

        self.verticalLayout_297.addWidget(self.input_alterar_numero_colaborador_as)


        self.horizontalLayout_134.addWidget(self.frame_410)

        self.frame_411 = QFrame(self.frame_407)
        self.frame_411.setObjectName(u"frame_411")
        self.frame_411.setMinimumSize(QSize(0, 0))
        self.frame_411.setMaximumSize(QSize(230, 16777215))
        self.frame_411.setFrameShape(QFrame.StyledPanel)
        self.frame_411.setFrameShadow(QFrame.Raised)
        self.verticalLayout_298 = QVBoxLayout(self.frame_411)
        self.verticalLayout_298.setSpacing(0)
        self.verticalLayout_298.setObjectName(u"verticalLayout_298")
        self.verticalLayout_298.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_bairro_colaborador_as = QLabel(self.frame_411)
        self.label_alterar_bairro_colaborador_as.setObjectName(u"label_alterar_bairro_colaborador_as")
        self.label_alterar_bairro_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_bairro_colaborador_as.setMaximumSize(QSize(230, 16777215))
        self.label_alterar_bairro_colaborador_as.setFont(font)

        self.verticalLayout_298.addWidget(self.label_alterar_bairro_colaborador_as)

        self.input_alterar_bairro_colaborador_as = QLineEdit(self.frame_411)
        self.input_alterar_bairro_colaborador_as.setObjectName(u"input_alterar_bairro_colaborador_as")
        self.input_alterar_bairro_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_bairro_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_bairro_colaborador_as.setFont(font)

        self.verticalLayout_298.addWidget(self.input_alterar_bairro_colaborador_as)


        self.horizontalLayout_134.addWidget(self.frame_411)

        self.frame_412 = QFrame(self.frame_407)
        self.frame_412.setObjectName(u"frame_412")
        self.frame_412.setMinimumSize(QSize(0, 0))
        self.frame_412.setMaximumSize(QSize(180, 16777215))
        self.frame_412.setFrameShape(QFrame.StyledPanel)
        self.frame_412.setFrameShadow(QFrame.Raised)
        self.verticalLayout_299 = QVBoxLayout(self.frame_412)
        self.verticalLayout_299.setSpacing(5)
        self.verticalLayout_299.setObjectName(u"verticalLayout_299")
        self.verticalLayout_299.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_cidade_colaborador_as = QLabel(self.frame_412)
        self.label_alterar_cidade_colaborador_as.setObjectName(u"label_alterar_cidade_colaborador_as")
        self.label_alterar_cidade_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_cidade_colaborador_as.setMaximumSize(QSize(180, 16777215))
        self.label_alterar_cidade_colaborador_as.setFont(font)

        self.verticalLayout_299.addWidget(self.label_alterar_cidade_colaborador_as)

        self.input_alterar_cidade_colaborador_as = QLineEdit(self.frame_412)
        self.input_alterar_cidade_colaborador_as.setObjectName(u"input_alterar_cidade_colaborador_as")
        self.input_alterar_cidade_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_cidade_colaborador_as.setMaximumSize(QSize(16777215, 30))
        self.input_alterar_cidade_colaborador_as.setFont(font)

        self.verticalLayout_299.addWidget(self.input_alterar_cidade_colaborador_as)


        self.horizontalLayout_134.addWidget(self.frame_412)

        self.frame_413 = QFrame(self.frame_407)
        self.frame_413.setObjectName(u"frame_413")
        self.frame_413.setMinimumSize(QSize(0, 0))
        self.frame_413.setMaximumSize(QSize(80, 16777215))
        self.frame_413.setFrameShape(QFrame.StyledPanel)
        self.frame_413.setFrameShadow(QFrame.Raised)
        self.verticalLayout_300 = QVBoxLayout(self.frame_413)
        self.verticalLayout_300.setSpacing(5)
        self.verticalLayout_300.setObjectName(u"verticalLayout_300")
        self.verticalLayout_300.setContentsMargins(0, 0, 0, 0)
        self.label_alterar_estado_colaborador_as = QLabel(self.frame_413)
        self.label_alterar_estado_colaborador_as.setObjectName(u"label_alterar_estado_colaborador_as")
        self.label_alterar_estado_colaborador_as.setMinimumSize(QSize(0, 0))
        self.label_alterar_estado_colaborador_as.setMaximumSize(QSize(80, 16777215))
        self.label_alterar_estado_colaborador_as.setFont(font)

        self.verticalLayout_300.addWidget(self.label_alterar_estado_colaborador_as)

        self.input_alterar_estado_colaborador_as = QLineEdit(self.frame_413)
        self.input_alterar_estado_colaborador_as.setObjectName(u"input_alterar_estado_colaborador_as")
        self.input_alterar_estado_colaborador_as.setMinimumSize(QSize(0, 30))
        self.input_alterar_estado_colaborador_as.setMaximumSize(QSize(16777215, 16777215))
        self.input_alterar_estado_colaborador_as.setFont(font)

        self.verticalLayout_300.addWidget(self.input_alterar_estado_colaborador_as)


        self.horizontalLayout_134.addWidget(self.frame_413)


        self.gridLayout_3.addWidget(self.frame_407, 2, 1, 1, 1)

        self.frame_414 = QFrame(self.frame_374)
        self.frame_414.setObjectName(u"frame_414")
        self.frame_414.setMinimumSize(QSize(125, 200))
        self.frame_414.setMaximumSize(QSize(125, 200))
        self.frame_414.setFrameShape(QFrame.StyledPanel)
        self.frame_414.setFrameShadow(QFrame.Raised)
        self.verticalLayout_301 = QVBoxLayout(self.frame_414)
        self.verticalLayout_301.setSpacing(0)
        self.verticalLayout_301.setObjectName(u"verticalLayout_301")
        self.verticalLayout_301.setContentsMargins(0, 0, 0, 0)
        self.input_alterar_foto_colaborador_as = QPushButton(self.frame_414)
        self.input_alterar_foto_colaborador_as.setObjectName(u"input_alterar_foto_colaborador_as")
        self.input_alterar_foto_colaborador_as.setMinimumSize(QSize(125, 153))
        self.input_alterar_foto_colaborador_as.setMaximumSize(QSize(125, 153))
        self.input_alterar_foto_colaborador_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.input_alterar_foto_colaborador_as.setStyleSheet(u"background-color: #F3B9BF; border: none")
        self.input_alterar_foto_colaborador_as.setIcon(icon11)
        self.input_alterar_foto_colaborador_as.setIconSize(QSize(120, 120))

        self.verticalLayout_301.addWidget(self.input_alterar_foto_colaborador_as)

        self.frame_433 = QFrame(self.frame_414)
        self.frame_433.setObjectName(u"frame_433")
        self.frame_433.setStyleSheet(u"background-color: rgb(243, 185, 191);")
        self.frame_433.setFrameShape(QFrame.StyledPanel)
        self.frame_433.setFrameShadow(QFrame.Raised)
        self.verticalLayout_302 = QVBoxLayout(self.frame_433)
        self.verticalLayout_302.setObjectName(u"verticalLayout_302")
        self.verticalLayout_302.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_301.addWidget(self.frame_433)

        self.verticalSpacer_14 = QSpacerItem(20, 19, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_301.addItem(self.verticalSpacer_14)


        self.gridLayout_3.addWidget(self.frame_414, 0, 0, 3, 1, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_137.addWidget(self.frame_374)


        self.verticalLayout_245.addWidget(self.frame_364)

        self.frame_365 = QFrame(self.frame_363)
        self.frame_365.setObjectName(u"frame_365")
        self.frame_365.setMaximumSize(QSize(16777215, 117))
        self.frame_365.setFrameShape(QFrame.StyledPanel)
        self.frame_365.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_128 = QHBoxLayout(self.frame_365)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.frame_366 = QFrame(self.frame_365)
        self.frame_366.setObjectName(u"frame_366")
        self.frame_366.setMinimumSize(QSize(0, 0))
        self.frame_366.setFrameShape(QFrame.StyledPanel)
        self.frame_366.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_121 = QHBoxLayout(self.frame_366)
        self.horizontalLayout_121.setSpacing(10)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.frame_367 = QFrame(self.frame_366)
        self.frame_367.setObjectName(u"frame_367")
        self.frame_367.setFrameShape(QFrame.StyledPanel)
        self.frame_367.setFrameShadow(QFrame.Raised)
        self.verticalLayout_246 = QVBoxLayout(self.frame_367)
        self.verticalLayout_246.setSpacing(5)
        self.verticalLayout_246.setObjectName(u"verticalLayout_246")
        self.verticalLayout_246.setContentsMargins(0, 0, 0, 0)
        self.frame_368 = QFrame(self.frame_367)
        self.frame_368.setObjectName(u"frame_368")
        self.frame_368.setFrameShape(QFrame.StyledPanel)
        self.frame_368.setFrameShadow(QFrame.Raised)
        self.verticalLayout_247 = QVBoxLayout(self.frame_368)
        self.verticalLayout_247.setSpacing(0)
        self.verticalLayout_247.setObjectName(u"verticalLayout_247")
        self.verticalLayout_247.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_246.addWidget(self.frame_368)

        self.frame_369 = QFrame(self.frame_367)
        self.frame_369.setObjectName(u"frame_369")
        self.frame_369.setFrameShape(QFrame.StyledPanel)
        self.frame_369.setFrameShadow(QFrame.Raised)
        self.verticalLayout_248 = QVBoxLayout(self.frame_369)
        self.verticalLayout_248.setObjectName(u"verticalLayout_248")
        self.verticalLayout_248.setContentsMargins(0, 0, 0, 0)
        self.btn_alterar_voltar_cadastro_colaborador_as = QPushButton(self.frame_369)
        self.btn_alterar_voltar_cadastro_colaborador_as.setObjectName(u"btn_alterar_voltar_cadastro_colaborador_as")
        self.btn_alterar_voltar_cadastro_colaborador_as.setMinimumSize(QSize(100, 40))
        self.btn_alterar_voltar_cadastro_colaborador_as.setMaximumSize(QSize(100, 40))
        self.btn_alterar_voltar_cadastro_colaborador_as.setFont(font11)
        self.btn_alterar_voltar_cadastro_colaborador_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_voltar_cadastro_colaborador_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.verticalLayout_248.addWidget(self.btn_alterar_voltar_cadastro_colaborador_as)


        self.verticalLayout_246.addWidget(self.frame_369)


        self.horizontalLayout_121.addWidget(self.frame_367)

        self.frame_370 = QFrame(self.frame_366)
        self.frame_370.setObjectName(u"frame_370")
        self.frame_370.setMinimumSize(QSize(282, 0))
        self.frame_370.setMaximumSize(QSize(281, 16777215))
        self.frame_370.setFrameShape(QFrame.StyledPanel)
        self.frame_370.setFrameShadow(QFrame.Raised)
        self.verticalLayout_249 = QVBoxLayout(self.frame_370)
        self.verticalLayout_249.setSpacing(5)
        self.verticalLayout_249.setObjectName(u"verticalLayout_249")
        self.verticalLayout_249.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_121.addWidget(self.frame_370)

        self.frame_371 = QFrame(self.frame_366)
        self.frame_371.setObjectName(u"frame_371")
        self.frame_371.setMinimumSize(QSize(231, 0))
        self.frame_371.setMaximumSize(QSize(230, 16777215))
        self.frame_371.setFrameShape(QFrame.StyledPanel)
        self.frame_371.setFrameShadow(QFrame.Raised)
        self.verticalLayout_250 = QVBoxLayout(self.frame_371)
        self.verticalLayout_250.setSpacing(0)
        self.verticalLayout_250.setObjectName(u"verticalLayout_250")
        self.verticalLayout_250.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_121.addWidget(self.frame_371)

        self.frame_372 = QFrame(self.frame_366)
        self.frame_372.setObjectName(u"frame_372")
        self.frame_372.setMinimumSize(QSize(231, 0))
        self.frame_372.setMaximumSize(QSize(230, 16777215))
        self.frame_372.setFrameShape(QFrame.StyledPanel)
        self.frame_372.setFrameShadow(QFrame.Raised)
        self.verticalLayout_252 = QVBoxLayout(self.frame_372)
        self.verticalLayout_252.setSpacing(0)
        self.verticalLayout_252.setObjectName(u"verticalLayout_252")
        self.verticalLayout_252.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_121.addWidget(self.frame_372)

        self.horizontalSpacer_69 = QSpacerItem(100, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_121.addItem(self.horizontalSpacer_69)

        self.frame_373 = QFrame(self.frame_366)
        self.frame_373.setObjectName(u"frame_373")
        self.frame_373.setFrameShape(QFrame.StyledPanel)
        self.frame_373.setFrameShadow(QFrame.Raised)
        self.verticalLayout_254 = QVBoxLayout(self.frame_373)
        self.verticalLayout_254.setSpacing(5)
        self.verticalLayout_254.setObjectName(u"verticalLayout_254")
        self.verticalLayout_254.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_13 = QSpacerItem(20, 27, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_254.addItem(self.verticalSpacer_13)

        self.btn_alterar_concluir_cadastro_colaborador_as = QPushButton(self.frame_373)
        self.btn_alterar_concluir_cadastro_colaborador_as.setObjectName(u"btn_alterar_concluir_cadastro_colaborador_as")
        self.btn_alterar_concluir_cadastro_colaborador_as.setMinimumSize(QSize(140, 40))
        self.btn_alterar_concluir_cadastro_colaborador_as.setMaximumSize(QSize(140, 40))
        self.btn_alterar_concluir_cadastro_colaborador_as.setFont(font11)
        self.btn_alterar_concluir_cadastro_colaborador_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_concluir_cadastro_colaborador_as.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px;}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}\n"
"\n"
"")

        self.verticalLayout_254.addWidget(self.btn_alterar_concluir_cadastro_colaborador_as)


        self.horizontalLayout_121.addWidget(self.frame_373, 0, Qt.AlignHCenter)


        self.horizontalLayout_128.addWidget(self.frame_366)


        self.verticalLayout_245.addWidget(self.frame_365)


        self.horizontalLayout_120.addWidget(self.frame_363)

        self.horizontalSpacer_68 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_120.addItem(self.horizontalSpacer_68)


        self.verticalLayout_251.addWidget(self.frame_362)

        self.stackedWidget_8.addWidget(self.page_alterar_colaborador_as)

        self.verticalLayout_188.addWidget(self.stackedWidget_8)


        self.verticalLayout_185.addWidget(self.frame_280)


        self.verticalLayout_283.addWidget(self.frame_273)

        self.stackedWidget_2.addWidget(self.page_alterar_dados_as)

        self.gridLayout_4.addWidget(self.stackedWidget_2, 0, 0, 1, 1)


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
        self.btn_alterar_foto_senha_farm = QPushButton(self.frame_20)
        self.btn_alterar_foto_senha_farm.setObjectName(u"btn_alterar_foto_senha_farm")
        self.btn_alterar_foto_senha_farm.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_foto_senha_farm.setStyleSheet(u"QPushButton{background-color: #E33B4E; border: none}")
        self.btn_alterar_foto_senha_farm.setIcon(icon1)
        self.btn_alterar_foto_senha_farm.setIconSize(QSize(140, 180))

        self.verticalLayout_14.addWidget(self.btn_alterar_foto_senha_farm)

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
        self.btn_cadastrar_farm.setFont(font6)
        self.btn_cadastrar_farm.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_farm.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon23 = QIcon()
        icon23.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/remedio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar_farm.setIcon(icon23)
        self.btn_cadastrar_farm.setIconSize(QSize(30, 30))

        self.verticalLayout_35.addWidget(self.btn_cadastrar_farm)

        self.btn_retirar_farm = QPushButton(self.frame_52)
        self.btn_retirar_farm.setObjectName(u"btn_retirar_farm")
        self.btn_retirar_farm.setMinimumSize(QSize(140, 45))
        self.btn_retirar_farm.setFont(font6)
        self.btn_retirar_farm.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_retirar_farm.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon24 = QIcon()
        icon24.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/medicamento.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_retirar_farm.setIcon(icon24)
        self.btn_retirar_farm.setIconSize(QSize(30, 30))

        self.verticalLayout_35.addWidget(self.btn_retirar_farm)

        self.btn_estoque_farm = QPushButton(self.frame_52)
        self.btn_estoque_farm.setObjectName(u"btn_estoque_farm")
        self.btn_estoque_farm.setMinimumSize(QSize(140, 45))
        self.btn_estoque_farm.setFont(font6)
        self.btn_estoque_farm.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_estoque_farm.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon25 = QIcon()
        icon25.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/estoque-pronto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_estoque_farm.setIcon(icon25)
        self.btn_estoque_farm.setIconSize(QSize(30, 30))

        self.verticalLayout_35.addWidget(self.btn_estoque_farm)


        self.horizontalLayout_36.addWidget(self.frame_52)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_18)


        self.verticalLayout_14.addWidget(self.frame_51)

        self.verticalSpacer_5 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

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
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 20)
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
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 30)
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

        self.frame_216 = QFrame(self.frame_23)
        self.frame_216.setObjectName(u"frame_216")
        self.frame_216.setMinimumSize(QSize(0, 30))
        self.frame_216.setMaximumSize(QSize(16777215, 30))
        self.frame_216.setFrameShape(QFrame.StyledPanel)
        self.frame_216.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.frame_216)


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
        self.horizontalLayout_16.setContentsMargins(0, 8, 8, 0)
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
        self.btn_alterar_foto_senha_fisio = QPushButton(self.frame_19)
        self.btn_alterar_foto_senha_fisio.setObjectName(u"btn_alterar_foto_senha_fisio")
        self.btn_alterar_foto_senha_fisio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_foto_senha_fisio.setStyleSheet(u"QPushButton{background-color: #E33B4E; border: none}")
        self.btn_alterar_foto_senha_fisio.setIcon(icon1)
        self.btn_alterar_foto_senha_fisio.setIconSize(QSize(140, 180))

        self.verticalLayout_11.addWidget(self.btn_alterar_foto_senha_fisio)

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
        self.btn_consulta_fisio.setFont(font6)
        self.btn_consulta_fisio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_consulta_fisio.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_consulta_fisio.setIcon(icon3)
        self.btn_consulta_fisio.setIconSize(QSize(30, 30))

        self.verticalLayout_20.addWidget(self.btn_consulta_fisio)

        self.btn_relatorios_fisio = QPushButton(self.frame_53)
        self.btn_relatorios_fisio.setObjectName(u"btn_relatorios_fisio")
        self.btn_relatorios_fisio.setMinimumSize(QSize(140, 45))
        self.btn_relatorios_fisio.setFont(font6)
        self.btn_relatorios_fisio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_relatorios_fisio.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_relatorios_fisio.setIcon(icon5)
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
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 20)
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
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 30)
        self.btn_sair_fisio = QPushButton(self.frame_54)
        self.btn_sair_fisio.setObjectName(u"btn_sair_fisio")
        self.btn_sair_fisio.setMinimumSize(QSize(120, 40))
        self.btn_sair_fisio.setFont(font2)
        self.btn_sair_fisio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sair_fisio.setLayoutDirection(Qt.RightToLeft)
        self.btn_sair_fisio.setStyleSheet(u"QPushButton{color: #fff; background-color: #FF3636; border-radius: 20px;}\n"
"QPushButton:hover{background-color: 	hsl(0, 100%, 64%)}\n"
"QPushButton:focus{outline:0}")
        self.btn_sair_fisio.setIcon(icon6)
        self.btn_sair_fisio.setIconSize(QSize(24, 24))

        self.verticalLayout_36.addWidget(self.btn_sair_fisio)

        self.frame_217 = QFrame(self.frame_54)
        self.frame_217.setObjectName(u"frame_217")
        self.frame_217.setMinimumSize(QSize(0, 30))
        self.frame_217.setMaximumSize(QSize(16777215, 30))
        self.frame_217.setFrameShape(QFrame.StyledPanel)
        self.frame_217.setFrameShadow(QFrame.Raised)

        self.verticalLayout_36.addWidget(self.frame_217)


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
        self.horizontalLayout_22.setContentsMargins(0, 8, 8, 0)
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
        self.btn_alterar_foto_senha_nutri = QPushButton(self.frame_24)
        self.btn_alterar_foto_senha_nutri.setObjectName(u"btn_alterar_foto_senha_nutri")
        self.btn_alterar_foto_senha_nutri.setStyleSheet(u"QPushButton{background-color: #E33B4E; border: none}")
        self.btn_alterar_foto_senha_nutri.setIcon(icon1)
        self.btn_alterar_foto_senha_nutri.setIconSize(QSize(140, 180))

        self.verticalLayout_17.addWidget(self.btn_alterar_foto_senha_nutri)

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
        font19 = QFont()
        font19.setFamilies([u"Six Caps"])
        font19.setPointSize(20)
        self.btn_plano_alimentar_nutri.setFont(font19)
        self.btn_plano_alimentar_nutri.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_plano_alimentar_nutri.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon26 = QIcon()
        icon26.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/seguranca-alimentar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_plano_alimentar_nutri.setIcon(icon26)
        self.btn_plano_alimentar_nutri.setIconSize(QSize(30, 30))

        self.verticalLayout_37.addWidget(self.btn_plano_alimentar_nutri)

        self.btn_consulta_nutri = QPushButton(self.frame_56)
        self.btn_consulta_nutri.setObjectName(u"btn_consulta_nutri")
        self.btn_consulta_nutri.setMinimumSize(QSize(140, 45))
        self.btn_consulta_nutri.setFont(font6)
        self.btn_consulta_nutri.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_consulta_nutri.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_consulta_nutri.setIcon(icon3)
        self.btn_consulta_nutri.setIconSize(QSize(30, 30))

        self.verticalLayout_37.addWidget(self.btn_consulta_nutri)

        self.btn_relatorios_nutri = QPushButton(self.frame_56)
        self.btn_relatorios_nutri.setObjectName(u"btn_relatorios_nutri")
        self.btn_relatorios_nutri.setMinimumSize(QSize(140, 45))
        self.btn_relatorios_nutri.setFont(font6)
        self.btn_relatorios_nutri.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_relatorios_nutri.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_relatorios_nutri.setIcon(icon5)
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
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 20)
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
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 30)
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

        self.frame_218 = QFrame(self.frame_55)
        self.frame_218.setObjectName(u"frame_218")
        self.frame_218.setMinimumSize(QSize(0, 30))
        self.frame_218.setMaximumSize(QSize(16777215, 30))
        self.frame_218.setFrameShape(QFrame.StyledPanel)
        self.frame_218.setFrameShadow(QFrame.Raised)

        self.verticalLayout_18.addWidget(self.frame_218)


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
        self.horizontalLayout_19.setContentsMargins(0, 8, 8, 0)
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
        self.btn_plano_alimentar_cadastrar_nutri.setFont(font7)
        self.btn_plano_alimentar_cadastrar_nutri.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_plano_alimentar_cadastrar_nutri.setLayoutDirection(Qt.RightToLeft)
        self.btn_plano_alimentar_cadastrar_nutri.setStyleSheet(u"QPushButton{color: #EC848C; background-color: #FEE4E1; border-radius: 20px ;border: none}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_plano_alimentar_cadastrar_nutri.setIcon(icon2)
        self.btn_plano_alimentar_cadastrar_nutri.setIconSize(QSize(80, 80))

        self.verticalLayout_27.addWidget(self.btn_plano_alimentar_cadastrar_nutri)

        self.btn_plano_alimentar_buscar_nutri = QPushButton(self.frame_42)
        self.btn_plano_alimentar_buscar_nutri.setObjectName(u"btn_plano_alimentar_buscar_nutri")
        self.btn_plano_alimentar_buscar_nutri.setMinimumSize(QSize(700, 154))
        self.btn_plano_alimentar_buscar_nutri.setMaximumSize(QSize(700, 154))
        self.btn_plano_alimentar_buscar_nutri.setFont(font7)
        self.btn_plano_alimentar_buscar_nutri.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_plano_alimentar_buscar_nutri.setLayoutDirection(Qt.RightToLeft)
        self.btn_plano_alimentar_buscar_nutri.setStyleSheet(u"QPushButton{color: #EC848C; background-color: #FEE4E1; border-radius: 20px ;border: none}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_plano_alimentar_buscar_nutri.setIcon(icon5)
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
        self.btn_alterar_foto_senha_psi = QPushButton(self.frame_33)
        self.btn_alterar_foto_senha_psi.setObjectName(u"btn_alterar_foto_senha_psi")
        self.btn_alterar_foto_senha_psi.setStyleSheet(u"QPushButton{background-color: #E33B4E; border: none}")
        self.btn_alterar_foto_senha_psi.setIcon(icon1)
        self.btn_alterar_foto_senha_psi.setIconSize(QSize(140, 180))

        self.verticalLayout_24.addWidget(self.btn_alterar_foto_senha_psi)

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
        self.frame_59.setFont(font19)
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
        self.btn_consulta_psi.setFont(font6)
        self.btn_consulta_psi.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_consulta_psi.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_consulta_psi.setIcon(icon3)
        self.btn_consulta_psi.setIconSize(QSize(30, 30))

        self.verticalLayout_39.addWidget(self.btn_consulta_psi)

        self.btn_relatorios_psi = QPushButton(self.frame_59)
        self.btn_relatorios_psi.setObjectName(u"btn_relatorios_psi")
        self.btn_relatorios_psi.setMinimumSize(QSize(140, 45))
        self.btn_relatorios_psi.setFont(font6)
        self.btn_relatorios_psi.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_relatorios_psi.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_relatorios_psi.setIcon(icon5)
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
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 20)
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
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 30)
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

        self.frame_219 = QFrame(self.frame_57)
        self.frame_219.setObjectName(u"frame_219")
        self.frame_219.setMinimumSize(QSize(0, 30))
        self.frame_219.setMaximumSize(QSize(16777215, 30))
        self.frame_219.setFrameShape(QFrame.StyledPanel)
        self.frame_219.setFrameShadow(QFrame.Raised)

        self.verticalLayout_38.addWidget(self.frame_219)


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
        self.horizontalLayout_24.setContentsMargins(0, 8, 8, 0)
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
        self.btn_alterar_foto_senha_secret = QPushButton(self.frame_15)
        self.btn_alterar_foto_senha_secret.setObjectName(u"btn_alterar_foto_senha_secret")
        self.btn_alterar_foto_senha_secret.setStyleSheet(u"QPushButton{background-color: #E33B4E; border: none}")
        self.btn_alterar_foto_senha_secret.setIcon(icon1)
        self.btn_alterar_foto_senha_secret.setIconSize(QSize(140, 180))

        self.verticalLayout_10.addWidget(self.btn_alterar_foto_senha_secret)

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
        self.btn_agenda_sec.setFont(font6)
        self.btn_agenda_sec.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agenda_sec.setLayoutDirection(Qt.LeftToRight)
        self.btn_agenda_sec.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_agenda_sec.setIcon(icon4)
        self.btn_agenda_sec.setIconSize(QSize(30, 30))

        self.verticalLayout_12.addWidget(self.btn_agenda_sec)

        self.btn_eventos_sec = QPushButton(self.frame_50)
        self.btn_eventos_sec.setObjectName(u"btn_eventos_sec")
        self.btn_eventos_sec.setMinimumSize(QSize(140, 45))
        self.btn_eventos_sec.setFont(font6)
        self.btn_eventos_sec.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_eventos_sec.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        icon27 = QIcon()
        icon27.addFile(u"./OneDrive - Servi\u00e7o Nacional de Aprendizagem Comercial/Fabrica-SW-96 2023/Fabrica-SW-96/icons/festa-de-aniversario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_eventos_sec.setIcon(icon27)
        self.btn_eventos_sec.setIconSize(QSize(30, 30))

        self.verticalLayout_12.addWidget(self.btn_eventos_sec)

        self.btn_relatorios_sec = QPushButton(self.frame_50)
        self.btn_relatorios_sec.setObjectName(u"btn_relatorios_sec")
        self.btn_relatorios_sec.setMinimumSize(QSize(140, 45))
        self.btn_relatorios_sec.setFont(font6)
        self.btn_relatorios_sec.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_relatorios_sec.setStyleSheet(u"QPushButton{background-color: #F9D9DD; color: #EC848C; border-radius: 15px}\n"
"QPushButton:hover{background-color: hsl(6, 94%, 92%)}\n"
"QPushButton:focus{outline: 0}")
        self.btn_relatorios_sec.setIcon(icon5)
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
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 20)
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
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 30)
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

        self.frame_220 = QFrame(self.frame_12)
        self.frame_220.setObjectName(u"frame_220")
        self.frame_220.setMinimumSize(QSize(0, 30))
        self.frame_220.setMaximumSize(QSize(16777215, 30))
        self.frame_220.setFrameShape(QFrame.StyledPanel)
        self.frame_220.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_220)


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
        self.horizontalLayout_14.setContentsMargins(0, 8, 8, 0)
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

        self.gridLayout_5.addWidget(self.inicio, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label_situacao_trabalho_usuario_as.setBuddy(self.input_situacao_trabalho_outros_usuario_as)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        self.inicio.setCurrentIndex(0)
        self.tipos_acesso.setCurrentIndex(0)
        self.stack_assistente.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_8.setCurrentIndex(0)
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
        self.label_Logo_ABREC.setText("")
        self.input_usuario_login.setText("")
        self.input_usuario_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.label_2.setText("")
        self.input_senha_login.setText("")
        self.input_senha_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.toolButton.setText("")
        self.btn_entrar_login.setText(QCoreApplication.translate("MainWindow", u"ENTRAR", None))
        self.btn_esqueci_senha_login.setText(QCoreApplication.translate("MainWindow", u"Esqueci Senha", None))
        self.label_Abrec_Logo_Paint.setText("")
        self.btn_alterar_foto_senha_as.setText("")
        self.label_ola_nome_as.setText(QCoreApplication.translate("MainWindow", u"Ol\u00e1, _ _ _ _ _ _", None))
        self.btn_cadastrar_as.setText(QCoreApplication.translate("MainWindow", u"  CADASTRAR", None))
        self.btn_consulta_as.setText(QCoreApplication.translate("MainWindow", u"   CONSULTA", None))
        self.btn_agenda_as.setText(QCoreApplication.translate("MainWindow", u"      AGENDA", None))
        self.btn_relatorios_as.setText(QCoreApplication.translate("MainWindow", u" RELAT\u00d3RIOS", None))
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
        self.input_sexo_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_sexo_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.input_sexo_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Feminino", None))

        self.label_telefone_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.label_email_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_cep_usuario_as.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.input_cep_usuario_as.setInputMask(QCoreApplication.translate("MainWindow", u"00.000-000", None))
        self.input_cep_usuario_as.setText(QCoreApplication.translate("MainWindow", u".-", None))
        self.btn_cep_buscar_usuario_as.setText("")
        self.label_logradouro_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.label_numero_usuario_as.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.label_bairro_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.label_cidade_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_estado_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.label_estado_civil_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Estado civil", None))
        self.input_estado_civil_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_estado_civil_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Solteiro", None))
        self.input_estado_civil_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Casado", None))
        self.input_estado_civil_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Divorciado", None))
        self.input_estado_civil_usuario_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Vi\u00favo", None))
        self.input_estado_civil_usuario_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Separado", None))

        self.label_escolaridade_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Escolaridade", None))
        self.input_escolaridade_usuario_comboBox_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_escolaridade_usuario_comboBox_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Fundamental", None))
        self.input_escolaridade_usuario_comboBox_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Fundamental incompleto", None))
        self.input_escolaridade_usuario_comboBox_as.setItemText(3, QCoreApplication.translate("MainWindow", u"M\u00e9dio", None))
        self.input_escolaridade_usuario_comboBox_as.setItemText(4, QCoreApplication.translate("MainWindow", u"M\u00e9dio incompleto", None))
        self.input_escolaridade_usuario_comboBox_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Superior completo", None))
        self.input_escolaridade_usuario_comboBox_as.setItemText(6, QCoreApplication.translate("MainWindow", u"Superior incompleto", None))

        self.label_pessoa_cdeficiencia_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Pessoa c/ defici\u00eancia", None))
        self.input_pessoa_cdeficiencia_sim_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.label_pessoa_cdeficiencia_nao_usuario_as.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_tipo_deficiencia_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Tipo de defici\u00eancia", None))
        self.input_tipo_deficiencia_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_tipo_deficiencia_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Visual", None))
        self.input_tipo_deficiencia_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Motora", None))
        self.input_tipo_deficiencia_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Amputada", None))
        self.input_tipo_deficiencia_usuario_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Mental", None))
        self.input_tipo_deficiencia_usuario_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Outra", None))

        self.label_renda_familiar_usuario_as.setText(QCoreApplication.translate("MainWindow", u"M\u00e9dia de renda familiar", None))
        self.input_renda_familiar_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_renda_familiar_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Menos 1 sal\u00e1rio", None))
        self.input_renda_familiar_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"1 sal\u00e1rio", None))
        self.input_renda_familiar_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Mais de 1 a 3 sal\u00e1rios", None))
        self.input_renda_familiar_usuario_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Mais que 3 sal\u00e1rios", None))

        self.label_meio_transporte_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Meio de transporte", None))
        self.input_meio_transporte_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_meio_transporte_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Particular", None))
        self.input_meio_transporte_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Carona", None))
        self.input_meio_transporte_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"\u00d4nibus coletivo", None))
        self.input_meio_transporte_usuario_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Ambul\u00e2ncia municipal", None))
        self.input_meio_transporte_usuario_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Moto", None))
        self.input_meio_transporte_usuario_as.setItemText(6, QCoreApplication.translate("MainWindow", u"Ambul\u00e2ncia particular", None))
        self.input_meio_transporte_usuario_as.setItemText(7, QCoreApplication.translate("MainWindow", u"Outro", None))

        self.label_vale_transporte_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Vale transporte", None))
        self.input_vale_transporte_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_vale_transporte_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Passe para os dias de tratamento", None))
        self.input_vale_transporte_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Passe do idoso", None))
        self.input_vale_transporte_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Passe livre", None))

        self.label_situacao_trabalho_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Situa\u00e7\u00e3o de trabalho", None))
        self.input_situacao_trabalho_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_situacao_trabalho_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Aposentado por Idade", None))
        self.input_situacao_trabalho_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Aposentado tempo de servi\u00e7o", None))
        self.input_situacao_trabalho_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Aposentado invalidez", None))
        self.input_situacao_trabalho_usuario_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Empregado/a Aut\u00f4nomo/a", None))
        self.input_situacao_trabalho_usuario_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Aposentado/a", None))
        self.input_situacao_trabalho_usuario_as.setItemText(6, QCoreApplication.translate("MainWindow", u"Pensionista", None))
        self.input_situacao_trabalho_usuario_as.setItemText(7, QCoreApplication.translate("MainWindow", u"Desempregado/a", None))
        self.input_situacao_trabalho_usuario_as.setItemText(8, QCoreApplication.translate("MainWindow", u"Aux\u00edlio doen\u00e7a", None))
        self.input_situacao_trabalho_usuario_as.setItemText(9, QCoreApplication.translate("MainWindow", u"Outros", None))

        self.label_beneficios_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Benef\u00edcios", None))
        self.input_beneficios_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_beneficios_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"BPC/Idoso", None))
        self.input_beneficios_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"BPC/PCD", None))
        self.input_beneficios_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Mais Social (Gov. Estadual)", None))
        self.input_beneficios_usuario_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Aux\u00edlio Brasil (Gov. Federal)", None))

        self.label_tarifa_social_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Tarifa social", None))
        self.input_tarifa_social_sim_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.input_tarifa_social_nao_usuario_as.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_tipo_tratamento_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Tipo de tratamento", None))
        self.input_tipo_tratamento_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_tipo_tratamento_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Pr\u00e9-Di\u00e1lise", None))
        self.input_tipo_tratamento_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Hemodi\u00e1lise", None))
        self.input_tipo_tratamento_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Di\u00e1lise Peritoneal", None))

        self.label_local_tratamento_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Local de tratamento", None))
        self.label_patologia_base_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Patologia base", None))
        self.input_patologia_base_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_patologia_base_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Hipertens\u00e3o", None))
        self.input_patologia_base_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Diabete 1", None))
        self.input_patologia_base_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Diabete 2", None))
        self.input_patologia_base_usuario_as.setItemText(4, QCoreApplication.translate("MainWindow", u"L\u00fapus", None))
        self.input_patologia_base_usuario_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Nefrites", None))
        self.input_patologia_base_usuario_as.setItemText(6, QCoreApplication.translate("MainWindow", u"Outros", None))

        self.label_data_inicio_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Data de in\u00edcio", None))
        self.label_periodo_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo", None))
        self.input_periodo_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_periodo_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Matutino", None))
        self.input_periodo_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Vespertino", None))
        self.input_periodo_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Noturno", None))

        self.btn_voltar_usuario_as.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_observacoes_sigilo_as.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es em sigilo", None))
        self.btn_salvar_usuario_as.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
        self.btn_proximo_as.setText(QCoreApplication.translate("MainWindow", u"PR\u00d3XIMO", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DO CUIDADOR", None))
        self.label_matricula_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Matricula", None))
        self.label_nome_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Nome cuidador", None))
        self.input_nome_cuidador_as.setText("")
        self.label_data_nascimento_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Data de nascimento", None))
        self.label_cpf_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.input_cpf_cuidador_as.setText("")
        self.label_rg_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.input_rg_cuidador_as.setText("")
        self.label_data_emissao_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Data de emiss\u00e3o", None))
        self.label_orgao_expedidor_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"\u00d3rg\u00e3o expedidor", None))
        self.label_sexo_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.input_sexo_cuidador_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_sexo_cuidador_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.input_sexo_cuidador_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Feminino", None))

        self.label_usuario_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.input_usuario_cuidador_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_usuario_cuidador_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.input_usuario_cuidador_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Feminino", None))

        self.label_parentesco_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Parentesco", None))
        self.label_telefone_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.label_email_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_cep_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.input_cep_cuidador_as.setInputMask(QCoreApplication.translate("MainWindow", u"00.000-000", None))
        self.input_cep_cuidador_as.setText(QCoreApplication.translate("MainWindow", u".-", None))
        self.btn_cep_buscar_cuidador_as.setText("")
        self.label_logradouro_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.label_numero_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.label_bairro_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.label_cidade_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_estado_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.label_observacoes_gerais_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es gerais Usu\u00e1rio e Cuidador", None))
        self.btn_voltar_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_finalizar_as.setText(QCoreApplication.translate("MainWindow", u"FINALIZAR", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"OBSERVA\u00c7\u00d5ES SIGILOSAS", None))
        self.label_obito_paciente_as.setText(QCoreApplication.translate("MainWindow", u"\u00d3bito do paciente", None))
        self.input_obito_paciente_sim_as.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.input_obito_paciente_nao_as.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_observacoes_obs_sigilosas_as.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es/informa\u00e7\u00f5es gerais", None))
        self.label_tabela_de_observacoes_obs_sigilosas_as.setText(QCoreApplication.translate("MainWindow", u"Tabela de Observa\u00e7\u00f5es", None))
        ___qtablewidgetitem = self.input_TableWidget_observacoes_sigilosas_as.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem1 = self.input_TableWidget_observacoes_sigilosas_as.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00e3o", None));
        ___qtablewidgetitem2 = self.input_TableWidget_observacoes_sigilosas_as.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem3 = self.input_TableWidget_observacoes_sigilosas_as.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem4 = self.input_TableWidget_observacoes_sigilosas_as.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem5 = self.input_TableWidget_observacoes_sigilosas_as.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem6 = self.input_TableWidget_observacoes_sigilosas_as.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem7 = self.input_TableWidget_observacoes_sigilosas_as.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem8 = self.input_TableWidget_observacoes_sigilosas_as.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem9 = self.input_TableWidget_observacoes_sigilosas_as.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem10 = self.input_TableWidget_observacoes_sigilosas_as.verticalHeaderItem(8)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem11 = self.input_TableWidget_observacoes_sigilosas_as.verticalHeaderItem(9)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem12 = self.input_TableWidget_observacoes_sigilosas_as.verticalHeaderItem(10)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem13 = self.input_TableWidget_observacoes_sigilosas_as.verticalHeaderItem(11)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem14 = self.input_TableWidget_observacoes_sigilosas_as.verticalHeaderItem(12)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem15 = self.input_TableWidget_observacoes_sigilosas_as.verticalHeaderItem(13)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"14", None));

        __sortingEnabled = self.input_TableWidget_observacoes_sigilosas_as.isSortingEnabled()
        self.input_TableWidget_observacoes_sigilosas_as.setSortingEnabled(False)
        self.input_TableWidget_observacoes_sigilosas_as.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.input_TableWidget_observacoes_sigilosas_as.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_voltar_observacoes_sigilosas_as.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_alterar_observacoes_sigilosas_as.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_cancelar_observacoes_sigilosas_as.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.btn_salvar_observacoes_sigilosas_as.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_excluir_observacoes_sigilosas_as.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.label_cadastro_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DO COLABORADOR", None))
        self.label_situacao_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Situa\u00e7\u00e3o", None))
        self.input_situacao_ativo_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Ativo", None))
        self.input_situacao_inativo_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Inativo", None))
        self.label_matricula_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Matricula", None))
        self.label_nome_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Nome colaborador", None))
        self.input_nome_colaborador_as.setText("")
        self.label_data_nascimento_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Data de nascimento", None))
        self.label_cpf_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.input_cpf_colaborador_as.setText("")
        self.label_rg_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.input_rg_colaborador_as.setText("")
        self.label_cep_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.input_cep_colaborador_as.setInputMask(QCoreApplication.translate("MainWindow", u"00.000-000", None))
        self.input_cep_colaborador_as.setText(QCoreApplication.translate("MainWindow", u".-", None))
        self.btn_cep_buscar_colaborador_as.setText("")
        self.label_logradouro_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.label_numero_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.label_bairro_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.label_cidade_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_estado_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.input_estado_colaborador_as.setText("")
        self.label_orgao_expedidor_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"\u00d3rg\u00e3o expedidor", None))
        self.label_data_emissao_rg_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Data de emiss\u00e3o", None))
        self.label_pis_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"PIS", None))
        self.label_sexo_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.input_sexo_colaborador_comboBox_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_sexo_colaborador_comboBox_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.input_sexo_colaborador_comboBox_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Feminino", None))

        self.label_telefone_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.label_email_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_usuario_colaborador_as_2.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.label_senha_colaborador_as_2.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_confirmar_senha_colaborador_as_2.setText(QCoreApplication.translate("MainWindow", u"Confirmar Senha", None))
        self.label_estado_civil_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Estado civil", None))
        self.input_estado_civil_colaborador_comboBox_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_estado_civil_colaborador_comboBox_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Solteiro", None))
        self.input_estado_civil_colaborador_comboBox_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Casado", None))
        self.input_estado_civil_colaborador_comboBox_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Divorciado", None))
        self.input_estado_civil_colaborador_comboBox_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Vi\u00favo", None))
        self.input_estado_civil_colaborador_comboBox_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Separado", None))

        self.label_salario_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Sal\u00e1rio", None))
        self.input_salario_colaborador_as.setText("")
        self.label_Data_de_admissao_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Data de admiss\u00e3o", None))
        self.label_escolaridade_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Escolaridade", None))
        self.input_escolaridade_colaborador_comboBox_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_escolaridade_colaborador_comboBox_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Fundamental", None))
        self.input_escolaridade_colaborador_comboBox_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Fundamental incompleto", None))
        self.input_escolaridade_colaborador_comboBox_as.setItemText(3, QCoreApplication.translate("MainWindow", u"M\u00e9dio", None))
        self.input_escolaridade_colaborador_comboBox_as.setItemText(4, QCoreApplication.translate("MainWindow", u"M\u00e9dio incompleto", None))
        self.input_escolaridade_colaborador_comboBox_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Superior completo", None))
        self.input_escolaridade_colaborador_comboBox_as.setItemText(6, QCoreApplication.translate("MainWindow", u"Superior incompleto", None))

        self.label_cargo_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Cargo", None))
        self.input_cargo_colaborador_comboBox_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_cargo_colaborador_comboBox_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Recepcionista", None))
        self.input_cargo_colaborador_comboBox_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Assistente Social", None))
        self.input_cargo_colaborador_comboBox_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Farmac\u00eautico (a)", None))
        self.input_cargo_colaborador_comboBox_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Psic\u00f3logo (a)", None))
        self.input_cargo_colaborador_comboBox_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Fisioterapeuta", None))
        self.input_cargo_colaborador_comboBox_as.setItemText(6, QCoreApplication.translate("MainWindow", u"Nutricionista", None))
        self.input_cargo_colaborador_comboBox_as.setItemText(7, "")

        self.label_periodo_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo", None))
        self.input_periodo_colaborador_comboBox_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_periodo_colaborador_comboBox_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Matutino", None))
        self.input_periodo_colaborador_comboBox_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Vespertino", None))
        self.input_periodo_colaborador_comboBox_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Noturno", None))
        self.input_periodo_colaborador_comboBox_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Integral", None))

        self.input_foto_colaborador_as.setText("")
        self.btn_voltar_cadastro_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_concluir_cadastro_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"CONCLUIR", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DE CURSOS E OFICINAS", None))
        self.label_data_inclusao_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Data de inclus\u00e3o", None))
        self.label_nome_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_tipo_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.input_tipo_cursos_as.setItemText(0, "")
        self.input_tipo_cursos_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Interno", None))
        self.input_tipo_cursos_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Externo", None))

        self.label_situacao_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Situa\u00e7\u00e3o", None))
        self.input_ativo_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Ativo", None))
        self.input_inativo_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Inativo", None))
        self.label_responsavel_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Respons\u00e1vel", None))
        self.label_data_inicio_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Data de in\u00edcio", None))
        self.label_data_termino_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Data de t\u00e9rmino", None))
        self.label_dias_aulas_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Dias das aulas", None))
        self.input_segunda_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Segunda-Feira", None))
        self.input_terca_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Ter\u00e7a-Feira", None))
        self.input_quarta_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Quarta-Feira", None))
        self.input_quinta_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Quinta-Feira", None))
        self.input_sexta_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Sexta-Feira", None))
        self.input_sabado_cursos_as.setText(QCoreApplication.translate("MainWindow", u"S\u00e1bado", None))
        self.label_horario_inicio_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Hor\u00e1rio In\u00edcio", None))
        self.label_horario_termino_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Hor\u00e1rio T\u00e9rmino", None))
        self.label_periodo_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo", None))
        self.input_periodo_cursos_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_periodo_cursos_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Matutino", None))
        self.input_periodo_cursos_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Vespertino", None))
        self.input_periodo_cursos_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Noturno", None))

        self.label_vagas_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Vagas", None))
        self.btn_voltar_cursos_as.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_lista_pessoas_cursos_as.setText(QCoreApplication.translate("MainWindow", u"Lista pessoas cadastradas", None))
        self.btn_concluir_cursos_as.setText(QCoreApplication.translate("MainWindow", u"CONCLUIR", None))
        self.label_consulta_consulta_as.setText(QCoreApplication.translate("MainWindow", u"CONSULTA", None))
        self.label_buscar_consulta_as.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.input_nome_radio_consulta_as.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.input_cpf_radio_consulta_as.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.input_matricula_radio_consulta_as.setText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula", None))
        self.label_matricula_consulta_as.setText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula", None))
        self.label_nome_consulta_as.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_cpf_consulta_as.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.label_nascimento_consulta_as.setText(QCoreApplication.translate("MainWindow", u"Data de nascimento", None))
        self.label_cidade_consulta_as.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_estado_consulta_as.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.btn_buscar_consulta_as.setText("")
        self.label_matricula_consulta_as_2.setText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula", None))
        self.input_matricula_consulta_as_2.setText("")
        self.label_nome_usuario_consulta_as.setText(QCoreApplication.translate("MainWindow", u"Nome do usu\u00e1rio", None))
        self.input_nome_usuario_consulta_as.setText("")
        self.label_cpf_consulta_as_2.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.input_cpf_consulta_as_2.setText("")
        self.label_ultima_consulta_consulta_as.setText(QCoreApplication.translate("MainWindow", u"Data da \u00faltima consulta", None))
        self.input_ultima_consulta_consulta_as.setText("")
        self.btn_imprimir_consulta_as.setText(QCoreApplication.translate("MainWindow", u"  IMPRIMIR", None))
        self.btn_alterar_consulta_as.setText(QCoreApplication.translate("MainWindow", u"  ALTERAR", None))
        self.btn_concluir_consulta_as.setText(QCoreApplication.translate("MainWindow", u"CONCLUIR", None))
        self.btn_voltar_consulta_as.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.label_inicio_periodo_relatorio_as.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_final_periodo_relatorio_as.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo", None))
        self.label_escolha_relatorio_as.setText(QCoreApplication.translate("MainWindow", u"Escolha", None))
        self.input_escolha_relatorio_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Escolha", None))
        self.input_escolha_relatorio_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.input_escolha_relatorio_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Faixa et\u00e1ria", None))
        self.input_escolha_relatorio_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.input_escolha_relatorio_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Bairros", None))
        self.input_escolha_relatorio_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.input_escolha_relatorio_as.setItemText(6, QCoreApplication.translate("MainWindow", u"BPC", None))
        self.input_escolha_relatorio_as.setItemText(7, QCoreApplication.translate("MainWindow", u"Aposentado", None))

        self.label_idade_relatorio_as.setText("")
        self.input_idade_inicial_relatorio_as.setText("")
        self.label_a_relatorio_as.setText("")
        self.input_idade_final_relatorio_as.setText("")
        self.btn_buscar_relatorio_as.setText("")
        self.input_buscar_dados_relatorio_as.setText("")
        self.input_buscar_dados_relatorio_as.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome /Cidade/ Bairro/Consulta", None))
        ___qtablewidgetitem16 = self.tableWidget_relatorio_as.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem17 = self.tableWidget_relatorio_as.verticalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.btn_gerar_excel_relatorio_as.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_gerar_pdf_relatorio_as.setText(QCoreApplication.translate("MainWindow", u"Gerar PDF", None))
        self.btn_imprimir_relatorio_as.setText(QCoreApplication.translate("MainWindow", u"  IMPRIMIR", None))
        self.btn_excluir_relatorio_as.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_voltar_relatorios_as.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.label_relatorio_as.setText(QCoreApplication.translate("MainWindow", u"Rel\u00e1torios", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"AGENDA", None))
        self.label_cpf_agendamento_as.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.input_cpf_agendamento_as.setText("")
        self.input_cpf_agendamento_as.setPlaceholderText("")
        self.btn_buscar_agendamento_as.setText("")
        self.label_nome_agendamento_as.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.input_nome_agendamento_as.setText("")
        self.label_telefone_agendamento_as.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.label_profissional_agendamento_as.setText(QCoreApplication.translate("MainWindow", u"Profissional", None))
        self.input_profissional_as_agendamento_as.setText(QCoreApplication.translate("MainWindow", u"Assistente Social", None))
        self.input_profissional_nutri_agendamento_as.setText(QCoreApplication.translate("MainWindow", u"Nutricionista", None))
        self.input_profissional_psi_agendamento_as.setText(QCoreApplication.translate("MainWindow", u"Psic\u00f3loga", None))
        self.label_data_agendamento_as.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_hora_agendamento_as.setText(QCoreApplication.translate("MainWindow", u"Hora", None))
        self.label_clinica_agendamento_as.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.label_filtro_agendamento_as.setText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        ___qtablewidgetitem18 = self.input_TableWidget_agendamento_as.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem19 = self.input_TableWidget_agendamento_as.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Agendamento", None));
        ___qtablewidgetitem20 = self.input_TableWidget_agendamento_as.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Profissional", None));
        ___qtablewidgetitem21 = self.input_TableWidget_agendamento_as.verticalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem22 = self.input_TableWidget_agendamento_as.verticalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem23 = self.input_TableWidget_agendamento_as.verticalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem24 = self.input_TableWidget_agendamento_as.verticalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem25 = self.input_TableWidget_agendamento_as.verticalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem26 = self.input_TableWidget_agendamento_as.verticalHeaderItem(5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem27 = self.input_TableWidget_agendamento_as.verticalHeaderItem(6)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem28 = self.input_TableWidget_agendamento_as.verticalHeaderItem(7)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem29 = self.input_TableWidget_agendamento_as.verticalHeaderItem(8)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem30 = self.input_TableWidget_agendamento_as.verticalHeaderItem(9)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem31 = self.input_TableWidget_agendamento_as.verticalHeaderItem(10)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem32 = self.input_TableWidget_agendamento_as.verticalHeaderItem(11)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem33 = self.input_TableWidget_agendamento_as.verticalHeaderItem(12)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem34 = self.input_TableWidget_agendamento_as.verticalHeaderItem(13)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"14", None));

        __sortingEnabled1 = self.input_TableWidget_agendamento_as.isSortingEnabled()
        self.input_TableWidget_agendamento_as.setSortingEnabled(False)
        self.input_TableWidget_agendamento_as.setSortingEnabled(__sortingEnabled1)

#if QT_CONFIG(tooltip)
        self.input_TableWidget_agendamento_as.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_voltar_agenda_as.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_alterar_agenda_as.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_cancelar_agenda_as.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.btn_concluir_agenda_as.setText(QCoreApplication.translate("MainWindow", u"CONCLUIR", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"CADASTRO CL\u00cdNICA", None))
        self.label_codigo_cadastro_clinica_as.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None))
        self.label_cnpj_cadastro_clinica_as.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.input_cnpj_cadastro_clinica_as.setText("")
        self.label_razao_social_cadastro_clinica_as.setText(QCoreApplication.translate("MainWindow", u"Raz\u00e3o Social", None))
        self.input_razao_social_cadastro_clinica_as.setText("")
        self.label_nome_fantasia_cadastro_clinica_as.setText(QCoreApplication.translate("MainWindow", u"Nome Fantasia", None))
        self.input_nome_fantasia_cadastro_clinica_as.setText("")
        self.label_telefone_clinica_as.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.label_email_clinica_as.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_cep_clinica_as.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.input_cep_clinica_as.setInputMask(QCoreApplication.translate("MainWindow", u"00.000-000", None))
        self.input_cep_clinica_as.setText(QCoreApplication.translate("MainWindow", u".-", None))
        self.btn_cep_buscar_colaborador_as_3.setText("")
        self.label_logradouro_clinica_as.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.label_numero_clinica_as.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.label_bairro_clinica_as.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.label_cidade_clinica_as.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_estado_clinica__as.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.label_informacoes_gerais_clinica_as.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es Gerais", None))
        self.btn_voltar_as.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_finalizar_as_2.setText(QCoreApplication.translate("MainWindow", u"CONCLUIR", None))
        self.label_altercao_de_dados.setText(QCoreApplication.translate("MainWindow", u"ALTERA\u00c7\u00c3O DE DADOS CADASTRADOS", None))
        self.label_tipo_alterar_cadastros_as.setText(QCoreApplication.translate("MainWindow", u"Tipo de Cadastro", None))
        self.comboBox_tipos_alterar_cadastros_as.setItemText(0, "")
        self.comboBox_tipos_alterar_cadastros_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Cuidador", None))
        self.comboBox_tipos_alterar_cadastros_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.comboBox_tipos_alterar_cadastros_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Colaborador", None))

        self.label_alterar_cpf_cnpj_as.setText(QCoreApplication.translate("MainWindow", u"CPF/CNPJ", None))
        self.lineEdit_alterar_buscar_cpf_cnpj_as.setText("")
        self.btn_buscar_alterar_as.setText("")
        self.label_alterar_matricula_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Matricula", None))
        self.label_alterar_nome_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Nome cuidador", None))
        self.input_alterar_nome_cuidador_as.setText("")
        self.label_alterar_cpf_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.input_alterar_cpf_cuidador_as.setText("")
        self.label_alterar_rg_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.input_alterar_rg_cuidador_as.setText("")
        self.label_alterar_data_emissao_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Data de emiss\u00e3o", None))
        self.label_alterar_orgao_expedidor_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"\u00d3rg\u00e3o expedidor", None))
        self.label_alterar_sexo_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.input_alterar_sexo_cuidador_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_alterar_sexo_cuidador_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.input_alterar_sexo_cuidador_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Feminino", None))

        self.label_alterar_parentesco_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Parentesco", None))
        self.label_alterar_telefone_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.label_alterar_email_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_alterar_cep_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.input_alterar_cep_cuidador_as.setInputMask(QCoreApplication.translate("MainWindow", u"00.000-000", None))
        self.input_alterar_cep_cuidador_as.setText(QCoreApplication.translate("MainWindow", u".-", None))
        self.btn_alterar_cep_buscar_cuidador_as.setText("")
        self.label_alterar_logradouro_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.label_alterar_numero_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.label_alterar_bairro_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.label_alterar_cidade_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_alterar_estado_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.label_alterar_observacoes_gerais_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es gerais Usu\u00e1rio e Cuidador", None))
        self.btn_alterar_voltar_cuidador_as.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_alterar_salvar_as.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
        self.btn_alterar_foto_usuario_as.setText("")
        self.label_alterar_matricula_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula", None))
        self.label_alterar_nome_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Nome do usu\u00e1rio", None))
        self.label_alterar_nascimento_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Data de nascimento", None))
        self.label_alterar_situacao_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Situa\u00e7\u00e3o", None))
        self.input_alterar_situacao_ativo_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Ativo", None))
        self.input_alterar_situacao_inativo_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Inativo", None))
        self.label_alterar_cpf_usuario_as.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.label_alterar_rg_usuario_as.setText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.label_alterar_data_emissao_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Data de emiss\u00e3o", None))
        self.label_alterar_orgao_expedidor_usuario_as.setText(QCoreApplication.translate("MainWindow", u"\u00d3rg\u00e3o expedidor", None))
        self.label_alterar_nis_usuario_as.setText(QCoreApplication.translate("MainWindow", u"NIS", None))
        self.label_alterar_cns_usuario_as.setText(QCoreApplication.translate("MainWindow", u"CNS", None))
        self.label_alterar_sexo_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.input_alterar_sexo_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_alterar_sexo_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.input_alterar_sexo_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Feminino", None))

        self.label_alterar_telefone_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.label_alterar_email_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_alterar_cep_usuario_as.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.input_alterar_cep_usuario_as.setInputMask(QCoreApplication.translate("MainWindow", u"00.000-000", None))
        self.input_alterar_cep_usuario_as.setText(QCoreApplication.translate("MainWindow", u".-", None))
        self.btn_alterar_cep_buscar_usuario_as.setText("")
        self.label_alterar_logradouro_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.label_alterar_numero_usuario_as.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.label_alterar_bairro_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.label_alterar_cidade_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_alterar_estado_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.label_alterar_estado_civil_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Estado civil", None))
        self.input_alterar_estado_civil_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_alterar_estado_civil_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Solteiro", None))
        self.input_alterar_estado_civil_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Casado", None))
        self.input_alterar_estado_civil_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Divorciado", None))
        self.input_alterar_estado_civil_usuario_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Vi\u00favo", None))
        self.input_alterar_estado_civil_usuario_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Separado", None))

        self.label_alterar_escolaridade_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Escolaridade", None))
        self.input_alterar_escolaridade_usuario_comboBox_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_alterar_escolaridade_usuario_comboBox_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Fundamental", None))
        self.input_alterar_escolaridade_usuario_comboBox_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Fundamental incompleto", None))
        self.input_alterar_escolaridade_usuario_comboBox_as.setItemText(3, QCoreApplication.translate("MainWindow", u"M\u00e9dio", None))
        self.input_alterar_escolaridade_usuario_comboBox_as.setItemText(4, QCoreApplication.translate("MainWindow", u"M\u00e9dio incompleto", None))
        self.input_alterar_escolaridade_usuario_comboBox_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Superior completo", None))
        self.input_alterar_escolaridade_usuario_comboBox_as.setItemText(6, QCoreApplication.translate("MainWindow", u"Superior incompleto", None))

        self.label_alterar_pessoa_cdeficiencia_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Pessoa c/ defici\u00eancia", None))
        self.input_alterar_pessoa_cdeficiencia_sim_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.label_alterar_pessoa_cdeficiencia_nao_usuario_as.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_alterar_tipo_deficiencia_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Tipo de defici\u00eancia", None))
        self.input_alterar_tipo_deficiencia_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_alterar_tipo_deficiencia_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Visual", None))
        self.input_alterar_tipo_deficiencia_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Motora", None))
        self.input_alterar_tipo_deficiencia_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Amputada", None))
        self.input_alterar_tipo_deficiencia_usuario_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Mental", None))
        self.input_alterar_tipo_deficiencia_usuario_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Outra", None))

        self.label_alterar_renda_familiar_usuario_as.setText(QCoreApplication.translate("MainWindow", u"M\u00e9dia de renda familiar", None))
        self.input_alterar_renda_familiar_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_alterar_renda_familiar_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Menos 1 sal\u00e1rio", None))
        self.input_alterar_renda_familiar_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"1 sal\u00e1rio", None))
        self.input_alterar_renda_familiar_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Mais de 1 a 3 sal\u00e1rios", None))
        self.input_alterar_renda_familiar_usuario_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Mais que 3 sal\u00e1rios", None))

        self.label_alterar_meio_transporte_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Meio de transporte", None))
        self.input_alterar_meio_transporte_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_alterar_meio_transporte_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Particular", None))
        self.input_alterar_meio_transporte_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Carona", None))
        self.input_alterar_meio_transporte_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"\u00d4nibus coletivo", None))
        self.input_alterar_meio_transporte_usuario_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Ambul\u00e2ncia municipal", None))
        self.input_alterar_meio_transporte_usuario_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Moto", None))
        self.input_alterar_meio_transporte_usuario_as.setItemText(6, QCoreApplication.translate("MainWindow", u"Ambul\u00e2ncia particular", None))
        self.input_alterar_meio_transporte_usuario_as.setItemText(7, QCoreApplication.translate("MainWindow", u"Outro", None))

        self.label_alterar_vale_transporte_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Vale transporte", None))
        self.input_alterar_vale_transporte_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_alterar_vale_transporte_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Passe para os dias de tratamento", None))
        self.input_alterar_vale_transporte_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Passe do idoso", None))
        self.input_alterar_vale_transporte_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Passe livre", None))

        self.label_situacao_trabalho_alterar_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Situa\u00e7\u00e3o de trabalho", None))
        self.input_situacao_trabalho_alterar_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_situacao_trabalho_alterar_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Aposentado por Idade", None))
        self.input_situacao_trabalho_alterar_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Aposentado tempo de servi\u00e7o", None))
        self.input_situacao_trabalho_alterar_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Aposentado invalidez", None))
        self.input_situacao_trabalho_alterar_usuario_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Empregado/a Aut\u00f4nomo/a", None))
        self.input_situacao_trabalho_alterar_usuario_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Aposentado/a", None))
        self.input_situacao_trabalho_alterar_usuario_as.setItemText(6, QCoreApplication.translate("MainWindow", u"Pensionista", None))
        self.input_situacao_trabalho_alterar_usuario_as.setItemText(7, QCoreApplication.translate("MainWindow", u"Desempregado/a", None))
        self.input_situacao_trabalho_alterar_usuario_as.setItemText(8, QCoreApplication.translate("MainWindow", u"Aux\u00edlio doen\u00e7a", None))
        self.input_situacao_trabalho_alterar_usuario_as.setItemText(9, QCoreApplication.translate("MainWindow", u"Outros", None))

        self.label_alterar_beneficios_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Benef\u00edcios", None))
        self.input_alterar_beneficios_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_alterar_beneficios_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"BPC/Idoso", None))
        self.input_alterar_beneficios_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"BPC/PCD", None))
        self.input_alterar_beneficios_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Mais Social (Gov. Estadual)", None))
        self.input_alterar_beneficios_usuario_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Aux\u00edlio Brasil (Gov. Federal)", None))

        self.label_alterar_tarifa_social_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Tarifa social", None))
        self.input_alterar_tarifa_social_sim_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.input_alterar_tarifa_social_nao_usuario_as.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_alterar_tipo_tratamento_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Tipo de tratamento", None))
        self.input_alterar_tipo_tratamento_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_alterar_tipo_tratamento_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Pr\u00e9-Di\u00e1lise", None))
        self.input_alterar_tipo_tratamento_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Hemodi\u00e1lise", None))
        self.input_alterar_tipo_tratamento_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Di\u00e1lise Peritoneal", None))

        self.label_alterar_local_tratamento_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Local de tratamento", None))
        self.label_alterar_patologia_base_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Patologia base", None))
        self.input_alterar_patologia_base_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_alterar_patologia_base_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Hipertens\u00e3o", None))
        self.input_alterar_patologia_base_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Diabete 1", None))
        self.input_alterar_patologia_base_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Diabete 2", None))
        self.input_alterar_patologia_base_usuario_as.setItemText(4, QCoreApplication.translate("MainWindow", u"L\u00fapus", None))
        self.input_alterar_patologia_base_usuario_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Nefrites", None))
        self.input_alterar_patologia_base_usuario_as.setItemText(6, QCoreApplication.translate("MainWindow", u"Outros", None))

        self.label_alterar_data_inicio_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Data de in\u00edcio", None))
        self.label_alterar_periodo_usuario_as.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo", None))
        self.input_alterar_periodo_usuario_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_alterar_periodo_usuario_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Matutino", None))
        self.input_alterar_periodo_usuario_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Vespertino", None))
        self.input_alterar_periodo_usuario_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Noturno", None))

        self.btn_alterar_voltar_usuario_as.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_alterar_observacoes_sigilo_as.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es em sigilo", None))
        self.btn_alterar_proximo_as.setText(QCoreApplication.translate("MainWindow", u"PR\u00d3XIMO", None))
        self.btn_alterar_finalizar_as.setText(QCoreApplication.translate("MainWindow", u"FINALIZAR", None))
        self.label_alterar_estado_civil_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Estado civil", None))
        self.input_alterar_estado_civil_colaborador_comboBox_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_alterar_estado_civil_colaborador_comboBox_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Solteiro", None))
        self.input_alterar_estado_civil_colaborador_comboBox_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Casado", None))
        self.input_alterar_estado_civil_colaborador_comboBox_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Divorciado", None))
        self.input_alterar_estado_civil_colaborador_comboBox_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Vi\u00favo", None))
        self.input_alterar_estado_civil_colaborador_comboBox_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Separado", None))

        self.label_alterar_salario_colaborador_as_2.setText(QCoreApplication.translate("MainWindow", u"Sal\u00e1rio", None))
        self.input_alterar_salario_colaborador_as_2.setText("")
        self.label_alterar_escolaridade_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Escolaridade", None))
        self.input_alterar_escolaridade_colaborador_comboBox_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_alterar_escolaridade_colaborador_comboBox_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Fundamental", None))
        self.input_alterar_escolaridade_colaborador_comboBox_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Fundamental incompleto", None))
        self.input_alterar_escolaridade_colaborador_comboBox_as.setItemText(3, QCoreApplication.translate("MainWindow", u"M\u00e9dio", None))
        self.input_alterar_escolaridade_colaborador_comboBox_as.setItemText(4, QCoreApplication.translate("MainWindow", u"M\u00e9dio incompleto", None))
        self.input_alterar_escolaridade_colaborador_comboBox_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Superior completo", None))
        self.input_alterar_escolaridade_colaborador_comboBox_as.setItemText(6, QCoreApplication.translate("MainWindow", u"Superior incompleto", None))

        self.label_alterar_cargo_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Cargo", None))
        self.input_alterar_cargo_colaborador_comboBox_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_alterar_cargo_colaborador_comboBox_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Recepcionista", None))
        self.input_alterar_cargo_colaborador_comboBox_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Assistente Social", None))
        self.input_alterar_cargo_colaborador_comboBox_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Farmac\u00eautico (a)", None))
        self.input_alterar_cargo_colaborador_comboBox_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Psic\u00f3logo (a)", None))
        self.input_alterar_cargo_colaborador_comboBox_as.setItemText(5, QCoreApplication.translate("MainWindow", u"Fisioterapeuta", None))
        self.input_alterar_cargo_colaborador_comboBox_as.setItemText(6, QCoreApplication.translate("MainWindow", u"Nutricionista", None))
        self.input_alterar_cargo_colaborador_comboBox_as.setItemText(7, "")

        self.label_alterar_periodo_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo", None))
        self.input_alterar_periodo_colaborador_comboBox_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_alterar_periodo_colaborador_comboBox_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Matutino", None))
        self.input_alterar_periodo_colaborador_comboBox_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Vespertino", None))
        self.input_alterar_periodo_colaborador_comboBox_as.setItemText(3, QCoreApplication.translate("MainWindow", u"Noturno", None))
        self.input_alterar_periodo_colaborador_comboBox_as.setItemText(4, QCoreApplication.translate("MainWindow", u"Integral", None))

        self.label_alterar_orgao_expedidor_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"\u00d3rg\u00e3o expedidor", None))
        self.label_alterar_data_emissao_rg_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Data de emiss\u00e3o", None))
        self.label_alterar_pis_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"PIS", None))
        self.label_alterar_sexo_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.input_alterar_sexo_colaborador_comboBox_as.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.input_alterar_sexo_colaborador_comboBox_as.setItemText(1, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.input_alterar_sexo_colaborador_comboBox_as.setItemText(2, QCoreApplication.translate("MainWindow", u"Feminino", None))

        self.label_alterar_telefone_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.label_alterar_email_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_alterar_situacao_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Situa\u00e7\u00e3o", None))
        self.input_alterar_situacao_ativo_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Ativo", None))
        self.input_alterar_situacao_inativo_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Inativo", None))
        self.label_alterar_matricula_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Matricula", None))
        self.label_alterar_nome_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Nome colaborador", None))
        self.input_alterar_nome_colaborador_as.setText("")
        self.label_alterar_data_nascimento_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Data de nascimento", None))
        self.label_alterar_cpf_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.input_alterar_cpf_colaborador_as.setText("")
        self.label_alterar_rg_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.input_alterar_rg_colaborador_as.setText("")
        self.label_alterar_usuario_colaborador_as_2.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.label_alterar_senha_colaborador_as_2.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_alterar_confirmar_senha_colaborador_as_2.setText(QCoreApplication.translate("MainWindow", u"Confirmar Senha", None))
        self.label_alterar_cep_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.input_alterar_cep_colaborador_as.setInputMask(QCoreApplication.translate("MainWindow", u"00.000-000", None))
        self.input_alterar_cep_colaborador_as.setText(QCoreApplication.translate("MainWindow", u".-", None))
        self.btn_alterar_cep_buscar_colaborador_as.setText("")
        self.label_alterar_logradouro_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.label_alterar_numero_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.label_alterar_bairro_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.label_alterar_cidade_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_alterar_estado_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.input_alterar_estado_colaborador_as.setText("")
        self.input_alterar_foto_colaborador_as.setText("")
        self.btn_alterar_voltar_cadastro_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_alterar_concluir_cadastro_colaborador_as.setText(QCoreApplication.translate("MainWindow", u"CONCLUIR", None))
        self.btn_alterar_foto_senha_farm.setText("")
        self.label_ola_nome_farm.setText(QCoreApplication.translate("MainWindow", u"Ol\u00e1, _ _ _ _ _ _", None))
        self.btn_cadastrar_farm.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.btn_retirar_farm.setText(QCoreApplication.translate("MainWindow", u"   RETIRAR", None))
        self.btn_estoque_farm.setText(QCoreApplication.translate("MainWindow", u"   ESTOQUE", None))
        self.btn_sair_farm.setText(QCoreApplication.translate("MainWindow", u"SAIR  ", None))
        self.btn_alterar_foto_senha_fisio.setText("")
        self.label_ola_nome_fisio.setText(QCoreApplication.translate("MainWindow", u"Ol\u00e1, _ _ _ _ _ _", None))
        self.btn_consulta_fisio.setText(QCoreApplication.translate("MainWindow", u"    CONSULTA", None))
        self.btn_relatorios_fisio.setText(QCoreApplication.translate("MainWindow", u"  RELAT\u00d3RIOS", None))
        self.btn_sair_fisio.setText(QCoreApplication.translate("MainWindow", u"SAIR  ", None))
        self.btn_alterar_foto_senha_nutri.setText("")
        self.label_ola_nutri.setText(QCoreApplication.translate("MainWindow", u"Ol\u00e1, _ _ _ _ _ _", None))
        self.btn_plano_alimentar_nutri.setText(QCoreApplication.translate("MainWindow", u" PLANO ALIMENTAR", None))
        self.btn_consulta_nutri.setText(QCoreApplication.translate("MainWindow", u"    CONSULTA", None))
        self.btn_relatorios_nutri.setText(QCoreApplication.translate("MainWindow", u"  RELAT\u00d3RIOS", None))
        self.btn_sair_nutri.setText(QCoreApplication.translate("MainWindow", u"SAIR  ", None))
        self.btn_plano_alimentar_cadastrar_nutri.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR                 ", None))
        self.btn_plano_alimentar_buscar_nutri.setText(QCoreApplication.translate("MainWindow", u"BUSCAR                    ", None))
        self.btn_alterar_foto_senha_psi.setText("")
        self.label_ola_nome_psi.setText(QCoreApplication.translate("MainWindow", u"Ol\u00e1, _ _ _ _ _ _", None))
        self.btn_consulta_psi.setText(QCoreApplication.translate("MainWindow", u"   CONSULTA", None))
        self.btn_relatorios_psi.setText(QCoreApplication.translate("MainWindow", u"  RELAT\u00d3RIOS", None))
        self.btn_sair_psi.setText(QCoreApplication.translate("MainWindow", u"SAIR  ", None))
        self.btn_alterar_foto_senha_secret.setText("")
        self.label_ola_nome_secret.setText(QCoreApplication.translate("MainWindow", u"Ol\u00e1, _ _ _ _ _ _", None))
        self.btn_agenda_sec.setText(QCoreApplication.translate("MainWindow", u"    AGENDA", None))
        self.btn_eventos_sec.setText(QCoreApplication.translate("MainWindow", u"   EVENTOS", None))
        self.btn_relatorios_sec.setText(QCoreApplication.translate("MainWindow", u" RELAT\u00d3RIOS", None))
        self.btn_sair_sec.setText(QCoreApplication.translate("MainWindow", u"SAIR  ", None))
    # retranslateUi

