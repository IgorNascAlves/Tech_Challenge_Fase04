#carregar dados csv deentro do banco de dados mysql
import csv
import mysql.connector
import os
from dotenv import load_dotenv

def carrega_conexao():
    load_dotenv()
    env = os.environ

    # Connect to MySQL server
    localhost = env.get('MYSQL_HOST')
    user = env.get('MYSQL_USER')
    password = env.get('MYSQL_PASSWORD')

    conexao = mysql.connector.connect(user=user, password=password, host=localhost)
    return conexao

#Data;Pre�o - petr�leo bruto - Brent (FOB)
# 2024-01-16;80.15
# 2024-01-15;79.76

def le_csv(arquivo):
    with open(arquivo, 'r') as f:
        leitor = csv.reader(f, delimiter=';')
        # next(leitor)
        dados = []
        for linha in leitor:
            data = linha[0]
            preco = float(linha[1])
            dados.append((data, preco))
        return dados

def cria_tabela_db(conexao):
    cursor = conexao.cursor()
    #create db fase4_petroleo
    cursor.execute('CREATE DATABASE IF NOT EXISTS fase4_petroleo')
    #usa o db fase4_petroleo
    cursor.execute('USE fase4_petroleo')
    cursor.execute('DROP TABLE IF EXISTS petroleo')
    cursor.execute('CREATE TABLE petroleo (data DATE, preco FLOAT)')
    cursor.close()

def insere_dados(conexao, dados):
    cursor = conexao.cursor()
    cursor.executemany('INSERT INTO petroleo (data, preco) VALUES (%s, %s)', dados)
    conexao.commit()
    cursor.close()

def main():
    conexao = carrega_conexao()
    path = 'data\ipeadata_last.csv'
    dados = le_csv(path)
    cria_tabela_db(conexao)
    insere_dados(conexao, dados)
    conexao.close()

if __name__ == '__main__':
    main()
