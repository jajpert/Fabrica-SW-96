from qtcore import *

def validarCamposConsultaNutriImcCadastro(peso, altura, imc):
    if peso == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro Peso")
        msg.setText("Favor informar o peso!!!")
        msg.exec()
        return False
    
    elif altura == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro Altura")
        msg.setText("Favor informar a altura !!!")
        msg.exec()

    elif imc == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro IMC")
        msg.setText("Favor informar um peso e uma altura para o IMC!!!")
        msg.exec()
        
    else:
        return True