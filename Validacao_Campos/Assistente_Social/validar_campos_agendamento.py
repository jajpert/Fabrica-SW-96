from qtcore import *

def validarCamposAgendamentoCadastro(profissional):
    if profissional == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro Profissional")
        msg.setText("Favor selecionar um profissional!!!")
        msg.exec()
        return False
    else:
        return True