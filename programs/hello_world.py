
# Define the main function:
def main():

    # Check if you have python installed (in terminal):
    # python --version

    ########################

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

    #########################

    # Indentation:

    if 5 > 2:
        print("Five is greater than two...")

    # Python will give you an error if you skip the indentation.

    # The number of spaces used for indentation is up to the programmer
    # but generally 2 - 4 spaces are used.

    # The same number of spaces must be used within an individual block of code
    # otherwise you'll get an error.

    ##########################

    # Variables:

    # Python variables are created during assignment:

    # Create a variable and display its value:
    x = 5
    print(x)

    name = "Joey"
    print(name)

    #########################

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

    #########################


    # Variable:

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




    # Variables do not need to be declared with any particular type, and
    # the type can be changed after it has been set:

    age = 7 # "age" is of type int (integer)
    print(type(age))

    # Change the type of the variable
    age = "Seven" # "age" is now of type str (string)
    print(type(age))



    # Type Casting:

    # Type casting can be used to specify the data type for a variable:

    my_string = str(3)
    print(type(my_string)) # my_string is of type 'string'

    my_integer = int(3)
    print(type(my_integer)) # my_integer is of type 'integer'

    my_float = float(3)
    print(type(my_float))   # my_float is of type 'float'






    # String variables can be declared using single or double quotes:

    first_name = "Joey"
    # is the same as
    first_name = 'Joey'

    print(first_name)



    # Variable names are case-sensitive:

    my_name = "Joey"
    # is not the same as
    My_Name = "James"

    print(my_name)  # Will display "Joey"
    print(My_Name)  # Will display "James"



    # Variable names can be long or short, but it's helpful for them to
    # be descriptive.



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




    ###########################




# Call the main function:
main()
