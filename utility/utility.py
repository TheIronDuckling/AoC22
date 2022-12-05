import os
from copy import *
from pprint import pprint
import sys


def read_all_lines(file_name):
    """
    read all lines in a text file and return a list of lines.
    :param file_name: file to read
    :return: list of strings
    """
    with open(os.path.join(".", file_name), "r") as f:
        lines = [l.strip() for l in f]
    return lines


def read_all_lines_no_strip(file_name):
    """
    read all lines in a text file without stripping whitespace and return a list of lines
    :param file_name: file to read
    :return: list of strings
    """
    with open(os.path.join(".", file_name), "r") as f:
        lines = [l[:-1] if l[-1] == "\n" else l for l in f]
    return lines


def remove_char_from_string_at_index(org_string, idx):
    """
    remove a character from a string at a given index
    :param org_string: string to modify
    :param idx: index to remove
    :return: new string
    """
    return org_string[:idx] + org_string[idx+1:]


def remove_all_characters(in_str, c):
    """
    remove all instances of a given character (both upper and lower case) from a string
    :param in_str: string to modify
    :param c: character to remove (any string character)
    :return: new string
    """
    return in_str.replace(c.lower(), "").replace(c.upper(), "")\


def dijkstra_weighted_field(map, start, end, count_start_in_cost=False, allow_diag=False):
    class Node:
        def __init__(self, x, y, risk, others):
            self.x = x
            self.y = y
            self.risk = risk
            self.others = others
            self.adj = []
            self.visited = False
            self.min_to_here = sys.maxsize
            self.min_path_to_here = []
            self.coords = (self.y, self.x)

        @property
        def max_x(self):
            return len(self.others[0]) - 1

        @property
        def max_y(self):
            return len(self.others) - 1

        def calc_adjacent(self, allow_diag=False):
            up_avail = self.y > 0
            down_avail = self.y < self.max_y
            left_avail = self.x > 0
            right_avail = self.x < self.max_x
            if left_avail:
                self.adj.append(self.others[self.y][self.x - 1])
            if right_avail:
                self.adj.append(self.others[self.y][self.x + 1])
            if up_avail:
                self.adj.append(self.others[self.y - 1][self.x])
            if down_avail:
                self.adj.append(self.others[self.y + 1][self.x])
            if allow_diag:
                if up_avail and left_avail:
                    self.adj.append(self.others[self.y - 1][self.x - 1])
                if up_avail and right_avail:
                    self.adj.append(self.others[self.y - 1][self.x + 1])
                if down_avail and left_avail:
                    self.adj.append(self.others[self.y + 1][self.x - 1])
                if down_avail and right_avail:
                    self.adj.append(self.others[self.y + 1][self.x + 1])

        def check_neighbours(self):
            mn = min(self.adj, key=lambda x: x.min_to_here)
            nm = mn.min_to_here + self.risk
            if nm < self.min_to_here:
                self.min_to_here = nm
                self.min_path_to_here = mn.min_path_to_here + [self.coords]
            self.visited = True
            for a in self.adj:
                mi = self.min_to_here + a.risk
                if mi < a.min_to_here and a.visited:
                    a.check_neighbours()
    nm = []
    for y_idx, y in enumerate(map):
        nm.append([])
        for x_idx, r in enumerate(y):
            nm[y_idx].append(Node(x=x_idx, y=y_idx, risk=int(r), others=nm))

    sn = nm[start[0]][start[1]]
    for y in nm:
        for x in y:
            x.calc_adjacent(allow_diag=allow_diag)
    sn.min_to_here = 0 if not count_start_in_cost else sn.risk
    sn.min_path_to_here = [sn.coords]
    for y in nm:
        for x in y:
            x.check_neighbours()
    en = nm[end[0]][end[1]]
    return en.min_to_here, en.min_path_to_here


if __name__ == "__main__":
    map =  [[int(a) for a in "1163751742"],
            [int(a) for a in "1381373672"],
            [int(a) for a in "2136511328"],
            [int(a) for a in "3694931569"],
            [int(a) for a in "7463417111"],
            [int(a) for a in "1319128137"],
            [int(a) for a in "1359912421"],
            [int(a) for a in "3125421639"],
            [int(a) for a in "1293138521"],
            [int(a) for a in "2311944581"]]
    start = [0, 0]
    end = [len(map) - 1, len(map[0]) - 1]
    cost, path = dijkstra_weighted_field(map, start, end, count_start_in_cost=False, allow_diag=True)
    print(cost)
    print(path)
    for i in path:
        cm = deepcopy(map)
        for i in path:
            map[i[0]][i[1]] = " "
    for l in cm:
        print("".join([str(a) for a in l]))