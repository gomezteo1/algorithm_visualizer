import pygame


class Bar:

    def __init__(self, x, width):

        self.x = x
        self.width = width

        self.height = 0
        self.color = (255, 255, 255)

    def update(self, height, color):

        self.height = height
        self.color = color

    def draw(self, screen, window_height):

        rect = pygame.Rect(
            self.x,
            window_height - self.height,
            self.width,
            self.height
        )

        pygame.draw.rect(screen, self.color, rect)

        font = pygame.font.SysFont(
            "consolas",
            18
        )

        text = font.render(
            str(self.height),
            True,
            (250,255,255)
        )

        text_rect = text.get_rect(
            center=(
                self.x + self.width // 2,
                window_height - self.height - 15
            )
        )

        screen.blit(text, text_rect)

        pygame.draw.rect(screen, self.color, rect)