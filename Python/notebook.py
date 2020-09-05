# -*- coding: cp1252 -*-
import time

def startUp():
    try:
        noteBook = open("notebook.txt","r")
        return noteBook
    except(IOError):
        noteBook = open("notebook.txt","w")
        print("No default notebook was found, created one.")
        return noteBook
    
def main():
    noteBook = startUp()
    statusCheck = True
    while statusCheck == True:
        print("Now using file",noteBook.name)
        print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Change the notebook\n(5) Quit")
        userCmd = int(input("Please select one: "))
        if (userCmd == 1):
            noteBook.close()
            noteBook = open(noteBook.name,"r")
            nbCont = noteBook.readlines()
            for i in nbCont:
                print(i)
            noteBook.close()
        elif (userCmd == 2):
            noteBook.close()
            noteBook = open(noteBook.name,"a")
            lbAdd = ("\n")
            textAdd = input("Write a new note: ")
            noteBook.write(textAdd)
            noteBook.write(":::")
            noteBook.write(time.strftime("%X %x"))
            noteBook.write(lbAdd)               
            noteBook.close()
        elif (userCmd == 3):
            noteBook = open(noteBook.name,"w")
            noteBook.close()
            print("Notes deleted.")
        elif (userCmd == 4):
            noteBook.close()
            newInput = input("Give the name of the new file: ")
            try:
                noteBook = open(newInput,"r")
                
            except(IOError):
                noteBook = open(newInput,"w")
                print("No notebook with that name detected, created one.")
                
        elif (userCmd == 5):
            statusCheck = False

    print("Notebook shutting down, thank you.")

if __name__ == "__main__":
    main()
