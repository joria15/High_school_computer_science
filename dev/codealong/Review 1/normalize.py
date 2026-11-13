"""
author: Anthony Antczak
date: 01/20/2025
normalizes the number
"""

def normalize(item:int, avg:int) -> int:    
    """This function returns the average of each number
    >>> normalize(6, 3)
    2
    >>> normnalize(8, 2)
    4
    """
    return item/avg

def main():
    #input
    nums = [8, 6, 7, 5, 3, 0, 9, 1, 8, 0, 0, 2, 5, 7, 2, 0, 0, 1]
    wist = []
    # Do list transformation
    #processing
    avg = sum(nums)/len(nums)
    for num in nums:
        wist.append(normalize(num, avg))
    # Print new list
    #output
    print(wist)
if __name__ == "__main__":
    main()