import java.util.ArrayList;
import java.util.List;

public class Autor extends Pessoa {
    private List<Livro> livros;

    public Autor(String nome, int idade) {
        super(nome, idade);
        this.livros = new ArrayList<>();
    }

    public void adicionarLivro(Livro livro) {
        livros.add(livro);
    }

    public List<Livro> getLivros() {
        return livros;
    }
}
