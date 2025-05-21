from qtcore import *

def validarCamposBeneficiosFarmaceuticaCadastro(tipo, codigo, unidade_medida, quantidade):
    if tipo == "" or tipo == "Selecione...":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro TIPO")
        msg.setText("Favor selecionar um tipo para o beneficio!!!")
        msg.exec()
        return False
    
    elif codigo == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro CODIGO")
        msg.setText("Digite um codigo para o beneficio!!!")
        msg.exec()
        return False
    
    elif unidade_medida == "Selecione...":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro UNIDADE MEDIDA")
        msg.setText("Selecione uma unidade de medida para o beneficio!!!")
        msg.exec()
        return False
    
    elif quantidade == "" or quantidade == 0:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro QUANTIDADE")
        msg.setText("Favor informe uma quantidade para o beneficio!!!")
        msg.exec()
        return False

    else:
        return True