# weekday.py
# This program outputs whether or not today is a weekday
# Source: 1. https://www.w3schools.com/python/python_datetime.asp
#         2. https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date           
# Author: Anja Antolkovic

import datetime # importing datetime module to work with dates

todayDate = datetime.datetime.now() # finding today's date
todayDay = todayDate.strftime("%A") # using a method to format the date into a full version string 
if todayDay == "Saturday" or "Sunday": # checking the condition
    print("It is the weekend, yay!") # returing the statement if it's a weekend
else: print("Yes, unfortunately today is a weekday") # returning a statement if it weekday

