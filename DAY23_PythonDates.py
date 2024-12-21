
# Python Dates - we can import a module named datetime to work with dates as date objects.


# Example: Import the datetime module and display the current date.
import datetime

x = datetime.datetime.now()

print(x)



# example: Return the year and name of weekday

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))




# Creating Date Objects: we can use datetime() class(constructor) of the datetime module.

import datetime
x = datetime.datetime(2020, 4, 23)

print(x)
