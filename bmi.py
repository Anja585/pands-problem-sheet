# This program calculates user's Body Mass Index (BMI)
# Author: Anja Antolkovic

height = input ("Enter height (in cm): ") # Place height here
weight = input ("Enter weight (in kg): ") # Place weight here
BMI1 = int(weight)/((int(height)/100)**2) # Calculates BMI to a float
BMI2 = round (BMI1,2) # Rounds BMI to two decimal places
print ("BMI is", BMI2) # prints the BMI