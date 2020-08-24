def square(width, height):
    areaSize = width * height
    return areaSize

def main():
    #there are no default values
    #giving empty value results in an error
    print("Square area calculator")
    valueOne = float(input("Give area width in meters: "))
    valueTwo = float(input("Give area height in meters: "))
    squareArea = square(valueOne, valueTwo)
    print("The square area size is: ",squareArea,"m2")

if __name__ == "__main__":
    main()
