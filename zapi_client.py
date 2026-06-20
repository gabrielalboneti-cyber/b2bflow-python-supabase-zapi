import requests


def enviar_mensagem(config, telefone, mensagem):
    headers = {
        "Client-Token": config.zapi_client_token,
        "Content-Type": "application/json",
    }

    body = {
        "phone": telefone,
        "message": mensagem,
    }

    response = requests.post(
        config.zapi_url,
        json=body,
        headers=headers,
        timeout=30,
    )

    if not response.ok:
        raise Exception(
            f"Status {response.status_code} - {response.text}"
        )

    if response.content:
        return response.json()

    return {}
