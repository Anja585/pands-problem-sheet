# squareroot.py
# Source: https://www.school-for-champions.com/algebra/square_root_approx.htm#.YGM0hq9KjIW
#         https://mathworld.wolfram.com/NewtonsIteration.html
#         https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots
# This program takes a positive floating-point number as input and outputs an approximation of its square root
# Author: Anja Antolkovic

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


