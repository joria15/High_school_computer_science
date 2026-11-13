# 1.2 - De Morgan's Laws - Practice Questions
# Instructions: make a file called de_morgans_law.py to program the questions below. Complete the truth table on a separate sheet of paper. 
# ---

# ## Question 1
# Apply De Morgan's Law to simplify the following expression:

# ```python
#not (x > 10 and y < 5)
# ```

# **Your Answer:**
# ```python
# # Write your simplified expression here:
#(x <= 10 or y >= 5)

# ```

# **Verify with Python:**
# Write code to test that both expressions give the same result for different values of x and y.
x = 5
y = 4

if not (x > 10 and y < 5):
    print("yes")
else: 
    print("no")

if (x <= 10 or y >= 5):
    print("yes")
else: 
    print("no")



# ## Question 2
# A video game checks if a player CANNOT play a level using this condition:

# ```python
player_level = 6
has_power_up = False
if not (player_level >= 5 and has_power_up):
        print("Level locked!")
# ```

# **Part A:** Rewrite this condition using De Morgan's Law to make it more readable.

# ```python
# # Your rewritten condition:
if (player_level < 5 or not(has_power_up)):
    print("Level locked!")
# ```


# **Part B:** Explain in plain English what the new condition means (when is the level locked?).

# **Your explanation:**
#The new condition expresses that if the players level is less than 5 or they do not have a power up,
#then the level is locked to them

# ---

## Question 3: Truth Table
# Complete the truth table for the expression: `not (A or B)`

# | A | B | A OR B | NOT(A OR B) | NOT A | NOT B | (NOT A) AND (NOT B) |
# |---|---|--------|-------------|-------|-------|---------------------|
# | T | T |   T    |      F      |   F   |   F   |        F            |
# | T | F |   T    |      F      |   F   |   T   |        F            |
# | F | T |   T    |      F      |   T   |   F   |        F            |
# | F | F |   F    |      T      |   T   |   T   |        T            |

# **Question:** Which two columns should be identical? Why?

# **Your answer:**
#NOT (A OR B) and (NOT A) AND (NOT B), the reason is that they both express that when both inputs are false
#then its true that the output is going to be false: for an OR statement, both inputs or just
#one input being true will make the output true. These not statements for both will show that when both
#inputs are false, then it is true that the output is going to be false for the original gate

# ---

## Question 4:
# A student wrote this code to check if someone should NOT receive a discount:

# ```python
age = 17
is_student = True
is_senior = False

if not (age < 18 or is_student or age >= 65 or is_senior):
    print("No discount available")
else:
    print("Discount available!")
# ```

# **Part A:** This condition is confusing! Apply De Morgan's Law to rewrite it in a clearer way.

# ```python
# # Your rewritten condition:
if (age >= 18 and not(is_student) and age < 65 and not(is_senior)):
    print("No discount available")
else:
    print("Discount available!")

# ```

# **Part B:** Test your rewritten condition with these cases to verify it works:
# - age=16, is_student=False, is_senior=False → Should print "Discount available!"
# - age=25, is_student=True, is_senior=False → Should print "Discount available!"
# - age=25, is_student=False, is_senior=False → Should print "No discount available"


# **Part C:** Draw a truth table to show all the possible outcomes of this program
# | 18 <= age < 65 | is_student | is_senior | age AND NOT(is_student) AND NOT(is_senior) |Result |           Output           |
# |----------------|------------|-----------|--------------------------------------------|-------|----------------------------|
# |      25        |      F     |    F      |               F                            |   F   |   "No discount available"  |
# |      27        |      T     |    F      |               T                            |   T   |   "Discount available!"    |
# |      30        |      T     |    T      |               T                            |   T   |   "Discount available!"    |
# |      31        |      F     |    T      |               T                            |   T   |   "Discount available!"    |
# |      17        |      F     |    F      |               T                            |   T   |   "Discount available!"    |
# |      16        |      T     |    T      |               T                            |   T   |   "Discount available!"    |
# |      75        |      F     |    T      |               T                            |   T   |   "Discount available!"    |
# |      80        |      T     |    F      |               T                            |   T   |   "Discount available!"    |
# ---

## Question 5: 
# Write a Python program that validates whether a user can post a comment on a website.

# **Requirements:**
# - User must be logged in AND their account must be verified
# - Write a condition that checks if the user CANNOT post (using NOT with AND)
# - Then rewrite it using De Morgan's Law to check the same thing more clearly
# - Test your code with at least 3 different scenarios

# ```python
# Your code here:
logged_in = False
verified = True

if (not(logged_in) and not(verified)):
    print("CANNOT post")
else:
    print("yur")


# ```

# **Test Cases:**

# | is_logged_in | is_verified | Can Post? | Output |
# |--------------|-------------|-----------|--------|
# | True         | True        | True      |   yur    |
# | True         | False       | True      |   yur    |
# | False        | True        | True      |   yur     |
# | False        | False       | False     |   CANNOT post |

# ---

# ## Bonus Challenge! 🌟
# Apply De Morgan's Law twice to simplify this complex expression:
temperature = 26
humidity = 59
# ```python
if not (not (temperature > 25) and not (humidity < 60)):
    print("hot")
else:
    print("meh")

# ```

# **Step 1:** Apply De Morgan's to the outer NOT
(not(not (temperature > 25)) or not(not (humidity < 60)))
# **Step 2:** Simplify the double negatives (NOT NOT = nothing)
(temperature > 25 or humidity < 60)
# **Final simplified expression:**
if (temperature > 25 or humidity < 60):
    print("hot")
else:
    print("meh")