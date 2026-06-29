from code.Entity import Entity
import pygame
from code.Consts import WIN_WIDTH, WIN_HEIGHT

class Dragon(Entity):
    def __init__(self, image_path=None, target_width=40):
        super().__init__(image_path)
        try:
            w, h = self.image.get_size()
            if w != target_width:
                scale = target_width / w
                new_size = (max(1, int(w * scale)), max(1, int(h * scale)))
                self.image = pygame.transform.smoothscale(self.image, new_size)
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
        except Exception:
            pass

        self.hp = 100
        self.max_hp = 100
        self.score = 0
        self.speed = 4

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= self.speed
        if pressed[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += self.speed
        if pressed[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= self.speed
        if pressed[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += self.speed

    def eat_bird(self):
        pass

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)