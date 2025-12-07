from flask import Flask, jsonify
from datetime import datetime
import requests
from bs4 import BeautifulSoup  # Importando a ferramenta de raspagem

app = Flask(__name__)

# Rota 1: Dólar (Mantivemos a antiga)
@app.route('/api/tempo')
def pegar_cotacao():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    resposta = requests.get(url)
    valor_dolar = resposta.json()['USDBRL']['bid']
    return jsonify({
        "saudacao": f"Dólar: R$ {float(valor_dolar):.2f}",
        "hora_servidor": datetime.now().strftime("%H:%M:%S")
    })

# Rota 2: Web Scraping (NOVA!)
@app.route('/api/wiki')
def raspar_wikipedia():
    # Vamos acessar a página sobre Inteligência Artificial
    url_alvo = "https://pt.wikipedia.org/wiki/Inteligência_artificial"
    
    # 1. O requests baixa o HTML inteiro do site
    resposta = requests.get(url_alvo)
    
    # 2. O BeautifulSoup organiza a bagunça
    soup = BeautifulSoup(resposta.content, 'html.parser')
    
    # 3. Procuramos o título principal (tag <h1>) e pegamos o texto dele
    titulo_pagina = soup.find('h1').get_text()
    
    # 4. Procuramos o primeiro parágrafo (o primeiro <p> depois do título)
    # (Isso é um pouco mais técnico, pegamos o primeiro parágrafo de conteúdo)
    paragrafo = soup.find('div', {'class': 'mw-parser-output'}).find('p', class_=None).get_text()
    
    # Retornamos para o seu site
    return jsonify({
        "titulo_encontrado": titulo_pagina,
        "resumo": paragrafo[:150] + "..." # Pegamos só os primeiros 150 caracteres
    })

if __name__ == '__main__':
    app.run()