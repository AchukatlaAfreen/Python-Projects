import pygame
import time
import random


pygame.init()


WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)


BLOCK_SIZE = 20
SPEED = 15
clock = pygame.time.Clock()

font = pygame.font.SysFont("bahnschrift", 25)

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, BLACK, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    text = font.render(msg, True, color)
    win.blit(text, [WIDTH / 6, HEIGHT / 3])

def game_loop():
    game_over = False
    game_close = False

    
    x = WIDTH / 2
    y = HEIGHT / 2


    dx = 0
    dy = 0

    snake_list = []
    snake_length = 1

    
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    score = 0

    while not game_over:

        while game_close:
            win.fill(WHITE)
            message("You Lost! Press C-Play Again or Q-Quit", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -BLOCK_SIZE
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = BLOCK_SIZE
                    dx = 0

        
        x += dx
        y += dy

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        win.fill(WHITE)
        pygame.draw.rect(win, GREEN, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        head = [x, y]
        snake_list.append(head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        
        for segment in snake_list[:-1]:
            if segment == head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)

        
        score_text = font.render(f"Score: {score}", True, BLUE)
        win.blit(score_text, [10, 10])

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1
            score += 1

        clock.tick(SPEED)

    pygame.quit()
    quit()


game_loop()

