"""
author: Anthony Antczak
date: 09/11/2025
0.5 - Lists Review Exercises
"""

from unittest.mock import patch 

#exercise 1
def exercise_1(x):
    """
    Read 10 integers from the user and store them in a 10-element list.

    Then, Print:
    - Sum of the values
    - Average of the values
    - Highest and lowest values
    - Number of odd and even values

    Arg: None

    Return: None

    Example:
    >>> exercise_1() # user inputs 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    Sum: 55, Average: 5.5, Max: 10, Min: 1, Odd Numbers: 5, Even Numbers: 5
    """
    # your code goes here
    #processing
    odd = 0
    even = 0
    sumer = sum(x)
    avg = sumer/10
    maxy = max(x)
    miny = min(x)
    for c in x:
        if c % 2 == 0:
            even += 1
        else:
            odd += 1
    return f"The sum is {sumer}, the average is {avg}, max: {maxy}, Min: {miny}, odd: {odd}, even: {even}"

x = []

#input
for i in range(10):
    integer = int(input("enter a number: "))
    x.append(integer)

#output
print(x)
print(exercise_1(x))

#exercise 2
def is_descending(lst):
    """
    Checks if the list is in descending order.

    Args:
        lst (List[int]): List of integers.

    Returns:
        bool: True if list is in descending order, False otherwise.

    Example:
    >>> is_descending([5, 4, 3, 2, 1]) 
    True
    >>> is_descending([1, 2, 3]) 
    False
    """
    # your code goes here
    #processing
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            return False
    return True

#output
print(is_descending([5, 4, 3, 2, 1]))
print(is_descending([1, 2, 3]))
print(is_descending([4,2,3,1]))

#exercise 3
def fibonacci(n):
    """
    Generates the first n terms of the Fibonacci sequence.

    Args:
        n (int): Number of terms.

    Returns:
        List[int]: List containing the first n Fibonacci numbers.

    Example:
    >>> fibonacci(5) 
    [0, 1, 1, 2, 3]
    
    """
    # your code goes here
    #processing
    lst = []
    a = 0
    b = 1
    c = 0
    for i in range(n-1):
        lst.append(c)
        c = a + b
        a = b
        b = c
        if len(lst) == 1:
            lst.append(b)
    
    return lst

#output
print(fibonacci(int(input("enter a number: "))))

#exercise 4
def cumulative_sum(lst):
    """
    Returns the cumulative sum of a list.

        Args:
            lst (List[int]): List of integers.

        Returns:
            List[int]: Cumulative sum list.

        Example:
        >>> cumulative_sum([1, 2, 3]) 
        [1, 3, 6]
        """
    # your code goes here
    #processing
    sumer = [0, ]
    for i in range(len(lst)):
        Asum = sumer[i] + lst[i]
        sumer.append(Asum)
    sumer.remove(sumer[0])
    return sumer

#output
print(cumulative_sum([1,2,3]))

#exercise 5
def remove_duplicates(lst):
    """
    Removes duplicate elements from a list.


    Args:
    lst (List[int]): List of integers.


    Returns:
    List[int]: List with unique elements in original order.


    Example:
    >>> remove_duplicates([1, 2, 3, 3, 4, 2, 1, 5])
    [1, 2, 3, 4, 5]
    """
    # your code goes here
    #processing
    no_dup = []
    for i in lst:
        if i not in no_dup:
            no_dup.append(i)
    return no_dup



#output
print("\nRemove Duplicates Tests:")
print(remove_duplicates([1, 2, 3, 3, 4, 2, 1, 5]))  # [1, 2, 3, 4, 5]
print(remove_duplicates([1, 1, 1, 1]))              # [1]
print(remove_duplicates([]))                       # []
print(remove_duplicates([5, 4, 3, 2, 1]))           # [5, 4, 3, 2, 1]


#input
# Test cases, DO NOT TOUCH!
def test_exercise_1_with_input():
    """Simulates user input for exercise_1 and prints the result."""
    test_inputs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    with patch('builtins.input', side_effect=test_inputs):
        exercise_1()

if __name__ == "__main__":
    print("Exercise 1 Test:")
    test_exercise_1_with_input() # Sum: 55, Average: 5.5, Max: 10, Min: 1, Odd Numbers: 5, Even Numbers: 5

    print("\nis_descending Tests")
    print(is_descending([5, 4, 3, 2, 1]))  # True
    print(is_descending([5, 5, 5, 5]))     # True
    print(is_descending([1, 2, 3]))        # False
    print(is_descending([]))              # True


    print("\nFibonacci Tests::")
    print(fibonacci(0))  # []
    print(fibonacci(1))  # [0]
    print(fibonacci(2))  # [0, 1]
    print(fibonacci(7))  # [0, 1, 1, 2, 3, 5, 8]


    print("\nCumulative Sum Tests")
    print(cumulative_sum([1, 2, 3]))       # [1, 3, 6]
    print(cumulative_sum([0, 0, 0]))       # [0, 0, 0]
    print(cumulative_sum([-1, -2, -3]))    # [-1, -3, -6]
    print(cumulative_sum([]))              # []


    print("\nRemove Duplicates Tests:")
    print(remove_duplicates([1, 2, 3, 3, 4, 2, 1, 5]))  # [1, 2, 3, 4, 5]
    print(remove_duplicates([1, 1, 1, 1]))              # [1]
    print(remove_duplicates([]))                       # []
    print(remove_duplicates([5, 4, 3, 2, 1]))           # [5, 4, 3, 2, 1]
