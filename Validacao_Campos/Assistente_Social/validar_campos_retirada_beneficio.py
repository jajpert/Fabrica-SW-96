from qtcore import *

def validarCamposRetiradaBeneficiosCadastro(cpf, data, codigo, quantidade):
    if cpf == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro CPF")
        msg.setText("Favor informar o CPF!!!")
        msg.exec()
        return False
    
    elif data == "" or data == "01/01/2023" or data == "2023-01-01":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro DATA")
        msg.setText("Favor informe a data de retirada!!!")
        msg.exec()
        return False
    
    elif codigo == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro CODIGO")
        msg.setText("Favor informe o codigo do beneficio!!!")
        msg.exec()
        return False
    
    elif quantidade == "" or quantidade == 0:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro QUANTIDADE")
        msg.setText("Digite a quantidade de retirada!!!")
        msg.exec()
        return False
    

    else:
        return True