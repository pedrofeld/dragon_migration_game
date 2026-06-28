import pygame

from code.Background import Background
from code.Consts import WIN_WIDTH, WIN_HEIGHT, FPS, GAME_MUSIC_PATH, BG_GAME_PATH, BG_SCORE_PATH, SCORE_MUSIC_PATH, DRAGON_IMAGE_PATH, BIRD_IMAGE_PATH
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
            elif choice == "SCORE":
                self.show_score_screen()

        pygame.quit()

    def game_loop(self):
        while self.running and self.state == "game":
            self.events()
            self.update()
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
            title = font.render("SCORE", True, (255, 255, 255))
            hint = font.render("Pressione ENTER ou ESC para voltar", True, (255, 255, 255))
            self.window.blit(title, title.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 20)))
            self.window.blit(hint, hint.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 20)))
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