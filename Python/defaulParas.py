def tester(givenstring = "Too short"):
    dimension = len(givenstring)
    if givenstring != "quit":
        if dimension < 9:
            tester()
            return
            
        elif dimension >= 9:
            stringX = "X"
            if stringX in givenstring == True:
                print("X spotted!")
                main()
                
            elif stringX in givenstring == False:
                print(givenstring)
                main()
                  
    elif givenstring == "quit":
        return

    return
                                     
def main():
    userInput = str(input("Write something (quit ends): "))
    tester(userInput)

if __name__ == "__main__":
    main()
