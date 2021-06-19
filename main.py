from constants import Consts
from node import Node


def read_map():
    with open(Consts.MAP_FILE, 'r') as map_file:
        w, h = (int(i) for i in map_file.readline().split())
        rows = []
        for row in map_file:
            if row == '':
                continue
            rows.append(''.join(row.split()))

        columns = [''] * w
        for row in rows:
            for i, char in enumerate(row):
                columns[i] += char

        # Create horizontal nodes
        horizontal_nodes = []
        for i, mask in enumerate(rows):
            node = Node(('h', i), len(mask))
            node.apply_mask_filter(mask)
            horizontal_nodes.append(node)

        # Create vertical nodes
        vertical_nodes = []
        for i, mask in enumerate(columns):
            node = Node(('v', i), len(mask))
            node.apply_mask_filter(mask)
            vertical_nodes.append(node)

        #


def main():
    read_map()


main()
