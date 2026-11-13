"""
author: Anthony Antczak
date: 11/27/2024
investigating max_search
"""

def max_search(haystack):
    """Searches for  max index of number
    >>> max_search([1, 2, 3])
    2
    >>> max_search([1, 2, 5, 7])
    3
    """
    max_index = 0
    for i in range(len(haystack)):
        if haystack[i] > haystack[max_index]:
            max_index = i
    return max_index
def main():
    #input
    haystack = [1, 2, 3, 5, 6, 7, 8, 9]
    #processing/output
    print(max_search(haystack))
if __name__ == "__main__":
    main()