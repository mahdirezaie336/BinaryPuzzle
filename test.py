import pygame

pygame.init()


def colorize(image, newColor):
    """
    Create a "colorized" copy of a surface (replaces RGB values with the given color, preserving the per-pixel alphas of
    original).
    :param image: Surface to create a colorized copy of
    :param newColor: RGB color to use (original alpha values are preserved)
    :return: New colorized Surface instance
    """
    image = image.copy()

    # zero out RGB values
    image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
    # add in new RGB values
    image.fill(newColor[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)

    return image


screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))
image = pygame.image.load('./images/1.png').convert_alpha()
screen.blit(colorize(image, (255, 0, 0)), (100, 100))

pygame.display.update()
while True:
    pygame.event.pump()
