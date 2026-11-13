"""
author: Anthony Antczak
date: 09/23/2024
Making with conditionals
"""

#input
number_1 = int(input("enter a number: "))

#processing
#output

if 0<=number_1<=49:
    print("Level 0")
elif 50<=number_1<=59:
    print("Level 1")
elif 60<=number_1<=69:
    print("Level 2")
elif 70<=number_1<=79:
    print("Level 3")
else:
    print("Level 4")
