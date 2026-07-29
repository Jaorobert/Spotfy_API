import requests
from auth import get_token


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