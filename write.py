'''opening the file in write mode and writing hello world on the file'''
import os
def write(filename):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            print("Successfully opened " + filename)
            f.write("Hello world!!")
    except IOError:
        print("Errror opening "+ filename+ " in write mode")



if __name__ == "__main__":
    write("bob.txt")