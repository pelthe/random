def poweroftwo(number):
    result = pow(number, number
    return result
	
def main():
    userNumb = int(input("Give a number: "))
    calc1 = poweroftwo(userNumb)
    print("The result is ", calc1)
	
if __name__ == "__main__":
    main()
