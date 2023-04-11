import mysql.connector

class DataBase():
    def __init__(self, banco = "abrec") -> None:
        self.banco = banco

    def connect(self):
        self.conn = mysql.connector.connect(host='192.168.22.9',database=self.banco,user='fabrica',password='fabrica@2022')
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


    def cadastro_usuario(self,endereco,pessoa,cuidador):
        self.connect()
        try:
            self.cursor.execute("""
                INSERT INTO endereco (cep,rua,numero,bairro,complemento,id_cidade) VALUES (%s,%s,%s,%s,%s,%s)
            """,(endereco[0],endereco[1],endereco[2],endereco[3],"",endereco[4]))

            id_endereco = self.cursor.lastrowid

            print(id_endereco)
            print(pessoa)

            self.cursor.execute("""
                INSERT INTO cuidador (parentesco,observacao,id_matricula) VALUES (%s,%s,%s)
            """,(cuidador[0],cuidador[1],cuidador[2]))

            id_cuidador = self.cursor.lastrowid
            print(id_cuidador)

            self.cursor.execute("""
                insert into pessoa (nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,data_cadastro,status,telefone,email,escolaridade,estado_civil,pessoa_Cdeficiencia,id_endereco,id_colaborador_resp)
                values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
             """,(pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],pessoa[5],pessoa[6],pessoa[7],pessoa[8],pessoa[9],pessoa[10],pessoa[11],pessoa[12],pessoa[13],id_endereco,id_cuidador))

            self.cursor.execute("""
                INSERT INTO usuario (nis,cns,observacao_,situacao_trabalho,tipo_transporte,tipo_tratamento,beneficio,id_beneficio,id_matricula_,id_beneficio,id_cuidador,id_clinica,id_curso) 
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,(cuidador[0],cuidador[1],cuidador[2],pessoa[3],pessoa[4],pessoa[5],pessoa[6],pessoa[7],pessoa[8],pessoa[9],id_cuidador,pessoa[10],pessoa[11]))

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
        
    def cadastro_colaborador(self,endereco,pessoa,colaborador):
        self.connect()
        try:
            args = (endereco[0],endereco[1],endereco[2],endereco[3])
            self.cursor.execute('INSERT INTO endereco(cep, logradouro, numero, bairro) VALUES (%s,%s,%s,%s)', args)
        
            id_endereco = self.cursor.lastrowid
            print('ID do endereco',id_endereco)

            args2 = (pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],pessoa[5],pessoa[6],pessoa[7],pessoa[8],pessoa[9],pessoa[10],pessoa[11],pessoa[12],id_endereco)
            self.cursor.execute('INSERT INTO pessoa(nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,data_cadastro,telefone,email,escolaridade,estado_civil,pessoa_deficiencia,id_endereco) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', args2)
            id_matricula = self.cursor.lastrowid
            print('id matricula',id_matricula)

            self.cursor.execute("""
                INSERT INTO colaborador (salario,data_admissao,pis,id_matricula,id_cargo) VALUES (%s,%s,%s,%s,%s)
            """,(colaborador[0],colaborador[1],colaborador[2],id_matricula,1))

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
    
            args2 = (curso[0],curso[1],curso[2],curso[3],curso[4])
            self.cursor.execute('INSERT INTO curso_evento (nome_curso_evento,data_inicio,data_fim,carga_horaria,id_palestrante) VALUES (%s,%s,%s,%s,%s)',args2)

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



