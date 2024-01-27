import pandas as pd
from datetime import datetime


def salva_dados(df, file_name):

    # Saving data to CSV and drop header
    df.to_csv(f'data/{file_name}', index=False, sep=';', encoding='latin-1')

    # subscrever o ultimo arquivo com os dados atualizados
    df.to_csv('data/ipeadata_last.csv', index=False, sep=';', encoding='latin-1', header=False)

def carrega_dados(url, nome_colunas):
    # Reading data from IPEADATA
    df = pd.read_html(url, decimal=',', thousands='.')[2]

    # Renaming columns
    df.columns = nome_colunas   

    #drop first line
    df = df.drop(df.index[0])

    # Changing data type
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
    df['Preço - petróleo bruto - Brent (FOB)'] = df['Preço - petróleo bruto - Brent (FOB)'].astype(float)

    return df

def info(df, file_name):
    # Report
    print(f'Localização do arquivo: data/{file_name}')
    print('Quantidade de linhas: ', df.shape[0])
    print('Primeira data: ', df['Data'].min().strftime('%d/%m/%Y'))
    print('Última data: ', df['Data'].max().strftime('%d/%m/%Y'))


def main():
    # Downloading data from IPEADATA
    url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'
    nome_colunas = ['Data', 'Preço - petróleo bruto - Brent (FOB)']
    # file name with date
    file_name = f'ipeadata{datetime.now().strftime("%Y%m%d")}.csv'

    df = carrega_dados(url, nome_colunas)
    salva_dados(df, file_name)
    info(df, file_name)

if __name__ == '__main__':
    main()


