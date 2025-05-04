import pygame
import random
import math

pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

# Player
player_img = pygame.Surface((50, 40))
player_img.fill((0, 255, 0))
player_x = 370
player_y = 480
player_x_change = 0

# Enemy
enemy_img = pygame.Surface((50, 40))
enemy_img.fill((255, 0, 0))
enemy_x = random.randint(0, 750)
enemy_y = random.randint(50, 150)
enemy_x_change = 4
enemy_y_change = 40

# Bullet
bullet_img = pygame.Surface((5, 20))
bullet_img.fill((255, 255, 0))
bullet_x = 0
bullet_y = 480
bullet_y_change = 10
bullet_state = "ready"

# Score
score = 0
font = pygame.font.Font(None, 36)

def show_score():
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y):
    screen.blit(enemy_img, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 22, y))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.hypot(enemy_x - bullet_x, enemy_y - bullet_y)
    return distance < 27

# Game loop
running = True
while running:
    screen.fill((0, 0, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player_x_change = 0

    # Movement updates
    player_x += player_x_change
    player_x = max(0, min(player_x, 750))

    enemy_x += enemy_x_change
    if enemy_x <= 0 or enemy_x >= 750:
        enemy_x_change *= -1
        enemy_y += enemy_y_change

    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    if is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
        bullet_y = 480
        bullet_state = "ready"
        score += 1
        enemy_x = random.randint(0, 750)
        enemy_y = random.randint(50, 150)

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    show_score()
    pygame.display.update()

pygame.quit()
