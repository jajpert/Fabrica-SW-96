from qtcore import *

class Ui_Login_Ivalido(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)
        Dialog.setAttribute(Qt.WA_NoSystemBackground)
        Dialog.resize(440, 450)
        Dialog.setMinimumSize(QSize(440, 450))
        Dialog.setMaximumSize(QSize(440, 450))
        Dialog.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"background-color: #FEE2E6; border-radius: 20px; border: 1px solid #E58893")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: none")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_imagem_login_invalido_popup_as = QLabel(self.frame_2)
        self.label_imagem_login_invalido_popup_as.setObjectName(u"label_imagem_login_invalido_popup_as")
        self.label_imagem_login_invalido_popup_as.setMinimumSize(QSize(200, 200))
        self.label_imagem_login_invalido_popup_as.setMaximumSize(QSize(200, 200))
        self.label_imagem_login_invalido_popup_as.setPixmap(QPixmap(u"./icons/perigo.png"))
        self.label_imagem_login_invalido_popup_as.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_imagem_login_invalido_popup_as)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border: none")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_login_invalido_popup_as = QLabel(self.frame_4)
        self.label_login_invalido_popup_as.setObjectName(u"label_login_invalido_popup_as")
        self.label_login_invalido_popup_as.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Abel"])
        font.setPointSize(14)
        self.label_login_invalido_popup_as.setFont(font)
        self.label_login_invalido_popup_as.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_login_invalido_popup_as)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(167, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.btn_voltar_popup_login_invalido_as = QPushButton(self.frame_5)
        self.btn_voltar_popup_login_invalido_as.setObjectName(u"btn_voltar_popup_login_invalido_as")
        self.btn_voltar_popup_login_invalido_as.setMinimumSize(QSize(100, 30))
        self.btn_voltar_popup_login_invalido_as.setFont(font)
        self.btn_voltar_popup_login_invalido_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_popup_login_invalido_as.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(247, 176, 181);\n"
"border: 2px ;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(236, 132, 140);}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(247, 176, 181);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_voltar_popup_login_invalido_as)

        self.horizontalSpacer_2 = QSpacerItem(167, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)
        self.btn_voltar_popup_login_invalido_as.clicked.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_imagem_login_invalido_popup_as.setText("")
        self.label_login_invalido_popup_as.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Login Invalido</p></body></html>", None))
        self.btn_voltar_popup_login_invalido_as.setText(QCoreApplication.translate("Dialog", u"VOLTAR", None))
    # retranslateUi





class Ui_Area_Sob_Sigilo(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        
        Dialog.setWindowFlags(Qt.Dialog|Qt.FramelessWindowHint)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)

        Dialog.resize(500, 510)
        Dialog.setMinimumSize(QSize(500, 510))
        Dialog.setMaximumSize(QSize(500, 510))
        Dialog.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #FEE2E6; border: 1px solid #FD7D8C; border-radius: 40px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setLayoutDirection(Qt.LeftToRight)
        self.frame_4.setStyleSheet(u"border: none")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(220, 220))
        self.label.setMaximumSize(QSize(220, 220))
        self.label.setPixmap(QPixmap(u"./icons/ciber-seguranca.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_4)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Abel"])
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"border: none")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Abel"])
        font1.setPointSize(17)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"border: none")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: none")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.input_entrar_area_sigilo = QLineEdit(self.frame_2)
        self.input_entrar_area_sigilo.setObjectName(u"input_entrar_area_sigilo")
        self.input_entrar_area_sigilo.setMinimumSize(QSize(315, 40))
        self.input_entrar_area_sigilo.setMaximumSize(QSize(315, 40))
        font2 = QFont()
        font2.setFamilies([u"Abel"])
        font2.setPointSize(14)
        self.input_entrar_area_sigilo.setFont(font2)
        self.input_entrar_area_sigilo.setStyleSheet(u"QLineEdit{border-radius:20px; border: 1px solid #FD7D8C; background-color: #fff; padding-left: 0.5em; padding-right: 0.5em}\n"
"")
        self.input_entrar_area_sigilo.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.input_entrar_area_sigilo.setEchoMode(QLineEdit.Password)
        self.input_entrar_area_sigilo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.input_entrar_area_sigilo)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border: none")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_entrar_area_sigilo = QPushButton(self.frame_3)
        self.btn_entrar_area_sigilo.setObjectName(u"btn_entrar_area_sigilo")
        self.btn_entrar_area_sigilo.setMinimumSize(QSize(100, 30))
        self.btn_entrar_area_sigilo.setMaximumSize(QSize(100, 30))
        font3 = QFont()
        font3.setFamilies([u"Abel"])
        font3.setPointSize(12)
        self.btn_entrar_area_sigilo.setFont(font3)
        self.btn_entrar_area_sigilo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_entrar_area_sigilo.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(246, 176, 181);\n"
"border: 2px ;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(236, 132, 140);}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(246, 176, 181);}\n"
"")

        self.horizontalLayout_4.addWidget(self.btn_entrar_area_sigilo)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u00c1REA SOB SIGILO !", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"DIGITE O C\u00d3DIGO DE SEGURAN\u00c7A", None))
        self.input_entrar_area_sigilo.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite sua senha", None))
        self.btn_entrar_area_sigilo.setText(QCoreApplication.translate("Dialog", u"ENTRAR", None))
    # retranslateUi


############################################################################################


class Ui_Cadastro_Conclusao(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")

        Dialog.setWindowFlags(Qt.Dialog|Qt.FramelessWindowHint)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)

        Dialog.resize(440, 240)
        Dialog.setMinimumSize(QSize(440, 240))
        Dialog.setMaximumSize(QSize(440, 240))
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(440, 16777215))
        self.frame.setStyleSheet(u"background-color: rgb(254, 226, 230);\n"
"border-radius: 20px; \n"
"border:1px solid rgb(229, 136, 147);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: 0px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_popup_cadastro_conclusao = QLabel(self.frame_2)
        self.label_popup_cadastro_conclusao.setObjectName(u"label_popup_cadastro_conclusao")
        self.label_popup_cadastro_conclusao.setGeometry(QRect(0, 0, 420, 111))
        self.label_popup_cadastro_conclusao.setMinimumSize(QSize(230, 40))
        font = QFont()
        font.setFamilies([u"Abel"])
        font.setPointSize(14)
        self.label_popup_cadastro_conclusao.setFont(font)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border: 0px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(82, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_voltar_popup_cadastro_conclusao = QPushButton(self.frame_4)
        self.btn_voltar_popup_cadastro_conclusao.setObjectName(u"btn_voltar_popup_cadastro_conclusao")
        self.btn_voltar_popup_cadastro_conclusao.setMinimumSize(QSize(100, 30))
        self.btn_voltar_popup_cadastro_conclusao.setMaximumSize(QSize(100, 30))
        font1 = QFont()
        font1.setFamilies([u"Abel"])
        font1.setPointSize(12)
        self.btn_voltar_popup_cadastro_conclusao.setFont(font1)
        self.btn_voltar_popup_cadastro_conclusao.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_popup_cadastro_conclusao.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(247, 176, 181);\n"
"border: 2px ;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(236, 132, 140);}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(247, 176, 181);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_voltar_popup_cadastro_conclusao)

        self.btn_concluir_popup_cadastro_conclusao = QPushButton(self.frame_4)
        self.btn_concluir_popup_cadastro_conclusao.setObjectName(u"btn_concluir_popup_cadastro_conclusao")
        self.btn_concluir_popup_cadastro_conclusao.setMinimumSize(QSize(100, 30))
        self.btn_concluir_popup_cadastro_conclusao.setMaximumSize(QSize(100, 30))
        self.btn_concluir_popup_cadastro_conclusao.setFont(font1)
        self.btn_concluir_popup_cadastro_conclusao.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_concluir_popup_cadastro_conclusao.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(0, 168, 232);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px ;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 124, 191);}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 168, 232);\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_concluir_popup_cadastro_conclusao)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.horizontalSpacer_2 = QSpacerItem(82, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_popup_cadastro_conclusao.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><br/></p><p align=\"center\">Deseja concluir o cadastro?</p></body></html>", None))
        self.btn_voltar_popup_cadastro_conclusao.setText(QCoreApplication.translate("Dialog", u"VOLTAR", None))
        self.btn_concluir_popup_cadastro_conclusao.setText(QCoreApplication.translate("Dialog", u"CONCLUIR", None))
    # retranslateUi


############################################################################################


class Ui_Cadastro_Incompleto(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")

        Dialog.setWindowFlags(Qt.Dialog|Qt.FramelessWindowHint)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)

        Dialog.resize(440, 450)
        Dialog.setMinimumSize(QSize(440, 450))
        Dialog.setMaximumSize(QSize(440, 450))
        Dialog.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"background-color: #FEE2E6; border-radius: 20px; border: 1px solid #E58893")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: none")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 200))
        self.label.setMaximumSize(QSize(200, 200))
        self.label.setPixmap(QPixmap(u"./icons/perigo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border: none")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Abel"])
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(167, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.btn_voltar_popup_as = QPushButton(self.frame_5)
        self.btn_voltar_popup_as.setObjectName(u"btn_voltar_popup_as")
        self.btn_voltar_popup_as.setMinimumSize(QSize(100, 30))
        self.btn_voltar_popup_as.setFont(font)
        self.btn_voltar_popup_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_popup_as.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(247, 176, 181);\n"
"border: 2px ;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(236, 132, 140);}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(247, 176, 181);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_voltar_popup_as)

        self.horizontalSpacer_2 = QSpacerItem(167, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">O cadastro est\u00e1 incompleto!</p><p align=\"center\">Por favor complete o cadastro </p><p align=\"center\">para prosseguir</p></body></html>", None))
        self.btn_voltar_popup_as.setText(QCoreApplication.translate("Dialog", u"VOLTAR", None))
    # retranslateUi


############################################################################################


class Ui_Cadastro_Nao_Salvo(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")

        Dialog.setWindowFlags(Qt.Dialog|Qt.FramelessWindowHint)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)

        Dialog.resize(440, 240)
        Dialog.setMinimumSize(QSize(440, 240))
        Dialog.setMaximumSize(QSize(440, 240))
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: #FEE2E6; border-radius: 20px; border: 1px solid #E58893")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border: none")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(230, 70))
        font = QFont()
        font.setFamilies([u"Abel"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"padding-top: 2em")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: none")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_sair_popup_cadastro_nao_salvo_as = QPushButton(self.frame_4)
        self.btn_sair_popup_cadastro_nao_salvo_as.setObjectName(u"btn_sair_popup_cadastro_nao_salvo_as")
        self.btn_sair_popup_cadastro_nao_salvo_as.setMinimumSize(QSize(100, 30))
        self.btn_sair_popup_cadastro_nao_salvo_as.setMaximumSize(QSize(100, 30))
        font1 = QFont()
        font1.setFamilies([u"Abel"])
        font1.setPointSize(12)
        self.btn_sair_popup_cadastro_nao_salvo_as.setFont(font1)
        self.btn_sair_popup_cadastro_nao_salvo_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sair_popup_cadastro_nao_salvo_as.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(247, 176, 181);\n"
"border: 2px ;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(236, 132, 140);}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(247, 176, 181);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_sair_popup_cadastro_nao_salvo_as)

        self.btn_continuar_popup_cadastro_nao_salvo_as = QPushButton(self.frame_4)
        self.btn_continuar_popup_cadastro_nao_salvo_as.setObjectName(u"btn_continuar_popup_cadastro_nao_salvo_as")
        self.btn_continuar_popup_cadastro_nao_salvo_as.setMinimumSize(QSize(100, 30))
        self.btn_continuar_popup_cadastro_nao_salvo_as.setMaximumSize(QSize(100, 30))
        self.btn_continuar_popup_cadastro_nao_salvo_as.setFont(font1)
        self.btn_continuar_popup_cadastro_nao_salvo_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_continuar_popup_cadastro_nao_salvo_as.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(0, 168, 232);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px ;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 124, 191);}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 168, 232);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_continuar_popup_cadastro_nao_salvo_as)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.horizontalSpacer_2 = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">O cadastro n\u00e3o foi salvo. </p><p align=\"center\">Deseja sair mesmo assim?</p></body></html>", None))
        self.btn_sair_popup_cadastro_nao_salvo_as.setText(QCoreApplication.translate("Dialog", u"SAIR", None))
        self.btn_continuar_popup_cadastro_nao_salvo_as.setText(QCoreApplication.translate("Dialog", u"CONTINUAR", None))
    # retranslateUi


############################################################################################


class Ui_Dados_Salvos(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")

        Dialog.setWindowFlags(Qt.Dialog|Qt.FramelessWindowHint)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)

        Dialog.resize(350, 350)
        Dialog.setMinimumSize(QSize(350, 350))
        Dialog.setMaximumSize(QSize(350, 350))
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(350, 350))
        self.frame.setMaximumSize(QSize(350, 350))
        self.frame.setStyleSheet(u"background-color: #FEE2E6; border-radius: 20px; border: 1px solid #E58893")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        font = QFont()
        font.setFamilies([u"Abel"])
        font.setPointSize(14)
        self.frame_3.setFont(font)
        self.frame_3.setMouseTracking(True)
        self.frame_3.setStyleSheet(u"border:0px")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: none")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_imagem_salvo = QLabel(self.frame_2)
        self.label_imagem_salvo.setObjectName(u"label_imagem_salvo")
        self.label_imagem_salvo.setMinimumSize(QSize(150, 150))
        self.label_imagem_salvo.setMaximumSize(QSize(150, 150))
        self.label_imagem_salvo.setPixmap(QPixmap(u"./icons/salve-.png"))
        self.label_imagem_salvo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_imagem_salvo)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.label_pop_up_dados_salvos = QLabel(self.frame_3)
        self.label_pop_up_dados_salvos.setObjectName(u"label_pop_up_dados_salvos")
        self.label_pop_up_dados_salvos.setFont(font)
        self.label_pop_up_dados_salvos.setStyleSheet(u"")
        self.label_pop_up_dados_salvos.setFrameShape(QFrame.NoFrame)
        self.label_pop_up_dados_salvos.setAlignment(Qt.AlignCenter)
        self.label_pop_up_dados_salvos.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.label_pop_up_dados_salvos)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 2)

        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_imagem_salvo.setText("")
        self.label_pop_up_dados_salvos.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">DADOS SALVOS COM SUCESSO!</p><p </body></html>", None))
    # retranslateUi


############################################################################################


class Ui_Tirar_Foto(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")

        Dialog.setWindowFlags(Qt.Dialog|Qt.FramelessWindowHint)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)

        Dialog.resize(600, 350)
        Dialog.setMinimumSize(QSize(600, 350))
        Dialog.setMaximumSize(QSize(600, 350))
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #FEE2E6; border-radius: 15px; border: 1px solid #E58893;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 200))
        self.frame_5.setMaximumSize(QSize(16777215, 200))
        self.frame_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_tirar_foto_popup_foto_as = QLabel(self.frame_5)
        self.label_tirar_foto_popup_foto_as.setObjectName(u"label_tirar_foto_popup_foto_as")
        self.label_tirar_foto_popup_foto_as.setMinimumSize(QSize(140, 140))
        self.label_tirar_foto_popup_foto_as.setMaximumSize(QSize(140, 140))
        self.label_tirar_foto_popup_foto_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_tirar_foto_popup_foto_as.setPixmap(QPixmap(u"./icons/camera.png"))
        self.label_tirar_foto_popup_foto_as.setScaledContents(True)
        self.label_tirar_foto_popup_foto_as.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_tirar_foto_popup_foto_as)


        self.verticalLayout.addWidget(self.frame_5)

        self.btn_tirar_foto_popup_foto_as = QPushButton(self.frame_2)
        self.btn_tirar_foto_popup_foto_as.setObjectName(u"btn_tirar_foto_popup_foto_as")
        self.btn_tirar_foto_popup_foto_as.setMinimumSize(QSize(140, 140))
        font = QFont()
        font.setFamilies([u"Abel"])
        font.setPointSize(32)
        self.btn_tirar_foto_popup_foto_as.setFont(font)
        self.btn_tirar_foto_popup_foto_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_tirar_foto_popup_foto_as)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(2, 0))
        self.line.setMaximumSize(QSize(2, 16777215))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border: none;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 200))
        self.frame_4.setMaximumSize(QSize(16777215, 200))
        self.frame_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_importar_popup_foto_as = QLabel(self.frame_4)
        self.label_importar_popup_foto_as.setObjectName(u"label_importar_popup_foto_as")
        self.label_importar_popup_foto_as.setMinimumSize(QSize(140, 140))
        self.label_importar_popup_foto_as.setMaximumSize(QSize(140, 140))
        self.label_importar_popup_foto_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_importar_popup_foto_as.setPixmap(QPixmap(u"./icons/seta-para-baixo.png"))
        self.label_importar_popup_foto_as.setScaledContents(True)
        self.label_importar_popup_foto_as.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_importar_popup_foto_as)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.btn_importar_popup_foto_as = QPushButton(self.frame_3)
        self.btn_importar_popup_foto_as.setObjectName(u"btn_importar_popup_foto_as")
        self.btn_importar_popup_foto_as.setMinimumSize(QSize(140, 140))
        self.btn_importar_popup_foto_as.setFont(font)
        self.btn_importar_popup_foto_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btn_importar_popup_foto_as)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_tirar_foto_popup_foto_as.setText("")
        self.btn_tirar_foto_popup_foto_as.setText(QCoreApplication.translate("Dialog", u"Tirar foto", None))
        self.label_importar_popup_foto_as.setText("")
        self.btn_importar_popup_foto_as.setText(QCoreApplication.translate("Dialog", u"Importar", None))
    # retranslateUi


############################################################################################


class Ui_Alterar_Senha_Foto(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowFlags(Qt.Popup|Qt.FramelessWindowHint)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)
        Dialog.setAttribute(Qt.WA_NoSystemBackground)
        Dialog.resize(600, 350)
        Dialog.setMinimumSize(QSize(600, 350))
        Dialog.setMaximumSize(QSize(600, 350))
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #FEE2E6; border-radius: 15px; border: 1px solid #E58893;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolButton_alterar_foto_popup_perfil_as = QToolButton(self.frame_2)
        self.toolButton_alterar_foto_popup_perfil_as.setObjectName(u"toolButton_alterar_foto_popup_perfil_as")
        self.toolButton_alterar_foto_popup_perfil_as.setMinimumSize(QSize(298, 348))
        font = QFont()
        font.setFamilies([u"Abel"])
        font.setPointSize(32)
        font.setBold(True)
        self.toolButton_alterar_foto_popup_perfil_as.setFont(font)
        self.toolButton_alterar_foto_popup_perfil_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_alterar_foto_popup_perfil_as.setFocusPolicy(Qt.StrongFocus)
        self.toolButton_alterar_foto_popup_perfil_as.setStyleSheet(u"QToolButton::hover{\n"
"background-color: rgb(251, 207, 216);\n"
"}")
        icon = QIcon()
        icon.addFile(u"./icons/camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_alterar_foto_popup_perfil_as.setIcon(icon)
        self.toolButton_alterar_foto_popup_perfil_as.setIconSize(QSize(145, 145))
        self.toolButton_alterar_foto_popup_perfil_as.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.toolButton_alterar_foto_popup_perfil_as)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(2, 0))
        self.line.setMaximumSize(QSize(2, 16777215))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border: none;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toolButton_alterar_senha_popup_perfil_as = QToolButton(self.frame_3)
        self.toolButton_alterar_senha_popup_perfil_as.setObjectName(u"toolButton_alterar_senha_popup_perfil_as")
        self.toolButton_alterar_senha_popup_perfil_as.setMinimumSize(QSize(298, 348))
        self.toolButton_alterar_senha_popup_perfil_as.setFont(font)
        self.toolButton_alterar_senha_popup_perfil_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_alterar_senha_popup_perfil_as.setFocusPolicy(Qt.StrongFocus)
        self.toolButton_alterar_senha_popup_perfil_as.setStyleSheet(u"QToolButton::hover{\n"
"background-color: rgb(251, 207, 216);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./icons/troca.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_alterar_senha_popup_perfil_as.setIcon(icon1)
        self.toolButton_alterar_senha_popup_perfil_as.setIconSize(QSize(145, 145))
        self.toolButton_alterar_senha_popup_perfil_as.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.toolButton_alterar_senha_popup_perfil_as)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.toolButton_alterar_foto_popup_perfil_as.setText(QCoreApplication.translate("Dialog", u"Alterar foto", None))
        self.toolButton_alterar_senha_popup_perfil_as.setText(QCoreApplication.translate("Dialog", u"Alterar senha", None))
    # retranslateUi


############################################################################################



class Ui_Restaurar_Senha(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")

        Dialog.setWindowFlags(Qt.Dialog|Qt.FramelessWindowHint)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)

        Dialog.resize(440, 670)
        Dialog.setStyleSheet(u";")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 15px;border: 1px solid #E58893")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: #F8C0C7; border-top-left-radius: 15px; border-bottom-left-radius: 0px; border-top-right-radius: 15px; border-bottom-right-radius: 0px; border: none;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_recuperacao_popup_senha = QLabel(self.frame_9)
        self.label_recuperacao_popup_senha.setObjectName(u"label_recuperacao_popup_senha")
        font = QFont()
        font.setFamilies([u"Abel"])
        font.setPointSize(20)
        self.label_recuperacao_popup_senha.setFont(font)
        self.label_recuperacao_popup_senha.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_recuperacao_popup_senha)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{background-color: #FEE2E6;border-top-left-radius: 0px; border-bottom-left-radius: 15px; border-top-right-radius: 0px; border-bottom-right-radius: 15px; border: none}\n"
"QLineEdit{background-color: #fff; border-radius: 15px; padding-left: 0.5em; padding-right: 0.5em; border: 1px solid #A85751; height: 30px}\n"
"QLineEdit:focus{outline:0; border: 2px solid #A85751}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(40, 10, 40, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_cpf_popup_senha = QLabel(self.frame_3)
        self.label_cpf_popup_senha.setObjectName(u"label_cpf_popup_senha")
        font1 = QFont()
        font1.setFamilies([u"Abel"])
        font1.setPointSize(16)
        self.label_cpf_popup_senha.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_cpf_popup_senha)

        self.input_cpf_popup_senha = QLineEdit(self.frame_3)
        self.input_cpf_popup_senha.setObjectName(u"input_cpf_popup_senha")
        self.input_cpf_popup_senha.setMinimumSize(QSize(0, 35))
        self.input_cpf_popup_senha.setMaximumSize(QSize(16777215, 35))
        self.input_cpf_popup_senha.setFont(font1)
        self.input_cpf_popup_senha.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.input_cpf_popup_senha)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_pergunta1_popup_senha = QLabel(self.frame_4)
        self.label_pergunta1_popup_senha.setObjectName(u"label_pergunta1_popup_senha")
        self.label_pergunta1_popup_senha.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_pergunta1_popup_senha)

        self.input_pergunta1_popup_senha = QLineEdit(self.frame_4)
        self.input_pergunta1_popup_senha.setObjectName(u"input_pergunta1_popup_senha")
        self.input_pergunta1_popup_senha.setMinimumSize(QSize(0, 35))
        self.input_pergunta1_popup_senha.setMaximumSize(QSize(16777215, 35))
        self.input_pergunta1_popup_senha.setFont(font1)

        self.verticalLayout_6.addWidget(self.input_pergunta1_popup_senha)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_pergunta2_popup_senha = QLabel(self.frame_5)
        self.label_pergunta2_popup_senha.setObjectName(u"label_pergunta2_popup_senha")
        self.label_pergunta2_popup_senha.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_pergunta2_popup_senha)

        self.input_pergunta2_popup_senha = QLineEdit(self.frame_5)
        self.input_pergunta2_popup_senha.setObjectName(u"input_pergunta2_popup_senha")
        self.input_pergunta2_popup_senha.setMinimumSize(QSize(0, 35))
        self.input_pergunta2_popup_senha.setMaximumSize(QSize(16777215, 35))
        self.input_pergunta2_popup_senha.setFont(font1)

        self.verticalLayout_7.addWidget(self.input_pergunta2_popup_senha)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_nova_senha_popup_senha = QLabel(self.frame_6)
        self.label_nova_senha_popup_senha.setObjectName(u"label_nova_senha_popup_senha")
        self.label_nova_senha_popup_senha.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_nova_senha_popup_senha)

        self.input_nova_senha_popup_senha = QLineEdit(self.frame_6)
        self.input_nova_senha_popup_senha.setObjectName(u"input_nova_senha_popup_senha")
        self.input_nova_senha_popup_senha.setMinimumSize(QSize(0, 35))
        self.input_nova_senha_popup_senha.setMaximumSize(QSize(16777215, 35))
        self.input_nova_senha_popup_senha.setFont(font1)

        self.verticalLayout_8.addWidget(self.input_nova_senha_popup_senha)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_confirmar_senha_popup_senha = QLabel(self.frame_7)
        self.label_confirmar_senha_popup_senha.setObjectName(u"label_confirmar_senha_popup_senha")
        self.label_confirmar_senha_popup_senha.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_confirmar_senha_popup_senha)

        self.input_confirmar_senha_popup_senha = QLineEdit(self.frame_7)
        self.input_confirmar_senha_popup_senha.setObjectName(u"input_confirmar_senha_popup_senha")
        self.input_confirmar_senha_popup_senha.setMinimumSize(QSize(0, 35))
        self.input_confirmar_senha_popup_senha.setMaximumSize(QSize(16777215, 35))
        self.input_confirmar_senha_popup_senha.setFont(font1)

        self.verticalLayout_9.addWidget(self.input_confirmar_senha_popup_senha)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_8)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_verificar_popup_senha = QPushButton(self.frame_8)
        self.btn_verificar_popup_senha.setObjectName(u"btn_verificar_popup_senha")
        self.btn_verificar_popup_senha.setMinimumSize(QSize(120, 40))
        self.btn_verificar_popup_senha.setMaximumSize(QSize(120, 40))
        self.btn_verificar_popup_senha.setFont(font)
        self.btn_verificar_popup_senha.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_verificar_popup_senha.setStyleSheet(u"QPushButton{color: #fff; background-color: #00A8E8; border-radius: 20px; border: none}\n"
"QPushButton:hover{background-color: #23B2EE}\n"
"QPushButton:focus{outline:0}")

        self.horizontalLayout.addWidget(self.btn_verificar_popup_senha)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame_8)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 8)

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_recuperacao_popup_senha.setText(QCoreApplication.translate("Dialog", u"RECUPERA\u00c7\u00c3O DE SENHA", None))
        self.label_cpf_popup_senha.setText(QCoreApplication.translate("Dialog", u"CPF", None))
        self.label_pergunta1_popup_senha.setText(QCoreApplication.translate("Dialog", u"Pergunta de seguran\u00e7a 1", None))
        self.label_pergunta2_popup_senha.setText(QCoreApplication.translate("Dialog", u"Pergunta de seguran\u00e7a 2", None))
        self.label_nova_senha_popup_senha.setText(QCoreApplication.translate("Dialog", u"Nova senha", None))
        self.label_confirmar_senha_popup_senha.setText(QCoreApplication.translate("Dialog", u"Confirmar senha", None))
        self.btn_verificar_popup_senha.setText(QCoreApplication.translate("Dialog", u"Verificar", None))
    # retranslateUi

######################################################################################################################################################
class Ui_Confirma_Saida(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")

        Dialog.setWindowFlags(Qt.Dialog|Qt.FramelessWindowHint)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)

        Dialog.resize(440, 240)
        Dialog.setMinimumSize(QSize(440, 240))
        Dialog.setMaximumSize(QSize(440, 240))
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(440, 16777215))
        self.frame.setStyleSheet(u"background-color: rgb(254, 226, 230);\n"
"border-radius: 20px; \n"
"border:1px solid rgb(229, 136, 147);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: 0px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_popup_confirma_saida = QLabel(self.frame_2)
        self.label_popup_confirma_saida.setObjectName(u"label_popup_confirma_saida")
        self.label_popup_confirma_saida.setGeometry(QRect(0, 0, 420, 111))
        self.label_popup_confirma_saida.setMinimumSize(QSize(230, 40))
        font = QFont()
        font.setFamilies([u"Abel"])
        font.setPointSize(14)
        self.label_popup_confirma_saida.setFont(font)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border: 0px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(82, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_nao_popup_confirma_saida = QPushButton(self.frame_4)
        self.btn_nao_popup_confirma_saida.setObjectName(u"btn_nao_popup_confirma_saida")
        self.btn_nao_popup_confirma_saida.setMinimumSize(QSize(100, 30))
        self.btn_nao_popup_confirma_saida.setMaximumSize(QSize(100, 30))
        font1 = QFont()
        font1.setFamilies([u"Abel"])
        font1.setPointSize(12)
        self.btn_nao_popup_confirma_saida.setFont(font1)
        self.btn_nao_popup_confirma_saida.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_nao_popup_confirma_saida.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(247, 176, 181);\n"
"border: 2px ;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(236, 132, 140);}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(247, 176, 181);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_nao_popup_confirma_saida)

        self.btn_sim_popup_confirma_saida = QPushButton(self.frame_4)
        self.btn_sim_popup_confirma_saida.setObjectName(u"btn_sim_popup_confirma_saida")
        self.btn_sim_popup_confirma_saida.setMinimumSize(QSize(100, 30))
        self.btn_sim_popup_confirma_saida.setMaximumSize(QSize(100, 30))
        self.btn_sim_popup_confirma_saida.setFont(font1)
        self.btn_sim_popup_confirma_saida.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sim_popup_confirma_saida.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(0, 168, 232);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px ;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 124, 191);}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 168, 232);\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_sim_popup_confirma_saida)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.horizontalSpacer_2 = QSpacerItem(82, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_popup_confirma_saida.setText(QCoreApplication.translate("", u"<html><head/><body><p align=\"center\"><br/></p><p align=\"center\">Deseja sair?</p></body></html>", None))
        self.btn_nao_popup_confirma_saida.setText(QCoreApplication.translate("Dialog", u"N\u00c3O", None))
        self.btn_sim_popup_confirma_saida.setText(QCoreApplication.translate("Dialog", u"SIM", None))
    # retranslateUi

