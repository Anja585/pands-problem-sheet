# secondstring.py
# This program asks a user to input a string and outputs every second letter in reverse order
# Source: Jake VanderPlas, A Whirlwind tour of Python, page 33
# Author: Anja Antolkovic

firstString = input("Please enter a sentence: ") # place the string here
secondString = firstString[::-2] # -2 is a step size
print(secondString) # printing out the string

