import pygame

from code.Consts import WIN_WIDTH, WIN_HEIGHT, BG_MENU_PATH

class Background():
    def __init__(self, window, path_image=BG_MENU_PATH):
        self.window = window
        self.path_image = path_image
        self.image = pygame.image.load(str(path_image)).convert()
        self.image = pygame.transform.scale(self.image, (WIN_WIDTH, WIN_HEIGHT))
        self.scroll_speed = 1

    def update(self):
        pass

    def draw(self):
        if self.window is not None:
            self.window.blit(self.image, (0, 0))