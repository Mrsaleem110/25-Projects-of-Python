import pygame
import random
import sys

# Pygame ki initialisation
pygame.init()

# Game ke size
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
COLUMNS = SCREEN_WIDTH // BLOCK_SIZE
ROWS = SCREEN_HEIGHT // BLOCK_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)

# Shapes (Tetrominoes)
SHAPES = [
    [[1, 1, 1, 1]],  # I shape
    [[1, 1], [1, 1]],  # O shape
    [[0, 1, 0], [1, 1, 1]],  # T shape
    [[0, 1, 1], [1, 1, 0]],  # S shape
    [[1, 1, 0], [0, 1, 1]],  # Z shape
    [[1, 0, 0], [1, 1, 1]],  # J shape
    [[0, 0, 1], [1, 1, 1]]   # L shape
]

COLORS = [CYAN, YELLOW, GREEN, RED, PURPLE, ORANGE, BLUE]

# Pygame window setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Game clock
clock = pygame.time.Clock()

# Function to create grid
def create_grid():
    return [[0] * COLUMNS for _ in range(ROWS)]

# Function to draw the grid
def draw_grid(grid):
    for y in range(ROWS):
        for x in range(COLUMNS):
            color = WHITE if grid[y][x] == 0 else grid[y][x]
            pygame.draw.rect(screen, color, pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Function to rotate the shape
def rotate(shape):
    return [list(row) for row in zip(*shape[::-1])]

# Function to check valid position of the shape
def valid_position(grid, shape, offset):
    off_y, off_x = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if (y + off_y >= ROWS or
                    x + off_x < 0 or
                    x + off_x >= COLUMNS or
                    grid[y + off_y][x + off_x]):
                    return False
    return True

# Function to merge shape with the grid
def merge(grid, shape, offset, color):
    off_y, off_x = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                grid[y + off_y][x + off_x] = color

# Function to clear full rows
def clear_rows(grid):
    new_grid = [row for row in grid if any(cell == 0 for cell in row)]
    while len(new_grid) < ROWS:
        new_grid.insert(0, [0] * COLUMNS)
    return new_grid

# Function to show the game over screen
def game_over():
    font = pygame.font.SysFont('Arial', 36)
    text = font.render("GAME OVER", True, RED)
    screen.blit(text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000)  # Wait for 2 seconds before closing the game

# Main game function
def main():
    grid = create_grid()
    current_shape = random.choice(SHAPES)
    current_color = random.choice(COLORS)
    offset = [0, COLUMNS // 2 - len(current_shape[0]) // 2]
    
    while True:
        screen.fill(BLACK)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Key presses for controlling the shape
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            new_offset = [offset[0], offset[1] - 1]
            if valid_position(grid, current_shape, new_offset):
                offset = new_offset
        elif keys[pygame.K_RIGHT]:
            new_offset = [offset[0], offset[1] + 1]
            if valid_position(grid, current_shape, new_offset):
                offset = new_offset
        elif keys[pygame.K_UP]:
            rotated = rotate(current_shape)
            if valid_position(grid, rotated, offset):
                current_shape = rotated
        elif keys[pygame.K_DOWN]:
            new_offset = [offset[0] + 1, offset[1]]
            if valid_position(grid, current_shape, new_offset):
                offset = new_offset
        
        # Drop shape
        new_offset = [offset[0] + 1, offset[1]]
        if not valid_position(grid, current_shape, new_offset):
            merge(grid, current_shape, offset, current_color)
            grid = clear_rows(grid)
            current_shape = random.choice(SHAPES)
            current_color = random.choice(COLORS)
            offset = [0, COLUMNS // 2 - len(current_shape[0]) // 2]
            if not valid_position(grid, current_shape, offset):
                game_over()
                return
        
        # Draw everything
        temp_grid = [row[:] for row in grid]
        merge(temp_grid, current_shape, offset, current_color)
        draw_grid(temp_grid)
        
        pygame.display.flip()
        clock.tick(10)  # Speed of the game (frames per second)

if __name__ == "__main__":
    main()
