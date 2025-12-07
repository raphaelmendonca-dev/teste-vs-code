from flask import Flask, jsonify
from datetime import datetime
import requests

# Criamos a aplicação Flask
app = Flask(__name__)

# Definimos a rota (o endereço que o JS vai chamar)
@app.route('/api/tempo')
def pegar_cotacao():
    # 1. Busca os dados externos (igual antes)
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    resposta = requests.get(url)
    valor_dolar = resposta.json()['USDBRL']['bid']
    
    # Formatação
    valor_formatado = f"R$ {float(valor_dolar):.2f}"
    hora_atual = datetime.now().strftime("%H:%M:%S")

    # 2. O Retorno Mágico
    # O jsonify transforma o dicionário em JSON e coloca os headers automaticamente!
    return jsonify({
        "saudacao": f"Dólar (via Flask): {valor_formatado}",
        "hora_servidor": hora_atual,
        "framework": "Flask 🌶️"
    })

# Esse comando final é necessário para o Vercel entender o app
if __name__ == '__main__':
    app.run()
