"""
author: Anthony Antczak
date: 09/03/2025
0.1 - Back to basics
"""

import math

#exercise 1
#1`
#input
def is_prime(n):
    '''
    >>>is_prime(10)
    False

    >>>is_prime(7)
    True

    '''
    for i in range(2,n-1):
        if n%i == 0:
            return False
        else:
            return True
        
#input
#output
print(is_prime(10))

#2 calculate
#processing
def func(x):
    ''' 
    Makes the x-value go through an equation
    >>>func(10)
    9.119
    >>>func(5)
    1.369
    '''

    return (0.08*math.sqrt(x**2-8) + 12)/(x+4)

#input
num = float(input("please enter a number: "))

#output
print(func(num))

#exercise 2
#input
slices = int(input("number of pizzas per child: "))
boxes = int(input("How many boxes of pizza: "))

#processing
pizzas = 12*boxes
got = pizzas//slices
left = pizzas%slices

#output
gotten = (f"Each child got {got} slices and {left} were left")
print(gotten)

#exercise 3
#input
numerator = int(input("enter a numerator: "))
denominator = int(input("enter a denominator: "))

#processing
whole = numerator//denominator
left = numerator%denominator

#output
print("Mixed fraction: ", whole, f"{left}/{denominator}")
print("Improper fraction: ", f"{numerator}/{denominator}")
