from flask import Flask
from webscraping import obtemDados

app = Flask(__name__)
# flask --app .\app.py run --debug

# producao
@app.route("/producao", methods=['GET'])
def obtemProducao():
    return obtemDados("http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02").to_json(orient='records', indent=4)

# processamento
@app.route("/processamento", methods=['GET'])
def obtemProcessamento():
    return obtemDados("http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02").to_json(orient='records', indent=4)

# comercializacao
@app.route("/comercializacao", methods=['GET'])
def obtemComercializacao():
    return obtemDados("http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02").to_json(orient='records', indent=4)

# importacao
@app.route("/importacao", methods=['GET'])
def obtemImportacao():
    return obtemDados("http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02").to_json(orient='records', indent=4)

# exportacao
@app.route("/exportacao", methods=['GET'])
def obtemExportacao():
    return obtemDados("http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02").to_json(orient='records', indent=4)


