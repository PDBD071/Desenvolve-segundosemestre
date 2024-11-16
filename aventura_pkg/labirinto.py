"""
Este módulo contém a lógica do labirinto no jogo Aventura no Labirinto.
Ele inclui funções para criar e imprimir um labirinto simples,
assim como mover o jogador dentro do labirinto.
"""

def criar_labirinto():
    """
    Função que cria um labirinto simples (matriz 2D) com paredes (#) e espaço livre (.).
    
    :return: Lista 2D representando o labirinto.
    :rtype: list[list[str]]
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
    
    :param labirinto: A matriz 2D representando o labirinto.
    :type labirinto: list[list[str]]
    """
    for linha in labirinto:
        print(' '.join(linha))

def mover_jogador(x, y):
    """
    Move o jogador para a nova posição (x, y).
    
    :param x: Nova posição na direção x.
    :param y: Nova posição na direção y.
    :return: None
    """
    pass
