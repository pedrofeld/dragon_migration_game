from code.Entity import Entity
import pygame
from code.Consts import WIN_HEIGHT

class Bird(Entity):
    def __init__(self, image_path=None, target_width=40):
        super().__init__(image_path)
        self.health = 1
        self.speed = 2
        try:
            w, h = self.image.get_size()
            if w > target_width:
                scale = target_width / w
                new_size = (max(1, int(w * scale)), max(1, int(h * scale)))
                self.image = pygame.transform.smoothscale(self.image, new_size)
                self.image = pygame.transform.flip(self.image, True, False)
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
        except Exception:
            pass

    def flee(self, dragon):
        dx = self.rect.centerx - dragon.rect.centerx
        if abs(dx) < 200:
            if dragon.rect.centery < self.rect.centery:
                if self.rect.bottom + 1 <= WIN_HEIGHT:
                    self.rect.centery += 1
            elif dragon.rect.centery > self.rect.centery:
                if self.rect.top - 1 >= 0:
                    self.rect.centery -= 1

    def update(self, dragon=None):
        self.rect.centerx -= self.speed
        if dragon is not None:
            self.flee(dragon)
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT