import pygame

# Constants for the game board
BOARD_WIDTH = 300
BOARD_HEIGHT = 300
CELL_SIZE = 100

# Initialize Pygame
pygame.init()

# Set up the game window
window = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load the X and O images
x_img = pygame.image.load('x.png')
x_img = pygame.transform.scale(x_img, (CELL_SIZE, CELL_SIZE))
o_img = pygame.image.load('o.png')
o_img = pygame.transform.scale(o_img, (CELL_SIZE, CELL_SIZE))

# Initialize the game board
board = [[None, None, None] for _ in range(3)]

# Initialize the current player (X starts first)
current_player = 'X'

# Flag to track if the game is over
game_over = False

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_x, mouse_y = event.pos
            # Calculate the row and column of the clicked cell
            row = mouse_y // CELL_SIZE
            col = mouse_x // CELL_SIZE
            # Place the current player's symbol in the clicked cell
            if board[row][col] is None:
                board[row][col] = current_player
                # Switch to the other player
                current_player = 'O' if current_player == 'X' else 'X'
        elif event.type == pygame.KEYDOWN:
            # Reset the game if the user presses the space bar
            if event.key == pygame.K_SPACE:
                board = [[None, None, None] for _ in range(3)]
                current_player = 'X'
                game_over = False
    
    # Draw the game board
    window.fill(BLACK)
    for row in range(3):
    # Draw the grid lines
      for i in range(1, 3):
    # Vertical lines
        pygame.draw.line(window, WHITE, (i * CELL_SIZE, 0), (i * CELL_SIZE, BOARD_HEIGHT), 1)
    # Horizontal lines
        pygame.draw.line(window, WHITE, (0, i * CELL_SIZE), (BOARD_WIDTH, i * CELL_SIZE), 1)
  
        for col in range(3):
            # Get the symbol at this position
            symbol = board[row][col]
            # Calculate the top-left corner of the cell
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            if symbol == 'X':
                # Draw the X image
                window.blit(x_img, (x, y))
            elif symbol == 'O':
                # Draw the O image
                window.blit(o_img, (x, y))
            else:
                # Draw a white square for an empty cell
                pygame.draw.rect(window, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
    
    # Check for a winner
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            # There is a winner along this row
            game_over = True
            winner = board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            # There is a winner along this column
            game_over = True
            winner = board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        # There is a winner along the diagonal
        game_over = True
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        # There is a winner along the other diagonal
        game_over = True
        winner = board[0][2]
    
    # Check for a tie
    if not any(None in row for row in board):
        # The board is full and there is no winner, so it's a tie
        game_over = True
        winner = None
    
    # Display the winner (if any)
    if game_over:
        if winner is None:
            # It's a tie
            message = 'It\'s a tie!'
        else:
            # There is a winner
            message = f'{winner} wins!'
        # Render the message as an image
        font = pygame.font.Font(None, 36)
        text = font.render(message, True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (BOARD_WIDTH // 2, BOARD_HEIGHT // 2)
        # Draw the message on top of the game board
        window.blit(text, text_rect)
    
    # Update the display
    pygame.display.update()

# Clean up Pygame
pygame.quit()