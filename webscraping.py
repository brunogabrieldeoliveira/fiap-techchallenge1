import requests
from bs4 import BeautifulSoup
import pandas as pd

# obtem dados   
def obtemDados(url): 
    response= requests.get(url)

    # verifica se requisição bem-sucedida
    response.raise_for_status()

    # parseia ao HTML da página usando o BeautifulSoup
    soup= BeautifulSoup(response.text, 'html.parser')

    # encontra a tabela específica pela classe
    table= soup.find('table', {'class': 'tb_base tb_dados'})

    # extrai as linhas da tabela
    rows= table.find_all('tr')

    # lista para armazenar os dados
    data= []

    # itera sobre as linhas e extrai o texto das células
    for row in rows:
        cells= row.find_all({'th', 'td'})
        cells_text= [cell.get_text(strip=True) for cell in cells]
        data.append(cells_text)

    # converte os dados em um Dataframe do pandas
    return pd.DataFrame(data[1:], columns=data[0]) # linha é o cabeçalho