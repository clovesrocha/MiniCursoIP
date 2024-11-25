### Aqui está um exemplo prático do SQL para resolver parte do desafio proposto:
### Mentor_Prof_Cloves_Rocha :D Calma, que você vai conseguir... 
### Procedimento Armazenado: Atualização de Estoque Após Procedimento Médico
Este procedimento reduz a quantidade de medicamento em estoque após a realização de um procedimento médico.

```sql
DELIMITER //

CREATE PROCEDURE AtualizarEstoqueMedico(
    IN medicamento_id INT,
    IN quantidade_utilizada INT
)
BEGIN
    -- Verifica se o estoque é suficiente
    DECLARE estoque_atual INT;

    SELECT quantidade
    INTO estoque_atual
    FROM estoque
    WHERE id = medicamento_id;

    IF estoque_atual < quantidade_utilizada THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Estoque insuficiente para o procedimento';
    ELSE
        -- Atualiza o estoque
        UPDATE estoque
        SET quantidade = quantidade - quantidade_utilizada
        WHERE id = medicamento_id;
    END IF;
END;

//
DELIMITER ;
```

### Gatilho: Notificação para Reposição de Medicamentos
Este gatilho insere uma notificação quando o estoque de medicamentos está abaixo de um limite definido.

```sql
DELIMITER //

CREATE TRIGGER NotificarReposicaoEstoque
AFTER UPDATE ON estoque
FOR EACH ROW
BEGIN
    IF NEW.quantidade < 10 THEN
        INSERT INTO notificacoes (mensagem, data_notificacao)
        VALUES (
            CONCAT('Atenção: O estoque do medicamento ID ', NEW.id, ' está baixo.'),
            NOW()
        );
    END IF;
END;

//
DELIMITER ;
```

### Segurança e Controle de Acesso
#### Estratégias Adotadas:
1. **Criação de Usuários e Permissões**:
   Controlar o acesso por meio de roles específicas com permissões mínimas necessárias.

```sql
-- Criação de usuários com privilégios restritos
CREATE USER 'medico'@'%' IDENTIFIED BY 'senha_secreta';
CREATE USER 'farmaceutico'@'%' IDENTIFIED BY 'senha_secreta';

-- Permissões específicas
GRANT SELECT, INSERT, UPDATE ON banco_de_dados.pacientes TO 'medico'@'%';
GRANT SELECT, UPDATE ON banco_de_dados.estoque TO 'farmaceutico'@'%';
```

2. **Mascaramento de Dados Sensíveis**:
   Utilizar mascaramento para proteger informações pessoais.

```sql
-- Exemplo de mascaramento de dados
CREATE VIEW PacientesAnonimizados AS
SELECT
    id,
    CONCAT(SUBSTRING(nome, 1, 2), '*****') AS nome,
    SUBSTRING(cpf, 1, 3) AS cpf_parcial,
    data_nascimento,
    '******' AS historico_medico
FROM pacientes;
```

3. **Auditoria de Acessos**:
   Implementar tabelas de log para registrar todas as ações sensíveis no banco de dados.

```sql
CREATE TABLE log_acessos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50),
    acao VARCHAR(100),
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Exemplo de trigger para registrar ações
DELIMITER //

CREATE TRIGGER LogAcessoPaciente
AFTER SELECT ON pacientes
FOR EACH ROW
BEGIN
    INSERT INTO log_acessos (usuario, acao)
    VALUES (USER(), 'Consulta ao paciente ID ' || NEW.id);
END;

//
DELIMITER ;
```

### Essas soluções integram automação, notificação, e segurança de dados no sistema, atendendo os requisitos do desafio.
