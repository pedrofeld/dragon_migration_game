import pygame
import random
from code.Consts import WIN_WIDTH, WIN_HEIGHT
from code.Dragon import Dragon
from code.Bird import Bird

class Level:
    def __init__(self, window, dragon_image_path, bird_image_path):
        self.window = window
        self.dragon = Dragon(dragon_image_path)
        self.dragon.rect.left = 10
        self.dragon.rect.centery = WIN_HEIGHT // 2
        self.bird_image_path = bird_image_path
        self.birds = []
        self.score = 0
        self.last_spawn = pygame.time.get_ticks()
        self.spawn_interval_ms = 2000

    def update(self):
        self.dragon.move()

        now = pygame.time.get_ticks()
        if now - self.last_spawn > self.spawn_interval_ms:
            self.spawn_bird()
            self.last_spawn = now

        for bird in list(self.birds):
            bird.update(self.dragon)
            if bird.rect.right < 0:
                self.birds.remove(bird)

    def draw(self):
        self.window.blit(self.dragon.image, self.dragon.rect)
        for bird in self.birds:
            self.window.blit(bird.image, bird.rect)

    def spawn_bird(self):
        b = Bird(self.bird_image_path)
        b.rect.left = WIN_WIDTH + 5
        b.rect.centery = random.randint(20, WIN_HEIGHT - 20)
        b.speed = random.randint(2, 4)
        self.birds.append(b)

    def spawn_spaceship(self):
        pass