import math
import sys
import pygame
import rgb_colors
from hexagon_painter import HexagonPainter
from pygame.math import Vector2

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    while True:
        clock.tick(40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        painter = HexagonPainter(screen,
                                 10,
                                 rgb_colors.RgbColors.WHITE,
                                 rgb_colors.RgbColors.WHITE)

        painter.draw(Vector2(200, 200),
                                 50,
                                 0)
        painter.draw(Vector2(200, 200 + (50**2 * 3**(1/2) / (2 * 50)) * 2),
                                 50,
                                 0)

        # rectangles = [
        #     pygame.draw.rect(screen,
        #                      (0, 128, 128),
        #                      (50 + i * 10, 50 + i * 10, 100, 100), i)
        #     for i in range(0, 5)]
        #
        # image = pygame.image.load("test_image.jpg")
        # screen.blit(pygame.transform.scale(image, (160, 90)), (150, 150))

        pygame.display.flip()
