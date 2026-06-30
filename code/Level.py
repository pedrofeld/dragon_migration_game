import pygame
import random
from code.Consts import WIN_WIDTH, WIN_HEIGHT
from code.Dragon import Dragon
from code.Bird import Bird
from code.EntityMediator import EntityMediator
from code.HUD import HUD


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
        self.game_duration = 240000
        self.start_time = pygame.time.get_ticks()
        self.last_damage = pygame.time.get_ticks()
        self.finished = False
        self.result = None

    def update(self):
        self.dragon.move()

        now = pygame.time.get_ticks()

        elapsed = now - self.start_time
        self.remaining = max(0, self.game_duration - elapsed)

        seconds = self.remaining // 1000
        minutes = seconds // 60
        seconds = seconds % 60
        self.time_text = f"{minutes:02}:{seconds:02}"

        elapsed_seconds = elapsed // 1000
        damage = 1
        if elapsed_seconds >= 60:
            damage = 2
        if elapsed_seconds >= 120:
            damage = 3
        if elapsed_seconds >= 180:
            damage = 4

        if now - self.last_damage >= 1000:
            self.dragon.take_damage(damage)
            self.last_damage = now

        if now - self.last_spawn >= self.spawn_interval_ms:
            self.spawn_bird()
            self.last_spawn = now

        if self.remaining <= 0:
            self.win = True

        for bird in self.birds[:]:
            bird.update(self.dragon)

            EntityMediator.process_collision(self.dragon, bird)

            if bird.rect.right < 0:
                self.birds.remove(bird)

        EntityMediator.verify_health(self.birds)

        if self.dragon.hp <= 0:
            self.finished = True
            self.result = "lose"

        if self.remaining <= 0 and self.dragon.hp > 0:
            self.finished = True
            self.result = "win"

        if self.finished:
            return

    def draw(self):
        self.window.blit(self.dragon.image, self.dragon.rect)

        for bird in self.birds:
            self.window.blit(bird.image, bird.rect)

        HUD.draw_hp(self.window, self.dragon.hp)
        HUD.draw_score(self.window, self.dragon.score)
        HUD.draw_timer(self.window, self.time_text)

    def spawn_bird(self):
        b = Bird(self.bird_image_path)
        b.rect.left = WIN_WIDTH + 5
        b.rect.centery = random.randint(20, WIN_HEIGHT - 20)
        elapsed_seconds = (pygame.time.get_ticks() - self.start_time) // 1000
        if elapsed_seconds < 60:
            min_speed = 2
            max_speed = 4
        elif elapsed_seconds < 120:
            min_speed = 3
            max_speed = 5
        elif elapsed_seconds < 180:
            min_speed = 4
            max_speed = 6
        else:
            min_speed = 5
            max_speed = 7
        b.speed = random.randint(min_speed, max_speed)
        self.birds.append(b)