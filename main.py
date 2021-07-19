from cell import Cell
from constants import Consts
from constraint import UnaryConstraint, BinaryConstraint
from graph import Node, Arc
import heapq

from screenmanager import Display


def two_diff(cell1, cell2, node1, node2) -> bool:
    """ A constraint function which checks if two cells are equal. """
    return cell1 != cell2


def same_number_of_digits(cell) -> bool:
    """ A constraint function which checks if number of 1s is equal to 0s. """
    return cell.count_substring('1') == cell.count_substring('0')


def more_than_two_digits(cell) -> bool:
    """ A constraint functions which checks if there is more than
        two same digits in a cell consecutive. """
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


def read_map() -> (list[Node], list[Node]):
    """ Reads map from file,
        Creates node of constraint graph,
        Creates arcs of constraint graph and sets the constraint function on them,
        Connects each node via the corresponding arc and
        Applies the map limitation on each node.
        :returns List of all vertical nodes and horizontal nodes
        """
    map_object = []
    # Opening map file
    with open(Consts.MAP_FILE, 'r') as map_file:
        w, h = (int(i) for i in map_file.readline().split())

        # Reading rows
        rows = []
        for row in map_file:
            if row == '':
                continue
            rows.append(''.join(row.split()))

        # Reading columns
        columns = [''] * w
        for row in rows:
            for i, char in enumerate(row):
                columns[i] += char

        # Create horizontal nodes
        horizontal_nodes = []
        for i, mask in enumerate(rows):
            map_object.append(mask)
            node = Node(('h', i), len(mask))
            node.apply_mask_filter(mask)
            horizontal_nodes.append(node)

        # Create vertical nodes
        vertical_nodes = []
        for i, mask in enumerate(columns):
            node = Node(('v', i), len(mask))
            node.apply_mask_filter(mask)
            vertical_nodes.append(node)

        # Some binary constraints
        two_diff_constraint = BinaryConstraint(two_diff)
        same_rac_constraint = BinaryConstraint(same_row_and_column)

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

        # Connect horizontal nodes to verticals
        for h_node in horizontal_nodes:
            for v_node in vertical_nodes:
                arc = Arc(h_node, v_node, same_rac_constraint)
                h_node.connect_to_another_node(v_node, arc)

    return horizontal_nodes, vertical_nodes, map_object


def forward_check(node: Node):
    for arc in node.get_arcs():
        arc.make_me_consistent(node)


def backtrack_search(all_nodes: list[Node], res_iter: list[tuple[Node, Cell]]):
    """ Performs a backtrack search on list of nodes which is sorted. """
    if len(all_nodes) <= 0:
        return 0
    root = all_nodes.pop()
    if len(root.get_possible_cells()) == 0:
        return -1
    for cell in root.get_possible_cells():
        root.set_value(cell)
        forward_check(root)
        heapq.heapify(all_nodes)
        res = backtrack_search(all_nodes.copy(), res_iter)
        if res == 0:
            res_iter.append((root, cell))
            return 0
        root.undo_applying_binary_constraint()
        for node in root.get_a_list_of_neighbours():
            node.undo_applying_binary_constraint()
    return -1


def main():
    h, v, map_object = read_map()

    all_nodes = []
    all_nodes.extend(h)
    all_nodes.extend(v)

    # Applying unary constraints
    same_nod_constraint = UnaryConstraint(same_number_of_digits)
    more_ttd_constraint = UnaryConstraint(more_than_two_digits)
    for node in all_nodes:
        node.apply_unary_constraint(same_nod_constraint)
        node.apply_unary_constraint(more_ttd_constraint)

    # Running solution
    heapq.heapify(all_nodes)
    result_iteration = []
    res_code = backtrack_search(all_nodes.copy(), result_iteration)

    # Showing result
    display = Display(map_object)
    display.begin_display()
    display.show_solution(result_iteration)
    if res_code == -1:
        print('The problem has no answer')
    for i in h:
        print(i.get_possible_cells())
    pass


main()
