
# Define the main function:
def main():

    """This is a function docstring...
    Just doing some refreshing and testing...

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








    # Indentation:

    if 5 > 2:
        print("Five is greater than two...")

    # Python will give you an error if you skip the indentation.

    # The number of spaces used for indentation is up to the programmer
    # but generally 2 - 4 spaces are used.

    # The same number of spaces must be used within an individual block of code
    # otherwise you'll get an error.








    # Variables:

    # Python variables are created during assignment:

    # Create a variable and display its value:
    x = 5
    print(x)

    name = "Joey"
    print(name)








    # Comments:

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


    # Type Casting:

    # Type casting can be used to specify the data type for a variable:

    my_string = str(3)
    print(type(my_string)) # my_string is of type 'string'

    my_integer = int(3)
    print(type(my_integer)) # my_integer is of type 'integer'

    my_float = float(3)
    print(type(my_float))   # my_float is of type 'float'


    ######################


    # String variables can be declared using single or double quotes:

    first_name = "Joey"
    # is the same as
    first_name = 'Joey'

    print(first_name)


    ######################


    # Variable names are case-sensitive:

    my_name = "Joey"
    # is not the same as
    My_Name = "James"

    print(my_name)  # Will display "Joey"
    print(My_Name)  # Will display "James"


    # Variable names can be long or short, but it's helpful for them to
    # be descriptive.


    ######################


    # Rules for Python Variables Names:

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


    # Many Values to Multiple Variables

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


    # Assign One Value to Multiple Variables:

    # We can assign the same value to multiple variables in on line:

    name = manager = badass = "Joey"

    # Display the values of each variable:

    print(name)
    print(manager)
    print(badass)


    ######################


    # Collection Unpacking

    # We can extract the values contained within a list, tuple, etc
    # into variables through a process called unpacking

    # Create a list of employees:
    employees = ["John", "James", "Jason"]

    # Unpack the list into variables:
    emp_1, emp_2, emp_3 = employees

    # Display the value of each variable:
    print(emp_1, emp_2, emp_3)


    ######################


    # Output Variables

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


    # Global Variables:


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


    # The global Keyword


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


    # Built-in Data Types

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


    # Getting the Data Type

    # We can get the data type of any object using the type() function:


    # Define a variable:
    my_num = 7
    # Display the data type of the variable:
    print(type(my_num))


    # Setting the Data Type

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


    # Setting the Specific Data Type

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










    ###########################








# Call the main function:
main()
