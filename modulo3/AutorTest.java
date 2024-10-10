import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class AutorTest {

    @Test
    public void testCriacaoAutor() {
        Autor autor = new Autor("Jess", "Brasileira");

        assertEquals("Jess", autor.getNome());
        assertEquals("Brasileira", autor.getNacionalidade());
    }

    @Test
    public void testAlterarNomeAutor() {
        Autor autor = new Autor("Jess", "Brasileira");
        autor.setNome("Jessica");

        assertEquals("Jessica", autor.getNome());
    }
}




