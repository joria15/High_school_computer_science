# ## Review Questions:
# 1. What does it mean that strings are immutable? Give an example of what you can and cannot do with strings.
# 2. Explain the difference between `word[2:5]` and `word[2:6]`. If word = "Python", what would each slice return?
# 3. What is the difference between iterating through a string using `for letter in word:` versus `for i in range(len(word)):`? When might you prefer one over the other?
# 4. Describe what the `.split()` method does. What does it return, and what is the default separator?
# 5. Explain the difference between `.find()` and the `in` operator when searching for substrings. What does each return?
# 6. What is aliasing? Explain why `list2 = list1` creates an alias rather than a copy.
# 7. Describe two different methods to create an independent copy of a list. Provide code examples for each.
# 8. Explain the difference between `==` and `is` when comparing lists. What does each operator check for?
# 9. When creating a 2D list, why is it dangerous to use code like this: `grid = [row] * 3`? What problem does this create?
# 10. How do you access an element in a 2D list? Explain the notation `grid[row][column]` with an example.
# 11. What are the key differences between tuples and lists? Discuss mutability, syntax, speed, and memory usage.
# 12. Why must a single-element tuple be written as `(5,)` instead of `(5)`? What happens if you forget the comma?
# 13. Explain what tuple unpacking is and provide an example of how it's useful (such as swapping variables).
# 14. When should you use a tuple instead of a list? Provide at least two specific scenarios.
# 15. What are the only two methods available for tuples? Why are there so few compared to lists?
# 16. Explain the structure of a dictionary. What are keys and values, and what restrictions exist for each?
# 17. Why is `dictionary.get(key)` safer than `dictionary[key]` when accessing values? What happens in each case if the key doesn't exist?
# 18. Describe three different ways to iterate through a dictionary. When would you use each method?
# 19. Explain the difference between `.pop()` and `.popitem()` when removing items from a dictionary.
# 20. What does it mean that dictionaries are "insertion-ordered" in Python 3.7+? 

# ## Practice Questions:

# ### Q1. String Processing with Validation
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

# ---

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

# ---
# ### Q4. String Mystery
# Analyze this code and answer the questions:

# ```python
# def mystery_string_function(text):
#     result = ""
#     for i in range(len(text)):
#         if text[i].isalpha():
#             if i % 2 == 0:
#                 result += text[i].upper()
#             else:
#                 result += text[i].lower()
#         else:
#             result += text[i]
#     return result

# output = mystery_string_function("Hello World!")
# print(output)
# ```

# **Questions:**
# 1. What will be printed? Show your step-by-step reasoning.
# 2. Describe in words what this function does.
# 3. Rewrite this function using a more Pythonic approach (you may use enumerate, zip, or a counter variable).

# ---
# ### Q5. The Aliasing Bug
# Analyze this code:

# ```python
# def create_game_board():
#     row = ["_", "_", "_"]
#     board = []
    
#     for i in range(3):
#         board.append(row)
    
#     return board

# def make_move(board, row, col, symbol):
#     board[row][col] = symbol
#     return board

# # Game play
# game = create_game_board()
# print("Initial board:", game)

# game = make_move(game, 0, 0, "X")
# print("After move 1:", game)

# game = make_move(game, 1, 1, "O")
# print("After move 2:", game)
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
# def organize_data(records):
#     categories = {}
    
#     for record in records:
#         category = record[0]
#         value = record[1]
        
#         if category in categories:
#             categories[category].append(value)
#         else:
#             categories[category] = [value]
    
#     totals = {}
#     for cat, values in categories.items():
#         totals[cat] = sum(values)
    
#     return totals

# data = [("A", 10), ("B", 20), ("A", 15), ("C", 30), ("B", 25), ("A", 5)]
# result = organize_data(data)
# print(result)
# ```

# **Questions:**
# 1. Trace through the code and predict the output. Show the state of `categories` and `totals` dictionaries at key steps.
# 2. Describe what this function does in plain English.
# 3. Modify the function to also return the average value for each category (in addition to the total). Return both pieces of information using a tuple as the dictionary value.
# 4. How would you modify this function to handle empty input (`records = []`) safely?

# ---
# **Q7.** Fix this tuple creation:
# ```python
# my_tuple = (42)
# ```

# **Q8.** What's wrong with this code?
# ```python
# numbers = (1, 2, 3, 4)
# numbers.append(5)
# ```

# **Q9.** Create a dictionary from these two lists:
# ```python
# keys = ["name", "age", "grade"]
# values = ["Emma", 17, 12]
# ```

# **Q10.** Write a one-line solution to swap two variables using tuples:
# ```python
# a = 5
# b = 10
# # Your code here
# ```

# **Q11.** Fix this list copy to avoid aliasing:
# ```python
# original = [1, 2, 3, 4, 5]
# copy = original
# copy.append(6)
# # original should still be [1, 2, 3, 4, 5]
# ```

# **Q12.** What will this code print?
# ```python
# text = "Python123"
# print(text.isalnum())
# ```

# **Q13.** Complete this code to count how many times "an" appears in the sentence:
# ```python
# sentence = "banana and anvil"
# count = # Your code here
# ```

# **Q14.** What is the output?
# ```python
# a = [1, 2, 3]
# b = a
# c = a[:]
# a.append(4)
# print(b)
# print(c)
# ```

# **Q15.** Create a 2x2 grid filled with zeros (no aliasing):
# ```python
# # Your code here
# ```

# **Q16.** What will be printed?
# ```python
# coords = (5, 10, 15)
# x, y, z = coords
# print(y)
# ```

# **Q17.** Write code to check if a key "email" exists in a dictionary called `student`:
# ```python
# # Your code here
# ```

# **Q18.** What is the output?
# ```python
# info = {"name": "Alice", "age": 17}
# print(info.get("grade", "Not found"))
# ```

# **Q19.** Complete the code to iterate through both keys and values:
# ```python
# scores = {"Alice": 90, "Bob": 85}
# for _____, _____ in _____:
#     print(f"{_____}: {_____}")
# ```

# **Q20.** Fix this code to create independent rows in a 3x3 grid:
# ```python
# row = [0, 0, 0]
# grid = [row] * 3  # This creates aliasing!
# # Fix it:
# ```