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
        self.label_trocar_foto_popup_foto_as = QLabel(self.frame_5)
        self.label_trocar_foto_popup_foto_as.setObjectName(u"label_trocar_foto_popup_foto_as")
        self.label_trocar_foto_popup_foto_as.setMinimumSize(QSize(140, 140))
        self.label_trocar_foto_popup_foto_as.setMaximumSize(QSize(140, 140))
        self.label_trocar_foto_popup_foto_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_trocar_foto_popup_foto_as.setPixmap(QPixmap(u"./icons/camera.png"))
        self.label_trocar_foto_popup_foto_as.setScaledContents(True)
        self.label_trocar_foto_popup_foto_as.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_trocar_foto_popup_foto_as)


        self.verticalLayout.addWidget(self.frame_5)

        self.btn_trocar_foto_popup_foto_as = QPushButton(self.frame_2)
        self.btn_trocar_foto_popup_foto_as.setObjectName(u"btn_trocar_foto_popup_foto_as")
        self.btn_trocar_foto_popup_foto_as.setMinimumSize(QSize(140, 140))
        font = QFont()
        font.setFamilies([u"Abel"])
        font.setPointSize(32)
        self.btn_trocar_foto_popup_foto_as.setFont(font)
        self.btn_trocar_foto_popup_foto_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_trocar_foto_popup_foto_as)


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
        self.label_alterar_senha_popup_foto_as = QLabel(self.frame_4)
        self.label_alterar_senha_popup_foto_as.setObjectName(u"label_alterar_senha_popup_foto_as")
        self.label_alterar_senha_popup_foto_as.setMinimumSize(QSize(140, 140))
        self.label_alterar_senha_popup_foto_as.setMaximumSize(QSize(140, 140))
        self.label_alterar_senha_popup_foto_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_alterar_senha_popup_foto_as.setPixmap(QPixmap(u"./icons/troca.png"))
        self.label_alterar_senha_popup_foto_as.setScaledContents(True)
        self.label_alterar_senha_popup_foto_as.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_alterar_senha_popup_foto_as)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.btn_alterar_senha_popup_alterar_as = QPushButton(self.frame_3)
        self.btn_alterar_senha_popup_alterar_as.setObjectName(u"btn_alterar_senha_popup_alterar_as")
        self.btn_alterar_senha_popup_alterar_as.setMinimumSize(QSize(140, 140))
        self.btn_alterar_senha_popup_alterar_as.setFont(font)
        self.btn_alterar_senha_popup_alterar_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btn_alterar_senha_popup_alterar_as)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_trocar_foto_popup_foto_as.setText("")
        self.btn_trocar_foto_popup_foto_as.setText(QCoreApplication.translate("Dialog", u"Trocar foto", None))
        self.label_alterar_senha_popup_foto_as.setText("")
        self.btn_alterar_senha_popup_alterar_as.setText(QCoreApplication.translate("Dialog", u"Alterar senha", None))
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


################################################################################


class Ui_Popup_Lista_Pessoas(object):
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
        if (self.tabela_lista_de_cadastro_Oficinas_as.rowCount() < 23):
            self.tabela_lista_de_cadastro_Oficinas_as.setRowCount(23)
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
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(9, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(10, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(11, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(12, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(13, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(14, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(15, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(16, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(17, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(18, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(19, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(20, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(21, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tabela_lista_de_cadastro_Oficinas_as.setVerticalHeaderItem(22, __qtablewidgetitem28)
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
    # retranslateUi

