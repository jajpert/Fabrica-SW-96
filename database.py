import mysql.connector

class DataBase():
    def __init__(self, banco = "Abrec") -> None:
        self.banco = banco

    def connect(self):
        
        self.conn = mysql.connector.connect(host='192.168.22.9',database='abrec',user='fabrica',password='fabrica@2022')
        #self.conn = mysql.connector.connect(host='localhost',database='abrec',user='root',password='')	

        #self.conn = mysql.connector.connect(host='localhost',database='abrec',user='root',password='')	

        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            # print("Conectado ao Servidor de Banco de Dados: ", db_info)
        else:
            print("Erro")  

    def select_agendamentos(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT id_agendamento, DATE_FORMAT(data, '%d/%m/%Y') AS data, TIME_FORMAT(hora, "%H:%i") AS hora, nome, profissional, anotacao FROM agendamento WHERE profissional LIKE "Assistente Social" AND flag LIKE "NAO";
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
    
    def select_agendamentos_psi(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT id_agendamento, DATE_FORMAT(data, '%d/%m/%Y') AS data, TIME_FORMAT(hora, "%H:%i") AS hora, nome, profissional, anotacao FROM agendamento WHERE profissional LIKE "Psicóloga" AND flag LIKE "NAO";
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()


    def select_pessoa(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT id_matricula FROM pessoa ORDER BY id_matricula DESC LIMIT 1;
            """)
            result = self.cursor.fetchall()
            
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
    
    def select_pessoa_cpf(self, cpf):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT id_matricula, nome, telefone FROM pessoa WHERE cpf IN ({cpf});
            """)
            resultado1 = self.cursor.fetchall()
            id_matricu = resultado1[0][0]

            self.cursor.execute(f"""
                SELECT clinica.nome_fantasia FROM clinica 
                INNER JOIN usuario ON usuario.local_tratamento
                WHERE id_matricula IN ({id_matricu});
            """)
            resultado2 = self.cursor.fetchall()

            lista = []
            for i in resultado1:
                for n in i:
                    lista.append(n)
            for i in resultado2:
                for n in i:
                    lista.append(n)          
            return lista
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
    
    def select_colaborador(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT id_colaborador FROM colaborador ORDER BY id_colaborador DESC LIMIT 1;
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def validarLogin(self, login, senha):
        self.connect()
        try:
            #
            self.cursor.execute(f"""Select login, senha, perfil from colaborador where login = '{login}' and senha = '{senha}';""")
            result = self.cursor.fetchall() 

            self.cursor.execute(f"""Select id_matricula from colaborador where login = '{login}' and senha = '{senha}';""")
            result2 = self.cursor.fetchall()
            print("id resulte = ",result2) 

            return result, result2

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def cadastro_beneficios(self,beneficios):
        self.connect()
        try:
            args = (beneficios[0],beneficios[1],beneficios[2],beneficios[3],beneficios[4],beneficios[5],beneficios[6])
            self.cursor.execute('INSERT INTO beneficios(tipo, codigo, lote, unidade_medida, descricao, validade, quantidade) VALUES (%s,%s,%s,%s,%s,%s,%s)', args)
            id_beneficios = self.cursor.lastrowid

            self.conn.commit()
            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            #print(err)
            return "ERRO",str(err)
        
    def cadastro_retirada_beneficios(self,saida_beneficio):
        self.connect()
        try:
            args = (saida_beneficio[0],saida_beneficio[1],saida_beneficio[2],saida_beneficio[3],saida_beneficio[4])
            self.cursor.execute('INSERT INTO saida_beneficio (id_matricula,cpf, cod_beneficio, quantidade_retirada, data_retirada) VALUES (%s,%s, %s, %s, %s)', args)
            #id_saida_beneficio = self.cursor.lastrowid



            # args = (saida_beneficio[0], saida_beneficio[1], saida_beneficio[2], saida_beneficio[3], saida_beneficio[4], saida_beneficio[5], saida_beneficio[6])
            # self.cursor.execute('INSERT INTO saida_beneficio (id_saida_beneficio, cpf, DATE_FORMAT,(validade,"%d/%m/%Y") AS data_retirada, codigo_retirada, quantidade_retirada, id_usuario, id_beneficio) VALUES (%s, %s, %s, %s, %s, %s, %s)', args)              # Retrieve the ID of the last inserted row
            # id_saida_beneficio = self.cursor.lastrowid


            self.conn.commit()
            return "OK","Cadastro realizado com sucesso!!"


        except Exception as err:
            #print(err)
            return "ERRO",str(err)
        
    def select_usuario(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT id_usuario FROM usuario ORDER BY id_usuario DESC LIMIT 1;
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
            
    def relatorio_pessoa(self):
        self.connect()
        try:
            self.cursor.execute("""
                    SELECT pessoa.nome, pessoa.cpf, TIMESTAMPDIFF(YEAR, data_nascimento,NOW()) as idades, pessoa.sexo, pessoa.telefone, usuario.beneficio, usuario.cns,
                    usuario.nis, usuario.situacao_trabalho,usuario.situacao_trabalho_outros,clinica.nome_fantasia, endereco.bairro, 
                    endereco.cidade,pessoa.data_cadastro
                    FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                    INNER JOIN endereco ON endereco.id_endereco = pessoa.id_endereco
                    INNER JOIN clinica ON clinica.id_clinica = usuario.local_tratamento;
                    """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
            
    def relatorio_pessoa_nutri(self, id_relatorio_nutri):
        self.connect()
        try:
            self.cursor.execute(f"""
                Select consulta.data_consulta,pessoa.nome, pessoa.cpf, usuario.cns, usuario.nis, TIMESTAMPDIFF(YEAR, pessoa.data_nascimento,NOW()) as idade,pessoa.sexo,nutri_usuario.peso,nutri_usuario.imc,
                pessoa.telefone,usuario.situacao_trabalho,clinica.nome_fantasia as clinica, endereco.bairro,endereco.cidade
                FROM pessoa 
                INNER JOIN usuario
                ON pessoa.id_matricula = usuario.id_matricula
                INNER JOIN consulta
                ON usuario.id_matricula = consulta.id_matricula
                INNER JOIN nutri_usuario
                ON  usuario.id_matricula = nutri_usuario.id_matricula 
                INNER JOIN clinica
                ON usuario.local_tratamento = clinica.id_clinica
                INNER JOIN endereco
                ON pessoa.id_endereco = endereco.id_endereco WHERE consulta.id_colaborador = '{id_relatorio_nutri}';
                    """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
            
    def filter_data(self,texto_data_inicio,texto_data_final):
        self.connect()
        try:
            self.cursor.execute(f"""
                    SELECT pessoa.nome, pessoa.cpf,TIMESTAMPDIFF(YEAR, data_nascimento,NOW()) as idades, pessoa.sexo, pessoa.telefone, usuario.beneficio, usuario.cns,
                    usuario.nis, usuario.local_tratamento, usuario.situacao_trabalho,usuario.situacao_trabalho_outros,usuario.situacao,clinica.nome_fantasia, endereco.bairro, 
                    endereco.cidade,pessoa.data_cadastro
                    FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                    INNER JOIN endereco ON endereco.id_endereco = pessoa.id_endereco
                    LEFT JOIN clinica ON clinica.id_endereco = endereco.id_endereco WHERE data_cadastro BETWEEN '{texto_data_inicio}' and '{texto_data_final}';
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()


    def relatorio_cuidador(self):
        self.connect()
        try:
            self.cursor.execute("""
             SELECT pes.nome AS cuidador_nome,pes.cpf,TIMESTAMPDIFF( YEAR,pes.data_nascimento,NOW()),pes.sexo,pes.telefone,endereco.logradouro,endereco.bairro,endereco.cidade,parente.nome AS usuario_nome,cuidador.parentesco
                    FROM pessoa AS parente
                    INNER JOIN usuario ON parente.id_matricula = usuario.id_cuidador
                    INNER JOIN cuidador ON cuidador.id_cuidador = usuario.id_cuidador
                    INNER JOIN pessoa AS pes ON cuidador.id_matricula = pes.id_matricula
                    INNER JOIN endereco ON pes.id_endereco = endereco.id_endereco;
                """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def filtrar_relatorio_cuidador(self,texto):
        self.connect()
        try:
            self.cursor.execute(f"""
                     SELECT pes.nome AS cuidador_nome,pes.cpf,TIMESTAMPDIFF(YEAR,pes.data_nascimento,NOW()),pes.sexo,pes.telefone,endereco.logradouro,endereco.bairro,endereco.cidade,parente.nome AS usuario_nome,cuidador.parentesco
                    FROM pessoa AS parente
                    INNER JOIN usuario ON parente.id_matricula = usuario.id_cuidador
                    INNER JOIN cuidador ON cuidador.id_cuidador = usuario.id_cuidador
                    INNER JOIN pessoa AS pes ON cuidador.id_matricula = pes.id_matricula
                    INNER JOIN endereco ON pes.id_endereco = endereco.id_endereco
                    WHERE pes.nome LIKE "%{texto}%" OR pes.cpf LIKE "%{texto}%" OR pes.sexo LIKE "%{texto}%" OR pes.data_nascimento LIKE "%{texto}%" OR endereco.logradouro LIKE "%{texto}%" OR endereco.bairro LIKE "%{texto}%" OR pes.telefone LIKE "%{texto}%" OR cuidador.parentesco LIKE "%{texto}%" OR parente.nome LIKE "%{texto}%";
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def filter_data_relatorio_cuidador(self,texto_data_inicio,texto_data_final):
        self.connect()
        try:
            self.cursor.execute(f"""
                  SELECT pes.nome AS cuidador_nome,pes.cpf,TIMESTAMPDIFF(YEAR,pes.data_nascimento,NOW()),pes.sexo,pes.telefone,endereco.logradouro,endereco.bairro,endereco.cidade,parente.nome AS usuario_nome,cuidador.parentesco
                    FROM pessoa AS parente
                    INNER JOIN usuario ON parente.id_matricula = usuario.id_cuidador
                    INNER JOIN cuidador ON cuidador.id_cuidador = usuario.id_cuidador
                    INNER JOIN pessoa AS pes ON cuidador.id_matricula = pes.id_matricula
                    INNER JOIN endereco ON pes.id_endereco = endereco.id_endereco
                    wHERE pes.data_nascimento BETWEEN '{texto_data_inicio}' and '{texto_data_final}';
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

            
            
    def filter_data_participante_curso(self,texto_data_inicio,texto_data_final):
        self.connect()
        try:
            self.cursor.execute(f"""
                    SELECT pessoa.nome, pessoa.cpf, pessoa.telefone, pessoa.telefone_contato, curso_evento.nome_curso_evento, curso_evento.periodo, curso_evento.data_inicio, 
                    curso_evento.data_fim, curso_evento.tipo_curso, curso_evento.descricao
                    from pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                    INNER JOIN participantes ON participantes.id_matricula = pessoa.id_matricula
                    LEFT JOIN curso_evento ON curso_evento.id_curso_evento = participantes.id_evento
                    wHERE curso_evento.data_inicio BETWEEN '{texto_data_inicio}' and '{texto_data_final}';
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
    
    def filter_data_relatorio_psi(self,texto_data_inicio_psi,texto_data_final_psi):
        self.connect()
        try:
            self.cursor.execute(f"""
                    SELECT pessoa.nome, pessoa.cpf, usuario.cns, pessoa.sexo, pessoa.telefone, pessoa.telefone_contato, clinica.nome_fantasia, consulta.data_consulta, consulta.situacao, consulta.observacao
                    from pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                    INNER JOIN consulta ON consulta.id_matricula = pessoa.id_matricula
                    INNER JOIN clinica ON clinica.id_clinica = usuario.local_tratamento
                    WHERE consulta.data_consulta BETWEEN '{texto_data_inicio_psi}' and '{texto_data_final_psi}';
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
    
    def relatorio_beneficio(self):
        self.connect()
        try:
            self.cursor.execute("""
                        select pessoa.nome,pessoa.cpf, usuario.cns,pessoa.sexo, usuario.situacao_trabalho,usuario.beneficio,beneficios.tipo, beneficios.descricao,saida_beneficio.quantidade_retirada, saida_beneficio.data_retirada
                        from pessoa
                        inner join usuario on pessoa.id_matricula = usuario.id_matricula
                        inner join saida_beneficio on saida_beneficio.id_matricula = usuario.id_matricula
                        inner join beneficios on saida_beneficio.cod_beneficio = beneficios.codigo;
                    """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def filtrar_relatorio_beneficio(self,texto):
        self.connect()
        try:
            self.cursor.execute(f"""
                    select pessoa.nome,pessoa.cpf, usuario.cns,pessoa.sexo, usuario.situacao_trabalho,usuario.beneficio,beneficios.tipo, beneficios.descricao,saida_beneficio.quantidade_retirada, saida_beneficio.data_retirada
                    from pessoa
                    inner join usuario on pessoa.id_matricula = usuario.id_matricula
                    inner join saida_beneficio on saida_beneficio.id_matricula = usuario.id_matricula
                    inner join beneficios on saida_beneficio.cod_beneficio = beneficios.codigo
                    WHERE pessoa.nome LIKE "%{texto}%" OR pessoa.cpf LIKE "%{texto}%" OR usuario.cns LIKE "%{texto}%" OR pessoa.sexo LIKE "%{texto}%" OR usuario.situacao_trabalho LIKE "%{texto}%"
                    OR beneficios.tipo LIKE "%{texto}%" OR beneficios.descricao LIKE "%{texto}%" OR usuario.beneficio LIKE "%{texto}%" OR saida_beneficio.quantidade_retirada LIKE "%{texto}%" OR saida_beneficio.data_retirada LIKE "%{texto}%";
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def filter_data_relatorio_beneficio(self,texto_data):
        self.connect()
        print(texto_data)
        try:
            self.cursor.execute(f"""
                    select pessoa.nome,pessoa.cpf, usuario.cns,pessoa.sexo, usuario.situacao_trabalho,beneficios.tipo, beneficios.descricao,saida_beneficio.quantidade_retirada, saida_beneficio.data_retirada
                    from pessoa
                    inner join usuario on pessoa.id_matricula = usuario.id_matricula
                    inner join saida_beneficio on saida_beneficio.id_matricula = usuario.id_matricula
                    inner join beneficios on saida_beneficio.cod_beneficio = beneficios.codigo
                    WHERE saida_beneficio.data_retirada BETWEEN '{texto_data[0]}' and '{texto_data[1]}';
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
            
    def filtrar_relatorio(self,texto):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT pessoa.nome, pessoa.cpf,TIMESTAMPDIFF(YEAR, data_nascimento,NOW()) as idades, pessoa.sexo, pessoa.telefone, usuario.beneficio, usuario.cns,
                usuario.nis, usuario.situacao_trabalho,clinica.nome_fantasia, endereco.bairro, endereco.cidade
                FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                INNER JOIN endereco ON endereco.id_endereco = pessoa.id_endereco
                LEFT JOIN clinica ON clinica.id_clinica = usuario.local_tratamento 
                WHERE pessoa.nome LIKE "%{texto}%" OR pessoa.cpf LIKE "%{texto}%" OR clinica.nome_fantasia LIKE "%{texto}%" OR endereco.bairro LIKE "%{texto}%" OR endereco.cidade LIKE "%{texto}%"
                OR pessoa.sexo LIKE "%{texto}%" OR usuario.beneficio LIKE "%{texto}%";
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
        
    def filter_idade(self,texto_idade_inicio,texto_idade_final):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT pessoa.nome, pessoa.cpf, TIMESTAMPDIFF(YEAR, data_nascimento,NOW()) as idades, pessoa.sexo, pessoa.telefone, usuario.beneficio, usuario.cns,
                usuario.nis, usuario.situacao_trabalho,usuario.situacao_trabalho_outros,clinica.nome_fantasia, endereco.bairro, 
                endereco.cidade,pessoa.data_cadastro
                FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                INNER JOIN endereco ON endereco.id_endereco = pessoa.id_endereco
                LEFT JOIN clinica ON clinica.id_endereco = endereco.id_endereco WHERE TIMESTAMPDIFF(YEAR, data_nascimento,NOW()) BETWEEN '{texto_idade_inicio}' and '{texto_idade_final}';""")
            result = self.cursor.fetchall()
        
            return result
        
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
            
            
    def filter_usuario_area_sigilosa(self,id_area_sigilosa):
        self.connect()
        try: 
            self.cursor.execute(f"""select  area_sigilosa.id_area_sigilosa, area_sigilosa.data_cadastro, area_sigilosa.observacao_gerais from area_sigilosa
                                INNER JOIN pessoa ON pessoa.id_matricula = area_sigilosa.id_matricula and 
                                pessoa.id_matricula = '{id_area_sigilosa}';""")
            result = self.cursor.fetchall()
        
            return result
        
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
    def filter_agenda(self,text):
        self.connect()
        try: 
            self.cursor.execute(f"""select id_agendamento, data, hora, nome, profissional, anotacao from agendamento where nome like '%{text}%' or  profissional like '%{text}%';""")
            result = self.cursor.fetchall()
        
            return result
        
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
        
    
    def select_usuario_ids(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT id_usuario, id_matricula FROM usuario WHERE id_cuidador IS NULL ORDER BY id_usuario DESC LIMIT 10;
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
            
    def buscarIdColabAssis(self, nome_login):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT id_colaborador FROM colaborador INNER JOIN pessoa ON colaborador.id_matricula = pessoa.id_matricula WHERE colaborador.login LIKE '{nome_login}';
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
            
    def buscarIdColabPsic(self, nome_login):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT id_colaborador FROM colaborador INNER JOIN pessoa ON colaborador.id_matricula = pessoa.id_matricula WHERE colaborador.login LIKE '{nome_login}';
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def buscarIdColabNutri(self, nome_login):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT id_colaborador FROM colaborador INNER JOIN pessoa ON colaborador.id_matricula = pessoa.id_matricula WHERE colaborador.login LIKE '{nome_login}';
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def filter_data_relatorio_fisio(self,texto_data_inicio_fisio,texto_data_final_fisio):
        self.connect()
        try:
            self.cursor.execute(f"""
                    SELECT consulta.data_consulta, pessoa.nome, pessoa.cpf, usuario.cns, usuario.nis, TIMESTAMPDIFF(YEAR, pessoa.data_nascimento,NOW()) as idades, pessoa.sexo, pessoa.telefone, usuario.beneficio, clinica.razao_social as clinica, endereco.bairro, endereco.cidade
                    from pessoa 
                    INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                    INNER JOIN consulta on consulta.id_consulta = usuario.id_usuario
                    INNER JOIN endereco ON endereco.id_endereco = pessoa.id_endereco
                    INNER JOIN clinica ON clinica.id_clinica = usuario.local_tratamento
                    WHERE consulta.data_consulta BETWEEN '{texto_data_inicio_fisio}' and '{texto_data_final_fisio}';
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def filter_data_relatorio_nutri(self,texto_data_inicio_nutri,texto_data_final_nutri,id_relatorio_nutri):
        self.connect()
        try:
            self.cursor.execute(f"""
            select consulta.data_consulta,pessoa.nome, pessoa.cpf, usuario.cns, usuario.nis, TIMESTAMPDIFF(YEAR, pessoa.data_nascimento,NOW()) as idade,pessoa.sexo,nutri_usuario.peso,nutri_usuario.imc,
            pessoa.telefone,usuario.situacao_trabalho,clinica.nome_fantasia as clinica, endereco.bairro,endereco.cidade
            from pessoa 
            inner join usuario
            on pessoa.id_matricula = usuario.id_matricula
            inner join consulta
            on usuario.id_matricula = consulta.id_matricula
            inner join nutri_usuario
            on  usuario.id_matricula = nutri_usuario.id_matricula 
            inner join clinica
            on usuario.local_tratamento = clinica.id_clinica
            inner join endereco
            on pessoa.id_endereco = endereco.id_endereco where consulta.id_colaborador = '{id_relatorio_nutri}'
            AND consulta.data_consulta BETWEEN  '{texto_data_inicio_nutri}' and '{texto_data_final_nutri}';
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def buscar_relatorio_fisio(self,):
        self.connect()
        try:
            self.cursor.execute(f"""
                                SELECT consulta.data_consulta, pessoa.nome, pessoa.cpf, usuario.cns, usuario.nis, TIMESTAMPDIFF(YEAR, pessoa.data_nascimento,NOW()) as idades, pessoa.sexo, pessoa.telefone, usuario.beneficio, clinica.razao_social as clinica, endereco.bairro, endereco.cidade
                                from pessoa 
                                INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                                INNER JOIN consulta on consulta.id_consulta = usuario.id_usuario
                                INNER JOIN endereco ON endereco.id_endereco = pessoa.id_endereco
                                INNER JOIN clinica ON clinica.id_clinica = usuario.local_tratamento;
                                """)
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def buscar_relatorio_fisio_pesquisa(self,texto):
        self.connect()
        try:
            self.cursor.execute(f"""
                                SELECT consulta.data_consulta, pessoa.nome, pessoa.cpf, usuario.cns, usuario.nis, TIMESTAMPDIFF(YEAR, pessoa.data_nascimento,NOW()) as idades, pessoa.sexo, pessoa.telefone, usuario.beneficio, clinica.razao_social as clinica, endereco.bairro, endereco.cidade
                                from pessoa 
                                INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                                INNER JOIN consulta on consulta.id_consulta = usuario.id_usuario
                                INNER JOIN endereco ON endereco.id_endereco = pessoa.id_endereco
                                INNER JOIN clinica ON clinica.id_clinica = usuario.local_tratamento
                                WHERE pessoa.nome LIKE "%{texto}%" OR pessoa.cpf LIKE "%{texto}%" OR usuario.cns LIKE "%{texto}%" OR usuario.nis LIKE "%{texto}%" OR pessoa.data_nascimento LIKE "%{texto}%" OR pessoa.sexo LIKE "%{texto}%" OR pessoa.telefone LIKE "%{texto}%" OR usuario.beneficio LIKE "%{texto}%" OR usuario.situacao_trabalho LIKE "%{texto}%" OR clinica.razao_social LIKE "%{texto}%" OR endereco.bairro LIKE "%{texto}%" OR endereco.cidade LIKE "%{texto}%";
                                """)
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def buscar_relatorio_nutri_pesquisa(self,texto):
        self.connect()
        try:
            self.cursor.execute(f"""
                                select consulta.data_consulta,pessoa.nome, pessoa.cpf, usuario.cns, usuario.nis, TIMESTAMPDIFF(YEAR, pessoa.data_nascimento,NOW()) as idade,pessoa.sexo,nutri_usuario.peso,nutri_usuario.imc,
                                pessoa.telefone,usuario.situacao_trabalho,clinica.nome_fantasia as clinica, endereco.bairro,endereco.cidade
                                from pessoa 
                                inner join usuario
                                on pessoa.id_matricula = usuario.id_matricula
                                inner join consulta
                                on usuario.id_matricula = consulta.id_matricula
                                inner join nutri_usuario
                                on  usuario.id_matricula = nutri_usuario.id_matricula 
                                inner join clinica
                                on usuario.local_tratamento = clinica.id_clinica
                                inner join endereco
                                on pessoa.id_endereco = endereco.id_endereco
                                WHERE pessoa.nome LIKE "%{texto}%" OR pessoa.cpf LIKE "%{texto}%" OR usuario.cns LIKE "%{texto}%" OR usuario.nis LIKE "%{texto}%" OR pessoa.data_nascimento LIKE "%{texto}%" OR pessoa.sexo LIKE "%{texto}%" OR pessoa.telefone LIKE "%{texto}%" OR usuario.beneficio LIKE "%{texto}%" OR usuario.situacao_trabalho LIKE "%{texto}%" OR clinica.razao_social LIKE "%{texto}%" OR endereco.bairro LIKE "%{texto}%" OR endereco.cidade LIKE "%{texto}%";
                                """)
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def buscarIdColabFisio(self, nome_login):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT id_colaborador FROM colaborador INNER JOIN pessoa ON colaborador.id_matricula = pessoa.id_matricula WHERE colaborador.login LIKE '{nome_login}';
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def select_clinica_ids(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT id_clinica FROM clinica ORDER BY id_clinica;
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()


    def select_cursos_ids(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT id_curso_evento FROM curso_evento ORDER BY id_curso_evento;
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
    def select_cuidador(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT id_cuidador FROM cuidador ORDER BY id_cuidador DESC LIMIT 1;
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
    
    def select_nome_usuario(self,id_matricula):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT nome FROM pessoa WHERE id_matricula = {id_matricula};
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()


    def select_nome_Clinica(self,id_clinica):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT razao_social FROM clinica WHERE id_clinica = {id_clinica};
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()


    def select_nome_curso_evento(self,id_curso_evento):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT nome_curso_evento FROM curso_evento WHERE id_curso_evento = {id_curso_evento};
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()


    def select_nome_colab_login(self,login_colab):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT id_matricula FROM pessoa WHERE nome LIKE '{login_colab}';
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def buscarIdFotoColab(self,id_colab):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT idFoto_usuario FROM foto_usuario WHERE id_colaborador = {id_colab};
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()


    def tirar_foto_usuario(self, foto):
        self.connect()
        try:
            args = (foto[0], foto[1], foto[2])
            self.cursor.execute("""INSERT INTO foto_usuario (nome, caminho, id_usuario) VALUES (%s, %s, %s)""", args)
            self.conn.commit()
            return "Entrou banco"
        except Exception as err:
            return "ERRO",str(err)
        
        finally:
            self.close_connection()

    def tirar_foto_colaborador(self, foto):
        self.connect()
        try:
            args = (foto[0], foto[1], foto[2])
            self.cursor.execute("""INSERT INTO foto_usuario (nome, caminho, id_colaborador) VALUES (%s, %s, %s)""", args)
            self.conn.commit()
            return "Entrou banco"
        except Exception as err:
            return "ERRO",str(err)
        
        finally:
            self.close_connection()

    def alterar_foto_colaborador(self, foto):
        self.connect()
        try:
            id_foto = str(foto[0])
            print(id_foto)
            self.cursor.execute(f"""UPDATE foto_usuario SET nome = '{foto[1]}', caminho = '{foto[2]}' WHERE idfoto_usuario = {id_foto}""")
            self.conn.commit()
            return "Entrou banco"
        except Exception as err:
            return "ERRO",str(err)
        
        finally:
            self.close_connection()

    def alterar_foto_usuario(self, foto):
        self.connect()
        try:
            id_foto = str(foto[0])
            print(id_foto)
            self.cursor.execute(f"""UPDATE foto_usuario SET nome = '{foto[1]}', caminho = '{foto[2]}' WHERE idfoto_usuario = {id_foto}""")
            self.conn.commit()
            return "Entrou banco"
        except Exception as err:
            return "ERRO",str(err)
        
        finally:
            self.close_connection()

    def buscar_foto_colaborador(self, id_colaborador):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT caminho FROM foto_usuario WHERE id_colaborador = {id_colaborador};""")
            result = self.cursor.fetchall()
            return result[0]
        
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def buscar_foto_usuario(self, id_usuario):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT caminho FROM foto_usuario WHERE id_usuario ={id_usuario};""")
            result = self.cursor.fetchall()
            return result[0]
        
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
    def busca_cuidador(self, cpf):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT pessoa.id_matricula, nome, data_nascimento, cpf, rg, data_emissao, orgao_exp, sexo, 
                                    parentesco, observacao, telefone,  telefone_contato, cep, logradouro, numero, bairro, 
                                    cidade,estado, endereco.id_endereco, cuidador.id_matricula
                                    FROM pessoa INNER JOIN endereco ON pessoa.id_endereco = endereco.id_endereco 
                                    INNER JOIN cuidador ON pessoa.id_matricula = cuidador.id_matricula 
                                    WHERE cpf LIKE '{cpf}';""")
            result = self.cursor.fetchall()
            return result[0]
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    
    def busca_usuario(self, cpf):
        self.connect()
        try:
            
            self.cursor.execute(f"""
                SELECT pessoa.id_matricula, pessoa.nome, data_nascimento,status, cpf,
                rg, data_emissao, orgao_exp, nis, cns, sexo, pessoa.telefone, 
                pessoa.telefone_contato, cep, logradouro, numero, bairro, cidade, estado,
                estado_civil, escolaridade, pessoa_deficiencia, tipo_deficiencia, outras_deficiencias,
                media_renda_familiar, tipo_transporte, vale_transporte, situacao_trabalho, situacao_trabalho_outros,
                beneficio, tarifa_social, tipo_tratamento, clinica.id_clinica, patologia_base, outras_patologias, data_inicio, periodo,
                endereco.id_endereco, usuario.id_usuario, foto_usuario.caminho, foto_usuario.idfoto_usuario
                FROM pessoa INNER JOIN endereco ON pessoa.id_endereco = endereco.id_endereco 
                INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula 
                INNER JOIN foto_usuario ON usuario.id_usuario = foto_usuario.id_usuario
                INNER JOIN clinica ON clinica.id_clinica = usuario.local_tratamento WHERE cpf LIKE '%{cpf}%'; """)
            result = self.cursor.fetchall()
            return result[0]
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()


    def busca_colaborador(self, cpf):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT pessoa.id_matricula, pessoa.nome, pessoa.data_nascimento, pessoa.cpf, pessoa.rg, pessoa.status, pessoa.orgao_exp, pessoa.data_emissao,
                                    colaborador.pis, pessoa.sexo, pessoa.telefone, pessoa.email, endereco.cep, endereco.logradouro, endereco.numero, endereco.bairro, endereco.cidade, endereco.estado,
                                    pessoa.estado_civil, pessoa.escolaridade, colaborador.cargo, colaborador.periodo, colaborador.salario, colaborador.login, colaborador.senha, endereco.id_endereco, colaborador.id_colaborador,
                                    foto_usuario.caminho, foto_usuario.idfoto_usuario
                                    FROM pessoa INNER JOIN endereco ON pessoa.id_endereco = endereco.id_endereco  
                                    INNER JOIN colaborador ON colaborador.id_matricula = pessoa.id_matricula
                                    INNER JOIN foto_usuario ON colaborador.id_colaborador
                                    WHERE cpf LIKE '%{cpf}%';""")
            result = self.cursor.fetchall()
            return result[0]
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
    

    def busca_usuario_nutri_agendamento(self, cpf):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT pessoa.nome, pessoa.telefone, clinica.nome_fantasia, usuario.id_matricula
                                    FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                                    INNER JOIN clinica ON clinica.id_clinica = usuario.local_tratamento
                                    LEFT JOIN agendamento ON agendamento.id_matricula = usuario.id_matricula
                                    WHERE pessoa.cpf LIKE '%{cpf}%';""")
            result = self.cursor.fetchall()
            return result[0]
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
            
    def busca_usuario_nutri_consulta(self, cpf):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT pessoa.nome, pessoa.telefone, clinica.nome_fantasia, usuario.tipo_tratamento, usuario.patologia_base, 
                                    agendamento.data, agendamento.hora, usuario.id_matricula,agendamento.flag
                                    FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                                    INNER JOIN clinica ON clinica.id_clinica = usuario.local_tratamento
                                    LEFT JOIN agendamento ON agendamento.id_matricula = usuario.id_matricula
                                    WHERE pessoa.cpf LIKE '%{cpf}%';""")
            result = self.cursor.fetchall()
            return result[0]
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def busca_usuario_consulta_fisio_puxar(self, cpf):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT pessoa.nome, pessoa.telefone, clinica.nome_fantasia, agendamento.data, agendamento.hora, usuario.id_matricula, agendamento.flag
                                    FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                                    INNER JOIN clinica ON clinica.id_clinica = usuario.local_tratamento
                                    LEFT JOIN agendamento ON agendamento.id_matricula = usuario.id_matricula
                                    WHERE pessoa.cpf LIKE '%{cpf}%';""")
            result = self.cursor.fetchall()
            return result[0]
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()


    def busca_usuario_agendamento_fisio(self, cpf):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT pessoa.nome, pessoa.telefone, clinica.nome_fantasia, pessoa.id_matricula
                                    FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                                    LEFT JOIN clinica ON clinica.id_clinica = usuario.local_tratamento
                                    WHERE pessoa.cpf LIKE '%{cpf}%';""")
            result = self.cursor.fetchall()
            return result[0]
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def busca_usuario_fisio(self, cpf):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT pessoa.nome, pessoa.telefone, clinica.nome_fantasia, usuario.tipo_tratamento, usuario.patologia_base,
                                    agendamento.data, agendamento.hora, usuario.id_matricula
                                    FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                                    INNER JOIN clinica ON clinica.id_clinica = usuario.local_tratamento
                                    LEFT JOIN agendamento ON agendamento.id_matricula = usuario.id_matricula
                                    WHERE pessoa.cpf LIKE '%{cpf}%';""")
            result = self.cursor.fetchall()
            return result[0]
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def busca_nutri_agendamento_tabela(self):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT id_agendamento, DATE_FORMAT(data, '%d/%m/%Y') AS data, TIME_FORMAT(hora, "%H:%i") AS hora, nome, profissional, anotacao FROM agendamento WHERE profissional LIKE "Nutricionista" AND flag LIKE "NAO";""")
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:

            self.close_connection()
    def busca_fisio_agendamento_tabela(self):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT id_agendamento, DATE_FORMAT(data, '%d/%m/%Y') AS data, TIME_FORMAT(hora, "%H:%i") AS hora, nome, profissional, anotacao FROM agendamento WHERE profissional LIKE "Fisioterapeuta" AND flag LIKE "NAO";""")
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    

    def busca_nutri_consulta_tabela(self, cpf, id_colab_nutri):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT consulta.id_consulta, DATE_FORMAT(consulta.data_consulta, '%d/%m/%Y') AS data, TIMESTAMPDIFF(YEAR, data_nascimento,NOW()) as idades, consulta.situacao, consulta.observacao 
                                    FROM consulta INNER JOIN pessoa ON consulta.id_matricula = pessoa.id_matricula
                                    INNER JOIN agendamento ON agendamento.id_matricula = pessoa.id_matricula
                                    INNER JOIN nutri_usuario ON nutri_usuario.id_matricula = pessoa.id_matricula
                                    WHERE pessoa.cpf LIKE '{cpf}' AND consulta.id_colaborador LIKE '{id_colab_nutri}';""")
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
          
    def busca_psic_consulta_tabela(self, cpf, id_colab_psic):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT consulta.id_consulta, consulta.data_consulta, consulta.situacao, consulta.observacao
                                    FROM consulta INNER JOIN pessoa ON consulta.id_matricula = pessoa.id_matricula
                                    INNER JOIN agendamento ON agendamento.id_matricula = pessoa.id_matricula
                                    WHERE pessoa.cpf LIKE '{cpf}' AND consulta.id_colaborador LIKE '{id_colab_psic}';""")
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

            
            
            
    def busca_clinica_nome_fantasia(self):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT nome_fantasia FROM clinica;""")
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def buscar_consulta(self,cpf):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT usuario.id_matricula, pessoa.nome, pessoa.telefone, clinica.nome_fantasia, data, hora, agendamento.flag
                                    FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                                    LEFT JOIN clinica ON clinica.id_clinica = usuario.local_tratamento
                                    INNER JOIN agendamento ON agendamento.id_matricula = pessoa.id_matricula
                                    WHERE pessoa.cpf LIKE '%{cpf}%';""")
            result = self.cursor.fetchall()
            print(result)
            return result[0]
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def buscar_consulta_usuario_psi(self,cpf):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT pessoa.nome, pessoa.telefone, agendamento.clinica, agendamento.data, agendamento.hora, usuario.id_matricula, agendamento.flag
                                    FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                                    LEFT JOIN agendamento ON agendamento.id_matricula = usuario.id_matricula
                                    WHERE pessoa.cpf LIKE '%{cpf}%';""")
            result = self.cursor.fetchall()
            return result[0]
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def buscar_participante(self,cpf):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT pessoa.id_matricula, pessoa.nome, pessoa.telefone, pessoa.telefone_contato, clinica.nome_fantasia 
                                    FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                                    LEFT JOIN clinica ON clinica.id_clinica = usuario.local_tratamento WHERE pessoa.cpf LIKE '%{cpf}%';""")
            result = self.cursor.fetchall()
            return result[0]
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
    
    
    def cadastro_consulta(self,consulta):
        self.connect()
        try:
            args = (consulta[0],consulta[1],consulta[2],consulta[3],consulta[4],consulta[5])
            self.cursor.execute('INSERT INTO consulta(situacao,data_consulta,hora,observacao,id_matricula,id_colaborador) VALUES (%s,%s,%s,%s,%s,%s)', args)
            self.conn.commit()
            return "Cadastrado com Sucesso!!"

        except Exception as err:
            erro = str(err)
            print(erro)

        finally:
            self.close_connection()

    def busca_usuario_consulta_fisio(self,consulta):
        self.connect()
        print("PSIC CONSULTA DB PSICO",consulta)
        try:
            args = (consulta[0],consulta[1],consulta[2],consulta[3],consulta[4],consulta[5])
            self.cursor.execute('INSERT INTO consulta (situacao, data_consulta, hora, observacao, id_matricula) VALUES (%s,%s,%s,%s,%s)', args)
            self.conn.commit()
            return "Cadastrado com Sucesso!!"

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def cadastro_consulta_fisio(self,consulta):
        self.connect()
        print("PSIC CONSULTA DB FISIO",consulta)
        try:
            args = (consulta[0],consulta[1],consulta[2],consulta[3],consulta[4],consulta[5])
            self.cursor.execute('INSERT INTO consulta(situacao,data_consulta,hora,observacao,id_matricula,id_colaborador) VALUES (%s,%s,%s,%s,%s,%s)', args)
            self.conn.commit()
            return "Cadastrado com Sucesso!!"

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
            
    def cadastro_consulta_psi(self,consulta):
        self.connect()
        print("PSIC CONSULTA DB FISIO",consulta)
        try:
            args = (consulta[0],consulta[1],consulta[2],consulta[3],consulta[4],consulta[5])
            self.cursor.execute('INSERT INTO consulta(situacao,data_consulta,hora,observacao,id_matricula,id_colaborador) VALUES (%s,%s,%s,%s,%s,%s)', args)
            self.conn.commit()
            return "Cadastrado com Sucesso!!"

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()


    def buscar_consulta_fisio(self, cpf, id_colab_fisio):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT consulta.id_consulta, consulta.data_consulta, consulta.situacao, consulta.observacao
                                    FROM consulta INNER JOIN pessoa ON consulta.id_matricula = pessoa.id_matricula
                                    INNER JOIN agendamento ON agendamento.id_matricula = pessoa.id_matricula
                                    WHERE pessoa.cpf LIKE '{cpf}' AND consulta.id_colaborador LIKE '{id_colab_fisio}';""")
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
            
    def buscar_consulta_psic(self, cpf, id_colab_psi):
        self.connect()
        try:
            self.cursor.execute(f"""SELECT consulta.id_consulta, consulta.data_consulta, consulta.situacao, consulta.observacao
                                    FROM consulta INNER JOIN pessoa ON consulta.id_matricula = pessoa.id_matricula
                                    INNER JOIN agendamento ON agendamento.id_matricula = pessoa.id_matricula
                                    WHERE pessoa.cpf LIKE '{cpf}' AND consulta.id_colaborador LIKE '{id_colab_psi}' ;""")
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def cadastro_consulta_nutri(self,consulta):
        self.connect()
        print("Consulta NUTRI ->", consulta)
        try:
            args = (consulta[0],consulta[1],consulta[2],consulta[3],consulta[4],consulta[5])
            self.cursor.execute('INSERT INTO consulta(situacao,data_consulta,hora,observacao,id_matricula,id_colaborador) VALUES (%s,%s,%s,%s,%s,%s)', args)
            self.conn.commit()
            return "Cadastrado com Sucesso!!"

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def buscar_info_consulta(self,cpf,id_colab_ass):
        self.connect()
        
        print("database ->",cpf)
        print("database ->",id_colab_ass)
        try:
            self.cursor.execute(f"""
                                    SELECT consulta.id_consulta, consulta.data_consulta, consulta.situacao, consulta.observacao, agendamento.flag
                                    FROM consulta INNER JOIN pessoa ON consulta.id_matricula = pessoa.id_matricula
                                    INNER JOIN agendamento ON agendamento.id_matricula = pessoa.id_matricula
                                    WHERE pessoa.cpf LIKE '{cpf}' AND consulta.id_colaborador LIKE '{id_colab_ass}' ;
                                """)
            result = self.cursor.fetchall()
            print(result)
            return result

        except Exception as err:
            erro = str(err)
            print(erro)

        finally:
            self.close_connection()


    def buscar_participantes_curso(self,):
        self.connect()
        try:
            self.cursor.execute(f"""
                                SELECT pessoa.nome, pessoa.cpf, pessoa.telefone, pessoa.telefone_contato, curso_evento.nome_curso_evento, curso_evento.periodo, curso_evento.data_inicio, 
                                curso_evento.data_fim, curso_evento.tipo_curso, curso_evento.descricao
                                from pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                                INNER JOIN participantes ON participantes.id_matricula = pessoa.id_matricula
                                LEFT JOIN curso_evento ON curso_evento.id_curso_evento = participantes.id_evento;
                                """)
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
    
    def buscar_relatorio_psi(self,):
        self.connect()
        try:
            self.cursor.execute(f"""
                                SELECT pessoa.nome, pessoa.cpf, usuario.cns, pessoa.sexo, pessoa.telefone, pessoa.telefone_contato, clinica.nome_fantasia, consulta.data_consulta, consulta.situacao, consulta.observacao
                                from pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                                INNER JOIN consulta ON consulta.id_matricula = pessoa.id_matricula
                                INNER JOIN clinica ON clinica.id_clinica = usuario.local_tratamento
                                """)
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
            
    def buscar_participantes_curso_pesquisa(self,texto):
        self.connect()
        try:
            self.cursor.execute(f"""
                                SELECT pessoa.nome, pessoa.cpf, pessoa.telefone, pessoa.telefone_contato, curso_evento.nome_curso_evento, curso_evento.periodo, curso_evento.data_inicio, 
                                curso_evento.data_fim, curso_evento.tipo_curso, curso_evento.descricao
                                from pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                                INNER JOIN participantes ON participantes.id_matricula = pessoa.id_matricula
                                LEFT JOIN curso_evento ON curso_evento.id_curso_evento = participantes.id_evento
                                WHERE pessoa.nome LIKE "%{texto}%" OR pessoa.cpf LIKE "%{texto}%" OR curso_evento.nome_curso_evento LIKE "%{texto}%" OR curso_evento.periodo LIKE "%{texto}%";
                                """)
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
            
    def buscar_relatorio_psi_pesquisa(self,texto):
        self.connect()
        try:
            self.cursor.execute(f"""
                                SELECT pessoa.nome, pessoa.cpf, usuario.cns, pessoa.sexo, pessoa.telefone, pessoa.telefone_contato, clinica.nome_fantasia, consulta.data_consulta, consulta.situacao, consulta.observacao
                                from pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                                INNER JOIN consulta ON consulta.id_matricula = pessoa.id_matricula
                                INNER JOIN clinica ON clinica.id_clinica = usuario.local_tratamento
                                WHERE pessoa.nome LIKE "%{texto}%" OR pessoa.cpf LIKE "%{texto}%" OR pessoa.sexo LIKE "%{texto}%" OR clinica.nome_fantasia LIKE "%{texto}%" OR consulta.data_consulta LIKE "%{texto}%" OR consulta.situacao LIKE "%{texto}%";
                                """)
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
    

    def buscar_info_participante(self,cpf):
        self.connect()
        try:
            self.cursor.execute(f"""
                                SELECT pessoa.nome, pessoa.cpf, pessoa.telefone, clinica.nome_fantasia, curso_evento.nome_curso_evento
                                FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                                RIGHT JOIN participantes ON participantes.id_matricula = pessoa.id_matricula
                                INNER JOIN curso_evento ON curso_evento.id_curso_evento = participantes.id_evento
                                LEFT JOIN clinica ON clinica.id_clinica = usuario.local_tratamento WHERE pessoa.cpf LIKE '%{cpf}%';
                                """)
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def cadastrar_participante(self,participante):
        self.connect()
        try:
            args = (participante[0], participante[1])
            self.cursor.execute("INSERT INTO participantes (id_evento,id_matricula) VALUES (%s,%s)", args)
            self.conn.commit()

            return "Cadastro feito com Sucesso!!"

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def alterar_usuario_consulta_psi(self, campo):
        self.connect()
        try:
            self.cursor.execute(f""" UPDATE consulta SET
                                     data = '{campo[1]}',
                                     observacao = '{campo[3]}'
                                     WHERE id_consulta = '{campo[0]}';
            """)
            self.conn.commit()
            return "Alteração feita com Sucesso!!!"

        except Exception as err:
            return "ERRO",str(err)
        finally:
            self.conn.close()
            return ("Conexão encerrada com Sucesso!!!")
        
    def alterarAreaSigilosa(self, campo):
        self.connect()
        try:
            self.cursor.execute(f""" UPDATE area_sigilosa SET
                                     observacao_gerais = '{campo[2]}'
                                     WHERE id_area_sigilosa = '{campo[0]}';
            """)
            self.conn.commit()
            return "Alteração feita com Sucesso!!!"

        except Exception as err:
            return "ERRO",str(err)
        finally:
            self.conn.close()
            return ("Conexão encerrada com Sucesso!!!")
    
    def deletar_consulta_relatorio_psi(self,id_consulta):
        self.connect()
        try:
            self.cursor.execute(
                f"""DELETE FROM consulta WHERE id_consulta = '{id_consulta}' """
            )
            self.conn.commit()
            return "OK","Cadastro excluído com sucesso!"

        except Exception as err:
            return "ERRO",str(err)

    def alterar_usuario_consulta_as(self, campo):
        self.connect()
        try:
            self.cursor.execute(f""" UPDATE consulta SET
                                     data_consulta = '{campo[1]}',
                                     observacao = '{campo[3]}'
                                     WHERE id_consulta = '{campo[0]}';
            """)
            self.conn.commit()
            return "Alteração feita com Sucesso!!!"

        except Exception as err:
            return "ERRO",str(err)
        finally:
            self.conn.close()
            return ("Conexão encerrada com Sucesso!!!")
    
    def deletar_consulta_relatorio(self,id_consulta):
        self.connect()
        try:
            self.cursor.execute(
                f"""DELETE FROM consulta WHERE id_consulta = '{id_consulta}' """
            )
            self.conn.commit()
            return "OK","Cadastro excluído com sucesso!"

        except Exception as err:
            return "ERRO",str(err)


    def atualizar_cuidador (self,cuidador,pessoa,endereco):
        id_matricula_cuidador = str(cuidador[2])
        id_endereco_cuidador = str(endereco[0])
        self.connect()
        try:
            self.cursor.execute(f""" UPDATE cuidador SET parentesco = '{cuidador[0]}', observacao = '{cuidador[1]}' WHERE id_matricula = '{id_matricula_cuidador}';""")
            self.conn.commit()

            self.cursor.execute(f"""UPDATE pessoa SET nome = '{pessoa[1]}', data_nascimento = '{pessoa[2]}', cpf = '{pessoa[3]}', rg = '{pessoa[4]}', data_emissao = '{pessoa[5]}',
                                orgao_exp = '{pessoa[6]}', sexo = '{pessoa[7]}', telefone = '{pessoa[8]}', telefone_contato = '{pessoa[9]}' WHERE id_matricula = {pessoa[0]};  """)
            id_matricula = self.cursor.lastrowid
            self.conn.commit()

            self.cursor.execute(f"""UPDATE endereco  SET cep = '{endereco[1]}', logradouro = '{endereco[2]}',
                                numero = '{endereco[3]}', bairro = '{endereco[4]}', cidade = '{endereco[5]}',
                                estado = '{endereco[6]}' WHERE id_endereco = '{id_endereco_cuidador}';""")
            self.conn.commit()
            


            return "OK","Cuidador atualizado com sucesso!!"
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def atualizar_usuario(self,endereco,pessoa,usuario):
        id_endereco_usuario = str(endereco[0])
        id_matricula_usuario = str(usuario[16])
        id_matricula_pessoa = str(pessoa[0])
        print("TUPLA PES: ", pessoa)
        print("TUPLA USER: ", usuario)

        self.connect()
        try:              


            self.cursor.execute(f"""UPDATE endereco  SET cep = '{endereco[1]}', logradouro = '{endereco[2]}',
                                numero = '{endereco[3]}', bairro = '{endereco[4]}', cidade = '{endereco[5]}',
                                estado = '{endereco[6]}' WHERE id_endereco = '{id_endereco_usuario}';""")
            self.conn.commit()
            
            

            self.cursor.execute(f"""UPDATE pessoa SET nome = '{pessoa[1]}', data_nascimento = '{pessoa[2]}', cpf = '{pessoa[3]}',rg = '{pessoa[4]}', data_emissao = '{pessoa[5]}',
                                 orgao_exp = '{pessoa[6]}', sexo = '{pessoa[7]}', status = '{pessoa[8]}', telefone = '{pessoa[9]}', 
                                 telefone_contato = '{pessoa[10]}', escolaridade = '{pessoa[11]}', estado_civil = '{pessoa[12]}',
                                 pessoa_deficiencia = '{pessoa[13]}', tipo_deficiencia = '{pessoa[14]}', outras_deficiencias = '{pessoa[15]}' WHERE id_matricula = '{id_matricula_usuario}';  """)
            self.conn.commit()
            

            self.cursor.execute(f"""UPDATE usuario SET nis = '{usuario[0]}', cns = '{usuario[1]}', observacao = '{usuario[2]}', situacao_trabalho = '{usuario[3]}', situacao_trabalho_outros = '{usuario[4]}',
                                tipo_transporte = '{usuario[5]}', tipo_tratamento = '{usuario[6]}', beneficio = '{usuario[7]}', local_tratamento = '{usuario[8]}',
                                 periodo = '{usuario[9]}', data_inicio = '{usuario[10]}', patologia_base = '{usuario[11]}', outras_patologias = '{usuario[12]}', tarifa_social = '{usuario[13]}', media_renda_familiar = '{usuario[14]}',
                                 vale_transporte = '{usuario[15]}'  WHERE id_matricula = '{id_matricula_pessoa}';  """)
            self.conn.commit()

            return "OK","Usuario atualizado com sucesso!!"
        except Exception as err:
            erro = str(err)
            print(erro)
            #return "ERRO",str(err)

        finally:
            self.close_connection()


    def atualizar_colaborador(self,colaborador,pessoa,endereco):     
        id_matricula_pessoa = int(pessoa[0])
        id_endereco_colaborador = int(endereco[0])
        tipo_endereco = type(id_endereco_colaborador)
        tipo_pessoa = type(id_matricula_pessoa)
        self.connect()
        try: 
            self.cursor.execute(f"""UPDATE endereco  SET cep = '{endereco[1]}', logradouro = '{endereco[2]}',
                                numero = '{endereco[3]}', bairro = '{endereco[4]}', cidade = '{endereco[5]}',
                                estado = '{endereco[6]}' WHERE id_endereco = '{id_endereco_colaborador}';""")
            self.conn.commit()


            self.cursor.execute(f"""UPDATE pessoa SET nome = '{pessoa[1]}', data_nascimento = '{pessoa[2]}', cpf = '{pessoa[3]}', rg = '{pessoa[4]}',
                                data_emissao = '{pessoa[5]}', orgao_exp = '{pessoa[6]}', sexo ='{pessoa[7]}', status = '{pessoa[8]}', telefone = '{pessoa[9]}',
                                email = '{pessoa[10]}' WHERE id_matricula = '{id_matricula_pessoa}'; """)
            self.conn.commit()
            
            self.cursor.execute(f"""UPDATE colaborador SET pis = '{colaborador[0]}', data_admissao = '{colaborador[1]}', salario = '{colaborador[2]}', cargo = '{colaborador[3]}',
                                periodo = '{colaborador[4]}', login = '{colaborador[5]}', senha = '{colaborador[6]}' WHERE id_matricula = '{id_matricula_pessoa}';""")
            self.conn.commit()

            return "OK","Colaborador atualizado com sucesso!!"
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()





    def cadastro_usuario(self,endereco,pessoa,usuario):
        self.connect()
        try:
            args = (endereco[0],endereco[1],endereco[2],endereco[3],endereco[4],endereco[5])
            self.cursor.execute('INSERT INTO endereco(cep,logradouro,numero,bairro,cidade,estado) VALUES (%s,%s,%s,%s,%s,%s)', args)
            id_endereco = self.cursor.lastrowid
            self.conn.commit()

            print(endereco)
            print(id_endereco)
            print(pessoa)

            # self.cursor.execute("""
            #     INSERT INTO cuidador (parentesco,observacao,id_matricula) VALUES (%s,%s,%s)
            # """,(cuidador[0],cuidador[1],cuidador[2]))

            # id_cuidador = self.cursor.lastrowid
            # print(id_cuidador)
            # print(len(usuario))
            # print(len(pessoa))

            self.cursor.execute('INSERT INTO pessoa(nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status,telefone,telefone_contato,escolaridade,estado_civil,pessoa_deficiencia,tipo_deficiencia,outras_deficiencias,id_endereco) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],pessoa[5],pessoa[6],pessoa[7],pessoa[8],pessoa[9],pessoa[10],pessoa[11],pessoa[12],pessoa[13],pessoa[14],id_endereco))
            id_matricula = self.cursor.lastrowid
            self.conn.commit()

            self.cursor.execute("""
                INSERT INTO usuario (nis,cns,observacao,situacao_trabalho,situacao_trabalho_outros,tipo_transporte,tipo_tratamento,beneficio,local_tratamento,periodo,data_inicio,patologia_base,outras_patologias,tarifa_social,media_renda_familiar,vale_transporte,id_matricula) 
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,(usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5],usuario[6],usuario[7],usuario[8],usuario[9],usuario[10],usuario[11],usuario[12],usuario[13],usuario[14],usuario[15],id_matricula))

            self.conn.commit()

            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def cadastro_cuidador(self,endereco,pessoa,cuidador,usuario):
        self.connect()
        try:
            args = (endereco[0],endereco[1],endereco[2],endereco[3],endereco[4],endereco[5])
            self.cursor.execute('INSERT INTO endereco(cep,logradouro,numero,bairro,cidade,estado) VALUES (%s,%s,%s,%s,%s,%s)', args)
            id_endereco = self.cursor.lastrowid
            self.conn.commit()


            args2 = (pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],pessoa[5],pessoa[6],pessoa[7],pessoa[8],id_endereco)
            self.cursor.execute('INSERT INTO pessoa(nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,telefone,telefone_contato,id_endereco) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', args2)
            id_matricula = self.cursor.lastrowid
            self.conn.commit()


            self.cursor.execute("""
                INSERT INTO cuidador (parentesco,observacao,id_matricula) VALUES (%s,%s,%s)
            """,(cuidador[0],cuidador[1],id_matricula))
            id_matricula_cuidador = self.cursor.lastrowid
            self.conn.commit()

            self.cursor.execute(f'UPDATE usuario SET id_cuidador = {id_matricula_cuidador} WHERE id_usuario = {usuario}')
            self.conn.commit()

            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            return "ERRO",str(err)
        
 



    

        
    def cadastro_colaborador(self,endereco,pessoa,colaborador):
        self.connect()
        try:
            args = (endereco[0],endereco[1],endereco[2],endereco[3],endereco[4],endereco[5])
            self.cursor.execute('INSERT INTO endereco(cep, logradouro, numero, bairro, cidade, estado) VALUES (%s,%s,%s,%s,%s,%s)', args)
        
            id_endereco = self.cursor.lastrowid

            args2 = (pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],pessoa[5],pessoa[6],pessoa[7],pessoa[8],pessoa[9],pessoa[10],pessoa[11],id_endereco)
            self.cursor.execute('INSERT INTO pessoa(nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status,telefone,email,escolaridade,estado_civil,id_endereco) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', args2)
            id_matricula = self.cursor.lastrowid

            args3 = (colaborador[0],colaborador[1],colaborador[2],colaborador[3],colaborador[4],colaborador[5],colaborador[6],colaborador[7],id_matricula)
            self.cursor.execute("INSERT INTO colaborador (pis,data_admissao,salario,cargo,periodo,login,senha,perfil,id_matricula) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", args3)
            id_colaborador = self.cursor.lastrowid
            self.conn.commit()
            
            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            return "ERRO",str(err)
        
    def cadastro_fornecedor(self,endereco,fornecedor):
        self.connect()
        try:
            args = (endereco[0],endereco[1],endereco[2],endereco[3],endereco[4],endereco[5])
            self.cursor.execute('INSERT INTO endereco(cep, logradouro, numero, bairro, cidade, estado) VALUES (%s,%s,%s,%s,%s,%s)', args)
            print(args)
            id_endereco = self.cursor.lastrowid
            #print('ID do endereco',id_endereco)
            #print('Chegou o id')
            
            args2 = (fornecedor[0],fornecedor[1],fornecedor[2],fornecedor[3],fornecedor[4],fornecedor[5],fornecedor[6],fornecedor[7],fornecedor[8],fornecedor[9],id_endereco)
            self.cursor.execute('INSERT INTO fornecedor(razao_social,nome_fantasia,cnpj,telefone_celular,telefone_fixo,email,contato,inscricao_municipal,inscricao_estadual,observacao,id_endereco) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', args2)
            self.conn.commit()
            id_fornecedor = self.cursor.lastrowid
            #print('ID do fornecedor', id_fornecedor)

             
            return "OK","Cadastro Fornecedor realizado com sucesso!! "

        except Exception as err:
            #print(err)
            return "ERRO",str(err)

    def cadastro_curso(self,tupla_curso):
        self.connect()
        try: 
            
            args2 = (tupla_curso[0],tupla_curso[1],tupla_curso[2],tupla_curso[3],tupla_curso[4],tupla_curso[5],tupla_curso[6],tupla_curso[7],tupla_curso[8],tupla_curso[9],tupla_curso[10],tupla_curso[11],tupla_curso[12],tupla_curso[13],tupla_curso[14],tupla_curso[15],tupla_curso[16])
            
            self.cursor.execute('INSERT INTO curso_evento (nome_curso_evento, tipo_curso, data_inicio, data_fim, periodo, responsavel, horario_inicial, horario_final, vagas, segunda_feira, terca_feira, quarta_feira, quinta_feira, sexta_feira, sabado, situacao,descricao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)', args2)

            
                                                                                                                                                 
            self.conn.commit()
            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            return "ERRO",str(err)
    
    def cadastro_agendamento(self, agendamento):
        self.connect()
        print("args ->",agendamento)
        try:
            args = (agendamento[0],  agendamento[1], agendamento[2], agendamento[3], agendamento[4], agendamento[5], agendamento[6], agendamento[7], agendamento[8], agendamento[9])
            self.cursor.execute("INSERT INTO agendamento(id_matricula, cpf, nome, telefone, clinica, profissional, data, hora, anotacao, flag) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", args)
    
            self.conn.commit()
            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            erro = str(err)
            print(erro)

    def alterar_agendamento(self, campo):
        self.connect()
        
        try:
            self.cursor.execute(f""" UPDATE agendamento SET
                                     data = '{campo[1]}',
                                     hora = '{campo[2]}',
                                     anotacao = '{campo[5]}'
                                     WHERE id_agendamento = '{campo[0]}';
            """)
            
            self.conn.commit()
            return "Alteração feita com Sucesso!!!"
        except Exception as err:
            return "ERRO",str(err)
        finally:
            self.conn.close()
            return ("Conexão encerrada com Sucesso!!!")
        

    def cadastro_agendamento_psi(self, agendamento):
        self.connect()
        try:
            args = (agendamento[0],  agendamento[1],agendamento[2], agendamento[3], agendamento[4], agendamento[5], agendamento[6], agendamento[7], agendamento[8], agendamento[9])
            self.cursor.execute('INSERT INTO agendamento(id_matricula, cpf, nome, telefone, clinica, profissional, data, hora, anotacao, flag) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', args)
    
            self.conn.commit()
            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            erro = str(err)
            print(erro)
        
    def cadastro_agendamento_fisio(self, agendamento):
        self.connect()
        try:
            args = (agendamento[0],  agendamento[1],agendamento[2], agendamento[3], agendamento[4], agendamento[5], agendamento[6], agendamento[7], agendamento[8], agendamento[9])
            self.cursor.execute('INSERT INTO agendamento(id_matricula, cpf, nome, telefone, clinica, profissional, data, hora, anotacao, flag) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', args)
    
            self.conn.commit()
            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            return "ERRO",str(err)
        
    def cadastro_agendamento_nutri(self, agendamento):
        self.connect()
        print("AGENDAMENTO NUTRI BANCO ->", agendamento)
        try:
            args = (agendamento[0],  agendamento[1],agendamento[2], agendamento[3], agendamento[4], agendamento[5], agendamento[6], agendamento[7], agendamento[8], agendamento[9])
            self.cursor.execute('INSERT INTO agendamento(id_matricula, cpf, nome, telefone, clinica, profissional, data, hora, anotacao, flag) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', args)
    
            self.conn.commit()
            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            erro = str(err)
            print(erro)

    def cadastroIMC(self, imc):
        self.connect()
        print(imc)
        try:
            args = (imc[0], imc[1], imc[2], imc[3], imc[4], imc[5], imc[6], imc[7])
            self.cursor.execute('INSERT INTO nutri_usuario(peso, altura, imc, atendimento, data, hora, evolucao, id_matricula) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);', args)
    
            self.conn.commit()
            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            return "ERRO",str(err)

    def alterar_agendamento_psi(self, campo):
        self.connect()
        
        try:
            self.cursor.execute(f""" UPDATE agendamento SET
                                     data = '{campo[1]}',
                                     hora = '{campo[2]}',
                                     anotacao = '{campo[5]}'
                                     WHERE id_agendamento = '{campo[0]}';
            """)
            
            self.conn.commit()
            return "Alteração feita com Sucesso!!!"
        except Exception as err:
            return "ERRO",str(err)
        finally:
            self.conn.close()
            return ("Conexão encerrada com Sucesso!!!")    
        
    def buscar_id_matricula_area_sigilosa(self,id_matricula):
        self.conn()
        try:
            self.cursor.execute(f"""SELECT id_matricula from usuario WHERE ususario.id_matricula = ;""")

            return(f"Puxei o id {id_matricula}")
        except Exception as err:
            return "ERRO",str(err)
        finally:
            self.close_connection()




    def cadastrar_area_sigilosa (self,area_sigilosa):
        self.connect()
        try:
            args = (area_sigilosa[0],area_sigilosa[1],area_sigilosa[2])
            self.cursor.execute('INSERT INTO area_sigilosa(obito_paciente, observacao_gerais,id_matricula) VALUES (%s,%s,%s)', args)
            self.conn.commit()

            return("OK","Cadastro area sigilosa com sucesso!!!")

        except Exception as err:
            return "ERRO",str(err)
        finally:
            self.close_connection()
        
    def update(self,tupla_de_dados):
        self.connect()
        try:
                self.cursor.execute(f"""UPDATE cadastro SET 
                cnpj = '{tupla_de_dados[1]}',
                nome = '{tupla_de_dados[2]}',
                fone = '{tupla_de_dados[3]}',
                email = '{tupla_de_dados[4]}',
                endereco = '{tupla_de_dados[5]}',
                cidade = '{tupla_de_dados[6]}'
                WHERE id={tupla_de_dados[0]}
                """)
                self.conn.commit()
                #quando o dado for string deve ter '{var}' se for inteiro somente {id}
                return 'OK','Dados atualizados com sucesso!!!'

        except AttributeError as err:
            return "ERRO",str(err)
        finally:
            self.close_connection()
    
    def alterar_cadastro_beneficios(self, dados):
        self.connect()
        try:
            self.cursor.execute(f""" UPDATE beneficios SET
                                    tipo = '{dados[1]}',
                                    codigo = '{dados[2]}',
                                    lote = '{dados[3]}',
                                    unidade_medida = '{dados[4]}',
                                    descricao = '{dados[5]}',
                                    validade = '{dados[6]}',
                                    quantidade = '{dados[7]}'

                                    WHERE id_beneficios = '{dados[0]}';
            """)
            self.conn.commit()
            return "OK", "Beneficio atualizado com sucesso!!"
        except Exception as err:
            print(err)
            return "ERRO", str(err)
        finally:
            self.close_connection()

    def deletar_cadastro_beneficios(self,id_beneficios):
        self.connect()
        try:
            self.cursor.execute(
                f"""DELETE FROM beneficios WHERE id_beneficios = '{id_beneficios}' """
            )
            self.conn.commit()
            return "OK","Cadastro excluído com sucesso!"

        except Exception as err:
            print(err)

    def busca_beneficios(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT id_beneficios,tipo,codigo,lote,unidade_medida,descricao,validade,quantidade FROM beneficios;
            """)

            result = self.cursor.fetchall()

            return result
        except Exception as err:
            print(err)
        finally:
            self.close_connection()

    def busca_beneficios_relatorio_farmaceutica(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT pessoa.nome, pessoa.cpf, usuario.cns, pessoa.sexo, usuario.situacao_trabalho, usuario.beneficio, 
                beneficios.tipo, beneficios.descricao, saida_beneficio.quantidade_retirada, saida_beneficio.data_retirada
                FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                INNER JOIN saida_beneficio ON saida_beneficio.id_matricula = pessoa.id_matricula
                INNER JOIN beneficios ON beneficios.codigo = saida_beneficio.cod_beneficio AND beneficios.tipo = "medicação";
            """)

            result = self.cursor.fetchall()

            return result
        except Exception as err:
            print(err)
        finally:
            self.close_connection()
            
    def busca_beneficios_relatorio_farmaceutica_filtro_data(self, data_inicial, data_final):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT pessoa.nome, pessoa.cpf, usuario.cns, pessoa.sexo, usuario.situacao_trabalho, usuario.beneficio, 
                beneficios.descricao, saida_beneficio.quantidade_retirada, saida_beneficio.data_retirada
                FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                INNER JOIN saida_beneficio ON saida_beneficio.id_matricula = pessoa.id_matricula
                INNER JOIN beneficios ON beneficios.codigo = saida_beneficio.cod_beneficio WHERE saida_beneficio.data_retirada BETWEEN '{data_inicial}' AND '{data_final}'  ;
            """)

            result = self.cursor.fetchall()

            return result
        except Exception as err:
            print(err)
        finally:
            self.close_connection()

    def busca_beneficios_relatorio_farmaceutica_filtro(self, txt):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT pessoa.nome, pessoa.cpf, usuario.cns, pessoa.sexo, usuario.situacao_trabalho, usuario.beneficio, beneficios.tipo,
                beneficios.descricao, saida_beneficio.quantidade_retirada, saida_beneficio.data_retirada
                FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                INNER JOIN saida_beneficio ON saida_beneficio.id_matricula = pessoa.id_matricula
                INNER JOIN beneficios ON beneficios.codigo = saida_beneficio.cod_beneficio WHERE pessoa.cpf LIKE "%{txt}%" OR pessoa.sexo LIKE "%{txt}%" OR usuario.situacao_trabalho LIKE "%{txt}%" OR beneficios.descricao LIKE "%{txt}%" AND beneficios.tipo = "medicação";
            """)

            result = self.cursor.fetchall()
            return result
        except Exception as err:
            print(err)
        finally:
            self.close_connection()


    def select_retirada_beneficio_cpf(self, cpf):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT
                    pessoa.id_matricula, 
                    pessoa.nome ,
                    TIMESTAMPDIFF(YEAR, pessoa.data_nascimento, NOW()) as idade, 
                    pessoa.telefone ,
                    usuario.cns ,
                    usuario.id_matricula ,
                    clinica.razao_social 
                    FROM pessoa
            INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
            LEFT JOIN clinica ON clinica.id_clinica = usuario.local_tratamento
            WHERE pessoa.cpf LIKE '{cpf}';
            """)
            #clinica.nome_fantasia razao_social
            resultado1 = self.cursor.fetchall()

            if resultado1:
                return {

                    'id_matricula': resultado1[0][0],
                    'nome': resultado1[0][1],
                    'idade': resultado1[0][2],
                    'telefone': resultado1[0][3],
                    'cns': resultado1[0][4],
                    'clinica': resultado1[0][6]
                }
            else:
                return None
        except Exception as e:
            print(f"Error in select_retirada_beneficio_cpf: {e}")
            return None

    def select_retirada_beneficio_codigo(self, codigo):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT
                    codigo,
                    descricao
                FROM beneficios
                WHERE codigo LIKE '{codigo}';
            """)
            
            resultado1 = self.cursor.fetchall()

            if resultado1:
                return {
                    'id_beneficios': resultado1[0][0],
                    'descricao': resultado1[0][1]
                }
            else:
                return None
        except Exception as e:
            print(f"Erro na função select_retirada_beneficio_codigo: {e}")
            return None




    def cadastro_clinica(self,endereco,clinica):
        self.connect()
        try:
            args = (endereco[0],endereco[1],endereco[2],endereco[3],endereco[4],endereco[5])
            self.cursor.execute('INSERT INTO endereco(cep, logradouro, numero, bairro, cidade, estado) VALUES (%s,%s,%s,%s,%s,%s)', args)
            id_endereco = self.cursor.lastrowid
            


            args2 = (clinica[0],clinica[1],clinica[2],clinica[3],clinica[4],clinica[5],id_endereco)
            self.cursor.execute('INSERT INTO clinica(cnpj,razao_social,nome_fantasia,telefone,email,observacao,id_endereco) VALUES (%s,%s,%s,%s,%s,%s,%s)', args2)

            
            self.conn.commit()

            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection() 

    def filter_data_relatorio_clinica_cadastrada(self,texto_data_inicio_clinica_cadastrada,texto_data_final_clinica_cadastrada):
        self.connect()
        try:
            self.cursor.execute(f"""
                    SELECT clinica.cnpj, clinica.email, clinica.razao_social, clinica.telefone, endereco.logradouro from clinica
                    INNER JOIN endereco on endereco.id_endereco = clinica.id_endereco
                    WHERE clinica.data_cadastro BETWEEN '{texto_data_inicio_clinica_cadastrada}' and '{texto_data_final_clinica_cadastrada}';
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def buscar_relatorio_clinica_cadastrada(self):
        self.connect()
        try:
            self.cursor.execute(f"""
                               SELECT clinica.cnpj, clinica.email, clinica.razao_social, clinica.telefone, endereco.logradouro from clinica
                               INNER JOIN endereco on endereco.id_endereco = clinica.id_endereco;
                                """)
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def buscar_relatorio_clinica_cadastrada_pesquisa(self,texto):
        self.connect()
        try:
            self.cursor.execute(f"""
                                SELECT clinica.cnpj, clinica.email, clinica.razao_social, clinica.telefone, endereco.logradouro from clinica
                                INNER JOIN endereco on endereco.id_endereco = clinica.id_endereco
                                WHERE clinica.cnpj LIKE "%{texto}%" OR clinica.email LIKE "%{texto}%" OR clinica.razao_social LIKE "%{texto}%" OR clinica.telefone LIKE "%{texto}%" OR endereco.logradouro LIKE "%{texto}%";
                                """)
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def filter_data_relatorio_fornecedor_cadastrado(self,texto_data_inicio_fornecedor_cadastrado,texto_data_final_fornecedor_cadastrado):
        self.connect()
        try:
            self.cursor.execute(f"""
                    SELECT fornecedor.cnpj, fornecedor.razao_social, fornecedor.telefone_celular, fornecedor.telefone_fixo, fornecedor.email, endereco.logradouro, endereco.cidade, endereco.estado from fornecedor
                    INNER JOIN endereco on endereco.id_endereco = fornecedor.id_endereco
                    WHERE clinica.data_cadastro BETWEEN '{texto_data_inicio_fornecedor_cadastrado}' and '{texto_data_final_fornecedor_cadastrado}';
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def buscar_relatorio_fornecedor_cadastrado(self):
        self.connect()
        try:
            self.cursor.execute(f"""
                                SELECT fornecedor.cnpj, fornecedor.razao_social, fornecedor.telefone_celular, fornecedor.telefone_fixo, fornecedor.email, endereco.logradouro, endereco.cidade, endereco.estado from fornecedor
                                INNER JOIN endereco on endereco.id_endereco = fornecedor.id_endereco;
                                """)
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def buscar_relatorio_fornecedor_cadastrado_pesquisa(self,texto):
        self.connect()
        try:
            self.cursor.execute(f"""
                                SELECT fornecedor.cnpj, fornecedor.razao_social, fornecedor.telefone_celular, fornecedor.telefone_fixo, fornecedor.email, endereco.logradouro, endereco.cidade, endereco.estado from fornecedor
                                INNER JOIN endereco on endereco.id_endereco = fornecedor.id_endereco
                                WHERE fornecedor.cnpj LIKE "%{texto}%" OR fornecedor.email LIKE "%{texto}%" OR fornecedor.razao_social LIKE "%{texto}%" OR fornecedor.telefone_celular LIKE "%{texto}%" OR fornecedor.telefone_fixo LIKE "%{texto}%" OR endereco.logradouro LIKE "%{texto}%" OR endereco.cidade LIKE "%{texto}%" OR endereco.estado LIKE "%{texto}%";
                                """)
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
  
    def buscar_relatorio_atendimento_pesquisa(self, texto):
        self.connect()
        try:
            busca = """
                SELECT pessoa.nome, pessoa.cpf, usuario.cns, pessoa.sexo, pessoa.telefone, pessoa.email clinica.nome_fantasia, consulta.data_consulta, consulta.situacao
                FROM pessoa
                INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                INNER JOIN consulta ON consulta.id_matricula = pessoa.id_matricula
                INNER JOIN clinica ON clinica.id_clinica = usuario.local_tratamento
                WHERE pessoa.nome LIKE %s OR pessoa.cpf LIKE %s OR usuario.cns LIKE %s OR pessoa.sexo LIKE %s OR pessoa.telefone LIKE %s OR pessoa.email LIKE %s OR clinica.razao_social LIKE %s OR consulta.data_consulta LIKE %s OR consulta.situacao LIKE %s;
            """
            parametro = tuple(f"%{texto}%" for _ in range(9)) 
            self.cursor.execute(busca, parametro)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO", str(err)
        finally:
            self.close_connection()

    
    def buscar_relatorio_atendimento(self,):
        self.connect()
        try:
            self.cursor.execute(f"""
                                SELECT pessoa.nome, pessoa.cpf, usuario.cns, pessoa.sexo, pessoa.telefone, pessoa.email, clinica.razao_social, consulta.data_consulta, consulta.situacao
                                from pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                                INNER JOIN consulta ON consulta.id_matricula = pessoa.id_matricula
                                INNER JOIN clinica ON clinica.id_clinica = usuario.local_tratamento
                                """)
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def filter_data_relatorio_atendimento(self,texto_data_inicio_atendimento,texto_data_final_atendimento):
        self.connect()
        try:
            self.cursor.execute(f"""
                    SELECT pessoa.nome, pessoa.cpf, usuario.cns, pessoa.sexo, pessoa.telefone, pessoa.email, clinica.razao_social, consulta.data_consulta, consulta.situacao
                    from pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                    INNER JOIN consulta ON consulta.id_matricula = pessoa.id_matricula
                    INNER JOIN clinica ON clinica.id_clinica = usuario.local_tratamento
                    WHERE consulta.data_consulta BETWEEN '{texto_data_inicio_atendimento}' and '{texto_data_final_atendimento}';
            """)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
   

    def delete(self,id):
        self.connect()
        try:
            #self.connect()
            self.cursor.execute(
                f"""DELETE FROM cadastro WHERE id = '{id}' """
            )
            self.conn.commit()

            return "OK","Cadastro excluído com sucesso!"

        except Exception as err:
            return "ERRO",str(err)
        
        finally:
            self.close_connection()





    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            # print("Conexão encerrada com sucesso!!")

if __name__ == "__main__":
    db = DataBase()
    db.connect()
    db.close_connection()

