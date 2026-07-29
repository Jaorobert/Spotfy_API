from fastapi import FastAPI
from app.spotify import buscar_artista_resumo
from app.models import ArtistaResponse


app = FastAPI(
    title="Spotify API",
    description="API para consulta de artistas usando Spotify Web API",
    version="1.0"
)


@app.get("/")
def inicio():

    return {
        "mensagem": "API Spotify funcionando"
    }



@app.get(
    "/artista/{nome}",
    response_model=ArtistaResponse
)
def buscar_artista(nome: str):

    resultado = buscar_artista_resumo(nome)

    return resultado