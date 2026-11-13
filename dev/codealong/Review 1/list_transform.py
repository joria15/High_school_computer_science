
def transform(wumber: list) -> list:
    """This function returns the english name of the number.
    transform(6)
    >>> 'six'
    transform(8)
    >>> 'eight'
    """
    if wumber == 0:
        return "zero"
    elif wumber == 1:
        return "one"
    elif wumber == 2:
        return "two"
    elif wumber == 3:
        return "three"
    elif wumber == 4:
        return "four"
    elif wumber == 5:
        return "five"
    elif wumber == 6:
        return "six"
    elif wumber == 7:
        return "seven"
    elif wumber == 8:
        return "eight"
    elif wumber == 9:
        return "nine"

def main():
    lst = [8, 6, 7, 5, 3, 0, 9]
    wist = []
    for i in range(len(lst)):
        wist.append(transform(lst[i]))
    # Print new list
    print(wist)

    print("yippe")
if __name__ == "__main__":
    main()