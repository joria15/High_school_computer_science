import random

y_n = str(input("enter yes or no: "))

while(y_n == "yes"):
    if y_n == "no":
        break
    num = random.randint(1,100)
    lst = []
    for i in range(1, num):
        if num % i == 0:
            lst.append(i)
    print(lst)
    y_n = str(input("enter yes or no: "))
    
