import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


font = pygame.font.SysFont(None, 60)


board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False

def draw_grid():
    
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), LINE_WIDTH)
    
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), LINE_WIDTH)

def draw_marks():
    for row in range(3):
        for col in range(3):
            mark = board[row][col]
            if mark != "":
                text = font.render(mark, True, BLACK)
                screen.blit(text, (col * 100 + 30, row * 100 + 20))

def check_winner(player):
   
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player: return True
        if board[0][i] == board[1][i] == board[2][i] == player: return True
    if board[0][0] == board[1][1] == board[2][2] == player: return True
    if board[0][2] == board[1][1] == board[2][0] == player: return True
    return False

def is_board_full():
    return all(board[row][col] != "" for row in range(3) for col in range(3))

def show_winner(message):
    global game_over
    text = font.render(message, True, BLACK)
    screen.fill(WHITE)
    screen.blit(text, (50, 120))
    pygame.display.update()
    pygame.time.wait(2000)
    game_over = True

def restart_game():
    global board, current_player, game_over
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False
    screen.fill(WHITE)
    draw_grid()


screen.fill(WHITE)
draw_grid()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row = y // 100
            col = x // 100

            if board[row][col] == "":
                board[row][col] = current_player
                if check_winner(current_player):
                    show_winner(f"{current_player} wins!")
                elif is_board_full():
                    show_winner("It's a tie!")
                else:
                    current_player = "O" if current_player == "X" else "X"

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()

    draw_marks()
    pygame.display.update()

