'''Function to open file in read mode'''
import os
def read(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print("Successfully opened "+ filename)
            reading =f.read()
            print(reading)
    except IOError:
        print("Error opening "+ filename + " in read mode")




if __name__ == "__main__":
    read("well.txt")