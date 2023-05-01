'''The program prints the Number of lines'''
import os
def print_line(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            count = 0
            for line in f:
                count += 1
            print(f"The Number of lines are = {count}")
    except IOError:
        print("Error printing contents!! Closing File...")



if __name__ == "__main__":
    print_line("bob.txt")