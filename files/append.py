'''A program that appends a file and creates new file if file does not exist'''
import os
def appending(filename):
    try:
        with open(filename, "a", encoding="utf-8") as f:
            print("Successfully openned "+ filename +"in append mode")
            f.write("Finally")
    except IOError:
        print("Error opening " +filename+ "in append mode")



if __name__ == "__main__":
    appending("bob.txt")