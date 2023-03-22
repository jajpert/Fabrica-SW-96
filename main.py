import sys
from os import getcwd
from ctypes import windll
from qtcore import *
from ui_telas_abrec import *
from ui_dialog import *
from database import *

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
        self.ui = Ui_Restaurar_Senha()
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
        self.ui = Ui_Tirar_Foto()
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


class DialogCadastroIncompletoUsuario(QDialog):
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
        self.ui = Ui_Alterar_Senha_Foto()
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

        ######################### banco #########################

        self.db = DataBase()





        self.popup = Overlay(self)
        self.popup.setMinimumWidth(1920)
        self.popup.setMinimumHeight(1080)
        self.popup.hide()

        self.showMaximized()

        self.ui.input_senha_login.setEchoMode(QLineEdit.Password)

        ###############SIGNALS#################
        self.ui.btn_entrar_login.clicked.connect(lambda: self.ui.inicio.setCurrentWidget(self.ui.area_principal))
        self.ui.toolButton.clicked.connect(self.visibilidade)        

        self.ui.btn_sair_as.clicked.connect(lambda: self.ui.inicio.setCurrentWidget(self.ui.login))
        
        self.ui.btn_cadastrar_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_consulta_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_consulta_as))
        self.ui.btn_buscar_consulta_as.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_consulta_depois))

        self.ui.btn_cadastrar_cuidador_usuario_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_cuidador_as))
        self.ui.btn_proximo_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_usuario_as))
        self.ui.btn_cadastrar_cursos_oficinas_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastrar_cursos_e_oficinas_as))
        self.ui.btn_cadastrar_colaborador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_colaborador_as))
        self.ui.btn_relatorios_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_relatorios_as))
        self.ui.btn_agenda_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_agenda_as))


        #############SIGNALS BOTOES voltar#############
        self.ui.btn_voltar_cursos_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_voltar_cuidador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_voltar_agenda_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_principal_as))
        self.ui.btn_voltar_usuario_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_cuidador_as))
        self.ui.btn_voltar_consulta_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_principal_as))
        self.ui.btn_voltar_observacoes_sigilosas_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_usuario_as))
        self.ui.btn_voltar_relatorios_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_principal_as))


        ######SIGNALS POPUP recuperar senha login######
        self.ui.btn_esqueci_senha_login.clicked.connect(self.recuperarSenha)
        


        ######SIGNALS POPUP trocar foto e senha AS######
        self.ui.btn_alterar_foto_senha_as.clicked.connect(self.trocarFotoSenha)
        
        
        ############SIGNALS POPUP Usuario AS############
        self.ui.btn_foto_usuario_as.clicked.connect(self.tirarFoto)


        ############SIGNALS POPUP Cuidador AS############
        #self.ui.btn_sair_as.clicked.connect(self.sair)
        #mudar tbm
        self.ui.btn_observacoes_sigilo_as.clicked.connect(self.permissaoSigilosa)
        #self.ui.btn_finalizar_as.clicked.connect(self.concluirCadastroIncompletoUsuario)


        ############SIGNALS POPUP Cursos e oficinas AS############
        self.ui.btn_concluir_cursos_as.clicked.connect(self.cadastroIncompletoCursos)


        ############SIGNALS BANCO ##########################
        self.ui.btn_finalizar_as.clicked.connect(self.cadastroUsuario)




########################### FUNÇÕES BANCO ###########################

    def cadastroUsuario(self):
        cep = self.ui.input_cep_usuario_as.text()
        rua = self.ui.input_logradouro_usuario_as.text()
        numero = self.ui.input_numero_usuario_as.text()
        bairro = self.ui.input_bairro_usuario_as.text()

        tupla_endereco = (cep,rua,numero,bairro)

        #######################################################

        nome = self.ui.input_nome_usuario_as.text()
        data_nascimento = '2004-06-25'
        cpf = self.ui.input_cpf_usuario_as.text()
        rg = self.ui.input_rg_usuario_as.text()
        data_emissao = self.ui.input_data_emissao_usuario_as.text()
        orgao_exp = self.ui.input_orgao_expedidor_usuario_as.text()
        sexo = self.ui.input_sexo_usuario_as.text()
        #status = 'f'
        telefone = self.ui.input_telefone_usuario_as.text()
        email = self.ui.input_email_usuario_as.text()
        escolaridade = self.ui.input_escolaridade_usuario_as.currentText()
        id_colaborador_resp = 1
        
        if self.ui.input_pessoa_cdeficiencia_sim_usuario_as.isChecked():
            pessoa_deficiencia = 'S'
        elif self.ui.label_pessoa_cdeficiencia_nao_usuario_as.isChecked():
            pessoa_deficiencia = 'N'

        tupla_pessoa = (nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,telefone,email,escolaridade,pessoa_deficiencia,id_colaborador_resp)

        #######################################################

        data_inclusao = "2023-03-18 18:16:51"
        nis = self.ui.input_nis_usuario_as.text()
        cns = self.ui.input_cns_usuario_as.text()
        situacao_trabalho = self.ui.input_situacao_trabalho_usuario_as.currentText()
        tipo_transporte = self.ui.input_meio_transporte_usuario_as.currentText()
        tipo_tratamento = self.ui.input_tipo_tratamento_usuario_as.currentText()
        beneficio = self.ui.input_beneficios_usuario_as.currentText()

        tupla_usuario = (data_inclusao, nis, cns, situacao_trabalho, tipo_transporte, tipo_tratamento, beneficio)
        

        print(tupla_endereco)
        print(tupla_pessoa)
        print(tupla_usuario)
        result = self.db.cadastro_usuario(tupla_endereco,tupla_pessoa,tupla_usuario)
        print(result)



####################### FUNÇÕES POP UP #######################

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

    def concluirCadastroIncompletoUsuario(self):
        msg = DialogCadastroIncompletoUsuario(self)
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
    
    myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid) 

    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('icons\Abrec logo paint-02 (2).png'))

    w = TelaPrincipal()
    w.show()
    app.exec()