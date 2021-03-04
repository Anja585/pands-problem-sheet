# secondstring.py
# This program asks a user to input a string and outputs every second letter in reverse order
# Source: https://stackoverflow.com/questions/48873854/python-printing-ever-other-letter-of-a-word
# Author: Anja Antolkovic

#creating empty string
secondString = str()
# place the string here
firstString = input("Please enter a sentence: ")
for i in range(0,len(firstString)): # checking the condition
  if i % 2 != 0: # there should be a remainder if we what to start from the last letter (index -1)
      secondString += firstString[i] # adding the character to an empty string
print(secondString[::-1]) # printing in reverse order




