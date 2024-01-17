from qtcore import *
from ui_telas_abrec import *

def validarCamposUsuarioCadastro(cpf,rg,nis,cns,telefone,sexo,cep,numero):
    if cpf == "" or len(cpf) < 11:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro CPF")
        msg.setText("Favor inserir um CPF valido!!!")
        msg.exec()
        return False
    elif rg == "" or len(rg) < 7:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro RG")
        msg.setText("Favor inserir um RG válido!!!")
        msg.exec()
        return False

    elif nis == "" or len(nis) < 11:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro NIS")
        msg.setText("Favor inserir um NIS válido!!!")
        msg.exec()
        return False

    elif cns == "" or len(cns) < 15:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro CNS")
        msg.setText("Favor inserir um CNS válido!!!")
        msg.exec()
        return False

    elif sexo == "" or sexo == "Selecione":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro SEXO")
        msg.setText("Favor selecione um Sexo!!!")
        msg.exec()
        return False

    elif telefone == "" or len(telefone) < 10:
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
    else:
        return True