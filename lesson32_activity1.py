import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (100, 50, 80), pygame.Rect(80, 40, 200, 100))
    pygame. display.flip()