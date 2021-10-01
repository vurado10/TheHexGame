import sys
import pygame
from button import Button
from hex_field import HexField
from pygame.math import Vector2
from rectangular_figure import RectangularFigure
from rectangular_painter import RectangularPainter
from rgb_colors import RgbColors

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((800, 450))
    clock = pygame.time.Clock()
    scene = None

    hex_field = HexField(screen, 11, 11, RgbColors.WHITE,
                         RgbColors.BLACK, RgbColors.WHITE, RgbColors.BLACK)
    hex_field.show()

    # button = Button(RectangularFigure(Vector2(250, 250), 80, 45,
    #                                   RectangularPainter(screen,
    #                                                      RgbColors.WHITE)))
    #
    # button.on_click_function = lambda b: print("Clicked")

    while True:
        clock.tick(40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if button.is_clicked(Vector2(pygame.mouse.get_pos())):
                #     button.on_click_function(button)
                for i in hex_field.controls:
                    if i.is_clicked(Vector2(pygame.mouse.get_pos())):
                        i.on_click_function(i)
                        break

        pygame.display.flip()
