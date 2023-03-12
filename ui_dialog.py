from qtcore import *


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


class Ui_DadosSalvos(object):
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
        self.label_imagem_salvo.setPixmap(QPixmap(u"../icons/salve-.png"))
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


class Ui_TirarFoto(object):
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

