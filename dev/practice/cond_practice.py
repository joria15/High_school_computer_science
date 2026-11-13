"""
author: Anthony Antczak
date: 09/20/2024
practicing conditionals
"""

#input

number_1 = int(input("enter a number: "))
number_2 = int(input("enter another number: "))
number_3 = int(input("enter the final number: "))

#processing
#output

if number_1<number_2<number_3:
    print(number_1, number_2, number_3)

elif number_1<number_3<number_2:
    print(number_1, number_3, number_2)

elif number_3<number_2<number_1:
    print(number_3, number_2, number_1)

elif number_2<number_3<number_1:
    print(number_2, number_3, number_1)

elif number_3<number_1<number_2:
    print(number_3, number_1, number_2)

else:
    print(number_2, number_1, number_3)
