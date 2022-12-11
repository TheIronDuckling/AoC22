# Advent of Code 2022
# import os
import sys
import math
from utility.utility import *

from cProfile import Profile
# Day 11 - Monkey in the Middle
day = os.path.basename(__file__)[:-3].split("_")[1]


class MonkeyManager:
    def __init__(self, div_three=True):
        self.monkeys = []
        self.div_three = div_three
        self.common_denominator = None

    def perform_round(self):
        if self.common_denominator is None:
            self.common_denominator = 1
            for i in [m.test_value for m in self.monkeys]:
                self.common_denominator *= i
            print(self.common_denominator)
        for m in self.monkeys:
            assert isinstance(m, Monkey)
            m.take_turn()

    def get_all_inspection_counts(self):
        return [m.inspection_count for m in self.monkeys]

    def add_monkey(self, number, starting_items, operation, test,
                   true_target, false_target):
        assert number == len(self.monkeys)
        self.monkeys.append(Monkey(starting_items=starting_items,
                                   operation=operation,
                                   test=test,
                                   true_target=true_target,
                                   false_target=false_target,
                                   manager=self))

    def pass_item_to_monkey(self, item, target):
        self.monkeys[target].add_item(item)


class Monkey:
    def __init__(self, starting_items: list, operation, test,
                 true_target, false_target, manager: MonkeyManager):
        self.items = starting_items
        self.operation = operation
        self.test_value = test
        self.true_case = true_target
        self.false_case = false_target
        self.manager = manager
        self.inspection_count = 0

    def add_item(self, item):
        self.items.append(item)

    def take_turn(self):
        while len(self.items) > 0:
            i = self.items[0]
            i = self.inspect_item(i)
            self.resolve_item(i)
            self.items = self.items[1:]

    def perform_operation(self, old):
        return eval(" ".join(self.operation))

    def resolve_test(self, item):
        return item % self.test_value == 0

    def inspect_item(self, item):
        item = int(self.perform_operation(item))
        if self.manager.div_three:
            item = int(item // 3)
        else:
            item %= self.manager.common_denominator
        self.inspection_count += 1
        return item

    def resolve_item(self, item):
        if self.resolve_test(item):
            self.manager.pass_item_to_monkey(item, self.true_case)
        else:
            self.manager.pass_item_to_monkey(item, self.false_case)


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
        mm = MonkeyManager()
        mn = si = op = te = tr = fa = None
        for l in lines:
            if l.startswith("Monkey "):
                mn = int(l[-2])
            elif l.startswith("Starting items: "):
                si = [int(i) for i in l.split(":")[1].split(",")]
            elif l.startswith("Operation: "):
                op = l.split(":")[1].split()[-3:]
            elif l.startswith("Test: "):
                te = int(l.split(":")[1].split()[-1])
            elif l.startswith("If true: "):
                tr = int(l.split(":")[1].split()[-1])
            elif l.startswith("If false: "):
                fa = int(l.split(":")[1].split()[-1])
            elif l == "":
                assert None not in [mn, si, op, te, tr, fa], "Didnt get all the needed values"
                mm.add_monkey(number=mn,
                              starting_items=si,
                              operation=op,
                              test=te,
                              true_target=tr,
                              false_target=fa)
                mn = si = op = te = tr = fa = None
        assert None not in [mn, si, op, te, tr, fa], "Didnt get all the needed values"
        mm.add_monkey(number=mn,
                      starting_items=si,
                      operation=op,
                      test=te,
                      true_target=tr,
                      false_target=fa)
        for round in range(20):
            mm.perform_round()
            # print(f"ROUND {round+1} ====================================")
            # for i, m in enumerate(mm.monkeys):
            #     vals = ", ".join([str(k) for k in m.items])
            #     print(f"Monkey {i}: {vals}")

        totals = mm.get_all_inspection_counts()
        top_two = sorted(totals)[-2:]
        print(top_two[0] * top_two[1])
        # ==============================================================================================================
        # Part 2 =======================================================================================================
        print("=====================   PART 2   =========================")
        mm2 = MonkeyManager(div_three=False)
        mn2 = si2 = op2 = te2 = tr2 = fa2 = None
        for l in lines:
            if l.startswith("Monkey "):
                mn2 = int(l[-2])
            elif l.startswith("Starting items: "):
                si2 = [int(i) for i in l.split(":")[1].split(",")]
            elif l.startswith("Operation: "):
                op2 = l.split(":")[1].split()[-3:]
            elif l.startswith("Test: "):
                te2 = int(l.split(":")[1].split()[-1])
            elif l.startswith("If true: "):
                tr2 = int(l.split(":")[1].split()[-1])
            elif l.startswith("If false: "):
                fa2 = int(l.split(":")[1].split()[-1])
            elif l == "":
                assert None not in [mn2, si2, op2, te2, tr2, fa2], "Didnt get all the needed values"
                mm2.add_monkey(number=mn2,
                               starting_items=si2,
                               operation=op2,
                               test=te2,
                               true_target=tr2,
                               false_target=fa2)
                mn2 = si2 = op2 = te2 = tr2 = fa2 = None
        assert None not in [mn2, si2, op2, te2, tr2, fa2], "Didnt get all the needed values"
        mm2.add_monkey(number=mn2,
                       starting_items=si2,
                       operation=op2,
                       test=te2,
                       true_target=tr2,
                       false_target=fa2)
        for round2 in range(10000):
            mm2.perform_round()
            # print(f"ROUND {round2 + 1}")
            # for i, m in enumerate(mm2.monkeys):
            #     vals = ", ".join([str(k) for k in m.items])
            #     print(f"Monkey {i}: {vals}")

        totals2 = mm2.get_all_inspection_counts()
        top_two2 = sorted(totals2)[-2:]
        print(top_two2[0] * top_two2[1])
        # ==============================================================================================================
        print("==========================================================")

