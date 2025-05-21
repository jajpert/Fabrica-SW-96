from qtcore import *
from ui_telas_abrec import *

def validarCamposAlterarColaboradorCadastro(senha, conf_senha): 
    if senha != conf_senha:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro SENHA")
        msg.setText("Senhas não são iguais!!!")
        msg.exec()
        return False
    
    else:
        return True