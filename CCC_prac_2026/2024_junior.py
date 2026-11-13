# #J1

# R = int(input())
# G = int(input())
# B = int(input())

# C = (3 * R) + (4 * G) + (5 * B)
# print(C)

#J2
# D = int(input())

# for i in range(3):
#     s = int(input())
#     if D > s:
#         D += s
#     else:
#         break
# print(D)

#J3
N = int(input())
scores = [int(input()) for i in range(N)]

scores.sort(reverse=True)
find = scores[2]

print(find, scores.count(find))
print(scores)