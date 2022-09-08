     Informações sobre o projeto
 *Premissas assumidas
- Para realizar o projeto foi utilizado Python(FLASK), Bootstrap, HTML, CSS e MySql(PHPMyadmin).
- O Flask foi utilizado para criar a API e a Criação/Integração com o Banco de dados(flask_sqlalchemy e mysqlconnector).
- O Mysql foi o banco de dados utilizado por sua facilidade de uso e fácil compatibilidade com  o Flask.
- A interface foi estruturada em HTML, o estilo foi feito com Bootstrap e CSS.

 *Instruções pra executar o sistema

  Instalações e Bibliotecas usadas/necessárias
Bibliotecas
- Flask
- flask_sqlalchemy
- mysql.connector
- request
- DateTime
- SQLAlchemy
- SQLAlchemy-Utils

*Instalações
- MySql 
- obs: caso tenha o xampp na máquina não é necessário instalar, apenas inicar o banco, acessando o painel)

*Passo a Passo
- Após clonar o repositório em sua máquina.
- Acesse e ative o banco de dados MySQL para que seja criado em sua máquina(banco utilizado PHPMyadmin).
- Acesse a página config.py e prepara_banco.py e altere os dados de acesso ao banco de dados do seu usuário.
- Dê um deploy na aba prepara_banco.py para que o banco de dados seja criado com sucesso.
- Acesso a página app.py e incia a API.

 *Sobre as pastas
 - API = onde roda a api e inicia o projeto
 - CONFIG = todas as configurações do projeto e do banco de dados, onde também tem as informações de acesso ao banco.
 - VIEWS = onde ficam as rotas da API
 - PREPARA_BANCO = código que cria o banco de dados e insere as primeiras informações
 - MODELS = modelos das tabelas do banco de dados.
 
 ![alt text](https://github.com/vitoriadaamasceno/novo_lembrete/blob/main/interface.png)
