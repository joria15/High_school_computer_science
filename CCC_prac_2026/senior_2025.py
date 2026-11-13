#s1
# A = int(input("Base: "))
# B = int(input("Height: "))
# X = int(input("Base: "))
# Y = int(input("Height: "))

# c1b = A + X
# c1h = max(B, Y)
# param1 = 2 * (c1b + c1h)

# c2b = max(A, X)
# c2h = B + Y
# param2 = 2 * (c2b + c2h)

# print(min(param1, param2))

#s2
s = input("String: ")
c = int(input("index: "))
char = ""
decipher = ""
amount = ""
summed = 0

for i in range(len(s)):
    if s[i].isalpha():
        if char:
            decipher += (char * int(amount))
            amount = ""
        char = s[i]

    if s[i].isnumeric():
        summed += int(s[i])
        amount += s[i]

if char:
    decipher += (char * int(amount))
    amount = ""

if summed > c:
    print(decipher[c])
else:
    left = c % summed
    print(decipher[left - 1])