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
