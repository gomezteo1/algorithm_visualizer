import pygame

##conectar el HUD al renderer.
from ui.hud import HUD

from core.colors import (
    BACKGROUND,
    BAR_COLOR,
    ACTIVE_COLOR,
    SORTED_COLOR
)

from rendering.bar import Bar

from core.config import (
    WINDOW_HEIGHT,
    BAR_WIDTH
)


class Renderer:

    def __init__(self, screen, array_size):

        self.screen = screen
        
        self.bars = []

        self.hud = HUD()
        
        for index in range(array_size):

            x = index * (BAR_WIDTH + 2)

            bar = Bar(x, BAR_WIDTH)

            self.bars.append(bar)

    def render(self, state):

        self.screen.fill(BACKGROUND)

        for index, value in enumerate(state.data):

            color = BAR_COLOR

            if index in state.active_indices:
                color = ACTIVE_COLOR

            elif index in state.sorted_indices:
                color = SORTED_COLOR

            self.bars[index].update(value, color)

            self.bars[index].draw(
                self.screen,
                WINDOW_HEIGHT
            )
        self.hud.draw(
            self.screen,
            state
        )
        pygame.display.flip()