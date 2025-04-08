from flask import Flask, jsonify
from flask_caching import Cache
from webscraping import obtemDados, obtemProducao, obtemProcessamento, obtemComercializacao, obtemImportacao, obtemExportacao

# define configurações do cache
config = {
    "DEBUG": True,                  # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",    # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300    # timeout padrao
}

# flask --app .\app.py run --debug
app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

# producao ok
@app.route("/producao/ano=<ano>", methods=['GET'])
@cache.cached()
def producao(ano):
    return obtemProducao(ano)

# processamento
@app.route("/processamento/ano=<ano>", methods=['GET'])
@cache.cached()
def processamento(ano):
    return obtemProcessamento(ano)

# comercializacao ok
@app.route("/comercializacao/ano=<ano>", methods=['GET'])
@cache.cached()
def comercializacao(ano):
    return obtemComercializacao(ano)

# importacao
@app.route("/importacao/ano=<ano>", methods=['GET'])
@cache.cached()
def importacao(ano):
    return obtemImportacao(ano)

# exportacao
@app.route("/exportacao/ano=<ano>", methods=['GET'])
@cache.cached()
def exportacao(ano):
    return obtemExportacao(ano)