from PySide6.QtWidgets import *

from Services.ConsultarDados.Nutricionista.ConsultarNutriService import ConsultarNutriService
from Services.Limpar_Campos.Nutricionista.LimparCamposAtendimentoNutricionista import LimparCamposAtendimentoNutricionista
from database import DataBase


class nutriteste:
    def __init__(self, TelaPrincipal):
        self.ui = TelaPrincipal
        self.db = DataBase()
        self.carregarServices()

    def carregarServices(self):
        self.limpar = LimparCamposAtendimentoNutricionista(self.ui)
        self.consultas = ConsultarNutriService(self.db, self.ui)

    def main(self):
        ########################### NUTRICIONISTA ##########################################################################################################################################
        self.ui.btn_atendimento_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_consulta_nutri))
        self.ui.btn_atendimento_nutri.clicked.connect(self.limpar.execute())
        self.ui.btn_agenda_nutri.clicked.connect(self.limpar.execute())
        self.ui.btn_agenda_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_agenda_nutri))
        #self.ui.btn_voltar_agenda_nutri.clicked.connect(self.limparCamposAgendaNutricionista)
        self.ui.btn_voltar_agenda_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_principal_nutri))
        self.ui.btn_voltar_pagina_consulta_geral_nutri.clicked.connect(self.limpar.execute())
        self.ui.btn_voltar_pagina_consulta_geral_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_principal_nutri))
        self.ui.btn_voltar_pagina_relatorio_nutri.clicked.connect(self.limpar.execute())
        self.ui.btn_voltar_pagina_relatorio_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_principal_nutri))
        #self.ui.btn_relatorios_nutri.clicked.connect(self.teste)
        self.ui.btn_relatorios_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_relatorio_nutri))
        self.ui.btn_relatorios_nutri.clicked.connect(self.relatoriosNutri())
        #self.ui.btn_agenda_nutri.clicked.connect(self.tabela_agenda_nutri)
        self.ui.btn_buscar_cpf_pagina_consulta_geral_2.clicked.connect(self.consultas.buscar_dados_consulta_nutri())
        self.ui.btn_buscar_agendamento_nutri.clicked.connect(self.consultas.buscar_usuario_agenda_nutri())
        self.ui.btn_buscar_cpf_pagina_consulta_geral_2.clicked.connect(self.consultas.tabela_consulta_nutri_tabela())
        #self.ui.btn_salvar_agenda_nutri.clicked.connect(self.cadastroAgendamentoNutri)  # CADASTRO DO USUARIO NO AGENDAMENTO NUTRI
        #self.ui.btn_salvar_pagina_consulta_geral_nutri.clicked.connect(self.cadastrar_consulta_nutri)  # CADATRO DO USUARIO NA CONSULTA NUTRI
        #self.ui.input_altura_consulta_nutri.textChanged.connect(self.nutri_imc_usuario)  # IMC USUARIO CONSULTA NUTRI
        #self.ui.btn_relatorios_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_relatorio_nutri))
        #self.ui.btn_alterar_pagina_consulta_geral_nutri.clicked.connect(self.alterar_consulta_nutri)
        #self.ui.btn_gerar_excel_relatorio_nutri.clicked.connect(self.gerar_excel_relatorio_nutri)
        # self.ui.btn_voltar_relatorios_nutri.clicked.connect(lambda: self.ui.stackedWidget_12.setCurrentWidget(self.ui.page_principal_nutri))
        #self.ui.btn_alterar_agenda_nutri.clicked.connect(self.alterarAgendamentos_nutri)
        self.ui.btn_cancelar_agenda_nutri.clicked.connect(self.limpar.execute())
        #self.ui.btn_sair_nutri.clicked.connect(self.sairSistema)


    def relatoriosNutri(self):
        self.ui.input_filtro_pagina_relatorio_nutri.setText("")
        self.ui.input_filtro_pagina_relatorio_nutri.setPlaceholderText("Digite o CPF do paciente")
        self.ui.input_filtro_pagina_relatorio_nutri.setFocus()
        self.ui.tabela_relatorio_nutri.clearContents()
        self.ui.tabela_relatorio_nutri.setRowCount(0)
        self.ui.tabela_relatorio_nutri.setColumnCount(6)
        self.ui.tabela_relatorio_nutri.setHorizontalHeaderLabels(["ID", "CPF", "Nome", "Contato", "Clínica", "Data"])