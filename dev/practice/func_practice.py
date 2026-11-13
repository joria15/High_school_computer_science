"""
author: Anthony Antczak
date: 10/23/2024
A function investigation
"""


def evenly_divides(a: int, b: int) -> bool:
    """Evenly divides a number
    >>> def evently_divides(6,3)
    True

    >>> def evently_divides(3,4)
    False
    """
    if b % a == 0:
        return True
    else:
        return False


def is_prime(n: int) -> bool:
    """Checks if a number is a prime number
    >>> def is_prime(7)
    True

    >>> def is_prime(14)
    False
    """
    if n == 1: return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def main():
    #input
    number = int(input("enter a number: "))
    prime = is_prime
    #processing / output
    if prime == True:
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")

if __name__ == "__main__":
    main()