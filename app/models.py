from pydantic import BaseModel


class ArtistaResponse(BaseModel):
    nome: str
    id: str
    spotify_url: str
    imagem: str | None = None