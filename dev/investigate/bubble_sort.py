"""
author: Anthony Antczak
date: 12/02/2024
Bubble sorting
"""
def bubble_sort (lst):
    """Sorts the list
    >>> bubble_sort([2, 1, 3, 7])
    [7, 3, 2, 1]
    >>> bubble_sort([2, 1, 7, 5])
    [1, 2, 5, 7]
    """
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def main():
    #input
    lst = [8, 6, 7, 5, 3, 0, 9]
    #processing
    bubble_sort(lst)
    #output
    print(lst)
if __name__ == "__main__":
    main()