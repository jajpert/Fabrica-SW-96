from qtcore import *

def validarCamposClinicaCadastro(cnpj,razao_social,telefone,email,cep, numero):
    if cnpj == "" or len(cnpj) < 14:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro CNPJ")
        msg.setText("Digite um CNPJ válido!!!")
        msg.exec()
        return False
    
    elif razao_social == "" or len(razao_social) <= 5:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro Razão Social")
        msg.setText("Digite uma Razão social válida!!!")
        msg.exec()
        return False
    
    
    elif telefone == "" or len(telefone) < 10:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro TELEFONE")
        msg.setText("Digite um Telefone válido!!!")
        msg.exec()
        return False
    
    elif email == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro EMAIL")
        msg.setText("Digite um Email válido!!!")
        msg.exec()
        return False
    
    elif cep == "" or len(cep) < 10:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro CEP")
        msg.setText("Digite um CEP válido!!!")
        msg.exec()
        return False
    
    elif numero == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro NUMERO")
        msg.setText("Digite um numero válido!!!")
        msg.exec()
        return False
    
    else:
        return True