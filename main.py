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
from PIL import Image
import numpy as np
import openpyxl
import os


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


################POPUP RECUPERAR SENHA################
class DialogRecuperarSenha(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Restaurar_Senha()
        self.ui.setupUi(self)
        
##################POP UP LOGIN INVALIDO###################
class DialogLoginInvalido(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Login_Ivalido()
        self.ui.setupUi(self)

################POPUP TIRAR/IMPORTAR FOTO################
class DialogTirarImportarFotoUsuario(QDialog):
    def __init__(self, parent, nome_usuario, id_usuario) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Tirar_Importar_Foto()
        self.ui.setupUi(self)
        self.ui.toolButton_tirar_foto_popup_perfil_cadastro_as.clicked.connect(self.Tirar_foto_Usuario)
        self.ui.toolButton_importar_foto_popup_perfil_cadastro_as.clicked.connect(self.ImportarFotoUsuario)
        self.nome_usuario = nome_usuario
        self.id_usuario = id_usuario
        
    def Tirar_foto_Usuario(self):
        
        vid = cv2.VideoCapture(0)
        # StoreFilePath =(f"C:/Users/vboxuser/Pictures/capture{self.nome_usuario}.jpg")
        StoreFilePath =(f"C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test/capture{self.nome_usuario}.jpg")
        self.db = DataBase()  
        try:
            if self.nome_usuario == "":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Insira um Nome")
                msg.setText("Insira um nome para salvar a imagem")
                msg.exec()
                cv2.destroyAllWindows()
                
            else:
                while True:
                    ret, frame = vid.read()
                    cv2.imshow("Janela", frame)
                    
                    if not ret:
                        print('failed to grab frame')
                        break
                    
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        directory = "C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test"
                        # directory = "C:/Users/vboxuser/Pictures/"
                        
                        
                        if not os.path.exists(directory):
                            os.makedirs(directory)

                        if os.path.exists(StoreFilePath):
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Information)
                            msg.setWindowTitle("Imagem Existente")
                            msg.setText("Imagem já existe. Deseja sobrescrever?")
                            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                            resposta = msg.exec()

                            if resposta == QMessageBox.Yes:
                                image_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                                image_pil.save(StoreFilePath)
                                
                                cv2.waitKey(0)
                                cv2.destroyAllWindows()
                                
                                tupla_foto = (self.nome_usuario, StoreFilePath, self.id_usuario)
                                result = self.db.tirar_foto_usuario(tupla_foto) 
                                
                                msg = QMessageBox()
                                msg.setIcon(QMessageBox.Information)
                                msg.setWindowTitle("Imagem Salva")
                                msg.setText("Imagem Salva com Sucesso!!")
                                msg.exec()
                                
                                print("Imagem salva em:", StoreFilePath)
                                cv2.destroyAllWindows()
                                break

                            elif resposta == QMessageBox.No:
                                cv2.destroyAllWindows()
                                break
            
        except mysql.connector.Error as error:
            print("Failed inserting BLOB data into MySQL table")
            
          
        
    def ImportarFotoUsuario(self):
        self.db = DataBase()  
        
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        format =  ("*.png *.jpg *.jpeg *.gif *.bmp *.ico")
        print(self.nome_usuario)
        
        if self.nome_usuario == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Insira um Nome")
            msg.setText("Insira um nome para salvar a imagem")
            msg.exec()
            
        else:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getOpenFileName(None, "Selecionar Imagem", "C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test/Imagens_Banco_Teste/", "Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ico);;Todos os arquivos (*)", options=options)
            caminho_importado = file_path
            
            if caminho_importado != format:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Formato Incorreto")
                msg.setText("Formato incorreto selecione apenas imagens")
                msg.exec()

                file_dialog = QFileDialog()
                file_path, _ = file_dialog.getOpenFileName(None, "Selecionar Imagem", "C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test/Imagens_Banco_Teste/", "Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ico);;Todos os arquivos (*)", options=options)
                caminho_importado = file_path

            else:
                if caminho_importado == "":
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Imagem Não Selecionada")
                    msg.setText("Nenhuma imagem foi selecionada")
                    msg.exec()
                else:  
                    tupla_foto = (self.nome_usuario, caminho_importado, self.id_usuario)
                    result = self.db.tirar_foto_usuario(tupla_foto)
                    
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Imagem Salva")
                    msg.setText("Imagem Salva com Sucesso!!!")
                    msg.exec()
                


class DialogTirarImportarFotoColaborador(QDialog):
    def __init__(self, parent, nome_colab, id_colaborador) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Tirar_Importar_Foto_Colaborador()
        self.ui.setupUi(self)
        self.ui.toolButton_tirar_foto_popup_perfil_cadastro_colaborador_as.clicked.connect(self.Tirar_foto_Colaborador)
        self.ui.toolButton_importar_foto_popup_perfil_cadastro_colaborador_as.clicked.connect(self.ImportarFotoColaborador)
        self.nome_colab = nome_colab
        self.id_colaborador = id_colaborador

    def Tirar_foto_Colaborador(self):   
        vid = cv2.VideoCapture(0)
        # StoreFilePath =(f"C:/Users/vboxuser/Pictures/capture{self.nome_colab}.jpg")
        StoreFilePath =(f"C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test/capture{self.nome_colab}.jpg")
        self.db = DataBase()  
        try:
            if self.nome_colab == "":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Insira um Nome")
                msg.setText("Insira um nome para salvar a imagem")
                msg.exec()
                cv2.destroyAllWindows()
                
            else:
                while True:
                    ret, frame = vid.read()
                    cv2.imshow("Janela", frame)
                    
                    if not ret:
                        print('failed to grab frame')
                        break
                        
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        directory = "C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test"
                        # directory = "C:/Users/vboxuser/Pictures/"
                        
                        if not os.path.exists(directory):
                            os.makedirs(directory)
                            
                        if os.path.exists(StoreFilePath):
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Information)
                            msg.setWindowTitle("Imagem Existente")
                            msg.setText("Imagem já existe. Deseja sobrescrever?")
                            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                            resposta = msg.exec()

                            if resposta == QMessageBox.Yes:
                                image_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                                image_pil.save(StoreFilePath)
                                
                                cv2.waitKey(0)
                                cv2.destroyAllWindows()
                                
                                tupla_foto = (self.nome_colab, StoreFilePath, self.id_colaborador)
                                result = self.db.tirar_foto_colaborador(tupla_foto) 
                                
                                msg = QMessageBox()
                                msg.setIcon(QMessageBox.Information)
                                msg.setWindowTitle("Imagem Salva")
                                msg.setText("Imagem Salva com Sucesso!!")
                                msg.exec()
                                
                                print("Imagem salva em:", StoreFilePath)
                                cv2.destroyAllWindows()
                                break

                            elif resposta == QMessageBox.No:
                                cv2.destroyAllWindows()
                                break
                        
        except mysql.connector.Error as error:
            print("Failed inserting BLOB data into MySQL table {}".format(error))
        
            
         
        
    def ImportarFotoColaborador(self):
        self.db = DataBase()  
        
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        format =  ("*.png *.jpg *.jpeg *.gif *.bmp *.ico")

        if self.nome_colab == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Insira um Nome")
            msg.setText("Insira um nome para salvar a imagem")
            msg.exec()
            return

        else:
            file_path, _ = QFileDialog.getOpenFileName(None, "Selecionar Imagem", "", "Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ico);;Todos os arquivos (*)", options=options)
            caminho_importado = file_path
            if caminho_importado != format:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Formato Incorreto")
                msg.setText("Deseja importar novamente?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                resposta = msg.exec()


                if resposta == QMessageBox.Yes:
                    file_dialog = QFileDialog()
                    file_path, _ = file_dialog.getOpenFileName(None, "Selecionar Imagem", "C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test/Imagens_Banco_Teste/", "Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ico);;Todos os arquivos (*)", options=options)
                    caminho_importado = file_path

                    if caminho_importado == "":
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Imagem Não Selecionada")
                        msg.setText("Nenhuma imagem foi selecionada")
                        msg.exec()

                    if caminho_importado == format:
                        tupla_foto = (self.nome_colab, caminho_importado, self.id_colaborador)
                        result = self.db.tirar_foto_colaborador(tupla_foto) 
                        
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Imagem Salva")
                        msg.setText("Imagem Salva com Sucesso!!!")
                        msg.exec()
                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Formato incorreto")
                        msg.setText("Formato Incorreto")
                        msg.exec()
                        
                    
                elif resposta == QMessageBox.No:
                    return


    

################Class POPUP USUARIO################

class DialogConfirmarCadastro(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Cadastro_Conclusao()
        self.ui.setupUi(self)

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


##############Class Alterar Foto e Senha##############
class DialogConfirmarSaida(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Confirmar_Saida()
        self.ui.setupUi(self)   

        self.ui.btn_sim_popup_confirma_saida.clicked.connect(self.clicouSair) 
    
    def clicouSair(self):
        resposta = 1
        TelaPrincipal.confirmouSaida(self, resposta)
    

#############################################################################
class TelaPrincipal(QMainWindow, Ui_Confirmar_Saida):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ######################### banco #########################
        self.db = DataBase()        
        self.listarAgendamentos()
        self.listarBeneficios()
        self.buscar_clinica_nome_fantasia()
        self.buscar_curso_evento()
        self.id_area_sigilosa = self.relatorio_pessoa()
        ########### selected último id das tabelas do banco ##########
        self.ultimosIds()

        self.popup = Overlay(self)
        self.popup.setMinimumWidth(1920)
        self.popup.setMinimumHeight(1080)
        self.popup.hide()

        self.showMaximized()

        self.ui.input_senha_login.setEchoMode(QLineEdit.Password)

        ###############VALIDADORES E MASKS#############
        ############ Validadores ##############
        self.validaEmail = QRegularExpressionValidator(QRegularExpression("([a-z0-9]+[.-_])*[a-z0-9]+@[a-z]+(\\.[a-z]{2,})+"))
        self.validaNumeroInt = QRegularExpressionValidator(QRegularExpression("[0-9] \\.-]+"))
        self.validaSalario = QRegularExpressionValidator(QRegularExpression("[0-9]+,?[0-9]{0,2}"))
        self.validaString = QRegularExpressionValidator(QRegularExpression("[a-zA-Z çáàãâéíóôõúÇÁÀÃÂÉÍÓÔÕÚ\\.-]+"))

        ########### Mask CPF e RG ##############
        self.ui.input_cpf_agendamento_as.setInputMask("000.000.000-00")
        self.ui.input_cpf_usuario_as.setInputMask("000.000.000-00")
        self.ui.input_cpf_cuidador_as.setInputMask("000.000.000-00")
        self.ui.input_cpf_colaborador_as.setInputMask("000.000.000-00")
        self.ui.input_cpf_pagina_consulta_geral.setInputMask("000.000.000-00")
        self.ui.input_cpf_pagina_participante_geral.setInputMask("000.000.000-00")

        self.ui.input_rg_usuario_as.setInputMask("00.000.000-0")
        self.ui.input_rg_cuidador_as.setInputMask("00.000.000-0")
        self.ui.input_rg_colaborador_as.setInputMask("00.000.000-0")

        ########## Colocando os validadores ############
        self.ui.input_nome_usuario_as.setValidator(self.validaString)
        self.ui.input_nome_cuidador_as.setValidator(self.validaString)
        self.ui.input_nome_colaborador_as.setValidator(self.validaString)  

        self.ui.input_orgao_expedidor_usuario_as.setValidator(self.validaString) 
        self.ui.input_orgao_expedidor_cuidador_as.setValidator(self.validaString)
        self.ui.input_orgao_expedidor_colaborador_as.setValidator(self.validaString) 

        # self.ui.input_nis_usuario_as.setValidator(self.validaNumeroInt) 
         
           
        ######### Arrumando a data padrão ###########
        
        self.ui.input_nascimento_usuario_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_nascimento_usuario_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_data_emissao_usuario_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_data_emissao_usuario_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_data_inicio_usuario_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_data_inicio_usuario_as.setDateTime(QDateTime.currentDateTime())
        
        self.ui.input_data_nascimento_cuidador_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_data_nascimento_cuidador_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_data_emissao_cuidador_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_data_emissao_cuidador_as.setDateTime(QDateTime.currentDateTime())

        self.ui.input_data_emissao_rg_colaborador_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_data_emissao_rg_colaborador_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_data_nascimento_colaborador_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_data_nascimento_colaborador_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_data_admissao_colaborador_as_5.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_data_admissao_colaborador_as_5.setDateTime(QDateTime.currentDateTime())

        self.ui.input_data_inicio_cursos_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_data_inicio_cursos_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_data_termino_cursos_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_data_termino_cursos_as.setDateTime(QDateTime.currentDateTime())

        self.ui.input_alterar_data_nascimento_cuidador_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_alterar_data_emissao_cuidador_as.setDisplayFormat("dd/MM/yyyy")   
        self.ui.input_alterar_nascimento_usuario_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_alterar_data_emissao_usuario_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_alterar_data_inicio_usuario_as.setDisplayFormat("dd/MM/yyyy")

        self.ui.input_alterar_data_nascimento_colaborador_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_alterar_data_emissao_rg_colaborador_as.setDisplayFormat("dd/MM/yyyy")

        self.ui.input_data_pagina_consulta_geral.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_data_pagina_consulta_geral.setDateTime(QDateTime.currentDateTime())

        self.ui.input_data_agendamento_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_data_agendamento_as.setDateTime(QDateTime.currentDateTime())

        self.ui.input_inicio_periodo_relatorio_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_inicio_periodo_relatorio_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_final_periodo_relatorio_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_final_periodo_relatorio_as.setDateTime(QDateTime.currentDateTime())

        self.ui.input_dateEdit_cadastro_beneficio.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_dateEdit_cadastro_beneficio.setDateTime(QDateTime.currentDateTime())


        ###############SIGNALS################# 
        self.ui.btn_sair_as.clicked.connect(self.sairSistema)
        self.ui.btn_sair_farm.clicked.connect(self.sairSistema)
        self.ui.btn_sair_fisio.clicked.connect(self.sairSistema)
        self.ui.btn_sair_nutri.clicked.connect(self.sairSistema)
        self.ui.btn_sair_psi.clicked.connect(self.sairSistema)

        # self.ui.btn_entrar_login.clicked.connect(lambda: self.ui.inicio.setCurrentWidget(self.ui.area_principal))
        
        self.ui.btn_entrar_login.clicked.connect(self.validarLogin)
        
        self.ui.toolButton.clicked.connect(self.visibilidade)        

        
        ########################### ASSISTENTE SOCIAL ###########################
        self.ui.btn_cadastrar_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_atendimento_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_consulta))
        self.ui.btn_cadastrar_beneficios_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_beneficios_as))
        self.ui.btn_voltar_cadastro_beneficio.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_parceiros))
        self.ui.btn_cadastrar_cuidador_usuario_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_usuario_as))
        self.ui.btn_proximo_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_cuidador_as))   
        self.ui.btn_cadastrar_cursos_oficinas_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastrar_cursos_e_oficinas_as))
        self.ui.btn_cadastrar_colaborador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_colaborador_as))
        self.ui.btn_relatorios_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_relatorio))
        self.ui.btn_relatorio_pessoas.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_relatorios_as))
        self.ui.btn_cadastro_retirada_de_beneficios.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastrar_retirada_beneficios_as))
        self.ui.btn_agenda_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_agenda_as))
        self.ui.btn_cadastrar_alterar_dados_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_alterar_dados_as))
        self.ui.btn_buscar_alterar_as.clicked.connect(lambda: self.ui.stackedWidget_8.setCurrentWidget(self.buscar_Usuario()))        
        self.ui.btn_alterar_observacoes_sigilo_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_observacoes_sigilosas_as))
        self.ui.btn_parceiros_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_parceiros))
        self.ui.btn_voltar_clinica_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_parceiros))
        self.ui.btn_cadastrar_clinica_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_clinica_as))
        self.ui.btn_cadastrar_fornecedores_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_fornecedor_as))
        self.ui.btn_lista_pessoas_cursos_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastrar_participante))
        self.ui.btn_voltar_fornecedor_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_parceiros))
        self.ui.btn_lista_pessoas_cursos_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastrar_participante))
        self.ui.input_situacao_trabalho_usuario_as.currentIndexChanged.connect(self.on_tipo_usuario_changed)
        self.ui.input_situacao_trabalho_alterar_usuario_as.currentIndexChanged.connect(self.on_tipo_alterar_usuario_changed)
        #self.ui.input_escolha_relatorio_as.currentIndexChanged.connect(self.on_idade_relatorio)
        self.ui.input_patologia_base_usuario_as.currentIndexChanged.connect(self.on_patologia_base_usuario_changed)
        self.ui.input_alterar_patologia_base_usuario_as.currentIndexChanged.connect(self.on_patologia_base_usuario_alterar)
        self.ui.input_tipo_deficiencia_usuario_as.currentIndexChanged.connect(self.on_tipo_deficiencia_usuario_changed)
        self.ui.input_alterar_tipo_deficiencia_usuario_as.currentIndexChanged.connect(self.on_alterar_tipo_deficiencia_usuario_changed)
        self.ui.btn_voltar_observacoes_sigilosas_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_alterar_dados_as))
        self.ui.btn_voltar_pagina_participante_geral.clicked.connect(lambda:self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastrar_cursos_e_oficinas_as))



        ########################### FISIOTERAPEUTA ###########################
        self.ui.btn_atendimento_fisio.clicked.connect(lambda: self.ui.stackedWidget_11.setCurrentWidget(self.ui.page_consulta_fisio))
        self.ui.btn_agenda_fisio.clicked.connect(lambda: self.ui.stackedWidget_11.setCurrentWidget(self.ui.page_agenda_fisio))
        self.ui.btn_voltar_agenda_fisio.clicked.connect(lambda: self.ui.stackedWidget_11.setCurrentWidget(self.ui.page_principal_fisio))
        self.ui.btn_voltar_pagina_consulta_geral_fisio.clicked.connect(lambda: self.ui.stackedWidget_11.setCurrentWidget(self.ui.page_principal_fisio))


        ########################### NUTRICIONISTA ###########################
        self.ui.btn_atendimento_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_consulta_nutri))
        self.ui.btn_agenda_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_agenda_nutri))
        self.ui.btn_voltar_agenda_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_principal_nutri))
        self.ui.btn_voltar_pagina_consulta_geral_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_principal_nutri))


        ########################### PSICOLOGA ###########################
        self.ui.btn_atendimento_psi.clicked.connect(lambda: self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_consulta_psi))
        self.ui.btn_agenda_psi.clicked.connect(lambda: self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_agenda_psi))
        self.ui.btn_voltar_agenda_psi.clicked.connect(lambda: self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_principal_psi))
        self.ui.btn_voltar_pagina_consulta_geral_psi.clicked.connect(lambda: self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_principal_psi))


        #################SIGNALS CEP#################
        self.ui.btn_cep_buscar_cuidador_as.clicked.connect(self.validarCep)
        self.ui.btn_cep_buscar_usuario_as.clicked.connect(self.validarCep)
        self.ui.btn_cep_buscar_colaborador_as.clicked.connect(self.validarCep)
        self.ui.btn_cep_buscar_clinica_as.clicked.connect(self.validarCep)
        self.ui.btn_alterar_cep_buscar_cuidador_as.clicked.connect(self.validarCep)
        self.ui.btn_alterar_cep_buscar_usuario_as.clicked.connect(self.validarCep)
        self.ui.btn_alterar_cep_buscar_colaborador_as.clicked.connect(self.validarCep)
        self.ui.btn_cep_buscar_fornecedor_as.clicked.connect(self.validarCep)



        #################SIGNAL CPF##################
        self.ui.btn_buscar_agendamento_as.clicked.connect(self.buscarPessoa)
        self.ui.btn_buscar_cpf_cadastro_retirada_beneficio.clicked.connect(self.buscarRetirada)

        
        #############SIGNALS BOTOES voltar#############
        #self.self.btn_voltar_popup_as.connect(lambda: self.ui.inicio.setCurrentWidget(self.ui.login))

        self.ui.btn_voltar_cursos_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_voltar_cuidador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_usuario_as))
        self.ui.btn_voltar_agenda_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_principal_as))
        self.ui.btn_voltar_usuario_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_voltar_pagina_consulta_geral.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_principal_as))
        self.ui.btn_alterar_voltar_usuario_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_alterar_voltar_cuidador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_alterar_voltar_cadastro_colaborador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_voltar_observacoes_sigilosas_as.clicked.connect(lambda: self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_alterar_usuario))
        # page_alterar_usuario
        self.ui.btn_voltar_relatorios_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_relatorio))
        self.ui.btn_voltar_cadastro_colaborador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_voltar_cadastro_retirada_beneficio.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_relatorio))
        

        ######SIGNALS POPUP RECUPERAR SENHA AS######
        self.ui.btn_esqueci_senha_login.clicked.connect(self.recuperarSenha)
        


        ######SIGNALS POPUP ALTERAR FOTO E SENHA AS######
        self.ui.btn_alterar_foto_senha_as.clicked.connect(self.trocarFotoSenha)
        
        
        ############SIGNALS POPUP TIRAR E IMPORTAR FOTO AS############
        self.ui.btn_tirar_foto_usuario_as.clicked.connect(self.tirarImportarFotoUsuario)
        self.ui.btn_tirar_foto_colaborador_as.clicked.connect(self.tirarImportarFotoColaborador)
        self.ui.btn_alterar_foto_colab_as.clicked.connect(self.AlterarFotoColaborador)
        self.ui.btn_alterar_foto_usuario_as.clicked.connect(self.AlterarFotoUsuario)
        


        ############SIGNALS POPUP Cuidador AS############
        #self.ui.btn_sair_as.clicked.connect(self.sair)
        #mudar tbm
        #self.ui.btn_finalizar_as.clicked.connect(self.concluirCadastroIncompletoUsuario)


        ############SIGNALS POPUP Cursos e oficinas AS############
        # self.ui.btn_concluir_cursos_as.clicked.connect(self.cadastroIncompletoCursos)


        ############SIGNALS BANCO ##########################
        self.ui.btn_salvar_usuario_as.clicked.connect(self.cadastroUsuario)
        self.ui.btn_finalizar_as.clicked.connect(self.cadastroCuidador)
        self.ui.btn_concluir_cadastro_colaborador_as.clicked.connect(self.cadastroColaborador)
        self.ui.btn_finalizar_fornecedor_as.clicked.connect(self.cadastroFornecedor)
        self.ui.btn_salvar_agenda_as.clicked.connect(self.cadastroAgendamento)
        self.ui.btn_concluir_cursos_as.clicked.connect(self.cadastroCurso)
        self.ui.btn_salvar_cadastro_beneficio.clicked.connect(self.cadastro_beneficios)
        self.ui.btn_finalizar_cadastro_retirada_beneficio.clicked.connect(self.cadastro_retirada_beneficios)
        self.ui.btn_alterar_cadastro_beneficio.clicked.connect(self.alterar_cadastro_beneficios)
        self.ui.btn_excluir_cadastro_beneficio.clicked.connect(self.excluir_cadastro_beneficios)
        self.ui.btn_excluir_cadastro_beneficio.clicked.connect(self.listarBeneficios)
        self.ui.btn_alterar_salvar_as.clicked.connect(self.atualizar_cuidador)
        self.ui.btn_alterar_finalizar_as.clicked.connect(self.atualizar_usuario)
        self.ui.btn_alterar_concluir_cadastro_colaborador_as.clicked.connect(self.atualizar_colaborador)
        self.ui.btn_salvar_observacoes_sigilosas_as.clicked.connect(self.area_sigilosa)
        self.ui.btn_salvar_observacoes_sigilosas_as.clicked.connect(self.filtrar_usuario_area_sigilosa)
        self.ui.btn_alterar_observacoes_sigilo_as.clicked.connect(self.filtrar_usuario_area_sigilosa)
        self.ui.btn_finalizar_clinica_as.clicked.connect(self.cadastro_clinica)       
        self.ui.input_buscar_dados_relatorio_as.textChanged.connect(self.filtrar_dados)
        self.ui.btn_gerar_excel_relatorio_as.clicked.connect(self.gerar_excel)
        self.ui.btn_buscar_relatorio_as.clicked.connect(self.filtrar_data)
        self.ui.btn_buscar_relatorio_as.clicked.connect(self.filter_idade)
        self.ui.btn_gerar_pdf_relatorio_as.clicked.connect(self.gerar_pdf)
        self.ui.btn_buscar_cpf_pagina_consulta_geral.clicked.connect(self.buscar_dados_consulta)
        self.ui.btn_salvar_pagina_consulta_geral.clicked.connect(self.cadastrar_consulta)
        self.ui.btn_buscar_cpf_pagina_consulta_geral.clicked.connect(self.puxar_consulta)
        self.ui.btn_excluir_pagina_consulta_geral.clicked.connect(self.excluir_usuario_consulta)
        self.ui.input_filtro_agendamento_as.textChanged.connect(self.filtrar_agenda)
        self.ui.btn_proximo_as.clicked.connect(self.listarUsuarios)
        self.ui.btn_salvar_agenda_as.clicked.connect(self.listarAgendamentos)
        self.ui.btn_salvar_pagina_consulta_geral.clicked.connect(self.buscar_dados_consulta)
        self.ui.btn_lista_pessoas_cursos_as.clicked.connect(self.buscar_curso_evento)
        self.ui.btn_buscar_cpf_pagina_participante_geral.clicked.connect(self.buscar_dados_participante)
        self.ui.btn_salvar_pagina_participante_geral.clicked.connect(self.cadastrar_participante)
        self.ui.btn_buscar_cpf_pagina_participante_geral.clicked.connect(self.puxar_cadastro_participante)
        self.ui.btn_excel_pagina_participante_geral.clicked.connect(self.gerar_excel_participante)
        self.ui.btn_alterar_agenda_as.clicked.connect(self.alterarAgendamentos)
        self.ui.btn_relatorios_as.clicked.connect(self.filtrar_dados)
        self.ui.btn_buscar_codigo_beneficio_cadastro_retirada_beneficio.clicked.connect(self.buscarCodigoRetirada)
        

########################### Validar Login #############################
    def validarLogin(self):
        login = self.ui.input_usuario_login.text()
        senha = self.ui.input_senha_login.text()
        login_senha = []
        perfil = []
        resultados = self.db.validarLogin(login,senha)
        print(resultados)

        if resultados[0] == [] or resultados[1] == []:
            self.ui.inicio.setCurrentWidget(self.ui.login)
            self.loginInvalido() 
        
        else:
            login_senha.append(resultados[0][0][0])
            login_senha.append(resultados[0][0][1])
            perfil.append(resultados[0][0][2])
            matricula_colaborador = resultados[1][0][0]
            if len(login_senha)==0:
                self.ui.inicio.setCurrentWidget(self.ui.login)
                self.loginInvalido() 
            elif perfil[0] == 'adm':
                if login == login_senha[0] and senha == login_senha[1]:            
                    print ("Login realizado com sucesso")
                    nome_colab = self.db.select_nome_usuario(matricula_colaborador)
                    nome_colaborador = nome_colab[0][0]
                    self.ui.lineEdit_recebe_nome_as.setText(nome_colaborador)
                    self.LoginAssistenteS()         
                else:
                    print ("Usuário não encontrado")
                    self.ui.inicio.setCurrentWidget(self.ui.login)
                    self.loginInvalido() 
            
            elif perfil[0] == 'farm':
                if login == login_senha[0] and senha == login_senha[1]:            
                    print ("Login realizado com sucesso")
                    nome_colab = self.db.select_nome_usuario(matricula_colaborador)
                    nome_colaborador = nome_colab[0][0]
                    self.ui.lineEdit_recebe_nome_as.setText(nome_colaborador)
                    self.LoginFarm()        
                else:
                    print ("Usuário não encontrado")
                    self.ui.inicio.setCurrentWidget(self.ui.login)
                    self.loginInvalido() 
                
            elif perfil[0] == 'fisio':
                if login == login_senha[0] and senha == login_senha[1]:            
                    print ("Login realizado com sucesso")
                    nome_colab = self.db.select_nome_usuario(matricula_colaborador)
                    nome_colaborador = nome_colab[0][0]
                    self.ui.lineEdit_recebe_nome_as.setText(nome_colaborador)
                    self.LoginFisio()       
                else:
                    print ("Usuário não encontrado")
                    self.ui.inicio.setCurrentWidget(self.ui.login)
                    self.loginInvalido()    

            elif perfil[0] == 'nutri':
                if login == login_senha[0] and senha == login_senha[1]:            
                    print ("Login realizado com sucesso")
                    nome_colab = self.db.select_nome_usuario(matricula_colaborador)
                    nome_colaborador = nome_colab[0][0]
                    self.ui.lineEdit_recebe_nome_as.setText(nome_colaborador)
                    self.LoginNutri()       
                else:
                    print ("Usuário não encontrado")
                    self.ui.inicio.setCurrentWidget(self.ui.login)
                    self.loginInvalido() 

            elif perfil[0] == 'psic':
                if login == login_senha[0] and senha == login_senha[1]:            
                    print ("Login realizado com sucesso")
                    nome_colab = self.db.select_nome_usuario(matricula_colaborador)
                    nome_colaborador = nome_colab[0][0]
                    self.ui.lineEdit_recebe_nome_as.setText(nome_colaborador)
                    self.LoginPsico() 
                         
                else:
                    print ("Usuário não encontrado")
                    self.ui.inicio.setCurrentWidget(self.ui.login)
                    self.loginInvalido() 
                

        
        
########################### Validar Login Assistente S #############################        
    def LoginAssistenteS(self):
        self.ui.inicio.setCurrentWidget(self.ui.area_principal)
        self.ui.tipos_acesso.setCurrentWidget(self.ui.assistente_social)

########################### Validar Login Farm #############################        
    def LoginFarm(self):
        self.ui.inicio.setCurrentWidget(self.ui.page_farmaceutica)

########################### Validar Login Fisioterapeuta #############################        
    def LoginFisio(self):
        self.ui.inicio.setCurrentWidget(self.ui.page_fisioterapeuta)


########################### Validar Login Nutri #############################        
    def LoginNutri(self):
        self.ui.inicio.setCurrentWidget(self.ui.page_nutricionista)

########################### Validar Login Psico #############################        
    def LoginPsico(self):
        self.ui.inicio.setCurrentWidget(self.ui.page_psicologa)

########################### Validar CEP ###############################
    def validarCep(self):
        cep = ""
        inputCuidador = self.ui.input_cep_cuidador_as.text()
        inputUsuario = self.ui.input_cep_usuario_as.text()
        inputColaborador = self.ui.input_cep_colaborador_as.text()
        inputClinica = self.ui.input_cep_clinica_as.text()
        inputAlterarCuidador = self.ui.input_alterar_cep_cuidador_as.text()
        inputAlterarUsuario = self.ui.input_alterar_cep_usuario_as.text()
        inputAlterarColaborador = self.ui.input_alterar_cep_colaborador_as.text()
        inputFornecedor = self.ui.input_cep_fornecedor_as.text()
        sender = self.sender()
        if 'alterar' in sender.objectName():
            if 'cuidador' in sender.objectName():
                cep = inputAlterarCuidador
            elif 'usuario' in sender.objectName():
                cep = inputAlterarUsuario
            elif 'colaborador' in sender.objectName():
                cep = inputAlterarColaborador
        else:
            if 'cuidador' in sender.objectName():
                cep = inputCuidador
            elif 'usuario' in sender.objectName():
                cep = inputUsuario
            elif 'colaborador' in sender.objectName():
                cep = inputColaborador
            elif 'clinica' in sender.objectName():
                cep = inputClinica
            elif 'fornecedor' in sender.objectName():
                cep = inputFornecedor
        cep_tratado = str('')
        print(cep)
        cep_tratado = str('')
        for i in cep:
            if(i == "." or i == '-' or i == ' '):
                pass
            else:
                cep_tratado += i   
        cep_tratado = int(cep_tratado)
        self.puxarCep(cep_tratado, sender)

############################## puxar cep e 'setar' nos inputs ########################
    def puxarCep(self, cep_tratado, sender):
        cep_tratado = cep_tratado
        sender = self.sender()
        link = f'https://viacep.com.br/ws/{cep_tratado}/json/'
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        if 'alterar' in sender.objectName():
            if 'cuidador' in sender.objectName():
                ##### tratamento da requisição - logradouro #######
                logradouro = dic_requisicao['logradouro']
                self.ui.input_alterar_logradouro_cuidador_as.setText(str(logradouro))

                ##### tratamento da requisição - bairro #######
                bairro = dic_requisicao['bairro']
                self.ui.input_alterar_bairro_cuidador_as.setText(str(bairro))

                ##### tratamento da requisição - cidade #######
                cidade = dic_requisicao['localidade']
                self.ui.input_alterar_cidade_cuidador_as.setText(str(cidade))

                ##### tratamento da requisição - estado #######        
                estado = dic_requisicao['uf']
                self.ui.input_alterar_estado_cuidador_as.setText(str(estado))

            elif 'usuario' in sender.objectName():
                ##### tratamento da requisição - logradouro #######
                logradouro = dic_requisicao['logradouro']
                self.ui.input_alterar_logradouro_usuario_as.setText(str(logradouro))

                ##### tratamento da requisição - bairro #######
                bairro = dic_requisicao['bairro']
                self.ui.input_alterar_bairro_usuario_as.setText(str(bairro))

                ##### tratamento da requisição - cidade #######
                cidade = dic_requisicao['localidade']
                self.ui.input_alterar_cidade_usuario_as.setText(str(cidade))

                ##### tratamento da requisição - estado #######        
                estado = dic_requisicao['uf']
                self.ui.input_alterar_estado_usuario_as.setText(str(estado))

            elif 'colaborador' in sender.objectName():
                ##### tratamento da requisição - logradouro #######
                logradouro = dic_requisicao['logradouro']
                self.ui.input_alterar_logradouro_colaborador_as.setText(str(logradouro))

                ##### tratamento da requisição - bairro #######
                bairro = dic_requisicao['bairro']
                self.ui.input_alterar_bairro_colaborador_as.setText(str(bairro))

                ##### tratamento da requisição - cidade #######
                cidade = dic_requisicao['localidade']
                self.ui.input_alterar_cidade_colaborador_as.setText(str(cidade))

                ##### tratamento da requisição - estado #######        
                estado = dic_requisicao['uf']
                self.ui.input_alterar_estado_colaborador_as.setText(str(estado))
        else:
            if 'cuidador' in sender.objectName():
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

            elif 'fornecedor' in sender.objectName():
                ##### tratamento da requisição - logradouro #######
                logradouro = dic_requisicao['logradouro']
                self.ui.input_logradouro_fornecedor_as.setText(str(logradouro))

                ##### tratamento da requisição - bairro #######
                bairro = dic_requisicao['bairro']
                self.ui.input_bairro_fornecedor_as.setText(str(bairro))

                ##### tratamento da requisição - cidade #######
                cidade = dic_requisicao['localidade']
                self.ui.input_cidade_fornecedor_as.setText(str(cidade))

                ##### tratamento da requisição - estado #######        
                estado = dic_requisicao['uf']
                self.ui.input_estado_fornecedor_as.setText(str(estado))

########################### FUNÇÕES BANCO ###########################
    def buscarPessoa(self):
        cpf_temp = self.ui.input_cpf_agendamento_as.text()
        cpf = ''
        for i in cpf_temp:
            if i == '.' or i == '-':
                pass
            else:
                cpf += i
        result = self.db.select_pessoa_cpf(cpf)
        id_matricula = result[0]
        nome = result[1]
        telefone = result[2]
        tamanho = int(len(result))
        if tamanho > 3:
            clinica = result[3]
        else:
            clinica = 'Não possuí'
        self.ui.input_nome_agendamento_as.setText(nome)
        self.ui.input_telefone_agendamento_as.setText(telefone)
        self.ui.input_clinica_agendamento_as.setText(clinica)

        return id_matricula
        



        
    def buscar_Usuario(self):
        valorSelecionado = self.ui.comboBox_tipos_alterar_cadastros_as.currentIndex()
        cpf = self.ui.lineEdit_alterar_buscar_cpf_cnpj_as.text()
        if valorSelecionado == 0:
            self.ui.lineEdit_alterar_buscar_cpf_cnpj_as.setText("")
            return self.ui.page_2
        ############################CUIDADOR FUNCIONANDO#################################
        elif valorSelecionado == 1: 
            dados = self.db.busca_cuidador(cpf)
            self.ui.input_alterar_matricula_cuidador_as.setText(str(dados[0]))
            self.ui.input_alterar_nome_cuidador_as.setText(dados[1])
            self.ui.input_alterar_data_nascimento_cuidador_as.setDate(QDate(dados[2]))
            self.ui.input_alterar_cpf_cuidador_as.setText(dados[3])
            self.ui.input_alterar_rg_cuidador_as.setText(dados[4])
            self.ui.input_alterar_data_emissao_cuidador_as.setDate(QDate(dados[5]))
            self.ui.input_alterar_orgao_expedidor_cuidador_as.setText(dados[6])
            sexo = str(dados[7])
            if sexo == 'Masculino':
                self.ui.input_alterar_sexo_cuidador_as.setCurrentIndex(1)
            elif sexo == 'Feminino':
                self.ui.input_alterar_sexo_cuidador_as.setCurrentIndex(2)
            self.ui.input_alterar_parentesco_cuidador_as.setText(dados[8])  
            self.ui.input_alterar_informacoes_gerais_as.setHtml(dados[9])
            self.ui.input_alterar_telefone_cuidador_as.setText(dados[10]) 
            self.ui.input_alterar_email_cuidador_as.setText(dados[11]) 
            self.ui.input_alterar_cep_cuidador_as.setText(dados[12]) 
            self.ui.input_alterar_logradouro_cuidador_as.setText(dados[13]) 
            self.ui.input_alterar_numero_cuidador_as.setText(str(dados[14])) 
            self.ui.input_alterar_bairro_cuidador_as.setText(str(dados[15]))
            self.ui.input_alterar_cidade_cuidador_as.setText(dados[16])
            self.ui.input_alterar_estado_cuidador_as.setText(dados[17])
            self.ui.input_alterar_id_endereco_cuidador_as.setText(str(dados[18]))
            self.ui.input_alterar_id_endereco_cuidador_as.hide()
            self.ui.input_alterar_id_matricula_cuidador_as.setText(str(dados[19]))
            self.ui.input_alterar_id_matricula_cuidador_as.hide()
            
            return self.ui.page_alterar_cuidador
        ##################################################################################

        #######################USUARIO####################################################

        elif valorSelecionado == 2:
            self.buscar_clinica_nome_fantasia_alterar_usuario()
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


            self.ui.input_alterar_pessoa_cdeficiencia_sim_usuario_as.setChecked(bool(dados[21]))
            self.ui.input_alterar_pessoa_cdeficiencia_nao_usuario_as.setChecked(bool(dados[21]))

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
            self.ui.input_alterar_outras_deficiencias_usuario_as.setText(dados[23])

            mediaRendaFamiliar = str(dados[24])

            if mediaRendaFamiliar == 'Menos 1 salário':
                self.ui.input_alterar_renda_familiar_usuario_as.setCurrentIndex(1)

            elif mediaRendaFamiliar == '1 salário':
                self.ui.input_alterar_renda_familiar_usuario_as.setCurrentIndex(2)

            elif mediaRendaFamiliar == 'Mais de 1 a 3 salários':
                self.ui.input_alterar_renda_familiar_usuario_as.setCurrentIndex(3)

            elif mediaRendaFamiliar == 'Mais que 3 salários':
                self.ui.input_alterar_renda_familiar_usuario_as.setCurrentIndex(4)

            meioTransporte = str(dados[25])

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
           

            valeTransporte = str(dados[26])

            if valeTransporte == 'Passe para os dias de tratamento':
                self.ui.input_alterar_vale_transporte_usuario_as.setCurrentIndex(1)

            elif valeTransporte == 'Passe do idoso':
                self.ui.input_alterar_vale_transporte_usuario_as.setCurrentIndex(2)

            elif valeTransporte == 'Passe livre':
                self.ui.input_alterar_vale_transporte_usuario_as.setCurrentIndex(3)

            situacaoTrabalho = str(dados[27])

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
                self.ui.input_situacao_trabalho_alterar_usuario_as.setCurrentIndex(6)

            elif situacaoTrabalho == 'Desempregado/a':
                self.ui.input_situacao_trabalho_alterar_usuario_as.setCurrentIndex(7)

            elif situacaoTrabalho  == 'Auxílio doença':
                self.ui.input_situacao_trabalho_alterar_usuario_as.setCurrentIndex(8)

            elif situacaoTrabalho == 'Outros':
                self.ui.input_situacao_trabalho_alterar_usuario_as.setCurrentIndex(9)

            self.ui.input_situacao_trabalho_outros_alterar_usuario_as.setText(dados[28])
            

            beneficio = str(dados[29])

            if beneficio == 'BPC/Idoso':
                self.ui.input_alterar_beneficios_usuario_as.setCurrentIndex(1)

            elif beneficio == 'BPC/PCD':
                self.ui.input_alterar_beneficios_usuario_as.setCurrentIndex(2)

            elif beneficio == 'Mais Social (Gov. Estadual)':
                self.ui.input_alterar_beneficios_usuario_as.setCurrentIndex(3)

            elif beneficio == 'Auxílio Brasil (Gov. Federal)':
                self.ui.input_alterar_beneficios_usuario_as.setCurrentIndex(4)
    
            self.ui.input_alterar_tarifa_social_sim_usuario_as.setChecked(bool(dados[30]))
            self.ui.input_alterar_tarifa_social_nao_usuario_as.setChecked(bool(dados[30]))


            tipoTratamento = str(dados[31])

            if tipoTratamento == 'Pré-Diálise':
                self.ui.input_alterar_tipo_tratamento_usuario_as.setCurrentIndex(1)
            
            elif tipoTratamento == 'Hemodiálise':
                self.ui.input_alterar_tipo_tratamento_usuario_as.setCurrentIndex(2)

            elif tipoTratamento == 'Diálise Peritoneal':
                self.ui.input_alterar_tipo_tratamento_usuario_as.setCurrentIndex(3)

            # local_tratamento = str(dados[32])
            # if local_tratamento == dados[32]:
            self.ui.input_local_tratamento_alterar_usuario_as.setCurrentIndex(int(dados[32]))


            patologiaBase = dados[33]

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

            self.ui.input_alterar_outras_patologias_usuario_as.setText(dados[34])

            self.ui.input_alterar_data_inicio_usuario_as.setDate(QDate(dados[35]))

            periodo = dados[36]

            if periodo == 'Matutino':
                self.ui.input_alterar_periodo_usuario_as.setCurrentIndex(1)

            elif periodo == 'Vespertino':
                self.ui.input_alterar_periodo_usuario_as.setCurrentIndex(2)

            elif periodo == 'Noturno':
                self.ui.input_alterar_periodo_usuario_as.setCurrentIndex(3)
            self.ui.input_alterar_id_endereco_usuario_as.setText(str(dados[37]))
            self.ui.input_alterar_id_endereco_usuario_as.hide()
            self.ui.input_alterar_id_usuario_as.setText(str(dados[38]))
            self.ui.input_alterar_id_usuario_as.hide()
            original_image = cv2.imread(dados[39])

            desired_size = (240, 240)
            resized_image = cv2.resize(original_image, desired_size)

            resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

            h, w, ch = resized_image.shape
            bytes_per_line = ch * w
            qt_image = QImage(resized_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(qt_image)

            self.ui.label_foto_usuario_alterar_as.setPixmap(pixmap)
            self.ui.label_foto_usuario_alterar_as.setScaledContents(True)
            self.ui.label_foto_usuario_alterar_as.setFixedSize(QSize(w, h))
            self.ui.label_foto_usuario_alterar_as.setAlignment(Qt.AlignCenter)
            self.ui.input_id_foto_alterar_usuario_as.setText(str(dados[40]))
            self.ui.input_id_foto_alterar_usuario_as.hide()
            return self.ui.page_alterar_usuario
        
        ##################################################################################
        if valorSelecionado == 3:
            dados = self.db.busca_colaborador(cpf)
            print("Colab -> ", dados)
            self.ui.input_alterar_matricula_colaborador_as.setText(str(dados[0]))#
            self.ui.input_alterar_nome_colaborador_as.setText(dados[1])
            self.ui.input_alterar_data_nascimento_colaborador_as.setDate(QDate(dados[2]))
            self.ui.input_alterar_cpf_colaborador_as.setText(dados[3]) #
            self.ui.input_alterar_rg_colaborador_as.setText(dados[4]) #
            self.ui.input_alterar_situacao_ativo_colaborador_as.setChecked(bool(dados[5]))
            self.ui.input_alterar_situacao_inativo_colaborador_as.setChecked(bool(dados[5]))
            self.ui.input_alterar_orgao_expedidor_colaborador_as.setText(str(dados[6]))
            self.ui.input_alterar_data_emissao_rg_colaborador_as.setDate(QDate(dados[7]))
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
            self.ui.input_alterar_confirmar_senha_colaborador_as_2.setText(dados[24])
            self.ui.input_alterar_id_endereco_colaborador_as.setText(str(dados[25]))
            self.ui.input_alterar_id_endereco_colaborador_as.hide()
            self.ui.input_alterar_id_colaborador_as.setText(str(dados[26]))
            self.ui.input_alterar_id_colaborador_as.hide()
            original_image = cv2.imread(dados[27])
            desired_size = (240, 240)
            resized_image = cv2.resize(original_image, desired_size)
            resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
            h, w, ch = resized_image.shape
            bytes_per_line = ch * w
            qt_image = QImage(resized_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_image)
            self.ui.label_foto_colaborador_alterar_as.setPixmap(pixmap)
            self.ui.label_foto_colaborador_alterar_as.setScaledContents(True)
            self.ui.label_foto_colaborador_alterar_as.setFixedSize(QSize(w, h))
            self.ui.label_foto_colaborador_alterar_as.setAlignment(Qt.AlignCenter)
            self.ui.input_alterar_id_foto_usuario_as.setText(str(dados[28]))
            self.ui.input_alterar_id_foto_usuario_as.hide()

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
        data_nasc = self.ui.input_alterar_data_nascimento_cuidador_as.text()
        data_nascimento = "-".join(data_nasc.split("/")[::-1])
        cpf_temp = self.ui.input_alterar_cpf_cuidador_as.text()
        cpf = re.sub(r'[^\w\s]','',cpf_temp)
        rg = self.ui.input_alterar_rg_cuidador_as.text()
        data_emi = self.ui.input_alterar_data_emissao_cuidador_as.text()
        data_emissao = "-".join(data_emi.split("/")[::-1])
        orgao_exp = self.ui.input_alterar_orgao_expedidor_cuidador_as.text()
        sexo = self.ui.input_alterar_sexo_cuidador_as.currentText()
        telefone = self.ui.input_alterar_telefone_cuidador_as.text()
        email = self.ui.input_alterar_email_cuidador_as.text()  
        tupla_pessoa = (id_matricula,nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,telefone,email)
        

        ################### cuidador ###################################

        parentesco = self.ui.input_alterar_parentesco_cuidador_as.text()
        observacao = self.ui.input_alterar_informacoes_gerais_as.toPlainText()
        id_matricula_cuidador = self.ui.input_alterar_id_matricula_cuidador_as.text()
        tupla_cuidador = (parentesco,observacao,id_matricula_cuidador)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualizar Cuidador")
        msg.setText("Cuidador Atualizado com sucesso!")
        msg.exec()

        ################## insert #######################################
        result = self.db.atualizar_cuidador(tupla_cuidador,tupla_pessoa,tupla_endereco)
        self.ui.lineEdit_alterar_buscar_cpf_cnpj_as.setText("")
        self.ui.comboBox_tipos_alterar_cadastros_as.setCurrentIndex(0)
        return self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_2)

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
        situacao_trabalho_outros = self.ui.input_situacao_trabalho_outros_alterar_usuario_as.text()

        if situacao_trabalho != "Outros":
            situacao_trabalho_outros = self.ui.input_situacao_trabalho_outros_alterar_usuario_as.setText("")
        else:
            pass

        tipo_transporte = self.ui.input_alterar_meio_transporte_usuario_as.currentText()
        tipo_tratamento = self.ui.input_alterar_tipo_tratamento_usuario_as.currentText()
        beneficio = self.ui.input_alterar_beneficios_usuario_as.currentText()
        local_tratamento = self.ui.input_Local_Tratamento_Clinica_usuario_as.currentText()
        local_tratamento_id = local_tratamento.split("-")
        #local_tratamento_id_clinica = int(local_tratamento_id[0])
        patologia_base  = self.ui.input_alterar_patologia_base_usuario_as.currentText()
        outras_patologias = self.ui.input_alterar_outras_patologias_usuario_as.text()

        if patologia_base != "Outros":
            outras_patologias = self.ui.input_alterar_outras_patologias_usuario_as.setText("")
        else:
            pass

        data_ini = self.ui.input_alterar_data_inicio_usuario_as.text()
        data_inicio = "-".join(data_ini.split("/")[::-1])
        periodo = self.ui.input_alterar_periodo_usuario_as.currentText()
        media_renda_familiar = self.ui.input_alterar_renda_familiar_usuario_as.currentText()
        vale_transporte = self.ui.input_alterar_vale_transporte_usuario_as.currentText()
        tipo_deficiencia = self.ui.input_alterar_tipo_deficiencia_usuario_as.currentText()
        outras_deficiencias= self.ui.input_alterar_outras_deficiencias_usuario_as.text()

        if tipo_deficiencia != "Outra":
            outras_deficiencias = self.ui.input_alterar_outras_deficiencias_usuario_as.setText("")
        else:
            pass
        



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

        tupla_pessoa = (id_matricula,nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status,telefone,email,escolaridade,estado_civil,pessoa_deficiencia,tipo_deficiencia,outras_deficiencias)
        tupla_usuario = (nis,cns,observacao_,situacao_trabalho,situacao_trabalho_outros,tipo_transporte,tipo_tratamento,beneficio,local_tratamento,periodo,data_inicio,patologia_base,outras_patologias,tarifa_social,media_renda_familiar,vale_transporte,id_matricula_usuario)

        ######################## insert ##################################
        result = []
        result = self.db.atualizar_usuario(tupla_endereco,tupla_pessoa,tupla_usuario)        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualizar Usuario")
        msg.setText("Usuario Atualizado com sucesso!")
        msg.exec()

        self.ui.lineEdit_alterar_buscar_cpf_cnpj_as.setText("")
        self.ui.comboBox_tipos_alterar_cadastros_as.setCurrentIndex(0)
        return self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_2)
    
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
        id_matricula = self.ui.input_alterar_matricula_colaborador_as.text()
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
        perfil = self.ui.input_alterar_confirmar_senha_colaborador_as_2.text()
        ##ALTERAÇÃO PARA CADASTRAR COLABORADOR
        tupla_colaborador = (pis_colab,data_admissao,salario,cargo,periodo,login,senha,perfil)

        #################### insert ##########################################
        result = []
        result = self.db.atualizar_colaborador(tupla_colaborador,tupla_pessoa,tupla_endereco)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualizar Colaborador")
        msg.setText("Colaborador Atualizado com sucesso!")
        msg.exec()
        
        self.ui.lineEdit_alterar_buscar_cpf_cnpj_as.setText("")
        self.ui.comboBox_tipos_alterar_cadastros_as.setCurrentIndex(0)
        return self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_2)

    def AlterarFotoColaborador(self):
        nome_colab = self.ui.input_alterar_nome_colaborador_as.text()
        id_foto = self.ui.input_alterar_id_foto_usuario_as.text()
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecionar Imagem", "", "Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ico);;Todos os arquivos (*)", options=options)
        caminho_importado = file_path
        tupla_foto = (id_foto,nome_colab, caminho_importado)
        result = self.db.alterar_foto_colaborador(tupla_foto) 
        original_image = cv2.imread(caminho_importado)

        desired_size = (240, 240)
        resized_image = cv2.resize(original_image, desired_size)

        resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

        h, w, ch = resized_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(resized_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

        pixmap = QPixmap.fromImage(qt_image)

        self.ui.label_foto_colaborador_alterar_as.setPixmap(pixmap)
        self.ui.label_foto_colaborador_alterar_as.setScaledContents(True)
        self.ui.label_foto_colaborador_alterar_as.setFixedSize(QSize(w, h))
        self.ui.label_foto_colaborador_alterar_as.setAlignment(Qt.AlignCenter)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Foto Colaborador")
        msg.setText("Foto do Colaborador Atualizado com sucesso!")
        msg.exec()


    def AlterarFotoUsuario(self):
        nome_usua = self.ui.input_alterar_nome_usuario_as.text()
        id_foto = self.ui.input_id_foto_alterar_usuario_as.text()
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecionar Imagem", "", "Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ico);;Todos os arquivos (*)", options=options)
        caminho_importado = file_path
        tupla_foto = (id_foto, nome_usua, caminho_importado)
        result = self.db.alterar_foto_usuario(tupla_foto) 
        original_image = cv2.imread(caminho_importado)

        desired_size = (240, 240)
        resized_image = cv2.resize(original_image, desired_size)

        resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

        h, w, ch = resized_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(resized_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

        pixmap = QPixmap.fromImage(qt_image)

        self.ui.label_foto_usuario_alterar_as.setPixmap(pixmap)
        self.ui.label_foto_usuario_alterar_as.setScaledContents(True)
        self.ui.label_foto_usuario_alterar_as.setFixedSize(QSize(w, h))
        self.ui.label_foto_usuario_alterar_as.setAlignment(Qt.AlignCenter)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Foto Usuario")
        msg.setText("Foto do Usuario Atualizado com sucesso!")
        msg.exec()





















    def cadastroUsuario(self):
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
        rg_temp = self.ui.input_rg_usuario_as.text()
        rg = re.sub(r'[^\w\s]','',rg_temp)
        print(rg)
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
        situacao_trabalho_outros = self.ui.input_situacao_trabalho_outros_usuario_as.text()
        tipo_transporte = self.ui.input_meio_transporte_usuario_as.currentText()
        tipo_tratamento = self.ui.input_tipo_tratamento_usuario_as.currentText()
        beneficio = self.ui.input_beneficios_usuario_as.currentText()
        local_tratamento = self.ui.input_Local_Tratamento_Clinica_usuario_as.currentText()
        local_tratamento_id = local_tratamento.split("-")
        local_tratamento_id_clinica = int(local_tratamento_id[0])
        patologia_base  = self.ui.input_patologia_base_usuario_as.currentText()
        outras_patologias = self.ui.input_outras_patologias_usuario_as.text()
        
       

        
           
        data_ini = self.ui.input_data_inicio_usuario_as.text()
        data_inicio = "-".join(data_ini.split("/")[::-1])
        periodo = self.ui.input_periodo_usuario_as.currentText()
        media_renda_familiar = self.ui.input_renda_familiar_usuario_as.currentText()
        vale_transporte = self.ui.input_vale_transporte_usuario_as.currentText()
        tipo_deficiencia = self.ui.input_tipo_deficiencia_usuario_as.currentText()
        outras_deficiencias = self.ui.input_outras_deficiencias_usuario_as.text()


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

        
        tupla_pessoa = (nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status,telefone,email,escolaridade,estado_civil,pessoa_deficiencia,tipo_deficiencia,outras_deficiencias)
        tupla_usuario = (nis,cns,observacao_,situacao_trabalho,situacao_trabalho_outros,tipo_transporte,tipo_tratamento,beneficio,local_tratamento_id_clinica,periodo,data_inicio,patologia_base,outras_patologias,tarifa_social,media_renda_familiar,vale_transporte)

        ######################## insert ##################################
        result = []
        result = self.db.cadastro_usuario(tupla_endereco,tupla_pessoa,tupla_usuario)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro Usuário")
        msg.setText("Usuário cadastrado com sucesso!")
        msg.exec()
        # self.msg(result[0],result[1])
        self.limparCamposCadastroUsuario()
    
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
        c = 0
        while c < len(convertendo_nome):
            self.ui.input_usuario_cuidador_as.addItem("")
            c += 1
        while count < len(convertendo_nome):
            self.ui.input_usuario_cuidador_as.setItemText(itens, QCoreApplication.translate("MainWindow", f"{id_usuarios[count]}-{convertendo_nome[count]}", None))
            itens += 1
            count += 1
            
    def listarAgendamentos(self):
        res = self.db.select_agendamentos()

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_agendamento_as.setItem(row, column, QTableWidgetItem(str(data)))

    def listarBeneficios(self):
        resultado = self.db.busca_beneficios()
        
        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_cadastro_beneficio.setItem(row, column, QTableWidgetItem(str(data)))

    def ultimosIds(self):
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

                
                
    def alterarAgendamentos(self):
        try:
            dados = []
            for row in range(self.ui.input_TableWidget_agendamento_as.rowCount()):
                row_data = []
                for column in range(self.ui.input_TableWidget_agendamento_as.columnCount()):
                    item = self.ui.input_TableWidget_agendamento_as.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append("")  
                dados.append(row_data)
            
            for emp in dados:
                resultado = self.db.alterar_agendamento(emp)   

            self.filtrar_agenda()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Alterar Agendamento")
            msg.setText("Agendamento Alterado com sucesso!")
            msg.exec()    
            return "OK", "Benefício(s) atualizado(s) com sucesso!!"
        except Exception as err:
            return "ERRO", str(err)
        
        
        
        
                
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
        rg_temp = self.ui.input_rg_cuidador_as.text()
        rg = re.sub(r'[^\w\s]','',rg_temp)
        data_emi = self.ui.input_data_emissao_cuidador_as.text()
        data_emissao = "-".join(data_emi.split("/")[::-1])
        orgao_exp = self.ui.input_orgao_expedidor_cuidador_as.text()
        sexo = self.ui.input_sexo_cuidador_as.currentText()
        telefone = self.ui.input_telefone_cuidador_as.text()
        email = self.ui.input_email_cuidador_as.text()  

        tupla_pessoa = (nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,telefone,email)

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
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro Cuidador")
        msg.setText("Cuidador cadastrado com sucesso!")
        msg.exec()
        # self.msg(result[0],result[1])
        self.limparCamposCadastroCuidador()

    def formatar_salario(self):
        text = self.input_salario_colaborador_as.text()

        try:
            salario_formatado = '{:,.2f}'.format(float(text))
        except ValueError:
            salario_formatado = ''

        self.input_salario_colaborador_as.setText(salario_formatado)
    
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
        rg_temp = self.ui.input_rg_colaborador_as.text()
        rg = re.sub(r'[^\w\s]','',rg_temp)
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
    # ...

        salario = self.ui.input_salario_colaborador_as.text()
        data_admi = self.ui.input_data_admissao_colaborador_as_5.text()
        data_admissao = "-".join(data_admi.split("/")[::-1])
        pis_colab = self.ui.input_pis_colaborador_as.text()
        periodo = self.ui.input_periodo_colaborador_comboBox_as.currentText()
        cargo = self.ui.input_cargo_colaborador_comboBox_as.currentText() ##### ADDDDDD NO CÓDIGO
        # salario_formatado = self.ui.input_salario_colaborador_as.text().replace('.', '').replace(',', '.')

        #################### login e senha ####################################
        login = self.ui.input_usuario_colaborador_as_2.text()
        senha = self.ui.input_senha_colaborador_as_2.text()
        #confirmar_senha = self.ui.input_confirmar_senha_colaborador_as.text()
        if cargo in ["Recepcionista"]:
            perfil = 'rep'
        elif cargo in ["Assistente Social"]:
            perfil = 'adm'
        elif cargo in ["Farmacêutico (a)"]:
            perfil = 'farm'
        elif cargo in ["Psicólogo (a)"]:
            perfil = 'pisc'
        elif cargo in ["Fisioterapeuta"]:
            perfil = 'fisio'
        elif cargo in ["Nutricionista"]:
            perfil = 'nutri'

        ##ALTERAÇÃO PARA CADASTRAR COLABORADOR
        tupla_colaborador = (pis_colab, data_admissao, salario, cargo, periodo, login, senha, perfil)

        #################### insert ##########################################
        result = []
        result = self.db.cadastro_colaborador(tupla_endereco,tupla_pessoa,tupla_colaborador)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro Colaborador")
        msg.setText("Colaborador cadastrado com sucesso!")
        msg.exec()
        # self.msg(result[0],result[1])        
        self.limparCamposCadastroColaborador()



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
        
        regex = "([01]?[0-9]|2[0-3]):[0-5][0-9]"

        horario_inicial = self.ui.input_horario_inicio_cursos_as.text()
        
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

        result=self.db.cadastro_curso(tupla_curso)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro Curso")
        msg.setText("Curso cadastrado com sucesso!")
        msg.exec()
        self.limparCadastroCursos()
        
    
    def cadastroAgendamento(self):
        id_matricula = self.buscarPessoa()
        cpf = self.ui.input_cpf_agendamento_as.text()
        nome = self.ui.input_nome_agendamento_as.text()
        telefone = self.ui.input_telefone_agendamento_as.text()
        clinica = self.ui.input_clinica_agendamento_as.text()

        profissional = ''
        if self.ui.input_profissional_as_agendamento_as.isChecked():
            profissional = 'Assistente Social'
        elif self.ui.input_profissional_fisio_agendamento_as.isChecked():
            profissional = 'Fisioterapeuta'
        elif self.ui.input_profissional_nutri_agendamento_as.isChecked():
            profissional = 'Nutricionista'
        if self.ui.input_profissional_psi_agendamento_as.isChecked():
            profissional = 'Psicóloga'
        data = self.ui.input_data_agendamento_as.text()
        data_agend = "-".join(data.split("/")[::-1])
        hora = self.ui.input_hora_agendamento_as.text()
        anotacao = self.ui.input_anotacao_agendamento_as.toPlainText()

        tupla_agendamento = (id_matricula, cpf, nome, telefone, clinica, profissional, data_agend, hora, anotacao)
        result = self.db.cadastro_agendamento(tupla_agendamento)
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro Agendamento")
        msg.setText("Agendamento Cadastrado com sucesso!")
        msg.exec()
        # self.msg(result[0],result[1])   
        self.limparCamposAgenda() 
        self.listarAgendamentos()


    def cadastroFornecedor(self):
        ######################## endereço ###########################   
        cep = self.ui.input_cep_fornecedor_as.text()
        rua = self.ui.input_logradouro_fornecedor_as.text()
        numero = self.ui.input_numero_fornecedor_as.text()
        bairro = self.ui.input_bairro_fornecedor_as.text()
        cidade = self.ui.input_cidade_fornecedor_as.text()
        estado = self.ui.input_estado_fornecedor_as.text()
        
        tupla_endereco = (cep,rua,numero,bairro,cidade,estado)
         ###################### fornecedor ##############################
        cnpj = self.ui.input_cnpj_cadastro_fornecedor_as.text()
        razao_social = self.ui.input_razao_social_cadastro_fornecedor_as.text()
        nome_fantasia = self.ui.input_nome_fantasia_cadastro_fornecedor_as.text()
        celular = self.ui.input_telefone_celular_fornecedor_as.text()
        telefone_fixo = self.ui.input_telefone_fixo_fornecedor_as.text()
        email = self.ui.input_email_fornecedor_as.text()
        contato = self.ui.input_contato_fornecedor_as.text()
        inscricao_estadual = self.ui.input_inscricao_estadual_fornecedor_as.text()
        inscricao_municipal = self.ui.input_inscricao_municipal_fornecedor_as.text()
        informacao_geral = self.ui.input_informacoes_gerais_fornecedor_as.toPlainText()

        tupla_fornecedor = (razao_social,nome_fantasia,cnpj,celular,telefone_fixo,email,contato,inscricao_municipal,inscricao_estadual,informacao_geral)
                            #razao_social,nome_fantasia,cnpj,telefone_celular,telefone_fixo,email,contato,inscricao_municipal,inscricao_estadual,observacao,id_endereco
        result = []
        result = self.db.cadastro_fornecedor(tupla_endereco,tupla_fornecedor)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro Fornecedor")
        msg.setText("Fornecedor cadastrado com sucesso!")
        msg.exec()
        # self.msg(result[0],result[1])
        self.limparCamposCadastroFornecedor()


    def filtrar_agenda(self):
        txt = re.sub('[\W_]+','',self.ui.input_filtro_agendamento_as.text())
        res = self.db.filter_agenda(txt)
        self.ui.input_TableWidget_agendamento_as.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_agendamento_as.setItem(row, column, QTableWidgetItem(str(data)))

    def area_sigilosa(self):

        if self.ui.input_obito_paciente_sim_as.isChecked:
            situacao="Ativo"
        else:
            situacao="Inativo"
        
        observacao_gerais = self.ui.input_observacoes_obs_sigilosas_as.toPlainText()
        tupla_area_sigilosa = (situacao, observacao_gerais, self.id_area_sigilosa)
        result = self.db.cadastrar_area_sigilosa(tupla_area_sigilosa)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Area Sigilosa")
        msg.setText("Observção salva com sucesso!")
        msg.exec()
        self.limparCamposAreaSigilosa()

    def limparCamposCadastroUsuario (self):
        self.ultimosIds()
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
        self.ui.input_Local_Tratamento_Clinica_usuario_as.setCurrentIndex(int(0))
        self.ui.input_patologia_base_usuario_as.setCurrentIndex(int(0))
        self.ui.input_data_inicio_usuario_as.setDate(QDate(2000, 1, 1))
        self.ui.input_periodo_usuario_as.setCurrentIndex(int(0))
        self.ui.label_foto_usuario_alterar_as.setPixmap("")

        

 
    def limparCamposCadastroCuidador(self):
        self.ultimosIds()
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
        self.ultimosIds()
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
       
    def limparCadastroCursos(self):
        self.ui.input_nome_cursos_as.setText("")
        self.ui.input_tipo_cursos_as.setCurrentIndex(int(0))
        self.ui.input_responsavel_cursos_as.setText("")
        self.ui.input_data_inicio_cursos_as.setDate(QDate(2000, 1, 1))
        self.ui.input_data_termino_cursos_as.setDate(QDate(2000, 1, 1))
        self.ui.input_periodo_cursos_as.setCurrentIndex(int(0))
        self.ui.input_vagas_cursos_as.setText("")
        self.ui.input_ativo_cursos_as.setCheckable(False)
        self.ui.input_ativo_cursos_as.setCheckable(True)
        self.ui.input_inativo_cursos_as.setCheckable(False)
        self.ui.input_inativo_cursos_as.setCheckable(True)
        self.ui.input_descricao_atividade_cursos_as.setHtml("")
        self.ui.input_segunda_cursos_as.setCheckable(False)
        self.ui.input_segunda_cursos_as.setCheckable(True) 
        self.ui.input_terca_cursos_as.setCheckable(False)
        self.ui.input_terca_cursos_as.setCheckable(True) 
        self.ui.input_quarta_cursos_as.setCheckable(False)
        self.ui.input_quarta_cursos_as.setCheckable(True) 
        self.ui.input_quinta_cursos_as.setCheckable(False)
        self.ui.input_quinta_cursos_as.setCheckable(True) 
        self.ui.input_sexta_cursos_as.setCheckable(False)
        self.ui.input_sexta_cursos_as.setCheckable(True) 
        self.ui.input_sabado_cursos_as.setCheckable(False)
        self.ui.input_sabado_cursos_as.setCheckable(True) 
        self.ui.input_horario_inicio_cursos_as.setTime(QTime(00,00))
        self.ui.input_horario_termino_cursos_as.setTime(QTime(00,00))

    def limparCamposConsulta(self):
        self.ui.input_nome_pagina_consulta_geral.setText("")
        self.ui.input_contato_pagina_consulta_geral.setText("")
        self.ui.input_clinica_pagina_consulta_geral.setText("")
        self.ui.radioButton_Consulta_as.setCheckable(False)
        self.ui.radioButton_Consulta_as.setCheckable(True)
        self.ui.radioButton_Retorno_as.setCheckable(False)
        self.ui.radioButton_Retorno_as.setCheckable(True)
        self.ui.input_data_pagina_consulta_geral.setDate(QDate(2000, 1, 1))
        self.ui.input_hora_consulta_as.setText("")
        self.ui.input_relatorio_pagina_consulta_geral.setHtml("")

    def limparCamposAgenda(self):
        self.ui.input_nome_agendamento_as.setText("")
        self.ui.input_telefone_agendamento_as.setText("")
        self.ui.input_clinica_agendamento_as.setText("")
        self.ui.input_profissional_as_agendamento_as.setCheckable(False)
        self.ui.input_profissional_as_agendamento_as.setCheckable(True)
        self.ui.input_profissional_psi_agendamento_as.setCheckable(False)
        self.ui.input_profissional_psi_agendamento_as.setCheckable(True)
        self.ui.input_profissional_nutri_agendamento_as.setCheckable(False)
        self.ui.input_profissional_nutri_agendamento_as.setCheckable(True)
        self.ui.input_profissional_fisio_agendamento_as.setCheckable(False)
        self.ui.input_profissional_fisio_agendamento_as.setCheckable(True)
        self.ui.input_data_agendamento_as.setDate(QDate(2000, 1, 1))
        self.ui.input_hora_agendamento_as.setTime(QTime(00,00))
        self.ui.input_anotacao_agendamento_as.setHtml("")


    def limparCamposCadastroFornecedor(self):
         
        self.ui.input_cep_fornecedor_as.setText("")
        self.ui.input_logradouro_fornecedor_as.setText("")
        self.ui.input_numero_fornecedor_as.setText("")
        self.ui.input_bairro_fornecedor_as.setText("")
        self.ui.input_cidade_fornecedor_as.setText("")
        self.ui.input_estado_fornecedor_as.setText("")
             
        self.ui.input_cnpj_cadastro_fornecedor_as.setText("")
        self.ui.input_razao_social_cadastro_fornecedor_as.setText("")
        self.ui.input_nome_fantasia_cadastro_fornecedor_as.setText("")
        self.ui.input_telefone_celular_fornecedor_as.setText("")
        self.ui.input_telefone_fixo_fornecedor_as.setText("")
        self.ui.input_email_fornecedor_as.setText("")
        self.ui.input_contato_fornecedor_as.setText("")
        self.ui.input_inscricao_estadual_fornecedor_as.setText("")
        self.ui.input_inscricao_municipal_fornecedor_as.setText("")
        self.ui.input_informacoes_gerais_fornecedor_as.setHtml("")
        
    def limparCamposCadastroBeneficios(self):
        self.ui.input_tipo_cadastro_beneficio.setCurrentIndex(int(0))
        self.ui.input_codigo_cadastro_beneficio.setText("")
        self.ui.input_lote_cadastro_beneficio.setText("")
        self.ui.input_comboBox_udm_cadastro_benefecio.setCurrentIndex(int(0))
        self.ui.input_descricao_cadastro_beneficio.setText("")
        self.ui.input_dateEdit_cadastro_beneficio.setDate(QDate(2000, 1, 1))          
        self.ui.input_spinBox_cadastro_beneficio.setValue(0)
    
    def limparCamposCadastroRetiradaBeneficios(self):
            self.ui.input_cpf_cadastro_retirada_beneficio.setText("")
            self.ui.input_nome_cadastro_retirada_beneficio.setText("")
            self.ui.input_idade_cadastro_retirada_beneficio.setText("")
            self.ui.input_data_cadastro_retirada_beneficio.setDate(QDate(2020, 1, 1))
            self.ui.input_telefone_cadastro_retirada_beneficio.setText("")
            self.ui.input_cns_cadastro_retirada_beneficio.setText("")
            self.ui.input_clinica_cadastro_retirada_beneficio.setText("")
            
            self.ui.input_codigo_beneficio_cadastro_retirada_beneficio.setText("")
            self.ui.input_descricao_cadastro_retirada_beneficio.setText("")       
            self.ui.input_spinBox_cadastro_retirada_beneficio.setValue(0)
        
    def buscar_clinica_nome_fantasia(self):
        lista_clinica = self.db.select_clinica_ids()
        nomes = []
        id_clinicas = []

        for i in lista_clinica:
            id_clinica = i[0]
            id_clinica = str(id_clinica).zfill(3)
            nome = self.db.select_nome_Clinica(id_clinica)
            id_clinicas.append(id_clinica)
            nomes.append(nome)
        convertendo_nome = [i[0] for i in nomes]
        convertendo_nome_clinica = [i[0] for i in convertendo_nome]
        count = 0
        itens = 1
        c = 0
        while c < len(convertendo_nome_clinica):
            self.ui.input_Local_Tratamento_Clinica_usuario_as.addItem("") 
            c += 1
        while count < len(convertendo_nome_clinica):
            self.ui.input_Local_Tratamento_Clinica_usuario_as.setItemText(itens, QCoreApplication.translate("MainWindow",f"{id_clinicas[count]}-{convertendo_nome_clinica[count]}", None))
            itens += 1
            count += 1

    def buscar_clinica_nome_fantasia_alterar_usuario(self):
        lista_clinica = self.db.select_clinica_ids()
        nomes = []
        id_clinicas = []

        for i in lista_clinica:
            id_clinica = i[0]
            id_clinica = str(id_clinica).zfill(3)
            nome = self.db.select_nome_Clinica(id_clinica)
            id_clinicas.append(id_clinica)
            nomes.append(nome)
        convertendo_nome = [i[0] for i in nomes]
        convertendo_nome_clinica_alterar = [i[0] for i in convertendo_nome]
        count = 0
        itens = 1
        c = 0
        while c < len(convertendo_nome_clinica_alterar):
            self.ui.input_local_tratamento_alterar_usuario_as.addItem("")
            c += 1
        while count < len(convertendo_nome_clinica_alterar):
            self.ui.input_local_tratamento_alterar_usuario_as.setItemText(itens, QCoreApplication.translate("MainWindow",f"{id_clinicas[count]}-{convertendo_nome_clinica_alterar[count]}", None))
            itens += 1
            count += 1

    def buscar_curso_evento(self):
        lista_curso_evento = self.db.select_cursos_ids()
        nome_curso = []
        id_curso_eventos = []

        for i in lista_curso_evento:
            id_curso_evento = i[0]
            id_curso_evento = str(id_curso_evento).zfill(3)
            nome = self.db.select_nome_curso_evento(id_curso_evento)
            id_curso_eventos.append(id_curso_evento)
            nome_curso.append(nome)
        convertendo_nome = [i[0] for i in nome_curso]
        convertendo_nome_curso = [i[0] for i in convertendo_nome]
        count = 0
        itens = 1
        c = 0
        while c < len(convertendo_nome_curso):
            self.ui.comboBox_cursos_participante_geral.addItem("")
            c += 1
        while count < len(convertendo_nome_curso):
            self.ui.comboBox_cursos_participante_geral.setItemText(itens, QCoreApplication.translate("MainWindow",f"{id_curso_eventos[count]}-{convertendo_nome_curso[count]}", None))
            itens += 1
            count += 1

    def cadastrar_participante(self):
        nome_curso = self.ui.comboBox_cursos_participante_geral.currentText()
        nome_curso_id = nome_curso.split("-")
        nome_curso_id_tratado = int(nome_curso_id[0])
        id_matricula = self.ui.input_id_matricula_user_participante_geral.text()
        
        tupla_participante = (nome_curso_id_tratado,id_matricula)
        result = []
        result = self.db.cadastrar_participante(tupla_participante)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro Participante")
        msg.setText("Participante cadastrado com sucesso!")
        msg.exec()
        self.puxar_cadastro_participante()

    def buscar_dados_participante(self):
        cpf_tmp = self.ui.input_cpf_pagina_participante_geral.text()
        cpf = re.sub(r'[^\w\s]','',cpf_tmp)
        dados = self.db.buscar_participante(cpf)
        self.ui.input_id_matricula_user_participante_geral.setText(str(dados[0]))
        self.ui.input_id_matricula_user_participante_geral.hide()
        self.ui.input_nome_pagina_participante_geral.setText(dados[1])
        self.ui.input_telefone_pagina_participante_geral.setText(dados[2])
        self.ui.input_email_pagina_participante_geral.setText(dados[3])
        self.ui.input_clinica_pagina_participante_geral.setText(dados[4])

    def puxar_cadastro_participante(self):
        cpf_tmp = self.ui.input_cpf_pagina_participante_geral.text()
        cpf = re.sub(r'[^\w\s]','',cpf_tmp)
        result = self.db.buscar_info_participante(cpf)
        self.ui.input_TableWidget_pagina_participante_geral.clearContents()
        self.ui.input_TableWidget_pagina_participante_geral.setRowCount(len(result))   

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_pagina_participante_geral.setItem(row, column,QTableWidgetItem(str(data)))

    def gerar_excel_participante(self):
        dados = []
        all_dados =  []

        for row in range(self.ui.input_TableWidget_pagina_participante_geral.rowCount()):
            for column in range(self.ui.input_TableWidget_pagina_participante_geral.columnCount()):
                dados.append(self.ui.input_TableWidget_pagina_participante_geral.item(row, column).text())
        
            all_dados.append(dados)
            dados = []

        columns = ['NOME', 'CPF','TELEFONE', 'CLINICA', 'CURSO']
        
        relatorio = pd.DataFrame(all_dados, columns= columns)
        
        file, _ = QFileDialog.getSaveFileName(self,"Relatorio", "C:/Abrec", "Text files (*.xlsx)") 
        if file:
            with open(file, "w") as f:
                relatorio.to_excel(file, sheet_name='relatorio', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()

    def buscar_dados_consulta(self):
        cpf_temp = self.ui.input_cpf_pagina_consulta_geral.text()
        cpf = ''
        for i in cpf_temp:
            if i == '.' or i == '-':
                pass
            else:
                cpf += i
        dados = self.db.buscar_consulta(cpf)
        self.ui.input_id_usuario_consulta_as.setText(str(dados[0]))
        self.ui.input_id_usuario_consulta_as.hide()
        self.ui.input_nome_pagina_consulta_geral.setText(dados[1])
        self.ui.input_contato_pagina_consulta_geral.setText(dados[2])
        self.ui.input_clinica_pagina_consulta_geral.setText(dados[3])
        self.ui.input_data_pagina_consulta_geral.setDate(QDate(dados[4]))
        self.ui.input_hora_consulta_as.setText(str(dados[5]))
        self.puxar_consulta()

    def cadastrar_consulta(self):
        if self.ui.radioButton_Consulta_as.isChecked():
            situacao = "Consulta"
        if self.ui.radioButton_Retorno_as.isChecked():
            situacao = "Retorno"

        data = self.ui.input_data_pagina_consulta_geral.text()
        data_consulta = "-".join(data.split("/")[::-1])

        hora_bruta = self.ui.input_hora_consulta_as.text()

        relatorio = self.ui.input_relatorio_pagina_consulta_geral.toPlainText()

        id_usuario = self.ui.input_id_usuario_consulta_as.text()

        tupla_consulta = (situacao,data_consulta,hora_bruta,relatorio,id_usuario)

        result = []
        result = self.db.cadastro_consulta(tupla_consulta)
        self.limparCamposConsulta()
        self.puxar_consulta()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro Consulta")
        msg.setText("Consulta Cadastrada com sucesso!")
        msg.exec()

    def puxar_consulta(self):
        id_usuario = self.ui.input_id_usuario_consulta_as.text()
        result = self.db.buscar_info_consulta(id_usuario)
        self.ui.input_TableWidget_pagina_consulta_geral.clearContents()
        self.ui.input_TableWidget_pagina_consulta_geral.setRowCount(len(result))   

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_pagina_consulta_geral.setItem(row, column,QTableWidgetItem(str(data)))
                
    def alterar_usuario_consulta(self,campo):
        campo = []
        update_dados = []

        for row in range(self.ui.input_TableWidget_pagina_consulta_geral.rowCount()):
            for column in range(self.ui.input_TableWidget_pagina_consulta_geral.columnCount()):
                campo.append(self.ui.input_TableWidget_pagina_consulta_geral.item(row, column).text())
            update_dados.append(campo)
            campo = []
        for emp in update_dados:
           res = self.db.alterar_usuario_consulta_as(tuple(emp))

        self.puxar_consulta()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Alterar Consulta")
        msg.setText("Consulta Alterada com sucesso!")
        msg.exec()


    def excluir_usuario_consulta (self):
        id_consulta = self.ui.input_TableWidget_pagina_consulta_geral.selectionModel().currentIndex().siblingAtColumn(0).data()
        self.db.deletar_consulta_relatorio(id_consulta)

        self.puxar_consulta()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excluir Consulta")
        msg.setText("Consulta Excluida com sucesso!")
        msg.exec()
    
    def alterar_cadastro_beneficios(self, dados):
        try:
            dados = []

            for row in range(self.ui.input_TableWidget_cadastro_beneficio.rowCount()):
                row_data = []
                for column in range(self.ui.input_TableWidget_cadastro_beneficio.columnCount()):
                    item = self.ui.input_TableWidget_cadastro_beneficio.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append("")  
                dados.append(row_data)

            for emp in dados:
                resultado = self.db.alterar_cadastro_beneficios(emp)

            self.listarBeneficios()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Alterção Beneficio")
            msg.setText("Benefcio Alterado com sucesso!")
            msg.exec()
            
                
            return "OK", "Benefício(s) atualizado(s) com sucesso!!"
        except Exception as err:
            return "ERRO", str(err)
        

    def excluir_cadastro_beneficios (self):
        id_beneficios = self.ui.input_TableWidget_cadastro_beneficio.selectionModel().currentIndex().siblingAtColumn(0).data()
        self.db.deletar_cadastro_beneficios(id_beneficios)
        self.listarBeneficios()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Beneficio Excluir")
        msg.setText("Beneficio excluido com sucesso!")
        msg.exec()
        
        
#####Alterar SITUACAO de Trabalho Outros #########
    def on_tipo_usuario_changed(self):

        if self.ui.input_situacao_trabalho_usuario_as.currentText() == "Outros":
            self.ui.frame_438.setEnabled(True)
            self.ui.frame_438.show()
            self.ui.input_situacao_trabalho_outros_usuario_as.setEnabled(True)
            self.ui.input_situacao_trabalho_outros_usuario_as.setStyleSheet("") 
            self.ui.input_situacao_trabalho_outros_usuario_as.setEnabled(True)
            self.ui.input_situacao_trabalho_outros_usuario_as.show()
            
        else:
            self.ui.frame_438.hide()
            self.ui.input_situacao_trabalho_outros_usuario_as.setEnabled(False)
            self.ui.input_situacao_trabalho_outros_usuario_as.hide()
            self.ui.input_situacao_trabalho_outros_usuario_as.clear()

######################LOGIN INVALIDO POPUP####################
    def loginIvalido(self):       
        msg = DialogLoginInvalido(self)
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

    def loginInvalido(self):       
        msg = DialogLoginInvalido(self)
        self.popup.show()
        msg.exec()
        self.popup.hide()


    def trocarFotoSenha(self):
        msg = DialogAlterarSenhaFoto(self)
        self.popup.show()
        msg.exec()
        self.popup.hide()


    def concluirCadastroIncompletoUsuario(self):
        msg = DialogCadastroIncompletoUsuario(self)
        self.popup.show()
        msg.exec()
        self.popup.hide()

        #conectar com o botão entrar depois
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_cuidador_as)


    def cadastroIncompletoCursos(self):
        msg = DialogCadastroIncompletoCursos(self)
        self.popup.show()
        msg.exec()
        self.popup.hide()

        #conectar com o botão entrar depois
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastrar_cursos_e_oficinas_as)


    def tirarImportarFotoUsuario(self):
        nome_usuario = self.ui.input_nome_usuario_as.text()
        id_usuario = self.ui.input_matricula_usuario_as.text()
        msg = DialogTirarImportarFotoUsuario(self, nome_usuario, id_usuario)
        self.popup.show()
        msg.exec()
        self.popup.hide()
        
        caminho = self.db.buscar_foto_usuario(id_usuario)
        caminho_tratado = "".join(caminho)
        
        if caminho_tratado is not None and isinstance(caminho_tratado, str):
            if os.path.isfile(caminho_tratado):
                original_image = cv2.imread(caminho_tratado)
                # print("Original From-string -> ", original_image)
                if original_image is not None:
                    desired_size = (240, 240)
                    resized_image = cv2.resize(original_image, desired_size)

                    resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

                    h, w, ch = resized_image.shape
                    bytes_per_line = ch * w
                    qt_image = QImage(resized_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

                    pixmap = QPixmap.fromImage(qt_image)

                    self.ui.label_foto_usuario_as.setPixmap(pixmap)

                    self.ui.label_foto_usuario_as.setFixedSize(QSize(w, h))

                    self.ui.label_foto_usuario_as.setAlignment(Qt.AlignCenter)
                else:
                    print("Erro ao ler a imagem.")
            else:
                print("O arquivo de imagem não existe:", caminho)
        else:
            print("Caminho inválido:", caminho)


    def tirarImportarFotoColaborador(self):
        nome_colab = self.ui.input_nome_colaborador_as.text()
        id_colaborador = self.ui.input_matricula_colaborador_as.text()
        msg = DialogTirarImportarFotoColaborador(self, nome_colab, id_colaborador)
        self.popup.show()
        msg.exec()
        self.popup.hide()


        caminho = self.db.buscar_foto_colaborador(id_colaborador)
        caminho_tratado = "".join(caminho)
        if caminho_tratado is not None and isinstance(caminho_tratado, str):
            if os.path.isfile(caminho_tratado):
                original_image = cv2.imread(caminho_tratado)
                # print("Original From-string -> ", original_image)
                if original_image is not None:
                    desired_size = (240, 240)
                    resized_image = cv2.resize(original_image, desired_size)

                    resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

                    h, w, ch = resized_image.shape
                    bytes_per_line = ch * w
                    qt_image = QImage(resized_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

                    pixmap = QPixmap.fromImage(qt_image)

                    self.ui.label_foto_colaborador_as.setPixmap(pixmap)

                    self.ui.label_foto_colaborador_as.setFixedSize(QSize(w, h))

                    self.ui.label_foto_colaborador_as.setAlignment(Qt.AlignCenter)
                else:
                    print("Erro ao ler a imagem.")
            else:
                print("O arquivo de imagem não existe:", caminho)
        else:
            print("Caminho inválido:", caminho)


    def confirmarCadastro(self):
        msg = DialogConfirmarCadastro(self)
        self.popup.show()
        msg.exec()
        self.popup.hide()
        #self.clean()


    def clean(self):
        self.ui.input_nome_usuario_as.setText("")


    def confirmarSaida(self):
        msg = DialogConfirmarSaida(self)
        self.popup.show()
        msg.exec()
        self.popup.hide()
    
    def confirmouSaida(self, resposta):
        print("chegou")
        if resposta == 1:
            self.ui.inicio.setCurrentWidget(lambda: self.ui.login)
            # self.ui.inicio.input_usuario_login.setText("")
            # self.ui.input_senha_login.setText("")
        else:
            print("erro")



##################################################################


           
    

    
    def on_tipo_alterar_usuario_changed(self):

        if  self.ui.input_situacao_trabalho_alterar_usuario_as.currentText() == "Outros":
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
            cnpj = self.ui.input_cnpj_cadastro_clinica_as.text()
            razao_social = self.ui.input_razao_social_cadastro_clinica_as.text()
            nome_fantasia = self.ui.input_nome_fantasia_cadastro_clinica_as.text()
            telefone = self.ui.input_telefone_clinica_as.text()
            email = self.ui.input_email_clinica_as.text()
            obs = self.ui.input_informacoes_gerais_clinica_as.toPlainText()

            tupla_clinica = (cnpj,razao_social,nome_fantasia,telefone,email,obs)
            
            result = []
            result=self.db.cadastro_clinica(tupla_endereco,tupla_clinica)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Clinica")
            msg.setText("Clinica cadastrada com sucesso!")
            msg.exec()
            # self.msg(result[0],result[1])
            self.limparCamposCadastroClinica()

###########################################################################
    def cadastro_beneficios(self):
            
        ########################## dados ######################################       
            dados = self.db.busca_beneficios()
            tipo = self.ui.input_tipo_cadastro_beneficio.currentText()   
            if tipo == 'Medicação':
                self.ui.input_tipo_cadastro_beneficio.currentText()         

            codigo = self.ui.input_codigo_cadastro_beneficio.text()
            lote = self.ui.input_lote_cadastro_beneficio.text()
            dados = self.db.busca_beneficios()
            unidade_medida = self.ui.input_comboBox_udm_cadastro_benefecio.currentText()
            
            if unidade_medida == 'Quilo':
                self.ui.input_comboBox_udm_cadastro_benefecio.currentText()
              
            descricao = self.ui.input_descricao_cadastro_beneficio.text()
            vali=self.ui.input_dateEdit_cadastro_beneficio.text()
             
            validade = "-".join(vali.split("/")[::-1])          
            quantidade = self.ui.input_spinBox_cadastro_beneficio.value()

            tupla_beneficios = (tipo,codigo,lote,unidade_medida,descricao,validade,quantidade)
            
            result = []
            result=self.db.cadastro_beneficios(tupla_beneficios)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Beneficios")
            msg.setText("Beneficio cadastrado com sucesso!")
            msg.exec()
            # self.msg(result[0],result[1])
            self.limparCamposCadastroBeneficios()
            self.listarBeneficios()
    
    def buscarRetirada(self):
        cpf = self.ui.input_cpf_cadastro_retirada_beneficio.text()
        result = self.db.select_retirada_beneficio_cpf(cpf)
        
        print (result)
        if result:
            id_matricula = result.get('id_matricula', '')
            nome = result.get('nome', '')
            idade = result.get('idade', '')          
            telefone = result.get('telefone', '')
            cns = result.get('cns','')
            clinica = result.get('clinica', 'Não possui')

            self.ui.input_id_usuario_retirada_beneficio.setText(str(id_matricula))
            self.ui.input_id_usuario_retirada_beneficio.hide()
            self.ui.input_nome_cadastro_retirada_beneficio.setText(nome)
            self.ui.input_idade_cadastro_retirada_beneficio.setText(str(idade))
            self.ui.input_telefone_cadastro_retirada_beneficio.setText(telefone)            
            self.ui.input_cns_cadastro_retirada_beneficio.setText(cns)
            self.ui.input_clinica_cadastro_retirada_beneficio.setText(str(clinica))
            return id_matricula
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Retirada de Benefício")
            msg.setText("Nenhuma informação para este CPF.")
            msg.exec()
            
            return None
    
    def buscarCodigoRetirada(self):
        codigo = self.ui.input_codigo_beneficio_cadastro_retirada_beneficio.text()
        result = self.db.select_retirada_beneficio_codigo(codigo)
        
        if result:
            id_beneficios = result.get('id_beneficios', '')
            descricao = result.get('descricao', '')
            
            self.ui.input_codigo_beneficio_cadastro_retirada_beneficio.setText(str(id_beneficios))
            self.ui.input_descricao_cadastro_retirada_beneficio.setText(descricao)
            return id_beneficios
        
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Retirada de Benefício")
            msg.setText("Nenhuma informação para este Código.")
            msg.exec()
            return None


    def cadastro_retirada_beneficios(self):
            id_matricula = self.ui.input_id_usuario_retirada_beneficio.text()
            cpf = self.ui.input_cpf_cadastro_retirada_beneficio.text()
            data_retirada = self.ui.input_data_cadastro_retirada_beneficio.text()
            data_consulta = "-".join(data_retirada.split("/")[::-1]) 
            codigo_retirada = self.ui.input_codigo_beneficio_cadastro_retirada_beneficio.text()
            quantidade_retirada = self.ui.input_spinBox_cadastro_retirada_beneficio.value()

            tupla_retirada_beneficios = (id_matricula,cpf,codigo_retirada,quantidade_retirada,data_consulta)
            
            result = []
            result=self.db.cadastro_retirada_beneficios(tupla_retirada_beneficios)
            print (result)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Retirada de Beneficios")
            msg.setText("Cadastro de retirada efetuado com sucesso!")
            msg.exec()
            # self.msg(result[0],result[1])
            self.limparCamposCadastroRetiradaBeneficios()
    
    

######################## Deficiência base Outra################################

    def on_tipo_deficiencia_usuario_changed(self):

        if self.ui.input_tipo_deficiencia_usuario_as.currentText() == "Outra":
            self.ui.frame_502.setEnabled(True)
            self.ui.frame_502.show()
            self.ui.input_outras_deficiencias_usuario_as.setStyleSheet("")  
            self.ui.input_outras_deficiencias_usuario_as.setEnabled(True)
            self.ui.input_outras_deficiencias_usuario_as.show()           
        else:
            self.ui.frame_502.hide()
            self.ui.frame_502.setEnabled(False)
            self.ui.input_outras_deficiencias_usuario_as.hide()
            self.ui.input_outras_deficiencias_usuario_as.setEnabled(False)
            self.ui.input_outras_deficiencias_usuario_as.clear()

    def on_alterar_tipo_deficiencia_usuario_changed(self):
              
        if self.ui.input_alterar_tipo_deficiencia_usuario_as.currentText() == "Outra":
            self.ui.frame_550.setEnabled(True)
            self.ui.frame_550.show()
            self.ui.input_alterar_outras_deficiencias_usuario_as.setStyleSheet("")  
            self.ui.input_alterar_outras_deficiencias_usuario_as.setEnabled(True)
            self.ui.input_alterar_outras_deficiencias_usuario_as.show()           
        else:
            self.ui.frame_550.hide()
            self.ui.frame_550.setEnabled(False)
            self.ui.input_alterar_outras_deficiencias_usuario_as.hide()
            self.ui.input_alterar_outras_deficiencias_usuario_as.setEnabled(False)
            self.ui.input_alterar_outras_deficiencias_usuario_as.clear()


######################## Patologia base outros################################
      
    def on_patologia_base_usuario_changed(self):

        if self.ui.input_patologia_base_usuario_as.currentText() == "Outros":
            self.ui.frame_499.setEnabled(True)
            self.ui.frame_499.show()
            self.ui.input_outras_patologias_usuario_as.setStyleSheet("")  
            self.ui.input_outras_patologias_usuario_as.setEnabled(True)
            self.ui.input_outras_patologias_usuario_as.show()           
        else:
            self.ui.frame_499.hide()
            self.ui.frame_499.setEnabled(False)
            self.ui.input_outras_patologias_usuario_as.hide()
            self.ui.input_outras_patologias_usuario_as.setEnabled(False)
            self.ui.input_outras_patologias_usuario_as.clear()

    def on_patologia_base_usuario_alterar(self):
        if self.ui.input_alterar_patologia_base_usuario_as.currentText() == "Outros":
            self.ui.frame_500.setEnabled(True)
            self.ui.frame_500.show()
            self.ui.input_alterar_outras_patologias_usuario_as.setStyleSheet("") 
            self.ui.input_alterar_outras_patologias_usuario_as.setEnabled(True)
            self.ui.input_alterar_outras_patologias_usuario_as.show()
            
        else:
            self.ui.frame_500.hide()
            self.ui.frame_500.setEnabled(False)
            self.ui.input_alterar_outras_patologias_usuario_as.hide()
            self.ui.input_alterar_outras_patologias_usuario_as.setEnabled(False)
            self.ui.input_alterar_outras_patologias_usuario_as.clear()
            
    ######################################################################

    def sairSistema(self):  #Popup que Confirma saida - Botão Sair 
        
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Confirma Saida")
        dlg.setText("Deseja Sair?")
        
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()      

            
        if button == QMessageBox.Yes:
            self.ui.inicio.setCurrentIndex(0)
            self.ui.input_usuario_login.setText("")
            self.ui.input_senha_login.setText("")
        
        else:
            dlg.close()


    ######################################################################

    ########################################################################

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
        self.ui.tableWidget_relatorio_as.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.tableWidget_relatorio_as.setItem(row, column, QTableWidgetItem(str(data)))
    
    def filtrar_usuario_area_sigilosa(self):
        result = self.db.filter_usuario_area_sigilosa(self.id_area_sigilosa)
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
        
        res = self.db.filter_data(texto_data_inicio_tratada,texto_data_final_tratada)

        self.ui.tableWidget_relatorio_as.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.tableWidget_relatorio_as.setItem(row, column, QTableWidgetItem(str(data)))
                   
    def filter_idade(self):

        texto_idade_inicio = self.ui.input_idade_inicial_relatorio_as.text()
        texto_idade_final = self.ui.input_idade_final_relatorio_as.text()
        
        res = self.db.filter_idade(texto_idade_inicio,texto_idade_final)
        self.ui.tableWidget_relatorio_as.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.tableWidget_relatorio_as.setItem(row, column, QTableWidgetItem(str(data)))

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

        
        file, _ = QFileDialog.getSaveFileName(self,"Relatorio", "C:/Abrec", "Text files (*.xlsx)") 
        if file:
            with open(file, "w") as f:
                relatorio.to_excel(file, sheet_name='relatorio', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()
        
    def gerar_pdf(self):
        column_names = []
        for col in range(self.ui.tableWidget_relatorio_as.columnCount()):
            column_names.append(self.ui.tableWidget_relatorio_as.horizontalHeaderItem(col).text())
        file, _ = QFileDialog.getSaveFileName(self, "Selecionar pasta de saida", "C:/Abrec/", "PDF files (*.pdf)")
        pdf = canvas.Canvas(file)
        pdf.setFont("Times-Roman", 9)
        pdf.setTitle("Relatório")
        

        filtered_data = []
        
        for row in range(self.ui.tableWidget_relatorio_as.rowCount()):
            if not self.ui.tableWidget_relatorio_as.isRowHidden(row):
                row_data = [self.ui.tableWidget_relatorio_as.item(row, col).text() for col in range(self.ui.tableWidget_relatorio_as.columnCount())]
                filtered_data.append(row_data)
    
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
  
        if file:
            pdf.save()
        msg = QMessageBox()
        msg.setWindowTitle('PDF')
        msg.setText('PDF gerado com sucesso!')
        msg.exec()
    
    
    # def execute(self):
    #     for(int i=0; i<10; i++):
            
            
    
if __name__ == "__main__":
    
    myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid) 
    
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('icons\Abrec logo paint-02 (2).png'))
    w = TelaPrincipal()
    
    w.show()
    app.exec()
    
