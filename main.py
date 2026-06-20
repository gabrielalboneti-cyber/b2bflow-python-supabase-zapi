from config import Config
from supabase_client import buscar_contatos
from zapi_client import enviar_mensagem


def main():
    print("Início da execução")

    try:
        config = Config.from_env()
        contatos = buscar_contatos(config.supabase_url, config.supabase_key)
    except Exception as erro:
        print(f"Erro ao buscar contatos: {erro}")
        print("Finalização")
        return

    print(f"Quantidade de contatos encontrados: {len(contatos)}")

    for contato in contatos:
        nome = contato.get("nome")
        telefone = contato.get("telefone")

        if not nome or not telefone:
            print("Contato ignorado: nome ou telefone não informado")
            continue

        mensagem = f"Olá, {nome} tudo bem com você?"

        print(f"Enviando mensagem para {nome} ({telefone})")

        try:
            enviar_mensagem(config, telefone, mensagem)
            print(f"Sucesso no envio para {nome}")
        except Exception as erro:
            print(f"Erro no envio para {nome}: {erro}")

    print("Finalização")


if __name__ == "__main__":
    main()
