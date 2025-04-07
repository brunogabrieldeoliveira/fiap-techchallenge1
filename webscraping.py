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

def obtemProducao(ano):
    urls= {
        #"producao" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02"]
        "producao" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_02"]
    }

    # dicionario de dados
    data= {}

    # itero sobre as urls da aba processamento
    for aba in urls:       
        url= urls[aba][0]   # obtenho a url        
        df= obtemDados(url) # obtenho dos dados da url

        data[aba]= df.to_json(orient='records', indent=4) # guardo dados de todas as abas

    return data

def obtemProcessamento(ano):
    urls= {
        #"viniferas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_03"],        
		#"americanas_hibridas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_03"],
		#"uvas_mesa" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_03"],
		#"sem_classificacao" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_03"]
        "viniferas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_03&subopcao=subopt_01"],
        "americanas_hibridas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_03&subopcao=subopt_02"],
        "uvas_mesa" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_03&subopcao=subopt_03"],
        "sem_classificacao" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_03&subopcao=subopt_04"] 

    }

    # dicionario de dados
    data= {}

    # itero sobre as urls da aba processamento
    for aba in urls:       
        url= urls[aba][0]   # obtenho a url        
        df= obtemDados(url) # obtenho dos dados da url

        data[aba]= df.to_json(orient='records', indent=4) # guardo dados em formato json de todas as abas
    
    return data

def obtemComercializacao(ano):
    urls= {
        #"producao" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04"]
        "producao" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_04"]
    }

    # dicionario de dados
    data= {}

    # itero sobre as urls da aba processamento
    for aba in urls:       
        url= urls[aba][0]   # obtenho a url        
        df= obtemDados(url) # obtenho dos dados da url

        data[aba]= df.to_json(orient='records', indent=4) # guardo dados em formato json de todas as abas
    
    return data

def obtemImportacao(ano):
    urls= {
		#"vinhos_mesa" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_05"],
		#"espumantes" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_05"],
		#"uvas_frescas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_05"],
		#"uvas_passas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_05"],
		#"suco_uva" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_05&opcao=opt_05"]

        "vinhos_mesa" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_05&subopcao=subopt_01"],
		"espumantes" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_05&subopcao=subopt_02"],
		"uvas_frescas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_05&subopcao=subopt_03"],
		"uvas_passas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_05&subopcao=subopt_04"],
		"suco_uva" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_05&subopcao=subopt_05"]
    }

    # dicionario de dados
    data= {}

    # itero sobre as urls da aba processamento
    for aba in urls:       
        url= urls[aba][0]   # obtenho a url        
        df= obtemDados(url) # obtenho dos dados da url

        data[aba]= df.to_json(orient='records', indent=4) # guardo dados em formato json de todas as abas
    
    return data

def obtemExportacao(ano):
    urls= {
		#"vinhos_mesa" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_06"],
		#"espumantes" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_06"],
		#"uvas_frescas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_06"],
		#"suco_uva" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_06"]

        "vinhos_mesa" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_06&subopcao=subopt_01"],
		"espumantes" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_06&subopcao=subopt_02"],
		"uvas_frescas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_06&subopcao=subopt_03"],
		"suco_uva" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_06&subopcao=subopt_04"]
    }

    # dicionario de dados
    data= {}

    # itero sobre as urls da aba processamento
    for aba in urls:       
        url= urls[aba][0]   # obtenho a url        
        df= obtemDados(url) # obtenho dos dados da url

        data[aba]= df.to_json(orient='records', indent=4) # guardo dados em formato json de todas as abas
    
    return data