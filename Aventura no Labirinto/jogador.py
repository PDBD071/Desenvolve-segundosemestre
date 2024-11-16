# jogador.py

def iniciar_jogador(nome):
    """
    Função que inicializa o jogador com nome e posição inicial (1, 1).
    A posição (1, 1) é dentro do labirinto no espaço livre.
    """
    return {'nome': nome, 'posicao': (1, 1)}

def mover_jogador(jogador, direcao, labirinto):
    """
    Função que move o jogador dentro do labirinto com base na direção fornecida.
    Impede o movimento para fora do labirinto e verifica se a posição não está fora dos limites.
    """
    x, y = jogador['posicao']
    max_x = len(labirinto[0]) - 1  # Colunas do labirinto (última posição x válida)
    max_y = len(labirinto) - 1      # Linhas do labirinto (última posição y válida)

    # Verificação de movimento para cima (w)
    if direcao == 'w':  # Mover para cima
        if y > 0 and labirinto[y-1][x] != '#':  # Não ultrapassar a borda superior
            jogador['posicao'] = (x, y - 1)
        else:
            print("Movimento inválido! Você atingiu uma parede ou está fora do labirinto.")
    
    # Verificação de movimento para baixo (s)
    elif direcao == 's':  # Mover para baixo
        if y < max_y and labirinto[y+1][x] != '#':  # Não ultrapassar a borda inferior
            jogador['posicao'] = (x, y + 1)
        else:
            print("Movimento inválido! Você atingiu uma parede ou está fora do labirinto.")
    
    # Verificação de movimento para esquerda (a)
    elif direcao == 'a':  # Mover para a esquerda
        if x > 0 and labirinto[y][x-1] != '#':  # Não ultrapassar a borda esquerda
            jogador['posicao'] = (x - 1, y)
        else:
            print("Movimento inválido! Você atingiu uma parede ou está fora do labirinto.")
    
    # Verificação de movimento para direita (d)
    elif direcao == 'd':  # Mover para a direita
        if x < max_x and labirinto[y][x+1] != '#':  # Não ultrapassar a borda direita
            jogador['posicao'] = (x + 1, y)
        else:
            print("Movimento inválido! Você atingiu uma parede ou está fora do labirinto.")
    
    # Caso a direção não seja reconhecida
    else:
        print("Direção inválida! Use 'w', 'a', 's', 'd' para mover.")
    
    # Exibe a nova posição do jogador
    print(f"Jogador {jogador['nome']} se moveu para a posição {jogador['posicao']}")
