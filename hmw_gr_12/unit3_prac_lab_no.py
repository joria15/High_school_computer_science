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
        return item
   
    def is_full(self) -> bool:
        return len(self._items) >= self._max_capacity
   
    def add_item(self, item: Item) -> bool:
        if self.is_full() == True:
            print("Max capacity")
        else:
            print("Item added")
            self._items.append(item)
            return True
       
    def remove_item(self, item_name: str) -> bool:
        for item in self._items:
            if item.name == item_name:
                self._items.remove(item)
                return True
            
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


    def __str__(self):
        return f"{self.name} - max health: {self.get_max_health()} - Health: {self._health} - Level: {self._level}"


    def __repr__(self):
        return f"Name:{self.name}, max health: {self.get_max_health()}, Health: {self._health}, Level: {self._level}"
   
    def __eq__(self, value):
        return self.name == value.name

    def add_item_to_inventory(self, item: Item) -> bool:
        return self.inventory.add_item(item)
       
    def use_potion(self, potion_name: str) -> bool:
        item = self.inventory.get_item(potion_name)

        if item is None:
            print("Potion not found")
            return False

        if item._item_type != "potion":
            print("Item is not a potion")
            return False
        
        self.inventory.remove_item(potion_name)

        print(f"{self.name} used {potion_name} and healed 20 HP!")
        return True


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


        if self._health > self._max_health:
            self._health = self._max_health
       
    def is_alive(self) -> bool:
        if self._health > 0:
            return True
        else:
            return False
       

class Warrior(Character):
    def __init__(self, name, health, max_health, level, armor: int):
        super().__init__(name, health, max_health, level)
        self._armor = armor


    def __str__(self):
        return f"{self.name} (Level: {self._level}) | HP: {self._health}/{self.get_max_health()} | Armor: {self._armor}"


    def take_damage(self, damage) -> None:
        self._health -= (damage * (self._armor/100))
       
        if self._health < 0:
            self._health = 0


    def power_attack(self) -> str:
        return "HIYAAHHH"
   

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
        return f"{self.name} (Level: {self._level}) | HP: {self._health}/{self.get_max_health()} | Mana: {self._mana} | Max_mana: {self._max_mana}"
 

    def get_mana(self) -> int:
        return self._mana
   
    def cast_spell(self, mana_cost: int) -> int:
        if mana_cost > self._mana:
            print("Not enough mana")
            return False
        else:
            self._mana -= mana_cost
            return True
   
    def restore_mana(self, amount: int) -> None:
        self._mana += amount




        if self._mana > self._max_mana:
            self._mana = self._max_mana


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
        return f"{self.name} (Level: {self._level}) | HP: {self._health}/{self.get_max_health()} | Arrows: {self._arrows}"


    def get_arrows(self) -> int:
        return self._arrows
   
    def shoot_arrow(self) -> bool:
        if self._arrows > 0:
            print("Arrow has been used")
            self._arrows -= 1
            return True
        else:
            print("No arrows")
            return False
   
    def collect_arrows(self, amount: int) -> None:
        if amount + self._max_arrows > self._max_arrows:
            self._arrows = self._max_arrows
            print("cannot exceed max arrows, base is set to max amount of arrows")
        else:
            self._arrows += amount



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
    a.collect_arrows(5)
    print("Arrows after collecting:", a.get_arrows())








    print("\n===== PART 6: INVENTORY AND ITEMS =====")




    potion = Item("Health Potion", 10, "potion")
    elixir = Item("Mana Potion", 15, "potion")
    sword = Item("Iron Sword", 50, "weapon")




    print("\nAdding items to Warrior's inventory:")
    w.inventory.add_item(potion)
    w.inventory.add_item(elixir)
    w.inventory.add_item(sword)




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

if __name__ == "__main__":
    main()


