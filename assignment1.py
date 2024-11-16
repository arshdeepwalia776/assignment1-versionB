#!/usr/bin/env python3

'''
OPS445 Assignment 1 
Program: assignment1.py 
The python code in this file is original work written by
"Arshdeep Walia". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Author: Arshdeep Walia
Semester: Fall 2024
Descriptiion: this script prints future and past dates.The script will divide a typical year by a given value.
'''

import sys

def leap_year(year: int) -> bool:
    """This funct checks whethers a given year is a leap year and returns True if the year is a leap year, otherwise False."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) # check the year given year is divisible by 4 but not by 100 or is divisible by 400


def mon_max(month:int, year:int) -> int:
    " this funtion gives the maximum day for a given month, for a given year "
    if month == 2:  #this checks if the given month is February and gives the result accordingly
        return 29 if leap_year(year) else 28
    elif month in {4, 6, 9, 11}:  # this will check for the months with 30 days
        return 30
    return 31  # it will return 31 as all the remaining months have 31 days



def after(date: str) -> str: 
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function has been tested to work for year after 1582
    '''
    year, mon, day = (int(x) for x in date.split('-')) # this will split day,month and year of the date to integers
    day += 1  # Move to the next day by adding 1 to it

    #this will check if day exceeds the max days in the given month
    if day > mon_max(mon, year):
        day = 1
        mon += 1  # it will increase the month by 1 and move to the next month
        if mon > 12:  # If month exceeds December, reset to January of the next year
            mon = 1
            year += 1 #this increases the year by 1 

# this gives the date in YYYY-MM-DD format 
    return f"{year}-{mon:02}-{day:02}"
def before(date: str) -> str:
    """Returns previous day's date in YYYY-MM-DD format.

    before() -> date for previous day in YYYY-MM-DD string format

    Return the date for the previous day of the given date in YYYY-MM-DD format.
    """
    # this will split the date into year, month, and day and give them as integers 
    year, mon, day = (int(x) for x in date.split('-'))
    
    # Move to the previous day 
    day -= 1
    
    # it wil check if day goes below 1 
    if day < 1:
        # Move to the previous month by subtracting 1
        mon -= 1
        
        # If the month goes below January, it reset to December of the previous year
        if mon < 1:
            mon = 12 #reset the month to december
            year -= 1 # subtractting 1 from year to move to the previous year
        
        # this dictionary has info regarding the maximum days in each month,has 28 days for feb
        mon_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        
        # Checking if the new month is February in a leap year
        if mon == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            day = 29 # make the days 29 for feburary in leap year 
        else:
            day = mon_dict[mon] # have 28 days as in dictionary
    
    # Return the date in YYYY-MM-DD format
    return f"{year}-{mon:02}-{day:02}"

def usage():
    "This function Prints a usage message to the user and exits the program"

    print("Usage: " + str(sys.argv[0]) + " YYYY-MM-DD divisor") #this prints the usage message along with daete in yyyy-mm-dd format
    sys.exit() # exit the system

def valid_date(date: str) -> bool:
    """Check if the date is valid in YYYY-MM-DD format."""
    try:
        #this splits the  year, month, and day for the given date and converts it into integer
        year, mon, day = (int(x) for x in date.split('-'))
        
        # this checks the date by checking that year is a 4-digit number, month is between 1 and 12, and day is valid for the month
        if not (1000 <= year <= 9999): #range for the years
            return False
        
        #This gets the maximum day for the month and year
        max_day = mon_max(mon, year)
        
        #This is a debugging statement to observe values
        print(f"Debug: Year={year}, Month={mon}, Day={day}, Max Day for Month={max_day}")
        
        # Checking if the month and day are within valid ranges
        is_valid = 1 <= mon <= 12 and 1 <= day <= max_day
        print(f"Debug: Valid Date Check={is_valid}") #it is a debugging statement for validation
        return is_valid
    except ValueError:
        # if an error occurs , it return False
        return False


def dbda(start_date: str, step: int) -> str:
    """Given a start date and a number of days into the past/future, return the calculated date."""
    
    # this initializes the date with the start date
    date = start_date

    # this loops to move forward or backward by the number of days specified by step
    for _ in range(abs(step)):
        # Call after() if step is positive (to move forward), or before() if step is negative (to move backward)
        date = after(date) if step > 0 else before(date)
    
    # Return the final calculated date in YYYY-MM-DD format
    return date


if __name__ == "__main__":

""" This calculates and displays past and future dates based on a start date and divisor which is provided as a command lin argument"""

    # this checks that the command line arguments  are not equal to 3
    if len(sys.argv) != 3:
        usage() #prints the usage message

# this gets the start date from the command line argument provided
    start_date = sys.argv[1]
    try:
# converts the divisor argument to integer
        divisor = int(sys.argv[2])
        if divisor == 0: # this checks that dividsor should not be 0 and prints error message if 0  
            print("Error: Divisor cannot be zero.")
            usage()
    except ValueError:
        usage() # calls usage if divisor is not a valid integer

    # this checks that start date format is valid
    if not valid_date(start_date):
        print("Error: Invalid date format.") #print errir message if not valid
        usage()

    # this calculates the number of days to add/subtract
    days = round(365 / divisor)

    # Get the dates
    past_date = dbda(start_date, -days)
    future_date = dbda(start_date, days)

    # this prints output of the results
    print(f"A year divided by {divisor} is {days} days.")
    print(f"The date {days} days ago was {past_date}.")
    print(f"The date {days} from now will be {future_date}.")

