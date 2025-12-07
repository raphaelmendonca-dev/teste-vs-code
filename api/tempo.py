from http.server import BaseHTTPRequestHandler
from datetime import datetime
import json
import requests  # Importando a biblioteca que pedimos no requirements.txt

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Vamos buscar o Dólar na API externa
        url = "https://economia.awesomeapi.com.br/last/USD-BRL"
        resposta_externa = requests.get(url)
        dados_dolar = resposta_externa.json()
        
        # O valor vem dentro de ['USDBRL']['bid']
        valor_dolar = dados_dolar['USDBRL']['bid']
        # Arredondando para ficar bonito (ex: 5.42)
        valor_formatado = f"R$ {float(valor_dolar):.2f}"
        
        # 2. Montar nossa resposta
        mensagem = {
            "saudacao": f"Dólar Agora: {valor_formatado}",
            "hora_servidor": datetime.now().strftime("%H:%M:%S")
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(mensagem).encode('utf-8'))
        return