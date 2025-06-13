import pytest
import logging
import requests
from app.api_client import BASE_URL  # Importar BASE_URL de api_client

# Configuração de logging para os testes
# Pode ser configurado aqui ou no pytest.ini
# Este logger será usado para mensagens específicas dos fixtures ou da configuração de teste
logger = logging.getLogger(__name__)  # Logger específico para conftest
logger.setLevel(logging.DEBUG)  # Definir nível para este logger


# Fixture para a URL base da API
@pytest.fixture(scope="session")
def base_api_url():
    """Fornece a URL base para os testes de API."""
    logger.info(f"Fixture 'base_api_url' fornecendo: {BASE_URL}")
    return BASE_URL


# Fixture para um cliente de sessão de requests, se necessário para manter estado (cookies, headers)
@pytest.fixture(scope="session")
def api_session():
    """Fornece uma sessão de requests para ser usada nos testes."""
    logger.info("Criando fixture de sessão de requests.")
    session = requests.Session()
    # Você pode configurar headers padrão aqui, se necessário
    # session.headers.update({'Content-Type': 'application/json'})
    yield session
    logger.info("Fechando fixture de sessão de requests.")
    session.close()


# Exemplo de fixture para dados de teste (um novo post)
@pytest.fixture
def new_post_payload():
    """Fornece um payload de exemplo para criar um novo post."""
    payload = {"title": "foo", "body": "bar", "userId": 1}
    logger.debug(f"Fixture 'new_post_payload' fornecendo: {payload}")
    return payload


# Exemplo de fixture para dados de atualização de post
@pytest.fixture
def update_post_payload():
    """Fornece um payload de exemplo para atualizar um post."""
    payload = {
        "title": "foo updated",
        "body": "bar updated",
        "userId": 1,
        "id": 1,  # Geralmente o ID é parte da URL, mas se for no corpo...
    }
    logger.debug(f"Fixture 'update_post_payload' fornecendo: {payload}")
    return payload


# Você pode adicionar fixtures para setup e teardown de drivers Selenium/Playwright aqui
# Exemplo (requer implementação completa em web_automation.py ou aqui):
# @pytest.fixture(scope="module")
# def browser_playwright():
#     from playwright.sync_api import sync_playwright
#     logger.info("Iniciando browser Playwright para o módulo de testes.")
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         yield browser
#         logger.info("Fechando browser Playwright.")
#         browser.close()

# @pytest.fixture
# def page_playwright(browser_playwright):
#     logger.debug("Criando nova página Playwright para o teste.")
#     page = browser_playwright.new_page()
#     yield page
#     logger.debug("Fechando página Playwright.")
#     page.close()
