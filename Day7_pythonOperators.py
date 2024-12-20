
# Python Operators

# Python Arithmetic Operators
x = 5
y = 10
print(x + y)    # Output : 15 - Addition

print(x - y) # Output : -5 - Subtraction

print(x * y) # Output : 50 - Multiplication

print(x / y) # Output : 0.5 - Division

print(x % y) # Output : 5 - Modulus

print(x ** y) # Output :9765625 - Exponentiation

print(x // y) # Output : 0 - Floor Division




# Python Assignment Operators

q = 10
print(q) # Output : 10 - Assignment

q += 5
print(q) # Output : 15 - Addition Assignment

q -= 5
print(q) # Output : 10 - Subtraction Assignment

q *= 5
print(q) # Output : 50 - Multiplication Assignment

q /= 5
print(q) # Output : 10.0 - Division Assignment



# Python Comparison Operators : Comparison Operators are used to compare two values

a = 3
b = 7

print(a == b) # Output :False - Equal Comparison

print(a != b) # Output :True - Not Equal Comparison

print(a > b) # Output :False - Greater Comparison

print(a < b) # Output : True - Less Comparison

print(a >= b) # Output : False - Greater or Equal Comparison

print(a <= b) # Output : True - Less or Equal Comparison



# Python Logical Operators

print(a < 5 and b < 10)  # Output : True - And Operator

print(a < 5 or b < 10)  # Output : True - Or Operator

print(not (a < 5 and b < 10))  # Output : False - Not Operator



# Python Identity Operator

b = ["apple", ' banana']
x = ["apple", "banana"]
z = b

print(b is z)

# return True because z is the same object as b

print(b is x) 
# Return False because b is no the same object as x, even if they have the same content

print(b == x)
# to demonstrate the difference between "is" and "==" : this comparison returns True because x is equal to y
