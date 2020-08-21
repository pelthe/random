print("Calculator")
numberOne = input("Give the first number: ")
numberOne = int(numberOne)
numberTwo = input("Give the second number: ")
numberTwo = int(numberTwo)
print("(1) +\n(2) -\n(3) *\n(4) /")
calcSel = input("Please select something (1-4): ")
calcSel = int(calcSel)
if (calcSel == 1):
    result = numberOne + numberTwo
    print(result)
elif (calcSel == 2):
    result = numberOne - numberTwo
    print(result)
elif (calcSel == 3):
    result = numberOne * numberTwo
    print(result)
elif (calcSel == 4):
    result = numberOne / numberTwo
    print(result)
else:
    print("Selection was not correct.")
