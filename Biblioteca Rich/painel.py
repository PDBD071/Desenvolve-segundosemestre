from rich.console import Console
from rich.panel import Panel
import os

console = Console()

def exibir_com_painel(texto: str, isArquivo: bool):
    """
    Exibe o texto dentro de um painel com o título "Painel de Texto".
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
    painel = Panel(texto, title="Painel de Texto", style="bold yellow")
    console.print(painel)

def exibir_em_painel_com_borda(texto: str, isArquivo: bool):
    """
    Exibe o texto dentro de um painel com borda e padding personalizado.
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
    painel = Panel(texto, title="Painel com Borda", border_style="blue", padding=(1, 2))
    console.print(painel)

