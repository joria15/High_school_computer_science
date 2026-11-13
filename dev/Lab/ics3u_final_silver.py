"""
author: <Your name here>
date: 01/21/2025
Teacher helper
"""
def read_grades(filename: str)->list:
    """this function opens the file
    >>> read_grades(grade.txt)
    ['77\n']
    >>> read_grades(grade.txt)
    ['89\n']
    """
    with open("grades_silver.txt", mode="r") as f_in:
        contents = f_in.readlines()
        return contents
def get_number_of_grades(grades: list) -> int:
    """this function gets the elements of each number of grades
    >>> read_grades(grade.txt)
    30
    >>> read_grades(grade.txt)
    ['89\n']
    """
    return len(grades)

def get_lowest_grade_silver(grades: list) -> int:
    """Docstring here"""
    min_index = 0
    for i in range(len(grades)):
        if grades[i] < grades[min_index]:
            min_index = i
        return grades[min_index]
def get_highest_grade_silver(grades: list) -> int:
    """Docstring here"""
    max_index = 0
    for i in range(len(grades)):
        if grades[i] > grades[max_index]:
            max_index = i
    return grades[max_index]
def get_mid_range(higest_grade: int, lowest_grade: int) -> float:
    """Docstring here"""
    higest_grade = int(higest_grade)
    lowest_grade = int(lowest_grade)
    return (higest_grade+lowest_grade)/2

def main_silver():
    #input
    #processing
    #output
    grades = read_grades("grades_silver.txt")
    print(grades)
    # 50%
    num_grades = get_number_of_grades(grades)
    print(num_grades)  # 30

    # 65%
    lowest_grade = get_lowest_grade_silver(grades)
    print(f"The lowest grade is: {lowest_grade}")  # 27

    # 75%
    highest_grade = get_highest_grade_silver(grades)
    print(f"The highest grade is: {highest_grade}")  # 97

    # 80%
    mid_range = get_mid_range(lowest_grade, highest_grade)
    print(f"The midrange of the grades is {mid_range}")  # 62.0

    # Last 5% Is docstrings and IPO comments


if __name__ == "__main__":
    main_silver()