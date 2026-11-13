"""
author: Anthony Antczak
date: 11/27/2024
investigating linear_search
"""

def linear_search(haystack: list, needle)->int:
    """Searches for index of number
    >>> linear_search([1, 2, 3], 2)
    1
    >>> linear_search([1, 2, 3], 4)
    -1
    """
    
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return i
    return -1

def main():
    #input
    haystack = [1, 2, 3, 5, 6, 7, 8, 9]
    #processing/output
    print(linear_search(haystack, 6))
    print(linear_search(haystack, 4))
if __name__ == "__main__":
    main()