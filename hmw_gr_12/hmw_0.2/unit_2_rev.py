# Q1. String Processing with Validation
# Write a function called `validate_username(username)` that checks if a username is valid according to these rules:
# - Must be between 5 and 15 characters long
# - Must contain at least one digit
# - Must contain at least one uppercase letter
# - Must contain at least one lowercase letter
# - Must not contain any spaces


# The function should return `True` if valid, `False` otherwise.


# **Example:**
# ```python
# print(validate_username("Hello123"))  # True
# print(validate_username("hello"))     # False (no digit)
# print(validate_username("HELLO123"))  # False (no lowercase)
# print(validate_username("Hi 123"))    # False (has space)
# ```
def validate_username(username):
    if len(username) < 5 or len(username) > 15:
        return False
    if not username.isalnum():
        return False
    if username.isupper() or username.islower():
        return False
    if " " in username:
        return False
    return True
# ---
print(validate_username("Hello123"))  # True
print(validate_username("hello"))     # False (no digit)
print(validate_username("HELLO123"))  # False (no lowercase)
print(validate_username("Hi 123"))    # False (has space)


# ### Q2. Working with 2D Lists and Aliasing
# Write a function called `create_multiplication_table(size)` that creates a 2D list representing a multiplication table of the given size.


# **Requirements:**
# - Each row must be an independent list (no aliasing!)
# - The value at position `[i][j]` should be `(i+1) * (j+1)`
# - Return the completed 2D list


# **Example:**
# ```python
# table = create_multiplication_table(3)
# print(table)
# # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


# # Test that rows are independent
# table[0][0] = 999
# print(table)
# # Output: [[999, 2, 3], [2, 4, 6], [3, 6, 9]]
# # Only the first element changed!
# ```
def create_multiplication_table(size):


    new = []
    for i in range(size):
        holder = []
        for j in range(size):
            holder.append((i+1)*(j+1))
        new.append(holder)
    return new


table = create_multiplication_table(3)
print(table)


# ---


# ### Q3. Dictionary Data Analysis
# Write a function called `analyze_grades(grade_dict)` that takes a dictionary where keys are student names and values are lists of test scores.


# The function should return a NEW dictionary containing:
# - The student's name as the key
# - A tuple as the value containing: `(average, highest_score, lowest_score)`
# - Round the average to 2 decimal places


# **Example:**
# ```python
# students = {
#     "Alice": [85, 92, 88, 90],
#     "Bob": [78, 81, 85],
#     "Charlie": [95, 98, 93, 97, 94]
# }


# result = analyze_grades(students)
# print(result)
# # Output: {
# #     'Alice': (88.75, 92, 85),
# #     'Bob': (81.33, 85, 78),
# #     'Charlie': (95.4, 98, 93)
# # }
# ```
def analyze_grades(grade_dict):
    output = {}
    for keys, values in grade_dict.items():
        avg = sum(values)/len(values)
        maxxed = max(values)
        minnest = min(values)
        output[keys] = (round(avg, 2), maxxed, minnest)
    return output


students = {
    "Alice": [85, 92, 88, 90],
    "Bob": [78, 81, 85],
    "Charlie": [95, 98, 93, 97, 94]
}


result = analyze_grades(students)
print(result)
# ---
# ### Q4. String Mystery
# Analyze this code and answer the questions:


# ```python
def mystery_string_function(text):
    result = ""
    for i in range(len(text)):
        if text[i].isalpha():
            if i % 2 == 0:
                result += text[i].upper()
            else:
                result += text[i].lower()
        else:
            result += text[i]
    return result


output = mystery_string_function("Hello World!")
print(output)
# ```


# **Questions:**
# 1. What will be printed? Show your step-by-step reasoning.
#"HeLlO WoRlD!"
# 2. Describe in words what this function does.
#The function determines wether the text is a word or not, if not the character added.
#On the other hand, if it is a string, if the index number is even it will be capatalized,
#lower case if odd.
# ---
# ### Q5. The Aliasing Bug
# Analyze this code:


# ```python
def create_game_board():
    row = ["_", "_", "_"]
    board = []
   
    for i in range(3):
        board.append(row.copy())
   
    return board

def make_move(board, row, col, symbol):
    board[row][col] = symbol
    return board
# Game play
game = create_game_board()
print("Initial board:", game)

game = make_move(game, 0, 0, "X")
print("After move 1:", game)

game = make_move(game, 1, 1, "O")
print("After move 2:", game)
# ```


# **Questions:**
# 1. What will be printed after each move? Explain why.
# 2. Identify the bug in the code. Which function contains the problem?
# 3. Fix the `create_game_board()` function so that each row is independent.
# 4. Explain how you would test that your fix works properly.


# ---
# ### Q6. Dictionary Data Structure
# Analyze this code:


# ```python
def organize_data(records):
    #fix error []
    if len(records) < 1:
        return {}
    
    categories = {}
   
    for record in records:
        category = record[0]
        value = record[1]
       
        if category in categories:
            categories[category].append(value)
        else:
            categories[category] = [value]
   
    totals = {}
    for cat, values in categories.items():
        tot = sum(values)
        avg = tot/len(values)
        totals[cat] = (tot, avg)
   
    return totals


data = [("A", 10), ("B", 20), ("A", 15), ("C", 30), ("B", 25), ("A", 5)]
result = organize_data(data)
print(result)
# ```


# **Questions:**
# 1. Trace through the code and predict the output. Show the state of `categories` and `totals` dictionaries at key steps.
# 2. Describe what this function does in plain English.
# 3. Modify the function to also return the average value for each category (in addition to the total). Return both pieces of information using a tuple as the dictionary value.
# 4. How would you modify this function to handle empty input (`records = []`) safely?


# ---
# **Q7.** Fix this tuple creation:
# ```python
# my_tuple = (42,)#coma
# ```


# **Q8.** What's wrong with this code?
# ```python
# numbers = (1, 2, 3, 4)
# numbers.append(5) #tuples are immutable, no appending
# ```


# **Q9.** Create a dictionary from these two lists:
# ```python
# keys = ["name", "age", "grade"]
# values = ["Emma", 17, 12]
# dict = {}
# for i in range(len(keys)):
#   dict[keys[i]] = values[i]
# ```


# **Q10.** Write a one-line solution to swap two variables using tuples:
# ```python
# a = 5
# b = 10
# # Your code here
# #swap: a, b = b, a
# ```


# **Q11.** Fix this list copy to avoid aliasing:
# ```python
original = [1, 2, 3, 4, 5]
copy = original.copy()
copy.append(6)
print(copy)
# original should still be [1, 2, 3, 4, 5]
# ```


# **Q12.** What will this code print?
# ```python
# text = "Python123"
# print(text.isalnum())
# True
# ```


# **Q13.** Complete this code to count how many times "an" appears in the sentence:
# ```python
# sentence = "banana and anvil"
# count = sentence.count("an")
# 4 times
# ```


# **Q14.** What is the output?
# ```python
# a = [1, 2, 3]
# b = a
# c = a[:]
# a.append(4)
# print(b)
# print(c)
#[1, 2, 3, 4] and [1, 2, 3]
# ```


# **Q15.** Create a 2x2 grid filled with zeros (no aliasing):
# ```python
# # Your code here
final = []
grid = [0] * 2
for i in range(2):
    final.append(grid.copy())
    #final.append([0] * 2) works
print(final)
# ```


# **Q16.** What will be printed?
# ```python
coords = (5, 10, 15)
x, y, z = coords
print(y)
#10
# ```


# **Q17.** Write code to check if a key "email" exists in a dictionary called `student`:
# ```python
# Your code here
# email = student.get("email", "Nothing available")
# or
# if "email" in student.keys():
#    print("exist")
# else:
# print("non-existant")
# ```


# **Q18.** What is the output?
# ```python
# info = {"name": "Alice", "age": 17}
# print(info.get("grade", "Not found"))
# "Not found" is the output
# ```


# **Q19.** Complete the code to iterate through both keys and values:
# ```python
# scores = {"Alice": 90, "Bob": 85}
# for name, grade in scores.items():
#     print(f"{name}: {grade}")
# ```


# **Q20.** Fix this code to create independent rows in a 3x3 grid:
# ```python
grid = []
row = [0, 0, 0]
# grid = [row] * 3  # This creates aliasing!
for i in range(3):
    grid.append(row[:])
print(grid)
# # Fix it:

