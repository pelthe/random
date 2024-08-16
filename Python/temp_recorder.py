from pprint import pprint
import random


def matrix_random_number(n_filas, n_columnas, num_decimals=1):
    array = [[0 for _ in range(n_filas)] for _ in range(n_columnas)]

    for j in range(n_columnas):
        for i in range(n_filas):
            array[j][i] = round(random.uniform(10.0,30.0),1)
    return array

temps = matrix_random_number(12, 31)
pprint(temps)

# Next find average temp at noon, turn this to def()
total = 0.0
 
for day in temps:
    total += day[11]
 
average = round(total / 31, 1)
 
print("Average temperature at noon:", average)

# Find the highest temperature over 31 days, turn this to def()
highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("The highest temperature was:", highest)

# Find days when at noon the temp was over 20 C, turn this to def()
hot_days = 0
 
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
 
print(hot_days, "days were hot.")
