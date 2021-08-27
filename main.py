"""
Fun implementation of Collatz Conjecture in Python
Data visualisation with pandas and matplotlib
"""


import random
from typing import DefaultDict
import pandas as pd
import matplotlib.pyplot as plt


NUM_TO_RENDER = 10
RANGE = [1, 10000]


def handle_even(n):
    return n / 2


def handle_odd(n):
    return 3 * n + 1


def gen_int(range=[1, 10000]):
    min = range[0]
    max = range[1]
    return random.randint(a=min, b=max)


val = DefaultDict()
while len(val.keys()) < NUM_TO_RENDER:
    dig = gen_int()
    started_with = dig
    print("Running: ", dig)
    if dig not in val.keys():
        val[dig] = []
    while True:
        if dig % 2 == 0:
            if dig == 2 or dig == 4:
                val[started_with].append(dig)
                break
            dig = handle_even(dig)
            val[started_with].append(dig)

        elif not dig % 2 == 0:
            if dig == 1:
                val[started_with].append(dig)
                break
            dig = handle_odd(dig)
            val[started_with].append(dig)

df = pd.DataFrame.from_dict(val, orient="index")
df = df.T
print(df)
df.plot(kind="line")
plt.show()
