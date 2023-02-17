# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pop up area sob sigiloDegSFr.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtcore import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
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
        self.label.setPixmap(QPixmap(u"icons/ciber-seguranca.png"))
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

