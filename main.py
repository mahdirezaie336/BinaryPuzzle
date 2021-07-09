from constants import Consts
from graph import Node


def two_diff(cell1, cell2):
    return cell1 != cell2


def same_number_of_digits(cell):
    return cell.count_substring('1') == cell.count_substring('0')


def more_than_two_digits(cell):
    cell_str = str(cell)
    count = 0
    last_digit = ''
    for char in cell_str:
        if char == last_digit:
            count += 1
        else:
            count = 0
            last_digit = char
        if count == 2:
            return False
    return True


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
