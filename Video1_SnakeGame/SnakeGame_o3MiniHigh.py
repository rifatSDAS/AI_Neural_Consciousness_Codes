import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up clock for controlling the game speed
clock = pygame.time.Clock()

# Snake block size
block_size = 20


def get_random_food():
    """Return a random position for the food, aligned to the grid."""
    x = random.randrange(0, WIDTH - block_size, block_size)
    y = random.randrange(0, HEIGHT - block_size, block_size)
    return (x, y)


# Main game loop that also handles game resets
while True:
    # Initialize game state
    snake = [(WIDTH // 2, HEIGHT // 2)]  # Snake starting position
    snake_dir = (block_size, 0)  # Initial movement: right
    food = get_random_food()
    score = 0
    speed = 10  # Initial speed (FPS)

    game_over = False
    while not game_over:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Change direction but prevent reversing directly
                if event.key == pygame.K_LEFT and snake_dir != (block_size, 0):
                    snake_dir = (-block_size, 0)
                elif event.key == pygame.K_RIGHT and snake_dir != (-block_size, 0):
                    snake_dir = (block_size, 0)
                elif event.key == pygame.K_UP and snake_dir != (0, block_size):
                    snake_dir = (0, -block_size)
                elif event.key == pygame.K_DOWN and snake_dir != (0, -block_size):
                    snake_dir = (0, block_size)

        # Calculate new head position
        new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

        # Check collision with boundaries (restart game if hit)
        if (
            new_head[0] < 0
            or new_head[0] >= WIDTH
            or new_head[1] < 0
            or new_head[1] >= HEIGHT
        ):
            game_over = True
            break

        # Check collision with self (restart game if hit)
        if new_head in snake:
            game_over = True
            break

        # Move the snake: add new head
        snake.insert(0, new_head)

        # Check if snake eats the food
        if new_head == food:
            score += 1
            food = get_random_food()
            speed += 1  # Increase speed dynamically
        else:
            # Remove tail segment if no food eaten
            snake.pop()

        # Clear the screen
        screen.fill(BLACK)

        # Draw food
        pygame.draw.rect(screen, RED, (food[0], food[1], block_size, block_size))

        # Draw snake
        for segment in snake:
            pygame.draw.rect(
                screen, GREEN, (segment[0], segment[1], block_size, block_size)
            )

        # Draw the score
        font = pygame.font.SysFont(None, 35)
        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Update display and tick clock
        pygame.display.update()
        clock.tick(speed)

    # Delay before restarting the game after collision
    pygame.time.delay(1000)
