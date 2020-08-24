def tester(givenstring = "Too short."):
    dimension = len(givenstring)
    #statusChk = True
    while True:
        if givenstring == "Quit":
            False
            return
            
        elif dimension < 10:
            tester()
            
        else:
            print(givenstring)
                         
def main():
    userInput = str(input("Write something (quit ends): "))
    tester(userInput)
    
if __name__ == "__main__":
    main()
