# -*- coding: cp1252 -*-

import math

print("Calculator")
statusCheck = True
while statusCheck == True:
    numberOne = int(input("Give the first number: "))
    numberTwo = int(input("Give the second number: "))
    while statusCheck == True:
        print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)\n(7) Change numbers\n(8) Quit")
        print("Current numbers:",numberOne,numberTwo)
        calcSel = int(input("Please select something (1-6): "))
        if (calcSel == 1):
            result = numberOne + numberTwo
            print("The result is:",result)
        elif (calcSel == 2):
            result = numberOne - numberTwo
            print("The result is:",result)
        elif (calcSel == 3):
            result = numberOne * numberTwo
            print("The result is:",result)
        elif (calcSel == 4):
            result = numberOne / numberTwo
            print("The result is:",result)
        elif (calcSel == 5):
            result = math.sin(numberOne/numberTwo)
            print("The result is:",result)
        elif (calcSel == 6):
            result = math.cos(numberOne/numberTwo)
            print("The result is:",result)
        elif (calcSel == 7):
            break
        elif (calcSel == 8):
            statusCheck = False
print("Thank you!")
