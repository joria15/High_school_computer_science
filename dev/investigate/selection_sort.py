"""
author: Anthony Antczak
date: 12/05/2024
selection Sort
"""

def selection_sort(lst):
    for i in range(len(lst)):
            min_index = i
            for j in range(i, len(lst)):
                 if lst[j] < lst[min_index]:
                    min_index = j
            lst[i], lst[min_index] = lst[min_index], lst[i]
                  

def main():
    #input
    lst = [8, 6, 7, 5, 3, 0, 9]
    #processing
    selection_sort(lst)
    #output
    print(lst)
if __name__ == "__main__":
    main()