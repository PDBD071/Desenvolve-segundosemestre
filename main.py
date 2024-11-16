import keyboard  # Usando a biblioteca keyboard para detectar as teclas
import time  # Importando a biblioteca time para usar time.sleep()

# Função para mover o jogador
def mover_jogador(direcao, jogador):
    if direcao == 'w':  # cima
        jogador['posicao'][0] -= 1
    elif direcao == 'a':  # esquerda
        jogador['posicao'][1] -= 1
    elif direcao == 's':  # baixo
        jogador['posicao'][0] += 1
    elif direcao == 'd':  # direita
        jogador['posicao'][1] += 1

# Função principal do jogo
def jogar():
    jogador = {
        'nome': input("Digite o nome do jogador: "),
        'posicao': [1, 2]  # Posição inicial do jogador no labirinto
    }
    print(f"Jogador {jogador['nome']} no labirinto!")

    while True:
        # Espera pelo evento de tecla pressionada
        event = keyboard.read_event(suppress=True)  # Espera por um evento de teclado

        # Se a tecla pressionada for 'esc', o jogo é encerrado
        if event.name == 'esc' and event.event_type == keyboard.KEY_DOWN:
            print("Saindo do jogo!")
            break  # Sai do loop e encerra o jogo

        # Verifica qual direção foi pressionada
        direcao = None
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'w':
                direcao = 'w'
            elif event.name == 'a':
                direcao = 'a'
            elif event.name == 's':
                direcao = 's'
            elif event.name == 'd':
                direcao = 'd'
        
        # Movimenta o jogador se uma direção válida for pressionada
        if direcao:
            mover_jogador(direcao, jogador)
            print(f"Jogador {jogador['nome']} se moveu para a posição {jogador['posicao']}")
        elif event.event_type == keyboard.KEY_DOWN:  # Se a tecla pressionada não for válida
            print("Direção inválida! Use 'w', 'a', 's', 'd' para mover.")
        
        # Pequena pausa para reduzir a carga do processador
        time.sleep(0.1)

# Chama a função jogar para iniciar o jogo
if __name__ == "__main__":
    jogar()
