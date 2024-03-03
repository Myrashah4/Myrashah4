# Make sure you have Pygame installed. If not, you can install it using:
# pip install pygame
#Tic Tac Toe 2 person game using python
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
CELL_SIZE = WIDTH // 3
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
FONT_SIZE = 36

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Initialize the board
board = [[" " for _ in range(3)] for _ in range(3)]
players = ["X", "O"]
current_player = 0

# Load font
font = pygame.font.Font(None, FONT_SIZE)

def draw_board():
    """
    Draw the tic-tac-toe board.
    """
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 2)
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 2)

def draw_marks():
    """
    Draw X and O marks on the board.
    """
    for row in range(3):
        for col in range(3):
            mark = board[row][col]
            if mark == "X":
                x_pos = col * CELL_SIZE + CELL_SIZE // 2
                y_pos = row * CELL_SIZE + CELL_SIZE // 2
                pygame.draw.line(screen, LINE_COLOR, (x_pos - 30, y_pos - 30), (x_pos + 30, y_pos + 30), 2)
                pygame.draw.line(screen, LINE_COLOR, (x_pos - 30, y_pos + 30), (x_pos + 30, y_pos - 30), 2)
            elif mark == "O":
                pygame.draw.circle(screen, LINE_COLOR, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), 30, 2)

def check_winner():
    """
    Checks if the current player has won.
    """
    for row in board:
        if all(cell == players[current_player] for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == players[current_player] for row in range(3)):
            return True

    if board[0][0] == board[1][1] == board[2][2] == players[current_player]:
        return True

    if board[0][2] == board[1][1] == board[2][0] == players[current_player]:
        return True

    return False

def main():
    global current_player

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = y // CELL_SIZE, x // CELL_SIZE

                if board[row][col] == " ":
                    board[row][col] = players[current_player]
                    current_player = (current_player + 1) % 2

        screen.fill(WHITE)
        draw_board()
        draw_marks()

        if check_winner():
            winner_text = font.render(f"Player {players[current_player]} wins!", True, LINE_COLOR)
            screen.blit(winner_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
        elif all(cell != " " for row in board for cell in row):
            tie_text = font.render("It's a tie!", True, LINE_COLOR)
            screen.blit(tie_text, (WIDTH // 2 - 50, HEIGHT // 2 - 20))

        pygame.display.flip()

if __name__ == "__main__":
    main()
