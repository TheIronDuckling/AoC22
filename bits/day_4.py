# Advent of Code 2022
import os
import sys
import math
from utility.utility import *

# Day 4 - Camp Cleanup
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
        total = 0
        for l in lines:
            elf1_range, elf2_range = l.split(",")
            elf1_split = elf1_range.split("-")
            elf2_split = elf2_range.split("-")
            elf1_start = int(elf1_split[0])
            elf1_end = int(elf1_split[1])
            elf2_start = int(elf2_split[0])
            elf2_end = int(elf2_split[1])

            # does one contain the other
            if (elf1_start <= elf2_start and elf1_end >= elf2_end) or \
                    (elf2_start <= elf1_start and elf2_end >= elf1_end):
                total += 1
        print(total)
        # ==============================================================================================================
        # Part 2 =======================================================================================================
        print("=====================   PART 2   =========================")
        total2 = 0
        for l in lines:
            elf1_range, elf2_range = l.split(",")
            elf1_split = elf1_range.split("-")
            elf2_split = elf2_range.split("-")
            elf1_start = int(elf1_split[0])
            elf1_end = int(elf1_split[1])
            elf2_start = int(elf2_split[0])
            elf2_end = int(elf2_split[1])

            if (elf2_start >= elf1_start and elf2_start <= elf1_end) or \
                    (elf1_start >= elf2_start and elf1_start <= elf2_end):
                total2 += 1
        print(total2)
        # ==============================================================================================================
        print("==========================================================")

