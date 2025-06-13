# Projeto Final de Testes: Integração com APIs e Testes Automatizados (UNIVASF - TAC-3)

Este projeto visa demonstrar a implementação de testes automatizados para APIs e interfaces web, utilizando diversas ferramentas e técnicas conforme especificado na disciplina de Tópicos Avançados em Computação III - Testes.

## Introdução

O objetivo é realizar um conjunto de testes acessando o endpoint `https://jsonplaceholder.typicode.com/`, integrando o uso de APIs e ferramentas de testes automatizados como Selenium, Requests, Pytest e Playwright.

## Ferramentas Utilizadas (Principais)

* **Requests:** Para requisições HTTP e testes de API.
* **Pytest:** Framework para escrita e execução de testes.
* **Selenium:** Para automação de testes de interface web.
* **Playwright:** Alternativa moderna para automação de testes de interface web.
* **Logging (módulo `logging` do Python):** Para registrar operações e resultados dos testes.

Ferramentas diferenciais mencionadas no plano (Apidog, Robot Framework) podem ser integradas posteriormente.

## Estrutura de Diretórios

O projeto segue a seguinte estrutura:

```plaintext
project/
├── app/
│   ├── api_client.py          # Módulo com funções para requisições HTTP
│   ├── web_automation.py      # Módulo com scripts de automação web
│   └── __init__.py
├── tests/
│   ├── test_api.py            # Testes de API com pytest (e exemplos para unittest se necessário)
│   ├── test_web.py            # Testes de automação web
│   ├── conftest.py            # Configuração de fixtures do pytest
│   └── __init__.py
├── requirements.txt           # Arquivo com as dependências
├── pytest.ini                 # Configuração do pytest
├── api_client.log             # Log das operações do api_client.py
├── web_automation.log         # Log das operações do web_automation.py
├── pytest_run.log             # Log geral da execução do pytest
└── README.md                  # Manual do projeto
```

## Parte 1: Configuração do Ambiente e Estrutura

1. **Estrutura de Diretórios:** Criada conforme especificado.
2. **Arquivos `__init__.py`:** Adicionados para marcar `app` e `tests` como pacotes Python.
3. **Ambiente Virtual e Dependências:**
    * Recomenda-se criar um ambiente virtual:

        ```bash
        python -m venv venv
        source venv/bin/activate  # Linux/macOS
        # venv\Scripts\activate   # Windows
        ```

    * Instale as dependências:

        ```bash
        pip install -r requirements.txt
        ```

    * Para Playwright, instale os navegadores necessários:

        ```bash
        playwright install
        ```

    * Para Selenium, certifique-se de ter os WebDrivers apropriados no seu PATH ou use `webdriver-manager` (incluído no `requirements.txt`).

4. **`requirements.txt`:** Configurado com as bibliotecas principais. Adicione versões específicas conforme necessário.
5. **`tests/conftest.py`:** Implementado com fixtures básicas (ex: URL base da API) e configuração de logging.
6. **Sistema de Logging:**
    * O módulo `logging` do Python é utilizado.
    * `api_client.py` e `web_automation.py` configuram loggers para registrar suas operações em arquivos (`api_client.log`, `web_automation.log`) e no console.
    * `pytest.ini` está configurado para controlar a saída de log do Pytest durante a execução dos testes, tanto no console quanto em `pytest_run.log`.
    * `conftest.py` também pode ser usado para configurar logging específico para testes ou fixtures.

## Como Executar os Testes

Após configurar o ambiente e instalar as dependências:

1. Navegue até o diretório raiz do projeto (`project/`).
2. Execute o Pytest:

    ```bash
    pytest
    ```

    Ou com mais detalhes (verbose):

    ```bash
    pytest -v
    ```

3. Para executar testes com marcadores específicos (definidos em `pytest.ini` e nos arquivos de teste):

    ```bash
    pytest -m api  # Executa apenas testes de API
    pytest -m web  # Executa apenas testes web
    ```

4. Para ver a saída de logs no console durante a execução (já configurado em `pytest.ini`):

    ```bash
    pytest
    ```

    Os logs também serão salvos nos arquivos `.log` especificados.

## Próximos Passos (Conforme Plano de Atividades)

* **Parte 2:** Implementar os testes detalhados para API (GET, POST, PUT, DELETE, tempo de resposta) e Web (Selenium, Playwright, verificação de elementos, testes parametrizados).
  * O arquivo `tests/test_api.py` já contém implementações iniciais para vários itens da Parte 2.
  * O arquivo `tests/test_web.py` contém placeholders e precisa da implementação dos testes com Selenium e Playwright.
  * Para o item de teste PUT com `unittest` (Parte 2, Item 3), você pode criar um arquivo separado (ex: `tests/test_api_unittest.py`) ou adaptar o teste para Pytest se permitido.
* **Parte 3:** Desenvolver o roteiro de avaliação com testes mais específicos.
* **Parte 4:** Garantir que todos os entregáveis estejam completos e funcionais.
* **Parte 5 e 6:** Atentar para os critérios de avaliação e prazos.

## Documentação Adicional

* **Pytest:** [https://docs.pytest.org/](https://docs.pytest.org/)
* **Requests:** [https://requests.readthedocs.io/](https://requests.readthedocs.io/)
* **Selenium:** [https://www.selenium.dev/documentation/](https://www.selenium.dev/documentation/)
* **Playwright:** [https://playwright.dev/python/docs/intro](https://playwright.dev/python/docs/intro)
* **Logging HOWTO (Python):** [https://docs.python.org/3/howto/logging.html](https://docs.python.org/3/howto/logging.html)
