print("Calculator")
statusCheck = True
while statusCheck == True:
    numberOne = int(input("Give the first number: "))
    numberTwo = int(input("Give the second number: "))
    while statusCheck == True:
        print("(1) +\n(2) -\n(3) *\n(4) /\n(5) Change numbers\n(6) Quit")
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
            break
        elif (calcSel == 6):
            statusCheck = False
print("Thank you!")
