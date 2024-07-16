import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            print("Key pressed")

        if event.type == pygame.KEYUP:
            print("Key released")

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse clicked")

        if event.type == pygame.MOUSEBUTTONUP:
            print("Mouse released")

        if event.type == pygame.MOUSEMOTION:
            print("Mouse moving")

        if event.type == pygame.MOUSEWHEEL:
            print("Scroll-wheel moving/clicked")

pygame.quit()