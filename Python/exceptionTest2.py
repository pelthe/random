# -*- coding: cp1252 -*-

def fileName():
    myName = input("Give the file name: ")
    return myName

def main():
    
    fileOne = fileName()
    try:
        myFile = open(fileOne,"r")
        bigString = myFile.read()
        bigString = int(bigString)
        result = 1000 / bigString
  
    except (IOError):
        print("There seems to be no file with that name.")

    except (TypeError, ValueError):
        print("The file contents were unsuitable.")

    except (Exception):
        print("There was a problem with the program.")

    else:
        print("The result was",result)

if __name__ == "__main__":
    main()
