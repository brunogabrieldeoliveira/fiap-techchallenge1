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

# timeout cache
timeout= 300

# producao ok
@app.route("/producao", methods=['GET'])
@cache.cached()
def producao():
    return obtemProducao()

# processamento
@app.route("/processamento", methods=['GET'])
@cache.cached()
def processamento():
    return obtemProcessamento()

# comercializacao ok
@app.route("/comercializacao", methods=['GET'])
@cache.cached()
def comercializacao():
    return obtemComercializacao()

# importacao
@app.route("/importacao", methods=['GET'])
@cache.cached()
def importacao():
    return obtemImportacao()

# exportacao
@app.route("/exportacao", methods=['GET'])
@cache.cached()
def exportacao():
    return obtemExportacao()


