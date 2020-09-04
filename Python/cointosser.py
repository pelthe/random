# -*- coding: cp1252 -*-
import random

print("5 coin flips: ")
i = 0
while i <= 5:
    coinToss = random.randint(0,2)
    if coinToss == 0:
        print("Tails!")
        i += 1

    else:
        print("Heads!")
        i += 1
