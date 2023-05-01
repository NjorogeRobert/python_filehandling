'''A program that returns the file cursor to a certain position'''
def seeking(filename):
    '''
    This program returns the file cursor to the first index.
    args:
        filename: name of file
    '''
    with open(filename, "r", encoding="utf-8") as f:
        f.seek(0)