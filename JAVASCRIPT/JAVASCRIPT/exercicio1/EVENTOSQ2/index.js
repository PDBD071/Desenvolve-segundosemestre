// Array para armazenar os nomes
const likedNames = [];

// Função para atualizar a lista de curtidas
function updateLikeList() {
    const likeListElement = document.getElementById('likeList');

    if (likedNames.length === 0) {
        likeListElement.textContent = 'Ninguém curtiu';
    } else if (likedNames.length === 1) {
        likeListElement.textContent = `${likedNames[0]} curtiu`;
    } else if (likedNames.length === 2) {
        likeListElement.textContent = `${likedNames[0]} e ${likedNames[1]} curtiram`;
    } else {
        likeListElement.textContent = `${likedNames[0]}, ${likedNames[1]} e mais ${likedNames.length - 2} pessoas curtiram`;
    }
}

// Função para lidar com o clique no botão "Curtir"
document.getElementById('likeButton').addEventListener('click', () => {
    const nameInput = document.getElementById('nameInput').value.trim();
    
    // Verifica se o nome não está vazio e não está na lista
    if (nameInput && !likedNames.includes(nameInput)) {
        likedNames.push(nameInput);
        updateLikeList();
    }

    // Limpa o campo de texto
    document.getElementById('nameInput').value = '';
});
