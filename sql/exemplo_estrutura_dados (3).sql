CREATE TABLE `usuario` (
  `cpf` interger PRIMARY KEY,
  `nome` varchar(255),
  `sobrenome` varchar(255),
  `idade` interger
);

CREATE TABLE `cadastro_pj` (
  `cnpj` interger PRIMARY KEY,
  `nome` varchar(255),
  `descricao` varchar(255),
  `tipoatividade` varchar(255)
);

CREATE TABLE `produto` (
  `id` interger PRIMARY KEY,
  `nome` varchar(255),
  `descricao` varchar(255)
);

ALTER TABLE `cadastro_pj` ADD FOREIGN KEY (`cnpj`) REFERENCES `usuario` (`cpf`);

ALTER TABLE `produto` ADD FOREIGN KEY (`id`) REFERENCES `cadastro_pj` (`cnpj`);
