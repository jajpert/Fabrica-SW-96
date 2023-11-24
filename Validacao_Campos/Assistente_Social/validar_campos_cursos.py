from qtcore import *

def validarCamposCursoCadastro(tipo, responsavel, horario_inicial, horario_final, periodo, vagas):
    if tipo == "" or tipo == "Selecione...":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro TIPO")
        msg.setText("Favor selecionar um tipo para o curso!!!")
        msg.exec()
        return False
    
    elif responsavel == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro RESPONSAVEL")
        msg.setText("Digite um responsavel para o curso!!!")
        msg.exec()
        return False
    
    elif horario_inicial == "00:00":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro HORA INICIO")
        msg.setText("Digite uma hora de inicio do curso!!!")
        msg.exec()
        return False
    
    elif horario_final == "00:00":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro HORA FINAL")
        msg.setText("Digite uma hora de final do curso!!!")
        msg.exec()
        return False
    
    elif periodo == "Selecione":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro PERIODO")
        msg.setText("Favor informe o periodo para o curso!!!")
        msg.exec()
        return False
    
    elif vagas == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Erro VAGAS")
        msg.setText("Favor informe a quantidade de vagas para o curso!!!")
        msg.exec()
        return False

    else:
        return True