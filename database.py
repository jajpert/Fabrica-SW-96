import mysql.connector

class DataBase():
    def __init__(self, banco = "abrec") -> None:
        self.banco = banco

    def connect(self):
        self.conn = mysql.connector.connect(host='localhost',database=self.banco,user='root',password='')
        
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado ao Servidor de Banco de Dados: ",db_info)
        else:
            print("Erro")  


    def select(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT * FROM cadastro ORDER BY ID DESC;
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


    def cadastro_usuario(self,endereco,pessoa,usuario,cuidador):
        self.connect()
        try:
            args = (endereco[0],endereco[1],endereco[2],endereco[3])
            self.cursor.execute('INSERT INTO endereco(cep, logradouro, numero, bairro) VALUES (%s,%s,%s,%s)', args)
            id_endereco = self.cursor.lastrowid

            print(endereco)
            print(id_endereco)
            print(pessoa)

            self.cursor.execute("""
                INSERT INTO cuidador (parentesco,observacao,id_matricula) VALUES (%s,%s,%s)
            """,(cuidador[0],cuidador[1],cuidador[2]))

            id_cuidador = self.cursor.lastrowid
            print(id_cuidador)
            print(len(usuario))
            print(len(pessoa))

            print()
            self.cursor.execute("""
                insert into pessoa (nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status_,telefone,email,escolaridade,estado_civil,pessoa_deficiencia,data_cadastro,id_endereco,id_colaborador_resp)
                values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
             """,(pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],pessoa[5],pessoa[6],pessoa[7],pessoa[8],pessoa[9],pessoa[10],pessoa[11],pessoa[12],pessoa[13],id_endereco,pessoa[14]))
            id_matricula = self.cursor.lastrowid
            print(id_matricula)

            self.cursor.execute("""
                INSERT INTO usuario (nis,cns,observacao,situacao_trabalho,tipo_transporte,tipo_tratamento,beneficio,local_tratamento,periodo,data_inicio,patologia_base,tarifa_social,media_renda_familiar,vale_transporte,id_matricula,id_beneficio,id_cuidador,id_clinica,id_curso) 
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
            """,(usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5],usuario[6],usuario[7],usuario[8],usuario[9],usuario[10],usuario[11],usuario[12],usuario[13],id_matricula,1,id_cuidador,1,1))

            self.conn.commit()

            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            #print(err)
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def cadastro_cuidador(self,endereco,pessoa,cuidador):
        self.connect()
        try:
            args = (endereco[0],endereco[1],endereco[2],endereco[3])
            self.cursor.execute('INSERT INTO endereco(cep, logradouro, numero, bairro) VALUES (%s,%s,%s,%s)', args)
        
            id_endereco = self.cursor.lastrowid
            print('ID do endereco',id_endereco)

            args2 = (pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],pessoa[5],pessoa[6],pessoa[7],pessoa[8],pessoa[9],id_endereco,)
            self.cursor.execute('INSERT INTO pessoa(nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,data_cadastro,telefone,email,id_endereco) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', args2)
            id_matricula = self.cursor.lastrowid
            print('id matricula',id_matricula)

            self.cursor.execute("""
                INSERT INTO cuidador (parentesco,observacao,id_matricula) VALUES (%s,%s,%s)
            """,(cuidador[0],cuidador[1],id_matricula))

            self.conn.commit()
            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            #print(err)
            return "ERRO",str(err)
        
    def cadastro_colaborador(self,endereco,pessoa,colaborador,login):
        self.connect()
        try:
            args = (endereco[0],endereco[1],endereco[2],endereco[3])
            self.cursor.execute('INSERT INTO endereco(cep, logradouro, numero, bairro) VALUES (%s,%s,%s,%s)', args)
        
            id_endereco = self.cursor.lastrowid
            print('ID do endereco',id_endereco)

            args2 = (pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],pessoa[5],pessoa[6],pessoa[7],pessoa[8],pessoa[9],pessoa[10],pessoa[11],pessoa[12],pessoa[13],id_endereco)
            self.cursor.execute('INSERT INTO pessoa(nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status_,data_cadastro,telefone,email,escolaridade,estado_civil,pessoa_deficiencia,id_endereco) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', args2)
            id_matricula = self.cursor.lastrowid
            print('id matricula',id_matricula)

            self.cursor.execute("""
                INSERT INTO colaborador (salario,data_admissao,pis,periodo,descricao_cargo,id_matricula,id_cargo) VALUES (%s,%s,%s,%s,%s,%s,%s)
            """,(colaborador[0],colaborador[1],colaborador[2],pessoa[3],pessoa[4],id_matricula,1))
            id_colaborador = self.cursor.lastrowid
            print(id_colaborador)

            args3 = (login[0],login[1],login[2],login[3],login[4],id_colaborador)
            self.cursor.execute('INSERT INTO login(usuario, senha, perfil, data_login, status, id_colaborador) VALUES (%s,%s,%s,%s,%s,%s)', args3)


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
    #db.create_table()
    #db.insert("43434343","BLABLABLA","909090","bla@gmail.com","rua tal","CG","MS")
    #db.delete(23)
    #db.update(20,"PEDROO SAMPAIO SILVA")
    #dados = db.select()
    #db.filter("444")
    db.close_connection()

