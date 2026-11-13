"""
author: Anthony Antczak
date: 11/27/2024
investigating max_search
"""

def min_search(haystack):
    """Searches for  min index of number
    >>> min_search([1, 2, 3])
    0
    >>> min_search([2, 1, 5, 7])
    1
    """
    min_index = 0
    for i in range(len(haystack)):
        if haystack[i] < haystack[min_index]:
            min_index = i
    return min_index
def main():
    #input
    haystack = [1, 2, 3, 5, 6, 7, 8, 9]
    #processing/output
    print(min_search(haystack))
if __name__ == "__main__":
    main()