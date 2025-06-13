import pytest
import requests
import time
from app import api_client  # Importa o módulo api_client

# Testes de API com pytest e requests (usando funções de api_client)


# Parte 2, Item 1: Testar a resposta do endpoint GET /posts
def test_get_posts_status_and_content(base_api_url):
    """
    Valida status 200 para GET /posts e que a resposta contém uma lista de objetos.
    Ferramenta: requests + pytest.
    """
    response_data = api_client.get_posts()
    assert (
        response_data is not None
    ), "A resposta da API não deveria ser None (verifique erros no log do api_client)"

    # Validar que a chamada foi bem sucedida (implícito se response_data não é None e não houve exceção)
    # A validação do status code 200 já é feita dentro de api_client.get_posts() com raise_for_status()
    # Mas podemos re-checar se quisermos ser explícitos no teste ou se a função não lançasse exceção.
    # Para este exemplo, confiamos que api_client.get_posts() já validou o status ou retornou None.

    assert isinstance(
        response_data, list
    ), "A resposta de GET /posts deveria ser uma lista."
    assert len(response_data) > 0, "A lista de posts não deveria estar vazia."
    for item in response_data:
        assert isinstance(
            item, dict
        ), "Cada item na lista de posts deveria ser um dicionário."
        assert "id" in item, "Cada post deveria ter um 'id'."
        assert "title" in item, "Cada post deveria ter um 'title'."


# Parte 2, Item 2: Testar a criação de um novo post com POST /posts
def test_create_new_post(base_api_url, new_post_payload):
    """
    Valida status 201 para POST /posts e verifica se o corpo da resposta contém o título enviado.
    Ferramenta: requests + pytest.
    """
    title_sent = new_post_payload["title"]
    response_data, status_code = api_client.create_post(
        title=new_post_payload["title"],
        body=new_post_payload["body"],
        user_id=new_post_payload["userId"],
    )
    assert status_code == 201, f"Esperado status 201, mas foi obtido {status_code}."
    assert response_data is not None, "A resposta da API não deveria ser None."
    assert "id" in response_data, "A resposta deveria conter um 'id' para o novo post."
    assert (
        response_data.get("title") == title_sent
    ), "O título na resposta não corresponde ao título enviado."
    # Opcional: verificar outros campos se necessário


# Parte 2, Item 4: Testar a exclusão de um post com DELETE /posts/1
# (Item 3 usa unittest, será em outro arquivo ou adaptado se tudo for pytest)
@pytest.mark.parametrize("post_id_to_delete", [1, 5, 10])  # Exemplo de alguns IDs
def test_delete_post(base_api_url, post_id_to_delete):
    """
    Valida status 200 ou 204 para DELETE /posts/{id}.
    Ferramenta: requests + pytest.
    Nota: JSONPlaceholder retorna 200 para DELETE.
    """
    # Primeiro, vamos verificar se o post existe (opcional, mas bom para o teste ser mais robusto)
    # get_response = requests.get(f"{base_api_url}/posts/{post_id_to_delete}")
    # if get_response.status_code == 404:
    #     pytest.skip(f"Post {post_id_to_delete} não encontrado, pulando teste de exclusão.")

    status_code = api_client.delete_post(post_id_to_delete)
    assert (
        status_code == 200 or status_code == 204
    ), f"Esperado status 200 ou 204 para DELETE, mas foi obtido {status_code}."

    # Opcional: Tentar buscar o post excluído e verificar se retorna 404
    # (JSONPlaceholder pode não se comportar assim, pois é um mock)
    # response_after_delete = requests.get(f"{base_api_url}/posts/{post_id_to_delete}")
    # assert response_after_delete.status_code == 404, \
    #     f"Esperado status 404 ao tentar buscar post excluído {post_id_to_delete}, mas foi {response_after_delete.status_code}."


# Parte 2, Item 5: Testar o tempo de resposta do endpoint GET /posts
def test_get_posts_response_time(base_api_url):
    """
    Valida que o tempo de resposta do GET /posts seja inferior a 2 segundos.
    Ferramenta: requests + pytest.
    """
    start_time = time.time()
    response = requests.get(
        f"{base_api_url}/posts"
    )  # Chamada direta para medir apenas o request
    end_time = time.time()

    duration = end_time - start_time

    assert response.status_code == 200, "A requisição GET /posts falhou."
    assert (
        duration < 2.0
    ), f"O tempo de resposta foi {duration:.2f}s, que é >= 2 segundos."


# Parte 2, Item 9: Testes parametrizados com múltiplos IDs de posts
@pytest.mark.parametrize("post_id", [1, 2, 3, 99, 100])
def test_get_specific_post_status_ok(base_api_url, post_id):
    """
    Testar GET /posts/{id} com vários valores de id e validar status 200.
    Ferramenta: pytest com parametrize.
    """
    response = requests.get(f"{base_api_url}/posts/{post_id}")
    assert (
        response.status_code == 200
    ), f"Esperado status 200 para GET /posts/{post_id}, mas foi {response.status_code}."
    data = response.json()
    assert (
        data["id"] == post_id
    ), f"O ID do post na resposta ({data['id']}) não corresponde ao ID solicitado ({post_id})."


@pytest.mark.parametrize("post_id_not_found", [0, 101, -1, "abc"])
def test_get_specific_post_status_not_found(base_api_url, post_id_not_found):
    """
    Testar GET /posts/{id} com IDs inválidos/inexistentes e validar status 404.
    """
    response = requests.get(f"{base_api_url}/posts/{post_id_not_found}")
    assert (
        response.status_code == 404
    ), f"Esperado status 404 para GET /posts/{post_id_not_found}, mas foi {response.status_code}."


# Para o Item 3 (PUT com unittest), você criaria um arquivo separado, por exemplo, test_api_unittest.py
# ou adaptaria o teste para Pytest se a exigência de unittest não for estrita.
# Exemplo de como seria o PUT com Pytest, similar ao POST:
def test_update_existing_post(base_api_url, update_post_payload):
    """
    Valida status 200 para PUT /posts/1 e se os dados foram atualizados.
    Adaptado para Pytest.
    """
    post_id_to_update = 1  # Conforme o item 3
    title_sent = update_post_payload.get("title", "Título Padrão Atualizado")

    # Garantir que o post exista (opcional, JSONPlaceholder geralmente tem o post 1)
    # pre_check = requests.get(f"{base_api_url}/posts/{post_id_to_update}")
    # assert pre_check.status_code == 200, f"Post {post_id_to_update} não encontrado para atualização."

    response_data, status_code = api_client.update_post(
        post_id=post_id_to_update,
        title=title_sent,
        body=update_post_payload.get("body"),
        user_id=update_post_payload.get("userId"),
    )
    assert (
        status_code == 200
    ), f"Esperado status 200 para PUT, mas foi obtido {status_code}."
    assert response_data is not None, "A resposta da API não deveria ser None."
    assert (
        response_data.get("id") == post_id_to_update
    ), "O ID na resposta não corresponde ao ID atualizado."
    assert (
        response_data.get("title") == title_sent
    ), "O título na resposta não corresponde ao título enviado para atualização."
