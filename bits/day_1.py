# Advent of Code 2022
import os
import sys
import math
from utility.utility import *

# Day 1 - Calorie Counting
day = os.path.basename(__file__)[:-3].split("_")[1]


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
        elves = []
        current_count = 0
        for l in lines:
            if l == "":
                elves.append(current_count)
                current_count = 0
            else:
                current_count += int(l)
        print(f"Elf with most calories has: {max(elves)}")
        # ==============================================================================================================
        # Part 2 =======================================================================================================
        print("=====================   PART 2   =========================")
        top_3 = sorted(elves)[-3:]
        print(f"Top 3 Calorie holding Elves have: {top_3}")
        print(f"Together summing: {sum(top_3)}")
        # ==============================================================================================================
        print("==========================================================")

