import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Background import Background
from code.Consts import WIN_WIDTH, MENU_OPTION, FPS, C_BLACK, MENU_MUSIC_PATH, C_GREEN, BG_MENU_PATH

class Menu:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()
        self.background = Background(window, BG_MENU_PATH)

    def run(self):
        pygame.mixer.music.load(MENU_MUSIC_PATH)
        pygame.mixer.music.play(-1)
        menu_option = 0
        while True:
            self.background.draw()
            self.menu_text(50, "DRAGON", C_GREEN, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "MIGRATION", C_GREEN, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_GREEN, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_BLACK, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "QUIT"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(source=text_surface, dest=text_rect)