import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BROWN = (139, 69, 19)

# Clock
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Basket settings
basket_width, basket_height = 100, 20
basket = pygame.Rect(WIDTH//2 - basket_width//2, HEIGHT - 40, basket_width, basket_height)
basket_speed = 7

# Ball settings
ball_radius = 15
ball = pygame.Rect(random.randint(0, WIDTH - ball_radius), 0, ball_radius, ball_radius)
ball_speed = 5

# Game variables
score = 0
missed = 0
max_missed = 5

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Basket Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket.left > 0:
        basket.x -= basket_speed
    if keys[pygame.K_RIGHT] and basket.right < WIDTH:
        basket.x += basket_speed

    # Ball Movement
    ball.y += ball_speed

    # Collision Check
    if basket.colliderect(ball):
        score += 1
        ball.y = 0
        ball.x = random.randint(0, WIDTH - ball_radius)

    # Missed Ball
    if ball.y > HEIGHT:
        missed += 1
        ball.y = 0
        ball.x = random.randint(0, WIDTH - ball_radius)

    # Draw basket
    pygame.draw.rect(screen, BROWN, basket)

    # Draw ball
    pygame.draw.circle(screen, RED, (ball.x + ball_radius//2, ball.y + ball_radius//2), ball_radius)

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    missed_text = font.render(f"Missed: {missed}/{max_missed}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(missed_text, (10, 40))

    # Game over
    if missed >= max_missed:
        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH//2 - 80, HEIGHT//2))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
