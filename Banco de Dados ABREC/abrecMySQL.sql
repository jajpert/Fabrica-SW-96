use abrec;

desc pessoa;
alter table pessoa
drop column pessoa_cdeficiencia;

alter table pessoa
add column tipo_deficiencia varchar (45) after deficiencia;

/*CREATE TABLE IF NOT EXISTS `abrec`.`pessoa` (
  `id_pessoa` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `cpf` CHAR(11) NOT NULL UNIQUE,
  `rg` CHAR(10) NOT NULL,
  `data_emissao` DATE NOT NULL,
  `orgao_exp` VARCHAR(45) NOT NULL,
  `sexo` ENUM('F', 'M', 'O') NOT NULL,
  `data_cadastro` DATE NOT NULL,
  `status` CHAR(1) NOT NULL,
  `telefone` CHAR(11) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `formacao` VARCHAR(60) NOT NULL,
  `idendereco` INT NOT NULL,
  `id_colaborador_resp` INT NOT NULL,
  PRIMARY KEY (`id_pessoa`))*/
  
  desc endereco;
  alter table colaborador
  add pis char  (11) after matricula;
  
  
 
  alter table usuario
  modify observacao_sigilosa text after observacao;
 
  desc usuario;
  desc cargo;
  
  alter table cargo
  modify salario float;
  
  select *from clinica;
  
  desc usuario;  
 
  /*add tipo_curso_evento varchar(45) after nome_curso_evento,
  add status char(1) after tipo_curso_evento,
  add responsavel varchar(45) after status,
  add dias_aulas varchar (45) after data_fim,
  add horario_inicio date after dias_aulas,
  add periodo varchar (45),
  add vagas int,
  add id_endereco int not null,
  add descricao_atividade text;*/
  
	alter table medicamento
  add id_produto int after id_medicamento,
  add classificacao varchar (45) after id_produto,
  add observacao text after classificacao;
  
  
  create table produto(
  id_produto int not null primary key auto_increment,
  descricao varchar (100) not null,
  unidade_medida varchar(45) not null,
  quantidade int not null,
  lote varchar (45),
  fabricacao date,
  validade date );
  
create table fornecedor (
id_fornecedor int not null primary key auto_increment,
cnpj char (14) not null unique,
razao_social varchar (100) not null,
nome_fantasia varchar (100),
id_pessoa int);

drop table retirada;


create table retirada (
id_retirada int not null primary key auto_increment,
data_retirada datetime,
observacao text,
id_colaborador int,
id_medicamento int,
id_cuidador int,
id_usuario int,
id_saida_produto int);



  
  
  
  
  
  
  