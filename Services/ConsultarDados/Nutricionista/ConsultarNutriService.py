import re

from PySide6.QtCore import *
from PySide6.QtWidgets import *


class ConsultarNutriService:
    def __init__(self, Database, TelaPrincipal):
        self.ui = TelaPrincipal
        self.db = Database

    # SELECT USUARIO SOZINHO CONSULTA NUTRI
    def buscar_dados_consulta_nutri(self):
        cpf_temp = self.ui.input_cpf_pagina_consulta_geral_nutri.text()
        cpf = ''
        for i in cpf_temp:
            if i == '.' or i == '-':
                pass
            else:
                cpf += i
        dados = self.db.buscar_consulta_nutri(cpf)
        flags = []
        x = 0
        for i in dados:
            if dados[x][10] == 'SIM':
                x += 1
                pass
            else:
                flags.append((tuple(dados[x])))
                x += 1
        print(flags)
        if not flags:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Usuario Agendamento")
            msg.setText("Usuario não possui agendamento!!")
            msg.exec()
            return
        x = 0
        while x <= int(len(flags)):
            if x >= len(flags):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Usuario Agendamento")
                msg.setText("Usuario não possui agendamento!!")
                msg.exec()
                return
            elif flags[x][9] == "nutri":
                if flags[x][10] == "NAO":
                    self.ui.input_id_agendamento_nutri_consulta_geral.setText(str(flags[x][0]))
                    self.ui.input_id_matricula_nutri_consulta.setText(str(flags[x][1]))
                    self.ui.input_id_matricula_nutri_consulta.hide()
                    self.ui.input_nome_pagina_consulta_geral_nutri.setText(flags[x][2])
                    self.ui.input_contato_pagina_consulta_geral_nutri.setText(flags[x][3])
                    self.ui.input_clinica_pagina_consulta_geral_nutri.setText(flags[x][4])
                    self.ui.input_data_pagina_consulta_geral_nutri.setDate(QDate(flags[x][5]))
                    hora = str(flags[x][6]).split(":")
                    self.ui.input_hora_consulta_as_nutri.setText(str(flags[x][6]))
                    tipo_tratamento = flags[x][7]
                    if tipo_tratamento == "Transplantado/a":
                        self.ui.input_tipo_tratamento_consulta_nutri.setCurrentIndex(1)
                    elif tipo_tratamento == "Prevenção":
                        self.ui.input_tipo_tratamento_consulta_nutri.setCurrentIndex(2)
                    elif tipo_tratamento == "Pré-Diálise":
                        self.ui.input_tipo_tratamento_consulta_nutri.setCurrentIndex(3)
                    elif tipo_tratamento == "Hemodiálise":
                        self.ui.input_tipo_tratamento_consulta_nutri.setCurrentIndex(4)
                    elif tipo_tratamento == "Diálise Peritoneal":
                        self.ui.input_tipo_tratamento_consulta_nutri.setCurrentIndex(5)
                    patologia_base = flags[x][8]
                    if patologia_base == "Hipertensão":
                        self.ui.input_patologia_base_consulta_nutri.setCurrentIndex(1)
                    elif patologia_base == "Diabete 1":
                        self.ui.input_patologia_base_consulta_nutri.setCurrentIndex(2)
                    elif patologia_base == "Diabete 2":
                        self.ui.input_patologia_base_consulta_nutri.setCurrentIndex(3)
                    elif patologia_base == "Lúpus":
                        self.ui.input_patologia_base_consulta_nutri.setCurrentIndex(4)
                    elif patologia_base == "Nefrites":
                        self.ui.input_patologia_base_consulta_nutri.setCurrentIndex(5)
                    elif patologia_base == "Outros":
                        self.ui.input_patologia_base_consulta_nutri.setCurrentIndex(6)
                    (self.db.tabela_consulta_nutri_tabela())
                    print(flags[x][0])
                    break
            else:
                x += 1

    # BUSCA USUARIO AGENDAMENTO NUTRI
    def buscar_usuario_agenda_nutri(self):
        cpf_temp = self.ui.input_cpf_agendamento_nutri.text()
        cpf = ''
        for i in cpf_temp:
            if i == '.' or i == '-':
                pass
            else:
                cpf += i
        dados = self.db.busca_usuario_nutri_agendamento(cpf)
        self.ui.input_nome_agendamento_nutri.setText(dados[0])
        self.ui.input_telefone_agendamento_nutri.setText(dados[1])
        self.ui.input_clinica_agendamento_nutri.setText(dados[2])
        self.ui.input_id_matricula_nutri_agendamento.setText(str(dados[3]))
        self.ui.input_id_matricula_nutri_agendamento.hide()


    # SELECT USUARIO + COLABORADOR NUTRI
    def tabela_consulta_nutri_tabela(self):
        cpf_tmp = self.ui.input_cpf_pagina_consulta_geral_nutri.text()
        cpf = re.sub(r'[^\w\s]','',cpf_tmp)
        result = self.db.busca_nutri_consulta_tabela(cpf, self.id_colab_tratado_nutri)
        self.ui.input_TableWidget_pagina_consulta_geral_nutri.clearContents()
        self.ui.input_TableWidget_pagina_consulta_geral_nutri.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.input_TableWidget_pagina_consulta_geral_nutri.setItem(row, column,QTableWidgetItem(str(data)))