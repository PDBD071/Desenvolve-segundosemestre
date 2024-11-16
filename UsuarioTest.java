import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class UsuarioTest {

    @Test
    public void testCriacaoUsuario() {
        Usuario usuario = new Usuario("Gabriel", 21);

        assertEquals("Gabriel", usuario.getNome());
        assertEquals(21, usuario.getIdade());
    }

    @Test
    public void testAlterarIdadeUsuario() {
        Usuario usuario = new Usuario("Gabriel", 21);
        usuario.setIdade(22);

        assertEquals(22, usuario.getIdade());
    }

    @Test
    public void testAlterarNomeUsuario() {
        Usuario usuario = new Usuario("Gabriel", 21);
        usuario.setNome("Gabriel Santos");

        assertEquals("Gabriel Santos", usuario.getNome());
    }
}


