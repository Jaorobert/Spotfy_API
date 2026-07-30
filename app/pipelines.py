from app.spotify import buscar_artista_resumo
from app.models import ArtistaResponse


def pipeline_artista(nome_artista: str):

    dados = buscar_artista_resumo(nome_artista)

    if "erro" in dados:
        return dados

    artista = ArtistaResponse(
        nome=dados["nome"],
        id=dados["id"],
        spotify_url=dados["spotify_url"],
        imagem=dados["imagem"],
        popularidade=dados["popularidade"],
        seguidores=dados["seguidores"],
        generos=dados["generos"]
    )

    return artista