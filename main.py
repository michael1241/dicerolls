#! /usr/bin/env python3
from random import randint
import seaborn as sns
import matplotlib.pyplot as plt

def rollDice(num, d):
    return sum([randint(1,d) for _ in range(num)])

def generateData(rolls):
    data = {}
    for (num, d) in rolls:
        data[f"d{d}"] = [rollDice(num, d) for _ in range(100000)]
    return data

#dice 4 6 8 10 12 20 100 = LCM of 600
dice = [4, 6, 8, 12, 20, 100]
rolls = [(600//x, x) for x in dice]

data = generateData(rolls)
labels = [f"{num}d{d}" for (num, d) in rolls[::-1]]

sns.set_theme(style='dark', font_scale=1.25)
sns.displot(data, kind='kde', fill=True)
plt.legend(labels, loc='upper left', fontsize='x-large')

plt.show()
