import pygame
pygame.init()
s = pygame.display.set_mode((400, 400))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
    pygame.display.flip()