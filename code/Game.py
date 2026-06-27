import pygame

from code.Background import Background
from code.Consts import WIN_WIDTH, WIN_HEIGHT, FPS, GAME_MUSIC_PATH
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Dragon Migration")
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.background = Background(self.window)
        self.menu = Menu(self.window)
        self.state = "menu"

    def run(self):
        choice = self.menu.run()

        if choice == "QUIT" or choice is None:
            self.running = False
        elif choice in ("PLAY", "SCORE"):
            pygame.mixer.music.load(GAME_MUSIC_PATH)
            pygame.mixer.music.play(-1)
            self.state = "game"

        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def update(self):
        self.background.update()

    def draw(self):
        self.background.draw()
        font = pygame.font.SysFont("Lucida Sans Typewriter", 28)
        label = font.render("Dragon Sky - em desenvolvimento", True, (255, 255, 255))
        label_rect = label.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        self.window.blit(label, label_rect)
        pygame.display.flip()