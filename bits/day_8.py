# Advent of Code 2022
import os
import sys
import math
from utility.utility import *

# Day 8
day = os.path.basename(__file__)[:-3].split("_")[1]


def count_taller(my_val, others):
    visible = 0
    for t in others:
        if t < my_val:
            visible += 1
        elif t >= my_val:
            visible += 1
            break
    return visible


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
        m = []
        for l in lines:
            m.append([int(c) for c in l])

        for r in m:
            print(r)
        max_row = len(m) - 1
        max_column = len(m[0]) - 1
        visible = 0
        for row_index, row in enumerate(m):
            for column_index, tree in enumerate(row):
                # is it on the outside?
                if column_index == 0 or column_index == max_column or row_index == 0 or row_index == max_row:
                    #print(f"Tree at {row_index}:{column_index} is visible.")
                    visible += 1
                else:
                    whole_column = [c[column_index] for c in m]
                    whole_row = row
                    # is it visible from north
                    max_north = max(whole_column[:row_index])
                    max_south = max(whole_column[row_index+1:])
                    max_east = max(whole_row[column_index+1:])
                    max_west = max(whole_row[:column_index])
                    if tree > max_north:
                        #print(f"Tree at {row_index}:{column_index} is visible from the NORTH.")
                        visible += 1
                    elif tree > max_south:
                        #print(f"Tree at {row_index}:{column_index} is visible from the SOUTH.")
                        visible += 1
                    elif tree > max_east:
                        #print(f"Tree at {row_index}:{column_index} is visible from the EAST.")
                        visible += 1
                    elif tree > max_west:
                        #print(f"Tree at {row_index}:{column_index} is visible from the WEST.")
                        visible += 1
                    else:
                        pass
        print(f"{visible} TREES are visible.")
        # ==============================================================================================================
        # Part 2 =======================================================================================================
        print("=====================   PART 2   =========================")
        max_scenic_score = -1
        for row_index, row in enumerate(m):
            for column_index, tree in enumerate(row):
                my_value = tree
                whole_column = [c[column_index] for c in m]
                whole_row = row
                all_north = whole_column[:row_index]
                all_north.reverse()  # want to look going OUT so the deepest is first
                all_south = whole_column[row_index+1:]  # already in the right order
                all_east = whole_row[column_index + 1:]  # already in the right order
                all_west = whole_row[:column_index]
                all_west.reverse()  # want to look going OUT to deepest is first
                visible_north = count_taller(my_value, all_north)
                visible_south = count_taller(my_value, all_south)
                visible_east = count_taller(my_value, all_east)
                visible_west = count_taller(my_value, all_west)
                scenic_score = visible_north * visible_south * visible_east * visible_west
                max_scenic_score = max(max_scenic_score, scenic_score)
        print(f"Maximum Scenic Score is: {max_scenic_score}")


        # ==============================================================================================================
        print("==========================================================")

