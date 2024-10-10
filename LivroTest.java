import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class LivroTest {

    @Test
    public void testCriacaoLivro() {
        Autor autor = new Autor("Jess", "Brasileira");
        Livro livro1 = new Livro("Java Basico", autor, "tecnologia", true);

        assertEquals("Java Basico", livro1.getTitulo());
        assertEquals("tecnologia", livro1.getGenero());
        assertTrue(livro1.isDisponivel());
    }

    @Test
    public void testAlterarDisponibilidade() {
        Autor autor = new Autor("Jess", "Brasileira");
        Livro livro2 = new Livro("Java Avançado", autor, "tecnologia", false);
        
        livro2.setDisponivel(true);
        
        assertTrue(livro2.isDisponivel());
    }

    @Test
    public void testGetAutor() {
        Autor autor = new Autor("Jess", "Brasileira");
        Livro livro1 = new Livro("Java Basico", autor, "tecnologia", true);

        assertEquals(autor, livro1.getAutor());
    }
}


