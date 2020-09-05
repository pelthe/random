# -*- coding: cp1252 -*-

def getNumber():
    myNumber = input("Give a number: ")
    return myNumber

def main():
    
    numberOne = getNumber()
    try:
        number = int(numberOne)
  
    except (TypeError, ValueError):
        print("The input was malformed.")

    else:
        print("The input was suitable!")

if __name__ == "__main__":
    main()
