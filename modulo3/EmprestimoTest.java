import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Date;

public class EmprestimoTest {
    
    @Test
    public void testCriacaoEmprestimo() {
        Date dataRetirada = new Date();
        Date dataDevolucao = new Date();
        Livro livro = new Livro("Java Basics", new Autor("Alan Turing", "Inglês"), "Tecnologia", true);
        Usuario usuario = new Usuario("Gabriel", 21);
        
        Emprestimo emprestimo = new Emprestimo(livro, usuario, dataRetirada, dataDevolucao);
        
        assertEquals(livro, emprestimo.getLivro());
        assertEquals(usuario, emprestimo.getUsuario());
        assertEquals(dataRetirada, emprestimo.getDataRetirada());
        assertEquals(dataDevolucao, emprestimo.getDataDevolucao());
    }
    
    @Test
    public void testEmprestimoAtivo() {
        Date dataRetirada = new Date();
        Date dataDevolucao = null;  // Indica que ainda não foi devolvido
        Livro livro = new Livro("Java Basics", new Autor("Alan Turing", "Inglês"), "Tecnologia", true);
        Usuario usuario = new Usuario("Gabriel", 21);
        
        Emprestimo emprestimo = new Emprestimo(livro, usuario, dataRetirada, dataDevolucao);
        
        assertTrue(emprestimo.isAtivo());
    }
}

