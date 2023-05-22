import sys
import requests
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


################Class POPUP USUARIO################

class DialogCadastroUsuarioSucesso(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Cadastro_Conclusao()
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

############################################################

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
        self.ui.btn_cadastrar_alterar_dados_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_agenda_as))


        self.ui.btn_cep_buscar_cuidador_as.clicked.connect(self.validarCep)
        self.ui.btn_cep_buscar_usuario_as.clicked.connect(self.validarCep)
        self.ui.btn_cep_buscar_colaborador_as.clicked.connect(self.validarCep)
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
        self.ui.btn_salvar_as.clicked.connect(self.cadastroCuidador)
        self.ui.btn_concluir_cadastro_colaborador_as.clicked.connect(self.cadastroColaborador)
        self.ui.btn_concluir_cursos_as.clicked.connect(self.cadastroCurso)
    
########################### Validar CEP ###############################
    def validarCep(self):
        cep = ""
        inputCuidador = self.ui.input_cep_cuidador_as.text()
        inputUsuario = self.ui.input_cep_usuario_as.text()
        inputColaborador = self.ui.input_cep_colaborador_as.text()
        sender = self.sender()
        if 'cuidador' in sender.objectName():
            cep = inputCuidador
        elif 'usuario' in sender.objectName():
            cep = inputUsuario
        elif 'colaborador' in sender.objectName():
            cep = inputColaborador
        cep_tratado = str('')
        print(cep)
        for i in cep:
            if(i == "." or i == '-' or i == ' '):
                pass
            else:
                cep_tratado += i   
        cep_tratado = int(cep_tratado)
        print(cep_tratado)
        if 'cuidador' in sender.objectName():
            self.cadastroCuidador(cep_tratado)
        elif 'usuario' in sender.objectName():
            self.cadastroUsuario(cep_tratado)
        elif 'colaborador' in sender.objectName():
            self.cadastroColaborador(cep_tratado)


########################### FUNÇÕES BANCO ###########################
    
    def cadastroUsuario(self, cep_tratado):

        parentesco = self.ui.input_parentesco_cuidador_as.text()
        observacao ='none' #self.ui.input_informacoes_gerais_as.setText()''
        id_matricula = 1
        tupla_cuidador = (parentesco,observacao,id_matricula)

        ################ endereço ##################################

        ##### cep requisição #########
        cep_tratado = cep_tratado
        
        link = f'https://viacep.com.br/ws/{cep_tratado}/json/'
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()

        ##### tratamento da requisição - logradouro #######
        logradouro = dic_requisicao['logradouro']
        self.ui.input_logradouro_usuario_as.setText(str(logradouro))
        rua = self.ui.input_logradouro_usuario_as.text()

        ##### número #############
        numero = self.ui.input_numero_usuario_as.text()

        ##### tratamento da requisição - bairro #######
        bairro = dic_requisicao['bairro']
        self.ui.input_bairro_usuario_as.setText(str(bairro))
        bairro = self.ui.input_bairro_usuario_as.text()

        ##### tratamento da requisição - cidade #######
        cidade = dic_requisicao['localidade']
        self.ui.input_cidade_usuario_as.setText(str(cidade))
        cidade = self.ui.input_cidade_usuario_as.text()


        ##### tratamento da requisição - estado #######        
        estado = dic_requisicao['uf']
        self.ui.input_estado_usuario_as.setText(str(estado))
        estado = self.ui.input_estado_usuario_as.text()

        #irei mudar a tupla com o validador do cep
        tupla_endereco = (cep_tratado,rua,numero,bairro,cidade,estado)

        #######################################################

        nome = self.ui.input_nome_usuario_as.text()
        data_nascimento = '0000-00-00'
        cpf = self.ui.input_cpf_usuario_as.text()
        rg = self.ui.input_rg_usuario_as.text()
        data_emissao = self.ui.input_data_emissao_cuidador_as.text()
        orgao_exp = self.ui.input_orgao_expedidor_usuario_as.text()
        sexo = self.ui.input_sexo_usuario_as.text()
        telefone = self.ui.input_telefone_usuario_as.text()
        email = self.ui.input_email_usuario_as.text()
        escolaridade = self.ui.input_escolaridade_usuario_as.currentText()
        estado_civil = self.ui.input_estado_civil_usuario_as.currentText()

        id_colaborador_resp = 1

        #######################################################
        
        nis = self.ui.input_nis_usuario_as.text()
        cns = self.ui.input_cns_usuario_as.text()
        observacao_ = "OBS"
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

        tupla_pessoa = (nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status,telefone,email,escolaridade,estado_civil,pessoa_deficiencia,id_colaborador_resp)
        result = []
        result = self.db.cadastro_usuario(tupla_endereco,tupla_pessoa,tupla_usuario,tupla_cuidador)
        #print(result)
        #result = []
        self.msg(result[0],result[1])
        
    def cadastroCuidador(self, cep_tratado):

        ########################endereco################################

        ##### cep requisição #########
        cep_tratado = cep_tratado
        
        link = f'https://viacep.com.br/ws/{cep_tratado}/json/'
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()

        ##### tratamento da requisição - logradouro #######
        logradouro = dic_requisicao['logradouro']
        self.ui.input_logradouro_cuidador_as.setText(str(logradouro))
        rua = self.ui.input_logradouro_cuidador_as.text()

        ##### número #############
        numero = self.ui.input_numero_cuidador_as.text()

        ##### tratamento da requisição - bairro #######
        bairro = dic_requisicao['bairro']
        self.ui.input_bairro_cuidador_as.setText(str(bairro))
        bairro = self.ui.input_bairro_cuidador_as.text()

        ##### tratamento da requisição - cidade #######
        cidade = dic_requisicao['localidade']
        self.ui.input_cidade_cuidador_as.setText(str(cidade))
        if(cidade == 'Campo Grande'):
            id_cidade = 1
        else:
            id_cidade = 2

        ##### tratamento da requisição - estado #######        
        estado = dic_requisicao['uf']
        self.ui.input_estado_cuidador_as.setText(str(estado))

        tupla_endereco = (cep_tratado,rua,numero,bairro,id_cidade)

        ######################pessoa####################################
        nome = self.ui.input_nome_cuidador_as.text()
        data_nascimento = '2004-06-25'
        cpf = self.ui.input_cpf_cuidador_as.text()
        rg = self.ui.input_rg_cuidador_as.text()
        data_emissao = '2004-06-25'
        orgao_exp = self.ui.input_orgao_expedidor_cuidador_as.text()
        sexo = self.ui.input_sexo_cuidador_as.text()
        data_cadastro = '2004-06-25'
        telefone = self.ui.input_telefone_cuidador_as.text()
        email = self.ui.input_email_cuidador_as.text()  
        escolaridade = self.ui.input_escolaridade_colaborador_comboBox_as.currentText()     

        tupla_pessoa = (nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,data_cadastro,telefone,email,escolaridade)
        

        #############################cuidador#############################################3

        parentesco = self.ui.input_parentesco_cuidador_as.text()
        observacao = 'none' #self.ui.input_informacoes_gerais_as.setText()''
        tupla_cuidador = (parentesco,observacao)

        ##############################insert#######################################
        result = []
        result = self.db.cadastro_cuidador(tupla_endereco,tupla_pessoa,tupla_cuidador)
        #print(result)

    def cadastroColaborador(self, cep_tratado):


        ######################## endereco ###########################

        ##### cep requisição #########
        cep_tratado = cep_tratado
        link = f'https://viacep.com.br/ws/{cep_tratado}/json/'
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()

        ##### tratamento da requisição - logradouro #######
        logradouro = dic_requisicao['logradouro']
        self.ui.input_logradouro_colaborador_as.setText(str(logradouro))
        rua = self.ui.input_logradouro_colaborador_as.text()

        ##### número #############
        numero = self.ui.input_numero_colaborador_as.text()

        ##### tratamento da requisição - bairro #######
        bairro = dic_requisicao['bairro']
        self.ui.input_bairro_colaborador_as.setText(str(bairro))
        bairro = self.ui.input_bairro_colaborador_as.text()

        ##### tratamento da requisição - cidade #######
        cidade = dic_requisicao['localidade']
        self.ui.input_cidade_colaborador_as.setText(str(cidade))
        if(cidade == 'Campo Grande'):
            id_cidade = 1
        else:
            id_cidade = 2

        ##### tratamento da requisição - estado #######        
        estado = dic_requisicao['uf']
        self.ui.input_estado_colaborador_as.setText(str(estado))
        
        tupla_endereco = (cep_tratado,rua,numero,bairro,id_cidade)

        ####################################################
        nome = self.ui.input_nome_colaborador_as.text()
        data_nascimento = '00/00/0000'
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
        data_admissao = '2023-00-00'
        pis_colab = self.ui.input_pis_colaborador_as.text()
        periodo = self.ui.input_periodo_colaborador_comboBox_as.currentText()
        cargo = self.ui.input_cargo_colaborador_comboBox_as.currentText() ##### ADDDDDD NO CÓDIGO
        descricao_cargo = self.ui.input_descricao_cargo_colaborador_as.text()
        

        ##########################################################################

        login = self.ui.input_usuario_colaborador_as.text()
        senha = self.ui.input_senha_colaborador_as.text()
        #confirmar_senha = self.ui.input_confirmar_senha_colaborador_as.text()
        perfil = 'adm'
        ##ALTERAÇÃO PARA CADASTRAR COLABORADOR
        tupla_colaborador = (pis_colab,data_admissao,salario,cargo,periodo,login,senha,perfil,descricao_cargo)
        result = []
        result = self.db.cadastro_colaborador(tupla_endereco,tupla_pessoa,tupla_colaborador)
        #print(result)
        self.msg(result[0],result[1])        


    def cadastroCurso(self):
      ################################################ENDERECO#####
        cep = self.ui.input_cep_usuario_as.text()
        rua = self.ui.input_logradouro_usuario_as.text()
        numero = self.ui.input_numero_usuario_as.text()
        bairro = self.ui.input_bairro_usuario_as.text()
        cidade = self.ui.input_cidade_usuario_as.text()
        estado = self.ui.input_estado_usuario_as.text()

        tupla_endereco = (cep,rua,numero,bairro,cidade,estado)

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

    def msg(self,tipo,mensagem):
        msg = DialogCadastroUsuarioSucesso(self)
        self.popup.show()
        msg.exec()
        self.popup.hide()
        #self.clean()

    def clean(self):
        self.ui.input_nome_usuario_as.setText("")


        


if __name__ == "__main__":
    
    myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid) 

    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('icons\Abrec logo paint-02 (2).png'))

    w = TelaPrincipal()
    w.show()
    app.exec()