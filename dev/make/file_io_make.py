"""
author: Anthony Antczak
date: 11/12/2024
Length of adventure.txt
"""

#input
#processing
#output

def main():
    with open ("adventure.txt", mode="r") as f_in:
        adventure = f_in.read()
        adventure = adventure.split()
        length = (len(adventure))
    print(length)
    print(adventure)


if __name__ == "__main__":
    main()