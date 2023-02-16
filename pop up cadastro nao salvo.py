# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pop up cadastro nao salvoONRLPR.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from PySide6 import *
import sys

class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
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
        self.btn_sair_popup_cadastro_nao_salvo_as.setStyleSheet(u"background-color: #F7B0B5; border-radius: 15px")

        self.horizontalLayout_3.addWidget(self.btn_sair_popup_cadastro_nao_salvo_as)

        self.btn_continuar_popup_cadastro_nao_salvo_as = QPushButton(self.frame_4)
        self.btn_continuar_popup_cadastro_nao_salvo_as.setObjectName(u"btn_continuar_popup_cadastro_nao_salvo_as")
        self.btn_continuar_popup_cadastro_nao_salvo_as.setMinimumSize(QSize(100, 30))
        self.btn_continuar_popup_cadastro_nao_salvo_as.setMaximumSize(QSize(100, 30))
        self.btn_continuar_popup_cadastro_nao_salvo_as.setFont(font1)
        self.btn_continuar_popup_cadastro_nao_salvo_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_continuar_popup_cadastro_nao_salvo_as.setStyleSheet(u"background-color: #00A8E8; color: #FFF; border-radius: 15px")

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


    

app = QApplication(sys.argv)
dialog = QDialog()
ui = Ui_Dialog()
ui.setupUi(dialog)
dialog.show()
sys.exit(app.exec_())
