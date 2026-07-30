console.log("scripts.js carregado!");

window.buscar = async function () {

    const nome = document.getElementById("artista").value.trim();

    if (!nome) {
        alert("Digite o nome de um artista.");
        return;
    }

    try {

        const resposta = await fetch(`/artista/${encodeURIComponent(nome)}`);

        if (!resposta.ok) {
            throw new Error("Erro ao buscar artista.");
        }

        const artista = await resposta.json();

        document.getElementById("resultado").innerHTML = `
            <div class="card">

                <img src="${artista.imagem}" alt="${artista.nome}">

                <h2>${artista.nome}</h2>

                <p><strong>ID:</strong> ${artista.id}</p>

                <p><strong>Seguidores:</strong> ${artista.seguidores.toLocaleString()}</p>

                <p><strong>Popularidade:</strong> ${artista.popularidade}</p>

                <p><strong>Gêneros:</strong> ${artista.generos.join(", ")}</p>

                <a href="${artista.spotify_url}" target="_blank">
                    Abrir no Spotify
                </a>

            </div>
        `;

    } catch (erro) {

        console.error(erro);

        document.getElementById("resultado").innerHTML = `
            <p>Erro ao buscar o artista.</p>
        `;
    }

}