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
        self.ui.btn_tirar_foto_popup_foto_as.clicked.connect(self.TirarFotoWeb)
        self.ui.btn_importar_popup_foto_as.clicked.connect(self.ImportarFoto)
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
        self.ui.setupUi(self)

        ######################### banco #########################

        self.db = DataBase()

        ########### selected último id das tabelas do banco ##########
        selected_pessoa = self.db.select_pessoa()
        selected_colaborador = self.db.select_colaborador()
        ultimo_id_pessoa = (selected_pessoa[0])
        ultimo_id_colaborador = (selected_colaborador[0])
        ultimo_id_pessoa = ''.join(map(str, ultimo_id_pessoa))
        ultimo_id_colaborador = ''.join(map(str, ultimo_id_colaborador))
        proximo_id_pessoa = 1 + int(ultimo_id_pessoa)
        proximo_id_colaborador = 1 + int(ultimo_id_colaborador)
        proximo_id_pessoa = str(proximo_id_pessoa).zfill(4)
        proximo_id_colaborador = str(proximo_id_colaborador).zfill(4)

        self.ui.input_matricula_usuario_as.setText(f'{proximo_id_pessoa}')
        self.ui.input_matricula_usuario_as.setStyleSheet("color: black; qproperty-alignment: AlignCenter;")
        self.ui.input_matricula_cuidador_as.setText(f'{proximo_id_pessoa}')
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
        self.ui.btn_entrar_login.clicked.connect(lambda: self.ui.inicio.setCurrentWidget(self.ui.area_principal))
        self.ui.toolButton.clicked.connect(self.visibilidade)        

        self.ui.btn_sair_as.clicked.connect(lambda: self.ui.inicio.setCurrentWidget(self.ui.login))
        
        self.ui.btn_cadastrar_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_consulta_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_consulta_as))
        self.ui.btn_buscar_consulta_as.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_consulta_depois))

        self.ui.btn_cadastrar_cuidador_usuario_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_usuario_as))
        self.ui.btn_proximo_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_cuidador_as))    
        self.ui.btn_cadastrar_cursos_oficinas_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastrar_cursos_e_oficinas_as))
        self.ui.btn_cadastrar_colaborador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_colaborador_as))
        self.ui.btn_relatorios_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_relatorios_as))
        self.ui.btn_agenda_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_agenda_as))
        self.ui.btn_cadastrar_alterar_dados_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_alterar_dados_as))
        self.ui.btn_buscar_alterar_as.clicked.connect(lambda: self.ui.stackedWidget_8.setCurrentWidget(self.buscar_Usuario()))        
        self.ui.btn_observacoes_sigilo_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_observacoes_sigilosas_as))
        self.ui.input_situacao_trabalho_usuario_as.currentIndexChanged.connect(self.on_tipo_usuario_changed)
        self.ui.input_situacao_trabalho_alterar_usuario_as.currentIndexChanged.connect(self.on_tipo_alterar_usuario_changed)
        


        #################SIGNALS CEP#################
        self.ui.btn_cep_buscar_cuidador_as.clicked.connect(self.validarCep)
        self.ui.btn_cep_buscar_usuario_as.clicked.connect(self.validarCep)
        self.ui.btn_cep_buscar_colaborador_as.clicked.connect(self.validarCep)









        
        #############SIGNALS BOTOES voltar#############
        self.ui.btn_voltar_cursos_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_voltar_cuidador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_usuario_as))
        self.ui.btn_voltar_agenda_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_principal_as))
        self.ui.btn_voltar_usuario_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_voltar_consulta_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_principal_as))
        self.ui.btn_voltar_observacoes_sigilosas_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_usuario_as))
        self.ui.btn_voltar_relatorios_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_principal_as))
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
            self.ui.input_alterar_data_emissao_cuidador_as.date().toString(str(dados[4]))
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
            
            return self.ui.page_alterar_cuidador
        ##################################################################################



        #######################USUARIO####################################################

        elif valorSelecionado == 2:
            print ('to funfando == 2\n')
            dados = self.db.busca_usuario(cpf)
            print(dados)
        
            
            self.ui.input_alterar_matricula_usuario_as.setText(str(dados[0])) #
            self.ui.input_alterar_nome_usuario_as.setText(dados[1]) #
            self.ui.input_alterar_nascimento_usuario_as.date().toString(str(dados[2]))
            self.ui.input_alterar_situacao_inativo_usuario_as.setChecked(bool(dados[3]))
            self.ui.input_situacao_ativo_usuario_as.setChecked(bool(dados[3]))
            self.ui.input_alterar_cpf_usuario_as.setText(str(dados[4]))
            self.ui.input_alterar_rg_usuario_as.setText(dados[5]) #
            self.ui.input_alterar_data_emissao_usuario_as.date().toString(str(dados[6])) #
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

            self.ui.input_alterar_data_inicio_usuario_as.date().toString(str(dados[31]))

            periodo = dados[33]

            if periodo == 'Matutino':
                self.ui.input_alterar_periodo_usuario_as.setCurrentIndex(1)

            elif periodo == 'Vespertino':
                self.ui.input_alterar_periodo_usuario_as.setCurrentIndex(2)

            elif periodo == 'Noturno':
                self.ui.input_alterar_periodo_usuario_as.setCurrentIndex(3)

            return self.ui.page_alterar_usuario
        
        ##################################################################################




        if valorSelecionado == 3:
            dados = self.db.busca_colaborador(cpf)
            print(dados)
            self.ui.input_alterar_matricula_colaborador_as.setText(str(dados[0]))#
            self.ui.input_alterar_nome_colaborador_as.setText(dados[1])
            self.ui.input_data_nascimento_colaborador_as.date().toString(str(dados[2]))
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
            return self.ui.page_alterar_colaborador_as

    
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
        escolaridade = self.ui.input_escolaridade_usuario_comboBox_as.currentText()
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

        tupla_pessoa = (nome,cpf,rg,data_emissao,orgao_exp,sexo,telefone,email,escolaridade)
        

        ################### cuidador ###################################

        parentesco = self.ui.input_parentesco_cuidador_as.text()
        observacao = self.ui.input_informacoes_gerais_as.toPlainText()
        tupla_cuidador = (parentesco,observacao)

        ################## insert #######################################
        result = []
        result = self.db.cadastro_cuidador(tupla_endereco,tupla_pessoa,tupla_cuidador)
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

        login = self.ui.input_usuario_colaborador_as.text()
        senha = self.ui.input_senha_colaborador_as.text()
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
#####Alterar SITUACAO de Trabalho Outros #########
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

    def on_tipo_usuario_changed(self):
        
        if self.ui.input_situacao_trabalho_usuario_as.currentText() == "Outros":
            self.ui.frame_438.setEnabled(True)
            self.ui.frame_438.show()
            self.ui.input_situacao_trabalho_outros_usuario_as.setStyleSheet("")  
            self.ui.input_situacao_trabalho_outros_usuario_as.setEnabled(True)
            self.ui.input_situacao_trabalho_outros_usuario_as.show()           
        else:
            self.ui.frame_438.hide()
            self.ui.frame_438.setEnabled(False)
            self.ui.input_situacao_trabalho_outros_usuario_as.hide()
            self.ui.input_situacao_trabalho_outros_usuario_as.setEnabled(False)
            self.ui.input_situacao_trabalho_outros_usuario_as.clear()
            
            
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

   


if __name__ == "__main__":
    
    myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid) 
    
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('icons\Abrec logo paint-02 (2).png'))
    
    w = TelaPrincipal()
    
    w.show()
    app.exec()
    