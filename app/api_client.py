import requests
import logging

# Configuração básica de logging para o módulo
# O logging registrará as operações realizadas e eventuais erros.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("api_client.log"),  # Log para arquivo
        logging.StreamHandler(),  # Log para console
    ],
)
logger = logging.getLogger(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com/"


def get_posts():
    """Busca todos os posts."""
    try:
        logger.info(f"Realizando GET em {BASE_URL}posts")
        response = requests.get(f"{BASE_URL}posts")
        response.raise_for_status()  # Lança exceção para status de erro HTTP (4XX ou 5XX)
        logger.info(f"GET /posts - Status: {response.status_code}")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao buscar posts: {e}")
        return None


def create_post(title, body, user_id):
    """Cria um novo post."""
    payload = {"title": title, "body": body, "userId": user_id}
    try:
        logger.info(f"Realizando POST em {BASE_URL}posts com payload: {payload}")
        response = requests.post(f"{BASE_URL}posts", json=payload)
        response.raise_for_status()
        logger.info(
            f"POST /posts - Status: {response.status_code} - Resposta: {response.json()}"
        )
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao criar post: {e}")
        return None, getattr(e.response, "status_code", 500)


def update_post(post_id, title=None, body=None, user_id=None):
    """Atualiza um post existente."""
    payload = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if user_id is not None:
        payload["userId"] = user_id

    if not payload:
        logger.warning("Nenhum dado fornecido para atualização.")
        return None, 400  # Bad request se nada for atualizado

    try:
        logger.info(
            f"Realizando PUT em {BASE_URL}posts/{post_id} com payload: {payload}"
        )
        response = requests.put(f"{BASE_URL}posts/{post_id}", json=payload)
        response.raise_for_status()
        logger.info(
            f"PUT /posts/{post_id} - Status: {response.status_code} - Resposta: {response.json()}"
        )
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao atualizar post {post_id}: {e}")
        return None, getattr(e.response, "status_code", 500)


def delete_post(post_id):
    """Exclui um post."""
    try:
        logger.info(f"Realizando DELETE em {BASE_URL}posts/{post_id}")
        response = requests.delete(f"{BASE_URL}posts/{post_id}")
        response.raise_for_status()  # Considerar que DELETE pode não retornar JSON e 204 é sucesso
        logger.info(f"DELETE /posts/{post_id} - Status: {response.status_code}")
        return response.status_code  # Geralmente 200 ou 204 para sucesso
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao excluir post {post_id}: {e}")
        return getattr(e.response, "status_code", 500)


if __name__ == "__main__":
    # Exemplo de uso (pode ser removido ou movido para testes)
    logger.info("Testando as funções do api_client:")

    # GET posts
    posts = get_posts()
    if posts:
        logger.info(f"Total de posts obtidos: {len(posts)}")

    # CREATE post
    new_post_data, status_code = create_post("Título de Teste", "Corpo do teste", 1)
    if new_post_data:
        logger.info(f"Novo post criado com ID: {new_post_data.get('id')}")
        post_id_to_use = new_post_data.get("id")

        # UPDATE post (se criado com sucesso)
        if post_id_to_use:
            updated_post_data, update_status = update_post(
                post_id_to_use, title="Título Atualizado"
            )
            if updated_post_data:
                logger.info(f"Post {post_id_to_use} atualizado.")

            # DELETE post (se criado com sucesso)
            delete_status = delete_post(post_id_to_use)
            logger.info(
                f"Tentativa de exclusão do post {post_id_to_use} resultou no status: {delete_status}"
            )
