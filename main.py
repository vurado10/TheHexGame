import sys
import pygame
from rgb_colors import RgbColors
from button import Button
from hexagon_figure import HexagonFigure
from hexagon_painter import HexagonPainter
from pygame.math import Vector2

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    scene = None

    test_button = Button(HexagonFigure(
        Vector2(250, 250),
        50,
        0,
        HexagonPainter(screen,
                       0.95,
                       RgbColors.WHITE,
                       RgbColors.BLACK,
                       RgbColors.WHITE)
    ))

    test_button.on_click_function = lambda: test_button.switch_state()

    while True:
        clock.tick(40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if test_button.is_clicked(Vector2(pygame.mouse.get_pos())):
                    test_button.on_click_function()


        # image = pygame.image.load("test_image.jpg")
        # screen.blit(pygame.transform.scale(image, (160, 90)), (150, 150))

        pygame.display.flip()
