import pygame
from code.Consts import C_PURPLE, C_BLACK, WIN_WIDTH, WIN_HEIGHT


class HUD:
    @staticmethod
    def level_text(window, text_size, text, color, pos):
        font = pygame.font.SysFont(
            "Lucida Sans Typewriter",
            text_size
        )
        surface = font.render(text, True, color)
        rect = surface.get_rect(
            left=pos[0],
            top=pos[1]
        )
        window.blit(surface, rect)

    @staticmethod
    def draw_hp(window, hp):
        HUD.level_text(
            window,
            24,
            f"HP: {hp}",
            C_PURPLE,
            (10, 10)
        )

    @staticmethod
    def draw_score(window, score):
        HUD.level_text(
            window,
            24,
            f"Score: {score}",
            C_PURPLE,
            (10, 40)
        )

    @staticmethod
    def draw_timer(window, time_text):
        HUD.level_text(
            window,
            24,
            f"Tempo: {time_text}",
            C_PURPLE,
            (10, 70)
        )

    @staticmethod
    def draw_instructions(self):
        font = pygame.font.SysFont("Lucida Sans Typewriter", 16)
        text = font.render(
            "Use as setas do teclado para mover o dragão",
            True,
            C_BLACK
        )
        rect = text.get_rect(
            center=(WIN_WIDTH // 2, WIN_HEIGHT - 10)
        )
        self.window.blit(text, rect)