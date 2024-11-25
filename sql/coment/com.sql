/* Comentários de SQL Atualizado pela última vez: 2024-11-14 - Fonte: https://www.ibm.com/docs/pt-br/db2/12.1?topic=statements-sql-comments */
/* As instruções SQL estática podem incluir a linguagem do host ou os comentários de SQL. Instruções SQL dinâmicas podem incluir comentários SQL. */

/* Existem dois tipos de comentários SQL: comentários simples */
/* Os comentários simples são introduzidos por dois hífens consecutivos (--) e terminam com o fim da linha. comentários brackeados
/* Os comentários brackeados são introduzidos por / * e terminam com */.
/* Aplicam-se as seguintes regras para a utilização de comentários simples:
/* Os dois hífens devem estar na mesma linha e não devem ser separados por um espaço.
/* Os comentários simples podem ser iniciados onde quer que um espaço seja válido (exceto dentro de um token delimitador ou entre 'EXEC' e 'SQL ').
/* Comentários simples não podem ser continuados para a próxima linha.
/* Em COBOL, os hífens devem ser precedidos por um espaço.
/* Aplicam-se as seguintes regras para a utilização de comentários brados:
-- O / * deve estar na mesma linha e não deve ser separado por um espaço.
-- O */ deve estar na mesma linha e não deve ser separado por um espaço.
-- Os comentários brackeados podem ser iniciados onde quer que um espaço seja válido (exceto dentro de um token delimitador ou entre 'EXEC' e 'SQL ').
-- Os comentários brackeados podem ser continuados para as linhas subsequentes.

-- Exemplo 1: Este exemplo mostra como incluir comentários simples em uma instrução:
   
CREATE VIEW PRJ_MAXPER       -- PROJECTS WITH MOST SUPPORT PERSONNEL
     AS SELECT PROJNO, PROJNAME -- NUMBER AND NAME OF PROJECT
       FROM PROJECT
       WHERE DEPTNO = 'E21'     -- SYSTEMS SUPPORT DEPT CODE
       AND PRSTAFF > 1

-- Exemplo 2: Este exemplo mostra como incluir comentários brackeados em um comunicado:
   
CREATE VIEW PRJ_MAXPER       /* PROJECTS WITH MOST SUPPORT
                                     PERSONNEL                 */
     AS SELECT PROJNO, PROJNAME /* NUMBER AND NAME OF PROJECT  */
       FROM PROJECT
       WHERE DEPTNO = 'E21'     /* SYSTEMS SUPPORT DEPT CODE   */
       AND PRSTAFF > 1
