Definição do que é?

DEFINIÇÃO:

Sistema de gestão que faz a intregração de inicialmente 3 modulos:

 => ESTOQUE
 => COMPRAS
 => FINANCEIRO  

Documentação do processo de criação na tela de login.

Organize oque terá no seu menu de entrada.

- input de login

------------------------
        login
------------------------

- input de senha

------------------------
        senha
------------------------

faça as camadas de proteção.

--- para não confundir eu criei funções distintas def verifica_senha, def verifica_email --- 

Especificação de camadas teste // Projetando arquitetura de filtros. 

1° proteção de borda - failfast (nulos, vazios, espaços)

2° proteção de negocio(contém arroba, se é maior que 50)

3° permitir acesso ao core da aplicação (até que os dados estiverem seguros)

Modelagem de dados:

+ armazenar usuario em dicionario e analisar duplicaras (em andamento...)

