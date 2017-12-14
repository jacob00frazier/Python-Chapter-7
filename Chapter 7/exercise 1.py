# Jacob Frazier CH 7 EX 1

'''
Exercise 1: Write a program to read through a file and print
the contents of the file (line by line) all in upper case. Executing
the program will look as follows:

'''

textFile = open("mbox-short.txt")
opened = textFile.read()
uppercase = opened.upper()
print(uppercase)
