"""
author: Anthony Antczak
date: 11/07/2024
File input practicing!
"""


def main():
    # Code here
    #input
    L = []
    with open('grades.txt', mode="r") as f_in:
        #processing
        for s in f_in.readlines():  
            L.extend([int(x) for x in s.split(',')])
    a = sum(L)
    b = len(L)
    c = a/b
    #output
    print(c)


if __name__ == "__main__":
    main()