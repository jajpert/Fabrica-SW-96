import mysql.connector

class DataBase():
    def __init__(self, banco = "abrec") -> None:
        self.banco = banco

    def connect(self):
        ##self.conn = mysql.connector.connect(host='localhost',database='abrec2',user='root',password='3545')
        self.conn = mysql.connector.connect(host='192.168.22.9',database=self.banco,user='fabrica',password='fabrica@2022')
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado ao Servidor de Banco de Dados: ", db_info)
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

    def busca_cuidador(self, nome, cpf):
        print("entrei")
        self.connect()
        try:
            
            self.cursor.execute(f"""
                select p.id_matricula, nome, cpf, rg, data_emissao, orgao_exp,
                    sexo, parentesco, telefone, email, cep, logradouro,
                    numero, bairro, nome_cidade, sigla from pessoa p
                left join endereco e on p.id_endereco = e.id_endereco 
                left join cuidador c on p.id_matricula = c.id_matricula
                left join cidade c2 on e.id_cidade = c2.id_cidade
                left join estado e2 on c2.id_estado = e2.id_estado
                where nome like '{nome}' or cpf like '{cpf}' """)
            result = self.cursor.fetchall()
            
            #verifica os dados do select
            # for linha in result:
            #     print(linha)
            
            return result[0]
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()

    
    def busca_usuario(self, nome, cpf):
        print("entrei")
        self.connect()
        try:
            
            self.cursor.execute(f"""
                select p.id_matricula, nome, cpf, rg, data_emissao, orgao_exp,
                    sexo, parentesco, telefone, email, cep, logradouro,
                    numero, bairro, cidade, sigla from pessoa p
                left join endereco e on p.id_endereco = e.id_endereco 
                left join cuidador c on p.id_matricula = c.id_matricula
                left join cidade c2 on e.id_cidade = c2.id_cidade
                left join estado e2 on c2.id_estado = e2.id_estado
                where nome like '{nome}' or cpf like '{cpf}' """)
            result = self.cursor.fetchall()
            
            #verifica os dados do select
            # for linha in result:
            #     print(linha)
            
            return result[0]
        except Exception as err:
            return "ERRO",str(err)

        finally:
            self.close_connection()


    def cadastro_usuario(self,endereco,pessoa,usuario,cuidador):
        self.connect()
        try:
            args = (endereco[0],endereco[1],endereco[2],endereco[3],endereco[4],endereco[5])
            self.cursor.execute('INSERT INTO endereco(cep,logradouro,numero,bairro,cidade,estado) VALUES (%s,%s,%s,%s,%s,%s)', args)
            id_endereco = self.cursor.lastrowid

            print(endereco)
            print(id_endereco)
            print(pessoa)

            '''self.cursor.execute("""
                INSERT INTO cuidador (parentesco,observacao,id_matricula) VALUES (%s,%s,%s)
            """,(cuidador[0],cuidador[1],cuidador[2]))

            id_cuidador = self.cursor.lastrowid
            print(id_cuidador)'''
            print(len(usuario))
            print(len(pessoa))

            self.cursor.execute("""
                insert into pessoa (nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status,telefone,email,escolaridade,estado_civil,pessoa_deficiencia,id_endereco,id_colaborador_resp)
                values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
             """,(pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],pessoa[5],pessoa[6],pessoa[7],pessoa[8],pessoa[9],pessoa[10],pessoa[11],pessoa[12],id_endereco,pessoa[13]))
            id_matricula = self.cursor.lastrowid
            print(id_matricula)

            self.cursor.execute("""
                INSERT INTO usuario (nis,cns,observacao,situacao_trabalho,tipo_transporte,tipo_tratamento,beneficio,local_tratamento,periodo,data_inicio,patologia_base,tarifa_social,media_renda_familiar,vale_transporte,id_matricula,id_beneficio,id_clinica,id_curso) 
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
            """,(usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5],usuario[6],usuario[7],usuario[8],usuario[9],usuario[10],usuario[11],usuario[12],usuario[13],id_matricula,1,1,1))

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
            args = (endereco[0],endereco[1],endereco[2],endereco[3],endereco[4],endereco[5])
            self.cursor.execute('INSERT INTO endereco(cep,logradouro,numero,bairro,cidade,estado) VALUES (%s,%s,%s,%s,%s,%s)', args)
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

            args2 = (pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],pessoa[5],pessoa[6],pessoa[7],pessoa[8],pessoa[9],pessoa[10],pessoa[11],pessoa[12],pessoa[13],id_endereco)
            self.cursor.execute('INSERT INTO pessoa(nome,data_nascimento,cpf,rg,data_emissao,orgao_exp,sexo,status_,data_cadastro,telefone,email,escolaridade,estado_civil,pessoa_deficiencia,id_endereco) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', args2)
            id_matricula = self.cursor.lastrowid
            print('id matricula',id_matricula)

            self.cursor.execute("""
                INSERT INTO colaborador (pis,data_admissao,salario,cargo,periodo,login,senha,perfil,descricao_cargo,id_matricula) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,(colaborador[0],colaborador[1],colaborador[2],colaborador[3],colaborador[4],colaborador[5],colaborador[6],colaborador[7],colaborador[8],id_matricula))
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




    def SalvarFotoBanco(FilePath,self):
        #Função onde o usuario consegue selecionar o File
        with open (FilePath,"rb") as File:

            #Cria uma função onde escreve o arquivo como binario
            BinaryData = File.read()

        #Função Criada para dar Insert da imagem dentro da tabela desejada 
        SQlStatement = "INSERT INTO imagem_save (imagem) values (%s)"
        
        #Função onde ele executa as duas funções *BinaryData, SQLStatement* e adiciona dentro do banco de dados
        self.cursor.execute(SQlStatement, (BinaryData, ))
        db.commit()



    def PuxarFotoBanco(id,self):

        #Função criada para dar select na tabela selecionada buscando a imagem pelo id selecionado/inserido
        SQLStatement2 = "SELECT * FROM imagem_save WHERE id = '{0}'"
        
        #Executa o select da tabela selecionada e puxa o arquivo com base no id solicitado pelo usuario
        self.cursor.execute(SQLStatement2.format(str(id)))
        
        #Retorna uma unica sequencia por padrão, a tupla retornada consiste em dados retornados pelo servidor MySQL, convertidos em objetos Python
        MyResult = self.cursor.fetchone()[1]
        
        #Função em q salva a imagem com o nome de capture{id}.png, onde o id em q a imagem consta é alterado no nome do arquivo
        StoreFilePath = "capture{0}.png".format(str(id))
        
        #Mostra o numero binario da imagem
        print(MyResult)
        
        #Salva a imagem com o nome inserido na função StoreFilePath *capture{id}.png* para poder ser visualizada
        with open(StoreFilePath, "wb") as File:
            File.write(MyResult)
            File.close()

if __name__ == "__main__":
    db = DataBase()
    db.connect()
    db.close_connection()

