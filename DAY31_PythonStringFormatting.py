
# Python String Formatting 

# F - strings 

# Example : Create an f-string:
txt = f"The price is 49 dollars."
print(txt)



# Placeholders and modifiers - to format values in an f-string, add placeholders{}, a placeholder can contain variables,
# operators, functions and modifiers to format the values.


# Example: Add a placeholder for the price variable:
price = 49
txt = f"The price is {price} dollars."
print(txt)


# Example : Display the price with 2 decimals:

price = 59
txt = f"The prics is {price:.2f} dollars."
print(txt)  # Output : The price is 59.00 dollars.



# Perform Operations in F - strings.

# Example: Perform a math operation in the placeholders and return the result.

txt = f"The price is {20 * 39} dollars."
print(txt)  # Output : The price is 780 dollars.


# Example: Add taxes before displaying the price.

price = 59
tax = 0.25
txt = f"the price is {price * tax} dollars."
print(txt)  # Output : the price is 14.75 dollars.


# You can if...else statements insdie the placeholders.
# Return "Expensive" if the price is over 50, otherwise return "Cheap:
price = 49
txt  = f"It is very {"Expensive" if price > 50 else "cheap"}."

print(txt)



# Execute Functions in F - strings.

# Example: use the string method upper() to convert a value into upper case letters.
fruit = "apples"

txt = f"I love {fruit.upper()}."
print(txt)  # Output : I love APPLES.



# Create a function that converts feet into meters.

def myconverter(x):
    return x * 0.3048

txt = f"the plane is flying at a {myconverter(30000)} meter altitude."
print(txt)  # Output : the plane is flying at a 9144.0 meters altitude.



# String format()

# Example: add a placehoder where you want to display the price.
price = 50
txt = "the price is {} dollars."

print(txt.format(price))


# Format the price to be displayed as a number with two decimals.

txt = "the price is {:.2f} dollars."
print(txt.format(price))





# Multiple Values - 

quantity = 8
itemno = 567
price = 49.95

myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity,itemno,price))




# Index Numbers 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity,itemno,price))



# Named Indexes.
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "ford", model = "Mustang" ))