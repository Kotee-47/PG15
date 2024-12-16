# python -m pygame.examples.events примервы собитий

import pygame

pygame.init()
size = width, height = 720, 720
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("дарк блю кролик")
running = True
MYEVENTTYPE = pygame.USEREVENT + 1
pygame.time.set_timer(MYEVENTTYPE, 1000)
dt = 1
v = 400
fps = 30

screen2 = pygame.Surface(screen.get_size())
x1, y1, w, h = 0, 0, 0, 0
drawing = False  # режим рисования выключен
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True  # включаем режим рисования
            # запоминаем координаты одного угла
            x1, y1 = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            # сохраняем нарисованное (на втором холсте)
            screen2.blit(screen, (0, 0))
            drawing = False
            x1, y1, w, h = 0, 0, 0, 0
        if event.type == pygame.MOUSEMOTION:
            # запоминаем текущие размеры
            if drawing:
                w, h = event.pos[0] - x1, event.pos[1] - y1
    # рисуем на экране сохранённое на втором холсте
    screen.fill(pygame.Color('black'))
    screen.blit(screen2, (0, 0))
    if drawing:  # и, если надо, текущий прямоугольник
        if w > 0 and h > 0:
            pygame.draw.rect(screen, (0, 0, 255), ((x1, y1), (w, h)), 5)
    pygame.display.flip()
