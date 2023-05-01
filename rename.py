'''A program that renames a file'''
import os
def rename(filename, new_filename):
    '''
    A function that renames a file
    args:
        filename: the old name to the file
        new_filename: New file name to file
    
    Returns:
        new_filename(str)
    except:
        returns IOError if the renaming of file is not successfull
    '''
    try:
        os.rename(filename, new_filename)
        print("successfully renamed to "+ new_filename)
    except IOError:
        print("Error renaming " +filename)


if __name__ == "__main__":
    rename("bob.txt", "well.txt")