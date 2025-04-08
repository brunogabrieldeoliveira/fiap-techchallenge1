import requests
from bs4 import BeautifulSoup
import pandas as pd
from db import obtemDataOffProducao, obtemDataOffProcessamento

# obtem dados   
def obtemDados(url): 
    response= requests.get(url)

    # verifica se requisição bem-sucedida
    response.raise_for_status()

    # retorna erro conexao
    if response.status_code != 200:
        return pd.DataFrame(), response.status_code

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
    return pd.DataFrame(data[1:], columns=data[0]), response.status_code 

def obtemProducao(ano):
    urls= {
        "producao" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_02"]
    }

    # dicionario de dados
    data= {}

    # itero sobre as urls da aba Produção
    for aba in urls:       
        url= urls[aba][0]   # obtenho a url        
        df, status_code= obtemDados(url) # obtenho dos dados da url

        # obtem dados online
        if status_code == 200:
            data[aba]= df.to_json(orient='records', indent=4) # guardo dados de todas as abas        

        # obtem dados offline
        else:            
            json, status_code= obtemDataOffProducao(aba, ano)    
            if status_code != 200:                
                return {"error": "dados não encontrados"}
            else:
                data[aba]= json
            
    return data

def obtemProcessamento(ano):
    urls= {
        "viniferas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_03&subopcao=subopt_01"],
        "americanas_hibridas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_03&subopcao=subopt_02"],
        #"uvas_mesa" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_03&subopcao=subopt_03"],
        #"sem_classificacao" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_03&subopcao=subopt_04"] 
    }

    # dicionario de dados
    data= {}

    # itero sobre as urls da aba processamento
    for aba in urls:       
        url= urls[aba][0]   # obtenho a url        
        df, status_code= obtemDados(url) # obtenho dos dados da url

        # obtem dados online
        if status_code == 200:
            data[aba]= df.to_json(orient='records', indent=4) # guardo dados de todas as abas        

        # obtem dados offline
        else:            
            json, status_code= obtemDataOffProcessamento(aba, ano)    
            if status_code != 200:                
                return {"error": "dados não encontrados"}
            else:
                data[aba]= json
            
    return data

def obtemComercializacao(ano):
    urls= {
        "producao" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_04"]
    }

    # dicionario de dados
    data= {}

    # itero sobre as urls da aba Comercializacao
    for aba in urls:       
        url= urls[aba][0]   # obtenho a url        
        df, status_code= obtemDados(url) # obtenho dos dados da url

        if status_code == 200:
            data[aba]= df.to_json(orient='records', indent=4) # guardo dados de todas as abas
        else:
            # obtem dados do banco
            data[aba]= {"error" : "teste"}

    return data

def obtemImportacao(ano):
    urls= {
        "vinhos_mesa" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_05&subopcao=subopt_01"],
		"espumantes" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_05&subopcao=subopt_02"],
		"uvas_frescas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_05&subopcao=subopt_03"],
		"uvas_passas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_05&subopcao=subopt_04"],
		"suco_uva" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_05&subopcao=subopt_05"]
    }

    # dicionario de dados
    data= {}

    # itero sobre as urls da aba Importacao
    for aba in urls:       
        url= urls[aba][0]   # obtenho a url        
        df, status_code= obtemDados(url) # obtenho dos dados da url

        if status_code == 200:
            data[aba]= df.to_json(orient='records', indent=4) # guardo dados de todas as abas
        else:
            # obtem dados do banco
            data[aba]= {"error" : "teste"}

    return data

def obtemExportacao(ano):
    urls= {
        "vinhos_mesa" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_06&subopcao=subopt_01"],
		"espumantes" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_06&subopcao=subopt_02"],
		"uvas_frescas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_06&subopcao=subopt_03"],
		"suco_uva" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_06&subopcao=subopt_04"]
    }

    # dicionario de dados
    data= {}

    # itero sobre as urls da aba Exportação
    for aba in urls:       
        url= urls[aba][0]   # obtenho a url        
        df, status_code= obtemDados(url) # obtenho dos dados da url

        if status_code == 200:
            data[aba]= df.to_json(orient='records', indent=4) # guardo dados de todas as abas
        else:
            # obtem dados do banco
            data[aba]= {"error" : "teste"}

    return data