"""
author: Anthony Antczak
date: 10/09/2024
Iteration Investigation
"""
#input
#processing
#output


name = input("enter a name: ")
print(name)

number_stop = int(input("enter the number to stop at: "))

number = int(input("enter the number to go up by: "))


if number== "one":
    print(1)
elif number == "two":
    print(2)
elif number == "three":
    print(3)
elif number == "four":
    print(4)
elif number == "five":
    print(5)
elif number == "six":
    print(6)
elif number == "seven":
    print(7)
elif number == "eight":
    print(8)
elif number == "nine":
    print(9)
else:
    print(10)

for i in range(0, number_stop, number):
    print(i)



