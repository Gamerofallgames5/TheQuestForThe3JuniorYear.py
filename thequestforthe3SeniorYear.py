import pygame
import sys
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 40
PLAYER_SIZE = 36

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Mini Roguelike')

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the player
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos[0] -= GRID_SIZE
            elif event.key == pygame.K_RIGHT:
                player_pos[0] += GRID_SIZE
            elif event.key == pygame.K_UP:
                player_pos[1] -= GRID_SIZE
            elif event.key == pygame.K_DOWN:
                player_pos[1] += GRID_SIZE

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))

    pygame.display.flip()
    clock.tick(30)