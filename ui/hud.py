import pygame

from core.colors import WHITE


class HUD:

    def __init__(self):

        pygame.font.init()

        self.font = pygame.font.SysFont(
            "consolas",
            24
        )

    def draw(self, screen, state):

        title = self.font.render(
            "Bubble Sort Visualizer",
            True,
            WHITE
        )

        screen.blit(title, (20, 20))

        comparisons = self.font.render(
            f"Comparaciones: {state.comparisons}",
            True,
            WHITE
        )

        screen.blit(comparisons, (20, 60))

        swaps = self.font.render(
            f"Swaps: {state.swaps}",
            True,
            WHITE
        )

        screen.blit(swaps, (20, 100))

        message = self.font.render(
            state.message,
            True,
            WHITE
        )

        screen.blit(message, (20, 140))