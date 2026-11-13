#avg of koala's two favourite numbers
num = int(input("Koala1: "))
nums = int(input("Koala2: "))
# / divides and // divides, but removes remainders or decimals
def avg(num, nums):
    avgs = (num+nums)//2
    return avgs

print(avg(num, nums))