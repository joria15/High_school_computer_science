num = int(input("Enter a positive integer: "))

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

print(f"In {original_num}:")
print(f"Odd digits: {count_odd}")
print(f"Even digits: {count_even}")
print(f"Seven digits: {seven}")