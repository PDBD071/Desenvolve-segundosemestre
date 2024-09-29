/* Defina um array de objetos, cujas as chaves serão id, titulo, autor e quantidade. 
Cada item representa um livro disponível na livraria.*/

const estoqueLivros = [
    {id: 2035, titulo: `Harry Porter`, quantidade: 12},
    {id: 3547, titulo: `Senhor dos anéis`, quantidade: 15},
    {id: 4426, titulo: `O Livro das Fadas`, quantidade: 20},
    {id: 9139, titulo: `O Programador Programático`, quantidade: 7},
];

/* Criar uma função para adicionar um livro ao estoque. essa função recebe como,
 título, autor e quantidade.*/

 const adicionarLivro =(id, titulo, autor, quantidade) => {
    estoqueLivros.push({
        id,
        titulo,
        autor,
        quantidade
    });
 }

 adicionarLivro(3437, `Código Limpo`, `Tio Bob`, 18);
 console.log(estoque);

 /* Criar uma função para remover livro do estoque. Essa função recebe como parâmetro o id. */

 const removeLivro = (idDoLivro) => {
    const existeIdNoEstoque = !!estoque.find(livro => livro.id === idDoLivro)
    console.log('existe?', existeIdNoEstoque)
    if(existeIdNoEstoque) {
        for(let indice = 0; indice < estoque.length; indice++) {
            if(estoque[indice].id === idDoLivro) {
                estoque.splice(indice, 1);
                console.log(`O livro de id ${idDoLivro} foi removido`);
                break;
            }
        }
    }
    else{
        console.log(`O livro de id ${idDoLivro} não foi encontrado`);
    }   
 } 
 removeLivro(4426);
 console.log(estoque);


 /*Criar uma função para atualizar a quantidade de um livro do estoque. Essa função recebe 
 como parâmetro o id, novaQuantidade.*/

 const atualizaQuantidade = (idDoLivro, novaQuantidade) => {
    const existeIdNoEstoque = !!estoque.find(livro => livro.id === idDoLivro)
    if(existeIdNoEstoque) {
    for (let livro of estoque) {
        if(livro.id === idDoLivro) {
            livro.quantidade = novaQuantidade;
            console.log(`A quantidade do livro ${livro.titulo} foi atualizada para ${novaQuantidade}`);
            break;
        }
    } 
    } else {
        console.log(`O id ${idDoLivro} não foi localizado no estoque`)
    }
 }

 atualizaQuantidade(2035, 1200);
 console.log(estoque);

 /* Criar uma função que lista os livros que estão no array */

 const listarLvros = () => {
    if(estoque.length === 0) {
        console.log(`O estoque está vazio`)
    } else {
        console.log(`O estoque possui ${estoque.length} títulos`)
        for (let livro of estoque) {
            console.log(`
            ID: ${livro.id}
            Livro: ${livro.titulo}
            Autor: ${livro.autor}
            Quantidade: ${livro.quanrtidade}
            `)
        }
    }
 }
listarLvros()