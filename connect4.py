import pygame

# Constants
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
TILE_SIZE = 100
MARGIN = 10

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Initialize pygame
pygame.init()

# Set the width and height of the screen
screen_width = BOARD_WIDTH * TILE_SIZE + (BOARD_WIDTH - 1) * MARGIN
screen_height = BOARD_HEIGHT * TILE_SIZE + (BOARD_HEIGHT - 1) * MARGIN
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the caption of the window
pygame.display.set_caption("Connect Four")

# Create a 2D array to represent the game board
board = [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

# Initialize the game
current_player = "red"
game_over = False

# Run the game loop
while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the column that was clicked
            column = event.pos[0] // (TILE_SIZE + MARGIN)
            # Find the first empty row in the column
            for row in range(BOARD_HEIGHT):
                if board[row][column] is None:
                    board[row][column] = current_player
                    break
            # Switch players
            current_player = "red" if current_player == "yellow" else "yellow"
    # Draw the board
    screen.fill(BLACK)
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            color = RED if board[row][col] == "red" else YELLOW
            pygame.draw.circle(
                screen,
                color,
                (
                    col * (TILE_SIZE + MARGIN) + TILE_SIZE // 2,
                    row * (TILE_SIZE + MARGIN) + TILE_SIZE // 2,
                ),
                TILE_SIZE // 2 - MARGIN,
            )
    pygame.display.flip()

# Quit pygame
pygame.quit()
