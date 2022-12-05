# Advent of Code 2022
import os
import sys
import math
from utility.utility import *

# Day 2 - Rock Paper Scissors
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
        rock = 1
        paper = 2
        scissors = 3
        oppr = "A"
        oppp = "B"
        opps = "C"
        mer = "X"
        mep = "Y"
        mes = "Z"
        opp = None
        me = None
        score = 0
        for l in lines:
            left, right = l.split()
            if left == oppr:
                opp = rock
            elif left == oppp:
                opp = paper
            else:
                opp = scissors
            if right == mer:
                me = rock
            elif right == mep:
                me = paper
            else:
                me = scissors

            score += me
            if me == rock and opp == scissors or \
                me == paper and opp == rock or \
                me == scissors and opp == paper:
                score += 6
            elif me == opp:
                score += 3
        print (score)

        # ==============================================================================================================
        # Part 2 =======================================================================================================
        print("=====================   PART 2   =========================")
        score2 = 0
        for l in lines:
            opp, req = l.split()
            if req == "X":
                # need to lose
                if opp == oppr:
                    score2 += scissors
                elif opp == opps:
                    score2 += paper
                else:
                    score2 += rock
            elif req == "Z":
                # need to win
                score2 += 6
                if opp == oppr:
                    score2 += paper
                elif opp == opps:
                    score2 += rock
                else:
                    score2 += scissors
            else:
                if opp == oppr:
                    score2 += rock
                elif opp == opps:
                    score2 += scissors
                else:
                    score2 += paper
                score2 += 3
        print (score2)
        # ==============================================================================================================
        print("==========================================================")

