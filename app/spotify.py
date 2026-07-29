import requests
from app.auth import get_token


BASE_URL = "https://api.spotify.com/v1"


def buscar_artista(artist_id):

    token = get_token()

    url = f"{BASE_URL}/artists/{artist_id}"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        url,
        headers=headers
    )

    response.raise_for_status()

    return response.json()



def buscar_por_nome(nome_artista):

    token = get_token()

    url = f"{BASE_URL}/search"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    params = {
        "q": nome_artista,
        "type": "artist",
        "limit": 1
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    response.raise_for_status()

    return response.json()



def buscar_artista_resumo(nome_artista):

    resultado = buscar_por_nome(nome_artista)

    artistas = resultado["artists"]["items"]

    if not artistas:
        return {
            "erro": "Artista não encontrado"
        }

    artista = artistas[0]

    return {
        "nome": artista["name"],
        "id": artista["id"],
        "spotify_url": artista["external_urls"]["spotify"],
        "imagem": artista["images"][0]["url"] if artista["images"] else None
    }