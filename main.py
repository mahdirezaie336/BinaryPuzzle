from constants import Consts


def read_map():
    with open(Consts.MAP_FILE, 'r') as map_file:
        w, h = (int(i) for i in map_file.readline().split())
        rows = []
        for row in map_file:
            rows.append(''.join(row.split()))

        columns = [''] * w
        for row in rows:
            for i, char in enumerate(row):
                columns[i] += char



def main():
    read_map()


main()
