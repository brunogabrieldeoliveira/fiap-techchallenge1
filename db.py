import pandas as pd

# aba produção
def obtemDataOffProducao(aba, ano):  
    if aba == "producao":
        df= pd.read_csv("data_offline/" + aba + ".csv", sep=";")
        return df[['produto', str(ano)]].to_json(orient='records', indent=4), 200   
    
    return 404 # Not Found

#data= obtemDataOffProducao("producao", 2023)
#print(data)

# aba processamento
def obtemDataOffProcessamento(aba, ano):  
    print("data_offline/processamento/" + aba + ".csv")
    df= pd.read_csv("data_offline/processamento/" + aba + ".csv", sep=";", encoding='unicode_escape')
    print(df.head())
    if len(df[str(ano)].unique()) > 0:
        
        # viniferas
        if aba == "viniferas":
            return df[['cultivar', str(ano)]].to_json(orient='records', indent=4), 200
        
        # americanas hibridas
        if aba == "americanas_hibridas":
            return df[['cultivar', str(ano)]].to_json(orient='records', indent=4), 200
        
    return 404 # Not Found
    
#data= obtemDataOffProcessamento("americanas_hibridas", 2023)
#print(data)
