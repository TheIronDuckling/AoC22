# Advent of Code 2022
from utility.utility import *
from queue import LifoQueue
# Day 5 - Supply Stacks
day = os.path.basename(__file__)[:-3].split("_")[1]


class Crate:
    def __init__(self, s):
        self.s = s
        self.letter = self.s[1]


def move_boxes_and_print_top(lines, lift_multi=False):
    split_point = lines.index("")
    inst_lines = lines[split_point+1:]
    stack_lines = lines[:split_point]
    stack_lines.reverse()

    # Parse and Create Stacks
    stacks = {int(a): LifoQueue() for a in stack_lines[0].split()}
    stack_count = max(stacks.keys())
    for sl in stack_lines[1:]:
        for i in range(1, stack_count+1):
            c = sl[(i - 1) * 4:(i * 4)].strip()
            if c != "":
                stacks[i].put(Crate(s=c))

    # Parse and Perform Instructions
    for il in inst_lines:
        count, src, dst = (int(a) for a in il.split() if a.isnumeric())
        if lift_multi:
            temp_queue = LifoQueue()
            for _ in range(count):
                temp_queue.put(stacks[src].get())
            for _ in range(count):
                stacks[dst].put(temp_queue.get())
        else:
            for _ in range(count):
                temp = stacks[src].get()
                stacks[dst].put(temp)

    # Print Final Arrangement
    final = "".join([s.get().letter for _, s in stacks.items()])
    print(final)


def run():
    print("==========================================================")
    print("                ADVENT OF CODE 2022: DAY {}                ".format(day))
    print("==========================================================")
    input_filename = "day_{}_in.txt".format(day)
    lines = read_all_lines_no_strip(os.path.join("inputs", input_filename))
    if len(lines) == 0:
        print("Day {} has no input - Skipping".format(day))
    else:
        # Part 1 =======================================================================================================
        print("=====================   PART 1   =========================")
        move_boxes_and_print_top(lines)
        # ==============================================================================================================
        # Part 2 =======================================================================================================
        print("=====================   PART 2   =========================")
        move_boxes_and_print_top(lines, lift_multi=True)
        print("==========================================================")

