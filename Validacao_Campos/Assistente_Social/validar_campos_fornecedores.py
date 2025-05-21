from qtcore import *

def validarCamposFornecedoresCadastro(cnpj, celular, email, inscricao_estadual, inscricao_municipal, cep, numero):
    if cnpj == "" or len(cnpj) < 14:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro CNPJ")
        msg.setText("Digite um CNPJ válido!!!")
        msg.exec()
        return False
    
    elif celular == "" or len(celular) < 11:
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
    
    elif inscricao_estadual == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro Inscrição Estatual")
        msg.setText("Digite uma Incrição Estatual válida!!!")
        msg.exec()
        return False
    
    elif inscricao_municipal == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro Inscrição Municipal")
        msg.setText("Digite uma Incrição Municipal válida!!!")
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
        msg.setText("Digite um NUMERO válido!!!")
        msg.exec()
        return False
    
    else:
        return True