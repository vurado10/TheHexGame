import sys
import pygame

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    while True:
        clock.tick(40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        rectangles = [
            pygame.draw.rect(screen,
                             (0, 128, 128),
                             (50 + i * 10, 50 + i * 10, 100, 100), i)
            for i in range(0, 5)]

        image = pygame.image.load("test_image.jpg")
        screen.blit(pygame.transform.scale(image, (160, 90)), (150, 150))

        pygame.display.flip()
