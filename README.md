The following file explains how file is handled using python...
It gives the functions to use when:
1) Openining a file:(open.py)
    When opening a file we use the open() function
    syntax: f = open(file name, mode, encoding)
    or -> with open(filename, mode, encoding) as f:
            #do the necessary

2)After opening the file:(write.py, read.py, append.py)
you can either
-> read the file: this is done in read mode 'r'
-> write a file: in this mode you can create a new file if it does not exist but it overwrites the file that exists 'w'
-> append the file: In this mode it creates a new file if it does not exists but dpes not overwrite a file if it exists instead appends at the end of file.

while reading the file we use the file.read() function
while writing in the file or appending in the file we use file.write() function

3)Closing the file(close.py):
after opening a file we have to close the file afer operation. this is done through
close() function.
syntax: f.close()

4) Know where we are at the file(tell.py)
at times we would love to know at what line we are when dealing with a large file.
here we use the tell() function.
syntax: file.tell().... it gives the position you are at.

5) Return to sender(seek.py):
we would also want to go back to where the file starts or at the desired place.
in this case we use seek() function.
syntax: file.seek(index)
index: represents the position you want to be at.

6) Rename(rename.py):
at times you may want to rename your file...in this case we use the os module.
The os module has a function that is used to rename a file.
syntax: import os
os.rename("old file", "new filename")

7) DELETE(delete.py):
We might want to delete a file...in this case we still use the os module
syntax: import os
os.remove("file name")