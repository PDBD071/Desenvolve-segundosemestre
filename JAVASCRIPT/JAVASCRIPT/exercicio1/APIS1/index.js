document.getElementById('searchButton').addEventListener('click', async () => {
    const username = document.getElementById('username').value;
    const userList = document.getElementById('userList');
    const noResults = document.getElementById('noResults');
    
    userList.innerHTML = ''; // Limpa a lista anterior
    noResults.style.display = 'none'; // Oculta a mensagem de "não encontrados"
    
    if (username.trim() === '') {
        alert('Por favor, insira um nome de usuário.');
        return;
    }

    try {
        const response = await fetch(`https://api.github.com/search/users?q=${username}`);
        const data = await response.json();
        
        if (data.total_count > 0) {
            data.items.forEach(user => {
                const listItem = document.createElement('li');
                listItem.textContent = `${user.login} - ${user.html_url}`;
                userList.appendChild(listItem);
            });
        } else {
            noResults.style.display = 'block'; // Exibe a mensagem se não encontrou usuários
        }
    } catch (error) {
        console.error('Erro ao buscar usuários:', error);
    }
});
