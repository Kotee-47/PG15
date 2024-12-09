# python -m pygame.examples.events примервы собитий

import pygame

pygame.init()
size = width, height = 720, 720
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("дарк блю кролик")
running = True
dt = 1
v = 400
fps = 30

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.circle(screen, 'dark blue', event.pos, 20)
            pygame.draw.ellipse(screen, 'dark blue', (event.pos[0] - 15, event.pos[1] - 40, 10, 40), 20)
            pygame.draw.ellipse(screen, 'dark blue', (event.pos[0] + 5, event.pos[1] - 40, 10, 40), 20)

    pygame.display.flip()

    screen.fill("dark grey")

    dt = clock.tick(fps) / 1000

pygame.quit()
