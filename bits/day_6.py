# Advent of Code 2022
import os
import sys
import math
from utility.utility import *
from cProfile import Profile

# Day 6 - Tuning Trouble
day = os.path.basename(__file__)[:-3].split("_")[1]


def find_first_unique(input, unique_size):
    index = 0
    substring = []
    while index <= len(input):
        substring.append(input[index])
        index += 1
        if index < unique_size - 1:
            continue
        else:
            if len(substring) > unique_size:
                substring = substring[1:]
            unique = set(substring)
            if len(unique) == unique_size:
                print(index)
                break


def find_first_unique_j(input, unique_size):
    for index in range(len(input)):
        t = input[index:index+unique_size]
        if len(set(t)) == unique_size:
            print(index + unique_size)
            break


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
        input = lines[0]
        find_first_unique(input, 4)
        find_first_unique_j(input, 4)
        # =============================================================================================================
        # Part 2 =======================================================================================================
        print("=====================   PART 2   =========================")
        find_first_unique(input, 14)
        find_first_unique_j(input, 14)
        # ==============================================================================================================
        print("==========================================================")

