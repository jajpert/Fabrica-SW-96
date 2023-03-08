from ui_telas_abrec import *

import mysql.connector

conexao = mysql.connector.connect(host = '192.168.22.9', 
database = 'fabrica96', user = 'fabrica', password = 'fabrica@2022')

if conexao.is_connected ():
    db_info = conexao.get_server_info()
    print ("Conectado ao banco de dados = ", db_info)

class DataBase(object):

   def __init__(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    '''def conexaoBD_Colaborador(self):
        matricula = input(self.ui.input_matricula_colaborador_as.text())
        nome_colaborador = input(self.ui.input_nome_colaborador_as.text())

        comando = INSERT INTO cadastro(nome,cpf,data_nascimento,endereco,telefone,salario)'''

        

