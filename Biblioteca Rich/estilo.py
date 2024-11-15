from rich.console import Console
from rich.text import Text
import os

console = Console()

def exibir_texto_com_estilo(texto: str, isArquivo: bool):
    """
    Exibe o texto com estilo de negrito, sublinhado e cor verde.
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
    texto_formatado = Text(texto, style="bold underline green")
    console.print(texto_formatado)

def exibir_texto_em_vermelho(texto: str, isArquivo: bool):
    """
    Exibe o texto com estilo de negrito e cor vermelha.
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
    texto_formatado = Text(texto, style="bold red")
    console.print(texto_formatado)
