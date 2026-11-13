n = int(input("enter a num: "))

count = 0

for i in range (6):
    b = n - i
    if 0 <= b <=5 and i>=b:
        count += 1
#b must stay inbetween 0-5 fingers, and i has to be bigger than b since b represent the fingers on one hand, and i represents fingers up on the other
#so for example: n=4, 4-1=3 which is b, so on the other hand 3 fingers are up, but on our main hand i, only one is up
#so until we see i become equal to or more than b, b is the lesser side hand and i is to check how many fingers will have the higher end
#and add to count when b is lesser hand and i is the more fingers hand
print(count)
