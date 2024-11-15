from rich.console import Console
from rich.progress import Progress
import os

console = Console()

def exibir_progresso(texto: str, isArquivo: bool):
    """
    Exibe uma barra de progresso enquanto lê o conteúdo de um arquivo.
    Caso o texto não seja um arquivo, ele apenas será impresso.

    Args:
    texto (str): Texto ou caminho para o arquivo a ser exibido.
    isArquivo (bool): Determina se o texto é o caminho de um arquivo. Se verdadeiro, o conteúdo do arquivo será lido.
    """
    if isArquivo:
        if os.path.exists(texto):
            with open(texto, 'r') as file:
                linhas = file.readlines()
                total_linhas = len(linhas)
                
                with Progress() as progress:
                    tarefa = progress.add_task("[cyan]Lendo arquivo...", total=total_linhas)
                    for i, linha in enumerate(linhas):
                        progress.update(tarefa, advance=1)
                        if i % 10 == 0:  # Exibe a cada 10 linhas
                            console.print(linha.strip(), style="green")
                    console.print(f"[bold yellow]Leitura completa![/bold yellow]")
        else:
            console.print("Arquivo não encontrado!", style="bold red")
    else:
        console.print(texto, style="bold red")

def exibir_progresso_simples(texto: str, isArquivo: bool):
    """
    Exibe uma barra de progresso simples sem ler o arquivo.
    Exibe uma mensagem de progresso para o texto fornecido.

    Args:
    texto (str): Texto a ser exibido ao final do progresso.
    isArquivo (bool): Este parâmetro não é utilizado neste caso, mas está presente para manter a consistência.
    """
    with Progress() as progress:
        tarefa = progress.add_task("[cyan]Carregando...", total=100)
        for _ in range(100):
            progress.update(tarefa, advance=1)
        console.print(f"[bold green]{texto} carregado com sucesso![/bold green]")
