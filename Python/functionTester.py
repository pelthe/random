# -*- coding: UTF8 -*-

import re

def tester():
    defaultValue = "Too short"
    while True:
        userInput = str(input("Write something (quit ends): "))
        if userInput != "quit":
            try:
                
                dimension = len(userInput)
                if dimension < 10:
                    print(defaultValue)
                elif dimension >= 10:
                    xSearch = re.search('[xX]',userInput)
                    if xSearch:
                        print(userInput)
                        print("X spotted!")
                    else:
                        print(userInput)
            except(Exception):
                break
        else:
            break
                                     
def main():
    
    testWord = tester()

if __name__ == "__main__":
    main()
