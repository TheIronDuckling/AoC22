# Advent of Code 2022
import os
import sys
import math
from utility.utility import *

# Day 7
day = os.path.basename(__file__)[:-3].split("_")[1]


class acfile:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class acdirectory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.basepath = "" if parent is None else f"{self.parent.basepath}/{self.name}"
        self.files = []
        self.dirs = {}

    def add_file(self, file):
        self.files.append(file)

    def add_dir(self, dir):
        nd = acdirectory(dir, self)
        self.dirs[nd.basepath] = nd

    def get_total_size(self):
        return sum([d.get_total_size() for d in self.dirs.values()]) + sum([f.size for f in self.files])

    def get_all_dir_sizes(self):
        own = {k: v.get_total_size() for k, v in self.dirs.items()}
        for v in self.dirs.values():
            sub = v.get_all_dir_sizes().items()
            for k, sv in sub:
                own[k] = sv
        return own


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
        command_key = "$"
        move_dir_key = "cd"
        back_dir_key = ".."
        list_dir_key = "ls"
        dir_identifier = "dir"
        top_dir = "/"
        print("=====================   PART 1   =========================")
        parent_dir = None
        current_dir = None
        #visited_dirs = []     # NOTE THAT THIS IS THE TRICK IN PART 1
        for l in lines:
            #print(l)
            sl = l.split()
            if sl[0] == command_key:
                # it is a command
                c = sl[1]
                if c == move_dir_key:
                    # changing dirs
                    dst = sl[2]
                    if parent_dir is None:
                        # first dir
                        parent_dir = acdirectory(top_dir, None)
                        current_dir = parent_dir
                    else:
                        if dst == back_dir_key:
                            #print("moving back a dir")
                            current_dir = current_dir.parent
                            #print(f"current dir is : {current_dir.name}")
                        else:
                            #assert dst not in visited_dirs     # NOTE THAT THIS IS THE TRICK IN PART 1
                            bp = f"{current_dir.basepath}/{dst}"     # NOTE THAT THIS IS THE TRICK IN PART 1
                            #visited_dirs.append(dst)     # NOTE THAT THIS IS THE TRICK IN PART 1
                            #print("moving down a dir")
                            current_dir = current_dir.dirs[bp]
                            #print(f"current dir is : {current_dir.name}")
                elif c == list_dir_key:
                    # listing dirs - dont need to do anything with this yet.
                    pass
            else:
                # not a command - at this stage, must be a list
                if sl[0] == dir_identifier:
                    # listing a dir
                    current_dir.add_dir(sl[1])
                elif sl[0].isnumeric():
                    # probably a file size
                    current_dir.add_file(acfile(sl[1], int(sl[0])))
        # get all with values less than 100000
        all_dirs = parent_dir.get_all_dir_sizes()
        all_dirs[top_dir] = parent_dir.get_total_size()

        above_100k = {d: s for d, s in all_dirs.items() if s <= 100000}
        total = sum([i for i in above_100k.values()])
        print(f"Total size of at most 100000 dirs: {total}")
        # ==============================================================================================================
        # Part 2 =======================================================================================================
        print("=====================   PART 2   =========================")
        total_space = 70000000
        required_space = 30000000
        available_space = total_space - parent_dir.get_total_size()
        required_to_free = required_space - available_space
        print(f"Total Used : {parent_dir.get_total_size()}")
        print(f"Total Aval : {available_space}")
        print(f"Total 2fre : {required_to_free}")
        # get smallest over the required size
        all_options = {d2: s2 for d2, s2 in all_dirs.items() if s2 >= required_to_free}
        print(all_options)
        min_key = min(all_options, key=all_options.get)
        min_size = all_options[min_key]
        print(f"Smallest single dir: {min_key} with size {min_size}")
        # ==============================================================================================================
        print("==========================================================")

