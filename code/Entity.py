import pygame

class Entity():
    def __init__(self):
        self.image = pygame.image.load("../img/Entity.png")
        self.rect = self.image.get_rect()
        self.speed = 0

    def move(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass