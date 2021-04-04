# es.py
# This program read in a text file and outputs the number od e's it contains
# The program takes the filename from an argument on the command line 
# Source: https://www.w3schools.com/python/ref_string_count.asp   
#         https://realpython.com/python-command-line-arguments/
#         https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/     
# Author: Anja Antolkovic

# importing module to interact with the 
import sys

# defining the function
def countLetter(x): # passing letter x in the file as an argument  
    filename = sys.argv[1] # file is a second argument from the command line, first is source code itself
    with open(filename, "rt") as f: # open file for a reading in text mode
        text = f.read() # defining a text file
    countX = text.count(x) # count the numbers of letters from a text file                       
    return countX # return the number of counts
    
count = countLetter("e")
print(count) # print the number of counts