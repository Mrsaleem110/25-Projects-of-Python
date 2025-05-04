import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = pygame.K_RIGHT

    def move(self):
        x, y = self.body[0]
        if self.direction == pygame.K_RIGHT:
            x += CELL_SIZE
        elif self.direction == pygame.K_LEFT:
            x -= CELL_SIZE
        elif self.direction == pygame.K_UP:
            y -= CELL_SIZE
        elif self.direction == pygame.K_DOWN:
            y += CELL_SIZE
        new_head = (x, y)
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    def check_collision(self):
        head = self.body[0]
        # Collision with walls
        if (
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT
        ):
            return True
        # Collision with itself
        if head in self.body[1:]:
            return True
        return False

class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        return (x, y)

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, CELL_SIZE, CELL_SIZE))

# Main game loop
def main():
    snake = Snake()
    food = Food()
    score = 0
    font = pygame.font.SysFont(None, 35)

    running = True
    while running:
        screen.fill(BLACK)
        snake.move()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if (event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]):
                    if abs(snake.direction - event.key) != 2:  # prevent reversing
                        snake.direction = event.key

        # Collision with food
        if snake.body[0] == food.position:
            snake.grow()
            food = Food()
            score += 1

        if snake.check_collision():
            print("Game Over!")
            running = False

        # Draw
        snake.draw()
        food.draw()
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(10)  # FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    