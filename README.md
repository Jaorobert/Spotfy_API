# 🎵 Spotify API — Consulta de Artistas

API web para consulta de artistas na plataforma Spotify, com cache local em banco de dados SQLite e interface web interativa.

---

## 📋 O que foi feito

Este projeto consome a **Spotify Web API** para buscar informações de artistas por nome. O resultado é exibido em uma interface web simples e também é armazenado localmente em banco de dados SQLite para evitar chamadas repetidas à API do Spotify.

### Fluxo de funcionamento

```
Usuário digita o nome do artista
        │
        ▼
[pipeline_artista]
        │
        ├── Artista já está no banco? ──► Retorna do banco (sem chamar Spotify)
        │
        └── Não está no banco?
                │
                ▼
         [Spotify Web API]
                │
                ▼
         Salva no banco SQLite
                │
                ▼
         Retorna resposta
```

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Versão | Uso |
|---|---|---|
| **Python** | 3.11+ | Linguagem principal |
| **FastAPI** | 0.141.1 | Framework web e API REST |
| **Uvicorn** | 0.52.0 | Servidor ASGI |
| **SQLAlchemy** | 2.0.51 | ORM para banco de dados |
| **SQLite** | — | Banco de dados local (arquivo `spotify.db`) |
| **Pydantic** | 2.13.4 | Validação e serialização de dados |
| **Requests** | 2.34.2 | Chamadas HTTP para a Spotify API |
| **python-dotenv** | 1.2.2 | Leitura de variáveis de ambiente do `.env` |
| **Jinja2** | 3.1.6 | Templates HTML |
| **HTML + CSS + JS** | — | Interface web do usuário |

---

## 📁 Estrutura do projeto

```
Spotfy_API/
├── app/
│   ├── __init__.py         # Inicialização do pacote
│   ├── auth.py             # Autenticação com a Spotify API (Client Credentials)
│   ├── database.py         # Configuração do SQLAlchemy e conexão com SQLite
│   ├── main.py             # Entrypoint FastAPI: rotas e configuração do app
│   ├── models.py           # Modelo ORM da tabela `artistas`
│   ├── pipelines.py        # Lógica de negócio: banco → Spotify → banco
│   ├── schemas.py          # Schema Pydantic para resposta da API
│   ├── spotify.py          # Funções de chamada à Spotify Web API
│   ├── static/
│   │   ├── scripts.js      # Lógica do frontend (fetch + renderização)
│   │   └── style.css       # Estilização da interface
│   └── templates/
│       └── index.html      # Página principal
├── tests/
│   └── test_main.py        # Testes da rota principal
├── .env                    # Credenciais (NÃO commitado)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Configuração e instalação

### 1. Pré-requisitos

- Python 3.11 ou superior
- Conta de desenvolvedor no [Spotify for Developers](https://developer.spotify.com/dashboard)

### 2. Clonar o repositório

```bash
git clone https://github.com/Jaorobert/Spotfy_API.git
cd Spotfy_API
```

### 3. Criar o ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux/Mac
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar as credenciais do Spotify

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
SPOTIFY_CLIENT_ID=seu_client_id_aqui
SPOTIFY_CLIENT_SECRET=seu_client_secret_aqui
```

> Para obter as credenciais, acesse o [Spotify Developer Dashboard](https://developer.spotify.com/dashboard), crie um app e copie o **Client ID** e o **Client Secret**.

### 6. Iniciar o servidor

```bash
uvicorn app.main:app --reload
```

Acesse no navegador: **http://127.0.0.1:8000**

---

## 🌐 Interface Web

Ao acessar `http://127.0.0.1:8000`, você verá uma interface onde pode:

1. Digitar o nome de um artista no campo de busca
2. Clicar em **Buscar**
3. Ver o card com imagem, nome e link direto para o Spotify

---

## 📡 Endpoints da API

### `GET /`
Retorna a página HTML da interface web.

---

### `GET /artista/{nome}`
Busca informações de um artista pelo nome.

**Parâmetros:**
| Nome | Tipo | Descrição |
|---|---|---|
| `nome` | `string` (path) | Nome do artista a ser buscado |

**Exemplo de requisição:**
```
GET /artista/Coldplay
```

**Exemplo de resposta (`200 OK`):**
```json
{
  "nome": "Coldplay",
  "id": "4gzpq5DPGxSnKTe4SA8HAU",
  "spotify_url": "https://open.spotify.com/artist/4gzpq5DPGxSnKTe4SA8HAU",
  "imagem": "https://i.scdn.co/image/ab6761610000e5eb..."
}
```

**Exemplo de resposta (artista não encontrado):**
```json
{
  "erro": "Artista não encontrado"
}
```

---

## 🗄️ Banco de dados

O projeto usa **SQLite** com o arquivo `spotify.db` gerado automaticamente na primeira execução.

### Tabela `artistas`

| Coluna | Tipo | Descrição |
|---|---|---|
| `id` | INTEGER (PK) | ID interno auto-incrementado |
| `spotify_id` | VARCHAR(100) | ID único do Spotify |
| `nome` | VARCHAR(150) | Nome do artista |
| `spotify_url` | VARCHAR(300) | URL do perfil no Spotify |
| `imagem` | VARCHAR(500) | URL da foto do artista |

> O banco é criado automaticamente pelo SQLAlchemy ao iniciar o servidor (`Base.metadata.create_all`).

---

## 🔐 Autenticação com o Spotify

O projeto usa o fluxo **Client Credentials** da Spotify API:

1. As credenciais (`CLIENT_ID:CLIENT_SECRET`) são codificadas em **Base64**
2. Uma requisição `POST` é feita para `https://accounts.spotify.com/api/token`
3. O token de acesso retornado é usado nas requisições subsequentes
4. Esse fluxo **não requer login do usuário**, sendo ideal para consultas públicas

---

## 🧪 Testes

```bash
pytest tests/
```

---

## 📝 Notas

- O arquivo `spotify.db` é ignorado pelo `.gitignore` e **não é versionado**
- O arquivo `.env` com as credenciais **nunca deve ser commitado**
- A cada busca, o sistema verifica o banco primeiro para evitar chamadas desnecessárias à API do Spotify (cache local)
