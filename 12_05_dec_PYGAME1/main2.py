# Example file showing a basic pygame "game loop"
import random

import pygame


def draw(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render('Hello, Pygame!',
                       True,
                       (100, 100, 255))
    text_w = text.get_width()
    text_h = text.get_height()
    text_x = width // 2 - text_w // 2
    text_y = height // 2 - text_h // 2
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 100, 255),
                     (text_x - 10,  text_y - 10, text_w + 20,  text_h + 20), 1)


def draw2(screen):
    for i in range(1000):
        screen.fill(pygame.Color('white'),
                    (random.random() * width,
                     random.random() * height, 2, 2))


def draw3(screen):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0),
                     (100, 100,
                      200, 200), 1)
    pygame.draw.polygon(screen, pygame.Color('orange'), [(0, 0), (150, 50), (50, 150)], 0)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True


while running:
    size = width, height = 800, 600
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    # draw(screen)
    # draw2(screen)
    draw3(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
