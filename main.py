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
import locale
import imghdr
import os


############################# VALIDAÇÕES ASSISTENTE SOCIAL ######################################################
from Validacao_Campos.Assistente_Social.validar_campos_usuario import validarCamposUsuarioCadastro
from Validacao_Campos.Assistente_Social.validar_campos_cuidador import validarCamposCuidadorCadastro
from Validacao_Campos.Assistente_Social.validar_campos_colaborador import validarCamposColaboradorCadastro
from Validacao_Campos.Assistente_Social.validar_campos_agendamento import validarCamposAgendamentoCadastro
from Validacao_Campos.Assistente_Social.validar_campos_clinica import validarCamposClinicaCadastro
from Validacao_Campos.Assistente_Social.validar_campos_fornecedores import validarCamposFornecedoresCadastro
from Validacao_Campos.Assistente_Social.validar_campos_beneficios import validarCamposBeneficiosCadastro
from Validacao_Campos.Assistente_Social.validar_campos_cursos import validarCamposCursoCadastro
from Validacao_Campos.Assistente_Social.validar_campos_retirada_beneficio import validarCamposRetiradaBeneficiosCadastro
##################################################################################################################

############################# VALIDAÇÕES NUTRICIONISTA###########################################################
from Validacao_Campos.Nutricionista.validar_campos_agendamento_nutri import validarCamposAgendamentoNutriCadastro
from Validacao_Campos.Nutricionista.validar_campos_consulta_nutri import validarCamposConsultaNutriCadastro
from Validacao_Campos.Nutricionista.valdiar_campos_consulta_nutri import validarCamposConsultaNutriImcCadastro
##################################################################################################################

############################## VALIDAÇÕES FISIOTERAPEUTA #########################################################
from Validacao_Campos.Fisioterapeuta.validar_campos_agendamento_fisio import validarCamposAgendamentoFisioCadastro
from Validacao_Campos.Fisioterapeuta.validar_campos_cosulta_fisio import validarCamposConsultaFisioCadastro
##################################################################################################################

############################## VALIDAÇÕES FARMACEUTICA ###########################################################
from Validacao_Campos.Farmaceutica.validar_campos_beneficios_farm import validarCamposBeneficiosFarmaceuticaCadastro
from Validacao_Campos.Farmaceutica.validar_campos_retirada_beneficio_farm import validarCamposRetiradaBeneficiosFarmaceuticaCadastro
##################################################################################################################

############################## VALIDAÇÕES PSICOLOGA ##############################################################
from Validacao_Campos.Psicologa.validar_campo_agendamento_psic import validarCamposAgendamentoPsicCadastro
from Validacao_Campos.Psicologa.validar_campo_consulta_pisc import validarCamposConsultaPsicCadastro
##################################################################################################################

############################## VALIDAÇÕES SECRETARIA #############################################################
from Validacao_Campos.Secretaria.validar_campos_agendamento_sec import validarCamposAgendamentoSecCadastro
##################################################################################################################


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


########## CLASSE POPUP RECUPERAR SENHA ####################################################################################################################################################
class DialogRecuperarSenha(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Restaurar_Senha()
        self.ui.setupUi(self)
        
########## CLASSE POP UP LOGIN INVALIDO ####################################################################################################################################################
class DialogLoginInvalido(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Login_Ivalido()
        self.ui.setupUi(self)

########## CLASSE POPUP TIRAR/IMPORTAR FOTO ################################################################################################################################################
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
        # StoreFilePath =(f"C:/Users/vboxuser/Pictures/Foto_{self.nome_usuario}.jpg")
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
                                
                                cv2.destroyAllWindows()
                                break

                            elif resposta == QMessageBox.No:
                                cv2.destroyAllWindows()
                                break
                            
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
                    
                    elif cv2.waitKey(1) & 0xFF == ord('x'):
                        cv2.destroyAllWindows()
                        break
                    
        except mysql.connector.Error as error:
            print("Failed inserting BLOB data into MySQL table {}".format(error))
            
          
        
    def ImportarFotoUsuario(self):
        self.db = DataBase()  
        
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        format =  ["png", "jpg", "jpeg", "gif", "bmp", "ico"]
        
        if self.nome_usuario == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Insira um Nome")
            msg.setText("Insira um nome para salvar a imagem")
            msg.exec()
            return
            
        else:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getOpenFileName(None, "Selecionar Imagem", "", "Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ico);;Todos os arquivos (*)", options=options)
            caminho_importado = file_path
            formato_importado = imghdr.what(caminho_importado)
            if formato_importado not in format:

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Erro ao importar")
                msg.setText("Erro ao improtar a Imagem\nDeseja importar novamente?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                resposta = msg.exec()
                
                if resposta == QMessageBox.Yes:
                    file_dialog = QFileDialog()
                    file_path, _ = file_dialog.getOpenFileName(None, "Selecionar Imagem", "", "Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ico);;Todos os arquivos (*)", options=options)
                    caminho_importado = file_path
                    formato_importado = imghdr.what(caminho_importado)
                    print(formato_importado)
                    
                    if formato_importado not in format:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Erro ao importar")
                        msg.setText("Erro ao improtar a Imagem\nTente Novamente")
                        msg.exec() 
                        return
                        
                    if formato_importado in format:
                        
                        tupla_foto = (self.nome_usuario, caminho_importado, self.id_usuario)
                        result = self.db.tirar_foto_usuario(tupla_foto)
                        
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Imagem Salva")
                        msg.setText("Imagem Salva com Sucesso!!!")
                        msg.exec() 
                          
                if resposta == QMessageBox.No:
                    return
            else:
                tupla_foto = (self.nome_usuario, caminho_importado, self.id_usuario)
                result = self.db.tirar_foto_usuario(tupla_foto)
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Imagem Salva")
                msg.setText("Imagem Salva com Sucesso!!!")
                msg.exec()         


########## CLASSE IMPORTAR FOTO COLABORADOR ################################################################################################################################################
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
        StoreFilePath =(f"C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test/capture{self.nome_colab}.jpg")
        # StoreFilePath =(f"C:/Users/vboxuser/Desktop/capture{self.nome_colab}.jpg")
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
                        # directory = "C:/Users/vboxuser/Desktop/"
                        directory = "C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test"
                        
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
                                    
                                cv2.destroyAllWindows()
                                break

                            elif resposta == QMessageBox.No:
                                cv2.destroyAllWindows()
                                break
                            
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
                    
                    elif cv2.waitKey(1) & 0xFF == ord('x'):
                        cv2.destroyAllWindows()
                        break
        except mysql.connector.Error as error:
            print("Failed inserting BLOB data into MySQL table {}".format(error))
        
            
         
        
    def ImportarFotoColaborador(self):
        self.db = DataBase()  
        
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        format =  ["png", "jpg", "jpeg", "gif", "bmp", "ico"]
        
        if self.nome_colab == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Insira um Nome")
            msg.setText("Insira um nome para salvar a imagem")
            msg.exec()
            return

        else:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getOpenFileName(None, "Selecionar Imagem", "", "Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ico);;Todos os arquivos (*)", options=options)
            caminho_importado = file_path
            formato_importado = imghdr.what(caminho_importado)
            
            if formato_importado not in format:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Erro ao importar")
                msg.setText("Erro ao improtar a Imagem\nDeseja importar novamente?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                resposta = msg.exec()


                if resposta == QMessageBox.Yes:
                    file_dialog = QFileDialog()
                    file_path, _ = file_dialog.getOpenFileName(None, "Selecionar Imagem", "", "Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ico);;Todos os arquivos (*)", options=options)
                    caminho_importado = file_path
                    formato_importado = imghdr.what(caminho_importado)
                    print(formato_importado)

                    if formato_importado not in format:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Erro ao importar")
                        msg.setText("Erro ao improtar a Imagem\nTente Novamente")
                        msg.exec() 
                        return

                    if formato_importado in format:
                        
                        tupla_foto = (self.nome_colab, caminho_importado, self.id_colaborador)
                        result = self.db.tirar_foto_colaborador(tupla_foto)
                        
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Imagem Salva")
                        msg.setText("Imagem Salva com Sucesso!!!")
                        msg.exec()
                        
                    
                    if resposta == QMessageBox.No:
                        return
            else:
                tupla_foto = (self.nome_colab, caminho_importado, self.id_colaborador)
                result = self.db.tirar_foto_colaborador(tupla_foto)

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Imagem Salva")
                msg.setText("Imagem Salva com Sucesso!!!")
                msg.exec()  
            

    

########## CLASSE POPUP USUARIO ############################################################################################################################################################
class DialogConfirmarCadastro(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Cadastro_Conclusao()
        self.ui.setupUi(self)

########## CLASSE CADASTRO INCOMPLETO ######################################################################################################################################################
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


########## CLASSE POPUP CURSOS E OFICINAS ##################################################################################################################################################
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



########## CLASSE ALTERAR FOTO E SENHA #####################################################################################################################################################
class DialogAlterarSenhaFoto(QDialog):
    def __init__(self, parent, id_colab, nome_colab_perfil) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Alterar_Senha_Foto()
        self.ui.setupUi(self)  
        self.ui.toolButton_alterar_foto_popup_perfil_as.clicked.connect(self.AlterarFotoColaborador)
        self.id_colaborador = id_colab
        print("Id Dilago DENTRO",self.id_colaborador)
        self.nome_colab_login = nome_colab_perfil
        print("Nome Login DENTRO", self.nome_colab_login)
               
        
    def AlterarFotoColaborador(self):
        self.db = DataBase()  
        
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        format =  ["png", "jpg", "jpeg", "gif", "bmp", "ico"]
        
        if self.nome_colab_login == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Insira um Nome")
            msg.setText("Insira um nome para salvar a imagem")
            msg.exec()
            return

        else:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getOpenFileName(None, "Selecionar Imagem", "", "Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ico);;Todos os arquivos (*)", options=options)
            
            #Verifica se o caminho escolhido pelo usuario é valido
            caminho_importado = file_path
            formato_importado = imghdr.what(caminho_importado)

            if formato_importado not in format:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Erro ao importar")
                msg.setText("Erro ao improtar a Imagem\nDeseja importar novamente?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                resposta = msg.exec()


                if resposta == QMessageBox.Yes:
                    file_dialog = QFileDialog()
                    file_path, _ = file_dialog.getOpenFileName(None, "Selecionar Imagem", "", "Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ico);;Todos os arquivos (*)", options=options)
                    caminho_importado = file_path
                    formato_importado = imghdr.what(caminho_importado)
                    print(formato_importado)

                    if formato_importado not in format:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Erro ao importar")
                        msg.setText("Erro ao improtar a Imagem\nTente Novamente")
                        msg.exec() 
                        return

                    if formato_importado in format:
                        
                        tupla_foto = (self.nome_colab_login, caminho_importado, self.id_colaborador)
                        result = self.db.tirar_foto_colaborador(tupla_foto)
                        
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Imagem Salva")
                        msg.setText("Imagem Salva com Sucesso!!!")
                        msg.exec()
                        
                    
                    if resposta == QMessageBox.No:
                        return
            else:
                #Trata o ID do Select feito no banco
                id_foto = self.db.buscarIdFotoColab(self.id_colaborador)
                id_foto_nt = id_foto[0][0]
                id_foto_tratada = id_foto_nt

                #Altera no Banco o caminho da imagem
                tupla_foto = (id_foto_tratada, self.nome_colab_login, caminho_importado)
                print(tupla_foto)
                result = self.db.alterar_foto_colaborador(tupla_foto)
                

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Imagem Salva")
                msg.setText("Imagem Salva com Sucesso!!!")
                msg.exec()  
            
            

########## CLASSE CONFIRMAR SAIDA ##########################################################################################################################################################
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

########## CLASSE PRINCIPAL ################################################################################################################################################################
class TelaPrincipal(QMainWindow, Ui_Confirmar_Saida):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ########## BUSCANDO DADOS BANCO ####################################################################################################################################################
        self.db = DataBase()
        self.relatorio_beneficio()        
        self.listarAgendamentos()
        self.listarBeneficios()
        self.buscar_clinica_nome_fantasia()
        self.buscar_curso_evento()
        self.puxar_relatorio_cuidador()
        self.id_area_sigilosa = self.relatorio_pessoa()
        
        
        ########### SELECT ÚLTIMO ID DO BANCO ##############################################################################################################################################
        self.ultimosIds()


        self.popup = Overlay(self)
        self.popup.setMinimumWidth(1920)
        self.popup.setMinimumHeight(1080)
        self.popup.hide()

        self.showMaximized()

        self.ui.input_senha_login.setEchoMode(QLineEdit.Password)
        locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')


        ########## VALIDADORES #############################################################################################################################################################
        self.validaEmail = QRegularExpressionValidator(QRegularExpression("([a-z0-9]+[.-_])*[a-z0-9]+@[a-z]+(\\.[a-z]{2,})+"))
        self.validaNumeroInt = QRegularExpressionValidator(QRegularExpression("[0-9] \\.-]+"))
        self.validaSalario = QRegularExpressionValidator(QRegularExpression("[0-9]+,?[0-9]{0,2}"))
        self.validaString = QRegularExpressionValidator(QRegularExpression("[a-zA-Z çáàãâéíóôõúÇÁÀÃÂÉÍÓÔÕÚ\\.-]+"))


        ########## MASKS ###################################################################################################################################################################
        self.ui.input_cpf_agendamento_as.setInputMask("000.000.000-00")
        self.ui.input_cpf_usuario_as.setInputMask("000.000.000-00")
        self.ui.input_cpf_cuidador_as.setInputMask("000.000.000-00")
        self.ui.input_cpf_colaborador_as.setInputMask("000.000.000-00")
        self.ui.input_cpf_pagina_consulta_geral.setInputMask("000.000.000-00")
        self.ui.input_cpf_pagina_consulta_geral_psi.setInputMask("000.000.000-00")
        self.ui.input_cpf_pagina_participante_geral.setInputMask("000.000.000-00")


        ########## COLOCANDO OS VALIDADORES ################################################################################################################################################
        self.ui.input_nome_usuario_as.setValidator(self.validaString)
        self.ui.input_nome_cuidador_as.setValidator(self.validaString)
        self.ui.input_nome_colaborador_as.setValidator(self.validaString)  

        self.ui.input_orgao_expedidor_usuario_as.setValidator(self.validaString) 
        self.ui.input_orgao_expedidor_cuidador_as.setValidator(self.validaString)
        self.ui.input_orgao_expedidor_colaborador_as.setValidator(self.validaString) 
         
           
        ########## ARRUMANDO DATA PADRÃO ###################################################################################################################################################     
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

        self.ui.input_inicio_periodo_relatorio_fisio.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_inicio_periodo_relatorio_fisio.setDateTime(QDateTime.currentDateTime())
        self.ui.input_final_periodo_relatorio_fisio.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_final_periodo_relatorio_fisio.setDateTime(QDateTime.currentDateTime())


        self.ui.input_inicio_periodo_relatorio_cuidadores_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_inicio_periodo_relatorio_cuidadores_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_final_periodo_relatorio_cuidadores_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_final_periodo_relatorio_cuidadores_as.setDateTime(QDateTime.currentDateTime())
        
        self.ui.input_inicio_periodo_relatorio_clinicas_cadastradas_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_inicio_periodo_relatorio_clinicas_cadastradas_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_final_periodo_relatorio_relatorio_clinicas_cadastradas_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_final_periodo_relatorio_relatorio_clinicas_cadastradas_as.setDateTime(QDateTime.currentDateTime())

        self.ui.input_inicio_periodo_relatorio_fornecedores_cadastrados.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_inicio_periodo_relatorio_fornecedores_cadastrados.setDateTime(QDateTime.currentDateTime())
        self.ui.input_final_periodo_relatorio_relatorio_fornecedores_cadastrados.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_final_periodo_relatorio_relatorio_fornecedores_cadastrados.setDateTime(QDateTime.currentDateTime())

        

        self.ui.input_inicio_periodo_relatorio_nutri.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_inicio_periodo_relatorio_nutri.setDateTime(QDateTime.currentDateTime())
        self.ui.input_final_periodo_relatorio_nutri.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_final_periodo_relatorio_nutri.setDateTime(QDateTime.currentDateTime())

        ###############SIGNALS################# 
        self.ui.btn_sair_as.clicked.connect(self.sairSistema)
        self.ui.input_data_cadastro_retirada_beneficio.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_data_cadastro_retirada_beneficio.setDateTime(QDateTime.currentDateTime())
        self.ui.input_inicio_periodo_relatorio_atendimentos.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_inicio_periodo_relatorio_atendimentos.setDateTime(QDateTime.currentDateTime())
        self.ui.input_final_periodo_relatorio_atendimentos.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_final_periodo_relatorio_atendimentos.setDateTime(QDateTime.currentDateTime())
        ##########RELATORIO AGENDAMENTO##########################################
        self.ui.input_inicio_periodo_relatorio_gendamento_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_final_periodo_relatorio_agendamento_as.setDisplayFormat("dd/MM/yyyy")
        self.ui.input_inicio_periodo_relatorio_gendamento_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_final_periodo_relatorio_agendamento_as.setDateTime(QDateTime.currentDateTime())
        ###############SIGNALS################# 

        # self.ui.btn_entrar_login.clicked.connect(lambda: self.ui.inicio.setCurrentWidget(self.ui.area_principal))


        ########################### LOGIN ##################################################################################################################################################
        self.ui.btn_entrar_login.clicked.connect(self.validarLogin)


        ########################### VISIBILIDADE ###########################################################################################################################################
        self.ui.toolButton.clicked.connect(self.visibilidade)        

        
        ########################### ASSISTENTE SOCIAL ######################################################################################################################################
        self.ui.btn_cadastrar_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_atendimento_as.clicked.connect(self.limparCamposAtendimentoAssistenteSocial)
        self.ui.btn_atendimento_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_consulta))
        self.ui.btn_cadastrar_beneficios_as.clicked.connect(self.limparCamposCadastroBeneficios)
        self.ui.btn_cadastrar_beneficios_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_beneficios_as))
        self.ui.btn_voltar_cadastro_beneficio.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_parceiros))
        self.ui.btn_cadastrar_cuidador_usuario_as.clicked.connect(self.limparCamposCadastroUsuario)
        self.ui.btn_cadastrar_cuidador_usuario_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_usuario_as))
        self.ui.btn_proximo_as.clicked.connect(self.limparCamposCadastroCuidador)
        self.ui.btn_proximo_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_cuidador_as))   
        self.ui.btn_cadastrar_cursos_oficinas_as.clicked.connect(self.limparCamposCursosOficinas)
        self.ui.btn_cadastrar_cursos_oficinas_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastrar_cursos_e_oficinas_as))
        self.ui.btn_cadastrar_colaborador_as.clicked.connect(self.limparCamposCadastroColaborador)
        self.ui.btn_cadastrar_colaborador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_colaborador_as))
        self.ui.btn_relatorios_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_relatorio))
        self.ui.btn_relatorio_pessoas.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_relatorios_as))
        self.ui.btn_relatorio_pessoas.clicked.connect(self.limparCamposRelatorioPessoas)
        self.ui.btn_cadastro_retirada_de_beneficios.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastrar_retirada_beneficios_as))
        self.ui.btn_agenda_as.clicked.connect(self.limparCamposAgendaAssistenteSocial)
        self.ui.btn_agenda_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_agenda_as))
        self.ui.btn_cadastrar_alterar_dados_as.clicked.connect(self.limparCamposAlterarDadosCadastrais)
        self.ui.btn_cadastrar_alterar_dados_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_alterar_dados_as))
        self.ui.btn_buscar_alterar_as.clicked.connect(lambda: self.ui.stackedWidget_8.setCurrentWidget(self.buscar_Usuario()))        
        self.ui.btn_parceiros_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_parceiros))
        self.ui.btn_voltar_clinica_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_parceiros))
        self.ui.btn_cadastrar_clinica_as.clicked.connect(self.limparCamposCadastroClinica)
        self.ui.btn_cadastrar_clinica_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_clinica_as))
        self.ui.btn_cadastrar_fornecedores_as.clicked.connect(self.limparCamposCadastroFornecedor)
        self.ui.btn_cadastrar_fornecedores_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_fornecedor_as))
        self.ui.btn_lista_pessoas_cursos_as.clicked.connect(self.limparCamposCadastroParticipante)
        self.ui.btn_voltar_fornecedor_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_parceiros))
        self.ui.btn_lista_pessoas_cursos_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastrar_participante))     
        self.ui.btn_voltar_pagina_relatorio_fornecedores_cadastrados.clicked.connect(self.limparCamposCadastroFornecedor)
        self.ui.btn_voltar_pagina_relatorio_fornecedores_cadastrados.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_fornecedor_as))
        self.ui.btn_alterar_pagina_consulta_geral.clicked.connect(self.alterar_usuario_consulta)
        self.ui.input_situacao_trabalho_usuario_as.currentIndexChanged.connect(self.on_tipo_usuario_changed)
        self.ui.input_situacao_trabalho_alterar_usuario_as.currentIndexChanged.connect(self.on_tipo_alterar_usuario_changed)
        self.ui.input_patologia_base_usuario_as.currentIndexChanged.connect(self.on_patologia_base_usuario_changed)
        self.ui.input_alterar_patologia_base_usuario_as.currentIndexChanged.connect(self.on_patologia_base_usuario_alterar)
        self.ui.input_tipo_deficiencia_usuario_as.setDisabled(True)
        self.ui.input_pessoa_cdeficiencia_sim_usuario_as.clicked.connect(self.pessoa_com_deficiencia)        
        self.ui.input_pessoa_cdeficiencia_nao_usuario_as.clicked.connect(self.pessoa_com_deficiencia)
        self.ui.input_alterar_tipo_deficiencia_usuario_as.setDisabled(True)
        self.ui.input_alterar_pessoa_cdeficiencia_sim_usuario_as.clicked.connect(self.pessoa_com_deficiencia_alterar)
        self.ui.input_alterar_pessoa_cdeficiencia_nao_usuario_as.clicked.connect(self.pessoa_com_deficiencia_alterar)
        self.ui.input_tipo_deficiencia_usuario_as.currentIndexChanged.connect(self.on_tipo_deficiencia_usuario_changed)
        self.ui.input_alterar_tipo_deficiencia_usuario_as.currentIndexChanged.connect(self.on_alterar_tipo_deficiencia_usuario_changed)
        self.ui.input_buscar_dados_relatorio_relatorio_clinicas_cadastradas_as.textChanged.connect(self.filtrar_relatorio_clinica_cadastrada)
        self.ui.btn_relatorio_clinicas_cadastradas_as.clicked.connect(self.limparCamposClinicasCadastradas)
        self.ui.btn_relatorio_clinicas_cadastradas_as.clicked.connect(self.puxar_relatorio_clinicas_cadastradas)
        self.ui.btn_relatorio_clinicas_cadastradas_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_relatorio_clinicas_cadastradas))
        self.ui.btn_buscar_relatorio_clinicas_cadastradas_as.clicked.connect(self.filtrar_data_relatorio_clinicas_cadastradas)
        self.ui.btn_buscar_relatorio_fornecedores_cadastrados.clicked.connect(self.filtrar_data_relatorio_fornecedor_cadastrado)
        self.ui.input_buscar_dados_relatorio_relatorio_fornecedor_cadastrado.textChanged.connect(self.filtrar_relatorio_fornecedor_cadastrado)
        self.ui.btn_relatorio_fornecedores_cadastrados.clicked.connect(self.limparCamposFornecedoresCadastrados)
        self.ui.btn_relatorio_fornecedores_cadastrados.clicked.connect(self.puxar_relatorio_fornecedor_cadastrado)
        self.ui.btn_relatorio_fornecedores_cadastrados.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_relatorio_fornecedores_cadastrados))
        self.ui.btn_buscar_relatorio_fornecedores_cadastrados.clicked.connect(self.filtrar_data_relatorio_fornecedor_cadastrado)
        self.ui.btn_voltar_observacoes_sigilosas_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_alterar_dados_as))
        self.ui.btn_relatorio_beneficios.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_relatorio_beneficio_as))
        self.ui.btn_relatorio_beneficios.clicked.connect(self.limparCamposRelatorioBeneficios)
        self.ui.btn_voltar_pagina_participante_geral.clicked.connect(self.limparCamposCursosOficinas)
        self.ui.btn_voltar_pagina_participante_geral.clicked.connect(lambda:self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastrar_cursos_e_oficinas_as))
        self.ui.btn_relatorio_cursos_participantes.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_relatorios_aluno_curso))
        self.ui.btn_relatorio_cursos_participantes.clicked.connect(self.limparCamposRelatorioCursosParticipantes)
        self.ui.btn_voltar_pagina_relatorio_aluno_curso.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_relatorio))
        self.ui.btn_relatorio_cuidadores.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_relatorio_cuidadores))
        self.ui.btn_relatorio_cuidadores.clicked.connect(self.limparCamposRelatorioCuidadores)
        self.ui.btn_voltar_relatorios_cuidadores_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_relatorio))
        self.ui.btn_voltar_pagina_relatorio_clinicas_cadastradas_as.clicked.connect(self.limparCamposCadastroClinica)
        self.ui.btn_voltar_pagina_relatorio_clinicas_cadastradas_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_clinica_as))
        self.ui.btn_relatorios_cadstrados_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_relatorio_atendimento_as))
        self.ui.btn_voltar_pagina_relatorio_atendimentos.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_consulta))
        self.ui.btn_voltar_pagina_relatorio_beneficios_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_relatorio))
        self.ui.btn_voltar_cursos_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_voltar_cuidador_as.clicked.connect(self.limparCamposCadastroUsuario)
        self.ui.btn_voltar_cuidador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cadastro_usuario_as))
        self.ui.btn_voltar_agenda_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_principal_as))
        self.ui.btn_voltar_usuario_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_voltar_pagina_consulta_geral.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_principal_as))
        self.ui.btn_alterar_voltar_usuario_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_alterar_voltar_cuidador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_alterar_voltar_cadastro_colaborador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_voltar_observacoes_sigilosas_as.clicked.connect(lambda: self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_alterar_usuario))
        self.ui.btn_voltar_relatorios_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_relatorio))
        self.ui.btn_voltar_cadastro_colaborador_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_botoes_cadastrar_as))
        self.ui.btn_voltar_cadastro_retirada_beneficio.clicked.connect(self.limparCamposCadastroBeneficios)
        self.ui.btn_voltar_cadastro_retirada_beneficio.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_beneficios_as))
        self.ui.btn_relatorio_agenda_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_relatorio_agendamento_as))
        self.ui.btn_sair_sec.clicked.connect(self.sairSistema)
        self.ui.btn_gerar_excel_relatorio_atendimentos.clicked.connect(self.gerar_excel_relatorio_atendimento)
        self.ui.btn_relatorio_agenda_as.clicked.connect(self.buscar_relatorio_agendamento)
        self.ui.btn_buscar_relatorio_agendamento_as.clicked.connect(self.filter_relatorio_agendamento)
        self.ui.btn_voltar_relatorios_agendamento_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_agenda_as))

        ########################### FISIOTERAPEUTA #########################################################################################################################################
        self.ui.btn_atendimento_fisio.clicked.connect(lambda: self.ui.stackedWidget_11.setCurrentWidget(self.ui.page_consulta_fisio))
        self.ui.btn_agenda_fisio.clicked.connect(lambda: self.ui.stackedWidget_11.setCurrentWidget(self.ui.page_agenda_fisio))
        self.ui.btn_voltar_agenda_fisio.clicked.connect(lambda: self.ui.stackedWidget_11.setCurrentWidget(self.ui.page_principal_fisio))
        self.ui.btn_voltar_pagina_consulta_geral_fisio.clicked.connect(lambda: self.ui.stackedWidget_11.setCurrentWidget(self.ui.page_principal_fisio))
        self.ui.btn_relatorios_fisio.clicked.connect(lambda: self.ui.stackedWidget_11.setCurrentWidget(self.ui.page_relatorio_fisio))
        self.ui.btn_voltar_relatorios_fisio.clicked.connect(lambda: self.ui.stackedWidget_11.setCurrentWidget(self.ui.page_principal_fisio))
        self.ui.btn_salvar_pagina_consulta_geral_fisio.clicked.connect(self.cadastrar_consulta_fisio) #CADASTRO USUARIO CONSULTA FISIO
        self.ui.btn_agenda_fisio.clicked.connect(self.tabela_agendamento_fisio) #TABELA AGENDAMENTO USUARIO FISIO 
        self.ui.btn_salvar_agenda_fisio.clicked.connect(self.cadastroAgendamento_fisio) #CADASTRO AGENDAMENTO USUARIO FISIO
        self.ui.btn_buscar_agendamento_fisio.clicked.connect(self.buscar_usuario_agendamento_fisio) #SELECT USUARIO AGENDAMENTO FISIO
        self.ui.btn_buscar_cpf_pagina_consulta_geral_fisio.clicked.connect(self.buscar_usuario_consulta_fisio) #SELECT USUARIO CONSULTA FISIO
        self.ui.input_buscar_dados_relatorio_fisio.textChanged.connect(self.filtrar_dados_relatorio_fisio)
        self.ui.input_buscar_dados_relatorio_nutri.textChanged.connect(self.filtrar_dados_relatorio_nutri)
        self.ui.btn_relatorios_fisio.clicked.connect(self.puxar_relatorio_fisio)
        self.ui.btn_buscar_relatorio_fisio.clicked.connect(self.filtrar_data_relatorio_fisio)
        self.ui.btn_buscar_relatorio_nutri.clicked.connect(self.filtrar_data_relatorio_nutri)
        self.ui.btn_buscar_relatorio_beneficios_farm.clicked.connect(self.listarBeneficiosFarmaceuticaRelatorioFiltro)
        self.ui.btn_sair_fisio.clicked.connect(self.sairSistema)


        ########################### NUTRICIONISTA ##########################################################################################################################################
        self.ui.btn_atendimento_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_consulta_nutri))
        self.ui.btn_agenda_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_agenda_nutri))
        self.ui.btn_voltar_agenda_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_principal_nutri))
        self.ui.btn_voltar_pagina_consulta_geral_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_principal_nutri))
        self.ui.btn_voltar_pagina_relatorio_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_principal_nutri))
        self.ui.btn_relatorios_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_relatorio_nutri))
        self.ui.btn_relatorios_nutri.clicked.connect(self.relatorio_pessoa_nutri)
        self.ui.btn_agenda_nutri.clicked.connect(self.tabela_agenda_nutri)
        self.ui.btn_buscar_cpf_pagina_consulta_geral_2.clicked.connect(self.buscar_usuario_nutri) #SELECT USUARIO SOZINHO CONSULTA NUTRI
        self.ui.btn_buscar_agendamento_nutri.clicked.connect(self.buscar_usuario_agenda_nutri) #SELECT USUARIO SOZINHO AGENDAMENTO NUTRI
        self.ui.btn_buscar_cpf_pagina_consulta_geral_2.clicked.connect(self.tabela_consulta_nutri_tabela) #SELECT USUARIO + COLABORADOR NUTRI
        self.ui.btn_salvar_agenda_nutri.clicked.connect(self.cadastroAgendamentoNutri) #CADASTRO DO USUARIO NO AGENDAMENTO NUTRI
        self.ui.btn_salvar_pagina_consulta_geral_nutri.clicked.connect(self.cadastrar_consulta_nutri) #CADATRO DO USUARIO NA CONSULTA NUTRI
        self.ui.input_altura_consulta_nutri.textChanged.connect(self.nutri_imc_usuario) #IMC USUARIO CONSULTA NUTRI
        self.ui.btn_relatorios_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_relatorio_nutri))
        self.ui.btn_alterar_pagina_consulta_geral_nutri.clicked.connect(self.alterar_consulta_nutri)
        self.ui.btn_excluir_pagina_consulta_geral_nutri.clicked.connect(self.excluir_usuario_consulta_nutri)
        #self.ui.btn_voltar_relatorios_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_principal_nutri))
        self.ui.btn_sair_nutri.clicked.connect(self.sairSistema)


        ########################### PSICÓLOGA ##############################################################################################################################################
        self.ui.btn_atendimento_psi.clicked.connect(lambda: self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_consulta_psi))
        self.ui.btn_agenda_psi.clicked.connect(lambda: self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_agenda_psi))
        self.ui.btn_agenda_psi.clicked.connect(self.listarAgendamentos_psi)
        self.ui.btn_voltar_agenda_psi.clicked.connect(lambda: self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_principal_psi))
        self.ui.btn_voltar_pagina_consulta_geral_psi.clicked.connect(lambda: self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_principal_psi))
        self.ui.btn_relatorios_psi.clicked.connect(lambda: self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_relatorio_psi))
        #self.ui.btn_voltar_pagina_relatorio_psi.clicked.connect(lambda: self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_principal_psi))
        self.ui.btn_buscar_cpf_pagina_consulta_geral_psi.clicked.connect(self.buscar_dados_consulta_psi) #SELECT USUARIO CONSULTA PSIC
        self.ui.btn_salvar_pagina_consulta_geral_psi.clicked.connect(self.cadastrar_consulta_psi) #CADASTRO CONSULTA USUARIO PSIC
        self.ui.btn_salvar_pagina_consulta_geral_psi.clicked.connect(self.tabela_consulta_psic_tabela) #SELECT USUARIO CONSULTA + COLADB ID
        self.ui.btn_alterar_pagina_consulta_geral_psi.clicked.connect(self.alterar_usuario_consulta_psi) #ALTERAR CONSULTA PSIC
        self.ui.btn_excluir_pagina_consulta_geral_psi.clicked.connect(self.excluir_usuario_consulta_psi) #EXCLUIR USUARIO CONSULTA PSIC
        self.ui.btn_buscar_agendamento_psi.clicked.connect(self.buscarPessoa_psi) #SELECT USUARIO AGENDAMENTO PISC
        self.ui.btn_salvar_agenda_psi.clicked.connect(self.cadastroAgendamento_psi) #CADASTRO AGENDAMENTO USUARIO PISC
        self.ui.btn_alterar_agenda_psi.clicked.connect(self.alterarAgendamentos_psi) #ALTERAR AGENDAMENTO USUARIO PISC
        self.ui.btn_relatorios_psi.clicked.connect(self.puxar_relatorio_psi)
        self.ui.btn_gerar_excel_relatorio_psi.clicked.connect(self.gerar_excel_relatorio_psi)

        #self.ui.btn_voltar_pagina_relatorio_psi.clicked.connect(lambda: self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_principal_psi))
        self.ui.btn_sair_psi.clicked.connect(self.sairSistema)
        

        ########################### FARMACÊUTICA ###########################################################################################################################################
        self.ui.btn_cadastrar_farm.clicked.connect(lambda: self.ui.stackedWidget_10.setCurrentWidget(self.ui.page_cadastrar_farm))
        self.ui.btn_relatorios_farm.clicked.connect(lambda: self.ui.stackedWidget_10.setCurrentWidget(self.ui.page_relatorio_farm))
        self.ui.btn_retirar_farm.clicked.connect(lambda: self.ui.stackedWidget_10.setCurrentWidget(self.ui.page_retirada_farm))
        self.ui.btn_salvar_cadastro_beneficio_farm.clicked.connect(self.cadastro_beneficios_farmaceutica)
        self.ui.btn_cadastrar_farm.clicked.connect(self.listarBeneficiosFarmaceutica)
        self.ui.btn_gerar_excel_relatorio_beneficios_farm.clicked.connect(self.gerar_excel_relatorio_beneficio_farm)
        self.ui.btn_alterar_cadastro_beneficio_farm.clicked.connect(self.alterar_cadastro_beneficios_farmaceutica)
        self.ui.btn_excluir_cadastro_beneficio_farm.clicked.connect(self.excluir_cadastro_beneficios_farmaceutica)
        self.ui.btn_cancelar_cadastro_beneficio_farm.clicked.connect(self.limparCamposCadastroBeneficiosFarmaceutica)
        self.ui.btn_relatorios_farm.clicked.connect(self.listarBeneficiosFarmaceuticaRelatorio)
        self.ui.btn_buscar_codigo_beneficio_cadastro_retirada_beneficio_farm.clicked.connect(self.buscarCodigoRetiradaFarmaceutica)
        self.ui.btn_finalizar_cadastro_retirada_beneficio_farm.clicked.connect(self.cadastro_retirada_beneficios_farmaceutica)
        self.ui.btn_buscar_cpf_cadastro_retirada_beneficio_farm.clicked.connect(self.buscarRetiradaFarmaceutica)
        self.ui.input_buscar_dados_relatorio_beneficios_farm.textChanged.connect(self.listarBeneficiosFarmaceuticaRelatorioFiltro)
        self.ui.btn_buscar_relatorio_beneficios_farm.clicked.connect(self.listarBeneficiosFarmaceuticaRelatorioFiltroData)
        self.ui.btn_sair_farm.clicked.connect(self.sairSistema)

        
        ########################### SECRETARIA ###########################
        self.ui.btn_agenda_sec.clicked.connect(lambda: self.ui.stackedWidget_13.setCurrentWidget(self.ui.page_agenda_sec))
        self.ui.btn_voltar_agenda_sec.clicked.connect(lambda: self.ui.stackedWidget_13.setCurrentWidget(self.ui.page_principal_sec))
        self.ui.btn_relatorios_sec.clicked.connect(lambda: self.ui.stackedWidget_13.setCurrentWidget(self.ui.page_relatorio_sec))
        self.ui.btn_voltar_relatorios_sec.clicked.connect(lambda: self.ui.stackedWidget_13.setCurrentWidget(self.ui.page_principal_sec))


        ########################### AREA SIGILOSA ###########################
        self.ui.btn_alterar_observacoes_sigilo_as.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_observacoes_sigilosas_as))
        self.ui.btn_salvar_observacoes_sigilosas_as.clicked.connect(self.area_sigilosa_salvar_usuario)
        self.ui.btn_salvar_observacoes_sigilosas_as.clicked.connect(self.filtrar_usuario_area_sigilosa)
        self.ui.btn_alterar_observacoes_sigilo_as.clicked.connect(self.filtrar_usuario_area_sigilosa)
        self.ui.btn_alterar_observacoes_sigilosas_as.clicked.connect(self.alterar_usuario_area_sigilosa)


        ########################## CEP #####################################################################################################################################################
        self.ui.btn_cep_buscar_cuidador_as.clicked.connect(self.validarCep)
        self.ui.btn_cep_buscar_usuario_as.clicked.connect(self.validarCep)
        self.ui.btn_cep_buscar_colaborador_as.clicked.connect(self.validarCep)
        self.ui.btn_cep_buscar_clinica_as.clicked.connect(self.validarCep)
        self.ui.btn_alterar_cep_buscar_cuidador_as.clicked.connect(self.validarCep)
        self.ui.btn_alterar_cep_buscar_usuario_as.clicked.connect(self.validarCep)
        self.ui.btn_alterar_cep_buscar_colaborador_as.clicked.connect(self.validarCep)
        self.ui.btn_cep_buscar_fornecedor_as.clicked.connect(self.validarCep)



        ########################### CPF ####################################################################################################################################################
        self.ui.btn_buscar_agendamento_as.clicked.connect(self.buscarPessoa)
        self.ui.btn_buscar_cpf_cadastro_retirada_beneficio.clicked.connect(self.buscarRetirada)
       

        ########################### POPUP RECUPERAR SENHA AS ######################
        self.ui.btn_esqueci_senha_login.clicked.connect(self.recuperarSenha)
        


        ########################### POPUP ALTERAR FOTO E SENHA AS #################
        #self.ui.btn_alterar_foto_colab_as(self.trocarFotoSenha)
        
        
        ########################### POPUP TIRAR E IMPORTAR FOTO AS ################
        self.ui.btn_tirar_foto_usuario_as.clicked.connect(self.tirarImportarFotoUsuario)
        self.ui.btn_tirar_foto_colaborador_as.clicked.connect(self.tirarImportarFotoColaborador)
        self.ui.btn_alterar_foto_colab_as.clicked.connect(self.AlterarFotoColaborador)
        self.ui.btn_alterar_foto_usuario_as.clicked.connect(self.AlterarFotoUsuario)
        self.ui.btn_alterar_foto_colab_as_perfil.clicked.connect(self.trocarFotoSenha)
        


        ########################### POPUP CURSOS E OFICINAS AS ####################
        # self.ui.btn_concluir_cursos_as.clicked.connect(self.cadastroIncompletoCursos)
        self.ui.input_altura_consulta_nutri.textChanged.connect(self.nutri_imc_usuario)
        self.ui.btn_gerar_excel_relatorio_beneficios_as.clicked.connect(self.gerar_excel_relatorio_beneficio)
        self.ui.input_buscar_dados_relatorio_beneficios_as.textChanged.connect(self.filtrar_dados_beneficio)
        self.ui.btn_buscar_relatorio_beneficios_as.clicked.connect(self.filtrar_data_beneficio)

        ########################### BANCO #########################################
        self.ui.btn_salvar_usuario_as.clicked.connect(self.cadastroUsuario)
        self.ui.btn_salvar_as.clicked.connect(self.cadastroCuidador)
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
        self.ui.btn_finalizar_clinica_as.clicked.connect(self.cadastro_clinica)       
        self.ui.input_buscar_dados_relatorio_as.textChanged.connect(self.filtrar_dados)
        self.ui.input_buscar_dados_relatorio_psi.textChanged.connect(self.filtrar_dados_relatorio_psi)
        #self.ui.input_buscar_dados_relatorio_aluno_curso.textChanged.connect(self.filtrar_dados_participantes_curso)
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
        self.ui.btn_lista_pessoas_cursos_as.clicked.connect(self.buscar_curso_evento)
        self.ui.btn_buscar_cpf_pagina_participante_geral.clicked.connect(self.buscar_dados_participante)
        self.ui.btn_salvar_pagina_participante_geral.clicked.connect(self.cadastrar_participante)
        self.ui.btn_buscar_cpf_pagina_participante_geral.clicked.connect(self.puxar_cadastro_participante)
        self.ui.btn_excel_pagina_participante_geral.clicked.connect(self.gerar_excel_participante)
        self.ui.btn_alterar_agenda_as.clicked.connect(self.alterarAgendamentos)
        self.ui.btn_relatorios_as.clicked.connect(self.filtrar_dados)
        self.ui.btn_buscar_codigo_beneficio_cadastro_retirada_beneficio.clicked.connect(self.buscarCodigoRetirada)
        self.ui.btn_relatorio_cursos_participantes.clicked.connect(self.puxar_participantes_curso)
        self.ui.btn_gerar_excel_relatorio_aluno_curso.clicked.connect(self.gerar_excel_paricipante_curso)
        self.ui.btn_buscar_relatorio_psi.clicked.connect(self.filtrar_data_relatorio_psi)
        self.ui.btn_buscar_dados_relatorio_aluno_curso.clicked.connect(self.filtrar_data_participante_curso)
        self.ui.btn_buscar_relatorio_beneficios_as.clicked.connect(self.filtrar_data_beneficio)
        self.ui.btn_gerar_excel_relatorio_beneficios_as.clicked.connect(self.gerar_excel_relatorio_beneficio)
        self.ui.input_buscar_dados_relatorio_beneficios_as.textChanged.connect(self.filtrar_dados_beneficio)
        self.ui.btn_gerar_excel_relatorio_cuidadores_as.clicked.connect(self.gerar_excel_relatorio_cuidador)
        self.ui.input_buscar_dados_relatorio_cuidadores_as.textChanged.connect(self.filtrar_relatorio_cuidador)
        self.ui.btn_buscar_relatorio_cuidadores_as.clicked.connect(self.filtrar_data_relatorio_cuidador)
        self.ui.btn_relatorios_cadstrados_as.clicked.connect(self.puxar_relatorio_atendimento)
        self.ui.input_buscar_dados_relatorio_atendimentos.textChanged.connect(self.filtrar_dados_relatorio_atendimento)
        self.ui.btn_buscar_relatorio_atendimentos.clicked.connect(self.filtrar_data_relatorio_atendimento)
        self.ui.btn_gerar_excel_relatorio_clinicas_cadastradas_as.clicked.connect(self.gerar_excel_relatorio_clinicas_cadastradas)
        self.ui.btn_gerar_excel_relatorio_fornecedores_cadastrados.clicked.connect(self.gerar_excel_relatorio_fornecedor_cadastrado)
        self.ui.btn_gerar_excel_relatorio_agendamento_as.clicked.connect(self.gerar_excel_relatorio_agendamento)
        self.ui.input_buscar_dados_relatorio_agendamento_as.textChanged.connect(self.filtrar_relatorio_agendamento)

      
        
        
        

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
            self.fotoLoginColab(matricula_colaborador)
            # self.cadastroAgendamento(matricula_colaborador)
            if len(login_senha)==0:
                self.ui.inicio.setCurrentWidget(self.ui.login)
                self.loginInvalido() 
            elif perfil[0] == 'adm':
                if login == login_senha[0] and senha == login_senha[1]:            
                    print ("Login realizado com sucesso")
                    nome_colab = self.db.select_nome_usuario(matricula_colaborador)
                    nome_colaborador = nome_colab[0][0]
                    self.ui.lineEdit_recebe_nome_as.setText(nome_colaborador)
                    self.buscarIdColabAssis()
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
                    self.ui.label_ola_nome_farm_3.setText(nome_colaborador)
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
                    self.ui.label_ola_nome_fisio.setText(nome_colaborador)
                    self.LoginFisio()       
                    self.buscarIdColabFisio()
                else:
                    print ("Usuário não encontrado")
                    self.ui.inicio.setCurrentWidget(self.ui.login)
                    self.loginInvalido()    

            elif perfil[0] == 'nutri':
                if login == login_senha[0] and senha == login_senha[1]:            
                    print ("Login realizado com sucesso")
                    nome_colab = self.db.select_nome_usuario(matricula_colaborador)
                    nome_colaborador = nome_colab[0][0]
                    self.ui.label_ola_nutri.setText(nome_colaborador)
                    self.LoginNutri()       
                    self.buscarIdColabNutri()
                    
                else:
                    print ("Usuário não encontrado")
                    self.ui.inicio.setCurrentWidget(self.ui.login)
                    self.loginInvalido() 

            elif perfil[0] == 'psic':
                if login == login_senha[0] and senha == login_senha[1]:            
                    print ("Login realizado com sucesso")
                    nome_colab = self.db.select_nome_usuario(matricula_colaborador)
                    nome_colaborador = nome_colab[0][0]
                    self.ui.label_ola_nome_psi.setText(nome_colaborador)
                    self.LoginPsico() 
                    self.buscarIdColabPsic()
                         
                else:
                    print ("Usuário não encontrado")
                    self.ui.inicio.setCurrentWidget(self.ui.login)
                    self.loginInvalido() 
                    
            elif perfil[0] == 'sec':
                if login == login_senha[0] and senha == login_senha[1]:            
                    print ("Login realizado com sucesso")
                    nome_colab = self.db.select_nome_usuario(matricula_colaborador)
                    nome_colaborador = nome_colab[0][0]
                    self.ui.label_ola_nome_sec.setText(nome_colaborador)
                    self.LoginSec() 
                    # self.buscarIdColabPsic()
                         
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
    ########################### Validar Login Psico #############################        
    def LoginSec(self):
        self.ui.inicio.setCurrentWidget(self.ui.page_secretaria)

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

    def buscarPessoa_psi(self):
        cpf_temp = self.ui.input_cpf_agendamento_psi.text()
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
        self.ui.input_nome_agendamento_psi.setText(nome)
        self.ui.input_telefone_agendamento_psi.setText(telefone)
        self.ui.input_clinica_agendamento_psi.setText(clinica)
        self.listarAgendamentos_psi()
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
            self.ui.input_alterar_telefone_contato_cuidador_as.setText(dados[11]) 
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
            situacao_usuario = str(dados[3])
            print(situacao_usuario)
            if situacao_usuario == "Ativo":
                self.ui.input_alterar_situacao_ativo_usuario_as.setChecked(True)
            elif situacao_usuario == "Inativo":
                self.ui.input_alterar_situacao_inativo_usuario_as.setChecked(True)
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
            elif sexo == "Selecione":
                self.ui.input_alterar_sexo_usuario_as.setCurrentIndex(0)
            
            self.ui.input_alterar_telefone_usuario_as.setText(dados[11]) #
            self.ui.input_alterar_telefone_contato_usuario_as.setText(dados[12]) #
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
                
            elif estadoCivil == "Selecione":
                self.ui.input_alterar_estado_civil_usuario_as.setCurrentIndex(0)

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
            
            elif Escolaridade == "Selecione":
                self.ui.input_alterar_escolaridade_usuario_comboBox_as.setCurrentIndex(0)


            pessoac_deficiencia = str(dados[21])
            print(pessoac_deficiencia)
            if pessoac_deficiencia == "SIM":
                self.ui.input_alterar_pessoa_cdeficiencia_sim_usuario_as.setChecked(True)
            elif pessoac_deficiencia == "NÃO":
                self.ui.input_alterar_pessoa_cdeficiencia_nao_usuario_as.setChecked(True)

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
                
            elif tipoDeDeficiencia == "Selecione":
                self.ui.input_alterar_tipo_deficiencia_usuario_as.setCurrentIndex(0)
                
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
                
            elif mediaRendaFamiliar == "Selecione":
                self.ui.input_alterar_renda_familiar_usuario_as.setCurrentIndex(0)

            meioTransporte = str(dados[25])

            if meioTransporte == 'Particular':
                self.ui.input_alterar_meio_transporte_usuario_as.setCurrentIndex(1)

            elif meioTransporte == 'Carona':
                self.ui.input_alterar_meio_transporte_usuario_as.setCurrentIndex(2)

            elif meioTransporte == 'Ônibus coletivo':
                self.ui.input_alterar_meio_transporte_usuario_as.setCurrentIndex(3)

            elif meioTransporte == 'Ambulância municipal':
                self.ui.input_alterar_meio_transporte_usuario_as.setCurrentIndex(4)

            elif meioTransporte == 'Moto':
                self.ui.input_alterar_meio_transporte_usuario_as.setCurrentIndex(5)

            elif meioTransporte == 'Ambulância particular':
                self.ui.input_alterar_meio_transporte_usuario_as.setCurrentIndex(6)
           
            elif meioTransporte == "Selecione":
                self.ui.input_alterar_meio_transporte_usuario_as.setCurrentIndex(6)
                
            valeTransporte = str(dados[26])

            if valeTransporte == 'Passe para os dias de tratamento':
                self.ui.input_alterar_vale_transporte_usuario_as.setCurrentIndex(1)

            elif valeTransporte == 'Passe do idoso':
                self.ui.input_alterar_vale_transporte_usuario_as.setCurrentIndex(2)

            elif valeTransporte == 'Passe livre':
                self.ui.input_alterar_vale_transporte_usuario_as.setCurrentIndex(3)

            elif valeTransporte == "Selecione":
                self.ui.input_alterar_vale_transporte_usuario_as.setCurrentIndex(0)
            
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
            
            elif situacaoTrabalho == "Selecione":
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

            elif beneficio == "Selecione":
                self.ui.input_alterar_beneficios_usuario_as.setCurrentIndex(0)
                
            tarifa_social = str(dados[30])
            if tarifa_social == "SIM":
                self.ui.input_alterar_tarifa_social_sim_usuario_as.setChecked(True)
            elif tarifa_social == "NÃO":
                self.ui.input_alterar_tarifa_social_nao_usuario_as.setChecked(True)


            tipoTratamento = str(dados[31])

            if tipoTratamento == 'Pré-Diálise':
                self.ui.input_alterar_tipo_tratamento_usuario_as.setCurrentIndex(1)
            
            elif tipoTratamento == 'Hemodiálise':
                self.ui.input_alterar_tipo_tratamento_usuario_as.setCurrentIndex(2)

            elif tipoTratamento == 'Diálise Peritoneal':
                self.ui.input_alterar_tipo_tratamento_usuario_as.setCurrentIndex(3)

            elif tipoTratamento == "Selecione":
                self.ui.input_alterar_tipo_tratamento_usuario_as.setCurrentIndex(0)
                
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
                
            elif patologiaBase == "Selecione":
                self.ui.input_alterar_patologia_base_usuario_as.setCurrentIndex(0)
                

            self.ui.input_alterar_outras_patologias_usuario_as.setText(dados[34])

            self.ui.input_alterar_data_inicio_usuario_as.setDate(QDate(dados[35]))

            periodo = dados[36]

            if periodo == 'Matutino':
                self.ui.input_alterar_periodo_usuario_as.setCurrentIndex(1)

            elif periodo == 'Vespertino':
                self.ui.input_alterar_periodo_usuario_as.setCurrentIndex(2)

            elif periodo == 'Noturno':
                self.ui.input_alterar_periodo_usuario_as.setCurrentIndex(3)
                
            elif periodo == "Selecione":
                self.ui.input_alterar_periodo_usuario_as.setCurrentIndex(0)
                
                
            self.ui.input_alterar_id_endereco_usuario_as.setText(str(dados[37]))
            self.ui.input_alterar_id_endereco_usuario_as.hide()
            self.ui.input_alterar_id_usuario_as.setText(str(dados[38]))
            self.ui.input_alterar_id_usuario_as.hide()
            foto = str(dados[39])
            if foto == None or foto == '':
                original_image = cv2.imread("./icons/adicionar foto.png")

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

                
            else:
                print(dados[39])
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
            situacao_colab = str(dados[5])
            if situacao_colab == "Ativo":
                self.ui.input_alterar_situacao_ativo_colaborador_as.setChecked(True)
            elif situacao_colab == "Inativo":
                self.ui.input_alterar_situacao_inativo_colaborador_as.setChecked(True)
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
            foto = str(dados[27])
            if foto == None or foto == '':
                original_image = cv2.imread("./icons/adicionar foto.png")

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
        
    
            else:
                
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
        telefone_contato = self.ui.input_alterar_telefone_contato_cuidador_as.text()  
        tupla_pessoa = (id_matricula,nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,telefone,telefone_contato)
        

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
        id_matricula = self.ui.input_alterar_id_usuario_as.text()
        id_matricula_usuario = self.ui.input_alterar_matricula_usuario_as.text()

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
        telefone_contato = self.ui.input_alterar_telefone_contato_usuario_as.text()
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
        

        tupla_pessoa = (id_matricula,nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status,telefone,telefone_contato,escolaridade,estado_civil,pessoa_deficiencia,tipo_deficiencia,outras_deficiencias)
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
        ##ALTERAÇÃO PARA CADASTRAR COLABORADOR
        tupla_colaborador = (pis_colab,data_admissao,salario,cargo,periodo,login,senha)

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

        format =  ["png", "jpg", "jpeg", "gif", "bmp", "ico"]
        
        if nome_colab == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Insira um Nome")
            msg.setText("Insira um nome para salvar a imagem")
            msg.exec()
            return
        
        else:

            file_path, _ = QFileDialog.getOpenFileName(self, "Selecionar Imagem", "", "Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ico);;Todos os arquivos (*)", options=options)
            caminho_importado = file_path
            formato_importado = imghdr.what(caminho_importado)

            if formato_importado not in format:

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Erro ao importar")
                msg.setText("Erro ao improtar a Imagem\nDeseja importar novamente?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                resposta = msg.exec()
                
                if resposta == QMessageBox.Yes:
                    file_dialog = QFileDialog()
                    file_path, _ = file_dialog.getOpenFileName(None, "Selecionar Imagem", "", "Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ico);;Todos os arquivos (*)", options=options)
                    caminho_importado = file_path
                    formato_importado = imghdr.what(caminho_importado)
                    print(formato_importado)
                    
                    if formato_importado not in format:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Erro ao importar")
                        msg.setText("Erro ao improtar a Imagem\nTente Novamente")
                        msg.exec() 
                        return
                        
                    if formato_importado in format:
                        
                        tupla_foto = (id_foto,nome_colab, caminho_importado)
                        result = self.db.alterar_foto_colaborador(tupla_foto) 
                        
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Imagem Salva")
                        msg.setText("Imagem Salva com Sucesso!!!")
                        msg.exec() 
                          
                if resposta == QMessageBox.No:
                    return
            
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
            msg.setText("Foto do Colaborador Atualizada com sucesso!")
            msg.exec()



    def AlterarFotoUsuario(self):
        nome_usua = self.ui.input_alterar_nome_usuario_as.text()
        id_foto = self.ui.input_id_foto_alterar_usuario_as.text()
        
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        
        format =  ["png", "jpg", "jpeg", "gif", "bmp", "ico"]

        if nome_usua == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Insira um Nome")
            msg.setText("Insira um nome para salvar a imagem")
            msg.exec()
            return
        
        else:
            file_path, _ = QFileDialog.getOpenFileName(self, "Selecionar Imagem", "", "Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ico);;Todos os arquivos (*)", options=options)
            caminho_importado = file_path
            formato_importado = imghdr.what(caminho_importado)
 
        
            if formato_importado not in format:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Erro ao importar")
                msg.setText("Erro ao improtar a Imagem\nDeseja importar novamente?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                resposta = msg.exec()
                    
                if resposta == QMessageBox.Yes:
                    file_dialog = QFileDialog()
                    file_path, _ = file_dialog.getOpenFileName(None, "Selecionar Imagem", "", "Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ico);;Todos os arquivos (*)", options=options)
                    caminho_importado = file_path
                    formato_importado = imghdr.what(caminho_importado)
                    print(formato_importado)
                    
                    if formato_importado not in format:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Erro ao importar")
                        msg.setText("Erro ao improtar a Imagem\nTente Novamente")
                        msg.exec() 
                        return
                        
                    if formato_importado in format:
                        
                        tupla_foto = (id_foto, nome_usua, caminho_importado)
                        result = self.db.alterar_foto_usuario(tupla_foto) 
                        
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Imagem Salva")
                        msg.setText("Imagem Salva com Sucesso!!!")
                        msg.exec() 

                if resposta == QMessageBox.No:
                    return
                
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

    
    def buscarIdColabAssis(self):
        login = self.ui.input_usuario_login.text()
        print("Login Assis ->", login)
        id_colab_colab = self.db.buscarIdColabAssis(login)
        id_colab_nt = id_colab_colab[0][0]
        self.id_colab_tratado_ass = id_colab_nt
        print("ID ASSISTENTE ->", self.id_colab_tratado_ass)

    
    def buscarIdColabPsic(self):
        login = self.ui.input_usuario_login.text()
        print("Login Pisc ->", login)
        id_colab_colab = self.db.buscarIdColabPsic(login)
        id_colab_nt = id_colab_colab[0][0]
        self.id_colab_tratado_psic = id_colab_nt
        print("ID PSIC ->", self.id_colab_tratado_psic)


    def buscarIdColabNutri(self):
        login = self.ui.input_usuario_login.text()
        print("Login Nutri ->", login)
        id_colab_nutri = self.db.buscarIdColabNutri(login)
        id_colab_nutri_nt = id_colab_nutri[0][0]
        self.id_colab_tratado_nutri = id_colab_nutri_nt
        print(self.id_colab_tratado_nutri)
        return self.id_colab_tratado_nutri

    def buscarIdColabFisio(self):
        login = self.ui.input_usuario_login.text()
        print("Login Fisio ->", login)
        id_colab_fisio= self.db.buscarIdColabFisio(login)
        id_colab_fisio_nt = id_colab_fisio[0][0]
        self.id_colab_tratado_fisio = id_colab_fisio_nt
        print("ID FISIO ->",self.id_colab_tratado_fisio)

    def filtrar_dados_relatorio_fisio(self):
        txt = re.sub('[\W_]+','',self.ui.input_buscar_dados_relatorio_fisio.text())
        res = self.db.buscar_relatorio_fisio_pesquisa(txt)
        self.ui.input_TableWidget_relatorio_fisio.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_fisio.setItem(row, column, QTableWidgetItem(str(data)))
                
    def filtrar_dados_relatorio_nutri(self):
        txt = re.sub('[\W_]+','',self.ui.input_buscar_dados_relatorio_nutri.text())
        res = self.db.buscar_relatorio_nutri_pesquisa(txt)
        self.ui.input_TableWidget_relatorio_nutri.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_nutri.setItem(row, column, QTableWidgetItem(str(data)))
    
    def filtrar_relatorio_clinica_cadastrada(self):
        txt = re.sub('[\W_]+','',self.ui.input_buscar_dados_relatorio_relatorio_clinicas_cadastradas_as.text())
        res = self.db.buscar_relatorio_clinica_cadastrada_pesquisa(txt)
        self.ui.input_TableWidget_relatorio_relatorio_clinicas_cadastradas_as.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_relatorio_clinicas_cadastradas_as.setItem(row, column, QTableWidgetItem(str(data)))
    
    def filtrar_relatorio_fornecedor_cadastrado(self):
        txt = re.sub('[\W_]+','',self.ui.input_buscar_dados_relatorio_relatorio_fornecedor_cadastrado.text())
        res = self.db.buscar_relatorio_fornecedor_cadastrado_pesquisa(txt)
        self.ui.input_TableWidget_relatorio_relatorio_fornecedores_cadastrados.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_relatorio_fornecedores_cadastrados.setItem(row, column, QTableWidgetItem(str(data)))
    
    def puxar_relatorio_fisio(self):
        result = self.db.buscar_relatorio_fisio()
        self.ui.input_TableWidget_relatorio_fisio.clearContents()
        self.ui.input_TableWidget_relatorio_fisio.setRowCount(len(result))   

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_fisio.setItem(row, column,QTableWidgetItem(str(data)))

    def puxar_relatorio_cuidador(self):
        result = self.db.relatorio_cuidador()
        self.ui.tableWidget_relatorio_cuidadores_as.clearContents()
        self.ui.tableWidget_relatorio_cuidadores_as.setRowCount(len(result))   

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.tableWidget_relatorio_cuidadores_as.setItem(row, column,QTableWidgetItem(str(data)))
    
    def puxar_relatorio_clinicas_cadastradas(self):
        result = self.db.buscar_relatorio_clinica_cadastrada()
        self.ui.input_TableWidget_relatorio_relatorio_clinicas_cadastradas_as.clearContents()
        self.ui.input_TableWidget_relatorio_relatorio_clinicas_cadastradas_as.setRowCount(len(result))   

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_relatorio_clinicas_cadastradas_as.setItem(row, column,QTableWidgetItem(str(data)))

    def puxar_relatorio_fornecedor_cadastrado(self):
        result = self.db.buscar_relatorio_fornecedor_cadastrado()
        self.ui.input_TableWidget_relatorio_relatorio_fornecedores_cadastrados.clearContents()
        self.ui.input_TableWidget_relatorio_relatorio_fornecedores_cadastrados.setRowCount(len(result))   

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_relatorio_fornecedores_cadastrados.setItem(row, column,QTableWidgetItem(str(data)))



                
    def filtrar_relatorio_cuidador(self):
        txt = re.sub('[\W_]+','',self.ui.input_buscar_dados_relatorio_cuidadores_as.text())
        res = self.db.filtrar_relatorio_cuidador(txt)
        print(res)
        self.ui.tableWidget_relatorio_cuidadores_as.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.tableWidget_relatorio_cuidadores_as.setItem(row, column, QTableWidgetItem(str(data)))

    def filtrar_data_relatorio_cuidador(self):  
        texto_data_inicio_cuidador = self.ui.input_inicio_periodo_relatorio_cuidadores_as.text()
        texto_data_final_cuidador = self.ui.input_final_periodo_relatorio_cuidadores_as.text()
        texto_data_inicio_cuidador =  "-".join(texto_data_inicio_cuidador.split("/")[::-1])
        texto_data_final_cuidador =  "-".join(texto_data_final_cuidador.split("/")[::-1])
        
        res = self.db.filter_data_relatorio_cuidador(texto_data_inicio_cuidador,texto_data_final_cuidador)

        self.ui.tableWidget_relatorio_cuidadores_as.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.tableWidget_relatorio_cuidadores_as.setItem(row, column, QTableWidgetItem(str(data)))

    def filtrar_data_relatorio_fisio(self):  
        texto_data_inicio_fisio = self.ui.input_inicio_periodo_relatorio_fisio.text()
        texto_data_final_fisio = self.ui.input_final_periodo_relatorio_fisio.text()
        texto_data_inicio_fisio =  "-".join(texto_data_inicio_fisio.split("/")[::-1])
        texto_data_final_fisio =  "-".join(texto_data_final_fisio.split("/")[::-1])
        
        res = self.db.filter_data_relatorio_fisio(texto_data_inicio_fisio,texto_data_final_fisio)

        self.ui.input_TableWidget_relatorio_fisio.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_fisio.setItem(row, column, QTableWidgetItem(str(data)))
    
    def filtrar_data_relatorio_clinicas_cadastradas(self):  
        texto_data_inicio_clinica_cadastrada = self.ui.input_inicio_periodo_relatorio_clinicas_cadastradas_as.text()
        texto_data_final_clinica_cadastrada = self.ui.input_final_periodo_relatorio_relatorio_clinicas_cadastradas_as.text()
        texto_data_inicio_clinica_cadastrada =  "-".join(texto_data_inicio_clinica_cadastrada.split("/")[::-1])
        texto_data_final_clinica_cadastrada =  "-".join(texto_data_final_clinica_cadastrada.split("/")[::-1])
        
        res = self.db.filter_data_relatorio_clinica_cadastrada(texto_data_inicio_clinica_cadastrada,texto_data_final_clinica_cadastrada)

        self.ui.input_TableWidget_relatorio_relatorio_clinicas_cadastradas_as.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_relatorio_clinicas_cadastradas_as.setItem(row, column, QTableWidgetItem(str(data)))

    def filtrar_data_relatorio_nutri(self):  
        texto_data_inicio_nutri = self.ui.input_inicio_periodo_relatorio_nutri.text()
        texto_data_final_nutri = self.ui.input_final_periodo_relatorio_nutri.text()
        texto_data_inicio_nutri =  "-".join(texto_data_inicio_nutri.split("/")[::-1])
        texto_data_final_nutri =  "-".join(texto_data_final_nutri.split("/")[::-1])
        id_relatorio_nutri = self.buscarIdColabNutri()
        res = self.db.filter_data_relatorio_nutri(texto_data_inicio_nutri,texto_data_final_nutri,id_relatorio_nutri)

        self.ui.input_TableWidget_relatorio_nutri.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_nutri.setItem(row, column, QTableWidgetItem(str(data)))
    def filtrar_data_relatorio_fornecedor_cadastrado(self):  
        texto_data_inicio_fornecedor_cadastrado = self.ui.input_inicio_periodo_relatorio_fornecedores_cadastrados.text()
        texto_data_final_fornecedor_cadastrado = self.ui.input_final_periodo_relatorio_relatorio_fornecedores_cadastrados.text()
        texto_data_inicio_fornecedor_cadastrado =  "-".join(texto_data_inicio_fornecedor_cadastrado.split("/")[::-1])
        texto_data_final_fornecedor_cadastrado =  "-".join(texto_data_final_fornecedor_cadastrado.split("/")[::-1])
        
        res = self.db.filter_data_relatorio_fornecedor_cadastrado(texto_data_inicio_fornecedor_cadastrado,texto_data_final_fornecedor_cadastrado)

        self.ui.input_TableWidget_relatorio_relatorio_fornecedores_cadastrados.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_relatorio_fornecedores_cadastrados.setItem(row, column, QTableWidgetItem(str(data)))







    def tabela_agenda_nutri(self): #TABELA TODOS OS AGENDAMENTOS
        result = self.db.busca_nutri_agendamento_tabela()
        self.ui.input_TableWidget_agendamento_nutri.clearContents()
        self.ui.input_TableWidget_agendamento_nutri.setRowCount(len(result))   

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_agendamento_nutri.setItem(row, column,QTableWidgetItem(str(data)))
                
    def tabela_consulta_nutri_tabela(self): #TABELA CONSULTA USUARIO NUTRI
        cpf_tmp = self.ui.input_cpf_pagina_consulta_geral_nutri.text()
        cpf = re.sub(r'[^\w\s]','',cpf_tmp)
        result = self.db.busca_nutri_consulta_tabela(cpf, self.id_colab_tratado_nutri)
        self.ui.input_TableWidget_pagina_consulta_geral_nutri.clearContents()
        self.ui.input_TableWidget_pagina_consulta_geral_nutri.setRowCount(len(result))   

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_pagina_consulta_geral_nutri.setItem(row, column,QTableWidgetItem(str(data)))
                
    def tabela_consulta_psic_tabela(self): #TABELA CONSULTA USUARIO PSIC
        cpf_tmp = self.ui.input_cpf_pagina_consulta_geral_psi.text()
        cpf = re.sub(r'[^\w\s]','',cpf_tmp)
        print("cpf cpnsulta psic ->", cpf)
        result = self.db.busca_psic_consulta_tabela(cpf, self.id_colab_tratado_psic)
        print(result)
        self.ui.input_TableWidget_pagina_consulta_geral_psi.clearContents()
        self.ui.input_TableWidget_pagina_consulta_geral_psi.setRowCount(len(result))   

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_pagina_consulta_geral_psi.setItem(row, column,QTableWidgetItem(str(data)))


    def tabela_agendamento_fisio(self): #TABELA TODOS OS AGENDAMENTOS FISIO
        result = self.db.busca_fisio_agendamento_tabela()
        self.ui.input_TableWidget_agendamento_fisio.clearContents()
        self.ui.input_TableWidget_agendamento_fisio.setRowCount(len(result))   

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_agendamento_fisio.setItem(row, column,QTableWidgetItem(str(data)))
    
    def nutri_imc_usuario(self):
        peso = int(self.ui.input_peso_consulta_nutri.text())
        altura = float(self.ui.input_altura_consulta_nutri.text())
        altura2x = altura ** altura
        imc = peso//altura2x
        self.ui.input_imc_consulta_nutri.setText(str(imc))

    def buscar_usuario_nutri(self):
        cpf = self.ui.input_cpf_pagina_consulta_geral_nutri.text()
        dados = self.db.busca_usuario_nutri_consulta(cpf)
        print(dados)
        if dados[8] == "SIM":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Usuario Agendamento")
            msg.setText("Usuario nao possui agendamento!!")
            msg.exec()
            return
        
                    
        elif dados[8] == "NAO":
            self.ui.input_nome_pagina_consulta_geral_nutri.setText(dados[0])
            self.ui.input_contato_pagina_consulta_geral_nutri.setText(dados[1])
            self.ui.input_clinica_pagina_consulta_geral_nutri.setText(dados[2])

            tipo_pat = str(dados[3])

            if tipo_pat == "":
                self.ui.input_tipo_tratamento_consulta_nutri.setCurrentIndex(0)
            elif tipo_pat == "Transplantado/a":
                self.ui.input_tipo_tratamento_consulta_nutri.setCurrentIndex(1)
            elif tipo_pat == "Prevenção":
                self.ui.input_tipo_tratamento_consulta_nutri.setCurrentIndex(2)
            elif tipo_pat == "Pré-Diálise":
                self.ui.input_tipo_tratamento_consulta_nutri.setCurrentIndex(3)
            elif tipo_pat == "Hemodiálise":
                self.ui.input_tipo_tratamento_consulta_nutri.setCurrentIndex(4)
            elif tipo_pat == "Diálise Peritoneal":
                self.ui.input_tipo_tratamento_consulta_nutri.setCurrentIndex(5)
                
            pat_base = str(dados[4])
            
            if pat_base == "":
                self.ui.input_patologia_base_consulta_nutri.setCurrentIndex(0)
            elif pat_base == "Hipertensão":
                self.ui.input_patologia_base_consulta_nutri.setCurrentIndex(1)
            elif pat_base == "Diabete 1":
                self.ui.input_patologia_base_consulta_nutri.setCurrentIndex(2)
            elif pat_base == "Diabete 2":
                self.ui.input_patologia_base_consulta_nutri.setCurrentIndex(3)
            elif pat_base == "Lúpus":
                self.ui.input_patologia_base_consulta_nutri.setCurrentIndex(4)
            elif pat_base == "Nefrites":
                self.ui.input_patologia_base_consulta_nutri.setCurrentIndex(5)
            elif pat_base == "Outros":
                self.ui.input_patologia_base_consulta_nutri.setCurrentIndex(6)

            self.ui.input_data_pagina_consulta_geral_nutri.setDate(QDate(dados[5]))

            self.ui.input_hora_consulta_as_nutri.setText(str(dados[6]))
            self.ui.input_id_matricula_nutri_consulta.setText(str(dados[7]))
            self.ui.input_id_matricula_nutri_consulta.hide()
            self.tabela_consulta_nutri_tabela()
        
    def buscar_usuario_agenda_nutri(self):
        cpf = self.ui.input_cpf_agendamento_nutri.text()
        dados = self.db.busca_usuario_nutri_agendamento(cpf)
        print(dados)
        self.ui.input_nome_agendamento_nutri.setText(dados[0])
        self.ui.input_telefone_agendamento_nutri.setText(dados[1])
        self.ui.input_clinica_agendamento_nutri.setText(dados[2])
        self.ui.input_id_matricula_nutri_agendamento.setText(str(dados[3]))
        self.ui.input_id_matricula_nutri_agendamento.hide()

    def buscar_usuario_agendamento_fisio(self):
        cpf = self.ui.input_cpf_agendamento_fisio.text()
        dados = self.db.busca_usuario_agendamento_fisio(cpf)
        print(dados)
        self.ui.input_nome_agendamento_fisio.setText(dados[0])
        self.ui.input_telefone_agendamento_fisio.setText(dados[1])
        self.ui.input_clinica_agendamento_fisio.setText(dados[2])
        self.ui.input_id_matricula_agendamento_fisio.setText(str(dados[3]))
        self.ui.input_id_matricula_agendamento_fisio.hide()


    def buscar_usuario_consulta_fisio(self):
        cpf = self.ui.input_cpf_pagina_consulta_geral_fisio.text()
        dados = self.db.busca_usuario_consulta_fisio_puxar(cpf)
        print(dados)
        if dados[6] == "SIM":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Usuario Agendamento")
            msg.setText("Usuario nao possui agendamento!!")
            msg.exec()
            print(dados[6])
        elif dados[6] == "NAO":   
            self.ui.input_nome_pagina_consulta_geral_fisio.setText(dados[0])
            self.ui.input_contato_pagina_consulta_geral_fisio.setText(dados[1])
            self.ui.input_clinica_pagina_consulta_geral_fisio.setText(dados[2])
            self.ui.input_data_pagina_consulta_geral_fisio.setDate(QDate(dados[3]))
            self.ui.input_hora_consulta_as_fisio.setText(str(dados[4]))
            self.ui.input_id_matricula_consulta_fisio.setText(str(dados[5]))
            self.ui.input_id_matricula_consulta_fisio.hide()
            self.puxar_consulta_fisio()

    def puxar_consulta_fisio(self):

        cpf_temp = self.ui.input_cpf_pagina_consulta_geral_fisio.text()
        cpf = ''
        for i in cpf_temp:
            if i == '.' or i == '-':
                pass
            else:
                cpf += i
        result = self.db.buscar_consulta_fisio(cpf, self.id_colab_tratado_fisio)
        self.ui.input_TableWidget_pagina_consulta_geral_fisio.clearContents()
        self.ui.input_TableWidget_pagina_consulta_geral_fisio.setRowCount(len(result))   

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_pagina_consulta_geral_fisio.setItem(row, column,QTableWidgetItem(str(data)))


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
        self.nome_usuario = nome
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
        telefone_contato = self.ui.input_telefone_contato_usuario_as.text()
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

        
        tupla_pessoa = (nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status,telefone,telefone_contato,escolaridade,estado_civil,pessoa_deficiencia,tipo_deficiencia,outras_deficiencias)
        tupla_usuario = (nis,cns,observacao_,situacao_trabalho,situacao_trabalho_outros,tipo_transporte,tipo_tratamento,beneficio,local_tratamento_id_clinica,periodo,data_inicio,patologia_base,outras_patologias,tarifa_social,media_renda_familiar,vale_transporte)
        
        
        if not validarCamposUsuarioCadastro(cpf,rg,nis,cns,telefone,sexo,cep,numero):
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("ERRO")
            msg.setText("Erro ao tentar cadastrar Usuario!")
            msg.exec()
        else:
        ######################## insert ##################################

            result = []
            result = self.db.cadastro_usuario(tupla_endereco,tupla_pessoa,tupla_usuario)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Usuário")
            msg.setText("Usuário cadastrado com sucesso!")
            msg.exec()
            # self.msg(result[0],result[1])
            # self.limparCamposCadastroUsuario()
    
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
    
    def listarAgendamentos_psi(self):
        res = self.db.select_agendamentos_psi()

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_agendamento_psi.setItem(row, column, QTableWidgetItem(str(data)))

    def listarBeneficios(self):
        resultado = self.db.busca_beneficios()
        
        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_cadastro_beneficio.setItem(row, column, QTableWidgetItem(str(data)))

    def listarBeneficiosFarmaceutica(self):
        resultado = self.db.busca_beneficios()
        
        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_cadastro_beneficio_farm.setItem(row, column, QTableWidgetItem(str(data)))

    def listarBeneficiosFarmaceuticaRelatorio(self):
        resultado = self.db.busca_beneficios_relatorio_farmaceutica()
        
        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_beneficios_farm.setItem(row, column, QTableWidgetItem(str(data)))
                
    def listarBeneficiosFarmaceuticaRelatorioFiltro(self):
        txt = re.sub('[\W_]+','',self.ui.input_buscar_dados_relatorio_beneficios_farm.text())
        resultado = self.db.busca_beneficios_relatorio_farmaceutica_filtro(txt)
        self.ui.input_TableWidget_relatorio_beneficios_farm.setRowCount(len(resultado))

        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_beneficios_farm.setItem(row, column, QTableWidgetItem(str(data)))
                
    def listarBeneficiosFarmaceuticaRelatorioFiltroData(self):
        texto_data_inicio = self.ui.input_inicio_periodo_relatorio_beneficio_farm.text()
        texto_data_final = self.ui.input_final_periodo_relatorio_beneficio_farm.text()
        texto_data_inicio_tratada =  "-".join(texto_data_inicio.split("/")[::-1])
        texto_data_final_tratada =  "-".join(texto_data_final.split("/")[::-1])
        resultado = self.db.busca_beneficios_relatorio_farmaceutica_filtro_data(texto_data_inicio_tratada,texto_data_final_tratada)
        print("data beneficio filtro ->", resultado)
        self.ui.input_TableWidget_relatorio_beneficios_farm.setRowCount(len(resultado))

        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_beneficios_farm.setItem(row, column, QTableWidgetItem(str(data)))

    
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
        
        
    def alterarAgendamentos_psi(self):
        try:
            dados = []
            for row in range(self.ui.input_TableWidget_agendamento_psi.rowCount()):
                row_data = []
                for column in range(self.ui.input_TableWidget_agendamento_psi.columnCount()):
                    item = self.ui.input_TableWidget_agendamento_psi.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append("")  
                dados.append(row_data)
            
            for emp in dados:
                resultado = self.db.alterar_agendamento_psi(emp)   

            self.filtrar_agenda_psi()

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
        telefone_contato = self.ui.input_telefone_contato_cuidador_as.text()  

        tupla_pessoa = (nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,telefone,telefone_contato)

        ################### cuidador ###################################

        parentesco = self.ui.input_parentesco_cuidador_as.text()
        observacao = self.ui.input_informacoes_gerais_as.toPlainText()
        tupla_cuidador = (parentesco,observacao)

        ################## usuário ####################################
        usuario_nome_id = self.ui.input_usuario_cuidador_as.currentText()
        usuario_nome_id = usuario_nome_id.split("-")
        usuario_id = int(usuario_nome_id[0])

        ################## insert #######################################
        if not validarCamposCuidadorCadastro(cpf,rg,telefone,cep,numero):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("ERRO")
            msg.setText("Erro ao tentar cadastrar Cuidador!")
            msg.exec()
        else:
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
        text = self.ui.input_salario_colaborador_as.text()
        salario_convertido = locale.currency(text, grouping=True)
        self.ui.input_salario_colaborador_as.setText(salario_convertido)
        print(salario_convertido)
        # self.ui.input_salario_colaborador_as.setInputMask("R$999.999.999,99")

        try:
            salario_formatado = '{:,.2f}'.format(float(text))
        except ValueError:
            salario_formatado = ''

        self.ui.input_salario_colaborador_as.setText(salario_formatado)
    

    def alterar_usuario_area_sigilosa(self):
        campo = []
        update_dados = []
        for row in range(self.ui.input_TableWidget_observacoes_sigilosas_as.rowCount()):
            for column in range(self.ui.input_TableWidget_observacoes_sigilosas_as.columnCount()):
                campo.append(self.ui.input_TableWidget_observacoes_sigilosas_as.item(row, column).text())
            update_dados.append(campo)
            campo = []

        for emp in update_dados:
           res = self.db.alterarAreaSigilosa(tuple(emp))

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Alterar Area Sigilosa")
        msg.setText("Usuario Alterado com sucesso!")
        msg.exec()
        self.filtrar_usuario_area_sigilosa()

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
        self.nome_colab = nome
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
        if not validarCamposColaboradorCadastro(cpf,rg,telefone,cep,numero):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar Colaborador!")
            msg.exec()
        else:
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

        tupla_curso = (nome_curso, tipo_curso, data_inicio, data_termino, periodo,responsavel, horario_inicial, horario_final, vagas,  segunda, terca, quarta, quinta, sexta, sabado,descricao)

        if not validarCamposCursoCadastro(tipo_curso, responsavel, horario_inicial, horario_final, periodo, vagas):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Erro Cadastro Curso")
            msg.setText("Erro cadastro Curso!")
            msg.exec()

        else:
            result=self.db.cadastro_curso(tupla_curso)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Curso")
            msg.setText("Curso cadastrado com sucesso!")
            msg.exec()
            self.limparCadastroCursos()
        
    
    def cadastroAgendamento(self):
        id_matricula = self.buscarPessoa()
        print(type(id_matricula))
        cpf_tmp = self.ui.input_cpf_agendamento_as.text()
        cpf = re.sub(r'[^\w\s]','',cpf_tmp)
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
        flag = "NAO"
        if not validarCamposAgendamentoCadastro(profissional):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Erro Cadastro")
            msg.setText("Erro ao cadastrar Agendamento!")
            msg.exec()
        else:

            tupla_agendamento = (id_matricula, cpf, nome, telefone, clinica, profissional, data_agend, hora, anotacao, flag)
            print("TUPLA AGENDAMENTO -> ",tupla_agendamento)
            result = self.db.cadastro_agendamento(tupla_agendamento)

                
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Agendamento")
            msg.setText("Agendamento Cadastrado com sucesso!")
            msg.exec()
            # self.msg(result[0],result[1])   
            self.limparCamposAgenda() 
            self.listarAgendamentos()

    def cadastroAgendamento_psi(self):
        id_matricula = self.buscarPessoa_psi()
        cpf = self.ui.input_cpf_agendamento_psi.text()
        nome = self.ui.input_nome_agendamento_psi.text()
        telefone = self.ui.input_telefone_agendamento_psi.text()
        clinica = self.ui.input_clinica_agendamento_psi.text()

        profissional = ''
        if self.ui.input_profissional_as_agendamento_psi.isChecked():
            profissional = 'Assistente Social'
        elif self.ui.input_profissional_fisio_agendamento_psi.isChecked():
            profissional = 'Fisioterapeuta'
        elif self.ui.input_profissional_nutri_agendamento_psi.isChecked():
            profissional = 'Nutricionista'
        if self.ui.input_profissional_psi_agendamento_psi.isChecked():
            profissional = 'Psicóloga'
        data = self.ui.input_data_agendamento_psi.text()
        data_agend = "-".join(data.split("/")[::-1])
        hora = self.ui.input_hora_agendamento_psi.text()
        anotacao = self.ui.input_anotacao_agendamento_psi.toPlainText()
        flag = "NAO"

        tupla_agendamento_psi = (id_matricula, cpf, nome, telefone, clinica, profissional, data_agend, hora, anotacao, flag)
        if not validarCamposAgendamentoPsicCadastro(profissional):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Erro Cadastro")
            msg.setText("Erro Cadastro!")
            msg.exec()
            
        else:
            
            result = self.db.cadastro_agendamento_psi(tupla_agendamento_psi)
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Agendamento")
            msg.setText("Agendamento Cadastrado com sucesso!")
            msg.exec()
        
            # self.msg(result[0],result[1])   
            self.tabela_consulta_psic_tabela()
            self.limparCamposAgendametoPsic() 
            self.listarAgendamentos_psi()

    def cadastroAgendamento_fisio(self):
        id_matricula = self.ui.input_id_matricula_agendamento_fisio.text()
        cpf = self.ui.input_cpf_agendamento_fisio.text()
        nome = self.ui.input_nome_agendamento_fisio.text()
        telefone = self.ui.input_telefone_agendamento_fisio.text()
        clinica = self.ui.input_clinica_agendamento_fisio.text()

        profissional = ''
        if self.ui.input_profissional_as_agendamento_fisio.isChecked():
            profissional = 'Assistente Social'
        elif self.ui.input_profissional_fisio_agendamento_fisio.isChecked():
            profissional = 'Fisioterapeuta'
        elif self.ui.input_profissional_nutri_agendamento_fisio.isChecked():
            profissional = 'Nutricionista'
        if self.ui.input_profissional_psi_agendamento_fisio.isChecked():
            profissional = 'Psicóloga'
        data = self.ui.input_data_agendamento_fisio.text()
        data_agend = "-".join(data.split("/")[::-1])
        hora = self.ui.input_hora_agendamento_fisio.text()
        anotacao = self.ui.input_anotacao_agendamento_fisio.toPlainText()
        flag = "NAO"

        tupla_agendamento_fisio = (id_matricula, cpf, nome, telefone, clinica, profissional, data_agend, hora, anotacao,flag)
        if not validarCamposAgendamentoFisioCadastro(profissional):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Erro Cadastro")
            msg.setText("Erro Cadastro!")
            msg.exec()

        else:

            result = self.db.cadastro_agendamento_fisio(tupla_agendamento_fisio)
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Agendamento")
            msg.setText("Agendamento Cadastrado com sucesso!")
            msg.exec()
            self.tabela_agendamento_fisio()
            self.limparCamposAgendamentoFisio()

    def cadastroAgendamentoNutri(self):
        id_matricula = self.ui.input_id_matricula_nutri_agendamento.text()
        cpf = self.ui.input_cpf_agendamento_nutri.text()
        nome = self.ui.input_nome_agendamento_nutri.text()
        telefone = self.ui.input_telefone_agendamento_nutri.text()
        clinica = self.ui.input_clinica_agendamento_nutri.text()


        profissional = ''
        if self.ui.input_profissional_as_agendamento_nutri.isChecked():
            profissional = 'Assistente Social'
        elif self.ui.input_profissional_fisio_agendamento_nutri.isChecked():
            profissional = 'Fisioterapeuta'
        elif self.ui.input_profissional_nutri_agendamento_nutri.isChecked():
            profissional = 'Nutricionista'
        if self.ui.input_profissional_psi_agendamento_nutri.isChecked():
            profissional = 'Psicóloga'
        data = self.ui.input_data_agendamento_nutri.text()
        data_agend = "-".join(data.split("/")[::-1])
        hora = self.ui.input_hora_agendamento_nutri.text()
        anotacao = self.ui.input_anotacao_agendamento_nutri.toPlainText()
        flag = "NAO"

        tupla_agendamento_nutri = (id_matricula, cpf, nome, telefone, clinica, profissional, data_agend, hora, anotacao, flag)

        if not validarCamposAgendamentoNutriCadastro(profissional):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Erro Cadastro")
            msg.setText("Erro ao agendar!")
            msg.exec()
        else:
            result = self.db.cadastro_agendamento_nutri(tupla_agendamento_nutri)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Agendamento")
            msg.setText("Agendamento Cadastrado com sucesso!")
            msg.exec()
            self.tabela_agenda_nutri()
            self.limparCamposAgendaNutri()

    def cadastroIMC(self):
        peso = self.ui.input_peso_consulta_nutri.text()
        altura = self.ui.input_altura_consulta_nutri.text()
        imc = self.ui.input_imc_consulta_nutri.text()
        id_matricula = self.ui.input_id_matricula_nutri_consulta.text()
        tupla_IMC = (peso, altura, imc, id_matricula)
        result = self.db.cadastroIMC(tupla_IMC)
        print(result)


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


        if not validarCamposFornecedoresCadastro(cnpj, celular, email, inscricao_estadual, inscricao_municipal, cep, numero):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Erro Cadastro")
            msg.setText("Erro cadastro fornecedor")
            msg.exec()

        else:

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
    
    def filtrar_agenda_psi(self):
        txt = re.sub('[\W_]+','',self.ui.input_filtro_agendamento_psi.text())
        res = self.db.filter_agenda(txt)
        self.ui.input_TableWidget_agendamento_psi.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_agendamento_psi.setItem(row, column, QTableWidgetItem(str(data)))

    def area_sigilosa_salvar_usuario(self):

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
        self.filtrar_usuario_area_sigilosa()
        self.limparCamposAreaSigilosa()


    def limparCamposCadastroUsuario (self):
        self.ultimosIds()
        self.ui.input_nome_usuario_as.setText("") #
        self.ui.input_nascimento_usuario_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_situacao_ativo_usuario_as.setCheckable(False)
        self.ui.input_situacao_ativo_usuario_as.setCheckable(True)
        self.ui.input_situacao_inativo_usuario_as.setCheckable(False)
        self.ui.input_situacao_inativo_usuario_as.setCheckable(True)
        self.ui.input_cpf_usuario_as.setText("")
        self.ui.input_rg_usuario_as.setText("")
        self.ui.input_data_emissao_usuario_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_orgao_expedidor_usuario_as.setText("")
        self.ui.input_nis_usuario_as.setText("")
        self.ui.input_cns_usuario_as.setText("")
        self.ui.input_sexo_usuario_as.setCurrentIndex(int(0))
        self.ui.input_telefone_usuario_as.setText("")
        self.ui.input_telefone_contato_usuario_as.setText("")
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
        self.ui.input_pessoa_cdeficiencia_nao_usuario_as.setCheckable(False)  
        self.ui.input_pessoa_cdeficiencia_nao_usuario_as.setCheckable(True)        
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
        self.ui.input_data_inicio_usuario_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_periodo_usuario_as.setCurrentIndex(int(0))

        
    def limparCamposCadastroCuidador(self):
        self.ultimosIds()
        self.ui.input_nome_cuidador_as.setText("")
        self.ui.input_data_nascimento_cuidador_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_cpf_cuidador_as.setText("")
        self.ui.input_rg_cuidador_as.setText("")
        self.ui.input_data_emissao_cuidador_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_orgao_expedidor_cuidador_as.setText("")
        self.ui.input_sexo_cuidador_as.setCurrentIndex(int(0))
        self.ui.input_usuario_cuidador_as.setCurrentIndex(int(0))
        self.ui.input_parentesco_cuidador_as.setText("")
        self.ui.input_telefone_cuidador_as.setText("")
        self.ui.input_telefone_contato_cuidador_as.setText("") 
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
        self.ui.input_data_nascimento_colaborador_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_cpf_colaborador_as.setText("")
        self.ui.input_rg_colaborador_as.setText("")
        self.ui.input_situacao_ativo_colaborador_as.setCheckable(False)
        self.ui.input_situacao_ativo_colaborador_as.setCheckable(True)
        self.ui.input_situacao_inativo_colaborador_as.setCheckable(False)
        self.ui.input_situacao_inativo_colaborador_as.setCheckable(True)
        self.ui.input_orgao_expedidor_colaborador_as.setText("")
        self.ui.input_data_emissao_rg_colaborador_as.setDateTime(QDateTime.currentDateTime())
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
        self.ui.input_data_admissao_colaborador_as_5.setDateTime(QDateTime.currentDateTime())
        self.ui.input_escolaridade_colaborador_comboBox_as.setCurrentIndex(int(0))
        self.ui.input_cargo_colaborador_comboBox_as.setCurrentIndex(int(0))
        self.ui.input_periodo_colaborador_comboBox_as.setCurrentIndex(int(0))
        self.ui.input_usuario_colaborador_as_2.setText("")
        self.ui.input_senha_colaborador_as_2.setText("")
        self.ui.input_confirmar_senha_colaborador_as_2.setText("")


    def limparCamposCursosOficinas(self):
        self.ui.input_nome_cursos_as.setText("")
        self.ui.input_tipo_cursos_as.setCurrentIndex(int(0))
        self.ui.input_responsavel_cursos_as.setText("")
        self.ui.input_data_inicio_cursos_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_data_termino_cursos_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_periodo_cursos_as.setCurrentIndex(int(0))
        self.ui.input_vagas_cursos_as.setText("")
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

    
    def limparCamposCadastroParticipante(self):
        self.ui.input_cpf_pagina_participante_geral.setText("")
        self.ui.input_nome_pagina_participante_geral.setText("")
        self.ui.input_telefone_pagina_participante_geral.setText("")
        self.ui.input_email_pagina_participante_geral.setText("")
        self.ui.input_clinica_pagina_participante_geral.setText("")
        self.ui.comboBox_cursos_participante_geral.setCurrentIndex(int(0))
    

    def limparCamposAlterarDadosCadastrais(self):
        self.ui.comboBox_tipos_alterar_cadastros_as.setCurrentIndex(int(0))
        self.ui.lineEdit_alterar_buscar_cpf_cnpj_as.setText("")
    

    def limparCamposAtendimentoAssistenteSocial(self):
        self.ui.input_cpf_pagina_consulta_geral.setText("")
        self.ui.input_nome_pagina_consulta_geral.setText("")
        self.ui.input_contato_pagina_consulta_geral.setText("")
        self.ui.input_clinica_pagina_consulta_geral.setText("")
        self.ui.radioButton_atendimento_as.setCheckable(False)
        self.ui.radioButton_atendimento_as.setCheckable(True)
        self.ui.radioButton_Retorno_as.setCheckable(False)
        self.ui.radioButton_Retorno_as.setCheckable(True)
        self.ui.input_data_pagina_consulta_geral.setDateTime(QDateTime.currentDateTime())
        self.ui.input_hora_consulta_as.setText("")
        self.ui.input_evolucao_pagina_consulta_geral.setHtml("")

    def limparCamposConsultaNutri(self):
        self.ui.input_nome_pagina_consulta_geral_nutri.setText("")
        self.ui.input_contato_pagina_consulta_geral_nutri.setText("")
        self.ui.input_clinica_pagina_consulta_geral_nutri.setText("")
        self.ui.input_tipo_tratamento_consulta_nutri.setCurrentIndex(0)
        self.ui.input_patologia_base_consulta_nutri.setCurrentIndex(0)
        self.ui.input_peso_consulta_nutri.setText("")
        self.ui.input_altura_consulta_nutri.setText("")
        self.ui.input_imc_consulta_nutri.setText("")
        self.ui.radioButton_atendimento_as_nutri.setCheckable(False)
        self.ui.radioButton_atendimento_as_nutri.setCheckable(True)
        self.ui.radioButton_Retorno_as_nutri.setCheckable(False)
        self.ui.radioButton_Retorno_as_nutri.setCheckable(True)
        self.ui.input_data_pagina_consulta_geral_nutri.setDate(QDate(2023, 1, 1))
        self.ui.input_hora_consulta_as_nutri.setText("")
        self.ui.input_evolucao_pagina_consulta_geral_nutri.setHtml("")

    def limparCamposAgendaNutri(self):
        self.ui.input_cpf_agendamento_nutri.setText("")
        self.ui.input_nome_agendamento_nutri.setText("")
        self.ui.input_telefone_agendamento_nutri.setText("")
        self.ui.input_clinica_agendamento_nutri.setText("")
        self.ui.input_clinica_pagina_consulta_geral_psi.setText("")
        self.ui.input_profissional_as_agendamento_nutri.setCheckable(False)
        self.ui.input_profissional_as_agendamento_nutri.setCheckable(True)
        self.ui.input_profissional_psi_agendamento_nutri.setCheckable(False)
        self.ui.input_profissional_psi_agendamento_nutri.setCheckable(True)
        self.ui.input_profissional_nutri_agendamento_nutri.setCheckable(False)
        self.ui.input_profissional_nutri_agendamento_nutri.setCheckable(True)
        self.ui.input_profissional_fisio_agendamento_nutri.setCheckable(False)
        self.ui.input_profissional_fisio_agendamento_nutri.setCheckable(True)
        self.ui.input_data_agendamento_nutri.setDate(QDate(2023, 1, 1))
        self.ui.input_hora_agendamento_nutri.setTime(QTime(00,00))
        self.ui.input_anotacao_agendamento_nutri.setHtml("")

    def limparCamposConsulta_psi(self):
        self.ui.input_cpf_agendamento_psi.setText("")
        self.ui.input_nome_pagina_consulta_geral_psi.setText("")
        self.ui.input_contato_pagina_consulta_geral_psi.setText("")
        self.ui.input_clinica_pagina_consulta_geral_psi.setText("")
        self.ui.radioButton_atendimento_as_psi.setCheckable(False)
        self.ui.radioButton_atendimento_as_psi.setCheckable(True)
        self.ui.radioButton_Retorno_as_psi.setCheckable(False)
        self.ui.radioButton_Retorno_as_psi.setCheckable(True)
        self.ui.input_data_pagina_consulta_geral_psi.setDate(QDate(2000, 1, 1))
        self.ui.input_hora_consulta_as_psi.setText("")
        self.ui.input_evolucao_pagina_consulta_geral_psi.setHtml("")

    def limparCamposAgendaAssistenteSocial(self):
        self.ui.input_cpf_agendamento_as.setText("")
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
        self.ui.input_data_agendamento_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_hora_agendamento_as.setTime(QTime(00,00))
        self.ui.input_anotacao_agendamento_as.setHtml("")


    def limparCamposRelatorioCuidadores(self):
        self.ui.input_inicio_periodo_relatorio_cuidadores_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_final_periodo_relatorio_cuidadores_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_idade_inicial_relatorio_cuidadores_as.setText("")
        self.ui.input_idade_final_relatorio_cuidadores_as.setText("")
        self.ui.input_buscar_dados_relatorio_cuidadores_as.setText("")

    
    def limparCamposRelatorioPessoas(self):
        self.ui.input_inicio_periodo_relatorio_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_final_periodo_relatorio_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_idade_inicial_relatorio_as.setText("")
        self.ui.input_idade_final_relatorio_as.setText("")
        self.ui.input_buscar_dados_relatorio_as.setText("")
    

    def limparCamposRelatorioCursosParticipantes(self):
        self.ui.input_inicio_periodo_relatorio_aluno_curso.setDateTime(QDateTime.currentDateTime())
        self.ui.input_final_periodo_relatorio_aluno_curso.setDateTime(QDateTime.currentDateTime())
        self.ui.input_buscar_dados_relatorio_aluno_curso.setText("")
    

    def limparCamposRelatorioBeneficios(self):
        self.ui.input_inicio_periodo_relatorio_beneficio_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_final_periodo_relatorio_beneficio_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_buscar_dados_relatorio_beneficios_as.setText("")

    
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

    
    def limparCamposClinicasCadastradas(self):
        self.ui.input_inicio_periodo_relatorio_clinicas_cadastradas_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_final_periodo_relatorio_relatorio_clinicas_cadastradas_as.setDateTime(QDateTime.currentDateTime())
        self.ui.input_buscar_dados_relatorio_relatorio_clinicas_cadastradas_as.setText("")


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
    

    def limparCamposFornecedoresCadastrados(self):
        self.ui.input_inicio_periodo_relatorio_fornecedores_cadastrados.setDateTime(QDateTime.currentDateTime())
        self.ui.input_final_periodo_relatorio_relatorio_fornecedores_cadastrados.setDateTime(QDateTime.currentDateTime())
        self.ui.input_buscar_dados_relatorio_relatorio_fornecedor_cadastrado.setText("")
    

    def limparCamposCadastroBeneficios(self):
        self.ui.input_tipo_cadastro_beneficio.setCurrentIndex(int(0))
        self.ui.input_codigo_cadastro_beneficio.setText("")
        self.ui.input_lote_cadastro_beneficio.setText("")
        self.ui.input_comboBox_udm_cadastro_benefecio.setCurrentIndex(int(0))
        self.ui.input_descricao_cadastro_beneficio.setText("")
        self.ui.input_dateEdit_cadastro_beneficio.setDateTime(QDateTime.currentDateTime())       
        self.ui.input_spinBox_cadastro_beneficio.setValue(0)

    def limparCamposCadastroBeneficiosFarmaceutica(self):
        self.ui.input_tipo_cadastro_beneficio_farm.setCurrentIndex(int(0))
        self.ui.input_codigo_cadastro_beneficio_2_farm.setText("")
        self.ui.input_lote_cadastro_beneficio_2.setText("")
        self.ui.input_comboBox_udm_cadastro_benefecio_farm.setCurrentIndex(int(0))
        self.ui.input_descricao_cadastro_beneficio_farm.setText("")
        self.ui.input_dateEdit_cadastro_beneficio_farm.setDate(QDate(2000, 1, 1))          
        self.ui.input_spinBox_cadastro_beneficio_farm.setValue(0)
    
    def limparCamposCadastroRetiradaBeneficiosFarmaceutica(self):
        self.ui.input_cpf_cadastro_retirada_beneficio_farm.setText("")
        self.ui.input_nome_cadastro_retirada_beneficio_2.setText("")
        self.ui.input_idade_cadastro_retirada_beneficio_farm.setText("")
        self.ui.input_data_cadastro_retirada_beneficio_2_farm.setDate(QDate(2020, 1, 1))
        self.ui.input_telefone_cadastro_retirada_beneficio_farm.setText("")
        self.ui.input_cns_cadastro_retirada_beneficio_farm.setText("")
        self.ui.input_clinica_cadastro_retirada_beneficio_farm.setText("")
        
        self.ui.input_codigo_beneficio_cadastro_retirada_beneficio_farm.setText("")
        self.ui.input_descricao_cadastro_retirada_beneficio_farm.setText("")       
        self.ui.input_spinBox_cadastro_retirada_beneficio_farm.setValue(0)

    def limparCamposCadastroRetiradaBeneficios(self):
        self.ui.input_cpf_cadastro_retirada_beneficio.setText("")
        self.ui.input_nome_cadastro_retirada_beneficio.setText("")
        self.ui.input_idade_cadastro_retirada_beneficio.setText("")
        self.ui.input_data_cadastro_retirada_beneficio.setDateTime(QDateTime.currentDateTime())
        self.ui.input_telefone_cadastro_retirada_beneficio.setText("")
        self.ui.input_cns_cadastro_retirada_beneficio.setText("")
        self.ui.input_clinica_cadastro_retirada_beneficio.setText("")
        
        self.ui.input_codigo_beneficio_cadastro_retirada_beneficio.setText("")
        self.ui.input_descricao_cadastro_retirada_beneficio.setText("")       
        self.ui.input_spinBox_cadastro_retirada_beneficio.setValue(0)

    def limparCadastroCursos(self):
        self.ui.input_nome_cursos_as.setText("")
        self.ui.input_tipo_cursos_as.setCurrentIndex(0)
        self.ui.input_responsavel_cursos_as.setText("")
        self.ui.input_data_inicio_cursos_as.setDate(QDate(2020, 1, 1))
        self.ui.input_data_termino_cursos_as.setDate(QDate(2020, 1, 1))
        self.ui.input_horario_inicio_cursos_as.setTime(QTime(00,00))
        self.ui.input_horario_termino_cursos_as.setTime(QTime(00,00))
        self.ui.input_periodo_cursos_as.setCurrentIndex(0)
        self.ui.input_vagas_cursos_as.setText("")
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

    def limparCamposAreaSigilosa(self):
        self.ui.input_obito_paciente_sim_as.setCheckable(False)
        self.ui.input_obito_paciente_sim_as.setCheckable(True)
        self.ui.input_obito_paciente_nao_as.setCheckable(False)
        self.ui.input_obito_paciente_nao_as.setCheckable(True)
        self.ui.input_observacoes_obs_sigilosas_as.setHtml("")


    def limparCamposConsultaNutri(self):
        self.ui.input_nome_pagina_consulta_geral_nutri.setText("")
        self.ui.input_contato_pagina_consulta_geral_nutri.setText("")
        self.ui.input_clinica_pagina_consulta_geral_nutri.setText("")
        self.ui.input_tipo_tratamento_consulta_nutri.setCurrentIndex(0)
        self.ui.input_patologia_base_consulta_nutri.setCurrentIndex(0)
        self.ui.input_peso_consulta_nutri.setText("")
        self.ui.input_altura_consulta_nutri.setText("")
        self.ui.input_imc_consulta_nutri.setText("")
        self.ui.radioButton_atendimento_as_nutri.setCheckable(False)
        self.ui.radioButton_atendimento_as_nutri.setCheckable(True)
        self.ui.radioButton_Retorno_as_nutri.setCheckable(False)
        self.ui.radioButton_Retorno_as_nutri.setCheckable(True)
        self.ui.input_data_pagina_consulta_geral_nutri.setDateTime(QDateTime.currentDateTime())
        self.ui.input_hora_consulta_as_nutri.setText("")
        self.ui.input_evolucao_pagina_consulta_geral_nutri.setHtml("")

    def limparCamposAgendaNutri(self):
        self.ui.input_cpf_agendamento_nutri.setText("")
        self.ui.input_nome_agendamento_nutri.setText("")
        self.ui.input_telefone_agendamento_nutri.setText("")
        self.ui.input_clinica_agendamento_nutri.setText("")
        self.ui.input_clinica_pagina_consulta_geral_psi.setText("")
        self.ui.input_profissional_as_agendamento_nutri.setCheckable(False)
        self.ui.input_profissional_as_agendamento_nutri.setCheckable(True)
        self.ui.input_profissional_psi_agendamento_nutri.setCheckable(False)
        self.ui.input_profissional_psi_agendamento_nutri.setCheckable(True)
        self.ui.input_profissional_nutri_agendamento_nutri.setCheckable(False)
        self.ui.input_profissional_nutri_agendamento_nutri.setCheckable(True)
        self.ui.input_profissional_fisio_agendamento_nutri.setCheckable(False)
        self.ui.input_profissional_fisio_agendamento_nutri.setCheckable(True)
        self.ui.input_data_agendamento_nutri.setDateTime(QDateTime.currentDateTime())
        self.ui.input_hora_agendamento_nutri.setTime(QTime(00,00))
        self.ui.input_anotacao_agendamento_nutri.setHtml("")

    def limparCamposConsulta_psi(self):
        self.ui.input_cpf_agendamento_psi.setText("")
        self.ui.input_nome_pagina_consulta_geral_psi.setText("")
        self.ui.input_contato_pagina_consulta_geral_psi.setText("")
        self.ui.input_clinica_pagina_consulta_geral_psi.setText("")
        self.ui.radioButton_atendimento_as_psi.setCheckable(False)
        self.ui.radioButton_atendimento_as_psi.setCheckable(True)
        self.ui.radioButton_Retorno_as_psi.setCheckable(False)
        self.ui.radioButton_Retorno_as_psi.setCheckable(True)
        self.ui.input_data_pagina_consulta_geral_psi.setDateTime(QDateTime.currentDateTime())
        self.ui.input_hora_consulta_as_psi.setText("")
        self.ui.input_evolucao_pagina_consulta_geral_psi.setHtml("")


    def limparCamposAgendamentoFisio(self):
        self.ui.input_nome_agendamento_fisio.setText("")
        self.ui.input_telefone_agendamento_fisio.setText("")
        self.ui.input_clinica_agendamento_fisio.setText("")
        self.ui.input_profissional_as_agendamento_fisio.setCheckable(False)
        self.ui.input_profissional_as_agendamento_fisio.setCheckable(True)
        self.ui.input_profissional_psi_agendamento_fisio.setCheckable(False)
        self.ui.input_profissional_psi_agendamento_fisio.setCheckable(True)
        self.ui.input_profissional_nutri_agendamento_fisio.setCheckable(False)
        self.ui.input_profissional_nutri_agendamento_fisio.setCheckable(True)
        self.ui.input_profissional_fisio_agendamento_fisio.setCheckable(False)
        self.ui.input_profissional_fisio_agendamento_fisio.setCheckable(True)
        self.ui.input_data_agendamento_fisio.setDateTime(QDateTime.currentDateTime())
        self.ui.input_hora_agendamento_fisio.setTime(QTime(00,00))
        self.ui.input_anotacao_agendamento_fisio.setHtml("")

    def limparCamposConsultaFisio(self):
        self.ui.input_nome_pagina_consulta_geral_fisio.setText("")
        self.ui.input_contato_pagina_consulta_geral_fisio.setText("")
        self.ui.input_clinica_pagina_consulta_geral_fisio.setText("")
        self.ui.radioButton_atendimento_as_fisio.setCheckable(False)
        self.ui.radioButton_atendimento_as_fisio.setCheckable(True)
        self.ui.radioButton_Retorno_as_fisio.setCheckable(False)
        self.ui.radioButton_Retorno_as_fisio.setCheckable(True)
        self.ui.input_data_pagina_consulta_geral_fisio.setDateTime(QDateTime.currentDateTime())
        self.ui.input_hora_consulta_as_fisio.setText("")
        self.ui.input_relatorio_pagina_evolucao_geral_fisio.setHtml("")
        
    def limparCamposAgendametoPsic(self):
        self.ui.input_nome_agendamento_psi.setText("")
        self.ui.input_telefone_agendamento_psi.setText("")
        self.ui.input_clinica_agendamento_psi.setText("")
        self.ui.input_profissional_as_agendamento_psi.setCheckable(False)
        self.ui.input_profissional_as_agendamento_psi.setCheckable(True)
        self.ui.input_profissional_psi_agendamento_psi.setCheckable(False)
        self.ui.input_profissional_psi_agendamento_psi.setCheckable(True)
        self.ui.input_profissional_nutri_agendamento_psi.setCheckable(False)
        self.ui.input_profissional_nutri_agendamento_psi.setCheckable(True)
        self.ui.input_profissional_fisio_agendamento_psi.setCheckable(False)
        self.ui.input_profissional_fisio_agendamento_psi.setCheckable(True)
        self.ui.input_data_agendamento_psi.setDateTime(QDateTime.currentDateTime())
        self.ui.input_hora_agendamento_psi.setTime(QTime(00,00))
        self.ui.input_anotacao_agendamento_psi.setHtml("")
        
        
        
        
        
        
        
        
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
        print(dados)
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

    def buscar_dados_consulta_psi(self):
        cpf_temp = self.ui.input_cpf_pagina_consulta_geral_psi.text()
        cpf = ''
        for i in cpf_temp:
            if i == '.' or i == '-':
                pass
            else:
                cpf += i
        dados = self.db.buscar_consulta_usuario_psi(cpf)
        print("DADOS CONSULTA PSIC ->",dados)
        if dados[6] == "SIM":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Usuario Agendamento")
            msg.setText("Usuario nao possui agendamento!")
            msg.exec()
        elif dados[6] == "NAO":
            self.ui.input_nome_pagina_consulta_geral_psi.setText(dados[0])
            self.ui.input_contato_pagina_consulta_geral_psi.setText(dados[1])
            self.ui.input_clinica_pagina_consulta_geral_psi.setText(dados[2])
            self.ui.input_data_pagina_consulta_geral_psi.setDate(QDate(dados[3]))
            self.ui.input_hora_consulta_as_psi.setText(str(dados[4]))
            self.ui.input_id_matricula_consulta_psi.setText(str(dados[5]))
            self.ui.input_id_matricula_consulta_psi.hide()
            self.puxar_consulta_psi()
            self.tabela_consulta_psic_tabela()


    def buscar_dados_consulta(self):
        cpf_temp = self.ui.input_cpf_pagina_consulta_geral.text()
        cpf = ''
        for i in cpf_temp:
            if i == '.' or i == '-':
                pass
            else:
                cpf += i
        dados = self.db.buscar_consulta(cpf)
        print(dados)
        if dados[6] == "SIM":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Usuario Agendamento")
            msg.setText("Usuario não possui agendamento!!")
            msg.exec()
            
        elif dados[6] == "NAO":
            self.ui.input_id_matricula_consulta_as.setText(str(dados[0]))
            self.ui.input_id_matricula_consulta_as.hide()
            self.ui.input_nome_pagina_consulta_geral.setText(dados[1])
            self.ui.input_contato_pagina_consulta_geral.setText(dados[2])
            self.ui.input_clinica_pagina_consulta_geral.setText(dados[3])
            self.ui.input_data_pagina_consulta_geral.setDate(QDate(dados[4]))
            hora  = str(dados[5]).split(":")
            self.ui.input_hora_consulta_as.setText(str(dados[5]))
            self.puxar_consulta();

    def cadastrar_consulta(self):
        if self.ui.radioButton_atendimento_as.isChecked():
            situacao = "Consulta"
        if self.ui.radioButton_Retorno_as.isChecked():
            situacao = "Retorno"

        data = self.ui.input_data_pagina_consulta_geral.text()
        data_consulta = "-".join(data.split("/")[::-1])

        hora_bruta = self.ui.input_hora_consulta_as.text()

        relatorio = self.ui.input_evolucao_pagina_consulta_geral.toPlainText()

        id_matricula = self.ui.input_id_matricula_consulta_as.text()
        
        

        tupla_consulta = (situacao,data_consulta,hora_bruta,relatorio,id_matricula, self.id_colab_tratado_ass)
        print(tupla_consulta)

        result = []
        result = self.db.cadastro_consulta(tupla_consulta)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro Consulta")
        msg.setText("Consulta Cadastrada com sucesso!")
        msg.exec()
        
        self.limparCamposAtendimentoAssistenteSocial()
        self.puxar_consulta()
        
    def cadastrar_consulta_nutri(self):

        if self.ui.radioButton_atendimento_as_nutri.isChecked():
            situacao = "Consulta"
        if self.ui.radioButton_Retorno_as_nutri.isChecked():
            situacao = "Retorno"

        data = self.ui.input_data_pagina_consulta_geral_nutri.text()
        data_consulta = "-".join(data.split("/")[::-1])

        hora = self.ui.input_hora_consulta_as_nutri.text()

        relatorio = self.ui.input_evolucao_pagina_consulta_geral_nutri.toPlainText()

        id_matricula = int(self.ui.input_id_matricula_nutri_consulta.text())
        peso = self.ui.input_peso_consulta_nutri.text()
        altura = self.ui.input_altura_consulta_nutri.text()
        imc = self.ui.input_imc_consulta_nutri.text()

        tupla_consulta = (situacao,data_consulta,hora,relatorio,id_matricula, self.id_colab_tratado_nutri)
        if not validarCamposConsultaNutriCadastro(situacao, data, hora):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Erro Cadastro")
            msg.setText("Erro Cadastro!")
            msg.exec()
            return
        
        elif not validarCamposConsultaNutriImcCadastro(peso, altura, imc):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Erro IMC")
            msg.setText("Erro IMC!")
            msg.exec()
            return

        else:
            result = []
            result = self.db.cadastro_consulta_nutri(tupla_consulta)
            self.cadastroIMC()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Consulta")
            msg.setText("Consulta Cadastrada com sucesso!")
            msg.exec()
            
            self.tabela_consulta_nutri_tabela()
            self.limparCamposConsultaNutri()

    def cadastrar_consulta_psi(self):
        if self.ui.radioButton_atendimento_as_psi.isChecked():
            situacao = "Consulta"
        elif self.ui.radioButton_Retorno_as_psi.isChecked():
            situacao = "Retorno"
        else:
            situacao = ""

        data = self.ui.input_data_pagina_consulta_geral_psi.text()
        data_consulta = "-".join(data.split("/")[::-1])

        hora = self.ui.input_hora_consulta_as_psi.text()

        relatorio = self.ui.input_evolucao_pagina_consulta_geral_psi.toPlainText()

        id_matricula = int(self.ui.input_id_matricula_consulta_psi.text())
        print(type(id_matricula))

        tupla_consulta_psi = (situacao,data_consulta,hora,relatorio,id_matricula, self.id_colab_tratado_psic)
        if not validarCamposConsultaPsicCadastro(situacao, data, hora):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Erro Cadastro")
            msg.setText("Erro Cadastro!")
            msg.exec()

        else:
            
            result = []
            result = self.db.cadastro_consulta_psi(tupla_consulta_psi)
    

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Consulta")
            msg.setText("Consulta Cadastrada com sucesso!")
            msg.exec()
            self.listarAgendamentos_psi()
            self.tabela_consulta_psic_tabela()
            self.limparCamposConsulta_psi()

    def cadastrar_consulta_fisio(self):
        if self.ui.radioButton_atendimento_as_fisio.isChecked():
            situacao = "Consulta"
        elif self.ui.radioButton_Retorno_as_fisio.isChecked():
            situacao = "Retorno"
        else:
            situacao = ""

        data = self.ui.input_data_pagina_consulta_geral_fisio.text()
        data_consulta = "-".join(data.split("/")[::-1])

        hora = self.ui.input_hora_consulta_as_fisio.text()

        relatorio = self.ui.input_relatorio_pagina_evolucao_geral_fisio.toPlainText()

        id_matricula = int(self.ui.input_id_matricula_consulta_fisio.text())
        print(type(id_matricula))

        tupla_consulta_psi = (situacao,data_consulta,hora,relatorio,id_matricula, self.id_colab_tratado_fisio)
        print(tupla_consulta_psi)
        if not validarCamposConsultaFisioCadastro(situacao, data, hora):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Erro Cadastro")
            msg.setText("Erro Cadastro")
            msg.exec()  

        else:

            result = []
            result = self.db.cadastro_consulta_fisio(tupla_consulta_psi)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Consulta")
            msg.setText("Consulta Cadastrada com sucesso!")
            msg.exec()
            self.puxar_consulta_fisio()
            self.limparCamposConsultaFisio()

    def puxar_consulta_psi(self):
        cpf_temp = self.ui.input_cpf_pagina_consulta_geral_psi.text()
        cpf = ''
        for i in cpf_temp:
            if i == '.' or i == '-':
                pass
            else:
                cpf += i
        result = self.db.buscar_consulta_psic(cpf, self.id_colab_tratado_psic)
        self.ui.input_TableWidget_pagina_consulta_geral_psi.clearContents()
        self.ui.input_TableWidget_pagina_consulta_geral_psi.setRowCount(len(result))   

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_pagina_consulta_geral_psi.setItem(row, column,QTableWidgetItem(str(data)))

    def alterar_usuario_consulta_psi(self,campo):
        campo = []
        update_dados = []

        for row in range(self.ui.input_TableWidget_pagina_consulta_geral_psi.rowCount()):
            for column in range(self.ui.input_TableWidget_pagina_consulta_geral_psi.columnCount()):
                campo.append(self.ui.input_TableWidget_pagina_consulta_geral_psi.item(row, column).text())
            update_dados.append(campo)
            campo = []
        for emp in update_dados:
           res = self.db.alterar_usuario_consulta_psi(tuple(emp))

        self.puxar_consulta_psi()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Alterar Consulta")
        msg.setText("Consulta Alterada com sucesso!")
        msg.exec()


    def excluir_usuario_consulta_psi (self):
        id_consulta = self.ui.input_TableWidget_pagina_consulta_geral_psi.selectionModel().currentIndex().siblingAtColumn(0).data()
        self.db.deletar_consulta_relatorio_psi(id_consulta)

        self.puxar_consulta_psi()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excluir Consulta")
        msg.setText("Consulta Excluida com sucesso!")
        msg.exec()
        
    def alterar_consulta_nutri(self, campo):
        campo = []
        update_dados = []

        for row in range(self.ui.input_TableWidget_pagina_consulta_geral_nutri.rowCount()):
            for column in range(self.ui.input_TableWidget_pagina_consulta_geral_nutri.columnCount()):
                campo.append(self.ui.input_TableWidget_pagina_consulta_geral_nutri.item(row, column).text())
            update_dados.append(campo)
            campo = []
        for emp in update_dados:
            self.db.alterar_consulta_nutri(tuple(emp))
            self.tabela_consulta_nutri_tabela()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Alterar Consulta")
        msg.setText("Consulta Alterada com sucesso!")
        msg.exec()
        
    def excluir_usuario_consulta_nutri (self):
        id_consulta = self.ui.input_TableWidget_pagina_consulta_geral_nutri.selectionModel().currentIndex().siblingAtColumn(0).data()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Alterar Consulta")
        msg.setText("Deseja alterar a consulta?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resposta = msg.exec()
        
        if resposta == QMessageBox.Yes:
            self.db.deletar_consulta_relatorio_nutri(id_consulta)
            self.tabela_consulta_nutri_tabela()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Alteração não concluida")
            msg.setText("Alteração não feita!!!")
            msg.exec()
        self.tabela_consulta_nutri_tabela()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excluir Consulta")
        msg.setText("Consulta Excluida com sucesso!")
        msg.exec()


    def puxar_consulta(self):
        cpf_tmp = self.ui.input_cpf_pagina_consulta_geral.text()
        cpf = re.sub(r'[^\w\s]','',cpf_tmp)
        print("CPF CONSULTA ASSIS ->", cpf)
        result = self.db.buscar_info_consulta(cpf, self.id_colab_tratado_ass)
        print(result)
        self.ui.input_TableWidget_pagina_consulta_geral.clearContents()
        self.ui.input_TableWidget_pagina_consulta_geral.setRowCount(len(result))   

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_pagina_consulta_geral.setItem(row, column,QTableWidgetItem(str(data)))

    def puxar_participantes_curso(self):
        result = self.db.buscar_participantes_curso()
        self.ui.input_TableWidget_relatorio_aluno_curso.clearContents()
        self.ui.input_TableWidget_relatorio_aluno_curso.setRowCount(len(result))   

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_aluno_curso.setItem(row, column,QTableWidgetItem(str(data)))
    
    def puxar_relatorio_psi(self):
        result = self.db.buscar_relatorio_psi()
        self.ui.input_TableWidget_relatorio_psi.clearContents()
        self.ui.input_TableWidget_relatorio_psi.setRowCount(len(result))   

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_psi.setItem(row, column,QTableWidgetItem(str(data)))

    def gerar_excel_paricipante_curso(self):
        dados = []
        all_dados =  []

        for row in range(self.ui.input_TableWidget_relatorio_aluno_curso.rowCount()):
            for column in range(self.ui.input_TableWidget_relatorio_aluno_curso.columnCount()):
                dados.append(self.ui.input_TableWidget_relatorio_aluno_curso.item(row, column).text())
        
            all_dados.append(dados)
            dados = []

        columns = ['NOME', 'CPF', 'TELEFONE', 'EMAIL', 'CURSO', 'PERIODO', 'DATA INICIO', 'DATA FIM', 'TIPO', 'DESCRIÇÃO']
        
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
        
    def gerar_excel_relatorio_psi(self):
        dados = []
        all_dados =  []

        for row in range(self.ui.input_TableWidget_relatorio_psi.rowCount()):
            for column in range(self.ui.input_TableWidget_relatorio_psi.columnCount()):
                dados.append(self.ui.input_TableWidget_relatorio_psi.item(row, column).text())
        
            all_dados.append(dados)
            dados = []

        columns = ['NOME', 'CPF', 'CNS', 'SEXO', 'TELEFONE', 'EMAIL', 'CLINICA', 'DATA', 'TIPO', 'DESCRIÇÃO']
        
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
        
    def gerar_excel_relatorio_beneficio(self):
        dados = []
        all_dados =  []

        for row in range(self.ui.input_TableWidget_relatorio_psi.rowCount()):
            for column in range(self.ui.input_TableWidget_relatorio_psi.columnCount()):
                dados.append(self.ui.input_TableWidget_relatorio_psi.item(row, column).text())
        
            all_dados.append(dados)
            dados = []

        columns = ['NOME', 'CPF', 'CNS', 'SEXO', 'TELEFONE', 'EMAIL', 'CLINICA', 'DATA', 'TIPO', 'DESCRIÇÃO']
        
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


    def alterar_cadastro_beneficios_farmaceutica(self, dados):
        try:
            dados = []

            for row in range(self.ui.input_TableWidget_cadastro_beneficio_farm.rowCount()):
                row_data = []
                for column in range(self.ui.input_TableWidget_cadastro_beneficio_farm.columnCount()):
                    item = self.ui.input_TableWidget_cadastro_beneficio_farm.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append("")  
                dados.append(row_data)

            for emp in dados:
                resultado = self.db.alterar_cadastro_beneficios(emp)

            self.listarBeneficiosFarmaceutica()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Alterção Beneficio")
            msg.setText("Benefcio Alterado com sucesso!")
            msg.exec()
            
                
            return "OK", "Benefício(s) atualizado(s) com sucesso!!"
        except Exception as err:
            return "ERRO", str(err)
        

    def excluir_cadastro_beneficios_farmaceutica(self):
        id_beneficios = self.ui.input_TableWidget_cadastro_beneficio_farm.selectionModel().currentIndex().siblingAtColumn(0).data()
        self.db.deletar_cadastro_beneficios(id_beneficios)
        self.listarBeneficiosFarmaceutica()
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


    def fotoLoginColab(self, id_colab):
        caminho = self.db.buscar_foto_colaborador(id_colab)
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

                    self.ui.label_foto_colab_inicio.setPixmap(pixmap)

                    self.ui.label_foto_colab_inicio.setFixedSize(QSize(w, h))

                    self.ui.label_foto_colab_inicio.setAlignment(Qt.AlignCenter)
                else:
                    print("Erro ao ler a imagem.")
            else:
                print("O arquivo de imagem não existe:", caminho)
        else:
            print("Caminho inválido:", caminho)

    def trocarFotoSenha(self):
        #Recebe o nome da label do colab logado no sistema
        self.nome_colab_perfil = self.ui.lineEdit_recebe_nome_as.text()

        #Recebe o Id do select do banco
        self.id_colab = self.db.select_nome_colab_login(self.nome_colab_perfil)

        #Trata o Id recebido 
        id_colab_nt = self.id_colab[0][0]
        id_colab_tratado = id_colab_nt

        #Passo como parametros as variaveis com as informções do colab
        msg = DialogAlterarSenhaFoto(self, id_colab_tratado, self.nome_colab_perfil)
        self.popup.show()
        msg.exec()
        self.popup.hide()
        self.fotoLoginColab(id_colab_tratado)
        


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

            if not validarCamposClinicaCadastro(cnpj,telefone,email,cep,numero):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Erro Cadastro")
                msg.setText("Erro cadastro clinica")
                msg.exec()

            else:
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
        print(codigo)
        lote = self.ui.input_lote_cadastro_beneficio.text()
        dados = self.db.busca_beneficios()
        unidade_medida = self.ui.input_comboBox_udm_cadastro_benefecio.currentText()
        
        if unidade_medida == 'Quilo':
            self.ui.input_comboBox_udm_cadastro_benefecio.currentText()
            
        descricao = self.ui.input_descricao_cadastro_beneficio.text()
        vali=self.ui.input_dateEdit_cadastro_beneficio.text()
            
        validade = "-".join(vali.split("/")[::-1])          
        print(validade)
        quantidade = self.ui.input_spinBox_cadastro_beneficio.value()
        print(quantidade)
        tupla_beneficios = (tipo,codigo,lote,unidade_medida,descricao,validade,quantidade)
        

        if not validarCamposBeneficiosCadastro(tipo, codigo, unidade_medida, quantidade):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Erro Cadastro")
            msg.setText("Erro ao cadastrar Beneficio!")
            msg.exec()
        
        else:
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

    def cadastro_beneficios_farmaceutica(self):
            
        ########################## dados ######################################       
            dados = self.db.busca_beneficios()
            tipo = self.ui.input_tipo_cadastro_beneficio_farm.currentText()   
            if tipo == 'Medicação':
                self.ui.input_tipo_cadastro_beneficio_farm.currentText()         

            codigo = self.ui.input_codigo_cadastro_beneficio_2_farm.text()
            lote = self.ui.input_codigo_cadastro_beneficio_2_farm.text()
            dados = self.db.busca_beneficios()
            unidade_medida = self.ui.input_comboBox_udm_cadastro_benefecio_farm.currentText()
            
            if unidade_medida == 'Quilo':
                self.ui.input_comboBox_udm_cadastro_benefecio_farm.currentText()
              
            descricao = self.ui.input_descricao_cadastro_beneficio_farm.text()
            vali=self.ui.input_dateEdit_cadastro_beneficio_farm.text()
             
            validade = "-".join(vali.split("/")[::-1])          
            quantidade = self.ui.input_spinBox_cadastro_beneficio_farm.value()

            tupla_beneficios = (tipo,codigo,lote,unidade_medida,descricao,validade,quantidade)
            if not validarCamposBeneficiosFarmaceuticaCadastro(tipo, codigo, unidade_medida, quantidade):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Erro Cadastro")
                msg.setText("Erro Cadastro!")
                msg.exec()

            else:
                result = []
                result=self.db.cadastro_beneficios(tupla_beneficios)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Cadastro Beneficios")
                msg.setText("Beneficio cadastrado com sucesso!")
                msg.exec()
                # self.msg(result[0],result[1])
                self.limparCamposCadastroBeneficiosFarmaceutica()
                self.listarBeneficiosFarmaceutica()
    
    def buscarRetirada(self):
        cpf_tmp = self.ui.input_cpf_cadastro_retirada_beneficio.text()
        cpf = re.sub(r'[^\w\s]','',cpf_tmp)
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
        
    def buscarRetiradaFarmaceutica(self):
        cpf_tmp = self.ui.input_cpf_cadastro_retirada_beneficio_farm.text()
        cpf = re.sub(r'[^\w\s]','',cpf_tmp)
        print(cpf)
        result = self.db.select_retirada_beneficio_cpf(cpf)
        
        print (result)
        if result:
            id_matricula = result.get('id_matricula', '')
            print(id_matricula)
            nome = result.get('nome', '')
            idade = result.get('idade', '')          
            telefone = result.get('telefone', '')
            cns = result.get('cns','')
            clinica = result.get('clinica', 'Não possui')

            self.ui.input_id_usuario_retirada_beneficio_farm.setText(str(id_matricula))
            self.ui.input_id_usuario_retirada_beneficio_farm.hide()
            self.ui.input_nome_cadastro_retirada_beneficio_2.setText(nome)
            self.ui.input_idade_cadastro_retirada_beneficio_farm.setText(str(idade))
            self.ui.input_telefone_cadastro_retirada_beneficio_farm.setText(telefone)            
            self.ui.input_cns_cadastro_retirada_beneficio_farm.setText(cns)
            self.ui.input_clinica_cadastro_retirada_beneficio_farm.setText(str(clinica))
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
        
    def buscarCodigoRetiradaFarmaceutica(self):
        codigo = self.ui.input_codigo_beneficio_cadastro_retirada_beneficio_farm.text()
        result = self.db.select_retirada_beneficio_codigo(codigo)
        
        if result:
            id_beneficios = result.get('id_beneficios', '')
            descricao = result.get('descricao', '')
            
            self.ui.input_codigo_beneficio_cadastro_retirada_beneficio_farm.setText(str(id_beneficios))
            self.ui.input_descricao_cadastro_retirada_beneficio_farm.setText(descricao)
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
            cpf_tmp = self.ui.input_cpf_cadastro_retirada_beneficio.text()
            cpf = re.sub(r'[^\w\s]','',cpf_tmp)
            print(cpf)
            data_retirada = self.ui.input_data_cadastro_retirada_beneficio.text()
            data_consulta = "-".join(data_retirada.split("/")[::-1]) 
            codigo_retirada = self.ui.input_codigo_beneficio_cadastro_retirada_beneficio.text()
            quantidade_retirada = self.ui.input_spinBox_cadastro_retirada_beneficio.value()

            tupla_retirada_beneficios = (id_matricula,cpf,codigo_retirada,quantidade_retirada,data_consulta)
            if not validarCamposRetiradaBeneficiosCadastro(cpf, data_retirada, codigo_retirada, quantidade_retirada):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Erro Cadastro")
                msg.setText("Erro Cadastro!")
                msg.exec()

            else:
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

    def cadastro_retirada_beneficios_farmaceutica(self):
            id_matricula = self.ui.input_id_usuario_retirada_beneficio_farm.text()
            cpf_tmp = self.ui.input_cpf_cadastro_retirada_beneficio_farm.text()
            cpf = re.sub(r'[^\w\s]','',cpf_tmp)
            data_retirada = self.ui.input_data_cadastro_retirada_beneficio_2_farm.text()
            data_consulta = "-".join(data_retirada.split("/")[::-1]) 
            codigo_retirada = self.ui.input_codigo_beneficio_cadastro_retirada_beneficio_farm.text()
            quantidade_retirada = self.ui.input_spinBox_cadastro_retirada_beneficio_farm.value()

            tupla_retirada_beneficios = (id_matricula,cpf,codigo_retirada,quantidade_retirada,data_consulta)
            if not validarCamposRetiradaBeneficiosFarmaceuticaCadastro(cpf, quantidade_retirada, data_retirada, codigo_retirada):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Erro Cadastro")
                msg.setText("Erro Cadastro!")
                msg.exec()

            else:

                result = []
                result=self.db.cadastro_retirada_beneficios(tupla_retirada_beneficios)
                print (result)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Cadastro Retirada de Beneficios")
                msg.setText("Cadastro de retirada efetuado com sucesso!")
                msg.exec()
                # self.msg(result[0],result[1])
                self.limparCamposCadastroRetiradaBeneficiosFarmaceutica()
    
######################## Pessoa com Deficiencia ###############################
   
    def pessoa_com_deficiencia (self):

        if self.ui.input_pessoa_cdeficiencia_sim_usuario_as.isChecked() == True:

            self.ui.input_tipo_deficiencia_usuario_as.setEnabled(True)
            self.ui.input_tipo_deficiencia_usuario_as.setCurrentIndex(int(0)) 

        else:
            self.ui.input_tipo_deficiencia_usuario_as.setEnabled(False)
            self.ui.input_tipo_deficiencia_usuario_as.setCurrentIndex(int(6))    
             
                
    def pessoa_com_deficiencia_alterar (self):
        
        if self.ui.input_alterar_pessoa_cdeficiencia_sim_usuario_as.isChecked() == True:

            self.ui.input_alterar_tipo_deficiencia_usuario_as.setEnabled(True)
            self.ui.input_alterar_tipo_deficiencia_usuario_as.setCurrentIndex(int(0))
        
        else:
        
            self.ui.input_alterar_tipo_deficiencia_usuario_as.setEnabled(False)
            self.ui.input_alterar_tipo_deficiencia_usuario_as.setCurrentIndex(int(6))
                      
            
############################### Deficiência base Outra ####################################

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
                
    def relatorio_pessoa_nutri(self): #ALIMENTA A TABELA A DE RELATORIO
        
        result = self.db.relatorio_pessoa_nutri(self.id_colab_tratado_nutri)

        self.ui.input_TableWidget_relatorio_nutri.clearContents()
        self.ui.input_TableWidget_relatorio_nutri.setRowCount(len(result))   

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_nutri.setItem(row, column,QTableWidgetItem(str(data)))
  
    def filtrar_dados(self):
        txt = re.sub('[\W_]+','',self.ui.input_buscar_dados_relatorio_as.text())
        res = self.db.filtrar_relatorio(txt)
        self.ui.tableWidget_relatorio_as.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.tableWidget_relatorio_as.setItem(row, column, QTableWidgetItem(str(data)))
                
    def filtrar_dados_participantes_curso(self):
        txt = re.sub('[\W_]+','',self.ui.input_buscar_dados_relatorio_aluno_curso.text())
        res = self.db.buscar_participantes_curso_pesquisa(txt)
        self.ui.input_TableWidget_relatorio_aluno_curso.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_aluno_curso.setItem(row, column, QTableWidgetItem(str(data)))
                
    def filtrar_dados_relatorio_psi(self):
        txt = re.sub('[\W_]+','',self.ui.input_buscar_dados_relatorio_psi.text())
        res = self.db.buscar_relatorio_psi_pesquisa(txt)
        self.ui.input_TableWidget_relatorio_psi.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_psi.setItem(row, column, QTableWidgetItem(str(data)))
    
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
                
    def filtrar_data_participante_curso(self):  
        texto_data_inicio = self.ui.input_inicio_periodo_relatorio_aluno_curso.text()
        texto_data_final = self.ui.input_final_periodo_relatorio_aluno_curso.text()
        texto_data_inicio_tratada =  "-".join(texto_data_inicio.split("/")[::-1])
        texto_data_final_tratada =  "-".join(texto_data_final.split("/")[::-1])
        
        res = self.db.filter_data_participante_curso(texto_data_inicio_tratada,texto_data_final_tratada)
        print(res)

        self.ui.input_TableWidget_relatorio_aluno_curso.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_aluno_curso.setItem(row, column, QTableWidgetItem(str(data)))
    
    def filtrar_data_relatorio_psi(self):  
        texto_data_inicio_psi = self.ui.input_inicio_periodo_relatorio_psi.text()
        texto_data_final_psi = self.ui.input_final_periodo_relatorio_psi.text()
        texto_data_inicio_tratada_psi =  "-".join(texto_data_inicio_psi.split("/")[::-1])
        texto_data_final_tratada_psi =  "-".join(texto_data_final_psi.split("/")[::-1])
        
        res = self.db.filter_data_relatorio_psi(texto_data_inicio_tratada_psi,texto_data_final_tratada_psi)

        self.ui.input_TableWidget_relatorio_psi.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_psi.setItem(row, column, QTableWidgetItem(str(data)))

    def gerar_excel_relatorio_beneficio(self):
        dados = []
        all_dados =  []

        for row in range(self.ui.input_TableWidget_relatorio_beneficios_as.rowCount()):
            for column in range(self.ui.input_TableWidget_relatorio_beneficios_as.columnCount()):
                dados.append(self.ui.input_TableWidget_relatorio_beneficios_as.item(row, column).text())
        
            all_dados.append(dados)
            dados = []

        columns = ['NOME', 'CPF', 'CNS', 'SEXO', 'SITUAÇÃO DE TRABALHO', 'BENEFICIO SOCIAL', 'TIPO BENEFICIO', 'DESCRIÇÃO', 'QUANTIDADE','DATA']
        
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

    def gerar_excel_relatorio_beneficio_farm(self):
        dados = []
        all_dados =  []

        for row in range(self.ui.input_TableWidget_relatorio_beneficios_farm.rowCount()):
            for column in range(self.ui.input_TableWidget_relatorio_beneficios_farm.columnCount()):
                dados.append(self.ui.input_TableWidget_relatorio_beneficios_farm.item(row, column).text())
        
            all_dados.append(dados)
            dados = []
            print(dados)
            print(all_dados)

        columns = ['NOME', 'CPF', 'CNS', 'SEXO', 'SITUAÇÃO DE TRABALHO', 'BENEFICIO SOCIAL', 'DESCRIÇÃO', 'QUANTIDADE','DATA']
        
        relatorio = pd.DataFrame(all_dados, columns= columns)

        
        file, _ = QFileDialog.getSaveFileName(self,"Relatorio", "", "Text files (*.xlsx)") 
        if file:
            with open(file, "w") as f:
                relatorio.to_excel(file, sheet_name='relatorio', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()

    def relatorio_beneficio(self):
        result = self.db.relatorio_beneficio()

        self.ui.input_TableWidget_relatorio_beneficios_as.clearContents()
        self.ui.input_TableWidget_relatorio_beneficios_as.setRowCount(len(result))
          
        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_beneficios_as.setItem(row, column,QTableWidgetItem(str(data)))

    def filtrar_dados_beneficio(self):
        txt = re.sub('[\W_]+','',self.ui.input_buscar_dados_relatorio_beneficios_as.text())
        res = self.db.filtrar_relatorio_beneficio(txt)
        self.ui.input_TableWidget_relatorio_beneficios_as.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_beneficios_as.setItem(row, column, QTableWidgetItem(str(data)))

    def filtrar_data_beneficio(self): 
        texto_data_inicio = self.ui.input_inicio_periodo_relatorio_beneficio_as.text()
        texto_data_final = self.ui.input_final_periodo_relatorio_beneficio_as.text()
        texto_data_inicio_tratada =  "-".join(texto_data_inicio.split("/")[::-1])
        texto_data_final_tratada =  "-".join(texto_data_final.split("/")[::-1])
        
        res = self.db.filter_data_relatorio_beneficio(texto_data_inicio_tratada,texto_data_final_tratada)

        self.ui.input_TableWidget_relatorio_beneficios_as.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_beneficios_as.setItem(row, column, QTableWidgetItem(str(data)))
                   
    def filter_idade(self):

        texto_idade_inicio = self.ui.input_idade_inicial_relatorio_as.text()
        texto_idade_final = self.ui.input_idade_final_relatorio_as.text()
        
        res = self.db.filter_idade(texto_idade_inicio,texto_idade_final)
        self.ui.tableWidget_relatorio_as.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.tableWidget_relatorio_as.setItem(row, column, QTableWidgetItem(str(data)))

    def puxar_relatorio_atendimento(self):
        result = self.db.buscar_relatorio_atendimento()
        self.ui.input_TableWidget_relatorio_atendimentos.clearContents()
        self.ui.input_TableWidget_relatorio_atendimentos.setRowCount(len(result))
        
        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_atendimentos.setItem(row, column,QTableWidgetItem(str(data)))
                

    def filtrar_dados_relatorio_atendimento(self):
        txt = re.sub('[\W_]+','',self.ui.input_buscar_dados_relatorio_atendimentos.text())
        res = self.db.buscar_relatorio_atendimento_pesquisa(txt)
        self.ui.input_TableWidget_relatorio_atendimentos.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_atendimentos.setItem(row, column, QTableWidgetItem(str(data)))

    def filtrar_data_relatorio_atendimento(self): 
        texto_data_inicio_atendimento = self.ui.input_inicio_periodo_relatorio_atendimentos.text()
        texto_data_final_atendimento = self.ui.input_final_periodo_relatorio_atendimentos.text()
        texto_data_inicio_atendimento =  "-".join(texto_data_inicio_atendimento.split("/")[::-1])
        texto_data_final_atendimento =  "-".join(texto_data_final_atendimento.split("/")[::-1])
        
        res = self.db.filter_data_relatorio_atendimento(texto_data_inicio_atendimento,texto_data_final_atendimento)

        self.ui.input_TableWidget_relatorio_atendimentos.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_relatorio_atendimentos.setItem(row, column, QTableWidgetItem(str(data)))

    def gerar_excel(self):
        dados = []
        all_dados =  []

        for row in range(self.ui.tableWidget_relatorio_as.rowCount()):
            for column in range(self.ui.tableWidget_relatorio_as.columnCount()):
                dados.append(self.ui.tableWidget_relatorio_as.item(row, column).text())
        
            all_dados.append(dados)
            dados = []

        columns = ['NOME', 'CPF', 'IDADE', 'SEXO', 'TELEFONE', 'BENEFICIO', 'CNS', 'NIS',
            'APOSENTADORIA','CLINICA','BAIRRO','CIDADE']
        
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




    def buscar_relatorio_agendamento(self):
        result = self.db.buscar_relatorio_agendamento()
        print(result)
        self.ui.tableWidget_relatorio_agendamento_as.clearContents()
        self.ui.tableWidget_relatorio_agendamento_as.setRowCount(len(result))
          
        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.tableWidget_relatorio_agendamento_as.setItem(row, column,QTableWidgetItem(str(data)))



    def filtrar_relatorio_agendamento(self):
            txt = re.sub('[\W_]+','',self.ui.input_buscar_dados_relatorio_agendamento_as.text())
            res = self.db.filtrar_relatorio_agendamento(txt)
            self.ui.tableWidget_relatorio_agendamento_as.setRowCount(len(res))

            for row, text in enumerate(res):
                for column, data in enumerate(text):
                    self.ui.tableWidget_relatorio_agendamento_as.setItem(row, column, QTableWidgetItem(str(data)))








                    
    def filter_relatorio_agendamento(self):  
        texto_data_inicio_relatorio_agend = self.ui.input_inicio_periodo_relatorio_gendamento_as.text()
        texto_data_final_relatorio_agend = self.ui.input_final_periodo_relatorio_agendamento_as.text()
        texto_data_inicio_relatorio_agend =  "-".join(texto_data_inicio_relatorio_agend.split("/")[::-1])
        texto_data_final_relatorio_agend =  "-".join(texto_data_final_relatorio_agend.split("/")[::-1])
        
        res = self.db.filter_data_relatorio_agendamento(texto_data_inicio_relatorio_agend,texto_data_final_relatorio_agend)

        self.ui.tableWidget_relatorio_agendamento_as.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.tableWidget_relatorio_cuidadores_as.setItem(row, column, QTableWidgetItem(str(data)))






                



    def gerar_excel_relatorio_agendamento(self):
        dados = []
        all_dados =  []

        for row in range(self.ui.tableWidget_relatorio_agendamento_as.rowCount()):
            for column in range(self.ui.tableWidget_relatorio_agendamento_as.columnCount()):
                dados.append(self.ui.tableWidget_relatorio_agendamento_as.item(row, column).text())
        
            all_dados.append(dados)
            dados = []

        columns = ['NOME', 'CPF', 'SEXO', 'TELEFONE', 'CLINICA', 'PROFISSIONAL', 'DATA', 'HORA', "TIPO"
        ]
        
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












    def gerar_excel_relatorio_cuidador(self):
        dados = []
        all_dados =  []

        for row in range(self.ui.tableWidget_relatorio_cuidadores_as.rowCount()):
            for column in range(self.ui.tableWidget_relatorio_cuidadores_as.columnCount()):
                dados.append(self.ui.tableWidget_relatorio_cuidadores_as.item(row, column).text())
        
            all_dados.append(dados)
            dados = []

        columns = ['NOME CUIDADOR', 'CPF', 'IDADE', 'SEXO', 'TELEFONE', 'ENDEREÇO', 'BAIRRO', 'CIDADE',
            'USUARIO','PARENTESCO']
        
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

    def gerar_excel_relatorio_clinicas_cadastradas(self):
        dados = []
        all_dados =  []

        for row in range(self.ui.input_TableWidget_relatorio_relatorio_clinicas_cadastradas_as.rowCount()):
            for column in range(self.ui.input_TableWidget_relatorio_relatorio_clinicas_cadastradas_as.columnCount()):
                dados.append(self.ui.input_TableWidget_relatorio_relatorio_clinicas_cadastradas_as.item(row, column).text())
        
            all_dados.append(dados)
            dados = []

        columns = ['CNPJ', 'EMAIL', 'RAZAO_SOCIAL', 'TELEFONE', 'ENDEREÇO']
        
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

    def gerar_excel_relatorio_fornecedor_cadastrado(self):
        dados = []
        all_dados =  []

        for row in range(self.ui.input_TableWidget_relatorio_relatorio_fornecedores_cadastrados.rowCount()):
            for column in range(self.ui.input_TableWidget_relatorio_relatorio_fornecedores_cadastrados.columnCount()):
                dados.append(self.ui.input_TableWidget_relatorio_relatorio_fornecedores_cadastrados.item(row, column).text())
        
            all_dados.append(dados)
            dados = []

        columns = ['CNPJ', 'RAZAO_SOCIAL','TELEFONE','TELEFONE_CONTATO', 'EMAIL', 'ENDERECO', 'CIDADE','ESTADO']
        
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


    def gerar_excel_relatorio_atendimento(self):
        dados = []
        all_dados =  []

        for row in range(self.ui.input_TableWidget_relatorio_atendimentos.rowCount()):
            for column in range(self.ui.input_TableWidget_relatorio_atendimentos.columnCount()):
                dados.append(self.ui.input_TableWidget_relatorio_atendimentos.item(row, column).text())
        
            all_dados.append(dados)
            dados = []

        columns = ['NOME', 'CPF', 'CNS', 'SEXO', 'TELEFONE', 'EMAIL', 'RAZAO_SOCIAL', 'DATA_CONSULTA', 'SITUACAO']
        
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
    
