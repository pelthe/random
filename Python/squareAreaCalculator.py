def square(width = float(1.0), height = float(1.0)):
    float(areaSize = width * height)
    return areaSize

def main():
    #there are no default values
    #giving empty value results in an error
    print("Square area calculator")
    valueOne = float(input("Give area width in meters (default 1m): "))
    valueTwo = float(input("Give area height in meters (default 1m): "))
    float(squareArea = square(valueOne, valueTwo))
    print("The square area size is: ",squareArea,"m2")

if __name__ == "__main__":
    main()
