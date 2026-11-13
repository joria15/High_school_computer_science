# avg = 0
# count = 0

# while True:
#     try:
#         num = int(input("Enter a number: "))

#         if num == -1:
#             break
#         else:
#             avg += num
#             count += 1

#     except ValueError:
#         print("enter a proper value")

# print(avg//count,"%")

avg = 0
count = 0

while True:
    try:
        temp = int(input("Enter a temperature (celsius): "))

        if temp == str(temp):
            if temp == "Done":
                break
            else:
                continue
        else:
            avg += temp
            count += 1

    except ValueError:
        print("enter a proper value")

print(avg//count,"degrees celsius")