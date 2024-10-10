import java.util.Date;

public class Main {
    public static void main(String[] args) {
        // Criação do autor
        Autor autor = new Autor("Jessica Felix", 30);
        
        // Criação do livro
        Livro livro = new Livro("Java for Beginners", autor, "Tecnologia");
        autor.adicionarLivro(livro);

        // Criação do usuário
        Usuario usuario = new Usuario("Lucas Rafael", 25);
        
        // Criando datas de retirada e devolução
        Date dataRetirada = new Date(); // Data atual
        Date dataDevolucao = new Date(); // Pode ser ajustada conforme necessário

        // Realizando o empréstimo
        Emprestimo emprestimo = new Emprestimo(livro, usuario, dataRetirada, dataDevolucao);

        // Imprimindo informações
        System.out.println("O livro não está disponível");
        System.out.println("Livro: " + emprestimo.getLivro().getTitulo());
        System.out.println("Autor: " + emprestimo.getLivro().getAutor().getNome());
        System.out.println("Gênero: " + emprestimo.getLivro().getGenero());
        System.out.println("Usuário: " + emprestimo.getUsuario().getNome());
        System.out.println("Idade: " + emprestimo.getUsuario().getIdade());
        System.out.println("Data de Retirada: " + emprestimo.getDataRetirada());
        System.out.println("Data de Devolução: " + emprestimo.getDataDevolucao());
    }
}


