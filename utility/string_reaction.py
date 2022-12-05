from utility.utility import *


def fully_react(input_str):
    """
    fully 'react' a given string, removing like characters next to each other.
    Part of Advent of Code 2020
    :param input_str:
    :return:
    """
    line = input_str
    removals = True
    while removals:
        removals = False
        for idx, c_1 in enumerate(line[:-1]):
            c_2 = line[idx + 1]
            if (c_1 != c_2) and (c_1.lower() == c_2.lower()):
                # print("[{}/{}] Removing [{}|{}]".format(idx, len(line), c_1, c_2))
                line = remove_char_from_string_at_index(line, idx + 1)
                line = remove_char_from_string_at_index(line, idx)
                removals = True
                break
    return line
