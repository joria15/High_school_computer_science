import math
#explain each part

#pt 1: 
# Read input
start = int(input("1: "))
end = int(input("2: "))

length = end - start + 1
n = math.ceil(math.sqrt(length))
if n % 2 == 0:
    n += 1

grid = [[None for _ in range(n)] for _ in range(n)]

x = y = n//2

#pt 2:

directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

current = start
steps = 1
direc_index = 0

grid[y][x] = current
current += 1

#pt 3: