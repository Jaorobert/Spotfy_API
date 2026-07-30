from app.spotify import buscar_artista_resumo
from app.schemas import ArtistaResponse
from app.models import Artista
from app.database import SessionLocal


def pipeline_artista(nome_artista: str):

    db = SessionLocal()

    try:

        # 1 - procura no banco pelo nome
        artista_existente = db.query(Artista).filter(
            Artista.nome.ilike(nome_artista)
        ).first()


        # 2 - encontrou no banco
        if artista_existente:

            return ArtistaResponse(
                nome=artista_existente.nome,
                id=artista_existente.spotify_id,
                spotify_url=artista_existente.spotify_url,
                imagem=artista_existente.imagem
           
            )


        # 3 - não encontrou, chama Spotify
        dados = buscar_artista_resumo(nome_artista)


        if "erro" in dados:
            return dados


        # 4 - salva no banco

        novo_artista = Artista(
            spotify_id=dados["id"],
            nome=dados["nome"],
            spotify_url=dados["spotify_url"],
            imagem=dados["imagem"]
        )


        db.add(novo_artista)
        db.commit()
        db.refresh(novo_artista)


        # 5 - retorna resposta

        return ArtistaResponse(
            nome=novo_artista.nome,
            id=novo_artista.spotify_id,
            spotify_url=novo_artista.spotify_url,
            imagem=novo_artista.imagem
        )


    finally:
        db.close()