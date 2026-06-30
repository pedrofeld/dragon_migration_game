import datetime

import pygame

from code.Background import Background
from code.Consts import WIN_WIDTH, WIN_HEIGHT, FPS, GAME_MUSIC_PATH, BG_GAME_PATH, BG_SCORE_PATH, SCORE_MUSIC_PATH, DRAGON_IMAGE_PATH, BIRD_IMAGE_PATH
from code.DBProxy import DBProxy
from code.Menu import Menu
from code.Level import Level

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Dragon Migration")
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_background = Background(self.window, BG_GAME_PATH)
        self.score_background = Background(self.window, BG_SCORE_PATH)
        self.menu = Menu(self.window)
        self.state = "menu"
        self.level = None
        self.db = DBProxy()

    def run(self):
        while self.running:
            choice = self.menu.run()

            if choice in ("QUIT", "EXIT", None):
                self.running = False
            elif choice == "PLAY":
                self.level = Level(self.window, DRAGON_IMAGE_PATH, BIRD_IMAGE_PATH)
                pygame.mixer.music.load(GAME_MUSIC_PATH)
                pygame.mixer.music.play(-1)
                self.state = "game"
                self.game_loop()
                if self.state == "score":
                    self.show_score_screen()
                    self.state = "menu"
            elif choice == "SCORE":
                    self.show_score_screen()

        self.db.close()
        pygame.quit()

    def game_loop(self):
        while self.running and self.state == "game":
            self.events()
            self.update()
            if self.level.finished:
                self.db.save_score(
                    self.level.dragon.score,
                    datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                )
                self.db.remove_old_scores()
                if self.level.result == "lose":
                    self.state = "menu"
                elif self.level.result == "win":
                    self.state = "score"
                break
            self.draw()
            self.clock.tick(FPS)
            if not self.running:
                break
            if self.state != "game":
                break

    def show_score_screen(self):
        showing = True
        font = pygame.font.SysFont("Lucida Sans Typewriter", 28)
        pygame.mixer.music.load(SCORE_MUSIC_PATH)
        pygame.mixer.music.play(-1)

        while self.running and showing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    showing = False
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RETURN, pygame.K_ESCAPE):
                        showing = False
            self.score_background.draw()
            title = font.render("LAST SCORES", True, (255, 255, 255))
            self.window.blit(
                title,
                title.get_rect(center=(WIN_WIDTH // 2, 60))
            )
            scores = self.db.get_last_scores()
            if len(scores) == 0:
                text = font.render("No scores yet", True, (255, 255, 255))
                self.window.blit(
                    text,
                    text.get_rect(center=(WIN_WIDTH // 2, 140))
                )
            else:
                for i, (score, date) in enumerate(scores):
                    text = font.render(
                        f"{i + 1}. {score}",
                        True,
                        (255, 255, 255)
                    )
                    self.window.blit(
                        text,
                        text.get_rect(center=(WIN_WIDTH // 2, 140 + i * 35))
                    )
            pygame.display.flip()
            self.clock.tick(FPS)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def update(self):
        self.game_background.update()
        if self.state == "game" and self.level is not None:
            self.level.update()

    def draw(self):
        self.game_background.draw()
        if self.state == "game" and self.level is not None:
            self.level.draw()
        else:
            font = pygame.font.SysFont("Lucida Sans Typewriter", 28)
            label = font.render("Dragon Migration - em desenvolvimento", True, (255, 255, 255))
            label_rect = label.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
            self.window.blit(label, label_rect)
        pygame.display.flip()