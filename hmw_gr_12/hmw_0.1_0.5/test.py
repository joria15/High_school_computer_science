num = ""
lst = []

while True:
    num = int(input("enter a number or -1 to stop: "))
    if num == -1:
        break
    lst.append(num)

print("this is the max number: ", max(lst))
print("this is the min number: ", min(lst))