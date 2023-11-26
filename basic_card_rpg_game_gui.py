import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Card RPG Game')

# Game colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Basic game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Game logic and drawing goes here
    # For example, drawing a simple rectangle for a card
    card_rect = pygame.Rect(100, 100, 120, 180)
    pygame.draw.rect(screen, BLACK, card_rect, 2)
    font = pygame.font.SysFont(None, 24)
    text = font.render('Fireball', True, BLACK)
    screen.blit(text, (110, 110))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
