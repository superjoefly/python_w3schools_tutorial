"""
Just doing some testing and refreshing Python skills
"""

import random


# Define the main function:
def main():

    """This is a function docstring...

    """

    # Check if you have python installed (in terminal):
    # python --version









    # Python can be directly executed in a terminal or by executing
    # a .py file (like this file) using the terminal:

    # c:\Users\Your Name>python3 hello_world.py

    # Print Statement:
    print("Hello World!")

    # To execute python directly in a terminal, open a terminal and type
    # python3

    # Then, type the python code directly:
    # print("Hello World!")

    # To exit terminal press ctrl + d or type exit()








    # INDENTATION:

    if 5 > 2:
        print("Five is greater than two...")

    # Python will give you an error if you skip the indentation.

    # The number of spaces used for indentation is up to the programmer
    # but generally 2 - 4 spaces are used.

    # The same number of spaces must be used within an individual block of code
    # otherwise you'll get an error.








    # VARIABLES:

    # Python variables are created during assignment:

    # Create a variable and display its value:
    x = 5
    print(x)

    name = "Joey"
    print(name)








    # COMMENTS:

    # Python comments start with a # and are used for in-code documentation,
    # to make code more readable and to prevent the execution of code

    # This is a comment

    # The following code is "commented out" to prevent execution:
    # print("Nothing")

    print("After-line comment") # This is an after-line comment

    ###########################

    # Multi-line Comments:

    # Multiple lines of comments can be created with multiple
    # hash symbols like this one, or we can use triple quotes
    # like so:

    """
    This is an
    example of a
    multiple-line comment...
    """










    # VARIABLES:

    # Variables are containers for storing data values:

    # Variables are created during assignment like so:

    # Declare and initialize a variable with the value of 7:
    x = 7

    # Display the value of the variable:
    print(x)

    # Create a variable with a value of "Atwood":
    last_name = "Atwood"

    # Display the value of the variable:
    print(last_name)


    ######################


    # Variables do not need to be declared with any particular type, and
    # the type can be changed after it has been set:

    age = 7 # "age" is of type int (integer)
    print(type(age))

    # Change the type of the variable
    age = "Seven" # "age" is now of type str (string)
    print(type(age))


    ######################


    # TYPE CASTING:

    # Type casting can be used to specify the data type for a variable:

    my_string = str(3)
    print(type(my_string)) # my_string is of type 'string'

    my_integer = int(3)
    print(type(my_integer)) # my_integer is of type 'integer'

    my_float = float(3)
    print(type(my_float))   # my_float is of type 'float'


    ######################


    # String variables can be declared using SINGLE or DOUBLE quotes:

    first_name = "Joey"
    # is the same as
    first_name = 'Joey'

    print(first_name)


    ######################


    # VARIABLE NAMES are CASE SENSITIVE:

    my_name = "Joey"
    # is not the same as
    My_Name = "James"

    print(my_name)  # Will display "Joey"
    print(My_Name)  # Will display "James"


    # Variable names can be long or short, but it's helpful for them to
    # be descriptive.


    ######################


    # RULES for PYTHON VARIABLE NAMES:

    # 1. variable names must start with a letter or underscore character
    # 2. a variable name cannot start with a number
    # 3. a variable name can only contain alpha-numeric characters and underscores
    # 4. variable names are case-sensitive



    # Variable names can be written in several ways to make them more
    # readable, but should generally follow the snake-case naming
    # convention like so:

    first_car = "Volkswagon"
    second_car = "Impalla"
    MY_NAME = "Joey" # This is a "constant" (will not change throughout program)

    print(first_car)
    print(second_car)
    print(MY_NAME)


    ######################


    # MANY VALUES to MULTIPLE VARIABLES (in one statement)

    # Python allows us to assign values to multiple variables in
    # one line; the number of variables MUST MATCH the number
    # of values:

    # Assign the variables:
    fruit_1, fruit_2, fruit_3 = "orange", "banana", "apple"

    # Display the values:
    print(fruit_1)
    print(fruit_2)
    print(fruit_3)


    ######################


    # ASSIGNING ONE VALUE to MULTIPLE VARIABLES:

    # We can assign the same value to multiple variables in on line:

    name = manager = badass = "Joey"

    # Display the values of each variable:

    print(name)
    print(manager)
    print(badass)


    ######################


    # COLLECTION UNPACKING

    # We can extract the values contained within a list, tuple, etc
    # into variables through a process called unpacking

    # Create a list of employees:
    employees = ["John", "James", "Jason"]

    # Unpack the list into variables:
    emp_1, emp_2, emp_3 = employees

    # Display the value of each variable:
    print(emp_1, emp_2, emp_3)


    ######################


    # OUTPUT VARIABLES

    # In Python we use the "print" statement to output variables.

    # We can use the "+" operator to combine text with variables:

    # Create a variable:
    first_name = "Joey"

    # Combine some text with the variable and display it:
    print(name + " is awesome!")


    ######################


    # We can also use the "+" operator to link together variables
    # through "string concatenation":

    # Create two variables:
    first_name = "Joey"
    age = "42"

    # Link the variables together within a message:
    print(first_name + " is " + age + " years young!")


    ######################


    # For numbers, the "+" operator works as a mathematical operator:


    # Define two variables:
    x = 9
    y = 24

    # Display the sum of the variables:
    print(x + y)


    ######################


    # If you try to combine a string and a number, Python will give
    # us an error!


    ######################


    # GLOBAL VARIABLES:


    # Variables that are created outside of a function are "global"
    # variables.

    # Global variables can be used by everyone... both inside
    # as well as outside of unctions:

    # Create a couple variables outside the function:
    first_name = "Joey"
    greeting = "Hi, my name is "

    # Create a function to display the name:
    def display_greeting():
        print(greeting + first_name + "!")

    # Call the function:
    display_greeting()


    ######################


    # Defining a variable within a function makes it "local"
    # to that function. This means that it can only be used (accessed)
    # within the function. Global variables with the same variable
    # name remain unchanged and are accessible everywhere.


    # Define a couple global variables for greeting:
    first_name = "Joey"
    greeting = "Hi there! My name is "

    # Define a function to display the greeting:
    def my_greeting():
        # Define a local variable with the same name:
        first_name = "Badass"
        print(greeting + first_name + "!")

    # Call the my_greeting function:
    my_greeting()

    # Global variable is unchanged:
    print(first_name)


    ######################


    # THE global KEYWORD


    # Normally, when we create a variable inside a function, that variable
    # is local, and can only be used inside a function.

    # To create a global variable within a function, we can use
    # the 'global' keyword.

    # Define a function:
    def greeting_2():
        global alias
        alias = "JoevoL"
        # Access the global variable from the "local" scope
        print("Hello there, " + alias)

    # Call the function:
    greeting_2()

    # Access the global variable from the "global" scope:
    print(alias)









    # PYTHON DATA TYPES


    # BUILT IN DATA TYPES

    # Variables can store data of different types, and different types
    # of data can be used to do different things.

    # Python has the following data types built-in by default:

    # Text Type: str
    # Numeric Types: int, float, complex
    # Sequence Types: list, tupple, range
    # Mapping Type: dict
    # Set Type: dict
    # Boolean Type: bool
    # Binary Types: bytes, bytearray, memoryview


    ###########################


    # GETTING DATA TYPE

    # We can get the data type of any object using the type() function:


    # Define a variable:
    my_num = 7
    # Display the data type of the variable:
    print(type(my_num))


    # SETTING DATA TYPE

    # In Python, the data type is automatically set when we assign
    # a value to the variable:

    # Create a string variable and display it's type:
    my_var = "Hello There!"
    print(type(my_var))

    # Create an integer variable and display it's type:
    my_var = 7
    print(type(my_var))

    # Create a float variable and display it's type:
    my_var = 7.0
    print(type(my_var))

    # Create a complex variable and display it's type:
    my_var = 7j
    print(type(my_var))

    # Create a list variable and display it's type:
    my_var = ["Joey", "Ben", "Hudson"]

    # Create a tuple variable and display it's type:
    my_var = ("Joey", "Ben", "Hudson")
    print(type(my_var))

    # Create a range variable and display it's type:
    my_var = range(7)
    print(type(my_var))

    # Create a dictionary variable and display it's type:
    my_var = {name: "Joey", age: 42}
    print(type(my_var))

    # Create a set variable and display it's type:
    my_var = {"Joey", "Ben", "Hudson"}
    print(type(my_var))

    # Create a frozen-set variable and display it's type:
    my_var = frozenset({"Joey", "Ben", "Hudson"})
    print(type(my_var))

    # Create a boolean variable and display it's type:
    my_var = True
    print(type(my_var))

    # Create a bytes variable and display it's type:
    my_var = b"Hello"
    print(type(my_var))

    # Create a bytearray variable and display it's type:
    my_var = bytearray(7)
    print(type(my_var))

    # Create a memoryview variable and display it's type:
    my_var = memoryview(bytes(7))
    print(type(my_var))


    ###########################


    # SETTING SPECIFIC DATA TYPE

    # Set and display the specific data type:
    my_var = str("Hello There!")
    print(type(my_var))

    my_var = int(7)
    print(type(my_var))

    my_var = float(7.0)
    print(type(my_var))

    my_var = complex(7j)
    print(type(my_var))

    my_var = list(("Joey", "Ben", "Hudson"))
    print(type(my_var))

    my_var = tuple(("Joey", "Ben", "Hudson"))
    print(type(my_var))

    my_var = range(7)
    print(type(my_var))

    my_var = dict(name="Joey", age=42)
    print(type(my_var))

    my_var = set(("Joey", "Ben", "Hudson"))
    print(type(my_var))

    my_var = frozenset(("Joey", "Ben", "Hudson"))
    print(type(my_var))

    my_var = bool(7)
    print(type(my_var))

    my_var = bytes(7)
    print(type(my_var))

    my_var = bytearray(7)
    print(type(my_var))

    my_var = memoryview(bytes(7))
    print(type(my_var))











    # PYTHON NUMBERS

    # Python Numbers

    # There are three numberic types in Python: int, float and complex

    # Variables of numeric types are created when you assign a value
    # to them.

    # Declare same numeric variables:
    my_int = 1       # int
    my_float = 2.2     # float
    my_complex = 7j      # complex

    # We can use the type() function to verify the type of any
    # object in Python:
    print(type(my_int))
    print(type(my_float))
    print(type(my_complex))




    # INT

    # An integer (int) is a whole number, positive or negative, without
    # decimals, of unlimited length.

    # Examples:
    my_int = 1
    my_long_int = 50983457203984
    my_short_int = -198347

    # Display the type of each variable:
    print(type(my_int))
    print(type(my_long_int))
    print(type(my_short_int))




    # FLOAT

    # A floating point number (float) is a number, positive or negative,
    # containing one or more decimals.

    # Examples:
    my_float = 1.10
    my_short_float = 1.0
    my_longer_float = -37.77

    # Display the type of each variable:
    print(type(my_float))
    print(type(my_short_float))
    print(type(my_longer_float))

    # Floatsd can also be scientific numbers with an "e" to
    # indicate the power of 10:

    my_float = 35e3
    my_short_float = 12E4
    my_longer_float = -87.7e100

    # Display the value of each variable:
    print(my_float)
    print(my_short_float)
    print(my_longer_float)




    # COMPLEX

    # Complex numbers are written with a "j" as the imaginary part.

    # Examples:
    x = 3 + 5j
    y = 5j
    z = -5j

    # Display the type of each variable:
    print(x)
    print(type(x))
    print(type(y))
    print(type(z))




    # TYPE CONVERSSION

    # We can convert from type to another with the int(), float() and complex() methods:

    # Examples:
    x = 1
    y = 2.8
    z = 7j

    # Convert from int to float:
    a = float(x)
    print(a)
    print(type(a))

    # Convert from float to int:
    b = int(y)
    print(b)
    print(type(b))

    # Convert from int to complex:
    c = complex(x)
    print(c)
    print(type(c))

    ### We cannot convert complex numbers into another type!




    # RANDOM NUMBER

    # Python does not have a random() function to make a random number,
    # but Python does have a built-in module called "random" that can
    # be used to make random numbers. This module is imported at the
    # beginning of this file!

    # Example:

    # Display a random number between 1 and 9:
    my_random_number = random.randrange(1, 10)
    print(my_random_number)


    #######################################


    # PYTHON CASTING

    # SPECIFY a VARIABLE TYPE:

    # Python is an object oriented programming language, ad as such
    # it uses classes to define data types, including its primitive types.



    # CASTING in Python is done using constructor functions:

    # int() -
    # constructs an integer number from an integer literal,
    # a float literal (by removing all decimals) or a string
    # literal (providing the string represents a whole number).

    # float() -
    # constructs a float number from an integer literal,
    # a float literal or a string literal (providing the string
    # represents a float or an integer).

    # str() -
    # constructs a string from a wide variety of data types,
    # including strings, integer literals and float literals.









    ###########################








# Call the main function:
main()
