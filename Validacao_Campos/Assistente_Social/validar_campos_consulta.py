from qtcore import *

def validarCamposConsultaCadastro(situacao):
    if situacao == "" or situacao == None:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro Situação")
        msg.setText("Favor informar a situação do usuario!!!")
        msg.exec()

    else:
        return True