#J4 (NO AI)
# M = int(input())

# count = 0
# coordinate = [0, 0]
# saved = [[0, 0]]

# for i in range(M):
#     step = input()

#     if step[0] != "S" or step[0] != "N":

#         if step[0] == "W":
#             for j in range(int(step[1:])):
#                 coordinate[0] = -(j + 1)
#                 if coordinate in saved:
#                     count += 1
#                 saved.append(coordinate[:])

#         else:
#             for j in range(int(step[1:])):
#                 coordinate[0] = (j + 1)
#                 if coordinate in saved:
#                     count += 1
#                 saved.append(coordinate[:])
#     else:
#         if step[0] == "S":
#             for j in range(int(step[1:])):
#                 coordinate[0] = -(j + 1)
#                 if coordinate in saved:
#                     count += 1
#                 saved.append(coordinate[:])

#         else:
#             for j in range(int(step[1:])):
#                 coordinate[0] = (j + 1)
#                 if coordinate in saved:
#                     count += 1
#                 saved.append(coordinate[:])

# print(count)


# #J5/S2 completed (AI to see why my indexing for "Y" replaces or adds in a list and nothing else)
# # N = int(input())
# # L = int(input())
# # Q = int(input())

# # spots = ["N"] * N

# # for i in range(L):
# #     pi, si = input().split()

# #     pi = int(pi)
# #     si = int(si)

# #     start = max(pi - si - 1, 0)
# #     end = min(pi + si, N)

# #     spots[start : end] = "Y" * (end - start)

# # for j in range(Q):
# #     check = int(input())
# #     print(spots[check - 1])

#S1 (DONE)

# A = int(input())
# B = int(input())
# K = int(input())
# T = int(input())

# steps = (B - A) // K

# small = min(abs(B - (K * steps + K)), B - (K * steps))
# maxxed = max(abs(B - (K * steps + K)), B - (K * steps))

# if A == 0 and B == 0:
#     print(0)
# elif T == 1:
#     print(steps + small)
# elif T == 2:
#     print(steps + maxxed)

#S3

N = int(input())
cards = input().split()
factors = []

asum = 0
bsum = sum(cards)
#make one a sum and make the other the card picker so we know the factor of the sum to figure out factor of picker
for i in range(bsum + 1):
    if bsum % i == 0:
        factors.appned(i)
print(factors)