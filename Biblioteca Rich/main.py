import argparse
from layout import exibir_texto_com_layout
from painel import exibir_com_painel
from progresso import exibir_progresso
from estilo import exibir_texto_com_estilo


def main():
    # Configurando o parser de argumentos
    parser = argparse.ArgumentParser(description="Personalize o texto com recursos de layout, painel, progresso e estilo.")
    
    # Argumento obrigatório: texto ou caminho para arquivo
    parser.add_argument("texto", help="Texto a ser exibido ou caminho para o arquivo de texto.")
    
    # Opção para ativar a leitura de arquivo
    parser.add_argument("-a", "--arquivo", action="store_true", help="Ativa a leitura de um arquivo de texto.")
    
    # Opção para escolher o módulo
    parser.add_argument("-m", "--modulo", choices=["layout", "painel", "progresso", "estilo"], required=True, 
                        help="Escolha o módulo a ser usado.")
    
    # Opção para escolher a função dentro do módulo
    parser.add_argument("-f", "--funcao", choices=["exibir_texto_com_layout", "exibir_com_painel", "exibir_progresso", "exibir_texto_com_estilo"], required=True, 
                        help="Escolha a função a ser executada.")
    
    # Parse dos argumentos
    args = parser.parse_args()
    
    # Função que verifica se o texto é de um arquivo
    def ler_texto(texto, is_arquivo):
        """Lê o texto de um arquivo ou usa o texto diretamente."""
        if is_arquivo:
            try:
                with open(texto, 'r') as f:
                    return f.read()
            except FileNotFoundError:
                print(f"Arquivo '{texto}' não encontrado.")
                return ""
        return texto
    
    # Lê o texto, se necessário
    texto_a_exibir = ler_texto(args.texto, args.arquivo)
    
    # Verificar qual módulo e função executar
    if args.modulo == "layout":
        if args.funcao == "exibir_texto_com_layout":
            # Passando o parâmetro isArquivo para a função exibir_texto_com_layout
            exibir_texto_com_layout(texto_a_exibir, args.arquivo)  # Adicionado args.arquivo aqui
    
    elif args.modulo == "painel":
        if args.funcao == "exibir_com_painel":
            # Passando o parâmetro isArquivo para a função exibir_com_painel
            exibir_com_painel(texto_a_exibir, args.arquivo)
    
    elif args.modulo == "progresso":
        if args.funcao == "exibir_progresso":
            # Passando o parâmetro isArquivo para a função exibir_progresso
            exibir_progresso(texto_a_exibir, args.arquivo)
    
    elif args.modulo == "estilo":
        if args.funcao == "exibir_texto_com_estilo":
            # Passando o parâmetro isArquivo para a função exibir_texto_com_estilo
            exibir_texto_com_estilo(texto_a_exibir, args.arquivo)


if __name__ == "__main__":
    main()


