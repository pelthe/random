# -*- coding: cp1252 -*-

import math

def userInput():
    while True:
        try:
            userNumber = input("Give a number: ")
            userNumber = int(userNumber)
            return userNumber
        
        except(TypeError,ValueError):
            print("This input is invalid.")        

def main():

    print("Calculator")
    statusCheck = True
    while statusCheck == True:
        numberOne = userInput()
        numberTwo = userInput()
        while statusCheck == True:
            print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)\n(7) Change numbers\n(8) Quit")
            print("Current numbers:",numberOne,numberTwo)
            calcSel = int(input("Please select something (1-8): "))
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

if __name__ == "__main__":
    main()
