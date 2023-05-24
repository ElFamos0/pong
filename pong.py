import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des constantes
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
BALL_SIZE = 10
PADDLE_SPEED = 5
BALL_SPEED = 3

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Création des objets
left_paddle = pygame.Rect(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_dx, ball_dy = BALL_SPEED, BALL_SPEED

while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mise à jour des objets
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < SCREEN_HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < SCREEN_HEIGHT:
        right_paddle.y += PADDLE_SPEED

    ball.x += ball_dx
    ball.y += ball_dy

    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_dx = -ball_dx
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_dy = -ball_dy

    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
        ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2

    # Dessin des objets
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    # Rafraîchissement de l'écran
    pygame.display.flip()
    pygame.time.delay(16)  # Contrôle de la vitesse du jeu