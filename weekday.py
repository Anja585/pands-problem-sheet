# weekday.py
# This program outputs whether or not today is a weekday
# Source: 1. https://www.w3schools.com/python/python_datetime.asp
#         2. https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date           
# Author: Anja Antolkovic

import datetime # importing datetime module to work with dates
todayDate = datetime.datetime.now() # finding today's date
todayDay = int(todayDate.strftime("%w")) # using a method to format the date into a number 
if todayDay in range(1,6): # checking the condition
    print("Yes, unfortunately today is a weekday") # returing the statement if it's a weekday
else: print("It is the weekend, yay!") # returning a statement if it weekend



