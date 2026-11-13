"""
author: Anthony Antczak
date: 09/08/2025
0.3 - iterations
"""

import random

#exercise 1
#input
num = int(input("enter a factorial: "))

#processing
facto = 1
for i in range(1,num+1):
    facto *= i

#output
print(facto)

#exercise 2
tot = 0
maxy = 0
miny = 100
mark = 0

#input
#processing
for i in range(5):
    while(mark < 0 or mark > 100):
        mark = int(input("enter a mark that is proper '1-100': "))

    mark = int(input("enter a mark and '-1' to stop: "))
    if mark == -1:
        break
    if mark > maxy:
        maxy = mark
    if mark < miny:
        miny = mark
    tot += mark

#output
print(tot/5)
print(maxy)
print(miny)

#exercise 3
#input
num  = int(input("enter a nunmber: "))

#processing
a = 0
b = 1
c = 0

for i in range(num):
    if i == 1:
        print("1")
    c = a + b
    a = b
    b = c

    #output
    print(c)

#exercise 4
#processing
num = ""
lst = []

while True:
    #input
    num = int(input("enter a number or -1 to stop: "))
    if num == -1:
        break
    lst.append(num)

#ouput
print("this is the max number: ", max(lst))
print("this is the min number: ", min(lst))

#exercise 5
#input
y_n = str(input("enter yes or no: "))

#processing
while(y_n == "yes"):
    if y_n == "no":
        break
    num = random.randint(1,100)
    lst = []
    for i in range(1, num):
        if num % i == 0:
            lst.append(i)

    #output
    print(lst)
    #input
    y_n = str(input("enter yes or no: "))

#exercise 6
#input
num = int(input("Enter a positive integer: "))

#processing
original_num = num
count_odd = 0
count_even = 0
seven = 0


while num >= 1:
    digit = num % 10
    if digit == 7:
        seven += 1
    if digit % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    num = num // 10

#output
print(f"In {original_num}:")
print(f"Odd digits: {count_odd}")
print(f"Even digits: {count_even}")
print(f"Seven digits: {seven}")