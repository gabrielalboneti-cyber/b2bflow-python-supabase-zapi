from supabase import create_client


def buscar_contatos(supabase_url, supabase_key, limite=3):
    supabase = create_client(supabase_url, supabase_key)

    response = (
        supabase.table("contatos")
        .select("id,nome,telefone")
        .limit(limite)
        .execute()
    )

    return response.data or []
