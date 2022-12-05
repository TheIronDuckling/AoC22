# Advent of Code 2022
import os
import sys
import math
from utility.utility import *

# Day 3 - Rucksack Reorganisation
day = os.path.basename(__file__)[:-3].split("_")[1]

lower_start = 1
upper_start = 27


def get_value(char):
    assert isinstance(char, str)
    if char.islower():
        return ord(char) - ord("a") + lower_start
    else:
        return ord(char) - ord("A") + upper_start


def find_common(l, r):
    for i in l:
        if i in r:
            return i


def find_common_three(f, s, t):
    for i in f:
        if i in s and i in t:
            return i


def find_common_list(l):
    """
    Take a list of strings, and find the common character between them
    """
    for c in l[0]:
        if all([c in b for b in l[1:]]):
            return c


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
            length = len(l) // 2
            left = l[:length]
            right = l[length:]
            #print(f"{left}||{right}")
            #c = find_common(left, right)
            c = find_common_list([left, right])
            v = get_value(c)
            #print(f"{c} || {v}")
            total += v
        print(f"TOTAL: {total}")
        # ==============================================================================================================
        # Part 2 =======================================================================================================
        print("=====================   PART 2   =========================")
        total2 = 0
        group = []
        for l in lines:
            group.append(l)
            if len(group) == 3:
                #print(group)
                #c = find_common_three(group[0], group[1], group[2])
                c = find_common_list(group)
                #print(c)
                v = get_value(c)
                #print(v)
                total2 += v
                group = []
        print(f"TOTAL 2: {total2}")
        # ==============================================================================================================
        print("==========================================================")

