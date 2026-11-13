#note: I actually figured this out by myself, only needed help for the range + 1 since i forgot: GGs
dice_1 = int(input("1: "))
dice_2 = int(input("2: "))

#set a count for how many times it equals 10
count = 0
#put a loop in a loop to loop over each other to find every combination which equals to 10 on the dice sides
# add 1 to the dices in the loops since we start at 0, input=5, range 0-4 so + 1 = 0-5
for i in range(dice_1 + 1):
    for j in range(dice_2 + 1):
        if i + j == 10:
            count += 1
#if it equals to 1 it is "way" and many is "ways"
if count == 1:
    print("There is 1 way to get a sum of 10")
else:
    print(f"There are {count} ways to get a sum of 10")