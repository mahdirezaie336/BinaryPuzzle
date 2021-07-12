import sys
import threading

import pygame

from constants import Consts


class Display:

    def __init__(self, map_):
        self.__map = map_
        w = self.__w = len(map_[0])
        h = self.__h = len(map_)

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

        one_image = pygame.image.load(Consts.ONE_IMAGE)
        zero_image = pygame.image.load(Consts.ZERO_IMAGE)
        self.images = {'1': pygame.transform.scale(one_image, (cell_size, cell_size)),
                       '0': pygame.transform.scale(zero_image, (cell_size, cell_size))}

        self.draw_cells()
        pygame.display.update()

    def draw_cells(self):
        sw, sh = Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT
        w, h = self.__w, self.__h
        rect_width, rect_height = self.rect_width, self.rect_height
        cell_size = self.cell_size

        # Drawing cells
        init_y = (sh - rect_height) / 2
        init_x = (sw - rect_width) / 2
        for j in range(h):
            for i in range(w):
                x = init_x + i * cell_size
                y = init_y + j * cell_size
                color = Consts.CELL_COLOR
                # Drawing Rectangles
                pygame.draw.rect(self.screen, color, (x, y, cell_size - 2, cell_size - 2), 0)
                if self.__map[j][i] in ['1', '0']:
                    self.draw_in_position(j, i, self.images[self.__map[j][i]])

    def draw_in_position(self, y: int, x: int, image):
        init_y = (Consts.SCREEN_HEIGHT - self.rect_height) / 2
        init_x = (Consts.SCREEN_WIDTH - self.rect_width) / 2
        pos_x = init_x + x * self.cell_size
        pos_y = init_y + y * self.cell_size
        self.screen.blit(image, (pos_x, pos_y))

    def begin_display(self):

        def infinite_loop():
            """ This is the function which includes the infinite loop for pygame pumping. """
            while True:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        sys.exit(0)

                pygame.display.update()
                pygame.time.wait(int(1000 / Consts.FPS))

        # Starting thread
        display_thread = threading.Thread(name='Display', target=infinite_loop)
        display_thread.setDaemon(False)
        display_thread.start()
