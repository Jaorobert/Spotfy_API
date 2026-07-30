from sqlalchemy import Column, Integer, String
from app.database import Base

class Artista(Base):

    __tablename__ = "artistas"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    spotify_id = Column(
        String(100),
        unique=True,
        nullable=False
    )

    nome = Column(
        String(150),
        nullable=False
    )

    spotify_url = Column(
        String(300)
    )

    imagem = Column(
        String(500)
    )
