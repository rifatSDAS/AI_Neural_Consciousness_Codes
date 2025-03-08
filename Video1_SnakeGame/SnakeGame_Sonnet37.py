import pygame
import time
import random

pygame.init()

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Set up the game window
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Game variables
BLOCK_SIZE = 20
SPEED_INCREASE_FACTOR = 0.05  # Speed increases by 5% per food eaten
BASE_SPEED = 10

# Font for score display
font = pygame.font.SysFont(None, 35)


def display_score(score):
    """Display the current score on the screen."""
    text = font.render(f"Score: {score}", True, WHITE)
    window.blit(text, (10, 10))


def draw_snake(snake_list):
    """Draw the snake on the screen."""
    for segment in snake_list:
        pygame.draw.rect(
            window, GREEN, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE]
        )


def game_loop():
    """Main game loop."""
    game_over = False
    game_exit = False

    # Initial snake position
    x = WIDTH // 2
    y = HEIGHT // 2

    # Snake movement
    x_change = 0
    y_change = 0

    # Snake body
    snake_list = []
    snake_length = 1

    # Initial food position
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    # Game speed and score
    speed = BASE_SPEED
    score = 0

    clock = pygame.time.Clock()

    while not game_exit:
        # Handle game over state
        while game_over:
            window.fill(BLACK)
            game_over_text = font.render(
                "Game Over! Press R to Restart or Q to Quit", True, WHITE
            )
            window.blit(game_over_text, (WIDTH // 4, HEIGHT // 2))
            display_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_r:
                        game_loop()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change != BLOCK_SIZE:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change != -BLOCK_SIZE:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP and y_change != BLOCK_SIZE:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change != -BLOCK_SIZE:
                    y_change = BLOCK_SIZE
                    x_change = 0

        # Move the snake
        x += x_change
        y += y_change

        # Check for wall collision
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_over = True

        # Draw game elements
        window.fill(BLACK)
        pygame.draw.rect(window, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Update snake
        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for self collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        draw_snake(snake_list)
        display_score(score)

        pygame.display.update()

        # Check for food collision
        if x == food_x and y == food_y:
            # Generate new food
            food_x = (
                round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            )
            food_y = (
                round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE)
                * BLOCK_SIZE
            )

            # Increase snake length and score
            snake_length += 1
            score += 10

            # Increase speed
            speed += BASE_SPEED * SPEED_INCREASE_FACTOR

        clock.tick(speed)

    pygame.quit()
    quit()


# Start the game
game_loop()
