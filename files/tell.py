'''a program that gives the location of the file'''
import os
def tell(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            number = f.tell()
            print(number)

    except IOError:
        print("Could not tell" + filename)



if __name__ == "__main__":
    tell("well.txt")