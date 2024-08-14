number = int(input("Give a number: "))

steps = 0

while number > 0:
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            steps += 1
        elif number % 2 != 0:
            number = 3 * number + 1
            steps += 1
        print(number)
    else:
        print("Steps: ", steps)
        break
