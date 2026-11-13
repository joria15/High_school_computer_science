"""
author: Anthony Antczak
date: 11/04/2024
LAB Silver
"""
#processing/Output
# This function transforms ONE piece of candy
def transform_candy(candy):  # Don't forget type annotations
    """Transforms candy by three times if three or more is given
    >>> def transform_candy(5):
    15
    >>> def transform_candy(2):
    2
    """
    if candy>=3:
        return candy*3
    else:
        return candy
#input
def main():

    candies = [1, 9, 2, 8, 1, 6, 2, 16, 13, 7, 7, 7]
    print(candies)
    # Your code here
    more_candy = []
    for i in range (len(candies)):
        more_candy.append(transform_candy(candies[i]))
    print(more_candy)
    print(sum(candies))
    print(sum(more_candy))
if __name__ == "__main__":
    main()