'''A program tha closses a file'''
import os
def close():
    try:
        filename = open("filename.txt","w")
        filename.close()
        print("Successfully closed  file")
    except IOError:
        print("Error closing file")





if __name__ == "__main__":
   close()