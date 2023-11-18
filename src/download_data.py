import pandas as pd
from datetime import datetime 

# Downloading data from IPEADATA
url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'

# Reading data from IPEADATA
df = pd.read_html(url, decimal=',', thousands='.')[2]

# Renaming columns
df.columns = ['Data', 'Preço - petróleo bruto - Brent (FOB)']

#drop first line
df = df.drop(df.index[0])

# Changing data type
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
df['Preço - petróleo bruto - Brent (FOB)'] = df['Preço - petróleo bruto - Brent (FOB)'].astype(float)

# file name with date
file_name = f'ipeadata{datetime.now().strftime("%Y%m%d")}.csv'

# Saving data to CSV and drop header
df.to_csv(f'data/{file_name}', index=False, sep=';', encoding='latin-1')

# subscrever o ultimo arquivo com os dados atualizados
df.to_csv('data/ipeadata_last.csv', index=False, sep=';', encoding='latin-1')

# Report
print(f'Localização do arquivo: data/{file_name}')
print('Quantidade de linhas: ', df.shape[0])
print('Primeira data: ', df['Data'].min().strftime('%d/%m/%Y'))
print('Última data: ', df['Data'].max().strftime('%d/%m/%Y'))