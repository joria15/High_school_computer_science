"""
author: Anthony Antczak
date: 10/24/2024
Making with functions
"""
#processing

def calculate_triangle(num):
    """Calculates the triangle
    >>> calculate_triangle(6)
    21
    """
    for i in range(num):
        num = i+num
    return num    

def calculate_factorial(num):
    """Calculates the factor
    >>> calculate_factorial(3)
    6
    """
    for i in range (num):
        if i == 0:
            i = 1
        num = i*num
    return num


def main():
    #input
    num = int(input("enter a number please to calculate: "))
    nums = int(input("enter a number please to factor: "))
    #output
    print(calculate_triangle(num))
    print(calculate_factorial(nums))
if __name__ == "__main__":
    main()