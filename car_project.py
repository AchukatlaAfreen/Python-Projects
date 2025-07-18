import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚗 Car Dodging Game")

# Colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (200, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Car settings
car_width = 50
car_height = 90
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_speed = 7

# Obstacle settings
obstacle_width = 50
obstacle_height = 90
obstacle_speed = 7
obstacles = []

# Score
score = 0
font = pygame.font.SysFont("Arial", 36)

def draw_text(text, x, y, color=WHITE):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def draw_car(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, car_width, car_height))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, RED, (x, y, obstacle_width, obstacle_height))

def game_over():
    screen.fill(GRAY)
    draw_text("Game Over!", WIDTH // 2 - 100, HEIGHT // 2 - 50, RED)
    draw_text(f"Score: {score}", WIDTH // 2 - 80, HEIGHT // 2, WHITE)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# Game loop
running = True
while running:
    screen.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed

    # Generate obstacles
    if random.randint(1, 30) == 1:
        x_pos = random.randint(0, WIDTH - obstacle_width)
        obstacles.append([x_pos, -obstacle_height])

    # Move and draw obstacles
    for obs in obstacles[:]:
        obs[1] += obstacle_speed
        draw_obstacle(obs[0], obs[1])

        # Collision detection
        if (car_y < obs[1] + obstacle_height and
            car_y + car_height > obs[1] and
            car_x < obs[0] + obstacle_width and
            car_x + car_width > obs[0]):
            game_over()

        # Remove off-screen obstacles
        if obs[1] > HEIGHT:
            obstacles.remove(obs)
            score += 1
            if score % 10 == 0:
                obstacle_speed += 1  # Increase difficulty

    draw_car(car_x, car_y)
    draw_text(f"Score: {score}", 10, 10)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
