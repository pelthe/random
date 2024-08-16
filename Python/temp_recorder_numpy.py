# Temperature record, going for hourly data for 31 days.

# temps = [[0.0 for h in range(24)] for d in range(31)] # h = hour, d = day

temps = numpy.random.uniform(low=10, high=25, size=(31,24) )


# Next find average temp at noon, turn this to def()
total = 0.0
 
for day in temps:
    total += day[11]
 
average = total / 31
 
print("Average temperature at noon:", average)

# Find the highest temperature over 31 days, turn this to def()
highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("The highest temperature was:", highest)

# Find days when at noon the temp was at least 20 C, turn this to def()
hot_days = 0
 
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
 
print(hot_days, "days were hot.")
