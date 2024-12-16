# python -m pygame.examples.events примервы собитий

import pygame

pygame.init()
size = width, height = 720, 720
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("[eqyzx]")
running = True
MYEVENTTYPE = pygame.USEREVENT + 1
pygame.time.set_timer(MYEVENTTYPE, 1000)
dt = 0
v = 5
fps = 10

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
screen.fill("blue")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill("blue")
            ggt = True
            R = 0
            while ggt is True:
                pygame.draw.circle(screen, 'yellow', event.pos, R)
                pygame.display.flip()
                R += v * dt
        if event.type == pygame.MOUSEBUTTONDOWN:
            ggt = False

    dt = clock.tick(fps) / 1000

pygame.quit()
