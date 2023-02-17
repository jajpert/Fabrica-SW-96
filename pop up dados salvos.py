# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pop up dados salvos modpqEGeR.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtcore import *
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
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
        self.label_imagem_salvo.setPixmap(QPixmap(u"icons/salve-.png"))
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

app = QApplication(sys.argv)
dialog = QDialog()
ui = Ui_Dialog()
ui.setupUi(dialog)
dialog.show()
sys.exit(app.exec_())