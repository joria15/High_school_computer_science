"""
author: Anthony Antczak
date: 09/04/2025
0.2 - Conditionals
"""

import math

#exercise 1
#input
num = int(input("Enter a num: "))

#multiples input
a_1 = int(input("Enter a num: "))
b_2 = int(input("Enter a num: "))
c_3 = int(input("Enter a num: "))

#largest of two inputs
f_1 = int(input("Enter a num: "))
f_2 = int(input("Enter a num: "))

#largest of two inputs
s_1 = int(input("Enter a num: "))
s_2 = int(input("Enter a num: "))
s_3 = int(input("Enter a num: "))

#processing
#output
#even/odd
if num%2 == 0:
    print("This number is even")
else:
    print("This number is odd")
#divisble by 4 or 9
if num % 4 or 9 == 0:
    print("It is divisible by 4 or 9")
else:
    print("This number is not divisble by 4 or 9")
#pos/neg/neither
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
elif num == 0:
    print("neither")
#multiples of each other

#processing
def multiples(a, b, c):
    ''' 
    Gives the number that is the multiple of the other two numbers
    >>>func(3, 6, 9)
    3 is a multiple of the other two
    >>>func(4, 8, 12)
    4 is a multiple of the other two
    '''
       
    if a and b % c == 0:
        return  (f"{c} is a multiple of the other two")
    if a and c % b == 0:
        return  (f"{b} is a multiple of the other two")
    if b and c % a == 0:
        return  (f"{a} is a multiple of the other two")
#output
print(multiples(a_1, b_2, c_3))

#processing
#largest of two
def two_big(a, b):
    ''' 
    Gives the biggest number of two inputs
    >>>two_big(1, 2)
    2
    >>>two_big(5, 6)
    6
    '''

    lst = []
    lst.append(a and b)
    return ("The largest of the two is:", max(lst))

#output
print(two_big(f_1, f_2))

#largest of three
#processing
def three_big(a, b, c):
    ''' 
    Gives the biggest number of three inputs
    >>>three_big(1, 2, 3)
    3
    >>>func(2, 4, 6)
    6
    '''
    lst = []
    lst.append(a and b and c)
    return ("The largest of the three is:", max(lst))
#output
print(three_big(s_1, s_2, s_3))

#exercise 2
#input
a = int(input("enter 'a' value: "))
b = int(input("enter 'b' value: "))
c = int(input("enter 'c' value: "))

#processing
def quadratic(a, b, c):
    ''' 
    Makes three values go through the quadratic formula as the a, b, c values
    >>>func(2, 4, -6)   
    x = 1, x= -3
    >>>func(3, 5, -8)
    x = 1, x = -8/3
    '''

    discriminant = (b**2) + (-4*a*c)
    if discriminant < 0:
        return "there are no solutions, imaginary number"
    if discriminant == 0:
        print("there is only one solution")
    if discriminant > 0:
        print("there are two solutions")
    #rest
    pos = ((-b)+math.sqrt(discriminant))/(2*a)
    neg = ((-b)-math.sqrt(discriminant))/(2*a)
    solution = (f"The solutions are {round(pos, 2)} and {round(neg, 2)}")
    return solution
#output
print(quadratic(a, b, c))

#exercise 3
#input
scones = int(input("Scones sold: "))

#processing
#output
bonus = 0

if 250 >= scones > 150:
    bonus += 10
    bonus += (scones - 150)*0.10
    print(f"The earned bonus is {bonus}$")
elif 350 >= scones > 250:
    bonus += 10
    bonus += (scones - 250)*0.25
    print(f"The earned bonus is {bonus}$")
elif 350 < scones:
    bonus += 10
    bonus += (scones - 350)*0.35
    print(f"The earned bonus is {bonus}$")