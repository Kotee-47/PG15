# Example file showing a basic pygame "game loop"
import pygame


def draw(screeen):
    screeen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render('Hello, Pygame!',
                       True,
                       (100, 100, 255))
    text_w = text.get_width()
    text_h = text.get_height()
    text_x = width // 2 - text_w // 2
    text_y = height // 2 - text_h // 2
    screeen.blit(text, (text_x, text_y))
    pygame.draw.rect(screeen, (0, 100, 255),
                     (text_x - 10,  text_y - 10, text_w + 10,  text_h + 10), 1)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
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
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
