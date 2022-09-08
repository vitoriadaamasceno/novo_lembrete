import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `dti`;")

cursor.execute("CREATE DATABASE `dti`;")

cursor.execute("USE `dti`;")

# criando tabelas
TABLES = {}
TABLES['Lembrete'] = ('''
      CREATE TABLE `lembrete` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `data` date NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')


# inserindo lembrete
lembrete_sql = 'INSERT INTO lembrete (nome, data) VALUES (%s, %s)'
lembretes = [
      ("Festa","17/09/2022")
      
]
cursor.executemany(lembrete_sql, lembretes)

cursor.execute('select * from dti.lembrete')
print(' -------------  Lembretes:  -------------')
for lembrete in cursor.fetchall():
    print(lembrete[1])

# commitando caso não nada tenha defeito
conn.commit()

cursor.close()
conn.close()