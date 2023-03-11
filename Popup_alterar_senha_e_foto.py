# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Popup_alterar_senha_e_foto.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 350)
        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 600, 350))
        self.frame_3.setStyleSheet(u"background-color: #FEE2E6; border: 1px solid #FD7D8C; border-radius: 40px")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.line = QFrame(self.frame_3)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(290, 0, 2, 351))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(300, 10, 291, 321))
        self.frame_4.setStyleSheet(u"border:none\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.btn_alterar_senha_usuario_sis = QPushButton(self.frame_4)
        self.btn_alterar_senha_usuario_sis.setObjectName(u"btn_alterar_senha_usuario_sis")
        self.btn_alterar_senha_usuario_sis.setGeometry(QRect(20, 20, 261, 291))
        self.btn_alterar_senha_usuario_sis.setStyleSheet(u"border:none\n"
"")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 80, 131, 101))
        self.label.setStyleSheet(u"border:none\n"
"")
        self.label.setPixmap(QPixmap(u"../../Documents/GitHub/Fabrica-SW-96/icons/troca.png"))
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 180, 281, 62))
        font = QFont()
        font.setFamilies([u"Abel"])
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"border: none")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 10, 271, 321))
        self.frame_5.setStyleSheet(u"border:none\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.btn_trocar_foto_usuario_sis = QPushButton(self.frame_5)
        self.btn_trocar_foto_usuario_sis.setObjectName(u"btn_trocar_foto_usuario_sis")
        self.btn_trocar_foto_usuario_sis.setGeometry(QRect(20, 20, 261, 291))
        self.btn_trocar_foto_usuario_sis.setStyleSheet(u"border:none\n"
"")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 180, 281, 62))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"border: none")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 70, 141, 111))
        self.label_3.setStyleSheet(u"border:none\n"
"")
        self.label_3.setPixmap(QPixmap(u"../../Downloads/camera 1.png"))
        self.label_3.setScaledContents(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_alterar_senha_usuario_sis.setText("")
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"ALTERAR SENHA", None))
        self.btn_trocar_foto_usuario_sis.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"TROCAR FOTO", None))
        self.label_3.setText("")
    # retranslateUi
