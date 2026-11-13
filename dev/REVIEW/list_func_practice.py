"""
author: Anthony Antczak
date: 10/25/2024
REVIEW
"""

def add20(num):  # Don't forget type annotations
    """Calculates the numbers in the list
    >>> add20(6)
    26
    >>> add20(8)
    28
    """
    return num+20
def main():
    # Input
    numbers = [8, 6, 7, 5, 3, 0, 9]
    bigger = []
    # Processing (Your code here)
    for i in range (len(numbers)):
        bigger.append(add20(numbers[i]))
    # Output
    print(bigger)

if __name__ == "__main__":
    main()

