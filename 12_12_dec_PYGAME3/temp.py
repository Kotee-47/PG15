import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[1] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left=10, top=10, cell_size=30):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        self.screen = screen
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(screen, pygame.Color('white'), (
                                 x * self.cell_size + self.left,
                                 y * self.cell_size + self.top,
                                 self.cell_size, self.cell_size),
                                 self.board[y][x])

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size
        if self.width >= x + 1 > 0 and self.height >= y + 1 > 0:
            return x, y

    def on_click(self, cell):
        print("Была выбрана ячейка " + str(cell))
        if cell:
            x, y = cell
            for i in range(self.height):
                self.board[i][x] = int(not self.board[i][x])
            for i in range(self.width):
                self.board[y][i] = int(not self.board[y][i])
            self.board[y][x] = int(not self.board[y][x])
            self.render(self.screen)


def main():
    pygame.init()
    size = width, height = 720, 720
    board = Board(17, 17)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("erm")
    running = True
    dt = 0
    fps = 30

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                board.get_click(event.pos)

        screen.fill("black")
        board.render(screen)
        board.set_view(20, 20, 40)
        pygame.display.flip()
        dt = clock.tick(fps) / 1000

    pygame.quit()


if __name__ == '__main__':
    main()
