import pygame

from code.Consts import WIN_WIDTH, WIN_HEIGHT

class Background():
    def __init__(self, window, path_image):
        self.window = window
        self.image = pygame.image.load(path_image).convert()
        self.image = pygame.transform.scale(self.image, (WIN_WIDTH, WIN_HEIGHT))
        self.scroll_speed = 1

    def update(self):
        pass

    def draw(self):
        if self.window is not None:
            self.window.blit(self.image, (0, 0))