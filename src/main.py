from settings import *
import pygame

class Main:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Conway's Game of Life")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #draw
            self.window.fill(BACKGROUND_COLOR)

            #update
            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    simulation = Main()
    simulation.run()