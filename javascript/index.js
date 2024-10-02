// Função para mudar o título
const mudaTitulo = (novoTitulo) => {
    const titulo = document.getElementById('titulo-principal');
    titulo.innerText = novoTitulo;
}

// Altera o título após 2 segundos
setTimeout(() => mudaTitulo('Oba! Alterei o título da página'), 2000);

// Seleciona os itens da lista e os parágrafos
const listaDeLi = document.getElementsByTagName('li');
const listaDeCores = ['#d60000', '#05f7ab']; // Cores para os itens da lista
const listaDeParagrafos = document.getElementsByTagName('p');

// Botão de manipulação
const botao = document.getElementById('Botao');

// Altera o botão após 3 segundos
setTimeout(() => {
    botao.innerText = 'Clique com o novo texto';
    botao.style.fontSize = '30px';
}, 3000);

// Adiciona a classe "paragrafo" a todos os parágrafos
for (let paragrafo of listaDeParagrafos) {
    paragrafo.classList.add('paragrafo');
}

// Aplica cores aos itens da lista
for (let i = 0; i < listaDeLi.length; i++) {
    listaDeLi[i].style.color = listaDeCores[i % listaDeCores.length];
}

    
   
   
       
