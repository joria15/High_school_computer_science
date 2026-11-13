# 3.3 - Exercise
# ---
# Note: don't forget docstrings, type annotation, and comments


# ### Problem 1
# Create an `Employee` parent class and `Manager` and `Developer` child classes.


# **Employee Class (parent):**
# - **Attributes:** `name`, `employee_id`, `_salary` (private)
# - **Methods:**
#   - `__init__(name, employee_id, salary)` - initialize employee
#   - `get_salary()` - return the salary
#   - `get_annual_bonus()` - return 5% of salary as bonus
#   - `__str__()` - return "Name (ID: ###) - Salary: $XX"


class Employee:
    def __init__(self, name: str, employee_id: str, salary: int) -> None:
        self.name = name
        self.employeed_id = employee_id
        self._salary = salary
   
    def __str__(self) -> str:
        return f"Name: {self.name} (ID: {self.employeed_id}) - Salary: ${self._salary}"


    def get_salary(self) -> str:
      return  f"Salary: %{self._salary}"
   
    def get_annual_bonus(self) -> str:
      return f"Annual bonus for employee: {self._salary * 0.05}"


# **Manager Class (child):**
# - **Attributes:** `name`, `employee_id`, `_salary`, `team_size`
# - **Methods:**
#   - `__init__(name, employee_id, salary, team_size)`
#   - `get_annual_bonus()` - override to return 10% of salary (managers get more!)
#   - `__str__()` - return "Name (ID: ###) - Manager of X people - Salary: $XX"


class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size: int) -> None:
        super().__init__(name, employee_id, salary)
        self.team_size = team_size


    def __str__(self) -> str:
        return f"Name: {self.name} (ID: {self.employeed_id}) - Manager of {self.team_size} people -Salary: ${self._salary}"


    def get_annual_bonus(self) -> str:
        return f"Annual bonus for manager: {self._salary * 0.10}"


# **Developer Class (child):**
# - **Attributes:** `name`, `employee_id`, `_salary`, `programming_language`
# - **Methods:**
#   - `__init__(name, employee_id, salary, programming_language)`
#   - `__str__()` - return "Name (ID: ###) - Developer (Language) - Salary: $XX"


class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language) -> None:
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language


    def __str__(self) -> str:
        return f"Name: {self.name} (ID: {self.employeed_id}) - Developer {self.programming_language} -Salary: ${self._salary}"


# **Test your code:**
# ```python
emp = Employee("Alice", "E001", 50000)
mgr = Manager("Bob", "M001", 70000, 5)
dev = Developer("Charlie", "D001", 60000, "Python")


print(emp.get_annual_bonus())  # 2500.00
print(mgr.get_annual_bonus())  # 7000.00
print(dev.get_annual_bonus())  # 3000.00


print(emp)  # Alice (ID: E001) - Salary: $50000
print(mgr)  # Bob (ID: M001) - Manager of 5 people - Salary: $70000
print(dev)  # Charlie (ID: D001) - Developer (Python) - Salary: $60000
# ```


# ---


# ### Problem 2: Shape Hierarchy
# Create a `Shape` parent class with `Circle` and `Rectangle` child classes.


# **Shape Class (parent):**
# - **Attributes:** `_colour` (private)
# - **Methods:**
#   - `__init__(colour)` - initialize with colour
#   - `get_colour()` - return the colour
#   - `area()` - return 0 (placeholder, to be overridden)
#   - `__str__()` - return "Shape (Colour)"


class Shape:
    def __init__(self, colour: str) -> None:
        self._colour = colour


    def __str__(self) -> str:
        return f"Shape: {self._colour}"
   
    def area(self) -> str:
        return 0
   
    def get_colour(self):
        return self._colour


# **Circle Class (child):**
# - **Attributes:** `_colour`, `_radius` (private)
# - **Methods:**
#   - `__init__(colour, radius)`
#   - `area()` - override to return π × r²
#   - `__str__()` - return "Circle (Colour) - Radius: X"


class Circle(Shape):
    def __init__(self, colour, radius: int):
        super().__init__(colour)
        self._radius = radius
   
    def __str__(self):
        return f"Circle {self._colour} - Radius: {self._radius}"
   
    def area(self) -> int:
        return 3.14 * (self._radius ** 2)
   
# **Rectangle Class (child):**
# - **Attributes:** `_colour`, `_width` (private), `_height` (private)
# - **Methods:**
#   - `__init__(colour, length, width)` - use `super()`
#   - `area()` - override to return length × width
#   - `__str__()` - return "Rectangle (colour) - Length: W, Width: w"


class Rectangle(Shape):
    def __init__(self, colour, height: int,  width: int) -> None:
        super().__init__(colour)
        self._width = width
        self._height = height
   
    def __str__(self) -> str:
        return f"Rectangle {self._colour} - Length: {self._height}, Width: {self._width}"
   
    def area(self) -> int:
        return self._width * self._height


# **Test your code:**
# ```python
circle = Circle("Red", 5)
rect = Rectangle("Blue", 4, 6)


print(circle.area())  # 78.53981633974483
print(rect.area())    # 24


print(circle)  # Circle (Red) - Radius: 5
print(rect)    # Rectangle (Blue) - Length: 4, Width: 6
# ```


# ---


# ### Problem 3: Bank Account Hierarchy
# Create a `BankAccount` parent class with `SavingsAccount` and `CheckingAccount` children.


# **BankAccount Class (parent):**
# - **Attributes:** `account_holder`, `_balance` (private)
# - **Methods:**
#   - `__init__(account_holder, initial_balance)`
#   - `deposit(amount)` - add to balance
#   - `withdraw(amount)` - subtract from balance (if sufficient funds)
#   - `get_balance()` - return balance
#   - `get_interest_rate()` - return interest rate (0% for base account)
#   - `__str__()` - return "Account: Holder - Balance: $XX"


class BankAccount:
    def __init__(self, account_holder: str, initial_balance: int) -> None:
        self.account_holder = account_holder
        self._balance = initial_balance
   
    def __str__(self) -> str:
        return f"Account: {self.account_holder} - Balance: ${self._balance}"


    def deposit(self, amount) -> None:
        self._balance += amount
   
    def widthdraw(self, amount) -> None | str:
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Must be withing your balance range")
   
    def get_balance(self) -> str:
        return self._balance
   
    def get_interest_rate(self) -> str:
        return "0%"


# **SavingsAccount Class (child):**
# - **Attributes:** `account_holder`, `_balance`, `_interest_rate` = 2%
# - **Methods:**
#   - `__init__(account_holder, initial_balance)`
#   - `get_interest_rate()` - override to return 2%
#   - `apply_interest()` - add interest to balance
#   - `withdraw(amount)` - override to charge $5 fee if balance < $100 after withdrawal
#   - `__str__()` - return "Savings Account: Holder - Balance: $XX - Interest Rate: 2%"


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance):
        super().__init__(account_holder, initial_balance)
   
    def __str__(self) -> str:
        return f"Savings Account: {self.account_holder} - Balance: ${self._balance} - Interest Rate: 2%"


    def get_interest_rate(self) -> int:
        return "2%"
   
    def apply_interest(self) -> None:
        self._balance += (self._balance * (0.02))
   
    def withdraw(self, amount) -> None:

        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Must be withing your balance range")

        if self._balance < 100:
            self._balance -= 5
            print("5$ fee for having under 100$")
   
# **CheckingAccount Class (child):**
# - **Attributes:** `account_holder`, `_balance`, `_checks_written` = 0 (private)
# - **Methods:**
#   - `__init__(account_holder, initial_balance)`
#   - `write_check(amount)` - withdraw money and increment check count
#   - `get_checks_written()` - return number of checks written
#   - `__str__()` - return "Checking Account: Holder - Balance: $XX - Checks: X"


class CheckingAccount(BankAccount):
    def __init__(self, account_holder, initial_balance) -> None:
        super().__init__(account_holder, initial_balance)
        self._checks_written = 0


    def __str__(self) -> str:
        return f"Checking Account: {self.account_holder} - Balance: ${self._balance} - Checks: {self._checks_written}"
   
    def write_check(self, amount) -> str:
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Must be withing your balance range")


        self._checks_written += 1
   
    def get_checks_written(self) -> str:
        return self._checks_written


# **Test your code:**
# ```python
savings = SavingsAccount("Alice", 1000)
checking = CheckingAccount("Bob", 500)


savings.deposit(200)
print(savings.get_balance())  # 1200


savings.apply_interest()
print(savings.get_balance())  # 1224 (1200 * 1.02)


checking.write_check(100)
print(checking.get_balance())  # 400
print(checking.get_checks_written())  # 1


savings.withdraw(150)
print(savings.get_balance())  # 1074 (1224 - 150, no fee)
# ```


# ---


# ### Problem 4: Video Game Character Hierarchy
# Create a `Character` parent class with `Warrior`, `Mage`, and `Archer` children.


# **Character Class (parent):**
# - **Attributes:** `name`, `_health`, `_experience`
# - **Methods:**
#   - `__init__(name, health)` - initialize with name and health, experience = 0
#   - `take_damage(damage)` - reduce health by damage amount
#   - `heal(amount)` - increase health, check amount does not go over the initial health
#   - `gain_experience(exp)` - add to experience
#   - `get_level()` - return level (hint: experience // 100 + 1)
#   - `get_health()` - return the character's health
#   - `special_ability()` - return generic ability message
#   - `__str__()` - return "Name - Health: X/Y - Level: Z"

class Character:
    def __init__(self, name: str, health: int, experience: int = 0) -> None:
        self.name = name
        self._health = health
        self._experience = experience
        
    
    def __str__(self) -> str:
        return f"{self.name} - Health: {self._health} - Level: {self.get_level()}"
    
    def get_level(self) -> int:
        return (self._experience // 100 + 1)
    
    def get_health(self) -> int:
        return self._health
    
    def gain_experience(self, exp: int) -> None:
        self._experience += exp
    
    def heal(self, amount: int) -> None:
        self._health += amount
    
    def take_damage(self, damage: int) -> None:
        self._health -= damage
    
    def special_ability(self) -> str:
        return "eternus baby monster has been activated"
    
    
# **Warrior Class (child):**
# - **Attributes:** `name`, `_health`, `_experience`, `_armor`
# - **Methods:**
#   - `__init__(name, health, armor)` - use `super()`
#   - `take_damage(damage)` - override to reduce damage by armor value
#   - `special_ability()` - override to return "Warrior uses Shield Bash!"
#   - `__str__()` - return parent string plus "Armor: X"

class Warrior(Character):
    def __init__(self, name, health, armor: int) -> None:
        super().__init__(name, health)
        self._armor = armor

    def __str__(self) -> str:
        return f"{self.name} - Health: {self._health} - Level: {self.get_level()} - Armor: {self._armor}"
    
    def take_damage(self, damage: int) -> None:
        self._health += self._armor
        self._health -= damage

        if self._health > 100:
            self._health = 100
        
    
    def special_ability(self) -> str:
        return "Warrior uses Shield Bash!"


# **Mage Class (child):**
# - **Attributes:** `name`, `_health`, `_experience`, `_mana`
# - **Methods:**
#   - `__init__(name, health, mana)` - use `super()`
#   - `cast_spell(mana_cost)` - use mana (check if enough available)
#   - `special_ability()` - override to return "Mage casts Fireball!"
#   - `__str__()` - return parent string plus "Mana: X"

class Mage(Character):
    def __init__(self, name, health, mana: int) -> None:
        super().__init__(name, health)
        self._mana = mana

    def __str__(self) -> str:
        return f"{self.name} - Health: {self._health} - Level: {self.get_level()} - Mana: {self._mana}"
    
    def cast_spell(self, mana_cost: int) -> None:
        if mana_cost <= self._mana:
            self._mana -= mana_cost
        else:
            print("You need more mana to cast this spell")
    
    def special_ability(self) -> str:
        return "Mage casts Fireball!"

# **Archer Class (child):**
# - **Attributes:** `name`, `_health`, `_experience`, `_arrows`
# - **Methods:**
#   - `__init__(name, health, arrows)` - use `super()`
#   - `shoot(target_name)` - use an arrow, decrease arrows count (check if enough), return attack message
#   - `special_ability()` - override to return "Archer shoots Triple Shot!"
#   - `__str__()` - return parent string plus "Arrows: X"

class Archer(Character):
    def __init__(self, name, health, arrows: int) -> None:
        super().__init__(name, health)
        self._arrows = arrows

    def __str__(self) -> str:
        return f"{self.name} - Health: {self._health} - Level: {self.get_level()} - Arrows: {self._arrows}"
    
    def shoot(self, target_name: str) -> None:
        if self._arrows > 0:
            self._arrows -= 1
            print(f"{target_name} has been shot by an arrow, {self._arrows} left")
        else:
            print ("You need more arrows")
    
    def special_ability(self) -> str:
        return "Archer shoots Triple Shot!"

# **Test your code:**
# ```python
warrior = Warrior("Aragorn", 100, 20)
mage = Mage("Gandalf", 80, 150)
archer = Archer("Legolas", 90, 30)


print(warrior.special_ability())  # Warrior uses Shield Bash!
print(mage.special_ability())     # Mage casts Fireball!
print(archer.special_ability())   # Archer shoots Triple Shot!


warrior.take_damage(15)
print(warrior.get_health())  # 100 (100 - 15 + 20 armor = 105, capped at max 100, took no damage)


warrior.gain_experience(150)
print(warrior.get_level())  # 2


archer.shoot("Goblin")  # Legolas shoots at Goblin! 29 arrows left
# ```


# ---


# ### Problem 5: Music Instrument Polymorphism
# Create an `Instrument` parent class with `Guitar`, `Piano`, and `Violin` children. Use polymorphism with a list.


# **Instrument Class (parent):**
# - **Attributes:** `name`, `brand`
# - **Methods:**
#   - `__init__(name, brand)` - initialize
#   - `play()` - return "Playing the instrument"
#   - `get_tuned()` - return "Instrument is tuned"
#   - `__str__()` - return "Instrument: Brand Name"

class Instrument:
    def __init__(self, name: str, brand: str) -> str:
        self.name = name
        self.brand = brand

    def __str__(self) -> str:
        return f"{self.name}: {self.brand}"

    def get_tuned(self) -> str:
        return f"{self.name} is tuned"
    
    def play(self) -> str:
        return f"Playing the instrument"
        

# **Guitar Class (child):**
# - **Methods:**
#   - `play()` - override to return "Playing guitar: Strummmmm"
#   - `get_tuned()` - override to return "Guitar tuned: EADGBE"

class Guitar(Instrument):
    def __init__(self, name, brand):
        super().__init__(name, brand)
    
    def play(self):
        return "Playing guitar: Strummmm"
    
    def get_tuned(self):
        return "Guitar tuned: EADGBE"

# **Piano Class (child):**
# - **Methods:**
#   - `play()` - override to return "Playing piano: Ding ding ding"
#   - `get_tuned()` - override to return "Piano tuned by professional"

class Piano(Instrument):
    def __init__(self, name, brand):
        super().__init__(name, brand)

    def play(self):
        return "Playing piano: Ding ding ding"
    
    def get_tuned(self):
        return "Piano tuned by professional"

# **Violin Class (child):**
# - **Methods:**
#   - `play()` - override to return "Playing violin: *dramatic music*"
#   - `get_tuned()` - override to return "Violin tuned by ear"

class Violin(Instrument):
    def __init__(self, name, brand):
        super().__init__(name, brand)
    
    def play(self):
        return "Playing violin: *dramatic music*"
    
    def get_tuned(self):
        return "Violin tuned by ear"

# **Functions:**
# Create a `perform_concert(instruments)` function that:
# - Takes a list of Instrument objects
# - Calls `get_tuned()` on each
# - Calls `play()` on each
# - Prints all output

def perform_concert(instruments: list) -> None:
    for gt in instruments:
        print(gt.get_tuned())
    
    for pl in instruments:
        print(pl.play())

# **Test your code by running main():**
# ```python
guitar = Guitar("Guitar", "Fender")
piano = Piano("Piano", "Steinway")
violin = Violin("Violin", "Stradivarius")


instruments = [guitar, piano, violin]
perform_concert(instruments)


# # Output should show tuning and playing for each instrument
# ```

