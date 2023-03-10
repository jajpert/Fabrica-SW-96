import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui_telas_abrec import Ui_MainWindow
import mysql.connector

conexao = mysql.connector.connect(host = '192.168.22.9', 
database = 'fabrica96', user = 'fabrica', password = 'fabrica@2022')

if conexao.is_connected ():
    db_info = conexao.get_server_info()
    print ("Conectado ao banco de dados = ", db_info)

cursor = conexao.cursor()

class DataBase(QMainWindow):

    def __init__(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
    def conexaoBD_Colaborador(self):
        nome_colaborador = input(self.ui.input_nome_colaborador_as.text())
        data_nascimento= input(self.ui.input_data_nascimento_colaborador_as.text())

        comando = f'(INSERT INTO cadastro (nome_colaborador,data_nascimento) values ({nome_colaborador},date_format({data_nascimento},%d/%m%Y)'

        cursor.execute(comando)
        conexao.commit()

        #comando = f'(INSERT INTO cadastro(matricula,nome_colaborador,data_nascimento,cpf,data_nascimento,endereco,telefone,salario)'

cursor.close() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = DataBase()
    db.show()
    app.exec()
    