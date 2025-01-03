
# Python Scope: A variable is only available from inside the region it is created. This is called Scope.

# Local Scope: A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myFunct():
    x = 300
    print(x)

myFunct()



# Function inside Function 

# Example: the local variable can be accessed from a function within a function:

def myfunc():
    x = 89
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()




# Global Scope:

# Example: A variable created outside of a function is global and can be used by anyone.

x = 300

def myfunc():
    print(x)
myfunc()

print(x)


# Naming Variables:

# Example: The function will print the local z and then the code will print the global z:

z = 34

def myfnc():
    z = 600
    print(f"The inside varaible is {z}")

myfunc()
          
print(z)



# Global keyword - if you need to create a global variable but are stuck in the lcoal scope, you can use the global keyword.


def myfunc():
    global a
    a = 89
myfunc()
print(a)



# Nonlocal Keyword = is used to work with variables inside nested functions.

def myfunc():
    x = "Jane Doe"
    def myfunc2():
        nonlocal x
        x = "Alice"
        print("Inside myfunc2 : ", x)
        myfunc2()
        return x

print(myfunc())