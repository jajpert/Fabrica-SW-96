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
        self.ui.btn_voltar_cadastro_colaborador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_colaborador_as))
#BTN Voltar Colaborador

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
        self.ui.btn_salvar_as.clicked.connect(self.cadastroCuidador)
        self.ui.btn_concluir_cadastro_colaborador_as.clicked.connect(self.cadastroColaborador)
        self.ui.btn_concluir_cursos_as.clicked.connect(self.cadastroCurso)




########################### FUNÇÕES BANCO ###########################
    
    def cadastroUsuario(self):

        parentesco = self.ui.input_parentesco_cuidador_as.text()
        observacao ='none' #self.ui.input_informacoes_gerais_as.setText()''
        id_matricula = 1
        tupla_cuidador = (parentesco,observacao,id_matricula)

        ################################################3#####
        cep = self.ui.input_cep_usuario_as.text()
        rua = self.ui.input_logradouro_usuario_as.text()
        numero = self.ui.input_numero_usuario_as.text()
        bairro = self.ui.input_bairro_usuario_as.text()
        id_cidade=2

        tupla_endereco = (cep,rua,numero,bairro,id_cidade)

        #######################################################

        nome = self.ui.input_nome_usuario_as.text()
        data_nascimento = '2004-06-25'
        cpf = self.ui.input_cpf_usuario_as.text()
        rg = self.ui.input_rg_usuario_as.text()
        data_emissao = '2004-06-25' #self.ui.input_data_emissao_usuario_as.text()
        orgao_exp = self.ui.input_orgao_expedidor_usuario_as.text()
        sexo = self.ui.input_sexo_usuario_as.text()
        data_cadastro = '2004-06-25'
        telefone = self.ui.input_telefone_usuario_as.text()
        email = self.ui.input_email_usuario_as.text()
        escolaridade = self.ui.input_escolaridade_usuario_as.currentText()
        estado_civil = self.ui.input_estado_civil_usuario_as.currentText()

        id_colaborador_resp = 1

        #######################################################
        
        nis = self.ui.input_nis_usuario_as.text()
        cns = self.ui.input_cns_usuario_as.text()
        observacao_ = 'none'
        situacao_trabalho = self.ui.input_situacao_trabalho_usuario_as.currentText()
        tipo_transporte = self.ui.input_meio_transporte_usuario_as.currentText()
        tipo_tratamento = self.ui.input_tipo_tratamento_usuario_as.currentText()
        beneficio = self.ui.input_beneficios_usuario_as.currentText()
        local_tratamento = self.ui.input_local_tratamento_usuario_as.text()
        patologia_base  = self.ui.input_patologia_base_usuario_as.currentText()
        data_inicio = self.ui.input_data_inicio_usuario_as.text()
        periodo = self.ui.input_periodo_usuario_as.currentText()
        media_renda_familiar = self.ui.input_renda_familiar_usuario_as.currentText()
        vale_trasnporte = self.ui.input_vale_transporte_usuario_as.currentText()


        tarifa_social =  self.ui.input_tarifa_social_sim_usuario_as.isChecked()

        if self.ui.input_tarifa_social_sim_usuario_as.isChecked():
            tarifa_social = 'S'
        else:
            tarifa_social = 'N'

        if self.ui.input_pessoa_cdeficiencia_sim_usuario_as.isChecked():
            pessoa_deficiencia = 'SIM'

        else:
            pessoa_deficiencia = 'NÃO'
        
        if self.ui.input_situacao_ativo_usuario_as.isChecked():
            status = 'Ativo'
        else:
            status = 'Inativo'
        


        tupla_usuario = (nis,cns,observacao_,situacao_trabalho,tipo_transporte,tipo_tratamento,beneficio,local_tratamento,periodo,data_inicio,patologia_base,tarifa_social,media_renda_familiar,vale_trasnporte)

        tupla_pessoa = (nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status,telefone,email,escolaridade,estado_civil,pessoa_deficiencia,data_cadastro,id_colaborador_resp)
         
        result = self.db.cadastro_usuario(tupla_endereco,tupla_pessoa,tupla_usuario,tupla_cuidador)
        print(result)

        
    def cadastroCuidador(self):

        ########################endereco################################
        cep = self.ui.input_cep_cuidador_as.text()
        rua = self.ui.input_logradouro_cuidador_as.text()
        numero = self.ui.input_numero_cuidador_as.text()
        bairro = self.ui.input_bairro_cuidador_as.text()
        id_cidade = 2
        
        tupla_endereco = (cep,rua,numero,bairro,id_cidade)

        ######################pessoa#################################

        nome = self.ui.input_nome_cuidador_as.text()
        data_nascimento = '00/00/0000'
        cpf = self.ui.input_cpf_cuidador_as.text()
        rg = self.ui.input_rg_cuidador_as.text()
        data_emissao = self.ui.input_data_emissao_cuidador_as.text()
        orgao_exp = self.ui.input_orgao_expedidor_cuidador_as.text()
        sexo = self.ui.input_sexo_cuidador_as.text()
        data_cadastro = '00/00/0000'
        telefone = self.ui.input_telefone_cuidador_as.text()
        email = self.ui.input_email_cuidador_as.text()  
        escolaridade = self.ui.input_escolaridade_colaborador_comboBox_as.currentText()     

        tupla_pessoa = (nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,data_cadastro,telefone,email,escolaridade)

        #############################cuidador#############################################3

        parentesco = self.ui.input_parentesco_cuidador_as.text()
        observacao ='none' #self.ui.input_informacoes_gerais_as.setText()''
        tupla_cuidador = (parentesco,observacao)

        print(tupla_endereco)
        print(tupla_pessoa)
        print(tupla_cuidador)

        ##############################insert#######################################

        result = self.db.cadastro_cuidador(tupla_endereco,tupla_pessoa,tupla_cuidador)
        print(result)

    def cadastroColaborador(self):
        cep = self.ui.input_cep_colaborador_as.text()
        rua = self.ui.input_logradouro_colaborador_as.text()
        numero = self.ui.input_numero_colaborador_as.text()
        bairro = self.ui.input_bairro_colaborador_as.text()
        id_cidade = 2
        
        tupla_endereco = (cep,rua,numero,bairro,id_cidade)

        nome = self.ui.input_nome_colaborador_as.text()
        data_nascimento = self.ui.input_data_nascimento_colaborador_as.text()
        cpf = self.ui.input_cpf_colaborador_as.text()
        rg = self.ui.input_rg_colaborador_as.text()
        data_emissao = self.ui.input_data_emissao_rg_colaborador_as.text()
        orgao_exp = self.ui.input_orgao_expedidor_colaborador_as.text()
        sexo = self.ui.input_sexo_colaborador_comboBox_as.currentText()
        data_cadastro = '00/00/0000'
        telefone = self.ui.input_telefone_colaborador_as.text()
        email = self.ui.input_email_colaborador_as.text()      
        escolaridade = self.ui.input_escolaridade_colaborador_comboBox_as.currentText()
        estado_civil = self.ui.input_estado_civil_colaborador_comboBox_as.currentText()

        if self.ui.input_pessoa_cdeficiencia_sim_colaborador_as.isChecked():
            pessoa_deficiencia = 'S'
        else:
            pessoa_deficiencia = 'N'
        if self.ui.input_situacao_ativo_usuario_as.isChecked():
            status = 'Ativo'
        else:
            status = 'Inativo'
        tipo_deficiencia = self.ui.input_tipo_deficiencia_colaborador_as.text()

        tupla_pessoa = (nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status,data_cadastro,telefone,email,escolaridade,estado_civil,pessoa_deficiencia,tipo_deficiencia)

        ##########################################################################3

        salario = self.ui.input_salario_colaborador_as.text()
        data_admissao = '00/00/0000'
        pis = self.ui.input_pis_colaborador_as.text()
        perido = self.ui.input_periodo_colaborador_comboBox_as.currentText()
        descricao_cargo = self.ui.input_descricao_cargo_colaborador_as.text()
        
        tupla_colaborador = (salario,data_admissao,pis,perido,descricao_cargo)

        ##########################################################################

        login = self.ui.input_usuario_colaborador_as.text()
        senha = self.ui.input_senha_colaborador_as.text()
        #confirmar_senha = self.ui.input_confirmar_senha_colaborador_as.text()
        perfil = 'non'
        data_login = '2004-06-25'
        status = 'n'

        tupla_login = (login, senha, perfil, data_login, status)

        print(tupla_endereco)
        print(tupla_pessoa)
        print(tupla_colaborador)

        result = self.db.cadastro_colaborador(tupla_endereco,tupla_pessoa,tupla_colaborador,tupla_login)
        print(result)


    def cadastroCurso(self):
        cep = self.ui.input_cep_cursos_as.text()
        rua = self.ui.input_logradouro_cursos_as.text()
        numero = self.ui.input_numero_cursos_as.text()
        bairro = self.ui.input_bairro_cursos_as.text()
        id_cidade=2

        tupla_endereco = (cep,rua,numero,bairro,id_cidade)

        nome_curso=self.ui.input_nome_cursos_as.text()
        data_inicio=self.ui.input_data_inicio_cursos_as.text()
        data_termino=self.ui.input_data_termino_cursos_as.text()
        carga_horaria= 120 
        id_palestrante = 1
        periodo=self.ui.input_periodo_cursos_as.currentText()
        data_inclusao=self.ui.input_data_inclusao_cursos_as.text()
        tipo_curso=self.ui.input_tipo_cursos_as.currentText()
        if self.ui.input_ativo_cursos_as.isChecked():
            situacao="Ativo"
        else:
            situacao="Inativo"
        responsavel=self.ui.input_responsavel_cursos_as.text()
        horario_inicial=self.ui.input_horario_cursos_as.text()
        horario_final=self.ui.input_as_cursos_as.text()
        vagas=self.ui.input_vagas_cursos_as.text()
        
        tupla_curso=(nome_curso,data_inicio,data_termino,carga_horaria,id_palestrante,periodo,data_inclusao,tipo_curso,responsavel,horario_inicial,horario_final,vagas)

        print(tupla_curso)
        print(tupla_endereco)
        result=self.db.cadastro_curso(tupla_endereco,tupla_curso)

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