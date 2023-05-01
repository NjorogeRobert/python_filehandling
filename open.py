'''we open a file in the default mode and creating a new file if does not exist'''
import os
def fileopen(filename):
    try:
        with open('bob.txt', "w", encoding="utf-8") as f:
            print("Successfully opened "+ filename)
    except IOError:
        print("Error opening " + filename)
    



if __name__ == "__main__":
    fileopen("bob.txt")
