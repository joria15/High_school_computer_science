"""
author: Anthony Antczak
date: 10/22/2024
A function investigation
"""

# All functions are called (invoked) below


# This is an example of a simple function.
def print_directions() -> None:
    """Prints the directions to get to Mr. Habib's mansion."""
    print("Turn left")
    print("Drive straight")
    print("Arrive @ destination")


# This is an example of a function with one parameter
def say_hello(name: str) -> None:
    """Print a personalized greeting."""
    print(f"Hello {name}! Nice to meet you!")


# This is an example of a function with two parameters
def personal_info(name: str, age: int) -> None:
    """Print the personal information of an individual"""
    print(f"Your name is {name} and you are {age} years old")


# This is an example of a function that returns a value
# This function also has two parameters
def add(a: int , b: int) -> int:
    """Calcluates the sum of two numbers

    >>> add(1, 2)
    3
    >>> add(-3, 1)
    -2
    """
    return a + b


# This function does some more calculations, but same as the one above
# Takes in two parameters and returns a value
# For contxet, gcd = Greatest Common Divisor
def gcd(a: int, b: int) -> int:
    """Calculates the greatest common divisor between two numbers.

    The greatest common divisor is defined as the largest number that `evenly divides`
    the two numbers in question.

    >>> gcd(15, 5)
    5
    >>> gcd(10, 21)
    1
    """
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd


# Finally, this function determines whether or not an ISBN is valid
def is_valid(isbn: str) -> bool:
    """Determines whether or not an ISBN is valid."""
    # Step 1: Get rid of every non numberic character in the string (the dashes)
    isbn_numbers_only = []
    for number in isbn:
        if number.isnumeric():
            isbn_numbers_only.append(int(number))

    # Step 2: Deterimine the length of the ISBN
    # These are two algorithms: Length 10 and Length 13
    if len(isbn_numbers_only) == 10:
        # Multiply each number by it's position and sum
        the_sum = 0
        for i in range(len(isbn_numbers_only)):
            the_sum += isbn_numbers_only[i] * (i + 1)

        # ISBN is valid if the sum is divisible by 11
        return the_sum % 11 == 0

    elif len(isbn_numbers_only) == 13:
        # Multiply each number by 3 if even and 1 if odd
        the_sum = 0
        for i in range(len(isbn_numbers_only)):
            if (i + len(isbn_numbers_only)) % 2 == 0:
                the_sum += isbn_numbers_only[i] * 3
            else:
                the_sum += isbn_numbers_only[i] * 1

        # ISBN is valid if this sum is divisible by 10
        return the_sum % 10 == 0
    else:
        # Not a valid ISBN
        return False

# TODO: Write two functions that compute the area and perimeter
# of a rectangle. Both functions should have two parameters (length, width)
# Call the first function calculate_area, and the second function calculate_perimeter
# Be sure to include proper function documentation and docstrings

def calculate_perimeter(length: int, width: int) -> int:
    """calculates the perimeter of rectangle
    >>> calculate_perimeter(2, 5)
    14
    >>> calculate_perimeter(5,4)
    18
    """
    return 2*width + 2*length

def calculate_area(length: int, width: int) -> int:
    """calculates the area of rectangle
    >>> calculate_area(2, 5)
    10
    >>> calculate_area(5,4)
    20
    """
    return width*length



def main():
    # Input
    name = "Mr. Habib"
    age = 27

    # Processing

    # Calling all the functions in the main method
    print_directions()

    # Calling functions that have parameters with arguments
    # Parameters are the variables in the `function definition`
    # Arguments are the data passed INTO the function. This creates
    # a hidden variable
    # In say_hello(name), name is a parameter
    # in say_hello("Mr. Habib"), "Mr. Habib" is an argument.
    # Python makes the variable name = "Mr. Habib" automatically when we
    # call the say_hello function.
    say_hello(name)
    personal_info(name, age)

    # Calling functions that return values
    # Notice that functions that return values, unlike the function calls above
    # are set equal to a variable! That's important!
    the_sum = add(10, 17)
    the_gcd = gcd(60, 15)

    # Different return values based off of length of ISBN
    is_valid_isbn1 = is_valid("0-7167-0344-0")
    is_valid_isbn2 = is_valid("978-0-7167-0344-0")
    is_valid_isbn3 = is_valid("978-0-7167-4-0")

    # Output
    print(the_sum)
    print(the_gcd)
    print(is_valid_isbn1)
    print(is_valid_isbn2)
    print(is_valid_isbn3)

    # TODO: Call your area and perimeter methods here
calculate_perimeter(3, 5)

calculate_area(2, 4)


if __name__ == "__main__":
    main()