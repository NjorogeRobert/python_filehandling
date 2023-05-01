'''The program prints the line one by one'''
import os
def print_all(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                print(line)
    except IOError:
        print("Error printing contents!! Closing File...")



if __name__ == "__main__":
    print_all("well.txt")
