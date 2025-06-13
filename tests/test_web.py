import pytest

# from app.web_automation import selenium_get_page_title, playwright_get_page_title_and_screenshot
# Para executar, você precisará ter Selenium, Playwright e os respectivos drivers/browsers instalados.

# URLs de teste
JSONPLACEHOLDER_URL = "https://jsonplaceholder.typicode.com/"
DUMMY_REST_API_URL = "https://dummy.restapiexample.com/"  # Para item 8

# Placeholder para os testes web. A implementação real exigirá as bibliotecas e drivers.


# Parte 2, Item 6: Automação de abertura da página inicial (Selenium)
@pytest.mark.web  # Marcador para testes web
@pytest.mark.skip(
    reason="Requer Selenium e WebDriver configurado. Implementação pendente."
)
def test_selenium_check_homepage_title():
    """
    Verificar se o título da página JSONPlaceholder contém "JSONPlaceholder".
    Ferramenta: Selenium.
    """
    # from selenium import webdriver
    # from selenium.webdriver.chrome.service import Service as ChromeService
    # from webdriver_manager.chrome import ChromeDriverManager
    #
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver.get(JSONPLACEHOLDER_URL)
    # page_title = driver.title
    # driver.quit()
    # assert "JSONPlaceholder" in page_title, \
    #     f"Título esperado contendo 'JSONPlaceholder', mas foi '{page_title}'"
    pytest.fail("Teste Selenium não implementado.")


# Parte 2, Item 7: Automação de navegação e captura de título com Playwright
@pytest.mark.web
@pytest.mark.skip(
    reason="Requer Playwright instalado e browsers baixados. Implementação pendente."
)
def test_playwright_check_title_and_screenshot():
    """
    Acessar a mesma URL (JSONPlaceholder), validar título e capturar um screenshot.
    Ferramenta: Playwright.
    """
    # from playwright.sync_api import sync_playwright
    #
    # with sync_playwright() as p:
    #     browser = p.chromium.launch()
    #     page = browser.new_page()
    #     page.goto(JSONPLACEHOLDER_URL)
    #     page_title = page.title()
    #     screenshot_path = "jsonplaceholder_playwright.png"
    #     page.screenshot(path=screenshot_path)
    #     browser.close()
    #
    # assert "JSONPlaceholder" in page_title, \
    #     f"Título esperado contendo 'JSONPlaceholder' (Playwright), mas foi '{page_title}'"
    # import os
    # assert os.path.exists(screenshot_path), f"Screenshot não foi salvo em {screenshot_path}"
    pytest.fail("Teste Playwright não implementado.")


# Parte 2, Item 8: Verificação da existência de um elemento HTML específico
# Este teste será dividido em dois: um para Selenium, outro para Playwright.
# O elemento a ser verificado pode ser, por exemplo, o <h1> na página dummy.restapiexample.com
# que geralmente contém "Dummy Rest API Example"


@pytest.mark.web
@pytest.mark.skip(reason="Requer Selenium e WebDriver. Implementação pendente.")
def test_selenium_check_element_exists_dummy_api():
    """
    Confirmar a presença de um elemento HTML específico com Selenium.
    URL: https://dummy.restapiexample.com/
    Elemento: <h1> contendo "Dummy Rest API Example"
    """
    # from selenium import webdriver
    # from selenium.webdriver.common.by import By
    # from selenium.webdriver.chrome.service import Service as ChromeService
    # from webdriver_manager.chrome import ChromeDriverManager
    #
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver.get(DUMMY_REST_API_URL)
    # try:
    #     element = driver.find_element(By.XPATH, "//h1[contains(text(),'Dummy Rest API Example')]")
    #     assert element.is_displayed(), "Elemento <h1> encontrado mas não está visível."
    # except Exception as e: # NoSuchElementException
    #     pytest.fail(f"Elemento <h1> não encontrado na página {DUMMY_REST_API_URL} com Selenium: {e}")
    # finally:
    #     driver.quit()
    pytest.fail("Teste Selenium (elemento) não implementado.")


@pytest.mark.web
@pytest.mark.skip(reason="Requer Playwright. Implementação pendente.")
def test_playwright_check_element_exists_dummy_api():
    """
    Confirmar a presença de um elemento HTML específico com Playwright.
    URL: https://dummy.restapiexample.com/
    Elemento: <h1> contendo "Dummy Rest API Example"
    """
    # from playwright.sync_api import sync_playwright
    #
    # with sync_playwright() as p:
    #     browser = p.chromium.launch()
    #     page = browser.new_page()
    #     page.goto(DUMMY_REST_API_URL)
    #     try:
    #         # Usando seletor de texto do Playwright ou XPath
    #         element = page.locator("h1:has-text('Dummy Rest API Example')")
    #         # element = page.query_selector("//h1[contains(text(),'Dummy Rest API Example')]")
    #         assert element.is_visible(), "Elemento <h1> encontrado mas não está visível (Playwright)."
    #     except Exception as e: # TimeoutError se o elemento não for encontrado dentro do tempo padrão
    #         pytest.fail(f"Elemento <h1> não encontrado na página {DUMMY_REST_API_URL} com Playwright: {e}")
    #     finally:
    #         browser.close()
    pytest.fail("Teste Playwright (elemento) não implementado.")


# Os testes da Parte 3 (Roteiro de Avaliação) são mais específicos e alguns podem
# se sobrepor ou detalhar os da Parte 2. Eles seriam implementados de forma similar.
# Por exemplo, "Teste com Playwright: Validar performance e tempo de resposta."
# exigiria o uso das métricas de performance do Playwright.
