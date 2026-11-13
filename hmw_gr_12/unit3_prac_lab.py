#NOTE: delete comments to see only full code
#when done, add documentation and neaten








# # Unit 3 Practice Lab








# ## Scenario
# You are building a role-playing game (RPG) system. Your game needs different types of characters, each with unique abilities, an inventory system, and equipment. You'll use object-oriented programming principles to create a flexible, maintainable system.








# ---


# ## Part 3: Composition
# Create an `Item` class and an `Inventory` class to demonstrate composition.








# ## Part 4: Enhanced Character with Inventory
# Modify your `Character` class to include an inventory:
# 1. Add an `inventory` attribute of type `Inventory` (composition)
# 2. Update the `__init__` method to create an inventory with capacity 10
# 3. Add these methods:
#    - `add_item_to_inventory(self, item: Item) -> bool`
#    - `use_potion(self, potion_name: str) -> bool`: heals character by 20 HP if potion found in inventory, removes potion after use
# 4. Update the `__str__` method to show inventory item count








# ---




# ### Item Class:
# - **Attributes**:
#   - `name` (str): item name
#   - `_value` (int): item value in gold
#   - `item_type` (str): type of item (e.g., "weapon", "potion", "armor")
# - **Methods**:
#   - `__init__(self, name: str, value: int, item_type: str) -> None`
#   - `get_value(self) -> int`: returns value
#   - `__str__(self) -> str`: returns formatted item description
#   - `__eq__(self, other: object) -> bool`: compares items by name




class Item:
    def __init__(self, name: str, value: int, item_type: str) -> None:
        self.name = name
        self._value = value
        self._item_type = item_type
   
    def __str__(self):
        return f"{self.name} - Value: {self._value} - Item type: {self._item_type}"
   
    def __eq__(self, value):
        return self.name == value.name
   
    def get_value(self) -> int:
        return self._value
       




# ### Inventory Class
# - **Attributes**:
#   - `_items` (list[Item]): list of items
#   - `_max_capacity` (int): maximum number of items
# - **Methods**:
#   - `__init__(self, max_capacity: int) -> None`
#   - `add_item(self, item: Item) -> bool`: adds item if space available, print a message, and returns True if successful
#   - `remove_item(self, item_name: str) -> bool`: removes item by name, print a message, and returns True if found
#   - `get_item(self, item_name: str) -> Item | None`: returns item if found, None otherwise
#   - `get_total_value(self) -> int`: calculates total value of all items
#   - `is_full(self) -> bool`: returns True if inventory is at capacity
#   - `list_items(self) -> None`: prints all items in inventory
#   - `__str__(self) -> str`: returns formatted inventory summary




class Inventory:
    def __init__(self, max_capacity: int) -> None:
        self._items: list[Item] = []


        if max_capacity < 0:
            print("Max capacity is base of '10' ")
            self._max_capacity = 10
        else:
            self._max_capacity = max_capacity
       
    def __str__(self) -> str:
        item = ""
        print(f"Inventory: ({len(self._items)}/{self._max_capacity} slots filled):")
        for ev in self._items:
            item += f"{ev} \n"
   
    def is_full(self) -> bool:
        return len(self._items) > self._max_capacity
   
    def add_item(self, item: Item) -> bool:
        if self.is_full() == True:
            print("Max capacity")
        else:
            print("Item added")
            self._items.append(item)
            return True
       
    def remove_item(self, item_name: str) -> bool:
        if item_name in self._items:
            self._items.remove(item_name)
            return True
        else:
            print("Item not found")
            return False
    def get_item(self, item_name: str) -> Item | None:
        for te in self._items:
            if te.name == item_name:
                return te
        return None
   
    def get_total_value(self) -> int:
        total = 0
        for val in self._items:
            total += val._value
        return total




    def list_items(self) -> None:
        for ev in self._items:
            print(f"{ev.name} - Value: {ev._value} - Type: {ev._item_type}")






# ## Part 1: Basic Character Class
# Create a `Character` class that serves as the base for all game characters.








# ### Requirements:
# 1. **Attributes** (all should be properly encapsulated):
#    - `name` (str): character's name
#    - `_health` (int): current health points
#    - `_max_health` (int): maximum health points
#    - `_level` (int): character level




class Character:
    def __init__(self, name: str, health: int, max_health: int, level: int) -> None:


        self.inventory = Inventory(10)


        if name == "":
            self.name = "Anonymous"
            print("Invalid, base name is set to 'Anonymous' ")
        else:
            self.name = name


        if health <= max_health and health > 0:
            self._health = health
        else:
            self._health = 100
            print("Invalid health, health is set to a base of '100' ")
        if max_health > 0:
            self._max_health = max_health
        else:
            self._max_health = 100
            print("Invalid max health, max health is set to a base of '100' ")
       
        if level > 0:
            self._level = level
        else:
            self._level = 1
            print("Invalid, base level is set to '1' ")








# 2. **Invariants** (document these in the class docstring):
#    - Health must be between 0 and max_health
#    - Max health must be greater than 0
#    - Level must be at least 1
#    - Name cannot be empty








# 3. **Methods**:
#    - `__init__(self, name: str, max_health: int, level: int) -> None`
#      - Validate all invariants
#      - Set default values for invalid inputs (ex., level defaults to 1)
#    - `get_health(self) -> int`: returns current health
#    - `get_max_health(self) -> int`: returns maximum health
#    - `get_level(self) -> int`: returns level
#    - `get_name(self) -> str`: returns name
#    - `take_damage(self, damage: int) -> None`: reduces health (cannot go below 0)
#    - `heal(self, amount: int) -> None`: increases health (cannot exceed max_health)
#    - `is_alive(self) -> bool`: returns True if health > 0
#    - `__str__(self) -> str`: returns a user-friendly string representation
#    - `__repr__(self) -> str`: returns a developer-friendly representation
#    - `__eq__(self, other: object) -> bool`: compares characters by name








    def __str__(self):
        return f"{self.name} - max health: {self.get_max_health} - Health: {self._health} - Level: {self._level}"




    def __repr__(self):
        return f"Name:{self.name}, max health: {self.get_max_health}, Health: {self._health}, Level: {self._level}"
   
    def __eq__(self, value):
        return self.name == value.name


# 3. Add these methods:
#    - `add_item_to_inventory(self, item: Item) -> bool`
#    - `use_potion(self, potion_name: str) -> bool`: heals character by 20 HP if potion found in inventory, removes potion after use
# 4. Update the `__str__` method to show inventory item count


    def add_item_to_inventory(self, item: Item) -> bool:
        return self.inventory.add_item(item)
       
    def use_potion(self, potion_name: str) -> bool:
        for pn in self.Inventory.self._items:
            if potion_name in pn.name:
                print(f"{pn.name} - Value: {pn.value} - Type: {pn._item_type} has been used")
                return self.remove_item(pn)      
        return False




    def get_health(self) -> int:
        return self._health
   
    def get_max_health(self) -> int:
        return self._max_health
   
    def get_level(self) -> int:
        return self._level
   
    def get_name(self) -> str:
        return self.name
   
    def take_damage(self, damage: int) -> None:
        self._health -= damage


        if self._health < 0:
            self._health = 0


    def heal(self, amount: int) -> None:
        self._health += amount


        if self._health > self.max_health:
            self._health = self._max_health
       
    def is_alive(self) -> bool:
        if self._health > 0:
            return True
        else:
            return False
       








# 4. **Documentation**:
#    - Include a comprehensive class docstring
#    - Add type annotations to all methods
#    - Write docstrings for each method with Args and Returns sections
#    - Include at least one doctest example in your class docstring








# ---








# ## Part 2: Character Inheritance
# Create three child classes that inherit from `Character`: `Warrior`, `Mage`, and `Archer`.








# ### Warrior Class:
# - **Additional Attributes**:
#   - `_armor` (int): armor damage reduction
# - **Invariants**:
#   - Armor must be between 0 and 100
# - **Methods**:
#   - Override `__init__` using `super()` and adding the new attribute
#   - Override `take_damage()`: reduce damage by armor percentage (e.g., 50 armor = 50% damage reduction)
#   - `power_attack(self) -> str`: returns a message about a powerful attack
#   - Override `__str__()` to include armor information








class Warrior(Character):
    def __init__(self, name, health, max_health, level, armor: int):
        super().__init__(name, health, max_health, level)
        self._armor = armor


    def __str__(self):
        return f"{self.name} (Level: {self._level}) | HP: {self._health}/{self.get_max_health} | Armour: {self._armor}"


    def take_damage(self, damage) -> None:
        self._health -= (damage * (self._armor/100))
       
        if self._health < 0:
            self._health = 0


    def power_attack(self) -> str:
        return "HIYAAHHH"
   
# ### Mage Class:
# - **Additional Attributes**:
#   - `_mana` (int): current mana points
#   - `_max_mana` (int): maximum mana points
# - **Invariants**:
#   - Mana must be between 0 and max_mana
#   - Max mana must be greater than 0
# - **Methods**:
#   - Override `__init__` using `super()` and adding the new attributes
#   - `get_mana(self) -> int`: returns current mana
#   - `cast_spell(self, mana_cost: int) -> bool`: uses mana if available, returns True if successful
#   - `restore_mana(self, amount: int) -> None`: restores mana (cannot exceed max_mana)
#   - Override `__str__()` to include mana information








class Mage(Character):
    def __init__(self, name, health, max_health, level, mana: int, max_mana: int):
        super().__init__(name, health, max_health, level)
        if mana > -1 and mana <= max_mana:
            self._mana = mana
        else:
            self._mana = 100
            print("Invalid, base mana is '100' ")
       
        if max_mana > 0:
            self._max_mana = max_mana
        else:
            self._mana = 100
            print("Invalid, base max mana is '100' ")




    def __str__(self) -> str:
        return f"{self.name} (Level: {self._level}) | HP: {self._health}/{self.get_max_health} | Mana: {self._mana} | Max_mana: {self._max_mana}"








    def get_mana(self) -> int:
        return self._mana
   
    def cast_spell(self, mana_cost: int) -> int:
        if mana_cost > self._mana:
            print("Not enough mana")
            return False
        else:
            return True
   
    def restore_mana(self, amount: int) -> None:
        self._mana += amount




        if self._mana > self._max_mana:
            self._mana = self._max_mana




# ### Archer Class:
# - **Additional Attributes**:
#   - `_arrows` (int): number of arrows
# - **Invariants**:
#   - Arrows cannot be negative
# - **Methods**:
#   - Override `__init__` using `super()` and adding the new attribute
#   - `get_arrows(self) -> int`: returns arrow count
#   - `shoot_arrow(self) -> bool`: uses one arrow if available, print a message, and returns True if successful
#   - `collect_arrows(self, amount: int) -> None`: adds arrows, cannot exceed _arrows amount
#   - Override `__str__()` to include arrow count




class Archer(Character):
    def __init__(self, name, health, max_health, level, arrows: int) -> None:
        super().__init__(name, health, max_health, level)
        self._max_arrows = 0
        if arrows < 0:
            self._arrows = 10
            self._max_arrows = 10
            print("Arrows cannot be negative, set base to '10' ")
        else:    
            self._arrows = arrows
            self._max_arrows = arrows
   
    def __str__(self) -> str:
        return f"{self.name} (Level: {self._level}) | HP: {self._health}/{self.get_max_health} | Arrows: {self._arrows}"




    def get_arrows(self) -> int:
        return self._arrows
   
    def shoot_arrow(self) -> bool:
        if self._arrows > 0:
            print("Arrow has been used")
            return True
        else:
            print("No arrows")
            return False
   
    def collect_arrows(self, amount: int) -> None:
        if amount > self._max_arrows:
            self._arrows = self._max_arrows
            print("cannot exceed max arrows, base is set to max amount of arrows")
        else:
            self._arrows += amount




# **Requirements for all child classes**:
# - Use `super().__init__()` to call the parent constructor
# - Include proper documentation with type annotations
# - Validate all invariants in constructors








# ---






# ---






# ## Part 5: Polymorphism Demonstration






# Create a function called `battle_simulation(characters: list[Character]) -> None` that:
# 1. Takes a list of different character types (Warrior, Mage, Archer)
# 2. Uses `isinstance()` to check character types
# 3. Calls appropriate methods based on character type (polymorphism)
# 4. Prints battle information using each character's `__str__` method
# 5. Demonstrates that the same method call (like `take_damage()`) works differently for different character types




def battle_simulation(characters: list[Character]) -> None:
    for character in characters:
        print(character)  # Polymorphism: different __str__ for each type
        character.take_damage(20)  # Polymorphism: Warriors take less damage
       
        if isinstance(character, Warrior):
            print(character.power_attack())
        elif isinstance(character, Mage):
            character.cast_spell(10)
        elif isinstance(character, Archer):
            character.shoot_arrow()
       


# Example structure:
# ```python
# def battle_simulation(characters: list[Character]) -> None:
#     """Simulate a battle with various character types."""
    # for character in characters:
    #     print(character)  # Polymorphism: different __str__ for each type
    #     character.take_damage(20)  # Polymorphism: Warriors take less damage
       
    #     if isinstance(character, Warrior):
    #         print(character.power_attack())
    #     elif isinstance(character, Mage):
    #         character.cast_spell(10)
    #     elif isinstance(character, Archer):
    #         character.shoot_arrow()
# ```




# ---








# ## Part 6: Testing and Main Program








# Create a `main()` function that demonstrates:
# 1. Creating at least one instance of each character type
# 2. Testing all methods of each class
# 3. Adding items to character inventories
# 4. Using potions to heal characters
# 5. Calling your `battle_simulation()` function
# 6. Testing `__eq__` by comparing characters
# 7. Using `isinstance()` and demonstrating polymorphism








# ---
def main():
    print("\n===== PART 1: INSTANCE CREATION =====")
    c = Character("Hero", 100, 100, 1)
    w = Warrior("Conan", 120, 120, 3, 40)
    m = Mage("Merlin", 80, 80, 5, 200, 200)
    a = Archer("Legolas", 90, 90, 2, 10)




    print(c)
    print(w)
    print(m)
    print(a)








    print("\n===== PART 2: TESTING BASIC METHODS =====")




    print("Health before damage:", c.get_health())
    c.take_damage(30)
    print("Health after 30 dmg:", c.get_health())




    c.heal(20)
    print("Health after heal:", c.get_health())




    print("Is alive?", c.is_alive())
    print("String:", str(c))
    print("Repr:", repr(c))








    print("\n===== PART 3: TESTING WARRIOR METHODS =====")




    print("Warrior health:", w.get_health())
    w.take_damage(50)  # armor should reduce this
    print("Warrior health after armored dmg:", w.get_health())
    print(w.power_attack())








    print("\n===== PART 4: TESTING MAGE METHODS =====")




    print("Mana before casting:", m.get_mana())
    success = m.cast_spell(20)
    print("Cast spell (50 mana):", success)
    print("Mana now:", m.get_mana())
    m.restore_mana(30)
    print("Mana after restore:", m.get_mana())








    print("\n===== PART 5: TESTING ARCHER METHODS =====")




    print("Arrows:", a.get_arrows())
    a.shoot_arrow()
    print("Arrows after shooting:", a.get_arrows())
    a.collect_arrow(5)
    print("Arrows after collecting:", a.get_arrows())








    print("\n===== PART 6: INVENTORY AND ITEMS =====")




    potion = Item("Health Potion", 10, "potion")
    elixir = Item("Mana Potion", 15, "potion")
    sword = Item("Iron Sword", 50, "weapon")




    print("\nAdding items to Warrior's inventory:")
    w.add_item(potion)
    w.add_item(elixir)
    w.add_item(sword)




    print("\nListing Warrior inventory:")
    w.inventory.list_items()




    print("\nTotal value:", w.inventory.get_total_value())




    print("\nTesting get_item():")
    print("Get sword:", w.inventory.get_item("Iron Sword"))



    print("\n===== PART 7: USING POTIONS =====")




    print("Health before potion:", w.get_health())
    used = w.use_potion("Health Potion")
    print("Used potion?", used)
    print("Health after potion:", w.get_health())




    print("\nTrying to use potion that doesn't exist:")
    print("Used potion?", w.use_potion("Health Potion"))



    print("\n===== PART 8: TESTING __eq__ =====")


    same_conan = Warrior("Conan", 150, 150, 10, 20)
    print("w == same_conan ?", w == same_conan)   # True (same name)
    print("w == m ?", w == m)                     # False


    print("\n===== PART 9: POLYMORPHISM AND isinstance() =====")




    characters = [c, w, m, a]




    for ch in characters:
        print(f"\nTesting character: {ch.get_name()}")
        print("Is Character?", isinstance(ch, Character))
        print("Is Warrior?", isinstance(ch, Warrior))
        print("Is Mage?", isinstance(ch, Mage))
        print("Is Archer?", isinstance(ch, Archer))




        # polymorphism: each has its own __str__()
        print("Polymorphic __str__:", str(ch))


    print("\n===== PART 10: BATTLE SIMULATION =====")

    battle_simulation(characters)     # or however your function is defined


    print("\n===== ALL TESTS COMPLETE =====")
    # ANSWERS:
        # ===== PART 1: INSTANCE CREATION =====
    # Hero (HP: 100/100, LVL: 1, Inventory: 0 items)
    # Conan (HP: 120/120, LVL: 3, Armor: 40%, Inventory: 0 items)
    # Merlin (HP: 80/80, LVL: 5, Mana: 200/200, Inventory: 0 items)
    # Legolas (HP: 90/90, LVL: 2, Arrows: 10, Inventory: 0 items)




    # ===== PART 2: TESTING BASIC METHODS =====
    # Health before damage: 100
    # Health after 30 dmg: 70
    # Health after heal: 90
    # Is alive? True
    # String: Hero (HP: 90/100, LVL: 1, Inventory: 0 items)
    # Repr: Character(name='Hero', max_health=100, level=1, health=90)




    # ===== PART 3: TESTING WARRIOR METHODS =====
    # Warrior health: 120
    # Warrior takes 50 damage (reduced by 40% armor): 30 damage applied
    # Warrior health after armored dmg: 90
    # Conan performs a POWER ATTACK!




    # ===== PART 4: TESTING MAGE METHODS =====
    # Mana before casting: 200
    # Cast spell (50 mana): True
    # Mana now: 150
    # Mana after restore: 180




    # ===== PART 5: TESTING ARCHER METHODS =====
    # Arrows: 10
    # Legolas shoots an arrow!
    # Arrows after shooting: 9
    # Arrows after collecting: 14




    # ===== PART 6: INVENTORY AND ITEMS =====




    # Adding items to Warrior's inventory:
    # Added Health Potion to inventory.
    # Added Mana Potion to inventory.
    # Added Iron Sword to inventory.




    # Listing Warrior inventory:
    # Inventory:
    #  - Health Potion (potion, value 10)
    #  - Mana Potion (potion, value 15)
    #  - Iron Sword (weapon, value 50)




    # Total value: 75




    # Testing get_item():
    # Get sword: Iron Sword (weapon, value 50)




    # ===== PART 7: USING POTIONS =====
    # Health before potion: 90
    # Used Health Potion on Conan! Healed 20 HP.
    # Used potion? True
    # Health after potion: 110




    # Trying to use potion that doesn't exist:
    # No such potion found.
    # Used potion? False




    # ===== PART 8: TESTING __eq__ =====
    # w == same_conan ? True
    # w == m ? False




    # ===== PART 9: POLYMORPHISM AND isinstance() =====




    # Testing character: Hero
    # Is Character? True
    # Is Warrior? False
    # Is Mage? False
    # Is Archer? False
    # Polymorphic __str__: Hero (HP: 90/100, LVL: 1, Inventory: 0 items)




    # Testing character: Conan
    # Is Character? True
    # Is Warrior? True
    # Is Mage? False
    # Is Archer? False
    # Polymorphic __str__: Conan (HP: 110/120, LVL: 3, Armor: 40%, Inventory: 2 items)




    # Testing character: Merlin
    # Is Character? True
    # Is Warrior? False
    # Is Mage? True
    # Is Archer? False
    # Polymorphic __str__: Merlin (HP: 80/80, LVL: 5, Mana: 180/200, Inventory: 0 items)




    # Testing character: Legolas
    # Is Character? True
    # Is Warrior? False
    # Is Mage? False
    # Is Archer? True
    # Polymorphic __str__: Legolas (HP: 90/90, LVL: 2, Arrows: 14, Inventory: 0 items)


    # ===== PART 10: BATTLE SIMULATION =====
    # Conan battles Merlin!
    # Conan strikes for damage!
    # Merlin casts a spell!
    # ... (your battle messages continue)

    # ===== ALL TESTS COMPLETE =====


if __name__ == "__main__":
    main()


# ## Bonus
# 1. **Level Up System**: Add a `level_up()` method to `Character` that increases level and max_health
# 2. **Critical Hits**: Add a method to Archer that has a 20% chance of critical hit (double damage)
# 3. **Spell System**: Create a `Spell` class and have Mage store a list of learnable spells
# 4. **Equipment System**: Create `Weapon` and `Armor` classes that characters can equip
# 5. **Save/Load System**: Implement methods to save character data to a file and load it back

# ## Example Output


# ```
# === Creating Characters ===
# Sir Galahad (Level 1) | HP: 100/100 | Armor: 50
# Merlin the Wise (Level 1) | HP: 80/80 | Mana: 100/100
# Robin Hood (Level 1) | HP: 90/90 | Arrows: 20



# === Battle Simulation ===
# Sir Galahad takes 20 damage -> HP: 90/100 (armor absorbed 10 damage)
# Merlin casts fireball for 30 mana -> Mana: 70/100
# Robin shoots an arrow -> Arrows: 19/20


# === Inventory System ===
# Robin found a Health Potion!
# Inventory: [Health Potion (50 gold)]
# Robin uses Health Potion -> HP: 90/90 (already at max)
# ```


