const postForm = document.getElementById('postForm');
const postsList = document.getElementById('postsList');
let posts = [];

// Função para gerar uma imagem aleatória de gatinho da API
async function getRandomCatImage() {
    const response = await fetch('https://api.thecatapi.com/v1/images/search');
    const data = await response.json();
    return data[0].url;
}

// Função para adicionar uma nova postagem
async function addPost(username, avatarUrl, text) {
    const post = {
        date: new Date(),
        username: username, // O nome de usuário digitado
        avatar: avatarUrl || 'https://www.w3schools.com/w3images/avatar6.png', // Avatar padrão feminino
        text: text,
        catImage: await getRandomCatImage(),
        likes: 0
    };
    posts.unshift(post); // Adiciona a postagem mais recente no início
    renderPosts();
}

// Função para renderizar as postagens
function renderPosts() {
    postsList.innerHTML = '';
    posts.forEach((post, index) => {
        const postElement = document.createElement('li');
        postElement.classList.add('post');
        postElement.innerHTML = `
            <div class="post-header">
                <img class="avatar" src="${post.avatar}" alt="Avatar">
                <div>
                    <strong>${post.username}</strong>
                    <small>${post.date.toLocaleString()}</small>
                </div>
            </div>
            <p>${post.text}</p>
            <img class="cat-image" src="${post.catImage}" alt="Cat Image">
            <button class="like-button" onclick="likePost(${index})">Curtir (${post.likes})</button>
        `;
        postsList.appendChild(postElement);
    });
}

// Função para curtir uma postagem
function likePost(index) {
    posts[index].likes++;
    renderPosts();
}

// Evento de envio do formulário
postForm.addEventListener('submit', function (e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const avatarUrl = document.getElementById('avatarUrl').value;
    const postContent = document.getElementById('postContent').value;
    if (username.trim() && postContent.trim()) {
        addPost(username, avatarUrl, postContent);
        postForm.reset(); // Limpa o formulário após a postagem
    }
});
