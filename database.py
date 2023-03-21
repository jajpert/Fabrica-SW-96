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
            print(result)
           # return result
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


    def cadastro_usuario(self,endereco, pessoa, usuario):
        self.connect()
        try:
            
            args = (endereco[0],endereco[1],endereco[2],endereco[3])
            self.cursor.execute('INSERT INTO endereco(cep, logradouro, numero, bairro) VALUES (%s,%s,%s,%s)', args)
        
            id_endereco = self.cursor.lastrowid


            args2 = (pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],pessoa[5],pessoa[6],pessoa[7],pessoa[8],pessoa[9],pessoa[10],id_endereco,pessoa[11])
            self.cursor.execute('INSERT INTO pessoa(nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,telefone,email,escolaridade,pessoa_deficiencia,id_endereco,id_colaborador_resp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', args2)
            id_matricula = self.cursor.lastrowid
            

            args3 = (usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5],usuario[6], id_matricula)
            self.cursor.execute('INSERT INTO usuario(data_inclusao, nis, cns, situacao_trabalho, tipo_transporte, tipo_tratamento, beneficio, id_matricula) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', args3)

            self.conn.commit()
            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            #print(err)
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def atualiza_usuario(self,tupla_de_dados):
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
    
