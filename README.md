# Projeto Final de Testes: Integração com APIs e Testes Automatizados

**UNIVASF - TAC-3**

---

## 📚 Sobre o Projeto

Este projeto demonstra a implementação de testes automatizados para APIs e interfaces web, utilizando ferramentas modernas e técnicas de automação, conforme os requisitos da disciplina **Tópicos Avançados em Computação III - Testes**.

---

## 🚀 Tecnologias e Ferramentas

- **Requests:** Requisições HTTP e testes de API.
- **Pytest:** Framework para escrita e execução de testes.
- **Selenium:** Automação de testes de interface web.
- **Playwright:** Alternativa moderna para automação web.
- **Logging (Python):** Registro de operações e resultados dos testes.

> Ferramentas diferenciais (Apidog, Robot Framework) podem ser integradas futuramente.

---

## 📁 Estrutura de Diretórios

```
project/
├── app/
│   ├── api_client.py          # Funções para requisições HTTP
│   ├── web_automation.py      # Scripts de automação web
│   └── __init__.py
├── tests/
│   ├── test_api.py            # Testes de API (Pytest)
│   ├── test_web.py            # Testes de automação web
│   ├── conftest.py            # Fixtures e configuração do Pytest
│   └── __init__.py
├── requirements.txt           # Dependências do projeto
├── pytest.ini                 # Configuração do Pytest
├── api_client.log             # Log do api_client.py
├── web_automation.log         # Log do web_automation.py
├── pytest_run.log             # Log geral do Pytest
└── README.md                  # Manual do projeto
```

---

## ⚙️ Configuração do Ambiente

1. **Crie um ambiente virtual:**

    ```bash
    python -m venv venv
    # Linux/macOS
    source venv/bin/activate
    # Windows
    venv\Scripts\activate
    ```

2. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Instale navegadores do Playwright:**

    ```bash
    playwright install
    ```

4. **Selenium:**
   Certifique-se de ter os WebDrivers no PATH ou utilize `webdriver-manager` (já incluso nas dependências).

---

## 📝 Execução dos Testes

1. **Execute todos os testes:**

    ```bash
    pytest
    ```

2. **Execução detalhada (verbose):**

    ```bash
    pytest -v
    ```

3. **Testes por marcador:**

    ```bash
    pytest -m api  # Apenas testes de API
    pytest -m web  # Apenas testes web
    ```

4. **Logs:**
   Os logs são exibidos no console e salvos nos arquivos `.log` correspondentes.

---

## 🔗 Documentação Útil

- [Pytest](https://docs.pytest.org/)
- [Requests](https://requests.readthedocs.io/)
- [Selenium](https://www.selenium.dev/documentation/)
- [Playwright](https://playwright.dev/python/docs/intro)
- [Logging HOWTO (Python)](https://docs.python.org/3/howto/logging.html)

---

## 📌 Próximos Passos

- **Parte 2:** Implementar testes detalhados para API (GET, POST, PUT, DELETE, tempo de resposta) e Web (Selenium, Playwright, verificação de elementos, testes parametrizados).
- **Parte 3:** Desenvolver roteiro de avaliação com testes específicos.
- **Parte 4:** Garantir que todos os entregáveis estejam completos e funcionais.
- **Parte 5 e 6:** Atentar para critérios de avaliação e prazos.

---

## ℹ️ Observações

- Os arquivos `__init__.py` marcam os diretórios como pacotes Python.
- O sistema de logging está configurado para registrar operações em arquivos e no console.
- O arquivo `pytest.ini` controla a saída de logs do Pytest.

---

## 🎓 Aviso

**Este projeto tem finalidade estritamente acadêmica e foi desenvolvido para fins de estudo na UNIVASF.**
