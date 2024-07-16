import pygame

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Load the background image
background = pygame.image.load('assets/background.jpeg')

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Check if the user has clicked the close button
            run = False

        if event.type == pygame.KEYDOWN:
            print(f"Key released: {event.unicode}") # event.key is gives out the ASCII value of the key

        if event.type == pygame.KEYUP: # Check if the user has released a key
            print("Key released")

        if event.type == pygame.MOUSEBUTTONDOWN: # Check if the user has clicked the mouse
            print(f'Mouse pressed: {event.button}')

        if event.type == pygame.MOUSEBUTTONUP: # Check if the user has released the mouse
            print("Mouse released")

        if event.type == pygame.MOUSEMOTION: # Check if the user has moved the mouse
            print(f"Mouse moved: {event.pos}")

        if event.type == pygame.MOUSEWHEEL: # Check if the user has scrolled the mouse wheel
            print(f"Mouse wheel: {event.y}")

    # Blit the background image
    screen.blit(background, (0, 0))

    # Update the display
    pygame.display.flip()

pygame.quit()