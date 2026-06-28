import pygame

class Entity():
    def __init__(self, image_path=None, health: int = 1):
        if image_path is None:
            self.image = pygame.Surface((1, 1), pygame.SRCALPHA)
        else:
            self.image = pygame.image.load(str(image_path)).convert_alpha()
        self.rect = self.image.get_rect()
        self.health = 0
        self.speed = 0

    def move(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass