# Advent of Code 2022
import os
import sys
import math
from utility.utility import *

# Day 9 - Rope Bridge
day = os.path.basename(__file__)[:-3].split("_")[1]


class knot:
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1
        self.all_positions = {f"{x1},{y1}": 1}

    def __repr__(self):
        return f"{self.x},{self.y}"

    def move(self, d):
        if d == "U":
            self.y += 1
        elif d == "D":
            self.y -= 1
        elif d == "R":
            self.x += 1
        elif d == "L":
            self.x -= 1
        else:
            ValueError(f"CANNOT MOVE IN DIRECTION [{d}]")
        self.register_pos()

    def chase(self, tx, ty):
        if abs(tx - self.x) > 1 or abs(ty - self.y) > 1:
            # too far away, needs to move
            # which direction do we move?
            diff_x = tx - self.x
            diff_y = ty - self.y
            if diff_x == 0:
                # we are in the same column
                if diff_y > 1:
                    # we need to move up
                    self.y += 1
                elif diff_y < -1:
                    # we need to move down
                    self.y -= 1
                else:
                    ValueError("(SAME COL) We shouldnt be able to get to here if we are more than 1 away")
            elif diff_y == 0:
                # we are in the same row
                if diff_x > 1:
                    # we need to move right
                    self.x += 1
                elif diff_x < -1:
                    # we need to move left
                    self.x -= 1
                else:
                    ValueError("(SAME ROW) We shouldnt be able to get to here if we are more than 1 away")
            else:
                # we are diagonally different.
                if diff_x > 0:
                    # move to the right
                    self.x += 1
                elif diff_x < 0:
                    # move to the left
                    self.x -= 1
                if diff_y > 0:
                    # move up
                    self.y += 1
                elif diff_y < 0:
                    # move down
                    self.y -= 1
            self.register_pos()

    def register_pos(self):
        # register new position
        sp = f"{self.x}{self.y}"
        if sp in self.all_positions:
            self.all_positions[sp] += 1
        else:
            self.all_positions[sp] = 1

    @property
    def count_unique_positions(self):
        return len(self.all_positions.keys())


def run():
    print("==========================================================")
    print("                ADVENT OF CODE 2022: DAY {}                ".format(day))
    print("==========================================================")
    input_filename = "day_{}_in.txt".format(day)
    lines = read_all_lines(os.path.join("inputs", input_filename))
    if len(lines) == 0:
        print("Day {} has no input - Skipping".format(day))
    else:
        # Part 1 =======================================================================================================
        print("=====================   PART 1   =========================")
        head = knot(0, 0)
        tail = knot(0, 0)
        for l in lines:
            direction, count = l.split()
            count = int(count)
            for _ in range(count):
                head.move(direction)
                tail.chase(head.x, head.y)

        print(tail.count_unique_positions)
        # ==============================================================================================================
        # Part 2 =======================================================================================================
        print("=====================   PART 2   =========================")
        knots = []
        for _ in range(10):
            knots.append(knot(0, 0))

        for l in lines:
            direction, count = l.split()
            count = int(count)
            for _ in range(count):
                for i, k in enumerate(knots):
                    if i == 0:
                        k.move(direction)
                    else:
                        k.chase(knots[i-1].x, knots[i-1].y)

        print(knots[9].count_unique_positions)
        # ==============================================================================================================
        print("==========================================================")

