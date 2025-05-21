from qtcore import *

def validarCamposConsultaFisioCadastro(situacao, data, hora):
    if situacao == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro Situação")
        msg.setText("Favor informe a situação do usuario!!!")
        msg.exec()

    elif data == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro Data")
        msg.setText("Favor Informar uma data!!!")
        msg.exec()

    elif hora == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro Profissional")
        msg.setText("Favor Informar um horario!!!")
        msg.exec()
        
    else:
        return True