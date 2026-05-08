import pygame

from core.colors import (
    BAR_COLOR,
    ACTIVE_COLOR,
    SORTED_COLOR
)


class Bar:

    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)