import sys
from os import getcwd
from qtcore import *
from ui_telas_abrec import *
from ui_dialog import *

class Overlay(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        palette = QPalette(self.palette())
        palette.setColor(QPalette.Window, Qt.transparent)
        self.setPalette(palette)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(0, 0, 0, 127)))
        painter.end()


################Class POPUP Login################
class DialogRecuperarSenha(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_RestaurarSenha()
        self.ui.setupUi(self)
        self.timer_msg = QTimer(self)
        self.timer_msg.setInterval(10000)
        self.timer_msg.timeout.connect(self.closeMsg)
        self.timer_msg.start()   

    def closeMsg(self):
        self.close()

    def closeEvent(self, event):
        self.timer_msg.stop()
        event.accept()


################Class POPUP Usuário################
class DialogTirarFoto(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_TirarFoto()
        self.ui.setupUi(self)
        self.timer_msg = QTimer(self)
        self.timer_msg.setInterval(10000)
        self.timer_msg.timeout.connect(self.closeMsg)
        self.timer_msg.start()   

    def closeMsg(self):
        self.close()

    def closeEvent(self, event):
        self.timer_msg.stop()
        event.accept()


################Class POPUP Cuidador################
class DialogAreaSigilo(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Area_Sob_Sigilo()
        self.ui.setupUi(self)
        self.timer_msg = QTimer(self)
        self.timer_msg.setInterval(10000)
        self.timer_msg.timeout.connect(self.closeMsg)
        self.timer_msg.start()   

    def closeMsg(self):
        self.close()

    def closeEvent(self, event):
        self.timer_msg.stop()
        event.accept()


class DialogCadastroIncompletoCuidador(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Cadastro_Incompleto()
        self.ui.setupUi(self)
        self.timer_msg = QTimer(self)
        self.timer_msg.setInterval(8000)
        self.timer_msg.timeout.connect(self.closeMsg)
        self.timer_msg.start()

    def closeMsg(self):
        self.close()

    def closeEvent(self, event):
        self.timer_msg.stop()
        event.accept()


##############Class POPUP Cursos e oficinas##############

class DialogCadastroIncompletoCursos(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Cadastro_Incompleto()
        self.ui.setupUi(self)
        self.timer_msg = QTimer(self)
        self.timer_msg.setInterval(8000)
        self.timer_msg.timeout.connect(self.closeMsg)
        self.timer_msg.start()

    def closeMsg(self):
        self.close()

    def closeEvent(self, event):
        self.timer_msg.stop()
        event.accept()



##############Class Alterar Foto e Senha##############
class DialogAlterarSenhaFoto(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_AlterarSenhaFoto()
        self.ui.setupUi(self)
        self.timer_msg = QTimer(self)
        self.timer_msg.setInterval(8000)
        self.timer_msg.timeout.connect(self.closeMsg)
        self.timer_msg.start()

    def closeMsg(self):
        self.close()

    def closeEvent(self, event):
        self.timer_msg.stop()
        event.accept()


#############################################################################
class TelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.popup = Overlay(self)
        self.popup.setMinimumWidth(1920)
        self.popup.setMinimumHeight(1080)
        self.popup.hide()

        self.showMaximized()

        self.ui.input_senha_login.setEchoMode(QLineEdit.Password)

        ###############SIGNALS#################
        self.ui.btn_entrar_login.clicked.connect(lambda: self.ui.inicio.setCurrentWidget(self.ui.area_principal))
        self.ui.toolButton.clicked.connect(self.visibilidade)        

        self.ui.btn_voltar_as.clicked.connect(lambda: self.ui.inicio.setCurrentWidget(self.ui.login))
        self.ui.btn_sair_as.clicked.connect(lambda: self.ui.inicio.setCurrentWidget(self.ui.login))
        
        self.ui.btn_cadastrar_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_cadastrar_cuidador_usuario_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_usuario_as))
        self.ui.btn_proximo_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_cuidador_as))
        self.ui.btn_cadastrar_cursos_oficinas_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastrar_cursos_e_oficinas_as))
        self.ui.btn_cadastrar_colaborador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_colaborador_as))

        ######SIGNALS POPUP recuperar senha login######
        self.ui.btn_esqueci_senha_login.clicked.connect(self.recuperarSenha)
        


        ######SIGNALS POPUP trocar foto e senha AS######
        self.ui.btn_alterar_foto_senha_as.clicked.connect(self.trocarFotoSenha)
        
        
        ############SIGNALS POPUP Usuario AS############
        self.ui.btn_foto_usuario_as.clicked.connect(self.tirarFoto)


        ############SIGNALS POPUP Cuidador AS############
        #self.ui.btn_sair_as.clicked.connect(self.sair)
        self.ui.btn_observacoes_sigilo_as.clicked.connect(self.permissaoSigilosa)
        self.ui.btn_finalizar_as.clicked.connect(self.concluirCadastroIncompletoCuidador)


        ############SIGNALS POPUP Cursos e oficinas AS############
        self.ui.btn_concluir_cursos_as.clicked.connect(self.cadastroIncompletoCursos)



    def visibilidade(self):
        if self.ui.input_senha_login.echoMode() == QLineEdit.Password:
                self.ui.input_senha_login.setEchoMode(QLineEdit.Normal)
                self.ui.toolButton.setIcon(QIcon("./icons/olho_fechado.png"))
        else:
            self.ui.input_senha_login.setEchoMode(QLineEdit.Password)
            self.ui.toolButton.setIcon(QIcon("./icons/olho.png"))


    def recuperarSenha(self):
        msg = DialogRecuperarSenha(self)
        self.popup.show()
        msg.exec()
        self.popup.hide()



    def trocarFotoSenha(self):
        msg = DialogAlterarSenhaFoto(self)
        self.popup.show()
        msg.exec()
        self.popup.hide()


    ################ def POPUP Cuidador################

    def permissaoSigilosa(self):
        msg = DialogAreaSigilo(self)
        self.popup.show()
        msg.exec()
        self.popup.hide()

        #conectar com o botão entrar depois
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_observacoes_sigilosas_as)

    def concluirCadastroIncompletoCuidador(self):
        msg = DialogCadastroIncompletoCuidador(self)
        self.popup.show()
        msg.exec()
        self.popup.hide()

        #conectar com o botão entrar depois
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_cuidador_as)


    ################ def POPUP Cursos e oficinas################

    def cadastroIncompletoCursos(self):
        msg = DialogCadastroIncompletoCursos(self)
        self.popup.show()
        msg.exec()
        self.popup.hide()

        #conectar com o botão entrar depois
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastrar_cursos_e_oficinas_as)


    ################ def POPUP Usuário################

    def tirarFoto(self):
        msg = DialogTirarFoto(self)
        self.popup.show()
        msg.exec()
        self.popup.hide()


        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TelaPrincipal()
    w.show()
    app.exec()