import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
BLOCK_SIZE = 20
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Snake class
class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.length = 1
        self.score = 0
        self.speed = 5  # Initial speed

    def update_position(self):
        head_x, head_y = self.positions[0]
        if self.direction == UP:
            new_head = (head_x, head_y - BLOCK_SIZE)
        elif self.direction == DOWN:
            new_head = (head_x, head_y + BLOCK_SIZE)
        elif self.direction == LEFT:
            new_head = (head_x - BLOCK_SIZE, head_y)
        else:  # RIGHT
            new_head = (head_x + BLOCK_SIZE, head_y)

        # Check if snake hits the edge
        if (
            new_head[0] >= WIDTH
            or new_head[0] < 0
            or new_head[1] >= HEIGHT
            or new_head[1] < 0
        ):
            return False

        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()
        return True

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, GREEN, (p[0], p[1], BLOCK_SIZE, BLOCK_SIZE))


# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (
            random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
            random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
        )

    def render(self, surface):
        pygame.draw.rect(
            surface, RED, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE)
        )


# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()

    # Font for score
    font = pygame.font.SysFont(None, 36)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.direction = DOWN
                elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT

        # Update snake position
        if not snake.update_position():
            # Snake hit edge - restart
            snake.reset()
            food.randomize_position()

        # Check if snake ate food
        if snake.positions[0] == food.position:
            snake.length += 1
            snake.score += 1
            # Increase speed every 5 points (capped at 20)
            snake.speed = min(5 + snake.score // 5, 20)
            food.randomize_position()

        # Draw everything
        window.fill(BLACK)
        snake.render(window)
        food.render(window)

        # Draw score
        score_text = font.render(f"Score: {snake.score}", True, (255, 255, 255))
        window.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(snake.speed)

    pygame.quit()


if __name__ == "__main__":
    main()
