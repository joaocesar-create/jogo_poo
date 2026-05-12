import pygame
import random

pygame.init()
pygame.mixer.init()  # 🎼 inicializa áudio

# 🎵 Música de fundo
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.set_volume(0.5)  # volume de 0.0 a 1.0
pygame.mixer.music.play(-1)  # loop infinito

# Tela
LARGURA = 600
ALTURA = 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Desvie dos Inimigos")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Jogador
player_x = 250
player_y = 300
player_largura = 50
player_altura = 50
velocidade = 5

# Inimigo
enemy_x = random.randint(0, LARGURA - 50)
enemy_y = 0
enemy_vel = 5

# Loop do jogo
rodando = True
clock = pygame.time.Clock()

while rodando:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        player_x -= velocidade
    if teclas[pygame.K_RIGHT]:
        player_x += velocidade

    # Movimento inimigo
    enemy_y += enemy_vel

    if enemy_y > ALTURA:
        enemy_y = 0
        enemy_x = random.randint(0, LARGURA - 50)

    # Colisão
    if (player_x < enemy_x + 50 and
        player_x + player_largura > enemy_x and
        player_y < enemy_y + 50 and
        player_y + player_altura > enemy_y):
        print("💀 Game Over!")
        rodando = False

    # Desenho
    tela.fill(BRANCO)
    pygame.draw.rect(tela, AZUL, (player_x, player_y, player_largura, player_altura))
    pygame.draw.rect(tela, VERMELHO, (enemy_x, enemy_y, 50, 50))

    pygame.display.update()

pygame.quit()
