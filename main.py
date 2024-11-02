import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define display dimensions
WIDTH = 400
HEIGHT = 400
GRID_SIZE = 20

# Set up the display
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

# Clock to control the frame rate
clock = pygame.time.Clock()

# Font for the score
font = pygame.font.SysFont('Arial', 25)

def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(display, GREEN, [segment[0], segment[1], GRID_SIZE, GRID_SIZE])

def draw_food(food_position):
    pygame.draw.rect(display, RED, [food_position[0], food_position[1], GRID_SIZE, GRID_SIZE])

def game_loop():
    game_over = False
    game_close = False

    # Initial snake position and body
    x = WIDTH // 2
    y = HEIGHT // 2
    snake_body = [[x, y]]
    snake_length = 1

    # Initial direction
    dx = 0
    dy = 0

    # Food position
    food_position = [random.randrange(1, (WIDTH // GRID_SIZE)) * GRID_SIZE,
                     random.randrange(1, (HEIGHT // GRID_SIZE)) * GRID_SIZE]

    while not game_over:

        while game_close:
            display.fill(BLACK)
            message = font.render("Press C-Continue or Q-Quit", True, WHITE)
            message_rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Center the text
            display.blit(message, message_rect)  # Blit at the centered position
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -GRID_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = GRID_SIZE
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -GRID_SIZE
                    dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = GRID_SIZE
                    dx = 0

        # Update the snake's position
        x += dx
        y += dy

        # Check for collision with boundaries
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_close = True

        # Update snake body
        snake_body.insert(0, [x, y])
        if x == food_position[0] and y == food_position[1]:
            snake_length += 1
            food_position = [random.randrange(1, (WIDTH // GRID_SIZE)) * GRID_SIZE,
                             random.randrange(1, (HEIGHT // GRID_SIZE)) * GRID_SIZE]
        else:
            snake_body.pop()

        # Check for collision with itself
        if snake_body[0] in snake_body[1:]:
            game_close = True

        # Draw everything
        display.fill(BLACK)
        draw_snake(snake_body)
        draw_food(food_position)

        # Update score
        score_text = font.render("Score: " + str(snake_length - 1), True, WHITE)
        display.blit(score_text, [0, 0])

        pygame.display.update()

        # Control the game speed
        clock.tick(10)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()
