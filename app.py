import os
from flask import Flask, jsonify
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

# URL do seu Key Vault (Substitua pelo seu nome de cofre)
KV_URL = "https://kv-orbitalwatch-551624.vault.azure.net/"

# O DefaultAzureCredential usa a Identidade Gerenciada do App Service automaticamente
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KV_URL, credential=credential)

@app.route('/')
def home():
    try:
        # Busca o segredo de forma segura no cofre, sem ter a senha no código!
        secret_value = client.get_secret("ApiKeyEspacial").value
        status_vault = "Conectado e Seguro"
    except Exception as e:
        secret_value = "Erro ao acessar cofre"
        status_vault = f"Erro: {str(e)}"

    return jsonify({
        "projeto": "OrbitalWatch - Monitoramento de Detritos",
        "seguranca": {
            "protocolo": "HTTPS/TLS",
            "autenticacao": "Managed Identity (Sem senhas no código)",
            "key_vault_status": status_vault
        },
        "ods_vinculada": "ODS 9 - Indústria, Inovação e Infraestrutura",
        "api_key_resgatada": secret_value # Isso prova que o código buscou no cofre!
    })

if __name__ == '__main__':
    app.run()