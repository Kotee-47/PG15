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


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    draw(screen)
    # обновление экрана
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()
