 # collatz.py
# This program asks the user to input any positive integer and outputs the successive values as follows:
  # 1. at each step calculates the next value by taking the current value
  # 2. if the number it is even, divides it by two
  # 3. if the number it is odd, multiplies it by three and adds one
  # 4. the program ends if the current value is one.
# Author: Anja Antolkovic

numbers = [] # creating an empty list to add the numbers to
number = int(input("Please enter a positive integer: "))
while number >= 1: # only work with integer numbers larger or equal to 1
   numbers.append(number) # adding number to the empty list
   if number == 1: # the program ends if the number is 1
         break
   if number % 2 == 0: # criteria for the evenness
      currentNumber = int(number / 2) # defining current value if the number was even 
   else: currentNumber = int(number * 3 + 1) # defining current value if the number was odd
   number = currentNumber # number changes its condition to current value
   
print(*numbers) # unpacking numbers from the list

