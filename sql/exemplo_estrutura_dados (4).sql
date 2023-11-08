CREATE TABLE [usuarios] (
  [cpf] interger PRIMARY KEY,
  [nome] nvarchar(255),
  [sobrenome] nvarchar(255),
  [idade] interger
)
GO

CREATE TABLE [cadastro_pj] (
  [cnpj] interger PRIMARY KEY,
  [nome] nvarchar(255),
  [descricao] nvarchar(255),
  [tipoatividade] nvarchar(255)
)
GO

CREATE TABLE [produto] (
  [id] interger PRIMARY KEY,
  [nome] nvarchar(255),
  [descricao] nvarchar(255)
)
GO

CREATE TABLE [user] (
  [id] int,
  [country_code] int
)
GO

CREATE TABLE [account] (
  [user_id] int,
  [country_code] int
)
GO

ALTER TABLE [produto] ADD FOREIGN KEY ([id]) REFERENCES [usuarios] ([cpf])
GO

ALTER TABLE [cadastro_pj] ADD FOREIGN KEY ([cnpj]) REFERENCES [produto] ([id])
GO

ALTER TABLE [user] ADD FOREIGN KEY ([id]) REFERENCES [account] ([user_id])
GO

ALTER TABLE [account] ADD FOREIGN KEY ([country_code]) REFERENCES [user] ([country_code])
GO
