"""
author: Anthony Antczak
date: 11/20/2025
3.2 - practice
"""


# 3.2 Exercise
# **Note: add docstrings, type annotation, and comments for each problem!**


# ### Problem 1: Movie Class
# Create a `Movie` class with the following requirements:


# **Attributes:**
# - `title` (public) - the movie title
# - `director` (public) - the director's name
# - `_rating` (private) - rating out of 10


# **Methods:**
# - `__init__(title, director, rating)` - initialize the movie
# - `set_rating(rating)` - set the rating (must be between 0 and 10)
# - `get_rating()` - return the rating
# - `is_highly_rated()` - return True if rating >= 8


# **Test your code:**
# ```python
# movie = Movie("Inception", "Christopher Nolan", 9)
# print(movie.get_rating())  # Should print 9
# movie.set_rating(11)  # Should print error message
# print(movie.get_rating())  # Should still be 9
# print(movie.is_highly_rated())  # Should print True
# ```
class Movie:
    def __init__(self, title: str, director: str, rating: str) -> None:
        self.title = title
        self.director = director
        self._rating = rating


    def set_rating(self, rating: int) -> None:
        if rating > 10 or rating < 0:
            print("Cannot be above 10 or below 0 (rating is current rating)")
        else:
            self._rating = rating
            return f"Rating has been changed to: ({rating})"
   
    def get_rating(self) -> str:
        return f"Rating: {self._rating}"
   
    def is_highly_rated(self) -> str:
        return  self._rating >= 8
       
movie = Movie("Inception", "Christopher Nolan", 9)
print(movie.get_rating())  # Should print 9
movie.set_rating(11)  # Should print error message
print(movie.get_rating())  # Should still be 9
print(movie.is_highly_rated())  # Should print True
print("")
# ---


# ### 2: Temperature Class
# Create a `Temperature` class that stores temperature in Celsius but validates the input:


# **Attributes:**
# - `_celsius` (private) - temperature in Celsius


# **Methods:**
# - `__init__(celsius)` - initialize (must be >= -200, default zero)
# - `set_celsius(celsius)` - set temperature with validation
# - `get_celsius()` - return temperature in Celsius
# - `get_fahrenheit()` - return temperature in Fahrenheit (F = C × 9/5 + 32), use the round function to round to the nearest whole number


class Temperature:
    def __init__(self, celsius: int) -> None:
        if celsius < -200:
            print("temperature is less than -200 celsius: default is zero")
            celsius = 0
        else:
            self._celsius = celsius
       
    def set_celsius(self, celsius: int) -> None:
        if celsius < -200:
            print("temperature is less than -200 celsius: nothing has changed")
        else:
            self._celsius = celsius


    def get_celsius(self) -> str:
        return f"Current temperature: {self._celsius} Celsisus"
   
    def get_fahrenheit(self) -> str:
        return f"Current fahrenheit temperature {int((self._celsius*(9/5)) + 32)} fahrenheit"

# **Test your code:**
# ```python
temp = Temperature(25)
print(temp.get_celsius())  # 25
print(temp.get_fahrenheit())  # 77
temp.set_celsius(-300)  # Should print error, set default to 0
print(temp.get_celsius())  # Still 25
print("")
# ```


# ### Problem 3: Product Class with `__str__` and `__repr__`
# Create a `Product` class for an online store:


# **Attributes:**
# - `name` (public) - product name
# - `_price` (private) - price in dollars
# - `_quantity` (private) - quantity in stock


# **Methods:**
# - `__init__(name, price, quantity)` - initialize the product
# - `__str__()` - return user-friendly format: "Product Name - $XX.XX, has X in stock"
# - `__repr__()` - return format: "Product('name', price, quantity)"
# - `get_price()` - return the price
# - `get_quantity()` - return the quantity
# - `restock(amount)` - add to quantity (must be positive)
# - `sell(amount)` - decrease quantity if enough in stock


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self._price = price
        self._quantity = quantity


    def __str__(self) -> str:
        return f"{self.name} - Price: ${round(self._price, 2)}, has {self._quantity} in stock"
   
    def __repr__(self) -> str:
        return f"Product('{self.name}', {self._price}, {self._quantity})"
   
    def get_price(self) -> str:
        return f"Price: ${self._price}"
   
    def get_quantity(self) -> str:
        return f"Stock: {self._quantity}"
   
    def restock(self, amount: int) -> str:
        if amount < 1:
            return "Amount must be positive and above zero"
        else:
            return f"Restocked amount: {self._quantity + amount}"
   
    def sell(self, amount: int) -> str:
        if amount > self._quantity:
            print("Amount of stock to be removed is more than the current stock")
        else:
            self._quantity -= amount
            return f"New stock amount: {self._quantity}"


# **Test your code:**
# ```python
laptop = Product("Laptop", 999.99, 5)
print(laptop)  # Laptop - $999.99, has 5 in stock
print(repr(laptop))  # Product('Laptop', 999.99, 5)
laptop.sell(2)
print(laptop)  # Laptop - $999.99 (3 in stock)
laptop.sell(10)  # Should print error - not enough stock
# ```
# ---


# ### Problem 4: Rectangle Class with Multiple Special Methods
# Create a `Rectangle` class with special methods:


# **Attributes:**
# - `_width` (private) - width of rectangle
# - `_height` (private) - height of rectangle


# **Methods:**
# - `__init__(width, height)` - initialize (both must be positive, default = 1)
# - `__str__()` - return "Rectangle: WxH"
# - `__repr__()` - return "Rectangle(width, height)"
# - `__eq__(other)` - return True if rectangles have same area
# - `get_area()` - return width × height
# - `get_perimeter()` - return 2 × (width + height)

class Rectangle:
    def __init__(self, width: int, height: int):
        if width < 0:
            print("Width cannot be less than zero (base = 1)")
            width = 1
        if height < 0:
            print("Height cannot be less than zero (base = 1)")
            height = 1

        self._width = width
        self._height = height

    def __str__(self) -> str:
        return f"Rectangle: {self._width}X{self._height}"
    
    def __repr__(self) -> str:
        return f"Rectangle({self._width}, {self._height})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return False
        return (self._width * self._height) == (other._height * other._width)

    def get_area(self) -> str:
        return f"Area: {self._width * self._height}"
    
    def get_perimeter(self) -> str:
        return f"Perimeter: {2 * (self._width * self._height)}"

# **Test your code:**
# ```python
rect1 = Rectangle(4, 5)
rect2 = Rectangle(5, 4)
rect3 = Rectangle(2, 10)


print(rect1)  # Rectangle: 4x5
print(rect1.get_area())  # 20
print(rect1.get_perimeter())
print(rect1 == rect2)  # True
print(rect1 == rect3)  # True
print("\n")
# ```


# ### Problem 5: Team and Player
# Create a sports team management system:


# **Player Class:**
# - **Attributes:** `name`, `jersey_number`, `_goals` (private)
# - **Methods:**
#   - `__init__(name, jersey_number)`
#   - `score_goal()` - increment goals by 1
#   - `get_goals()` - return number of goals
#   - `__str__()` - return "Name (#number) - X goals"


# **Team Class:**
# - **Attributes:** `team_name`, `_players` (list of Player objects, private)
# - **Methods:**
#   - `__init__(team_name)` - initialize with empty player list
#   - `add_player(player)` - add a Player object
#   - `remove_player(name)` - remove player by name
#   - `find_player(name)` - return Player object or None
#   - `get_total_goals()` - return sum of all players' goals
#   - `get_top_scorer()` - return Player with most goals
#   - `__str__()` - return "Team: name (X players, Y total goals)"

class Player:
    def __init__(self, name: str, jersey_number: str) -> None:
        self.name = name
        self.jersey_number = jersey_number
        self._goals = 0
    
    def __str__(self) -> str:
        return f"{self.name} - Jersey number: {self.jersey_number} - {self._goals} goals"
    
    def score_goal(self) -> None: 
        self._goals += 1
    
    def get_goals(self) -> int:
        return self._goals
    
class Team:
    def __init__(self, team_name: str) -> None:
        self.team_name = team_name
        self._players = []

    def add_player(self, player) -> None: 
        self._players.append(player)
    
    def remove_player(self, name) -> None:
        self._players.remove(name)

    def __str__(self) -> str:
        return f"{self.team_name}: {len(self._players)} players, {self.get_total_goals()} total goals "
    
    def get_total_goals(self) -> int:
        goal_sum = 0
        for play in self._players:
            goal_sum += play.get_goals()
        return goal_sum
    
    def get_top_scorer(self) -> str:
        top = 0
        top_name = ""
        jersey = 0

        for i in range(len(self._players)):
            if self._players[i].get_goals() > top:
                top = self._players[i].get_goals()
                top_name = self._players[i].name
                jersey = self._players[i].jersey_number
        return f"{top_name} (#{jersey}) - {top}"

# **Test your code:**
# ```python
player1 = Player("Alice", 10)
player2 = Player("Bob", 7)
player3 = Player("Charlie", 9)


team = Team("Toronto FC")
team.add_player(player1)
team.add_player(player2)
team.add_player(player3)


player1.score_goal()
player1.score_goal()
player2.score_goal()
player3.score_goal()
player3.score_goal()
player3.score_goal()


print(team)  # Team: Toronto FC (3 players, 6 total goals)
print(team.get_top_scorer())  # Charlie (#9) - 3 goals
# ```


# ---


# ### CHALLENGE: NO REQUIRED FOR WORK SUBMISSION, BUT EXTRA PRACTICE!
# Extend the Library/Book example from the lesson:


# Add these features:
# 1. **Author Class** with `name` and `birth_year` attributes
# 2. Modify **Book** to contain an Author object (composition!)
# 3. Add **Member Class** with borrowing limits (max 3 books)
# 4. Track due dates (14 days from checkout)
# 5. Calculate late fees ($0.50 per day)
# 6. Add `generate_report()` method to Library showing:
#    - Total books
#    - Checked out books
#    - Available books
#    - Most popular author



