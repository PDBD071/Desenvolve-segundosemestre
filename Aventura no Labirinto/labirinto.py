# labirinto.py

def criar_labirinto():
    """
    Função que cria um labirinto simples (matriz 2D) com paredes (#) e espaço livre (.).
    """
    return [
        ['#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '#'],
        ['#', '.', '#', '.', '#'],
        ['#', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#']
    ]

def imprimir_labirinto(labirinto):
    """
    Função que imprime o labirinto no terminal.
    """
    for linha in labirinto:
        print(' '.join(linha))
