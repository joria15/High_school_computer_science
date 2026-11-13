"""
author: Anthony Antczak
date: 12/02/2024
Bubble sorting
"""

def binary_search(haystack: list, needle: int) -> int:
    """Searches for the needle(the number you need to find) and returns index
    >>> binary_search([1, 2, 3, 5, 6, 7, 8, 9], 4)
    -1
    >>> binary_search([1, 2, 3, 5, 6, 7, 8, 9], 6)
    4
    """

    lo = 0
    hi = len(haystack)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if haystack[mid] > needle:
            lo = lo
            hi = mid-1
        elif haystack[mid] < needle:
            lo = mid+1
            hi = hi
        else:  #haystack[mid] == needle
            return mid
    return -1

 



def main():
    #input
    haystack = [1, 2, 3, 5, 6, 7, 8, 9]
    #processing/output
    print(binary_search(haystack, 6))
    print(binary_search(haystack, 4))
if __name__ == "__main__":
    main()