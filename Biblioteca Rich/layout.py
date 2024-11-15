from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import os

console = Console()

def exibir_texto_com_layout(texto: str, isArquivo: bool):
    """
    Exibe o texto dentro de um painel com o título "Painel de Layout".
    O texto pode ser fornecido diretamente ou lido de um arquivo.

    Args:
    texto (str): Texto ou caminho para o arquivo a ser exibido.
    isArquivo (bool): Determina se o texto é o caminho de um arquivo. Se verdadeiro, o conteúdo do arquivo será lido.
    """
    if isArquivo:
        if os.path.exists(texto):
            with open(texto, 'r') as file:
                texto = file.read()
        else:
            console.print("Arquivo não encontrado!", style="bold red")
            return
    texto_formatado = Text(texto)
    panel = Panel(texto_formatado, title="Painel de Layout", border_style="green")
    console.print(panel)

def exibir_secao(texto: str, isArquivo: bool):
    """
    Exibe o texto dentro de uma seção com estilo.
    O texto pode ser fornecido diretamente ou lido de um arquivo.

    Args:
    texto (str): Texto ou caminho para o arquivo a ser exibido.
    isArquivo (bool): Determina se o texto é o caminho de um arquivo. Se verdadeiro, o conteúdo do arquivo será lido.
    """
    if isArquivo:
        if os.path.exists(texto):
            with open(texto, 'r') as file:
                texto = file.read()
        else:
            console.print("Arquivo não encontrado!", style="bold red")
            return
    texto_formatado = Text(texto)
    console.print(f"[bold cyan]Seção:[/bold cyan] {texto_formatado}")

