"""
author: Anthony Antczak
date: 10/30/2024
An investigation on file input (reading)
"""
#input
#output
#processing

# Remove the quotations around this code to create the necssesary file for this
# investigation (for examples())

with open("input.txt", mode="w") as f_out:
    f_out.write("This is line 1\n")
    f_out.write("This is line 2\n")
    f_out.write("I think CS is fun :)\n")
    f_out.write("But only when I understand it :/\n")

# Remove the quotations around this code to create the necssesary file for this
# investigation (for your TODO)

names = ["Abigale\n", "Brendan\n", "Charlie\n", "Doug\n", "Elsie\n", "Faris\n", "Gayle\n", "Henry\n", "Isabel\n", "Juliette\n"]
with open("names.txt", mode="w") as f_out:
    f_out.writelines(names)


def read_file_as_string(filename: str) -> str:
    """Opens a file for reading and returns the content as a string"""
    with open(filename, mode="r") as f_in:
        file_contents = f_in.read()

    return file_contents

def transform_string(string: str) -> str:
    """Applies a transformation on a string (Reverse sentence case)

    >>> transform_string('Hello folks')
    'hELLO FOLKS'

    >>> transform_string('i wanna BE the bEst')
    'i WANNA BE THE BEST'
    """
    return string[0].lower() + string.upper()[1:]


def examples():
    """Some examples on how we can use a list as input"""
    # This is how you will use file input like 99% of the time
    with open("input.txt", mode="r") as f_in:
        file_contents = f_in.readlines()

    # Let's take a look at the variable
    print("\n\n == Printing file contents with the newline characters! == ")
    print(file_contents)

    # Notice all of the '\n's in the list? That's the new line character!
    # What if we don't want those pesky \n s? Well, we can read the file like this:
    with open("input.txt", mode="r") as f_in:
        file_contents = f_in.read().splitlines()

    print("\n\n == Printing file contents without the newline characters! == ")
    print(file_contents)

    # Boom, now this looks like a normal list we can do list transformations on!

    # Then we can process file_contents
    transformed_contents = []
    for line in file_contents:
        transformed_contents.append(transform_string(line))

    print("\n\n == Printing transformed file contents == ")
    # Now we can output this list however we want
    for line in transformed_contents:
        print(line)


    # We can also just read in the entire file as a string.
    # It looks the same as above, so to show you something new,
    # let's do that using the function defined above
    file_contents = read_file_as_string("input.txt")
    print("\n\n == Printing the file contents as a string! == ")
    print(file_contents)

    # I can perform any string action I want on this string too!
    print("\n\n == Details about the above string! == ")
    print(f"There are {file_contents.count('e')} es in this string!")

def main():
    # TODO: Your code here for names.txt
    pass
    with open("names.txt") as f_in:
        names = f_in.readlines()
    for name in names:
        name = name.translate({ord('\n'): None})
        print(f"Hello {name}!")


if __name__ == "__main__":
    examples()
    main()