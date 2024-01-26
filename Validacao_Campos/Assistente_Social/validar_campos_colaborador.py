from qtcore import *
from ui_telas_abrec import *

def validarCamposColaboradorCadastro(cpf,rg,telefone,cep,numero,pis, senha, conf_senha):
    if cpf == "" or len(cpf) < 11:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro CPF")
        msg.setText("Favor inserir um CPF válido!!!")
        msg.exec()
        return False
    
    elif rg == "" or len(rg) < 9:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro RG")
        msg.setText("Favor inserir um RG válido!!!")
        msg.exec()
        return False
    
    elif pis == "" or len(pis) < 11:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro PIS")
        msg.setText("Favor inserir um PIS válido!!!")
        msg.exec()
        return False
    
    elif telefone == "" or len(telefone) < 11:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro TELEFONE")
        msg.setText("Favor inserir um TELEFONE válido!!!")
        msg.exec()
        return False
    
    elif cep == "" or len(cep) < 10:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro CEP")
        msg.setText("Favor inserir um CEP válido!!!")
        msg.exec()
        return False
    
    elif numero == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro CEP")
        msg.setText("Favor inserir um CEP válido!!!")
        msg.exec()
        return False
    
    elif senha != conf_senha:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro SENHA")
        msg.setText("Senhas não são iguais!!!")
        msg.exec()
        return False
    
    else:
        return True