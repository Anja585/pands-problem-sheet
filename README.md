# pands-problem-sheet 
## Weekly tasks for Programming and Scripting module 2021
## Anja Antolkovic
# Introduction
This README file contains the explanations of the source codes with references to the weekly assignments for the Programming and Scripting module as a part of the Higher Diploma in Computing (Data Analytics) at GMIT. 
# Weekly Task 2
*Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py.The inputs are the person's height in centimetres and weight in kilograms. The output  is their weight divided by their height in metres squared.*
### Solution
```height = input ("Enter height (in cm): ") # Place height here
weight = input ("Enter weight (in kg): ") # Place weight here
BMI1 = int(weight)/((int(height)/100)**2) # Calculates BMI to a float
BMI2 = round (BMI1,2) # Rounds BMI to two decimal places
print ("BMI is", BMI2) # prints the BMI
```
Program asks the user to enter height and weight. Program then converts the data into an integers and performs the arithemtic operatins to get BMI. Function round() is used to round the result to 2 decimal places.  
### References
1. BMI Calculator, Available at: https://www.calculator.net/bmi-calculator.html (Accessed: 8th February 2021).
2. Python round() Function, Available at: https://www.w3schools.com/python/ref_func_round.asp#:~:text=The%20round()%20function%20returns,will%20return%20the%20nearest%20integer. (Accessed: 8th February 2021).
3. Jake VanderPlas (2016) A Whirlwind tour of Python, First Edition edn., Sebastopol, CA: O'Reilly.
# Weekly Task 3
*Write a program that takes asks a user to input a string and outputs every second letter in reverse order.*
### Solution
```firstString = input("Please enter a sentence: ") # place the string here
secondString = firstString[::-2] # -2 is a step size
print(secondString) # printing out the string
```
Program asks the user to enter a sentence. Program reverses the letters in a string and prints out every second letter; 'firstString[::-2]' is equivalent to 'firstString[0:len(firstString):-2]' where '2' denotes step size and '-' reverse order.  
### References
1. Jake VanderPlas (2016) A Whirlwind tour of Python, First Edition edn., Sebastopol, CA: O'Reilly.
2. Python - Slicing Strings, Available at: https://www.w3schools.com/python/python_strings_slicing.asp (Accessed: 4th March 2021).
3. Python Strings, Available at: https://www.w3schools.com/python/python_strings.asp (Accessed: 4th March 2021).
# Weekly Task 4
*Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.*
### Solution
```numbers = [] # creating an empty list to add the numbers to
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
```
Program asks the user to enter positive integer number. While loop is used to perform the calcutations on the number as follows:
 * number is added to an empty list;
 * if statement is used to break the loop if the number is equal to 1 (if user enters 1, number is added to the list and while loop broken);
 * if statement is used to divide the number by 2 if the number is even;
 * else statement is used to multiply the number by 3 and add 1 if the number is odd;
 * condition is changed by assiging the number a new current value. 
 ### References
 1. Jake VanderPlas (2016) A Whirlwind tour of Python, First Edition edn., Sebastopol, CA: O'Reilly.
 2. Python While Loops, Available at: https://www.w3schools.com/python/python_while_loops.asp (Accessed: 13th March 2021)
 3. Python For Loops, Available at: https://www.w3schools.com/python/python_for_loops.asp (Accessed: 13th March 2021).
 4. Making a collatz program automate the boring stuff, Available at: https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff (Accessed: 13th March 2021).
 # Weekly Task 5
 *Write a program that outputs whether or not today is a weekday.*
 ```
import datetime # importing datetime module to work with dates
todayDate = datetime.datetime.now() # finding today's date
todayDay = int(todayDate.strftime("%w")) # using a method to format the date into a number 
if todayDay in range(1,6): # checking the condition
    print("Yes, unfortunately today is a weekday") # returing the statement if it's a weekday
else: print("It is the weekend, yay!") # returning a statement if it weekend
```
This program prints out if today is a weekday or a weekend. Datetime module is used to find today's date and strftime() method to format today's day into a number (number 0-6, where 0 is Sunday). If statement checks if the todayDay (now formated into a number) falls into the range of numbers 1-5 which denote weekdays.  
 ### References
 1. Python Datetime, Available at: https://www.w3schools.com/python/python_datetime.asp (Accessed: 14th March 2021).
 2. How do I get the day of week given a date?, Available at: https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date (Accessed: 14th March 2021).
 # Weekly Task 6
 *Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.*
 ```
 # defining the function 
def doSqrt(num):
    estimate = 1.0 # inital assumption of the square root  
    tolerance = 0.000001 # defining how much estimate can deviate from the real result  
    while True: # we assume estimate and tolerance are true
        estimate = (num/estimate + estimate)/2 # changing the condition variable using the Newton's square root equation
        difference = abs(num - estimate**2) # returning the absolute value
        if difference <= tolerance: # checking the condition
            break # come out of the loop if condition is true
    return round(estimate, 1) # round to one decimal place

# main program:
num = float(input("Please enter a positive number: ")) # enter number here
if num > 0: # checking the condition
    print("The square root of {} is approx. {}.".format(num, doSqrt(num)))
```
Program asks the user to enter a positive number. Entered number is an argument in a function 'doSqrt' which calculates square root of the number:
* we make an inital assumption of square root value, and we define the tolerance value (the value by which the real square root can deviate from the one calculated by a function);
* Newton's iteration algorithm is used in a while loop to compute square root via recurrence equation √ N ≈ (N/A + A)/2. While loop is broked once if statement is true;
* the solution is rounded to 1 decimal place.
### References
1. Newton's Square Root Approximation, Available at: https://www.school-for-champions.com/algebra/square_root_approx.htm#.YHXJquhKjIX (Accessed: 30th March 2021).
2. Newton's Iteration, Available at: https://mathworld.wolfram.com/NewtonsIteration.html (Accessed: 30th March 2021).
3. Newton's method for approximating square roots, Available at: https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots (Accessed: 30th March 2021).
# Weekly Task 7
*Write a program that reads in a text file and outputs the number of e's it contains.
The program should take the filename from an argument on the command line.*
```
# importing module to interact with the commant line
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
```
This program counts the number of 'e' letters in Moby-Dick. Letter 'e' is placed as an argument in a function 'countLetter' once called. sys.argv() is an array for command line arguments in Python where file called has an index 0. Function takes a second argument (index 1) into account, in this case Moby-Dick text file. Program opens the text file in a read mode, count and returns the number of 'e' letters. 
### References
1. Python String count() Method, Available at: https://www.w3schools.com/python/ref_string_count.asp (Accessed: 4th April 2021).
2. Python Command Line Arguments, Available at: https://realpython.com/python-command-line-arguments/ (Accessed: 4th April 2021).
3. How to use sys.argv in Python, Available at: https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/ (Accessed: 4th April 2021).
# Weekly Task 8
*Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.*


### References
1. NumPy Array Indexing, Available at: https://www.w3schools.com/python/numpy/numpy_array_indexing.asp (Accessed: 10th April 2021).
2. NumPy Creating Arrays, Available at: https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp (Accessed: 10th April 2021).
3. Matplotlib Plotting, Available at: https://www.w3schools.com/python/matplotlib_plotting.asp (Accessed: 10th April 2021).
4. Matplotlib Line, Available at: https://www.w3schools.com/python/matplotlib_line.asp (Accessed: 10th April 2021).
5. Matplotlib Labels and Title, Available at: https://www.w3schools.com/python/matplotlib_labels.asp (Accessed: 10th April 2021).
