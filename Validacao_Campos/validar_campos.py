from qtcore import *

def validarCamposUsuarioCadastro(cpf):
    if cpf == "" or len(cpf) < 11:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("ERRO")
        msg.setText("ERRO")
        msg.exec()
        return False
    # elif rg == "" or len(rg) < 7:

    # elif nis == "" or len(nis) < 15:

    # elif cns == "" or len(cns) < 15:

    # elif sexo != self.ui.input_situacao_ativo_usuario_as.isChecked():

    # elif telefone == "" or len(telefone) < 11:

    # elif cep == "" or len(cep) < 10:
    else:
        return True