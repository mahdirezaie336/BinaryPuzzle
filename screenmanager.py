import pygame

from constants import Consts


class Display:

    def __init__(self):
        self.__map = map_ + 'F'
        self.__w = len(map_) + 1
        self.__h = 4
        w, h = self.__w, self.__h

        # PyGame part
        pygame.init()
        sw, sh = Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT
        self.screen = pygame.display.set_mode((sw, sh))
        self.screen.fill(Consts.BACKGROUND_COLOR)

        # Setting cell size and other sizes
        if w / h > sw / sh:
            rect_width = sw - 2 * Consts.SCREEN_MARGIN_SIZE
            cell_size = int(rect_width / w)
            rect_height = cell_size * h
        else:
            rect_height = sh - 2 * Consts.SCREEN_MARGIN_SIZE
            cell_size = int(rect_height / h)
            rect_width = cell_size * w
        self.cell_size = cell_size
        self.rect_width = rect_width
        self.rect_height = rect_height

        self.draw_cells()
        pygame.display.update()

    def draw_cells(self):
        pass
