# Advent of Code 2022
import os
import sys
import math
from utility.utility import *

# Day 10 - Cathode-Ray Tube
day = os.path.basename(__file__)[:-3].split("_")[1]
class cpu:
    def __init__(self):
        self.regx = 1
        self.cycles = 1
        self.curr_inst = []
        self.prev_inst = None
        self.check_points = []
        self.total_checks = 0

    def register_check_point(self, i):
        self.check_points.append(i)

    def tick(self):
        if self.cycles in self.check_points:
            strength = self.cycles * self.regx
            print(f"CPU CYCLE {self.cycles} START: REGX [{self.regx}] : Signal Strength [{strength}]")
            self.total_checks += strength
        self.cycles += 1
        if len(self.curr_inst) > 0:
            next_inst = self.curr_inst[0]
            if next_inst in ["noop", "addx"]:
                pass
            elif self.prev_inst == "addx":
                self.regx += int(next_inst)
            self.prev_inst = next_inst
            self.curr_inst = self.curr_inst[1:]

    @property
    def is_busy(self):
        return len(self.curr_inst) > 0

    def instruction(self, i: str):
        self.curr_inst = i.split()

    def __addx(self, val):
        self.regx += val

    def __noop(self):
        pass

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
        c = cpu()
        [c.register_check_point(a) for a in [20, 60, 100, 140, 180, 220]]
        while len(lines) > 0:
            while c.is_busy:
                c.tick()
            c.instruction(lines[0])
            lines = lines[1:]
        print(c.total_checks)
        # ==============================================================================================================
        # Part 2 =======================================================================================================
        print("=====================   PART 2   =========================")
        lines = read_all_lines(os.path.join("inputs", input_filename))
        tv = ""
        c = cpu()
        display = []
        while len(lines) > 0 or c.is_busy:
            if not c.is_busy:
                if len(lines) > 0:
                    c.instruction(lines[0])
                lines = lines[1:]
            sprite_pos = c.regx
            check_pos = c.cycles % 40
            ns = " "
            if sprite_pos <= check_pos <= sprite_pos + 2:
                ns = "#"
            tv = f"{tv}{ns}"
            if len(tv) == 40:
                display.append(tv)
                tv = ""
            c.tick()
        for r in display:
            print(r)
        # ==============================================================================================================
        print("==========================================================")

