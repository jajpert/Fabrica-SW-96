use abrec;
show tables;

desc cidade;
desc pessoa;
desc usuario;
desc endereco;
desc colaborador;


alter table pessoa
add column pessoa_cdeficiencia tinyint (1) not null after email;

alter table colaborador
drop column matricula;

show tables;

select * from pessoa;

desc cuidador;





