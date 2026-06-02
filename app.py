from flask import Flask, jsonify
import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

# Configuração do Key Vault
KV_URL = os.environ.get("AZURE_KEYVAULT_RESOURCEENDPOINT")
credential = DefaultAzureCredential()

@app.route('/')
def home():
    return {
        "status": "Online",
        "projeto": "OrbitalWatch",
        "equipe": "Nome dos Integrantes aqui",
        "ODS": "9 - Indústria, Inovação e Infraestrutura"
    }

@app.route('/alertas')
def alertas():
    # Simulação de dados de telemetria espacial
    return jsonify([
        {"id": 1, "objeto": "Debris-A1", "risco": "Alto", "distancia_km": 12.5},
        {"id": 2, "objeto": "Starlink-12", "risco": "Baixo", "distancia_km": 450.2}
    ])

if __name__ == '__main__':
    app.run()