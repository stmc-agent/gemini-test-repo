import pygame
import random

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Tetrominoes
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[0, 1, 0], [1, 1, 1]],
]

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
BLOCK_SIZE = 20
GRID_WIDTH = 10
GRID_HEIGHT = 20


class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.board = self.create_board()
        self.figure = None
        self.figure_x = 0
        self.figure_y = 0
        self.score = 0
        self.new_figure()

    def create_board(self):
        return [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    def new_figure(self):
        self.figure = random.choice(SHAPES)
        self.figure_x = int(GRID_WIDTH / 2 - len(self.figure[0]) / 2)
        self.figure_y = 0

    def intersects(self):
        for y, row in enumerate(self.figure):
            for x, cell in enumerate(row):
                if cell:
                    if (
                        self.figure_y + y >= GRID_HEIGHT
                        or self.figure_x + x < 0
                        or self.figure_x + x >= GRID_WIDTH
                        or self.board[self.figure_y + y][self.figure_x + x]
                    ):
                        return True
        return False

    def rotate(self):
        rotated_figure = [
            [self.figure[y][x] for y in range(len(self.figure))]
            for x in range(len(self.figure[0]) - 1, -1, -1)
        ]
        if not self.intersects():
            self.figure = rotated_figure

    def go_down(self):
        self.figure_y += 1
        if self.intersects():
            self.figure_y -= 1
            self.freeze()

    def go_side(self, dx):
        self.figure_x += dx
        if self.intersects():
            self.figure_x -= dx

    def freeze(self):
        for y, row in enumerate(self.figure):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.figure_y + y][self.figure_x + x] = 1
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.game_over = True

    def break_lines(self):
        lines_to_break = []
        for y, row in enumerate(self.board):
            if all(row):
                lines_to_break.append(y)
        for y in lines_to_break:
            del self.board[y]
            self.board.insert(0, [0 for _ in range(GRID_WIDTH)])
        self.score += len(lines_to_break)

    def draw_board(self):
        self.screen.fill(BLACK)
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        self.screen,
                        WHITE,
                        (
                            x * BLOCK_SIZE,
                            y * BLOCK_SIZE,
                            BLOCK_SIZE,
                            BLOCK_SIZE,
                        ),
                        0,
                    )
        if self.figure:
            for y, row in enumerate(self.figure):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(
                            self.screen,
                            GRAY,
                            (
                                (self.figure_x + x) * BLOCK_SIZE,
                                (self.figure_y + y) * BLOCK_SIZE,
                                BLOCK_SIZE,
                                BLOCK_SIZE,
                            ),
                            0,
                        )

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.go_side(-1)
                    if event.key == pygame.K_RIGHT:
                        self.go_side(1)
                    if event.key == pygame.K_DOWN:
                        self.go_down()
                    if event.key == pygame.K_UP:
                        self.rotate()

            self.go_down()
            self.draw_board()
            pygame.display.flip()
            self.clock.tick(5)
        pygame.quit()


if __name__ == "__main__":
    game = Tetris()
    game.run()
