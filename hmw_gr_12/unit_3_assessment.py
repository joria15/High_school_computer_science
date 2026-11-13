# ---

# ## PART B: Application Practice Questions

# ### Practice Question 1

# Create a complete `Student` class with the following requirements:

# #### Attributes:
# - `name` (public, string)
# - `student_id` (public, string)
# - `_age` (private, int)
# - `_average` (private, float)

# #### Constructor:
# - Initialize all four attributes
# - Include type annotations and docstring
# - **Invariants:**
#   - `name` must be non-empty, otherwise set to "Unknown"
#   - `student_id` must be non-empty, otherwise set to "000000"
#   - `_age` must be between 14 and 18 inclusive, otherwise set to 14
#   - `_average` must be between 0.0 and 100.0 inclusive, otherwise set to 0.0

# #### Methods:
# - `get_age() -> int`: Return the age
# - `set_average(new_average: float) -> None`: Update average only if between 0.0 and 100.0, otherwise print error
# - `is_honor_roll() -> bool`: Return True if average >= 80, False otherwise

# #### Special Method:
# - `__str__()`: Return "[Name] - ID: [student_id], Age: [age], Average: [average]"

class Student:
    def __init__(self, name: str, student_id: str, age: int, average: float) -> None:
        if name == "" or name == " ":
            self.name = "Unknown"
        else:
            self.name = name
        
        if student_id == "" or student_id == " ":
            self.student_id = "000000"
        else:
            self.student_id = student_id

        if age > 13 and age < 19:
            self._age = age
        else:
            self._age = 14
        
        if average < 0 or average > 100:
            self._average = 0.0
        else:   
            self._average = average
    
    def __str__(self) -> str:
        return f"{self.name} - ID: {self.student_id}, Age: {self._age}, Average: {self._average}"
    
    def get_age(self) -> int:
        return self._age
    
    def set_average(self, new_average: float) -> None:
        self._average = new_average
    
    def is_honor_roll(self) -> bool:
        if self._average >= 80:
            return True
        return False


# #### Example Usage:
# ```python
student = Student("Alice", "12345", 16, 90)
print(student)  # Alice - ID: 12345,  Age: 16, Average: 90
print(student.is_honor_roll())  # True
student.set_average(75)
print(student.is_honor_roll())  # False
print("")
# ```

# ---

# ### Practice Question 2:

# Create a `RestaurantOrder` class with the following requirements:

# #### Attributes:
# - `customer_name` (public, string)
# - `_item` (private, string)
# - `_quantity` (private, int)
# - `_price_per_item` (private, float)

# #### Constructor:
# - Initialize all four attributes
# - Include type annotations and docstring
# - **Invariants:**
#   - `customer_name` must be non-empty, otherwise set to "Guest"
#   - `_item` must be non-empty, otherwise set to "No Item"
#   - `_quantity` must be at least 1, otherwise set to 1
#   - `_price_per_item` must be greater than 0, otherwise set to 1.0

# #### Methods:
# - `get_total() -> float`: Calculate and return quantity × price_per_item x 1.13 (for tax)
# - `set_quantity(new_quantity: int) -> None`: Update quantity only if >= 1, otherwise print error
# - `add_items(amount: int) -> None`: Increase quantity by amount if amount > 0

# #### Special Method:
# - `__str__()`: Return "[customer_name] ordered [quantity] x [item] - Total: $[total]"

class RestaurantOrder:
    def __init__(self, custorname: str, item: str, quantity: int, price_per_item: float) -> None:
        if custorname == "" or custorname == " ":
            self.custorname = "Guest"
        else:
            self.custorname = custorname
        
        if item == "" or item == " ":
            self._item = "No Item"
        else:
            self._item = item

        if quantity < 1:
            self._quantity = 1
        else:
            self._quantity = quantity
        
        if price_per_item > 0:
            self._price_per_item = price_per_item
        else:   
            self._price_per_item = 1.0
    
    def __str__(self) -> str:
        return f"{self.custorname} ordered {self._quantity} x {self._item} - Total: ${self.get_total()}"
    
    def get_total(self) -> float:
        return (self._quantity * self._price_per_item) * 1.13
    
    def set_quantity(self, new_quantity: int) -> None:
        self._quantity = new_quantity
    
    def add_items(self, amount: int) -> None:
        if amount > 0:
            self._quantity += amount

# #### Example Usage:
# ```python
order = RestaurantOrder("John", "Pizza", 2, 12.99)
print(order)  # John ordered 2 x Pizza - Total: $29.36
order.add_items(1)
print(order)  # John ordered 3 x Pizza - Total: $44.04
# ```

# ---

# ## PART D: Thinking Practice Questions

# ### Practice Question 1

# **Scenario:** Analyze the following code for managing courses at a school.

# #### Given Code:

# ```python
class Course:
    """Represents a course with a name, code, and capacity."""
    
    def __init__(self, course_name: str, course_code: str, capacity: int) -> None:
        """Initialize a course."""
        self.course_name = course_name
        self.course_code = course_code
        self._capacity = capacity
    
    def get_capacity(self) -> int:
        """Return the course capacity."""
        return self._capacity
    
    def get_info(self) -> str:
        """Return formatted course information."""
        return f"{self.course_code}: {self.course_name} (Capacity: {self._capacity})"
    
    def __str__(self) -> str:
        """Return string representation."""
        return self.get_info()


class School:
    """Represents a school that contains courses."""
    
    def __init__(self, school_name: str) -> None:
        """Initialize school with a name and empty course list."""
        self.school_name = school_name
        self._courses = []
    
    def add_course(self, course: Course) -> None:
        """Add a course to the school."""
        self._courses.append(course)
    
    def get_total_capacity(self) -> int:
        """Calculate total capacity of all courses."""
        total = 0
        for course in self._courses:
            total += course.get_capacity()
        return total
    
    def display_courses(self) -> None:
        """Display all courses in the school."""
        print(f"{self.school_name} Courses:")
        for course in self._courses:
            print(course)
        print("--------------------------------")
        print(f"Total Capacity: {self.get_total_capacity()}")
# ```

# **a) Identify the Relationship and explain how you know**
# - What type of relationship exists between `School` and `Course`?
# - Explain which line(s) of code demonstrate this relationship.

#1: Course is a composition of school, since a school will have courses
#2: append course and course: Course/course.get_capacity()/print(course)
#The first appends the object memory that is related to Course/Second uses a method from Class Course, where the object is from/
#Print course means it that the object goes to class Course and uses the __str__ method

# **b) Method Analysis:**
# - Trace through the `get_total_capacity()` method. What does it do step-by-step?

#-> Iterate through the self._courses list that has the memory of all the objects from the course class
#-> For the total set to zero, for the object use the get_capcity() method in Course since that is the objects origin and add to total since it returns its capacity
#->return the total capacity from all the courses in the list combined

# - Why does it call `course.get_capacity()` instead of accessing `course._capacity` directly?

#For information hiding, we don't want to directly change the variable, therefore we must use its method to get its info

# #### Part 2: Write the Main Program (4 marks)

# Write a main program that produces this output:

# ```
# Father Michael Goetz Secondary School Courses:
# ICS4U: Computer Science (Capacity: 30)
# SCH4U: Chemistry (Capacity: 28)
# ENG4U: English (Capacity: 32)
# --------------------------------
# Total Capacity: 90
# ```

# **Requirements:**
# 1. Create 3 `Course` objects with the names and capacities shown
# 2. Create a `School` object for "Central High School"
# 3. Add all courses and display the results

# ---
print("")

def main():

    hs = School("Central High School")

    ICS4U = Course("Computer Science", "ICS4U", 30)
    SCH4U = Course("Chemistry", "SCH4U", 28)
    ENG4U = Course("English", "ENG4U", 32)

    hs.add_course(ICS4U)
    hs.add_course(SCH4U)
    hs.add_course(ENG4U)

    hs.display_courses()

if __name__ == "__main__":
    main()

# ### Practice Question 2

# **Scenario:** Analyze the following code for managing a sports team.

# #### Given Code:

# ```python
class Player:
    """Represents a player with name, jersey number, and points."""
    
    def __init__(self, name: str, jersey_number: int, points: int) -> None:
        """Initialize a player."""
        self.name = name
        self.jersey_number = jersey_number
        self._points = points
    
    def get_points(self) -> int:
        """Return the player's points."""
        return self._points
    
    def add_points(self, points: int) -> None:
        """Add points if points > 0."""
        if points > 0:
            self._points += points
    
    def __str__(self) -> str:
        """Return string representation."""
        return f"{self.name} #{self.jersey_number} - {self._points} points"


class Team:
    """Represents a team that contains players."""
    
    def __init__(self, team_name: str) -> None:
        """Initialize team with name and empty player list."""
        self.team_name = team_name
        self._players = []
    
    def add_player(self, player: Player) -> None:
        """Add a player to the team."""
        self._players.append(player)
    
    def get_team_total_points(self) -> int:
        """Calculate total points of all players."""
        total = 0
        for player in self._players:
            total += player.get_points()
        return total
    
    def display_roster(self) -> None:
        """Display all players on the team."""
        print(f"{self.team_name} Roster:")
        for player in self._players:
            print(player)
        print("--------------------------------")
        print(f"Team Total: {self.get_team_total_points()} points")
# ```

# #### Part 1: Code Analysis (6 marks)

# **a) Identify the Relationship:**
# - What type of relationship exists between `Team` and `Player`?
# - Explain which line(s) of code demonstrate this relationship.

# 1. Player is a composition of Team since a team is made up of players
# 2. player: Player, append the player object from the player class to a list/player.get_points() is using a method from the player class in team class
#/print(player) and it prints the str method for the object by going back to the player class which it  originates from

# **b) Method Analysis:**
# - Explain how `get_team_total_points()` calculates the total.

#->>> It iterates through every object in the self._players list and it calls the get_points() method, so the object travels back to the player class
# and it returns the objects points, it adds to a total summing all the points from all the objects

# - Why is encapsulation important here (using `get_points()` instead of direct access

# Because the points attribute is private, therefore we must use the method to return the points

# #### Part 2: Write the Main Program

print("")

def main():

    hs = Team("Raptors Roster")

    rick = Player("Rick", "12", 28)
    dicky = Player("Dicky", "13", 35)
    wick = Player("Wick", "14", 31)
    don = Player("Don", "69", 29)

    hs.add_player(rick)
    hs.add_player(dicky)
    hs.add_player(wick)
    hs.add_player(don)

    hs.display_roster()

if __name__ == "__main__":
    main()

# Write a main program that produces this output:
# ```
# Raptors Roster:
# LeBron James #23 - 28 points
# Stephen Curry #30 - 35 points
# Kevin Durant #7 - 31 points
# Giannis Antetokounmpo #34 - 29 points
# --------------------------------
# Team Total: 123 points
# ```

# **Requirements:**
# 1. Create 4 `Player` objects with the names, numbers, and points shown
# 2. Create a `Team` object for "Raptors"
# 3. Add all players and display the roster


