import sys
import re
import requests
from os import getcwd
from ctypes import windll
from qtcore import *
from ui_telas_abrec import *
from ui_dialog import *
from database import *
import cv2
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import landscape, A4
from openpyxl.styles import Font
import pandas as pd
from reportlab.pdfgen import canvas
import sys
import openpyxl



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
##################LOGIN INVALIDO###################
class DialogloginInvalido(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Login_Ivalido()
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
        self.ui.btn_tirar_foto_popup_foto_as.clicked.connect(self.TirarFotoWeb)
        #self.ui.btn_importar_popup_foto_as.clicked.connect(self.ImportarFoto)
        self.timer_msg = QTimer(self)
        self.timer_msg.setInterval(10000)
        self.timer_msg.timeout.connect(self.closeMsg)
        self.timer_msg.start()   

    def closeMsg(self):
        self.close()

    def closeEvent(self, event):
        self.timer_msg.stop()
        event.accept()
    
    def TirarFotoWeb(self):
        vid = cv2.VideoCapture(0)

        while(True):
            ret, frame = vid.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            cv2.imwrite("capture.png", frame)
        vid.release()
        cv2.destroyAllWindows()


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
        self.saida = Ui_Confirma_Saida()
        self.ui.setupUi(self)
        
        ######################### banco #########################

        self.db = DataBase()        
        self.listarUsuarios()
        self.id_area_sigilosa = self.relatorio_pessoa()
        self.filtrar_usuario_area_sigilosa()
        #self.gerar_excel()
        ########### selected último id das tabelas do banco ##########
        select_usuario = self.db.select_usuario()
        select_cuidador = self.db.select_cuidador()
        selected_colaborador = self.db.select_colaborador()
        ultimo_id_usuario = (select_usuario[0])
        ultimo_id_cuidador = (select_cuidador[0])
        ultimo_id_colaborador = (selected_colaborador[0])
        ultimo_id_usuario = ''.join(map(str, ultimo_id_usuario))
        ultimo_id_cuidador = ''.join(map(str, ultimo_id_cuidador))
        ultimo_id_colaborador = ''.join(map(str, ultimo_id_colaborador))
        proximo_id_usuario = 1 + int(ultimo_id_usuario)
        proximo_id_cuidador = 1 + int(ultimo_id_cuidador)
        proximo_id_colaborador = 1 + int(ultimo_id_colaborador)
        proximo_id_usuario = str(proximo_id_usuario).zfill(4)
        proximo_id_cuidador = str(proximo_id_cuidador).zfill(4)
        proximo_id_colaborador = str(proximo_id_colaborador).zfill(4)

        self.ui.input_matricula_usuario_as.setText(f'{proximo_id_usuario}')
        self.ui.input_matricula_usuario_as.setStyleSheet("color: black; qproperty-alignment: AlignCenter;")
        self.ui.input_matricula_cuidador_as.setText(f'{proximo_id_cuidador}')
        self.ui.input_matricula_cuidador_as.setStyleSheet("color: black; qproperty-alignment: AlignCenter;")
        self.ui.input_matricula_colaborador_as.setText(f'{proximo_id_colaborador}')
        self.ui.input_matricula_colaborador_as.setStyleSheet("color: black; qproperty-alignment: AlignCenter;")


        self.popup = Overlay(self)
        self.popup.setMinimumWidth(1920)
        self.popup.setMinimumHeight(1080)
        self.popup.hide()

        self.showMaximized()

        self.ui.input_senha_login.setEchoMode(QLineEdit.Password)

        ###############SIGNALS################# 
        # self.ui.btn_sair_as.clicked.connect(self.sairSistema)  

        self.ui.btn_entrar_login.clicked.connect(lambda: self.ui.inicio.setCurrentWidget(self.ui.area_principal))
        self.ui.btn_entrar_login.clicked.connect(self.validarLogin)
        
        self.ui.toolButton.clicked.connect(self.visibilidade)        

        
        
        self.ui.btn_cadastrar_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        # self.ui.btn_consulta_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_consulta_as))
        self.ui.btn_consulta_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_consulta))
        self.ui.btn_cadastrar_beneficios_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_beneficios_as))
        self.ui.btn_voltar_cadastro_beneficio.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_parceiros))
        self.ui.btn_cadastrar_cuidador_usuario_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_usuario_as))
        self.ui.btn_proximo_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_cuidador_as))    
        self.ui.btn_cadastrar_cursos_oficinas_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastrar_cursos_e_oficinas_as))
        self.ui.btn_cadastrar_colaborador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_colaborador_as))
        self.ui.btn_relatorios_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_relatorios_as))
        self.ui.btn_agenda_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_agenda_as))
        self.ui.btn_cadastrar_alterar_dados_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_alterar_dados_as))
        self.ui.btn_buscar_alterar_as.clicked.connect(lambda: self.ui.stackedWidget_8.setCurrentWidget(self.buscar_Usuario()))        
        self.ui.btn_observacoes_sigilo_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_observacoes_sigilosas_as))
        self.ui.btn_alterar_observacoes_sigilo_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_observacoes_sigilosas_as))
        self.ui.btn_parceiros_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_parceiros))
        self.ui.btn_voltar_clinica_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_parceiros))
        self.ui.btn_cadastrar_clinica_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_clinica_as))
        #self.ui.input_situacao_trabalho_usuario_as.currentIndexChanged.connect(self.on_tipo_usuario_changed)
        self.ui.input_situacao_trabalho_alterar_usuario_as.currentIndexChanged.connect(self.on_tipo_alterar_usuario_changed)
        self.ui.input_escolha_relatorio_as.currentIndexChanged.connect(self.on_idade_relatorio)
        
        
        
        #self.ui.input_patologia_base_usuario_as.currentIndexChanged.connect(self.on_patologia_base_usuario_changed)


        #################SIGNALS CEP#################
        self.ui.btn_cep_buscar_cuidador_as.clicked.connect(self.validarCep)
        self.ui.btn_cep_buscar_usuario_as.clicked.connect(self.validarCep)
        self.ui.btn_cep_buscar_colaborador_as.clicked.connect(self.validarCep)
        self.ui.btn_cep_buscar_clinica_as.clicked.connect(self.validarCep)


        
        #############SIGNALS BOTOES voltar#############
        #self.self.btn_voltar_popup_as.connect(lambda: self.ui.inicio.setCurrentWidget(self.ui.login))

        self.ui.btn_voltar_cursos_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_voltar_cuidador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_usuario_as))
        self.ui.btn_voltar_agenda_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_principal_as))
        self.ui.btn_voltar_usuario_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_voltar_pagina_consulta_geral.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_principal_as))
        self.ui.btn_alterar_voltar_usuario_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_usuario_as))
        self.ui.btn_voltar_observacoes_sigilosas_as.clicked.connect(lambda: self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_alterar_usuario))
        # page_alterar_usuario
        self.ui.btn_voltar_relatorios_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_voltar_cadastro_colaborador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        

        ######SIGNALS POPUP recuperar senha login######
        self.ui.btn_esqueci_senha_login.clicked.connect(self.recuperarSenha)
        


        ######SIGNALS POPUP trocar foto e senha AS######
        self.ui.btn_alterar_foto_senha_as.clicked.connect(self.trocarFotoSenha)
        
        
        ############SIGNALS POPUP Usuario AS############
        self.ui.btn_foto_usuario_as.clicked.connect(self.tirarFoto)


        ############SIGNALS POPUP Cuidador AS############
        #self.ui.btn_sair_as.clicked.connect(self.sair)
        #mudar tbm
        #self.ui.btn_finalizar_as.clicked.connect(self.concluirCadastroIncompletoUsuario)


        ############SIGNALS POPUP Cursos e oficinas AS############
        self.ui.btn_concluir_cursos_as.clicked.connect(self.cadastroIncompletoCursos)


        ############SIGNALS BANCO ##########################
        self.ui.btn_salvar_usuario_as.clicked.connect(self.cadastroUsuario)
        self.ui.btn_finalizar_as.clicked.connect(self.cadastroCuidador)
        self.ui.btn_concluir_cadastro_colaborador_as.clicked.connect(self.cadastroColaborador)
        # self.filtrar_usuario_area_sigilosa()
        self.ui.btn_concluir_cursos_as.clicked.connect(self.cadastroCurso)

        self.ui.btn_alterar_salvar_as.clicked.connect(self.atualizar_cuidador)
        self.ui.btn_alterar_finalizar_as.clicked.connect(self.atualizar_usuario)
        self.ui.btn_alterar_concluir_cadastro_colaborador_as.clicked.connect(self.atualizar_colaborador)
        self.ui.btn_salvar_observacoes_sigilosas_as.clicked.connect(self.area_sigilosa)
        self.ui.btn_salvar_observacoes_sigilosas_as.clicked.connect(self.filtrar_usuario_area_sigilosa)
        self.ui.btn_alterar_observacoes_sigilo_as.clicked.connect(self.filtrar_usuario_area_sigilosa)
        self.ui.btn_salvar_usuario_as.clicked.connect(self.limparCamposCadastroUsuario)
        self.ui.btn_finalizar_as.clicked.connect(self.limparCamposCadastroCuidador)
        self.ui.btn_finalizar_clinica_as.clicked.connect(self.cadastro_clinica)       
        self.ui.btn_concluir_cadastro_colaborador_as.clicked.connect(self.limparCamposCadastroColaborador)
        self.ui.btn_salvar_observacoes_sigilosas_as.clicked.connect(self.limparCamposAreaSigilosa)
        self.ui.input_buscar_dados_relatorio_as.textChanged.connect(self.filtrar_dados)
        
        self.ui.btn_gerar_excel_relatorio_as.clicked.connect(self.gerar_excel)
        
        self.ui.btn_buscar_relatorio_as.clicked.connect(self.filtrar_data)
        
        self.ui.btn_buscar_relatorio_as.clicked.connect(self.filter_idade)
        
        self.ui.btn_gerar_pdf_relatorio_as.clicked.connect(self.gerar_pdf)


########################### Validar Login #############################
    def validarLogin(self):
        login = self.ui.input_usuario_login.text()
        senha = self.ui.input_senha_login.text()
        login_senha = []
        login_senha = self.db.validarLogin(login,senha)
        if len(login_senha)==0:
            print ("login vazio")           
            self.ui.inicio.setCurrentWidget(self.ui.login)
            self.loginIvalido()


        elif login_senha[0][0] == login_senha[0][1]:
                print("Login e senha não podem ser iguais")
        else:

            if login == login_senha[0][0] and senha == login_senha[0][1]:            
                print ("Login realizado com sucesso")          
            else:
                print ("Usuário não encontrado")
        
        
        
        
########################### Validar CEP ###############################
    def validarCep(self):
        cep = ""
        inputCuidador = self.ui.input_cep_cuidador_as.text()
        inputUsuario = self.ui.input_cep_usuario_as.text()
        inputColaborador = self.ui.input_cep_colaborador_as.text()
        inputClinica = self.ui.input_cep_clinica_as.text()
        sender = self.sender()
        if 'cuidador' in sender.objectName():
            cep = inputCuidador
        elif 'usuario' in sender.objectName():
            cep = inputUsuario
        elif 'colaborador' in sender.objectName():
            cep = inputColaborador
        elif 'clinica' in sender.objectName():
            cep = inputClinica
        cep_tratado = str('')
        print(cep)
        for i in cep:
            if(i == "." or i == '-' or i == ' '):
                pass
            else:
                cep_tratado += i   
        cep_tratado = int(cep_tratado)
        print(cep_tratado)
        self.puxarCep(cep_tratado, sender)

############################## puxar cep e 'setar' nos inputs ########################
    def puxarCep(self, cep_tratado, sender):
        cep_tratado = cep_tratado
        sender = self.sender()
        print(cep_tratado)
        link = f'https://viacep.com.br/ws/{cep_tratado}/json/'
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        print(dic_requisicao)
        if 'cuidador' in sender.objectName():
            print("entrou cuidador!")
             ##### tratamento da requisição - logradouro #######
            logradouro = dic_requisicao['logradouro']
            self.ui.input_logradouro_cuidador_as.setText(str(logradouro))

            ##### tratamento da requisição - bairro #######
            bairro = dic_requisicao['bairro']
            self.ui.input_bairro_cuidador_as.setText(str(bairro))

            ##### tratamento da requisição - cidade #######
            cidade = dic_requisicao['localidade']
            self.ui.input_cidade_cuidador_as.setText(str(cidade))

            ##### tratamento da requisição - estado #######        
            estado = dic_requisicao['uf']
            self.ui.input_estado_cuidador_as.setText(str(estado))

        elif 'usuario' in sender.objectName():
            print("entrou usuário!")
             ##### tratamento da requisição - logradouro #######
            logradouro = dic_requisicao['logradouro']
            self.ui.input_logradouro_usuario_as.setText(str(logradouro))

            ##### tratamento da requisição - bairro #######
            bairro = dic_requisicao['bairro']
            self.ui.input_bairro_usuario_as.setText(str(bairro))

            ##### tratamento da requisição - cidade #######
            cidade = dic_requisicao['localidade']
            self.ui.input_cidade_usuario_as.setText(str(cidade))

            ##### tratamento da requisição - estado #######        
            estado = dic_requisicao['uf']
            self.ui.input_estado_usuario_as.setText(str(estado))

        elif 'colaborador' in sender.objectName():
            print("entrou colaborador!")
             ##### tratamento da requisição - logradouro #######
            logradouro = dic_requisicao['logradouro']
            self.ui.input_logradouro_colaborador_as.setText(str(logradouro))

            ##### tratamento da requisição - bairro #######
            bairro = dic_requisicao['bairro']
            self.ui.input_bairro_colaborador_as.setText(str(bairro))

            ##### tratamento da requisição - cidade #######
            cidade = dic_requisicao['localidade']
            self.ui.input_cidade_colaborador_as.setText(str(cidade))

            ##### tratamento da requisição - estado #######        
            estado = dic_requisicao['uf']
            self.ui.input_estado_colaborador_as.setText(str(estado))
        
        elif 'clinica' in sender.objectName():
            print("entrou clinica!")
             ##### tratamento da requisição - logradouro #######
            logradouro = dic_requisicao['logradouro']
            self.ui.input_logradouro_clinica_as.setText(str(logradouro))

            ##### tratamento da requisição - bairro #######
            bairro = dic_requisicao['bairro']
            self.ui.input_bairro_clinica_as.setText(str(bairro))

            ##### tratamento da requisição - cidade #######
            cidade = dic_requisicao['localidade']
            self.ui.input_cidade_clinica_as.setText(str(cidade))

            ##### tratamento da requisição - estado #######        
            estado = dic_requisicao['uf']
            self.ui.input_estado_clinica_as.setText(str(estado))

########################### FUNÇÕES BANCO ###########################

    def buscar_Usuario(self):


        valorSelecionado = self.ui.comboBox_tipos_alterar_cadastros_as.currentIndex()
        cpf = self.ui.lineEdit_alterar_buscar_cpf_cnpj_as.text()
        print("Valor selecionado:", valorSelecionado)

        if valorSelecionado == 0:
            return self.ui.page_2
        ############################CUIDADOR FUNCIONANDO#################################
        elif valorSelecionado == 1: 
            print(cpf)
            dados = self.db.busca_cuidador(cpf)
            
            print(dados)
            self.ui.input_alterar_matricula_cuidador_as.setText(str(dados[0]))
            self.ui.input_alterar_nome_cuidador_as.setText(dados[1])
            self.ui.input_alterar_cpf_cuidador_as.setText(dados[2])
            self.ui.input_alterar_rg_cuidador_as.setText(dados[3])
            self.ui.input_alterar_data_emissao_cuidador_as.setDate(QDate(dados[4]))
            self.ui.input_alterar_orgao_expedidor_cuidador_as.setText(dados[5])

            sexo = str(dados[6])
            if sexo == 'Masculino':
                self.ui.input_alterar_sexo_cuidador_as.setCurrentIndex(1)
            elif sexo == 'Feminino':
                self.ui.input_alterar_sexo_cuidador_as.setCurrentIndex(2)

            self.ui.input_alterar_parentesco_cuidador_as.setText(dados[7])  
            self.ui.input_alterar_informacoes_gerais_as.setHtml(dados[8])
            self.ui.input_alterar_telefone_cuidador_as.setText(dados[9]) 
            self.ui.input_alterar_email_cuidador_as.setText(dados[10]) 
            self.ui.input_alterar_cep_cuidador_as.setText(dados[11]) 
            self.ui.input_alterar_logradouro_cuidador_as.setText(dados[12]) 
            self.ui.input_alterar_numero_cuidador_as.setText(str(dados[13])) 
            self.ui.input_alterar_bairro_cuidador_as.setText(str(dados[14]))
            self.ui.input_alterar_cidade_cuidador_as.setText(dados[15])
            self.ui.input_alterar_estado_cuidador_as.setText(dados[16])
            self.ui.input_alterar_id_endereco_cuidador_as.setText(str(dados[17]))
            self.ui.input_alterar_id_endereco_cuidador_as.hide()
            self.ui.input_alterar_id_matricula_cuidador_as.setText(str(dados[18]))
            self.ui.input_alterar_id_matricula_cuidador_as.hide()
            
            return self.ui.page_alterar_cuidador
        ##################################################################################



        #######################USUARIO####################################################

        elif valorSelecionado == 2:
            print ('to funfando == 2\n')
            dados = self.db.busca_usuario(cpf)
            print(dados)
        
            
            self.ui.input_alterar_matricula_usuario_as.setText(str(dados[0])) #
            self.id_area_sigilosa = str(dados[0])#
            self.ui.input_alterar_nome_usuario_as.setText(dados[1]) #
            self.ui.input_alterar_nascimento_usuario_as.setDate(QDate(dados[2]))
            self.ui.input_alterar_situacao_inativo_usuario_as.setChecked(bool(dados[3]))
            self.ui.input_situacao_ativo_usuario_as.setChecked(bool(dados[3]))
            self.ui.input_alterar_cpf_usuario_as.setText(str(dados[4]))
            self.ui.input_alterar_rg_usuario_as.setText(dados[5]) #
            self.ui.input_alterar_data_emissao_usuario_as.setDate(QDate(dados[6])) #
            self.ui.input_alterar_orgao_expedidor_usuario_as.setText(dados[7]) #
            self.ui.input_alterar_nis_usuario_as.setText(dados[8]) #
            self.ui.input_alterar_cns_usuario_as.setText(dados[9]) #
            sexo = dados[10]
            if sexo == 'Masculino':
                self.ui.input_alterar_sexo_usuario_as.setCurrentIndex(1)
            elif sexo == 'Feminino':
                self.ui.input_alterar_sexo_usuario_as.setCurrentIndex(2)
            self.ui.input_alterar_telefone_usuario_as.setText(dados[11]) #
            self.ui.input_alterar_email_usuario_as.setText(dados[12]) #
            self.ui.input_alterar_cep_usuario_as.setText(dados[13]) #
            self.ui.input_alterar_logradouro_usuario_as.setText(dados[14]) #
            self.ui.input_alterar_numero_usuario_as.setText(str(dados[15])) #
            self.ui.input_alterar_bairro_usuario_as.setText(str(dados[16])) #
            self.ui.input_alterar_cidade_usuario_as.setText(dados[17]) #
            self.ui.input_alterar_estado_usuario_as.setText(dados[18])

            estadoCivil = str(dados[19]) #
            if estadoCivil == 'Solteiro':
                self.ui.input_alterar_estado_civil_usuario_as.setCurrentIndex(1)

            elif estadoCivil == 'Casado':
                self.ui.input_alterar_estado_civil_usuario_as.setCurrentIndex(2)

            elif estadoCivil == 'Divorciado':
                self.ui.input_alterar_estado_civil_usuario_as.setCurrentIndex(3)
            
            elif estadoCivil == 'Viúvo':
                self.ui.input_alterar_estado_civil_usuario_as.setCurrentIndex(4)

            elif estadoCivil == 'Separado':
                self.ui.input_alterar_estado_civil_usuario_as.setCurrentIndex(5)

            Escolaridade = str(dados[20])
            if Escolaridade == 'Fundamental':
                self.ui.input_alterar_escolaridade_usuario_comboBox_as.setCurrentIndex(1)
            
            elif Escolaridade == 'Fundamental incompleto':
                self.ui.input_alterar_escolaridade_usuario_comboBox_as.setCurrentIndex(2)
            
            elif Escolaridade == 'Médio':
                self.ui.input_alterar_escolaridade_usuario_comboBox_as.setCurrentIndex(3)

            elif Escolaridade == 'Médio imcompleto':
                self.ui.input_alterar_escolaridade_usuario_comboBox_as.setCurrentIndex(4)

            elif Escolaridade == 'Superior completo':
                self.ui.input_alterar_escolaridade_usuario_comboBox_as.setCurrentIndex(5)
            
            elif Escolaridade == 'Superior incompleto':
                self.ui.input_alterar_escolaridade_usuario_comboBox_as.setCurrentIndex(6)


            self.ui.input_pessoa_cdeficiencia_sim_usuario_as.setChecked(bool(dados[21]))
            self.ui.label_alterar_pessoa_cdeficiencia_nao_usuario_as.setChecked(bool(dados[21]))

            tipoDeDeficiencia = str(dados[22])

            if tipoDeDeficiencia == 'Visual':
                self.ui.input_alterar_tipo_deficiencia_usuario_as.setCurrentIndex(1)
            
            elif tipoDeDeficiencia == 'Motora':
                self.ui.input_alterar_tipo_deficiencia_usuario_as.setCurrentIndex(2)

            elif tipoDeDeficiencia == 'Amputada':
                self.ui.input_alterar_tipo_deficiencia_usuario_as.setCurrentIndex(3)

            elif tipoDeDeficiencia == 'Mental':
                self.ui.input_alterar_tipo_deficiencia_usuario_as.setCurrentIndex(4)

            elif tipoDeDeficiencia == 'Outra':
                self.ui.input_alterar_tipo_deficiencia_usuario_as.setCurrentIndex(5)

            mediaRendaFamiliar = str(dados[23])

            if mediaRendaFamiliar == 'Menos 1 salário':
                self.ui.input_alterar_renda_familiar_usuario_as.setCurrentIndex(1)

            elif mediaRendaFamiliar == '1 salário':
                self.ui.input_alterar_renda_familiar_usuario_as.setCurrentIndex(2)

            elif mediaRendaFamiliar == 'Mais de 1 a 3 salários':
                self.ui.input_alterar_renda_familiar_usuario_as.setCurrentIndex(3)

            elif mediaRendaFamiliar == 'Mais que 3 salários':
                self.ui.input_alterar_renda_familiar_usuario_as.setCurrentIndex(4)

            meioTransporte = str(dados[24])

            if meioTransporte == 'Particular':
                self.ui.input_alterar_meio_transporte_usuario_as.setCurrentIndex(1)

            elif meioTransporte == 'Carona':
                self.ui.input_alterar_meio_transporte_usuario_as.setCurrentIndex(2)

            elif meioTransporte == 'Ônibus coletivo':
                self.ui.input_alterar_meio_transporte_usuario_as.setCurrentIndex(3)

            elif meioTransporte == 'Ambulância municipal':
                self.ui.input_alterar_meio_transporte_usuario_as.setCurrentIndex(3)

            elif meioTransporte == 'Moto':
                self.ui.input_alterar_meio_transporte_usuario_as.setCurrentIndex(4)

            elif meioTransporte == 'Ambulância particular':
                self.ui.input_alterar_meio_transporte_usuario_as.setCurrentIndex(5)

            elif meioTransporte == 'Outro':
                self.ui.input_alterar_meio_transporte_usuario_as.setCurrentIndex(6)

            valeTransporte = str(dados[25])

            if valeTransporte == 'Passe para os dias de tratamento':
                self.ui.input_alterar_vale_transporte_usuario_as.setCurrentIndex(1)

            elif valeTransporte == 'Passe do idoso':
                self.ui.input_alterar_vale_transporte_usuario_as.setCurrentIndex(2)

            elif valeTransporte == 'Passe livre':
                self.ui.input_alterar_vale_transporte_usuario_as.setCurrentIndex(3)

            situacaoTrabalho = str(dados[26])

            if situacaoTrabalho == 'Aposentado por Idade':
                self.ui.input_situacao_trabalho_alterar_usuario_as.setCurrentIndex(1)

            elif situacaoTrabalho == 'Aposentado tempo de serviço':
                self.ui.input_situacao_trabalho_alterar_usuario_as.setCurrentIndex(2)

            elif situacaoTrabalho == 'Aposentado invalidez':
                self.ui.input_situacao_trabalho_alterar_usuario_as.setCurrentIndex(3)

            elif situacaoTrabalho == 'Empregado/a Autônomo/a':
                self.ui.input_situacao_trabalho_alterar_usuario_as.setCurrentIndex(4)

            elif situacaoTrabalho == 'Aposentado/a':
                self.ui.input_situacao_trabalho_alterar_usuario_as.setCurrentIndex(5)

            elif situacaoTrabalho == 'Pensionista':
                self.ui.input_alterar_situacao_trabalho_usuario_as.setCurrentIndex(6)

            elif situacaoTrabalho == 'Desempregado/a':
                self.ui.input_situacao_trabalho_alterar_usuario_as.setCurrentIndex(7)

            elif situacaoTrabalho  == 'Auxílio doença':
                self.ui.input_situacao_trabalho_alterar_usuario_as.setCurrentIndex(8)

            elif situacaoTrabalho == 'Outros':
                self.ui.input_situacao_trabalho_alterar_usuario_as.setCurrentIndex(9)

            beneficio = str(dados[27])

            if beneficio == 'BPC/Idoso':
                self.ui.input_alterar_beneficios_usuario_as.setCurrentIndex(1)

            elif beneficio == 'BPC/PCD':
                self.ui.input_alterar_beneficios_usuario_as.setCurrentIndex(2)

            elif beneficio == 'Mais Social (Gov. Estadual)':
                self.ui.input_alterar_beneficios_usuario_as.setCurrentIndex(3)

            elif beneficio == 'Auxílio Brasil (Gov. Federal)':
                self.ui.input_alterar_beneficios_usuario_as.setCurrentIndex(4)
    
            self.ui.input_alterar_tarifa_social_sim_usuario_as.setChecked(bool(dados[28]))
            self.ui.input_alterar_tarifa_social_nao_usuario_as.setChecked(bool(dados[28]))


            tipoTratamento = str(dados[29])

            if tipoTratamento == 'Pré-Diálise':
                self.ui.input_alterar_tipo_tratamento_usuario_as.setCurrentIndex(1)
            
            elif tipoTratamento == 'Hemodiálise':
                self.ui.input_alterar_tipo_tratamento_usuario_as.setCurrentIndex(2)

            elif tipoTratamento == 'Diálise Peritoneal':
                self.ui.input_alterar_tipo_tratamento_usuario_as.setCurrentIndex(3)

            self.ui.input_alterar_local_tratamento_usuario_as.setText(dados[30])

            patologiaBase = dados[31]

            if patologiaBase == 'Hipertensão':
                self.ui.input_alterar_patologia_base_usuario_as.setCurrentIndex(1)

            elif patologiaBase == 'Diabete 1':
                self.ui.input_alterar_patologia_base_usuario_as.setCurrentIndex(2)

            elif patologiaBase == 'Diabete 2':
                self.ui.input_alterar_patologia_base_usuario_as.setCurrentIndex(3)

            elif patologiaBase == 'Lúpus':
                self.ui.input_alterar_patologia_base_usuario_as.setCurrentIndex(4)

            elif patologiaBase == 'Nefrites':
                self.ui.input_alterar_patologia_base_usuario_as.setCurrentIndex(5)

            elif patologiaBase == 'Outros':
                self.ui.input_alterar_patologia_base_usuario_as.setCurrentIndex(6)

            self.ui.input_alterar_data_inicio_usuario_as.setDate(QDate(dados[32]))

            periodo = dados[33]

            if periodo == 'Matutino':
                self.ui.input_alterar_periodo_usuario_as.setCurrentIndex(1)

            elif periodo == 'Vespertino':
                self.ui.input_alterar_periodo_usuario_as.setCurrentIndex(2)

            elif periodo == 'Noturno':
                self.ui.input_alterar_periodo_usuario_as.setCurrentIndex(3)
            self.ui.input_alterar_id_endereco_usuario_as.setText(str(dados[34]))
            self.ui.input_alterar_id_endereco_usuario_as.hide()
            self.ui.input_alterar_id_matricula_usuario_as.setText(str(dados[35]))
            self.ui.input_alterar_id_matricula_usuario_as.hide()
            return self.ui.page_alterar_usuario
        
        ##################################################################################




        if valorSelecionado == 3:
            dados = self.db.busca_colaborador(cpf)
            print(dados)
            self.ui.input_alterar_matricula_colaborador_as.setText(str(dados[0]))#
            self.ui.input_alterar_nome_colaborador_as.setText(dados[1])
            self.ui.input_alterar_data_nascimento_colaborador_as.setDate(QDate(dados[2]))
            self.ui.input_alterar_cpf_colaborador_as.setText(dados[3]) #
            self.ui.input_alterar_rg_colaborador_as.setText(dados[4]) #
            self.ui.input_alterar_situacao_ativo_colaborador_as.setChecked(bool(dados[5]))
            self.ui.input_alterar_situacao_inativo_colaborador_as.setChecked(bool(dados[5]))
            self.ui.input_alterar_orgao_expedidor_colaborador_as.setText(str(dados[6]))
            self.ui.input_alterar_data_emissao_rg_colaborador_as.setText(str(dados[7]))
            self.ui.input_alterar_pis_colaborador_as.setText(dados[8])

            sexo = str(dados[9]) 
            if sexo == 'Masculino':
                self.ui.input_alterar_sexo_colaborador_comboBox_as.setCurrentIndex(1)
            elif sexo == 'Feminino':
                self.ui.input_alterar_sexo_colaborador_comboBox_as.setCurrentIndex(2)

            self.ui.input_alterar_telefone_colaborador_as.setText(dados[10])
            self.ui.input_alterar_email_colaborador_as.setText(dados[11])
            self.ui.input_alterar_cep_colaborador_as.setText(dados[12])
            self.ui.input_alterar_logradouro_colaborador_as.setText(str(dados[13]))
            self.ui.input_alterar_numero_colaborador_as.setText(str(dados[14]))
            self.ui.input_alterar_bairro_colaborador_as.setText(str(dados[15]))
            self.ui.input_alterar_cidade_colaborador_as.setText(str(dados[16]))
            self.ui.input_alterar_estado_colaborador_as.setText(str(dados[17]))

            estadoCivil = str(dados[18]) 
            if estadoCivil == 'Solteiro':
                self.ui.input_alterar_estado_civil_colaborador_comboBox_as.setCurrentIndex(1)

            elif estadoCivil == 'Casado':
                self.ui.input_alterar_estado_civil_colaborador_comboBox_as.setCurrentIndex(2)

            elif estadoCivil == 'Divorciado':
                self.ui.input_alterar_estado_civil_colaborador_comboBox_as.setCurrentIndex(3)
            
            elif estadoCivil == 'Viúvo':
                self.ui.input_alterar_estado_civil_colaborador_comboBox_as.setCurrentIndex(4)

            elif estadoCivil == 'Separado':
                self.ui.input_alterar_estado_civil_colaborador_comboBox_as.setCurrentIndex(5)


            Escolaridade = str(dados[19])
            if Escolaridade == 'Fundamental':
                self.ui.input_alterar_escolaridade_colaborador_comboBox_as.setCurrentIndex(1)
            
            elif Escolaridade == 'Fundamental incompleto':
                self.ui.input_alterar_escolaridade_colaborador_comboBox_as.setCurrentIndex(2)
            
            elif Escolaridade == 'Médio':
                self.ui.input_alterar_escolaridade_colaborador_comboBox_as.setCurrentIndex(3)

            elif Escolaridade == 'Médio imcompleto':
                self.ui.input_alterar_escolaridade_colaborador_comboBox_as.setCurrentIndex(4)

            elif Escolaridade == 'Superior completo':
                self.ui.input_alterar_escolaridade_colaborador_comboBox_as.setCurrentIndex(5)
            
            elif Escolaridade == 'Superior incompleto':
                self.ui.input_alterar_escolaridade_colaborador_comboBox_as.setCurrentIndex(6)

            cargo = str(dados[20])

            if cargo == 'Recepcionista':
                self.ui.input_alterar_cargo_colaborador_comboBox_as.setCurrentIndex(1)

            elif cargo == 'Assistente Social':
                self.ui.input_alterar_cargo_colaborador_comboBox_as.setCurrentIndex(2)

            elif cargo == 'Farmacêutico (a)':
                self.ui.input_alterar_cargo_colaborador_comboBox_as.setCurrentIndex(3)

            elif cargo == 'Psicólogo (a)':
                self.ui.input_alterar_cargo_colaborador_comboBox_as.setCurrentIndex(4)

            elif cargo == 'Fisioterapeuta':
                self.ui.input_alterar_cargo_colaborador_comboBox_as.setCurrentIndex(4)

            elif cargo == 'Nutricionista':
                self.ui.input_alterar_cargo_colaborador_comboBox_as.setCurrentIndex(5)

            periodo = str(dados[21])

            if periodo == 'Matutino':
                self.ui.input_alterar_periodo_colaborador_comboBox_as.setCurrentIndex(1)

            elif periodo == 'Vespertino':
                self.ui.input_alterar_periodo_colaborador_comboBox_as.setCurrentIndex(2)

            elif periodo == 'Noturno':
                self.ui.input_alterar_periodo_colaborador_comboBox_as.setCurrentIndex(3)

            elif periodo == 'Integral':
                self.ui.input_alterar_periodo_colaborador_comboBox_as.setCurrentIndex(4)

            self.ui.input_alterar_salario_colaborador_as_2.setText(str(dados[22]))
            self.ui.input_alterar_usuario_colaborador_as_2.setText(dados[23])
            self.ui.input_alterar_senha_colaborador_as_2.setText(dados[24])
            self.ui.input_alterar_confirmar_senha_colaborador_as_2.setText(dados[25])
            self.ui.input_alterar_id_endereco_colaborador_as.setText(str(dados[26]))
            self.ui.input_alterar_id_endereco_colaborador_as.hide()
            self.ui.input_alterar_id_matricula_colaborador_as.setText(str(dados[27]))
            self.ui.input_alterar_id_matricula_colaborador_as.hide()
            


            return self.ui.page_alterar_colaborador_as
    def atualizar_cuidador(self):
        ######################## endereço ################################
        id_endereco_cuidador = self.ui.input_alterar_id_endereco_cuidador_as.text()
        cep = self.ui.input_alterar_cep_cuidador_as.text()
        rua = self.ui.input_alterar_logradouro_cuidador_as.text()
        numero = self.ui.input_alterar_numero_cuidador_as.text()
        bairro = self.ui.input_alterar_bairro_cuidador_as.text()
        cidade = self.ui.input_alterar_cidade_cuidador_as.text()
        estado = self.ui.input_alterar_estado_cuidador_as.text()

        tupla_endereco = (id_endereco_cuidador,cep,rua,numero,bairro,cidade,estado)

        ###################### pessoa ####################################
        id_matricula = self.ui.input_alterar_matricula_cuidador_as.text()
        nome = self.ui.input_alterar_nome_cuidador_as.text()
        cpf_temp = self.ui.input_alterar_cpf_cuidador_as.text()
        cpf = re.sub(r'[^\w\s]','',cpf_temp)
        rg = self.ui.input_alterar_rg_cuidador_as.text()
        data_emi = self.ui.input_alterar_data_emissao_cuidador_as.text()
        data_emissao = "-".join(data_emi.split("/")[::-1])
        orgao_exp = self.ui.input_alterar_orgao_expedidor_cuidador_as.text()
        sexo = self.ui.input_alterar_sexo_cuidador_as.currentText()
        telefone = self.ui.input_alterar_telefone_cuidador_as.text()
        email = self.ui.input_alterar_email_cuidador_as.text()  
        tupla_pessoa = (id_matricula,nome,cpf,rg,data_emissao,orgao_exp,sexo,telefone,email)
        

        ################### cuidador ###################################

        parentesco = self.ui.input_alterar_parentesco_cuidador_as.text()
        observacao = self.ui.input_alterar_informacoes_gerais_as.toPlainText()
        id_matricula_cuidador = self.ui.input_alterar_id_matricula_cuidador_as.text()
        tupla_cuidador = (parentesco,observacao,id_matricula_cuidador)

        ################## insert #######################################
        result = self.db.atualizar_cuidador(tupla_cuidador,tupla_pessoa,tupla_endereco)
        print(result)


    def atualizar_usuario(self):

        ################ endereço ##################################
        id_endereco_usuario = self.ui.input_alterar_id_endereco_usuario_as.text()
        cep = self.ui.input_alterar_cep_usuario_as.text()
        rua = self.ui.input_alterar_logradouro_usuario_as.text()
        numero = self.ui.input_alterar_numero_usuario_as.text()
        bairro = self.ui.input_alterar_bairro_usuario_as.text()
        cidade = self.ui.input_alterar_cidade_usuario_as.text()
        estado = self.ui.input_alterar_estado_usuario_as.text()

        #irei mudar a tupla com o validador do cep
        tupla_endereco = (id_endereco_usuario,cep,rua,numero,bairro,cidade,estado)

        ################# pessoa ###################################

        #foto_imagem = self.ui.btn_foto_usuario_as.text()
        id_matricula = self.ui.input_alterar_id_matricula_usuario_as.text()
        nome = self.ui.input_alterar_nome_usuario_as.text()
        data_nasc = self.ui.input_alterar_nascimento_usuario_as.text()
        data_nascimento = "-".join(data_nasc.split("/")[::-1])
        cpf_temp = self.ui.input_alterar_cpf_usuario_as.text()
        cpf = re.sub(r'[^\w\s]','',cpf_temp)
        rg = self.ui.input_alterar_rg_usuario_as.text()
        data_emi = self.ui.input_alterar_data_emissao_usuario_as.text()
        data_emissao = "-".join(data_emi.split("/")[::-1])
        orgao_exp = self.ui.input_alterar_orgao_expedidor_usuario_as.text()
        sexo = self.ui.input_alterar_sexo_usuario_as.currentText()
        telefone = self.ui.input_alterar_telefone_usuario_as.text()
        email = self.ui.input_alterar_email_usuario_as.text()
        escolaridade = self.ui.input_alterar_escolaridade_usuario_comboBox_as.currentText()
        estado_civil = self.ui.input_alterar_estado_civil_usuario_as.currentText()

        ################ tratamento ##################################
        
        nis = self.ui.input_alterar_nis_usuario_as.text()
        cns = self.ui.input_alterar_cns_usuario_as.text()
        observacao_ = "OBS"
        situacao_trabalho = self.ui.input_situacao_trabalho_alterar_usuario_as.currentText()
        tipo_transporte = self.ui.input_alterar_meio_transporte_usuario_as.currentText()
        tipo_tratamento = self.ui.input_alterar_tipo_tratamento_usuario_as.currentText()
        beneficio = self.ui.input_alterar_beneficios_usuario_as.currentText()
        local_tratamento = self.ui.input_alterar_local_tratamento_usuario_as.text()
        patologia_base  = self.ui.input_alterar_patologia_base_usuario_as.currentText()
        data_ini = self.ui.input_alterar_data_inicio_usuario_as.text()
        data_inicio = "-".join(data_ini.split("/")[::-1])
        periodo = self.ui.input_alterar_periodo_usuario_as.currentText()
        media_renda_familiar = self.ui.input_alterar_renda_familiar_usuario_as.currentText()
        vale_transporte = self.ui.input_alterar_vale_transporte_usuario_as.currentText()
        tipo_deficiencia = self.ui.input_alterar_tipo_deficiencia_usuario_as.currentText()


        tarifa_social =  self.ui.input_alterar_tarifa_social_sim_usuario_as.isChecked()


        if self.ui.input_alterar_tarifa_social_sim_usuario_as.isChecked():
            tarifa_social = 'SIM'
        else:
            tarifa_social = 'NÃO'

        if self.ui.input_alterar_pessoa_cdeficiencia_sim_usuario_as.isChecked():
            pessoa_deficiencia = 'SIM'

        else:
            pessoa_deficiencia = 'NÃO'
        
        if self.ui.input_alterar_situacao_ativo_usuario_as.isChecked():
            status = 'Ativo'
        else:
            status = 'Inativo'
        id_matricula_usuario = self.ui.input_alterar_id_matricula_usuario_as.text()

        tupla_pessoa = (id_matricula,nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status,telefone,email,escolaridade,estado_civil,pessoa_deficiencia,tipo_deficiencia)
        tupla_usuario = (nis,cns,observacao_,situacao_trabalho,tipo_transporte,tipo_tratamento,beneficio,local_tratamento,periodo,data_inicio,patologia_base,tarifa_social,media_renda_familiar,vale_transporte,id_matricula_usuario)

        ######################## insert ##################################
        result = []
        result = self.db.atualizar_usuario(tupla_endereco,tupla_pessoa,tupla_usuario)
        print(result)
        

    def atualizar_colaborador(self):
        
        ######################## endereço ###########################
        cep = self.ui.input_alterar_cep_colaborador_as.text()
        rua = self.ui.input_alterar_logradouro_colaborador_as.text()
        numero = self.ui.input_alterar_numero_colaborador_as.text()
        bairro = self.ui.input_alterar_bairro_colaborador_as.text()
        cidade = self.ui.input_alterar_cidade_colaborador_as.text()
        estado = self.ui.input_alterar_estado_colaborador_as.text()
        id_endereco = self.ui.input_alterar_id_endereco_colaborador_as.text()
        tupla_endereco = (id_endereco,cep,rua,numero,bairro,cidade,estado)

        ###################### pessoa ##############################
        id_matricula = self.ui.input_alterar_id_matricula_colaborador_as.text()
        nome = self.ui.input_alterar_nome_colaborador_as.text()
        data_nasc = self.ui.input_alterar_data_nascimento_colaborador_as.text()
        data_nascimento = "-".join(data_nasc.split("/")[::-1])
        cpf_temp = self.ui.input_alterar_cpf_colaborador_as.text()
        cpf = re.sub(r'[^\w\s]','',cpf_temp)
        rg = self.ui.input_alterar_rg_colaborador_as.text()
        data_emi = self.ui.input_alterar_data_emissao_rg_colaborador_as.text()
        data_emissao = "-".join(data_emi.split("/")[::-1])
        orgao_exp = self.ui.input_alterar_orgao_expedidor_colaborador_as.text()
        sexo = self.ui.input_alterar_sexo_colaborador_comboBox_as.currentText()
        telefone = self.ui.input_alterar_telefone_colaborador_as.text()
        email = self.ui.input_alterar_email_colaborador_as.text()      
        escolaridade = self.ui.input_alterar_escolaridade_colaborador_comboBox_as.currentText()
        estado_civil = self.ui.input_alterar_estado_civil_colaborador_comboBox_as.currentText()
        if self.ui.input_alterar_situacao_ativo_colaborador_as.isChecked():
            status = 'Ativo'
        else:
            status = 'Inativo'
        
        

        tupla_pessoa = (id_matricula,nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status,telefone,email,escolaridade,estado_civil)

        ##################### cargo ###########################################

        salario = self.ui.input_alterar_salario_colaborador_as_2.text()
        data_admi = self.ui.input_data_admissao_colaborador_as_5.text()
        data_admissao = "-".join(data_admi.split("/")[::-1])
        pis_colab = self.ui.input_alterar_pis_colaborador_as.text()
        periodo = self.ui.input_alterar_periodo_colaborador_comboBox_as.currentText()
        cargo = self.ui.input_alterar_cargo_colaborador_comboBox_as.currentText() ##### ADDDDDD NO CÓDIGO        

        #################### login e senha ####################################

        login = self.ui.input_alterar_usuario_colaborador_as_2.text()
        senha = self.ui.input_alterar_senha_colaborador_as_2.text()
        # confirmar_senha = self.ui.input_alterar_confirmar_senha_colaborador_as_2.text()
        perfil = self.ui.input_alterar_confirmar_senha_colaborador_as_2.text()
        ##ALTERAÇÃO PARA CADASTRAR COLABORADOR
        tupla_colaborador = (pis_colab,data_admissao,salario,cargo,periodo,login,senha,perfil)

        #################### insert ##########################################
        result = []
        result = self.db.atualizar_colaborador(tupla_colaborador,tupla_pessoa,tupla_endereco)
        print(result)



    
    def cadastroUsuario(self):

        # parentesco = self.ui.input_parentesco_cuidador_as.text()
        # observacao ='none' #self.ui.input_informacoes_gerais_as.setText()''
        # id_matricula = 1
        # tupla_cuidador = (parentesco,observacao,id_matricula)

        ################ endereço ##################################
        cep = self.ui.input_cep_usuario_as.text()
        rua = self.ui.input_logradouro_usuario_as.text()
        numero = self.ui.input_numero_usuario_as.text()
        bairro = self.ui.input_bairro_usuario_as.text()
        cidade = self.ui.input_cidade_usuario_as.text()
        estado = self.ui.input_estado_usuario_as.text()

        #irei mudar a tupla com o validador do cep
        tupla_endereco = (cep,rua,numero,bairro,cidade,estado)

        ################# pessoa ###################################

        #foto_imagem = self.ui.btn_foto_usuario_as.text()
        nome = self.ui.input_nome_usuario_as.text()
        data_nasc = self.ui.input_nascimento_usuario_as.text()
        data_nascimento = "-".join(data_nasc.split("/")[::-1])
        cpf_temp = self.ui.input_cpf_usuario_as.text()
        cpf = re.sub(r'[^\w\s]','',cpf_temp)
        rg = self.ui.input_rg_usuario_as.text()
        data_emi = self.ui.input_data_emissao_usuario_as.text()
        data_emissao = "-".join(data_emi.split("/")[::-1])
        orgao_exp = self.ui.input_orgao_expedidor_usuario_as.text()
        sexo = self.ui.input_sexo_usuario_as.currentText()
        telefone = self.ui.input_telefone_usuario_as.text()
        email = self.ui.input_email_usuario_as.text()
        escolaridade = self.ui.input_escolaridade_usuario_as.currentText()
        estado_civil = self.ui.input_estado_civil_usuario_as.currentText()

        ################ tratamento ##################################
        
        nis = self.ui.input_nis_usuario_as.text()
        cns = self.ui.input_cns_usuario_as.text()
        observacao_ = "OBS"
        situacao_trabalho = self.ui.input_situacao_trabalho_usuario_as.currentText()
        tipo_transporte = self.ui.input_meio_transporte_usuario_as.currentText()
        tipo_tratamento = self.ui.input_tipo_tratamento_usuario_as.currentText()
        beneficio = self.ui.input_beneficios_usuario_as.currentText()
        local_tratamento = self.ui.input_local_tratamento_usuario_as.text()
        patologia_base  = self.ui.input_patologia_base_usuario_as.currentText()
        #outras_patologias = self.ui.input_outras_patologias_usuario_as.text()
       

        
           
        data_ini = self.ui.input_data_inicio_usuario_as.text()
        data_inicio = "-".join(data_ini.split("/")[::-1])
        periodo = self.ui.input_periodo_usuario_as.currentText()
        media_renda_familiar = self.ui.input_renda_familiar_usuario_as.currentText()
        vale_transporte = self.ui.input_vale_transporte_usuario_as.currentText()
        tipo_deficiencia = self.ui.input_tipo_deficiencia_usuario_as.currentText()


        tarifa_social =  self.ui.input_tarifa_social_sim_usuario_as.isChecked()


        if self.ui.input_tarifa_social_sim_usuario_as.isChecked():
            tarifa_social = 'SIM'
        else:
            tarifa_social = 'NÃO'

        if self.ui.input_pessoa_cdeficiencia_sim_usuario_as.isChecked():
            pessoa_deficiencia = 'SIM'

        else:
            pessoa_deficiencia = 'NÃO'
        
        if self.ui.input_situacao_ativo_usuario_as.isChecked():
            status = 'Ativo'
        else:
            status = 'Inativo'

        
        tupla_pessoa = (nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status,telefone,email,escolaridade,estado_civil,pessoa_deficiencia,tipo_deficiencia)
        tupla_usuario = (nis,cns,observacao_,situacao_trabalho,tipo_transporte,tipo_tratamento,beneficio,local_tratamento,periodo,data_inicio,patologia_base,tarifa_social,media_renda_familiar,vale_transporte)

        ######################## insert ##################################
        result = []
        result = self.db.cadastro_usuario(tupla_endereco,tupla_pessoa,tupla_usuario)
        print(result)
        # result = []
        self.msg(result[0],result[1])
    
    def listarUsuarios(self):
        lista_usuarios = self.db.select_usuario_ids()
        nomes = []
        id_usuarios = []
        for i in lista_usuarios:
            id_usuario = i[0]
            id_usuario = str(id_usuario).zfill(4)
            id_matricula = i[1]
            nome = self.db.select_nome_usuario(id_matricula)
            id_usuarios.append(id_usuario)
            nomes.append(nome)
        convertendo_nome = [i[0] for i in nomes]
        convertendo_nome = [i[0] for i in convertendo_nome]
        count = 0
        itens = 1
        while count < len(convertendo_nome):
            self.ui.input_usuario_cuidador_as.setItemText(itens, QCoreApplication.translate("MainWindow", f"{id_usuarios[count]}-{convertendo_nome[count]}", None))
            self.ui.input_usuario_cuidador_as.addItem("")
            itens += 1
            count += 1

    def cadastroCuidador(self):

        ######################## endereço ################################
        cep = self.ui.input_cep_cuidador_as.text()
        rua = self.ui.input_logradouro_cuidador_as.text()
        numero = self.ui.input_numero_cuidador_as.text()
        bairro = self.ui.input_bairro_cuidador_as.text()
        cidade = self.ui.input_cidade_cuidador_as.text()
        estado = self.ui.input_estado_cuidador_as.text()

        tupla_endereco = (cep,rua,numero,bairro,cidade,estado)

        ###################### pessoa ####################################
        nome = self.ui.input_nome_cuidador_as.text()
        data_nasc = self.ui.input_data_emissao_cuidador_as.text()
        data_nascimento = "-".join(data_nasc.split("/")[::-1])
        cpf_temp = self.ui.input_cpf_cuidador_as.text()
        cpf = re.sub(r'[^\w\s]','',cpf_temp)
        rg = self.ui.input_rg_cuidador_as.text()
        data_emi = self.ui.input_data_emissao_cuidador_as.text()
        data_emissao = "-".join(data_emi.split("/")[::-1])
        orgao_exp = self.ui.input_orgao_expedidor_cuidador_as.text()
        sexo = self.ui.input_sexo_cuidador_as.currentText()
        telefone = self.ui.input_telefone_cuidador_as.text()
        email = self.ui.input_email_cuidador_as.text()  
        escolaridade = self.ui.input_escolaridade_colaborador_comboBox_as.currentText()     

        tupla_pessoa = (nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,telefone,email,escolaridade)
        

        ################### cuidador ###################################

        parentesco = self.ui.input_parentesco_cuidador_as.text()
        observacao = self.ui.input_informacoes_gerais_as.toPlainText()
        tupla_cuidador = (parentesco,observacao)

        ################## usuário ####################################
        usuario_nome_id = self.ui.input_usuario_cuidador_as.currentText()
        usuario_nome_id = usuario_nome_id.split("-")
        usuario_id = int(usuario_nome_id[0])

        ################## insert #######################################
        result = []
        result = self.db.cadastro_cuidador(tupla_endereco,tupla_pessoa,tupla_cuidador, usuario_id)
        #print(result)
        self.msg(result[0],result[1])

    def cadastroColaborador(self):

        ######################## endereço ###########################
        cep = self.ui.input_cep_colaborador_as.text()
        rua = self.ui.input_logradouro_colaborador_as.text()
        numero = self.ui.input_numero_colaborador_as.text()
        bairro = self.ui.input_bairro_colaborador_as.text()
        cidade = self.ui.input_cidade_colaborador_as.text()
        estado = self.ui.input_estado_colaborador_as.text()
        
        tupla_endereco = (cep,rua,numero,bairro,cidade,estado)

        ###################### pessoa ##############################
        nome = self.ui.input_nome_colaborador_as.text()
        data_nasc = self.ui.input_data_nascimento_colaborador_as.text()
        data_nascimento = "-".join(data_nasc.split("/")[::-1])
        cpf_temp = self.ui.input_cpf_colaborador_as.text()
        cpf = re.sub(r'[^\w\s]','',cpf_temp)
        rg = self.ui.input_rg_colaborador_as.text()
        data_emi = self.ui.input_data_emissao_rg_colaborador_as.text()
        data_emissao = "-".join(data_emi.split("/")[::-1])
        orgao_exp = self.ui.input_orgao_expedidor_colaborador_as.text()
        sexo = self.ui.input_sexo_colaborador_comboBox_as.currentText()
        telefone = self.ui.input_telefone_colaborador_as.text()
        email = self.ui.input_email_colaborador_as.text()      
        escolaridade = self.ui.input_escolaridade_colaborador_comboBox_as.currentText()
        estado_civil = self.ui.input_estado_civil_colaborador_comboBox_as.currentText()
        if self.ui.input_situacao_ativo_usuario_as.isChecked():
            status = 'Ativo'
        else:
            status = 'Inativo'
        

        tupla_pessoa = (nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status,telefone,email,escolaridade,estado_civil)

        ##################### cargo ###########################################

        salario = self.ui.input_salario_colaborador_as.text()
        data_admi = self.ui.input_data_admissao_colaborador_as_5.text()
        data_admissao = "-".join(data_admi.split("/")[::-1])
        pis_colab = self.ui.input_pis_colaborador_as.text()
        periodo = self.ui.input_periodo_colaborador_comboBox_as.currentText()
        cargo = self.ui.input_cargo_colaborador_comboBox_as.currentText() ##### ADDDDDD NO CÓDIGO
        
        

        #################### login e senha ####################################

        login = self.ui.input_usuario_colaborador_as_2.text()
        senha = self.ui.input_senha_colaborador_as_2.text()
        #confirmar_senha = self.ui.input_confirmar_senha_colaborador_as.text()
        perfil = 'adm'
        ##ALTERAÇÃO PARA CADASTRAR COLABORADOR
        tupla_colaborador = (pis_colab,data_admissao,salario,cargo,periodo,login,senha,perfil)

        #################### insert ##########################################
        result = []
        result = self.db.cadastro_colaborador(tupla_endereco,tupla_pessoa,tupla_colaborador)
        #print(result)
        self.msg(result[0],result[1])        


    def cadastroCurso(self):
      ################################################ENDERECO#####
        
        nome_curso=self.ui.input_nome_cursos_as.text()
        tipo_curso=self.ui.input_tipo_cursos_as.currentText()

        if self.ui.input_ativo_cursos_as.isChecked():
            situacao=1
        if self.ui.input_inativo_cursos_as.isChecked():
            situacao=0

        responsavel=self.ui.input_responsavel_cursos_as.text()
        data_ini_curso=self.ui.input_data_inicio_cursos_as.text()
             
        data_inicio = "-".join(data_ini_curso.split("/")[::-1])
        
        data_ter_curso =self.ui.input_data_termino_cursos_as.text()
        data_termino= "-".join(data_ter_curso.split("/")[::-1])


        
        
        
        periodo=self.ui.input_periodo_cursos_as.currentText()
               
        
        
       # horario_inicial=self.ui.input_horario_inicio_cursos_as.text()

        
        regex = "([01]?[0-9]|2[0-3]):[0-5][0-9]"

        horario_inicial = self.ui.input_horario_inicio_cursos_as.text()
        
         
        #novo_hr_inicial = horario_inicial_str.replace(" PM", ":00")
        
        horario_final = self.ui.input_horario_termino_cursos_as.text()
        

        vagas=self.ui.input_vagas_cursos_as.text()
        descricao = self.ui.input_descricao_atividade_cursos_as.toPlainText()

        
        
        segunda = 1 if self.ui.input_segunda_cursos_as.isChecked() else 0
        terca = 1 if self.ui.input_terca_cursos_as.isChecked() else 0
        quarta = 1 if self.ui.input_quarta_cursos_as.isChecked() else 0
        quinta = 1 if self.ui.input_quinta_cursos_as.isChecked() else 0
        sexta = 1 if self.ui.input_sexta_cursos_as.isChecked() else 0
        sabado = 1 if self.ui.input_sabado_cursos_as.isChecked() else 0
             

        

        

        tupla_curso = (nome_curso, tipo_curso, data_inicio, data_termino, periodo,responsavel, horario_inicial, horario_final, vagas,  segunda, terca, quarta, quinta, sexta, sabado, situacao,descricao)

        print(tupla_curso)
        result=self.db.cadastro_curso(tupla_curso)
        print(result)

    def area_sigilosa(self):

        if self.ui.input_obito_paciente_sim_as.isChecked:
            situacao="Ativo"
        else:
            situacao="Inativo"
        
        observacao_gerais = self.ui.input_observacoes_obs_sigilosas_as.toPlainText()
        tupla_area_sigilosa = (situacao, observacao_gerais, self.id_area_sigilosa)
        result = self.db.cadastrar_area_sigilosa(tupla_area_sigilosa)
        print(result)


    def limparCamposCadastroUsuario (self):
        self.ui.input_nome_usuario_as.setText("") #
        self.ui.input_nascimento_usuario_as.setDate(QDate(2000, 1, 1))
        self.ui.input_situacao_ativo_usuario_as.setCheckable(False)
        self.ui.input_situacao_ativo_usuario_as.setCheckable(True)
        self.ui.input_situacao_inativo_usuario_as.setCheckable(False)
        self.ui.input_situacao_inativo_usuario_as.setCheckable(True)
        self.ui.input_cpf_usuario_as.setText("")
        self.ui.input_rg_usuario_as.setText("")
        self.ui.input_data_emissao_usuario_as.setDate(QDate(2000, 1, 1))
        self.ui.input_orgao_expedidor_usuario_as.setText("")
        self.ui.input_nis_usuario_as.setText("")
        self.ui.input_cns_usuario_as.setText("")
        self.ui.input_sexo_usuario_as.setCurrentIndex(int(0))
        self.ui.input_telefone_usuario_as.setText("")
        self.ui.input_email_usuario_as.setText("")
        self.ui.input_cep_usuario_as.setText("") #
        self.ui.input_logradouro_usuario_as.setText("") #
        self.ui.input_numero_usuario_as.setText("") #
        self.ui.input_bairro_usuario_as.setText("") #
        self.ui.input_cidade_usuario_as.setText("") #
        self.ui.input_estado_usuario_as.setText("") #
        self.ui.input_estado_civil_usuario_as.setCurrentIndex(int(0))
        self.ui.input_escolaridade_usuario_comboBox_as.setCurrentIndex(int(0))
        self.ui.input_pessoa_cdeficiencia_sim_usuario_as.setCheckable(False)
        self.ui.input_pessoa_cdeficiencia_sim_usuario_as.setCheckable(True)
        self.ui.label_pessoa_cdeficiencia_nao_usuario_as.setCheckable(False)  
        self.ui.label_pessoa_cdeficiencia_nao_usuario_as.setCheckable(True)        
        self.ui.input_tipo_deficiencia_usuario_as.setCurrentIndex(int(0))
        self.ui.input_renda_familiar_usuario_as.setCurrentIndex(int(0))
        self.ui.input_meio_transporte_usuario_as.setCurrentIndex(int(0))
        self.ui.input_vale_transporte_usuario_as.setCurrentIndex(int(0))
        self.ui.input_situacao_trabalho_usuario_as.setCurrentIndex(int(0))
        self.ui.input_beneficios_usuario_as.setCurrentIndex(int(0))
        self.ui.input_tarifa_social_sim_usuario_as.setCheckable(False)
        self.ui.input_tarifa_social_sim_usuario_as.setCheckable(True)
        self.ui.input_tarifa_social_nao_usuario_as.setCheckable(False)
        self.ui.input_tarifa_social_nao_usuario_as.setCheckable(True)
        self.ui.input_tipo_tratamento_usuario_as.setCurrentIndex(int(0))
        self.ui.input_local_tratamento_usuario_as.setText("")
        self.ui.input_patologia_base_usuario_as.setCurrentIndex(int(0))
        self.ui.input_data_inicio_usuario_as.setDate(QDate(2000, 1, 1))
        self.ui.input_periodo_usuario_as.setCurrentIndex(int(0))

        

 
    def limparCamposCadastroCuidador(self):
        self.ui.input_nome_cuidador_as.setText("")
        self.ui.input_data_nascimento_cuidador_as.setDate(QDate(2000, 1, 1))
        self.ui.input_cpf_cuidador_as.setText("")
        self.ui.input_rg_cuidador_as.setText("")
        self.ui.input_data_emissao_cuidador_as.setDate(QDate(2000, 1, 1))
        self.ui.input_orgao_expedidor_cuidador_as.setText("")
        self.ui.input_sexo_cuidador_as.setCurrentIndex(int(0))
        self.ui.input_usuario_cuidador_as.setCurrentIndex(int(0))
        self.ui.input_parentesco_cuidador_as.setText("")
        self.ui.input_telefone_cuidador_as.setText("")
        self.ui.input_email_cuidador_as.setText("") 
        self.ui.input_cep_cuidador_as.setText("")
        self.ui.input_logradouro_cuidador_as.setText("")
        self.ui.input_numero_cuidador_as.setText("")
        self.ui.input_bairro_cuidador_as.setText("")
        self.ui.input_cidade_cuidador_as.setText("")
        self.ui.input_estado_cuidador_as.setText("")        
        self.ui.input_informacoes_gerais_as.setHtml("")



    def limparCamposCadastroColaborador(self):
        self.ui.input_nome_colaborador_as.setText("")
        self.ui.input_data_nascimento_colaborador_as.setDate(QDate(2000, 1, 1))
        self.ui.input_cpf_colaborador_as.setText("")
        self.ui.input_rg_colaborador_as.setText("")
        self.ui.input_situacao_ativo_colaborador_as.setCheckable(False)
        self.ui.input_situacao_ativo_colaborador_as.setCheckable(True)
        self.ui.input_situacao_inativo_colaborador_as.setCheckable(False)
        self.ui.input_situacao_inativo_colaborador_as.setCheckable(True)
        self.ui.input_orgao_expedidor_colaborador_as.setText("")
        self.ui.input_data_emissao_rg_colaborador_as.setDate(QDate(2000, 1, 1))
        self.ui.input_pis_colaborador_as.setText("")
        self.ui.input_sexo_colaborador_comboBox_as.setCurrentIndex(int(0))
        self.ui.input_telefone_colaborador_as.setText("")
        self.ui.input_email_colaborador_as.setText("")      
        self.ui.input_cep_colaborador_as.setText("")
        self.ui.input_logradouro_colaborador_as.setText("")
        self.ui.input_numero_colaborador_as.setText("")
        self.ui.input_bairro_colaborador_as.setText("")
        self.ui.input_cidade_colaborador_as.setText("")
        self.ui.input_estado_colaborador_as.setText("")
        self.ui.input_estado_civil_colaborador_comboBox_as.setCurrentIndex(int(0))
        self.ui.input_salario_colaborador_as.setText("")
        self.ui.input_data_admissao_colaborador_as_5.setDate(QDate(2000, 1, 1))
        self.ui.input_escolaridade_colaborador_comboBox_as.setCurrentIndex(int(0))
        self.ui.input_cargo_colaborador_comboBox_as.setCurrentIndex(int(0))
        self.ui.input_periodo_colaborador_comboBox_as.setCurrentIndex(int(0))
        self.ui.input_usuario_colaborador_as_2.setText("")
        self.ui.input_senha_colaborador_as_2.setText("")
        self.ui.input_confirmar_senha_colaborador_as_2.setText("")


    def limparCamposAreaSigilosa(self):
        self.ui.input_obito_paciente_sim_as.setCheckable(False)
        self.ui.input_obito_paciente_sim_as.setCheckable(True)
        self.ui.input_obito_paciente_nao_as.setCheckable(False)
        self.ui.input_obito_paciente_nao_as.setCheckable(True)
        self.ui.input_observacoes_obs_sigilosas_as.setHtml("")

    def limparCamposCadastroClinica(self):
       self.ui.input_cnpj_cadastro_clinica_as.setText("")
       self.ui.input_razao_social_cadastro_clinica_as.setText("")
       self.ui.input_nome_fantasia_cadastro_clinica_as.setText("")
       self.ui.input_telefone_clinica_as.setText("")
       self.ui.input_email_clinica_as.setText("")       
       self.ui.input_cep_clinica_as.setText("")
       self.ui.input_logradouro_clinica_as.setText("")
       self.ui.input_numero_clinica_as.setText("")
       self.ui.input_bairro_clinica_as.setText("")
       self.ui.input_cidade_clinica_as.setText("")
       self.ui.input_estado_clinica_as.setText("")
       self.ui.input_informacoes_gerais_clinica_as.setHtml("")










#####Alterar SITUACAO de Trabalho Outros #########
######################LOGIN INVALIDO POPUP####################
    def loginIvalido(self):       
        msg = DialogloginInvalido(self)
        self.popup.show()
        msg.exec()
        self.popup.hide()


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


           
    

    
    def on_tipo_alterar_usuario_changed(self):

        if self.ui.input_situacao_trabalho_alterar_usuario_as.currentText() == "Outros":
            self.ui.frame_439.setEnabled(True)
            self.ui.frame_439.show()
            self.ui.input_situacao_trabalho_outros_alterar_usuario_as.setEnabled(True)
            self.ui.input_situacao_trabalho_outros_alterar_usuario_as.setStyleSheet("") 
            self.ui.input_situacao_trabalho_outros_alterar_usuario_as.setEnabled(True)
            self.ui.input_situacao_trabalho_outros_alterar_usuario_as.show()
            
        else:
            self.ui.frame_439.hide()
            self.ui.input_situacao_trabalho_outros_alterar_usuario_as.setEnabled(False)
            self.ui.input_situacao_trabalho_outros_alterar_usuario_as.hide()
            self.ui.input_situacao_trabalho_outros_alterar_usuario_as.clear()

    def on_idade_relatorio(self):
        if self.ui.input_escolha_relatorio_as.currentText() == "Faixa etária":
            self.ui.frame_237.setEnabled(True)
            self.ui.frame_237.show()
            self.ui.frame_246.setEnabled(True)
            self.ui.frame_246.show()

            self.ui.input_idade_inicial_relatorio_as.setEnabled(True)
            self.ui.input_idade_inicial_relatorio_as.setStyleSheet("")
            self.ui.input_idade_inicial_relatorio_as.show() 
            
            self.ui.input_idade_final_relatorio_as.setEnabled(True)
            self.ui.input_idade_final_relatorio_as.setStyleSheet("")
            self.ui.input_idade_final_relatorio_as.show()

            texto = "A"
            

            self.ui.label_a_relatorio_as.setEnabled(True)
            self.ui.label_a_relatorio_as.setStyleSheet("")
            self.ui.label_a_relatorio_as.setText(texto)
            self.ui.label_a_relatorio_as.show()

            self.ui.label_idade_relatorio_as.setEnabled(True)
            self.ui.label_idade_relatorio_as.setStyleSheet("")
            self.ui.label_idade_relatorio_as.setText("idade")
            self.ui.label_idade_relatorio_as.show()

        else:
            
            self.ui.input_idade_inicial_relatorio_as.setEnabled(False)
            self.ui.input_idade_inicial_relatorio_as.hide()
            self.ui.input_idade_inicial_relatorio_as.clear()

            
            self.ui.label_a_relatorio_as.setEnabled(False)
            self.ui.label_a_relatorio_as.hide()
            self.ui.label_a_relatorio_as.clear()

            
            self.ui.input_idade_final_relatorio_as.setEnabled(False)
            self.ui.input_idade_final_relatorio_as.hide()
            self.ui.input_idade_final_relatorio_as.clear()

            
            self.ui.label_idade_relatorio_as.setEnabled(False)
            self.ui.label_idade_relatorio_as.hide()
            self.ui.label_idade_relatorio_as.clear()
            self.ui.frame_246.hide()
            self.ui.frame_237.hide()

    def cadastro_clinica(self):

        ######################## endereço ################################
            cep = self.ui.input_cep_clinica_as.text()
            rua = self.ui.input_logradouro_clinica_as.text()
            numero = self.ui.input_numero_clinica_as.text()
            bairro = self.ui.input_bairro_clinica_as.text()
            cidade = self.ui.input_cidade_clinica_as.text()
            estado = self.ui.input_estado_clinica_as.text()

            tupla_endereco = (cep,rua,numero,bairro,cidade,estado)

        ########################## dados ######################################       
            # id_clinica = self.ui.input_codigo_cadastro_clinica_as.text()
            cnpj = self.ui.input_cnpj_cadastro_clinica_as.text()
            razao_social = self.ui.input_razao_social_cadastro_clinica_as.text()
            nome_fantasia = self.ui.input_nome_fantasia_cadastro_clinica_as.text()
            telefone = self.ui.input_telefone_clinica_as.text()
            email = self.ui.input_email_clinica_as.text()
            obs = self.ui.input_informacoes_gerais_clinica_as.toPlainText()

            tupla_clinica = (cnpj,razao_social,nome_fantasia,telefone,email,obs)
            
            result = []
            result=self.db.cadastro_clinica(tupla_endereco,tupla_clinica)
            print(result)
            self.msg(result[0],result[1])
            self.limparCamposCadastroClinica()
            


######################## Patologia base outros################################      
    def on_patologia_base_usuario_changed(self):

        if self.ui.input_patologia_base_usuario_as.currentText() == "Outros":
            self.ui.frame_440.setEnabled(True)
            self.ui.frame_440.show()
            self.ui.input_outras_patologias_usuario_as.setStyleSheet("")  
            self.ui.input_outras_patologias_usuario_as.setEnabled(True)
            self.ui.input_outras_patologias_usuario_as.show()           
        else:
            self.ui.frame_440.hide()
            self.ui.frame_440.setEnabled(False)
            self.ui.input_outras_patologias_usuario_as.hide()
            self.ui.input_outras_patologias_usuario_as.setEnabled(False)
            self.ui.input_outras_patologias_usuario_as.clear()
    ######################################################################


    def relatorio_pessoa(self): #ALIMENTA A TABELA A DE RELATORIO
        
        result = self.db.relatorio_pessoa()

        self.ui.tableWidget_relatorio_as.clearContents()
        self.ui.tableWidget_relatorio_as.setRowCount(len(result))   

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.tableWidget_relatorio_as.setItem(row, column,QTableWidgetItem(str(data)))

                            
    def filtrar_dados(self):
        txt = re.sub('[\W_]+','',self.ui.input_buscar_dados_relatorio_as.text())
        res = self.db.filtrar_relatorio(txt)
        #print(res)

        self.ui.tableWidget_relatorio_as.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.tableWidget_relatorio_as.setItem(row, column, QTableWidgetItem(str(data)))
    
    def filtrar_usuario_area_sigilosa(self):
        result = self.db.filter_usuario_area_sigilosa(self.id_area_sigilosa)
        print(result)
        self.ui.input_TableWidget_observacoes_sigilosas_as.clearContents()
        self.ui.input_TableWidget_observacoes_sigilosas_as.setRowCount(len(result))   

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_observacoes_sigilosas_as.setItem(row, column,QTableWidgetItem(str(data)))
                
                
    def filtrar_data(self): ###DATA NASCIMENTO 
        texto_data_inicio = self.ui.input_inicio_periodo_relatorio_as.text()
        texto_data_final = self.ui.input_final_periodo_relatorio_as.text()
        texto_data_inicio_tratada =  "-".join(texto_data_inicio.split("/")[::-1])
        texto_data_final_tratada =  "-".join(texto_data_final.split("/")[::-1])
        print(texto_data_inicio_tratada,texto_data_final_tratada)
        
        res = self.db.filter_data(texto_data_inicio_tratada,texto_data_final_tratada)
        #print(res)

        self.ui.tableWidget_relatorio_as.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.tableWidget_relatorio_as.setItem(row, column, QTableWidgetItem(str(data)))
        if self.ui.input_inicio_periodo_relatorio_as.text() == "":
            self.filtrar_dados()
        elif self.ui.input_final_periodo_relatorio_as.text() =="":
            self.filtrar_dados()
                
                
    def filter_idade(self):
        # self.ui.input_idade_inicial_relatorio_as.text()
        # self.ui.input_idade_final_relatorio_as.text()
        if self.ui.input_escolha_relatorio_as.currentIndex() == 1:
            texto_idade_inicio = 18
            texto_idade_final = 23
            print(texto_idade_inicio,texto_idade_final)
            
            res = self.db.filter_idade(texto_idade_inicio,texto_idade_final)
            self.ui.tableWidget_relatorio_as.setRowCount(len(res))

            for row, text in enumerate(res):
                for column, data in enumerate(text):
                    self.ui.tableWidget_relatorio_as.setItem(row, column, QTableWidgetItem(str(data)))
        elif self.ui.input_escolha_relatorio_as.currentIndex() == 0:
            self.filtrar_dados()
                
       
       
    def gerar_excel(self):
        dados = []
        all_dados =  []

        for row in range(self.ui.tableWidget_relatorio_as.rowCount()):
            for column in range(self.ui.tableWidget_relatorio_as.columnCount()):
                dados.append(self.ui.tableWidget_relatorio_as.item(row, column).text())
        
            all_dados.append(dados)
            dados = []

        columns = ['NOME', 'CPF', 'SEXO', 'TELEFONE', 'BENEFICIO', 'CNS', 'NIS',
            'LOCAL DE TRATAMENTO','SITUAÇÃO DE TRABALHO','CLINICA','BAIRRO','CIDADE']
        
        relatorio = pd.DataFrame(all_dados, columns= columns)
        
        #file, _ = QFileDialog.getSaveFileName(self, "Selecionar pasta de saida", "/relatorio", "Text files (*.xlsx)") 
        relatorio.to_excel("Relatorio.xlsx", sheet_name='relatorio', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()
        
    def gerar_pdf(self):
        #pegando o nome das colunas da tabela
        column_names = []
        for col in range(self.ui.tableWidget_relatorio_as.columnCount()):
            column_names.append(self.ui.tableWidget_relatorio_as.horizontalHeaderItem(col).text())

        #criando o pdf e escolhendo a fonte
        pdf = canvas.Canvas("relatorioPDF.pdf")
        pdf.setFont("Times-Roman", 9)

        #pegando os dados de cada linha da tabela
        filtered_data = []
        
        for row in range(self.ui.tableWidget_relatorio_as.rowCount()):
            if not self.ui.tableWidget_relatorio_as.isRowHidden(row):
                row_data = [self.ui.tableWidget_relatorio_as.item(row, col).text() for col in range(self.ui.tableWidget_relatorio_as.columnCount())]
                filtered_data.append(row_data)
        print(filtered_data)        
        #por exemplo: print(filter_data)
        #saida: lista de linhas da tabela
        """[['Calebe Pereira Lemos', '8932728', 'Ouvidor', '728', 'Cidade', 'Lagos', 'calebe.el@senc.ms', '67828293'], 
        ['Pedro', '838443', 'ouvi', '44', 'iijo', '', 'dasdas@', '672838'], 
        ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c'], 
        ['c', '1', 'c', 'c', 'c', 'c', 'c', 'c'], 
        ['c', '4', 'c', 'c', 'c', 'c', 'c', 'c'], 
        ['calebe', '29718', 'ouvidor', '672', 'cailar', 'cg', 'casbh!@fmail', '217267'], 
        ['eder', '7364', 'test', '67', 'ht', 'campo gran', 'asdbahs@gmail', '6791828'], 
        ['lucas', '0989', 'c', 'c', 'c', 'c', 'c', 'c'], 
        ['oliver', '2763173', '65', '176', 'caiçara', 'campo grande', 'oli@senac', '56888'], 
        ['test', '99089', 'tes', '653', 'rr', '', 'c@hmmn', '75676']]"""
    
        y_linha = 798 #y = 798 é o topo da folha segundo o plano cartesiano, então se x=0 e y=0 é o final da folha
        pdf.drawString(285, 820, "Relatório") #cabecalho do relatorio
        for linha in filtered_data:
            i=0 #definido para andar na lista de nomes das colunas
            for col in linha:
                if y_linha == 38: #se chegar ao final da folha, add uma nova
                    pdf.showPage() #adicionar nova folha
                    y_linha = 795 #topo da folha
                pdf.drawString(6, y_linha, column_names[i]+':') #escrever nome da coluna
                pdf.drawString(100, y_linha, '' + col) #escrever dado da coluna     
                y_linha-=20 #decrevementar y, para ir para prox linha
                i+=1 #incrementar i para pegar nome da prox coluna da tabela
            pdf.line(0, y_linha+15, 1000, y_linha+15) #desenhar linha para separar os dados
    
            
        pdf.save() #salvar pdf na raiz do projeto

        msg = QMessageBox()
        msg.setWindowTitle('Relatório')
        msg.setText('Relatório gerado com sucesso!')
        msg.exec()
   


if __name__ == "__main__":
    
    myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid) 
    
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('icons\Abrec logo paint-02 (2).png'))
    w = TelaPrincipal()
    
    w.show()
    app.exec()
    