from PySide6.QtCore import QDateTime
class LimparCamposAtendimentoNutricionista:
    def __init__(self, TelaPrincipal):
        self.ui = TelaPrincipal

    def execute(self):
        print("ENTREI NA FUNÇAO")
        self.ui.input_cpf_pagina_consulta_geral_nutri.setText("")
        self.ui.input_nome_pagina_consulta_geral_nutri.setText("")
        self.ui.input_contato_pagina_consulta_geral_nutri.setText("")
        self.ui.input_clinica_pagina_consulta_geral_nutri.setText("")
        self.ui.input_tipo_tratamento_consulta_nutri.setCurrentIndex(0)
        self.ui.input_patologia_base_consulta_nutri.setCurrentIndex(0)
        self.ui.input_peso_consulta_nutri.setText("")
        self.ui.input_altura_consulta_nutri.setText("")
        self.ui.input_imc_consulta_nutri.setText("")
        self.ui.radioButton_atendimento_as_nutri.setCheckable(False)
        self.ui.radioButton_atendimento_as_nutri.setCheckable(True)
        self.ui.radioButton_Retorno_as_nutri.setCheckable(False)
        self.ui.radioButton_Retorno_as_nutri.setCheckable(True)
        self.ui.input_data_pagina_consulta_geral_nutri.setDateTime(QDateTime.currentDateTime())
        self.ui.input_hora_consulta_as_nutri.setText("")
        self.ui.input_evolucao_pagina_consulta_geral_nutri.setHtml("")
        self.ui.input_filtro_pagina_consulta_geral_nutri.setText("")



#def limparCamposAtendimentoNutricionista(self):
#    self.ui.input_cpf_pagina_consulta_geral_nutri.setText("")
#    self.ui.input_nome_pagina_consulta_geral_nutri.setText("")
#    self.ui.input_contato_pagina_consulta_geral_nutri.setText("")
#    self.ui.input_clinica_pagina_consulta_geral_nutri.setText("")
#    self.ui.input_tipo_tratamento_consulta_nutri.setCurrentIndex(0)
#    self.ui.input_patologia_base_consulta_nutri.setCurrentIndex(0)
#    self.ui.input_peso_consulta_nutri.setText("")
#    self.ui.input_altura_consulta_nutri.setText("")
#    self.ui.input_imc_consulta_nutri.setText("")
#    self.ui.radioButton_atendimento_as_nutri.setCheckable(False)
#    self.ui.radioButton_atendimento_as_nutri.setCheckable(True)
#    self.ui.radioButton_Retorno_as_nutri.setCheckable(False)
#    self.ui.radioButton_Retorno_as_nutri.setCheckable(True)
#    self.ui.input_data_pagina_consulta_geral_nutri.setDateTime(QDateTime.currentDateTime())
#    self.ui.input_hora_consulta_as_nutri.setText("")
#    self.ui.input_evolucao_pagina_consulta_geral_nutri.setHtml("")
#    self.ui.input_filtro_pagina_consulta_geral_nutri.setText("")