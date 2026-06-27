import pygame

from code.Consts import WIN_WIDTH, WIN_HEIGHT

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        pass

    def events(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass