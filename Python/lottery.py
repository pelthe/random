from random import choice, sample

my_list = []

for i in range(1,31):
    my_list.append(i)

print(my_list)

print(sample(my_list, 7))
