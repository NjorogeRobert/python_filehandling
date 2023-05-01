'''A program that deletes a file'''
import os
def delete_file(filename):
    '''
    This program deletes the file.
    Args:
        filename: the file to be deleted
    '''
    try:
        os.remove(filename)
        print("Successfully deleted")
    except IOError:
        print("Error deleting file")
