import mysql.connector

class DataBase():
    def __init__(self, banco = "Abrec") -> None:
        self.banco = banco

    def connect(self):
        self.conn = mysql.connector.connect(host='localhost',database='abrec',user='root',password='*Samela710*')
        ##self.conn = mysql.connector.connect(host='192.168.22.9',database='abrec',user='fabrica',password='fabrica@2022')
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado ao Servidor de Banco de Dados: ", db_info)
        else:
            print("Erro")  


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

    def filter(self,texto):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT * FROM cadastro WHERE nome LIKE '%{texto}%' or cnpj LIKE '%{texto}%';
            """)
            result = self.cursor.fetchall()
            
            #verifica os dados do select
            for linha in result:
               print(linha)
            
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
                                cidade,estado
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
                beneficio, tarifa_social, tipo_tratamento, local_tratamento, patologia_base,data_inicio, periodo
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
                                    estado_civil, escolaridade, cargo, periodo, salario, perfil, senha, login
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
                INSERT INTO usuario (nis,cns,observacao,situacao_trabalho,tipo_transporte,tipo_tratamento,beneficio,local_tratamento,periodo,data_inicio,patologia_base,tarifa_social,media_renda_familiar,vale_transporte,id_matricula) 
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,(usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5],usuario[6],usuario[7],usuario[8],usuario[9],usuario[10],usuario[11],usuario[12],usuario[13],id_matricula))

            self.conn.commit()

            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            print(err)
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def cadastro_cuidador(self,endereco,pessoa,cuidador):
        self.connect()
        try:
            args = (endereco[0],endereco[1],endereco[2],endereco[3],endereco[4],endereco[5])
            self.cursor.execute('INSERT INTO endereco(cep,logradouro,numero,bairro,cidade,estado) VALUES (%s,%s,%s,%s,%s,%s)', args)
            id_endereco = self.cursor.lastrowid
            self.conn.commit()

            print('ID do endereco',id_endereco)

            args2 = (pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],pessoa[5],pessoa[6],pessoa[7],id_endereco)
            self.cursor.execute('INSERT INTO pessoa(nome,cpf,rg,data_emissao,orgao_exp,sexo,telefone,email,id_endereco) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)', args2)
            id_matricula = self.cursor.lastrowid
            self.conn.commit()

            print('id matricula',id_matricula)

            self.cursor.execute("""
                INSERT INTO cuidador (parentesco,observacao,id_matricula) VALUES (%s,%s,%s)
            """,(cuidador[0],cuidador[1],id_matricula))
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

            self.cursor.execute("""
                INSERT INTO colaborador (pis,data_admissao,salario,cargo,periodo,login,senha,perfil,id_matricula) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,(colaborador[0],colaborador[1],colaborador[2],colaborador[3],colaborador[4],colaborador[5],colaborador[6],colaborador[7],id_matricula))
            id_colaborador = self.cursor.lastrowid
            print(id_colaborador)


            self.conn.commit()
            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            #print(err)
            return "ERRO",str(err)


    def cadastro_curso(self,endereco,curso):
        self.connect()
        try:
            args = (endereco[0],endereco[1],endereco[2],endereco[3])
            self.cursor.execute('INSERT INTO endereco(cep, logradouro, numero, bairro) VALUES (%s,%s,%s,%s)', args)
    
            args2 = (curso[0],curso[1],curso[2],curso[3],curso[4],curso[5],curso[6],curso[7],curso[8],curso[9],curso[10],curso[11])
            self.cursor.execute('INSERT INTO curso_evento (nome_curso_evento,data_inicio,data_fim,carga_horaria,id_palestrante,periodo,data_inclusao,tipo_curso,responsavel,horario_inicial,horario_final,vagas) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',args2)

            self.conn.commit()
            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            #print(err)
            return "ERRO",str(err)
        
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

