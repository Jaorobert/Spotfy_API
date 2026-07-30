from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.schemas import ArtistaResponse
from app.pipelines import pipeline_artista


from app.database import engine, Base
from app import models


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Spotify API",
    description="API para consulta de artistas usando Spotify Web API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/artista/{nome}", response_model=ArtistaResponse)
def buscar_artista(nome: str):
    return pipeline_artista(nome)