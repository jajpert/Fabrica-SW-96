import mysql.connector

class DataBase():
    def __init__(self, banco = "Abrec") -> None:
        self.banco = banco

    def connect(self):
        
        self.conn = mysql.connector.connect(host='192.168.22.9',database='abrec',user='fabrica',password='fabrica@2022')
        #self.conn = mysql.connector.connect(host='localhost',database='abrec',user='root',password='Bnas123!@#')
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado ao Servidor de Banco de Dados: ", db_info)
        else:
            print("Erro")  

    def select_agendamentos(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT DATE_FORMAT(data, '%d/%m/%Y') AS data, TIME_FORMAT(hora, "%H:%i") AS hora, nome, profissional, anotacao FROM agendamento;
            """)

            result = self.cursor.fetchall()
            
            #verifica os dados do select
            #for linha in result:
            #   print(linha)
            
            return result
            #retorn a lista do banco para quem chamou a função
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_pessoa(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT id_matricula FROM pessoa ORDER BY id_matricula DESC LIMIT 1;
            """)
            result = self.cursor.fetchall()
            
            #verifica os dados do select
            #for linha in result:
            #   print(linha)
            
            return result
            #retorn a lista do banco para quem chamou a função
        except Exception as err:
            print(err)

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
                SELECT local_tratamento FROM usuario WHERE id_matricula IN ({id_matricu});
            """)
            resultado2 = self.cursor.fetchall()

            lista = []
            for i in resultado1:
                for n in i:
                    lista.append(n)
            for i in resultado2:
                for n in i:
                    lista.append(n)          
            
            #verifica os dados do select
            #for linha in result:
            #   print(linha)
            return lista
            #retorn a lista do banco para quem chamou a função
        except Exception as err:
            print(err)

        finally:
            self.close_connection()
    
    def select_colaborador(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT id_colaborador FROM colaborador ORDER BY id_colaborador DESC LIMIT 1;
            """)
            result = self.cursor.fetchall()
            
            #verifica os dados do select
            #for linha in result:
            #   print(linha)
            
            return result
            #retorn a lista do banco para quem chamou a função
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def validarLogin(self, login, senha):
        print("entrou validação login")
        self.connect()
        try:
            #
            self.cursor.execute(f"""Select login, senha from colaborador where login = '{login}' and senha = '{senha}';""")

            result = self.cursor.fetchall()
            #print (result)
            
            return result

        except Exception as err:
            print(err)

        finally:
            self.close_connection()
    
    def select_usuario(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT id_usuario FROM usuario ORDER BY id_usuario DESC LIMIT 1;
            """)
            result = self.cursor.fetchall()
            
            #verifica os dados do select
            #for linha in result:
            #   print(linha)
            
            return result
            #retorn a lista do banco para quem chamou a função
        except Exception as err:
            print(err)

        finally:
            self.close_connection()
            
    def relatorio_pessoa(self):
        self.connect()
        try:
            self.cursor.execute("""
                    SELECT pessoa.nome, pessoa.cpf, TIMESTAMPDIFF(YEAR, data_nascimento,NOW()) as idades, pessoa.sexo, pessoa.telefone, usuario.beneficio, usuario.cns,
                    usuario.nis, usuario.situacao_trabalho,clinica.nome_fantasia, endereco.bairro, 
                    endereco.cidade,pessoa.data_cadastro
                    FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                    INNER JOIN endereco ON endereco.id_endereco = pessoa.id_endereco
                    LEFT JOIN clinica ON clinica.id_endereco = endereco.id_endereco;
                    """)
            result = self.cursor.fetchall()
            #verifica os dados do select
            #for linha in result:
            #   print(linha)
            return result
            #retorn a lista do banco para quem chamou a função
        except Exception as err:
            print(err)

        finally:
            self.close_connection()
            
    def filter_data(self,texto_data_inicio,texto_data_final):
        self.connect()
        try:
            self.cursor.execute(f"""
                    SELECT pessoa.nome, pessoa.cpf,TIMESTAMPDIFF(YEAR, data_nascimento,NOW()) as idades, pessoa.sexo, pessoa.telefone, usuario.beneficio, usuario.cns,
                    usuario.nis, usuario.local_tratamento, usuario.situacao_trabalho,clinica.nome_fantasia, endereco.bairro, 
                    endereco.cidade,pessoa.data_cadastro
                    FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                    INNER JOIN endereco ON endereco.id_endereco = pessoa.id_endereco
                    LEFT JOIN clinica ON clinica.id_endereco = endereco.id_endereco WHERE data_cadastro BETWEEN '{texto_data_inicio}' and '{texto_data_final}';
            """)
            result = self.cursor.fetchall()
            
            #verifica os dados do select
            #for linha in result:
            #   print(linha)
            
            return result
            #retorn a lista do banco para quem chamou a função
        except Exception as err:
            print(err)

        finally:
            self.close_connection()
            
    def filtrar_relatorio(self,texto):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT pessoa.nome, pessoa.cpf,TIMESTAMPDIFF(YEAR, data_nascimento,NOW()) as idades, pessoa.sexo, pessoa.telefone, usuario.beneficio, usuario.cns,
                usuario.nis, usuario.local_tratamento, usuario.situacao_trabalho, clinica.nome_fantasia, endereco.bairro, endereco.cidade
                FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                INNER JOIN endereco ON endereco.id_endereco = pessoa.id_endereco
                LEFT JOIN clinica ON clinica.id_endereco = endereco.id_endereco
                WHERE pessoa.nome LIKE "%{texto}%" OR pessoa.cpf LIKE "%{texto}%" OR clinica.nome_fantasia LIKE "%{texto}%" OR endereco.bairro LIKE "%{texto}%" OR endereco.cidade LIKE "%{texto}%"
                OR pessoa.sexo LIKE "%{texto}%" OR usuario.beneficio LIKE "%{texto}%";
            """)
            result = self.cursor.fetchall()
            
            # #verifica os dados do select
            # for linha in result:
            #    print(linha)
            
            return result
            #retorna a lista do banco para quem chamou a função
        except Exception as err:
            print(err)

        finally:
            self.close_connection()
        
    def filter_idade(self,texto_idade_inicio,texto_idade_final):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT pessoa.nome, pessoa.cpf, TIMESTAMPDIFF(YEAR, data_nascimento,NOW()) as idades, pessoa.sexo, pessoa.telefone, usuario.beneficio, usuario.cns,
                usuario.nis, usuario.situacao_trabalho,clinica.nome_fantasia, endereco.bairro, 
                endereco.cidade,pessoa.data_cadastro
                FROM pessoa INNER JOIN usuario ON pessoa.id_matricula = usuario.id_matricula
                INNER JOIN endereco ON endereco.id_endereco = pessoa.id_endereco
                LEFT JOIN clinica ON clinica.id_endereco = endereco.id_endereco WHERE TIMESTAMPDIFF(YEAR, data_nascimento,NOW()) BETWEEN '{texto_idade_inicio}' and '{texto_idade_final}';""")
            result = self.cursor.fetchall()
        
            return result
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()
            
            
    def filter_usuario_area_sigilosa(self,id_area_sigilosa):
        self.connect()
        try: 
            self.cursor.execute(f"""select  area_sigilosa.data_cadastro, area_sigilosa.observacao_gerais from area_sigilosa
                                INNER JOIN pessoa ON pessoa.id_matricula = area_sigilosa.id_matricula and 
                                pessoa.id_matricula = '{id_area_sigilosa}';""")
            result = self.cursor.fetchall()
        
            return result
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()
    def filter_agenda(self,text):
        self.connect()
        try: 
            self.cursor.execute(f"""select data, hora , nome, profissional, anotacao from agendamento where nome like '%{text}%' or  profissional like '%{text}%';""")
            result = self.cursor.fetchall()
        
            return result
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()
        
    
    def select_usuario_ids(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT id_usuario, id_matricula FROM usuario WHERE id_cuidador IS NULL ORDER BY id_usuario DESC LIMIT 10;
            """)
            result = self.cursor.fetchall()
            
            #verifica os dados do select
            #for linha in result:
            #   print(linha)
            
            return result
            #retorn a lista do banco para quem chamou a função
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_clinica_ids(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT id_clinica FROM clinica ORDER BY id_clinica;
            """)
            result = self.cursor.fetchall()
            
            #verifica os dados do select
            #for linha in result:
            #   print(linha)
            
            return result
            #retorn a lista do banco para quem chamou a função
        except Exception as err:
            print(err)

        finally:
            self.close_connection()
    
    def select_cuidador(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT id_cuidador FROM cuidador ORDER BY id_cuidador DESC LIMIT 1;
            """)
            result = self.cursor.fetchall()
            
            #verifica os dados do select
            #for linha in result:
            #   print(linha)
            
            return result
            #retorn a lista do banco para quem chamou a função
        except Exception as err:
            print(err)

        finally:
            self.close_connection()
    
    def select_nome_usuario(self,id_matricula):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT nome FROM pessoa WHERE id_matricula = {id_matricula};
            """)
            result = self.cursor.fetchall()
            
            #verifica os dados do select
            # for linha in result:
            #    print(linha)
            
            return result
            #retorna a lista do banco para quem chamou a função
        except Exception as err:
            print(err)

        finally:
            self.close_connection()


    def select_nome_Clinica(self,id_clinica):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT nome_fantasia FROM clinica WHERE id_clinica = {id_clinica};
            """)
            result = self.cursor.fetchall()
            
            #verifica os dados do select
            # for linha in result:
            #    print(linha)
            
            return result
            #retorna a lista do banco para quem chamou a função
        except Exception as err:
            print(err)

        finally:
            self.close_connection()


    def busca_cuidador(self, cpf):
        print("entrou busca cuidador")
        self.connect()
        try:
            self.cursor.execute(f"""SELECT pessoa.id_matricula, nome, cpf, rg, data_emissao, orgao_exp, sexo, 
                                parentesco, observacao, telefone, email, cep, logradouro, numero, bairro, 
                                cidade,estado, endereco.id_endereco, cuidador.id_matricula
                                from pessoa inner join endereco on pessoa.id_endereco = endereco.id_endereco 
                                left join cuidador on pessoa.id_matricula = cuidador.id_matricula 
                                where cpf like '{cpf}';""")
            result = self.cursor.fetchall()
            
            #verifica os dados do select
            # for linha in result:
            #     print(linha)
            return result[0]
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    
    def busca_usuario(self, cpf):
        print("entrou busca usuario")
        self.connect()
        try:
            
            self.cursor.execute(f"""
                SELECT pessoa.id_matricula, nome, data_nascimento,status, cpf,
                rg, data_emissao, orgao_exp, nis, cns, sexo, telefone, 
                email, cep, logradouro, numero, bairro, cidade, estado,
                estado_civil, escolaridade, pessoa_deficiencia, tipo_deficiencia,
                media_renda_familiar, tipo_transporte, vale_transporte, situacao_trabalho,
                beneficio, tarifa_social, tipo_tratamento, local_tratamento, patologia_base,data_inicio, periodo,
                endereco.id_endereco, usuario.id_matricula
                from pessoa inner join endereco on pessoa.id_endereco = endereco.id_endereco 
                left join usuario on pessoa.id_matricula = usuario.id_matricula where cpf like '%{cpf}%'; """)
            result = self.cursor.fetchall()
            
            #verifica os dados do select
            # for linha in result:
            #     print(linha)
            
            return result[0]
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()


    def busca_colaborador(self, cpf):
        print("entrei")
        self.connect()
        try:
            self.cursor.execute(f"""SELECT pessoa.id_matricula, nome, data_nascimento, cpf, rg, pessoa.status, orgao_exp, data_emissao,
                                    colaborador.pis, sexo, telefone, email, cep, logradouro,numero, bairro, cidade, estado,
                                    estado_civil, escolaridade, cargo, periodo, salario, perfil, senha, endereco.id_endereco, colaborador.id_matricula
                                    from pessoa inner join endereco on pessoa.id_endereco = endereco.id_endereco  
                                    left join colaborador on colaborador.id_matricula = pessoa.id_matricula
                                    where cpf like '%{cpf}%';""")
            result = self.cursor.fetchall()
            
            #verifica os dados do select
            # for linha in result:
            #     print(linha)
            return result[0]
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
            self.cursor.execute(f"""SELECT usuario.id_usuario, pessoa.nome, pessoa.telefone, clinica.nome_fantasia
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
            args = (consulta[0],consulta[1],consulta[2],consulta[3],consulta[4])
            self.cursor.execute('INSERT INTO consulta(situacao,data,hora,observacao,id_usuario) VALUES (%s,%s,%s,%s,%s)', args)
            self.conn.commit()
            return "Cadastrado com Sucesso!!"

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def buscar_info_consulta(self,cpf):
        self.connect()
        try:
            self.cursor.execute(f"""
                                SELECT consulta.id_consulta,consulta.data,consulta.situacao,consulta.observacao FROM consulta 
                                INNER JOIN usuario ON usuario.id_usuario = consulta.id_usuario
                                left join pessoa ON pessoa.id_matricula = usuario.id_matricula AND 
                                pessoa.cpf LIKE '{cpf}';
                                """)
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()
            
    def alterar_usuario_consulta_as(self, campo):
        self.connect()
        try:
            self.cursor.execute(f""" UPDATE consulta SET
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
            print(err)


    def atualizar_cuidador (self,cuidador,pessoa,endereco):
        print("Entrou ATT CUIDADOR")

        id_matricula_cuidador = str(cuidador[2])
        id_endereco_cuidador = str(endereco[0])

        print(f"AQ É CUIDADOR -> {cuidador} ")
        print(f"AQ É PESSOA -> {pessoa} ")
        print(f"AQ É ENDERECO -> {endereco} ")


        self.connect()
        try:
            self.cursor.execute(f""" UPDATE cuidador SET parentesco = '{cuidador[0]}', observacao = '{cuidador[1]}' WHERE id_matricula = '{id_matricula_cuidador}';""")
            id_matricula = self.cursor.lastrowid
            print(id_matricula)
            self.conn.commit()

            self.cursor.execute(f"""UPDATE pessoa SET nome = '{pessoa[1]}', cpf = '{pessoa[2]}', rg = '{pessoa[3]}', data_emissao = '{pessoa[4]}',
                                orgao_exp = '{pessoa[5]}', sexo = '{pessoa[6]}', telefone = '{pessoa[7]}', email = '{pessoa[8]}' WHERE id_matricula = {pessoa[0]};  """)
            id_matricula = self.cursor.lastrowid
            self.conn.commit()

            self.cursor.execute(f"""UPDATE endereco  SET cep = '{endereco[1]}', logradouro = '{endereco[2]}',
                                numero = '{endereco[3]}', bairro = '{endereco[4]}', cidade = '{endereco[5]}',
                                estado = '{endereco[6]}' WHERE id_endereco = '{id_endereco_cuidador}';""")
            self.conn.commit()
            


            return "OK","Cuidador atualizado com sucesso!!"
        except Exception as err:
            print(err)
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def atualizar_usuario(self,endereco,pessoa,usuario):
        print("Entrou atualizar usuario!!")

        id_endereco_usuario = str(endereco[0])
        id_matricula_usuario = str(usuario[14])


        print(f"AQ É ENDEREÇO -> {endereco}")
        print(f"AQ É PESSOA -> {pessoa}")
        print(f"AQ É USUARIO -> {usuario}")
        self.connect()
        try:
            self.cursor.execute(f"""UPDATE endereco  SET cep = '{endereco[1]}', logradouro = '{endereco[2]}',
                                numero = '{endereco[3]}', bairro = '{endereco[4]}', cidade = '{endereco[5]}',
                                estado = '{endereco[6]}' WHERE id_endereco = '{id_endereco_usuario}';""")
            self.conn.commit()
            
            

            self.cursor.execute(f"""UPDATE pessoa SET nome = '{pessoa[1]}', data_nascimento = '{pessoa[2]}', cpf = '{pessoa[3]}',rg = '{pessoa[4]}', data_emissao = '{pessoa[5]}',
                                orgao_exp = '{pessoa[6]}', sexo = '{pessoa[7]}', status = '{pessoa[8]}', telefone = '{pessoa[9]}', 
                                email = '{pessoa[10]}', escolaridade = '{pessoa[11]}', estado_civil = '{pessoa[12]}',
                                pessoa_deficiencia = '{pessoa[13]}', tipo_deficiencia = '{pessoa[14]}' WHERE id_matricula = '{pessoa[0]}';  """)
            self.conn.commit()


            self.cursor.execute(f"""UPDATE usuario SET nis = '{usuario[0]}', cns = '{usuario[1]}', observacao = '{usuario[2]}', situacao_trabalho = '{usuario[3]}',
                                tipo_transporte = '{usuario[4]}', tipo_tratamento = '{usuario[5]}', beneficio = '{usuario[6]}', local_tratamento = '{usuario[7]}',
                                periodo = '{usuario[8]}', data_inicio = '{usuario[9]}', patologia_base = '{usuario[10]}', tarifa_social = '{usuario[11]}', media_renda_familiar = '{usuario[12]}',
                                vale_transporte = '{usuario[13]}'  WHERE id_matricula = '{id_matricula_usuario}';  """)
            self.conn.commit()

            return "OK","Usuario atualizado com sucesso!!"
        except Exception as err:
            print(err)
            return "ERRO",str(err)

        finally:
            self.close_connection()


    def atualizar_colaborador(self,colaborador,pessoa,endereco):
        print("Entrou ATT Colaborador")
        
        print(f"AQ É ENDERECO Colabo -> {endereco}")
        print(f"AQ É PESSOA Colabo -> {pessoa}")
        print(f"AQ É COLABORADOR Colabo -> {colaborador}")
        
        
        id_matricula_pessoa = int(pessoa[0])
        id_endereco_colaborador = int(endereco[0])
        tipo_endereco = type(id_endereco_colaborador)
        tipo_pessoa = type(id_matricula_pessoa)

        print(f"ID PESSOA -> {id_matricula_pessoa}")
        print(f"CLASSE PESSOA ID -> {tipo_pessoa}")
        print(f"ID ENDERECO -> {id_endereco_colaborador}")
        print(f"TIPO ENDERECO -> {tipo_endereco}")
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
                                periodo = '{colaborador[4]}', login = '{colaborador[5]}', senha = '{colaborador[6]}', perfil = '{colaborador[7]}' WHERE id_matricula = '{id_matricula_pessoa}';""")
            self.conn.commit()

            return "OK","Colaborador atualizado com sucesso!!"
        except Exception as err:
            print(err)
            return "ERRO",str(err)

        finally:
            self.close_connection()





    def cadastro_usuario(self,endereco,pessoa,usuario):
        print("Entrou cadastro usuario!!")
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

            self.cursor.execute('INSERT INTO pessoa(nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status,telefone,email,escolaridade,estado_civil,pessoa_deficiencia,tipo_deficiencia,id_endereco) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],pessoa[5],pessoa[6],pessoa[7],pessoa[8],pessoa[9],pessoa[10],pessoa[11],pessoa[12],pessoa[13],id_endereco))
            id_matricula = self.cursor.lastrowid
            self.conn.commit()
            print(id_matricula)

            self.cursor.execute("""
                INSERT INTO usuario (nis,cns,observacao,situacao_trabalho,tipo_transporte,tipo_tratamento,beneficio,local_tratamento,periodo,data_inicio,patologia_base,outras_patologias,tarifa_social,media_renda_familiar,vale_transporte,id_matricula) 
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,(usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5],usuario[6],usuario[7],usuario[8],usuario[9],usuario[10],usuario[11],usuario[12],usuario[13],usuario[14],id_matricula))

            self.conn.commit()

            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            print(err)
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

            print('ID do endereco',id_endereco)

            args2 = (pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],pessoa[5],pessoa[6],pessoa[7],pessoa[8],id_endereco)
            self.cursor.execute('INSERT INTO pessoa(nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,telefone,email,id_endereco) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', args2)
            id_matricula = self.cursor.lastrowid
            self.conn.commit()

            print('id matricula',id_matricula)

            self.cursor.execute("""
                INSERT INTO cuidador (parentesco,observacao,id_matricula) VALUES (%s,%s,%s)
            """,(cuidador[0],cuidador[1],id_matricula))
            id_matricula_cuidador = self.cursor.lastrowid
            self.conn.commit()

            self.cursor.execute(f'UPDATE usuario SET id_cuidador = {id_matricula_cuidador} WHERE id_usuario = {usuario}')
            print("fez o inset do id")
            self.conn.commit()

            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            #print(err)
            return "ERRO",str(err)
        
    def cadastro_colaborador(self,endereco,pessoa,colaborador):
        self.connect()
        try:
            args = (endereco[0],endereco[1],endereco[2],endereco[3],endereco[4],endereco[5])
            self.cursor.execute('INSERT INTO endereco(cep, logradouro, numero, bairro, cidade, estado) VALUES (%s,%s,%s,%s,%s,%s)', args)
        
            id_endereco = self.cursor.lastrowid
            print('ID do endereco',id_endereco)

            args2 = (pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],pessoa[5],pessoa[6],pessoa[7],pessoa[8],pessoa[9],pessoa[10],pessoa[11],id_endereco)
            self.cursor.execute('INSERT INTO pessoa(nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status,telefone,email,escolaridade,estado_civil,id_endereco) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', args2)
            id_matricula = self.cursor.lastrowid
            print('id matricula',id_matricula)

            args3 = (colaborador[0],colaborador[1],colaborador[2],colaborador[3],colaborador[4],colaborador[5],colaborador[6],colaborador[7],id_matricula)
            self.cursor.execute("INSERT INTO colaborador (pis,data_admissao,salario,cargo,periodo,login,senha,perfil,id_matricula) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", args3)
            id_colaborador = self.cursor.lastrowid
            print(id_colaborador)
            self.conn.commit()
            
            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            #print(err)
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
            #print(err)
            return "ERRO",str(err)
    
    def cadastro_agendamento(self, agendamento):
        self.connect()
        try:
            args = (1, agendamento[0],  agendamento[1],agendamento[2], agendamento[3], agendamento[4], agendamento[5], agendamento[6], agendamento[7], agendamento[8])
            self.cursor.execute('INSERT INTO agendamento(id_colaborador, id_matricula, cpf, nome, telefone, clinica, profissional, data, hora, anotacao) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', args)
    
            self.conn.commit()
            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            #print(err)
            return "ERRO",str(err)
        
        
    def buscar_id_matricula_area_sigilosa(self,id_matricula):
        self.conn()
        try:
            self.cursor.execute(f"""SELECT id_matricula from usuario WHERE ususario.id_matricula = ;""")

            return(f"Puxei o id {id_matricula}")
        except Exception as err:
            #print(err)
            return "ERRO",str(err)
        finally:
            self.close_connection()




    def cadastrar_area_sigilosa (self,area_sigilosa):
        self.connect()
        print(area_sigilosa)
        try:
            args = (area_sigilosa[0],area_sigilosa[1],area_sigilosa[2])
            self.cursor.execute('INSERT INTO area_sigilosa(obito_paciente, observacao_gerais,id_matricula) VALUES (%s,%s,%s)', args)
            self.conn.commit()

            return("OK","Cadastro area sigilosa com sucesso!!!")

        except Exception as err:
            #print(err)
            return "ERRO",str(err)
        finally:
            self.close_connection()
        
    def update(self,tupla_de_dados):
        #print(tupla_de_dados)
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
            print(err)
        
        finally:
            self.close_connection()

    def cadastro_clinica(self,endereco,clinica):
        print("Entrou cadastro usuario!!")
        self.connect()
        try:
            args = (endereco[0],endereco[1],endereco[2],endereco[3],endereco[4],endereco[5])
            self.cursor.execute('INSERT INTO endereco(cep, logradouro, numero, bairro, cidade, estado) VALUES (%s,%s,%s,%s,%s,%s)', args)
            id_endereco = self.cursor.lastrowid
            


            args2 = (clinica[0],clinica[1],clinica[2],clinica[3],clinica[4],clinica[5],id_endereco)
            self.cursor.execute('INSERT INTO clinica(cnpj,razao_social,nome_fantasia,telefone,email,observacao,id_endereco) VALUES (%s,%s,%s,%s,%s,%s,%s)', args2)

            
            
            print(args)
            print(args2)
            self.conn.commit()

            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            print(err)
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
            print(err)
        
        finally:
            self.close_connection()


    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexão encerrada com sucesso!!")

if __name__ == "__main__":
    db = DataBase()
    db.connect()
    db.close_connection()

