# bmi.py
# This program calculates user's Body Mass Index (BMI)
# Author: Anja Antolkovic

# Place height here
height = input ("Enter height (in cm): ")

# Place weight here
weight = input ("Enter weight (in kg): ")

# Calculates BMI to a float
BMI1 = int(weight)/((int(height)/100)**2)

# Rounds BMI to two decimal places
BMI2 = round (BMI1,2)

# prints the BMI
print ("BMI is", BMI2)