# update this each day
from bits.day_1 import run as d1
from bits.day_2 import run as d2
from bits.day_3 import run as d3
from bits.day_4 import run as d4
from bits.day_5 import run as d5
from bits.day_6 import run as d6
from bits.day_7 import run as d7
from bits.day_8 import run as d8
from bits.day_9 import run as d9
from bits.day_10 import run as d10
from bits.day_11 import run as d11
from bits.day_12 import run as d12
from bits.day_13 import run as d13
from bits.day_14 import run as d14
from bits.day_15 import run as d15
from bits.day_16 import run as d16
from bits.day_17 import run as d17
from bits.day_18 import run as d18
from bits.day_19 import run as d19
from bits.day_20 import run as d20
from bits.day_21 import run as d21
from bits.day_22 import run as d22
from bits.day_23 import run as d23
from bits.day_24 import run as d24
from bits.day_25 import run as d25

import sys
from typing import final
from datetime import datetime


def pick_day(sd=None):
    days = [None,
            d1, d2, d3, d4, d5,
            d6, d7, d8, d9, d10,
            d11, d12, d13, d14, d15,
            d16, d17, d18, d19, d20,
            d21, d22, d23, d24, d25]
    if sd is None:
        current_day = datetime.now().day
        current_hour = datetime.now().hour
        if current_hour < 16:
            return days[current_day - 1]
        else:
            return days[current_day]
    else:
        return days[sd]


if __name__ == "__main__":
    specific_day = None
    pick_day(specific_day)()
