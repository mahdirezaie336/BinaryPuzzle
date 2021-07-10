from constants import Consts
from constraint import UnaryConstraint, BinaryConstraint
from graph import Node, Arc


def two_diff(cell1, cell2, _):
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


def same_row_and_column(cell1, cell2, node1, node2):
    """ A binary constraint function that checks whether a row and a column can be
        in a table or no."""
    i = node1.get_id()[1]
    j = node2.get_id()[1]
    return cell1[j] == cell2[i]


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

        two_diff_constraint = BinaryConstraint(two_diff)
        # Connect each vertical node to the other
        for i in range(len(vertical_nodes)):
            for j in range(i+1, len(vertical_nodes)):
                node1 = vertical_nodes[i]
                node2 = vertical_nodes[j]
                arc = Arc(node1, node2, two_diff_constraint)
                node1.connect_to_another_node(node2, arc)

        # Connect each horizontal node to the other
        for i in range(len(horizontal_nodes)):
            for j in range(i + 1, len(horizontal_nodes)):
                node1 = horizontal_nodes[i]
                node2 = horizontal_nodes[j]
                arc = Arc(node1, node2, two_diff_constraint)
                node1.connect_to_another_node(node2, arc)


def main():
    read_map()


main()
