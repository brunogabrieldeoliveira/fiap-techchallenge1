from flask import Flask, jsonify
from webscraping import obtemDados, obtemProducao, obtemProcessamento, obtemComercializacao, obtemImportacao, obtemExportacao

# flask --app .\app.py run --debug
app = Flask(__name__)

# producao ok
@app.route("/producao", methods=['GET'])
def producao():
    return obtemProducao()

# processamento
@app.route("/processamento", methods=['GET'])
def processamento():
    return obtemProcessamento()

# comercializacao ok
@app.route("/comercializacao", methods=['GET'])
def comercializacao():
    return obtemComercializacao()

# importacao
@app.route("/importacao", methods=['GET'])
def importacao():
    return obtemImportacao()

# exportacao
@app.route("/exportacao", methods=['GET'])
def exportacao():
    return obtemExportacao()


