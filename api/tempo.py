from http.server import BaseHTTPRequestHandler
from datetime import datetime
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Pega a hora atual
        agora = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        
        # Cria uma resposta simples
        mensagem = {
            "saudacao": "Olá do Python!",
            "hora_servidor": agora,
            "linguagem": "Python 3"
        }
        
        # Prepara para enviar de volta ao navegador
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Envia a mensagem convertida para texto (JSON)
        self.wfile.write(json.dumps(mensagem).encode('utf-8'))
        return