# Example file showing a basic pygame "game loop"
import random

import pygame


def draw(screen, sp, ep):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, 'red', [(1, 1), (sp - 1, ep - 1)])


# pygame setup
lnchh = True
pygame.init()
a = input()
if ' ' in a:
    if len(a.split(' ')) == 2:
        if a.split(' ')[0].isdigit() and a.split(' ')[1].isdigit():
            if a.split(' ')[0] % a.split(' ')[1]
            w, h = a.split(' ')
        else:
            print('Неправильный формат ввода')
            lnchh = False
    else:
        print('Неправильный формат ввода')
        lnchh = False
else:
    print('Неправильный формат ввода')
    lnchh = False
if lnchh:
    screen = pygame.display.set_mode((int(w), int(h)))
    clock = pygame.time.Clock()
    running = True

else:
    running = False


while running:
    size = width, height = int(w), int(h)
    pygame.display.set_caption('Прямоугольник')
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    draw(screen, width, height)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS

pygame.quit()
