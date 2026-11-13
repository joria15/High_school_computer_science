#J1 (Correct)
# n = int(input("spot: "))
# c = int(input("Carts: "))
# p = int(input("seats: "))

# if n <= (c * p):
#     print("Yes")
# else:
#     print("No")

#J2 (Correct)
# d = int(input("donuts starting with: "))
# e = int(input("Events: "))

# for i in range(e):
#     pm = str(input("- to sell or + to add: "))
#     q = int(input("Donut amount associated: "))

#     if pm == "-":
#         d -= q
#     elif pm == "+":
#         d += q
#     else:
#         print("Nope!")
    
# print(d)

#J3 (Correct)
# n = int(input("How many checks: "))
# for i in range(n):
#     multi = ""
#     total = 0
#     checked = ""
#     check = str(input("bar code: "))

#     for j in range(len(check)):

#         if check[j] == "-":
#             multi += "-"

#         elif check[j].isdigit(): 
#             multi += check[j]

#         elif check[j].isalpha():
#             if check[j].isupper():
#                 checked += check[j]

#             if multi:
#                 total += int(multi)
#                 multi = ""

#     if multi:
#         total += int(multi)
#         multi = ""

#     print(checked + str(total))
            
#J4 Day:  1 2 3 4 5 6 7 8  (Correct)
# Data: P S P S S P P S
# n = int(input("days: "))
# bunch = []
# maxxed = 0
# longest_sun = []
# new_bunch = []
# longest = 0

# for i in range(n):
#     type = input("S or P: ")
#     bunch += type.split()

# for j in range(len(bunch)):
#     if bunch[j] == 'P':
#         new_bunch = bunch.copy()
#         new_bunch[j] = 'S'
#     else:
#         new_bunch = bunch.copy()

#     for k in range(len(new_bunch)):
#         if new_bunch[k] == 'S':
#             longest += 1

#         else:
#             if longest > maxxed:
#                 maxxed = longest
#                 longest_sun = new_bunch

#             longest = 0

#     if longest > maxxed:
#         maxxed = longest
#         longest_sun = new_bunch
#     longest = 0

# print(maxxed)
# print(longest_sun)

#J5
# r = int(input("Rows: "))
# c = int(input("Columns: "))
# m = int(input("Max value: "))

# start = 0
# shortest = 0
# path = 10000
# mcount = 1
# grid = []

# for i in range(r):
# #     grid.append(([""] * c).copy())

# for i in range(r):
#   for j in range(c):

#     grid[i][j] = mcount

#     mcount += 1
#     if mcount > m:
#         mcount = 1

# for k in range(r, , -1)
#     if k == r:
#        min
# for k in range(1, r):
    
#     if k == 1:
#         for l in range(c):
#             if l == 0:
#                 place = min(grid[k - 1][l] + grid[k][l], grid[k - 1][l + 1] + grid[k][l]) 
#                 if place < path:
#                     path = place
#                     start = l
#             elif l == c:
#                 place = min(grid[k - 1][l] + grid[k][l], grid[k - 1][k - 1] + grid[k][l]) 
#                 if place < path:
                    
            
#             else:
#                 place = min(grid[k - 1][l] + grid[k][l], grid[k - 1][l - 1] + grid[k][l], grid[k - 1][l + 1] + grid[k][l]) 
#                 if place < path:
#     if l == 0:
#         shortest += min(grid[k + 1][start], grid[k + 1][start + 1])
#     elif l == c:
#         shortest += min(grid[k + 1][start], grid[k + 1][start - 1])
#     else:
#         shortest += min(grid[k + 1][start], grid[k + 1][start - 1], grid[k + 1][start + 1])
        # .find
    # grid = [0] * c
    # mcount = 1

    # for i in range(r):
    # for j in range(c):
        
    #     mcount += 1

    #     if mcount > m:
    #     mcount = 1
        
    #     if r > 0:
    #     shortest = min(grid[c - (r*c) - 1], grid[c - (r*c)], grid[c - (r*c) + 1] )
    #compare with the current shortest by adding back with current and checking the current min

# print(grid)

#do the video way in 1 string and 2d list after

#s1

#s2

# s = input("ch: ")
# c = int(input("num: "))

# placeholder = s * c

# for i in range(len(placeholder)):
#    if i == c:
#     print(placeholder[i - 1])

#  for i in range(c):
#    total += grid[0][i]

#    for j in range(r):
#         if r == 0:
#             smallest = float['inf']
#             carry = {}
#             carry.update(j : grid[j + 1][i], j - 1 : grid[j + 1][i - 1], j + 1 : grid[j + 1][i + 1])

#             for ind, val in carry.items():
#             if val < smallest:
#                 smallest = val
#                 index = ind

#             total += smallest
#             continue
#         #dictionary for index now
#         total += min(grid[r + 1][index], grid[r + 1][index + 1], grid[r + 1][index - 1])

#start from the begging and go one by one,just say the next row min of the corners and specific test case for 
# boundaries and just say if the next row is the last then stop before the next index
#make row by row

#main
r = int(input("Rows: "))
c = int(input("Columns: "))
m = int(input("Max value: "))

mcount = 1
grid = []
temp = []

for i in range(r * c):

    temp.append(mcount)

    #once a column is reach
    if len(temp) == c: 
        grid.append(temp)
        temp = []

    mcount += 1
    if mcount > m:
        mcount = 1
prev_row = grid[0][:]

for i in range(1, r):
    distance = [float('inf')] * c

    for j in range(c):
        for prev in range(max(0, j - 1), min(c, j + 2)):
            distance[j] = min(distance[j], grid[i][j] + prev_row[prev])

    #make a copy of the total accumalated values from the previous rows
    prev_row = distance[:]

print(min(distance))