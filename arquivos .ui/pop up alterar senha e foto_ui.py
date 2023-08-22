# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pop up alterar senha e foto.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
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
        self.label_trocar_foto_popup_foto_as.setPixmap(QPixmap(u"../icons/camera.png"))
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
        self.label_alterar_senha_popup_foto_as.setPixmap(QPixmap(u"../icons/troca.png"))
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

