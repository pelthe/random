# -*- coding: cp1252 -*-
import time

statusCheck = True
while statusCheck == True:
    print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit")
    userCmd = int(input("Please select one: "))
    if (userCmd == 1):
        noteBook = open("notebook.txt","r")
        nbCont = noteBook.readlines()
        for i in nbCont:
            print(i)
        noteBook.close()
    elif (userCmd == 2):
        noteBook = open("notebook.txt","a")
        lbAdd = ("\n")
        textAdd = input("Write a new note: ")
        noteBook.write(textAdd)
        noteBook.write(":::")
        noteBook.write(time.strftime("%X %x"))
        noteBook.write(lbAdd)               
        noteBook.close()
    elif (userCmd == 3):
        noteBook = open("notebook.txt","w")
        noteBook.close()
        print("Notes deleted.")
    elif (userCmd == 4):
        statusCheck = False

print("Notebook shutting down, thank you.")
