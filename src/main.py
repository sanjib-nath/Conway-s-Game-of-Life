from settings import *
import pygame

class Main:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Conway's Game of Life")
        self.clock = pygame.time.Clock()
        self.running = True

    def draw_grid(self):
        for x in range(0, WIN_WIDTH, CELL_SIZE):
            for y in range(0, WIN_HEIGHT, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.window, GRID_COLOR, rect, 1)

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #draw
            self.window.fill(BACKGROUND_COLOR)
            self.draw_grid()

            #update
            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    simulation = Main()
    simulation.run()