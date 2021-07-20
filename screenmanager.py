import sys
import threading
import time

import pygame

from cell import Cell
from constants import Consts
from graph import Node


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

        one_image = pygame.image.load(Consts.ONE_IMAGE).convert_alpha()
        one_image = pygame.transform.scale(one_image, (cell_size, cell_size))
        one_image = Display.colorize(one_image, Consts.SOLID_COLOR)
        one_image_s = Display.colorize(one_image, Consts.SOFT_COLOR)
        zero_image = pygame.image.load(Consts.ZERO_IMAGE).convert_alpha()
        zero_image = pygame.transform.scale(zero_image, (cell_size, cell_size))
        zero_image = Display.colorize(zero_image, Consts.SOLID_COLOR)
        zero_image_s = Display.colorize(zero_image, Consts.SOFT_COLOR)
        self.images = {'1': one_image,
                       '0': zero_image,
                       '1S': one_image_s,
                       '0S': zero_image_s}

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

    def draw_cell(self, h_or_v: str, index: int, cell: Cell):
        if h_or_v == 'h':
            for i in range(len(cell)):
                self.draw_in_position(index, i, self.images[str(cell[i]) + 'S'])
        elif h_or_v == 'v':
            for i in range(len(cell)):
                self.draw_in_position(i, index, self.images[str(cell[i]) + 'S'])

    def show_solution(self, solution_list: list[tuple[Node, Cell]]):
        # Clearing screen
        self.draw_cells()

        # Putting items into screen
        for item in solution_list:
            time.sleep(Consts.TIME_STEP)
            cell = item[1]
            node_id = item[0].get_id()
            self.draw_cell(node_id[0], node_id[1], cell)

    @staticmethod
    def colorize(image, new_color):
        """
        Create a "colorized" copy of a surface (replaces RGB values with the given color, preserving the per-pixel alphas of
        original).
        :param image: Surface to create a colorized copy of
        :param new_color: RGB color to use (original alpha values are preserved)
        :return: New colorized Surface instance
        """
        image = image.copy()

        # zero out RGB values
        image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
        # add in new RGB values
        image.fill(new_color + '00', None, pygame.BLEND_RGBA_ADD)

        return image

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
