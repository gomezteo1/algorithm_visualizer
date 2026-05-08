import pygame

from core.colors import BACKGROUND
from core.colors import BAR_COLOR
from core.colors import ACTIVE_COLOR
from core.colors import SORTED_COLOR

from rendering.bar import Bar

from core.config import (
    WINDOW_HEIGHT,
    BAR_WIDTH
)


class Renderer:

    def __init__(self, screen):
        self.screen = screen

    def render(self, state):

        self.screen.fill(BACKGROUND)

        for index, value in enumerate(state.data):

            x = index * (BAR_WIDTH + 2)

            y = WINDOW_HEIGHT - value

            color = BAR_COLOR

            if index in state.active_indices:
                color = ACTIVE_COLOR

            elif index in state.sorted_indices:
                color = SORTED_COLOR

            bar = Bar(
                x=x,
                y=y,
                width=BAR_WIDTH,
                height=value,
                color=color
            )

            bar.draw(self.screen)

        pygame.display.flip()