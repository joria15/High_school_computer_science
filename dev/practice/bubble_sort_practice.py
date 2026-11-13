"""
author: Anthony Antczak
date: 12/03/2024
Practicing bubble sorting
"""


def bubble_sort (lst):
    """Sorts the list
    >>> bubble_sort(Thomas, White, Aiden])
    [Aiden, Thomas, White]
    """
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def main():
    #input
    with open ("students.txt", mode="r") as f_in:
        students = f_in.read().splitlines()
    #processing
    bubble_sort(students)
    for i in range(len(students)):
    #output
        print(students[i])
if __name__ == "__main__":
    main()