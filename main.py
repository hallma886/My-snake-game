import pygame
import sys
import random

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "😂😂Snake Game😂😂"

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

# Game variables and constants
CELL_SIZE = 10
direction = 1 #1 is up, 2 is right, 3 is down, 4 is left
update_snake = 0
score = 0   # Initialize score

snake_pos = [[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]]
snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE])
snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE * 2])
snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE * 3])

BG = (255, 200, 150)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BODY_INNER = (50, 175, 25)
BODY_OUTER = (100, 100, 200)
APPLE_COLOR = (225, 0, 0)

# Define apple position

apple_pos = [random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]
# Font for score
font = pygame.font.SysFont(None, 35)

def draw_screen():
    screen.fill(BG)

def draw_apple():
    pygame.draw.rect(screen, APPLE_COLOR, (apple_pos[0], apple_pos[1], CELL_SIZE, CELL_SIZE))

def draw_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, [10, 10])

running = True
while running:
    draw_screen()
    draw_apple()
    draw_score()

    # Loop through events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3: 
                direction = 1
            elif event.key == pygame.K_RIGHT and direction != 4: #Right
                direction = 2
            elif event.key == pygame.KDOWN and direction != 1:  # Down
                direction = 3
            elif event.key == pygame.K_LEFT and direction != 2: # Left
                direction = 4

    if update_snake > 99:
        update_snake = 0

        head_x, head_y = snake_pos[0]

        if direction == 1:
            head_y -= CELL_SIZE
        elif direction == 2:
            head_x += CELL_SIZE
        elif direction == 3:
            head_y -= CELL_SIZE
        elif direction == 4:
            head_x += CELL_SIZE
        
        snake_pos.insert(0, [head_x, head_y])
        snake_pos.pop()

        