// Função para atualizar a exibição da lista de pessoas que curtiram
function updateLikesDisplay() {
    const likesDisplay = document.getElementById('likesDisplay');
    const persons = JSON.parse(localStorage.getItem('persons')) || []; // Obtém a lista do localStorage

    // Atualiza a exibição de acordo com a quantidade de pessoas
    if (persons.length === 0) {
        likesDisplay.textContent = 'Ninguém curtiu';
    } else if (persons.length === 1) {
        likesDisplay.textContent = `${persons[0]} curtiu`;
    } else if (persons.length === 2) {
        likesDisplay.textContent = `${persons[0]} e ${persons[1]} curtiram`;
    } else {
        likesDisplay.textContent = `${persons[0]}, ${persons[1]} e mais ${persons.length - 2} pessoas curtiram`;
    }
}

// Evento para adicionar uma nova pessoa
document.getElementById('likeButton').addEventListener('click', () => {
    const personName = document.getElementById('personName').value.trim();
    if (personName) {
        const persons = JSON.parse(localStorage.getItem('persons')) || []; // Obtém a lista atual

        // Verifica se o nome já está na lista
        if (!persons.includes(personName)) {
            persons.push(personName); // Adiciona o novo nome à lista
            localStorage.setItem('persons', JSON.stringify(persons)); // Salva a lista no localStorage
            document.getElementById('personName').value = ''; // Limpa o campo de texto
            updateLikesDisplay(); // Atualiza a exibição
        } else {
            alert('Essa pessoa já curtiu!');
        }
    } else {
        alert('Por favor, insira um nome.');
    }
});

// Evento para limpar o localStorage
document.getElementById('clearStorageButton').addEventListener('click', () => {
    localStorage.removeItem('persons'); // Remove a lista do localStorage
    updateLikesDisplay(); // Atualiza a exibição
});

// Renderiza a lista inicialmente
updateLikesDisplay();

  
