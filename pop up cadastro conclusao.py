# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pop up cadastro conclusaoLrLeVq.ui'
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
import sys

class Ui_Dialog(object):
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
        self.btn_voltar_popup_cadastro_conclusao.setStyleSheet(u"background-color: rgb(247, 176, 181);\n"
"border-radius:15px;\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_voltar_popup_cadastro_conclusao)

        self.btn_concluir_popup_cadastro_conclusao = QPushButton(self.frame_4)
        self.btn_concluir_popup_cadastro_conclusao.setObjectName(u"btn_concluir_popup_cadastro_conclusao")
        self.btn_concluir_popup_cadastro_conclusao.setMinimumSize(QSize(100, 30))
        self.btn_concluir_popup_cadastro_conclusao.setMaximumSize(QSize(100, 30))
        self.btn_concluir_popup_cadastro_conclusao.setFont(font1)
        self.btn_concluir_popup_cadastro_conclusao.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_concluir_popup_cadastro_conclusao.setStyleSheet(u"background-color: rgb(0, 168, 232);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);")

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

app = QApplication(sys.argv)
dialog = QDialog()
ui = Ui_Dialog()
ui.setupUi(dialog)
dialog.show()
sys.exit(app.exec_())
