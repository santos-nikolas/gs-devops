==========================================================================
# ORBITALWATCH - SISTEMA DE MONITORAMENTO DE DETRITOS ESPACIAIS
==========================================================================

CONTEXTO DO PROJETO
-------------------
O OrbitalWatch é uma solução de software resiliente desenvolvida para a Global Solution 2026 da FIAP. O projeto foca no monitoramento e gerenciamento de detritos espaciais em órbita baixa (LEO), fornecendo uma API de alta disponibilidade para alertar sobre possíveis colisões e garantir a integridade de infraestruturas orbitais críticas.

Este projeto representa a convergência entre a Engenharia de Software e a Nova Corrida Espacial, onde o código é o combustível para operações seguras e sustentáveis no universo.

ALINHAMENTO COM ODS 9 (ONU)
---------------------------
O projeto está diretamente conectado ao ODS 9 (Indústria, Inovação e Infraestrutura), pois protege a infraestrutura de satélites que sustenta a economia moderna, desde comunicações globais até sistemas de geolocalização essenciais.


ARQUITETURA CLOUD (PaaS)
------------------------
A solução utiliza uma arquitetura moderna baseada em nuvem utilizando o ecossistema Microsoft Azure, priorizando o modelo de Plataforma como Serviço (PaaS):

- Azure App Service (Linux): Hospedagem da aplicação em ambiente escalável.
- Azure Key Vault: Gerenciamento centralizado e criptografado de segredos.
- Azure Application Insights: Monitoramento de performance (APM) e telemetria.
- Microsoft Entra ID: Autenticação via Identidade Gerenciada (Managed Identity).


SEGURANÇA E DEVSECOPS
---------------------
O OrbitalWatch foi desenvolvido seguindo os princípios de Security by Design e Zero Trust:

1. Managed Identity: A aplicação não possui senhas no código-fonte. Ela utiliza uma identidade de sistema para se autenticar no Azure.
2. RBAC (Role-Based Access Control): Atribuição de função restrita (Key Vault Secrets User) para o serviço de aplicativo.
3. Key Vault: Todas as chaves de APIs espaciais e segredos são armazenados em HSMs criptografados.
4. HTTPS Nativo: Criptografia de ponta a ponta garantida por TLS/SSL.


ESTEIRA DE CI/CD (GITHUB ACTIONS)
---------------------------------
O fluxo de integração e entrega contínua é 100% automatizado:
- Gatilho: Cada "push" na branch principal dispara o pipeline.
- Build: Configuração de runtime Python 3.12 e instalação de dependências.
- Deploy: Implantação automática no Azure via Publish Profile armazenado em GitHub Secrets.


MONITORAMENTO E OBSERVABILIDADE
-------------------------------
A saúde do sistema é monitorada proativamente através de:
- Application Insights: Coleta de métricas de latência e taxas de sucesso.
- Regras de Alerta: Configuração de alertas para erros HTTP 5xx (Server Errors), permitindo resposta rápida a incidentes.


TECNOLOGIAS UTILIZADAS
----------------------
- Linguagem: Python 3.12
- Framework: Flask
- Servidor: Gunicorn
- Nuvem: Microsoft Azure
- Pipeline: GitHub Actions


COMO EXECUTAR LOCALMENTE
------------------------
1. Clone o repositório.
2. Crie um ambiente virtual: python -m venv venv
3. Ative o ambiente virtual e instale as dependências: pip install -r requirements.txt
4. Execute a aplicação: python app.py


LINKS DO PROJETO
----------------
- URL da Aplicação (Azure): https://orbitalwatch-551624-cseeaggpf5a6a4e7.eastus2-01.azurewebsites.net/
- Repositório (GitHub): https://github.com/santos-nikolas/gs-devops/new/main?filename=README.md


EQUIPE (4º ANO ENGENHARIA DE SOFTWARE - FIAP)
---------------------------------------------
- Nikolas Rodrigues Moura dos Santos - RM 551566
- Pedro Henrique Pedrosa Tavares - RM 97877
- Thiago Jardim de Oliveira - RM 556124
- Guilherme Rocha Bianchini - RM 97974
- Rodrigo Brasileiro - RM 98952

--------------------------------------------------------------------------
Global Solution 2026 - Indústria Espacial: O Código que Move o Universo.
--------------------------------------------------------------------------
