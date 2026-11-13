def remove_duplicates(lst):
    """
    Removes duplicate elements from a list.

    Args:
    lst (List[int]): List of integers.

    Returns:
    List[int]: List with unique elements in original order.

    Example:
    >>> remove_duplicates([1, 2, 3, 3, 4, 2, 1, 5]) 
    [1, 2, 3, 4, 5]
    """
    # your code goes here
    no_dup = []
    for i in lst:
        if i not in no_dup:
            no_dup.append(i)
    return no_dup


print("\nRemove Duplicates Tests:")
print(remove_duplicates([1, 2, 3, 3, 4, 2, 1, 5]))  # [1, 2, 3, 4, 5]
print(remove_duplicates([1, 1, 1, 1]))              # [1]
print(remove_duplicates([]))                       # []
print(remove_duplicates([5, 4, 3, 2, 1]))           # [5, 4, 3, 2, 1]