from settings import *
import pygame

class Main:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Conway's Game of Life")
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_rect = []
        self.create_grid()

    def create_grid(self):
        for y in range(0, WIN_HEIGHT, CELL_SIZE):
            row = []
            for x in range(0, WIN_WIDTH, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                row.append([rect, GRID_COLOR, 1])

            self.all_rect.append(row)

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for row in self.all_rect:
                        for item in row:
                            if item[0].collidepoint(event.pos):
                                if item[1] == GRID_COLOR:
                                    item[1] = CELL_COLOR
                                    item[2] = None
                                else:
                                    item[1] = GRID_COLOR
                                    item[2] = 1

            self.window.fill(BACKGROUND_COLOR)

            for row in self.all_rect:
                for rect, color, width in row:
                    if width != None:
                        pygame.draw.rect(self.window, color, rect, width)
                    else:
                        pygame.draw.rect(self.window, color, rect)

            #update
            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    simulation = Main()
    simulation.run()