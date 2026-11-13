Burgers = {'1': '461', '2': '431', '3': '420', '4': '0',}
Sides = {'1': '100', '2': '57', '3': '70', '4': '0',}
Drinks = {'1': '130', '2': '160', '3': '118', '4': '0',}
Desserts = {'1': '167', '2': '266', '3': '75', '4': '0',}

def cal_count():
    Burgers_choice = input()
    Sides_choice = input()
    Drinks_choice = input()
    Desserts_choice = input()
    total_cals = (int(Burgers.get(Burgers_choice, 0)) + int(Drinks.get(Drinks_choice, 0)) + int(Sides.get(Sides_choice, 0)) +int(Desserts.get(Desserts_choice, 0)))
    return total_cals

print(cal_count())

#Done