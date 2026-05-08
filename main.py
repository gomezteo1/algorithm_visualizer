import pygame

from core.config import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    FPS,
    SORT_SPEED
)

from utils.helpers import generate_random_data

from algorithms.bubble_sort import BubbleSort

from rendering.renderer import Renderer


class VisualizerApp:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )

        pygame.display.set_caption(
            "Algorithm Visualizer"
        )

        self.clock = pygame.time.Clock()

        self.data = generate_random_data()
        
        self.renderer = Renderer(
            self.screen,
            len(self.data)
        )

        

        self.sort_generator = BubbleSort.sort(self.data)

        self.running = True

    def run(self):

        frame_counter = 0

        while self.running:

            self.clock.tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

            if frame_counter % SORT_SPEED == 0:

                try:
                    state = next(self.sort_generator)
                    self.renderer.render(state)

                except StopIteration:
                    pass

            frame_counter += 1

        pygame.quit()


if __name__ == "__main__":

    app = VisualizerApp()

    app.run()